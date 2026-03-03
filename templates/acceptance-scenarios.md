---
firewall: tester-only
---

# Acceptance Scenarios: [Feature Name]

> ⚠ **FIREWALL — Writer context boundary.**
> This document is input to the Tester and Coordinator only.
> The Writer (AI coder) must never receive this file or its contents.
> Keep it in a separate file from the brief at all times. Never paste scenarios into the brief.

**Brief:** [link to brief.md]
**Feature:** [feature name]
**Last updated:** YYYY-MM-DD

---

## Tier 1 — Automatable

_Deterministic. Verified by Playwright, DOM assertions, network intercepts, or snapshot comparisons. No judgment required — the outcome is objectively true or false._

### S1: [Scenario Name]

**Given:** [initial state or context — e.g., "the user has entered age 34 and the main screen is visible"]
**When:** [action taken — e.g., "the user holds the ring circle for 3.2 seconds"]
**Then:** [observable, measurable outcome — e.g., "the ring-circle background has transitioned from #0e0e1c to a non-black color, and the reading-lines container has exactly 5 child elements with class 'show'"]
**Method:** [Playwright selector / DOM assertion / network intercept / visual snapshot]

### S2: [Scenario Name]

**Given:**
**When:**
**Then:**
**Method:**

---

## Tier 2 — Judgment

_Requires evaluation against intent. An LLM-as-judge reads this document and the brief as its rubric, then evaluates the output. Each scenario must yield a machine-readable PASS or FAIL — not an opinion._

### S3: [Scenario Name]

**Given:** [initial state or context]
**When:** [action taken]
**Then:** [expected quality or behavioral outcome — e.g., "the reading lines feel derived from a coherent interpretive framework, not generic affirmations"]
**Rubric:** [what the judge should specifically look for — name the criteria, not the vibe. e.g., "Each of the four Filippi lines references a specific neurotransmitter phase. The fifth line references a traditional mood ring color by name."]
**Pass signal:** PASS if [specific condition]. FAIL if [specific condition].

### S4: [Scenario Name]

**Given:**
**When:**
**Then:**
**Rubric:**
**Pass signal:**

---

## Tester Output Format

Every run must produce a structured result the Coordinator can parse. No prose summaries — structured JSON only.

```json
{
  "run": 1,
  "result": "PASS",
  "scenarios": [
    {
      "id": "S1",
      "tier": 1,
      "result": "PASS",
      "reason": "ring-circle background transitioned to rgb(120,80,200); 5 reading-line elements found with class 'show'"
    },
    {
      "id": "S3",
      "tier": 2,
      "result": "FAIL",
      "reason": "Two of four reading lines were generic affirmations with no Filippi phase reference."
    }
  ],
  "spec_amendment": "Add to Design Constraints: each of the four Filippi reading lines must explicitly name the cycle it represents (moon, season, life arc, or circadian). Generic affirmations without a phase anchor are not acceptable."
}
```

**Rules for `spec_amendment`:**
- Required when `result` is `FAIL`. Omit when `PASS`.
- Must name the specific constraint that was violated.
- Must be written as a direct addition to the brief — the Coordinator pastes it in verbatim.
- One amendment per failed scenario. If multiple scenarios fail, list them separately.
