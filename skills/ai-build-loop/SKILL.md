---
name: ai-build-loop
description: Use when a brief has reached Aligned status and both the brief and acceptance scenarios documents are complete. Runs the three-actor build loop — Writer, Tester, Coordinator — and iterates until all scenarios pass or the iteration limit is reached. Produces a shipped output artifact and an amendment log.
---

## Quick Start

Confirm two files exist in `projects/<name>/briefs/`:
- `[feature-name].md` — the brief (Writer input)
- `[feature-name]-scenarios.md` — acceptance scenarios (Tester input only)

If either is missing or incomplete, stop. Use `skills/write-a-brief` first.

---

## The Three Actors

| Actor | Receives | Produces | Context rule |
|---|---|---|---|
| **Writer** | `brief.md` only | code / output artifact | Never sees `scenarios.md` |
| **Tester** | `brief.md` + `scenarios.md` + output artifact | Structured JSON: PASS/FAIL per scenario + `spec_amendment` | Never sees the Writer's code — only the running output |
| **Coordinator** | All artifacts | Orchestrates loop, applies amendments, signals done or escalates | The only actor that sees everything — never collapses Writer/Tester context |

---

## ⚠ The Firewall

**The acceptance scenarios document must never be passed to the Writer.**

This is the single most important rule in the loop. If the Writer sees the scenarios, it will optimize toward passing the test rather than solving the actual problem stated in the brief. The scenarios are the Tester's rubric — they exist to catch failures the Writer did not anticipate, not to guide the Writer's implementation.

Enforcement:
- Brief and scenarios are always separate files — never merge them
- When constructing the Writer's prompt, read only `brief.md`
- When constructing the Tester's prompt, read `brief.md` + `scenarios.md` + the output
- The Tester evaluates the output as a user would — rendered result or behavior trace, not source code

---

## Workflow

### 1. Gather — Confirm prerequisites

- [ ] Brief exists and status is `Aligned`
- [ ] Acceptance scenarios document exists and all scenarios have Pass signals defined
- [ ] Output type is clear: what artifact does the Writer produce? (HTML file, API endpoint, document, etc.)
- [ ] Max iterations agreed: default is **5**

### 2. Explore — Writer run

Pass `brief.md` to the Writer. The Writer produces the output artifact.

Writer prompt pattern:
```
You are the Writer in an AI build loop. Your input is the feature brief below.
Produce the specified output artifact. Do not ask clarifying questions — implement
to the best of your interpretation of the brief. If anything is ambiguous, make a
reasonable decision and note it in a comment.

[brief.md contents]
```

### 3. Discuss — Tester evaluation

Pass `brief.md` + `scenarios.md` + the output artifact to the Tester. The Tester must not see the Writer's source code — only the running output (rendered HTML, API response, observable behavior).

Tester prompt pattern:
```
You are the Tester in an AI build loop. Your inputs are:
1. The feature brief (what was intended)
2. The acceptance scenarios (what must be true for this to pass)
3. The output artifact (what was actually built)

Evaluate the output against every scenario. Produce the structured JSON result
defined in the scenarios document. Do not rationalize past a failure — if the
output does not satisfy a scenario, mark it FAIL and write a specific spec_amendment.

[brief.md contents]

---SCENARIOS---
[scenarios.md contents]

---OUTPUT---
[output artifact or behavior trace]
```

### 4. Plan — Coordinator decision

Read the Tester's JSON output.

- If `result: PASS` → proceed to step 5
- If `result: FAIL` and iteration count < max:
  - Append each `spec_amendment` to `brief.md` under a new section: `## Amendments — Run [N]`
  - Log the amendment with run number and date
  - Return to step 2 with the amended brief
- If `result: FAIL` and iteration count = max → escalate to human (see Escalation below)

### 5. Document — Ship and record

- Update brief status to `Shipped`
- Create `[feature-name]-amendment-log.md` in `briefs/` summarizing what changed across runs
- Deliver output artifact to the designated location
- Human reviews before any public deployment

---

## Escalation Protocol

If the loop hits the iteration limit without passing:

1. Do not attempt a 6th run
2. Create `[feature-name]-escalation.md` in `briefs/` containing:
   - The current state of the brief (all amendments applied)
   - The full Tester output from each failed run
   - A plain-language summary of what the spec keeps getting wrong
3. Bring to PM (Wintermute) — the spec has a structural problem that requires human judgment

The most common escalation cause: the brief's "Proposed Solution" and the acceptance scenarios are describing different things. Resolve the contradiction at the source.

---

## Execution

The Coordinator script enforces the firewall at the API call level — scenarios are structurally absent from the Writer's API call. It is impossible for the Writer to see the scenarios without modifying the source code.

### Setup

```bash
pip3 install -r skills/ai-build-loop/requirements.txt
export ANTHROPIC_API_KEY=your_key_here
```

### Run

```bash
python3 skills/ai-build-loop/coordinator.py \
  --brief   projects/<name>/briefs/<feature>.md \
  --scenarios projects/<name>/briefs/<feature>-scenarios.md
```

With an explicit output directory:

```bash
python3 skills/ai-build-loop/coordinator.py \
  --brief   projects/<name>/briefs/<feature>.md \
  --scenarios projects/<name>/briefs/<feature>-scenarios.md \
  --output-dir projects/<name>/build/
```

### Exit codes

| Code | Meaning | Artifacts produced |
|---|---|---|
| `0` | PASS | `<feature>.html`, audit log, amendment log |
| `1` | Input or firewall error | Error to stdout — nothing saved |
| `2` | Escalated — max runs reached | `<feature>-escalation.md`, audit log |

### Output files (all in `--output-dir`)

- `<feature>.html` — the passing artifact _(exit 0 only)_
- `output-run-N.html` — artifact from each individual run
- `<feature>-amended-run-N.md` — brief state after each amendment
- `<feature>-audit-<timestamp>.json` — full run log with per-scenario verdicts
- `<feature>-amendment-log.md` — human-readable summary of amendments _(if any)_
- `<feature>-escalation.md` — escalation report for PM review _(exit 2 only)_

## Checklist

- [ ] Both documents exist and are complete before loop starts
- [ ] Writer prompt contains only `brief.md` — not scenarios
- [ ] Tester receives output artifact, not source code
- [ ] Tester output is structured JSON — not prose
- [ ] Each amendment is appended to the brief with run number
- [ ] Loop exits at 5 iterations maximum
- [ ] Human reviews passing output before deployment
- [ ] Amendment log created on exit
