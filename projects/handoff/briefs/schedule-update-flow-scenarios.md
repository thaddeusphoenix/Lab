---
firewall: tester-only
---

# Acceptance Scenarios: Schedule Update Flow

> ⚠ **FIREWALL — Writer context boundary.**
> This document is input to the Tester and Coordinator only.
> The Writer (AI coder) must never receive this file or its contents.
> Keep it in a separate file from the brief at all times. Never paste scenarios into the brief.

**Brief:** [`schedule-update-flow.md`](schedule-update-flow.md)
**Feature:** Schedule Update Flow
**Last updated:** 2026-03-11

---

## Tier 1 — Automatable

### S1: Superintendent View renders all schedule activities

**Given:** The app loads with stubbed schedule data containing at least 5 active activities across 2+ trades
**When:** The Superintendent View is displayed
**Then:** All 5+ activities are visible in the reconciliation dashboard, each showing trade name, activity name, zone, and a status indicator
**Method:** DOM assertion — count activity rows; assert each row contains trade, activity, zone, and status elements

### S2: Foreman log entry maps to a schedule activity

**Given:** The Foreman View is open and the stubbed schedule contains an activity "Electrical Conduit — Zone 4"
**When:** The foreman submits the text "Zone 4 electrical conduit is 80% done"
**Then:** The Superintendent View shows that activity with a pending agent-proposed update of "80% complete" and an approve/override action available
**Method:** DOM assertion — find the activity row matching "Zone 4" + "Electrical", assert it has a pending-status class/indicator and an approve button

### S3: Gap detection — unlogged activities are visually distinct

**Given:** The stubbed schedule has 5 activities; only 3 have received foreman log entries
**When:** The Superintendent View is rendered
**Then:** The 2 activities with no log entry are visually distinct from logged activities — different color, icon, or label such as "No update" or "Gap"
**Method:** DOM assertion — activities with no submitted log have a distinct CSS class or attribute; activities with submitted logs do not share that class

### S4: Approve action resolves a pending update

**Given:** An activity has a pending agent-proposed update in the Superintendent View
**When:** The Superintendent clicks/taps the approve button for that activity
**Then:** The activity's status changes from "Pending" to "Approved" and the approve button is no longer present for that activity
**Method:** DOM assertion — after click, activity row no longer contains approve button; status indicator reflects approved state

---

## Tier 2 — Judgment

### S5: Agent mapping handles natural language variation

**Given:** The stubbed schedule contains activities with formal names (e.g., "Electrical Rough-In — Zone 4 North", "MEP Coordination — Level 2")
**When:** The Tester reads the HTML source and evaluates the agent/mapping logic against 3 natural language inputs: (1) "north side electrical rough-in is done", (2) "MEP on level two is about halfway", (3) "we finished the conduit in zone 4"
**Then:** The mapping logic demonstrates it would resolve at least 2 of 3 inputs to the correct schedule activity through keyword matching, fuzzy match, or LLM interpretation — not requiring an exact string match
**Rubric:** Evaluate how the Writer implemented mapping. Look for: zone/location keyword extraction, trade type matching, tolerance for informal phrasing. A hardcoded exact-match-only lookup fails this scenario.
**Pass signal:** PASS if the mapping approach handles at least 2 of 3 natural language variants without requiring exact field names. FAIL if mapping only works on exact matches or the input field requires structured formatting.

### S6: Superintendent View communicates workflow state clearly without instructions

**Given:** A first-time user opens the Superintendent View with a mix of approved, pending, and gap activities
**When:** The Tester reads the rendered output as a new user would
**Then:** The three states (approved, pending approval, no update/gap) are immediately distinguishable by visual treatment alone — without reading a legend or tooltip
**Rubric:** Look for: distinct color or iconography per state; a clear primary action (the approve button) that draws the eye on pending items; gap items that feel like a call to action, not just absence of data. The view should communicate "here is what needs your attention" at a glance.
**Pass signal:** PASS if the three states are visually distinct and the pending/gap items are more prominent than approved items. FAIL if all states look similar or the view requires reading labels to understand what action is needed.

### S7: Foreman View looks and behaves exactly like a native messaging app

**Given:** A foreman opens their input screen
**When:** The Tester reads the rendered Foreman View
**Then:** The UI is a native messaging app — chat bubble thread, text input pinned to the bottom, send button. Outgoing messages (foreman updates) are right-aligned bubbles. Incoming messages (agent replies) are left-aligned bubbles. There are zero form elements: no dropdowns, no labels, no input fields other than the message composer, no required fields, no submit buttons styled as form actions.
**Rubric:** Look for: (1) chat bubble layout with right/left alignment by sender, (2) message input fixed to bottom of screen, (3) send button adjacent to input — not a separate submit button above or below, (4) a conversation header with a contact name or bot name, (5) NO form elements — no `<select>`, no `<label>`, no structured input fields beyond the message textarea/input. The screen must be visually indistinguishable from iOS Messages or Android Messages at a glance.
**Pass signal:** PASS if the Foreman View renders as a chat bubble interface with no form elements and messages align right (outgoing) / left (incoming). FAIL if there are any dropdowns, labels, form-style inputs, or if messages do not use a bubble layout.

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
      "reason": "All 5 activity rows present; each contains trade, activity name, zone, and status indicator elements"
    },
    {
      "id": "S5",
      "tier": 2,
      "result": "FAIL",
      "reason": "Mapping uses exact string match only — 'north side electrical rough-in' does not resolve to the activity."
    }
  ],
  "spec_amendment": "Add to Proposed Solution: the agent mapping must resolve natural language zone and trade references using keyword extraction — not exact string matching. The input 'north side electrical' must map to any activity containing both a north/zone-4 location token and an electrical trade token."
}
```

**Rules for `spec_amendment`:**
- Required when `result` is `FAIL`. Omit when `PASS`.
- Must name the specific constraint that was violated.
- Must be written as a direct addition to the brief — the Coordinator pastes it in verbatim.
- One amendment per failed scenario. If multiple scenarios fail, combine into one amendment block.
