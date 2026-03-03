#!/usr/bin/env python3
"""
AI Build Loop Coordinator
skills/ai-build-loop/coordinator.py

Enforces the three-actor build loop defined in skills/ai-build-loop/SKILL.md.
The firewall between Writer and Tester is structural — scenarios are never
passed to the Writer API call, only to the Tester.

Usage:
    python3 coordinator.py --brief path/to/brief.md --scenarios path/to/scenarios.md
    python3 coordinator.py --brief path/to/brief.md --scenarios path/to/scenarios.md --output-dir path/to/output/

Exit codes:
    0 — All scenarios passed. Output saved. Human review required before deployment.
    1 — Configuration or input error (missing files, firewall violation).
    2 — Max iterations reached without passing. Escalation report saved.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import anthropic

# ── Constants ──────────────────────────────────────────────────────────────────

MODEL            = "claude-sonnet-4-6"
MAX_ITERATIONS   = 5
MAX_TOKENS_WRITER = 8192
MAX_TOKENS_TESTER = 4096

# Strings that must not appear in the brief.
# Their presence indicates scenarios content has leaked into the Writer's input.
CONTAMINATION_MARKERS = [
    r"firewall: tester-only",
    r"⚠ FIREWALL",
    r"\bTier [12] —",
    r"\bPass signal:",
    r"\bspec_amendment\b",
    r"---SCENARIOS---",
]

WRITER_SYSTEM = (
    "You are the Writer in an AI build loop. "
    "Your only input is the feature brief. "
    "Produce the output artifact exactly as described — for UI features this is a "
    "single self-contained HTML file with all CSS and JavaScript inline. "
    "Do not ask clarifying questions. If anything is ambiguous, make a reasonable "
    "decision and note it in an HTML comment. "
    "Return the raw file content only — no explanation, no markdown fences, no preamble."
)

TESTER_SYSTEM = (
    "You are the Tester in an AI build loop. "
    "You receive the feature brief (intent), acceptance scenarios (rubric), "
    "and the output artifact (what was built). "
    "Evaluate the output against every scenario. "
    "Return ONLY valid JSON — no markdown fences, no prose. "
    "Schema:\n"
    "{\n"
    '  "run": <int>,\n'
    '  "result": "PASS" | "FAIL",\n'
    '  "scenarios": [\n'
    '    { "id": "<id>", "tier": <1|2>, "result": "PASS"|"FAIL", "reason": "<specific observation>" }\n'
    "  ],\n"
    '  "spec_amendment": "<direct addition to brief if FAIL, omit if PASS>"\n'
    "}\n"
    "Do not rationalize past a failure. "
    "spec_amendment must be a concrete constraint the Writer can act on — not a general critique."
)


# ── Utilities ──────────────────────────────────────────────────────────────────

def strip_fences(text: str) -> str:
    """Remove markdown code fences wrapping the entire response."""
    match = re.match(r"^```[a-zA-Z]*\n?(.*?)\n?```\s*$", text.strip(), re.DOTALL)
    return match.group(1).strip() if match else text.strip()


def contamination_check(brief: str) -> list[str]:
    """Return list of flagged patterns found in the brief. Empty = clean."""
    return [p for p in CONTAMINATION_MARKERS if re.search(p, brief)]


# ── Writer ─────────────────────────────────────────────────────────────────────

def run_writer(client: anthropic.Anthropic, brief: str, run: int) -> str:
    """
    Writer actor. Receives brief ONLY.
    Scenarios are structurally absent — not a parameter, not in scope.
    """
    print(f"  [Writer] Run {run} — generating...")
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS_WRITER,
        system=WRITER_SYSTEM,
        messages=[{"role": "user", "content": brief}],
    )
    output = strip_fences(resp.content[0].text)
    print(f"  [Writer] Done — {len(output):,} chars")
    return output


# ── Tester ─────────────────────────────────────────────────────────────────────

def run_tester(
    client: anthropic.Anthropic,
    brief: str,
    scenarios: str,
    output: str,
    run: int,
) -> dict:
    """
    Tester actor. Receives brief + scenarios + output artifact.
    Never receives source code — only what the user would encounter.
    Returns parsed JSON verdict or raises ValueError on bad output.
    """
    print(f"  [Tester] Run {run} — evaluating...")
    prompt = (
        f"BRIEF:\n{brief}\n\n"
        f"---SCENARIOS---\n{scenarios}\n\n"
        f"---OUTPUT---\n{output}\n\n"
        f"Run number: {run}"
    )
    resp = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS_TESTER,
        system=TESTER_SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    raw = strip_fences(resp.content[0].text)

    try:
        verdict = json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(
            f"Tester returned invalid JSON on run {run}.\n"
            f"Error: {e}\nRaw (first 400 chars):\n{raw[:400]}"
        ) from e

    missing = {"run", "result", "scenarios"} - set(verdict)
    if missing:
        raise ValueError(f"Tester JSON missing fields: {missing}")
    if verdict["result"] not in ("PASS", "FAIL"):
        raise ValueError(f"Tester 'result' must be PASS or FAIL, got: {verdict['result']!r}")

    print(f"  [Tester] Verdict: {verdict['result']}")
    for s in verdict.get("scenarios", []):
        mark = "✓" if s["result"] == "PASS" else "✗"
        print(f"    {mark} {s['id']}: {s['reason'][:90]}")
    return verdict


# ── Coordinator loop ───────────────────────────────────────────────────────────

def run_loop(brief_path: Path, scenarios_path: Path, output_dir: Path) -> int:
    """
    Main orchestration. Returns exit code 0 (PASS), 1 (error), or 2 (escalation).
    """
    # Load
    brief_src     = brief_path.read_text(encoding="utf-8")
    scenarios_src = scenarios_path.read_text(encoding="utf-8")
    feature       = brief_path.stem
    ts            = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    print(f"\n{'='*58}")
    print(f"  AI Build Loop")
    print(f"  Brief:     {brief_path.name}")
    print(f"  Scenarios: {scenarios_path.name}")
    print(f"  Output:    {output_dir}")
    print(f"  Max runs:  {MAX_ITERATIONS}")

    # Firewall: contamination check — must pass before any API call
    flags = contamination_check(brief_src)
    if flags:
        print(f"\n[HALT] Firewall violation — brief contains scenario content.")
        for f in flags:
            print(f"  Flagged: {f}")
        print("Resolve before running. Brief and scenarios must be separate files.")
        return 1
    print(f"  Firewall:  CLEAN")
    print(f"{'='*58}\n")

    output_dir.mkdir(parents=True, exist_ok=True)
    client     = anthropic.Anthropic()
    audit      = {"brief": str(brief_path), "scenarios": str(scenarios_path),
                  "started": datetime.now(timezone.utc).isoformat(),
                  "max_iterations": MAX_ITERATIONS, "runs": []}
    current_brief = brief_src
    verdicts      = []
    last_output   = ""

    for iteration in range(1, MAX_ITERATIONS + 1):
        print(f"Run {iteration}/{MAX_ITERATIONS}")
        print("-" * 40)

        # ── Writer: brief only ─────────────────────────────────────────────────
        last_output = run_writer(client, current_brief, iteration)
        run_output  = output_dir / f"output-run-{iteration}.html"
        run_output.write_text(last_output, encoding="utf-8")
        print(f"  [Writer] Saved: {run_output.name}")

        # ── Tester: brief + scenarios + output ────────────────────────────────
        try:
            verdict = run_tester(client, current_brief, scenarios_src, last_output, iteration)
        except ValueError as e:
            print(f"\n[ERROR] Tester parse failure:\n{e}")
            audit["runs"].append({"run": iteration, "result": "TESTER_ERROR", "error": str(e)})
            if iteration < MAX_ITERATIONS:
                print("Continuing to next run...\n")
                continue
            break

        verdicts.append(verdict)
        amendment = verdict.get("spec_amendment") or ""
        audit["runs"].append({
            "run":              iteration,
            "timestamp":        datetime.now(timezone.utc).isoformat(),
            "result":           verdict["result"],
            "scenarios":        verdict.get("scenarios", []),
            "spec_amendment":   amendment or None,
        })

        if verdict["result"] == "PASS":
            # ── Ship ─────────────────────────────────────────────────────────
            final_html = output_dir / f"{feature}.html"
            final_html.write_text(last_output, encoding="utf-8")

            audit["finished"]     = datetime.now(timezone.utc).isoformat()
            audit["final_result"] = "PASS"
            audit["total_runs"]   = iteration
            audit_path = output_dir / f"{feature}-audit-{ts}.json"
            audit_path.write_text(json.dumps(audit, indent=2), encoding="utf-8")

            # Amendment log
            amended_runs = [r for r in audit["runs"] if r.get("spec_amendment")]
            if amended_runs:
                log_lines = [f"# Amendment Log: {feature}\n",
                             f"Converged in {iteration} run(s).\n"]
                for r in amended_runs:
                    log_lines += [f"\n## Run {r['run']} — {r['timestamp'][:10]}\n\n",
                                  r["spec_amendment"], "\n"]
                (output_dir / f"{feature}-amendment-log.md").write_text(
                    "".join(log_lines), encoding="utf-8"
                )

            print(f"\n{'='*58}")
            print(f"  PASS — run {iteration}")
            print(f"  Output:    {final_html.name}")
            print(f"  Audit log: {audit_path.name}")
            print(f"  Human review required before deployment.")
            print(f"{'='*58}\n")
            return 0

        # ── FAIL: amend and continue ───────────────────────────────────────────
        print(f"\n  Run {iteration}: FAIL")
        if amendment and iteration < MAX_ITERATIONS:
            block = (
                f"\n\n## Amendments — Run {iteration} "
                f"({datetime.now(timezone.utc).strftime('%Y-%m-%d')})\n\n"
                f"{amendment.strip()}\n"
            )
            current_brief += block
            amended_path = output_dir / f"{feature}-amended-run-{iteration}.md"
            amended_path.write_text(current_brief, encoding="utf-8")
            print(f"  Brief amended → {amended_path.name}\n")
        elif not amendment:
            print("  [WARN] No spec_amendment returned. Retrying without amendment.\n")

    # ── Escalation ─────────────────────────────────────────────────────────────
    audit["finished"]     = datetime.now(timezone.utc).isoformat()
    audit["final_result"] = "ESCALATED"
    audit["total_runs"]   = MAX_ITERATIONS
    audit_path = output_dir / f"{feature}-audit-{ts}.json"
    audit_path.write_text(json.dumps(audit, indent=2), encoding="utf-8")

    report_lines = [
        f"# Escalation Report: {feature}\n",
        f"_Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}_\n\n",
        f"Loop ran {MAX_ITERATIONS} iterations without passing all scenarios.\n",
        "Bring to PM (Wintermute). The spec has a structural problem requiring human judgment.\n\n",
        "---\n\n",
        "## Most common cause\n\n",
        "The brief's Proposed Solution and the acceptance scenarios describe different things. "
        "Resolve the contradiction at the source before re-running.\n\n",
        "---\n\n",
        "## Brief (with all amendments applied)\n\n```\n",
        current_brief,
        "\n```\n\n---\n\n## Tester Results per Run\n",
    ]
    for v in verdicts:
        report_lines.append(f"\n### Run {v.get('run', '?')}: {v.get('result', '?')}\n")
        for s in v.get("scenarios", []):
            report_lines.append(f"- **{s['id']}** ({s['result']}): {s['reason']}\n")
        if v.get("spec_amendment"):
            report_lines.append(f"\n**Amendment applied:** {v['spec_amendment']}\n")

    esc_path = output_dir / f"{feature}-escalation.md"
    esc_path.write_text("".join(report_lines), encoding="utf-8")

    print(f"\n{'='*58}")
    print(f"  ESCALATED — {MAX_ITERATIONS} runs, no convergence.")
    print(f"  Escalation:  {esc_path.name}")
    print(f"  Audit log:   {audit_path.name}")
    print(f"  Bring to PM. The spec has a structural problem.")
    print(f"{'='*58}\n")
    return 2


# ── CLI ────────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "AI Build Loop Coordinator. Enforces Writer/Tester firewall structurally. "
            "Iterates until all scenarios pass or the max iteration limit is reached."
        )
    )
    parser.add_argument("--brief",       required=True, metavar="PATH",
                        help="Brief .md file (Writer input only)")
    parser.add_argument("--scenarios",   required=True, metavar="PATH",
                        help="Scenarios .md file (Tester input only — never passed to Writer)")
    parser.add_argument("--output-dir",  default=None,  metavar="PATH",
                        help="Output directory (defaults to brief's directory)")
    args = parser.parse_args()

    brief_path     = Path(args.brief).resolve()
    scenarios_path = Path(args.scenarios).resolve()
    output_dir     = Path(args.output_dir).resolve() if args.output_dir else brief_path.parent

    for p, label in [(brief_path, "brief"), (scenarios_path, "scenarios")]:
        if not p.exists():
            print(f"[ERROR] {label} not found: {p}")
            sys.exit(1)

    sys.exit(run_loop(brief_path, scenarios_path, output_dir))


if __name__ == "__main__":
    main()
