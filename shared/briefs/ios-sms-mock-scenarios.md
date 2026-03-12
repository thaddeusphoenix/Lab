---
firewall: tester-only
---

# Acceptance Scenarios: iOS SMS Mock

> ⚠ **FIREWALL — Writer context boundary.**
> Tester and Coordinator input only. Writer must never receive this file.

**Brief:** [`ios-sms-mock.md`](ios-sms-mock.md)
**Feature:** iOS SMS Mock base component
**Last updated:** 2026-03-11

---

## Tier 1 — Automatable

### S1: Correct iOS bubble colors

**Given:** The page is loaded with pre-populated sample messages containing at least one outgoing and one incoming message
**When:** The message thread renders
**Then:** Outgoing bubbles have a background color of `#007AFF` (or `rgb(0, 122, 255)`) and white text. Incoming bubbles have a background color of `#E5E5EA` (or `rgb(229, 229, 234)`) and dark/black text.
**Method:** DOM assertion — inspect computed background-color on outgoing and incoming bubble elements

### S2: Send button state toggles with input

**Given:** The message input field is empty on load
**When:** The input is empty, then the user types any character
**Then:** The send button is visually inactive (gray or low-opacity) when the input is empty, and becomes active (blue, `#007AFF`) when the input contains text
**Method:** DOM assertion — check send button color/opacity class at empty state vs. non-empty state

### S3: Sending a message appends an outgoing bubble

**Given:** The input field contains the text "Test message"
**When:** The send button is clicked
**Then:** A new right-aligned bubble containing "Test message" appears in the thread, and the input field is cleared
**Method:** DOM assertion — count outgoing bubbles before and after click; assert new bubble text matches input; assert input value is empty after send

### S4: Auto-reply appears after send

**Given:** A message has just been sent (outgoing bubble appended)
**When:** 1–3 seconds elapse
**Then:** A new incoming (left-aligned, gray) bubble appears in the thread containing the configured auto-reply text
**Method:** DOM assertion with timeout — after send event, wait up to 3000ms and assert a new incoming bubble has been added

---

## Tier 2 — Judgment

### S5: Visual match to iOS Messages

**Given:** The page is loaded with sample messages
**When:** The Tester reads the full rendered output as a visual designer would
**Then:** The interface is visually indistinguishable from an iOS Messages screenshot — correct status bar, navigation header with back chevron and contact name, bubble tails, input bar pill shape with send button, overall proportions and spacing
**Rubric:** Look for: (1) status bar with time + icons at top, (2) header with `<` back chevron + contact name centered + icons right, (3) bubble tails (CSS triangles pointing toward sender side), (4) pill-shaped input field, (5) circular send button with arrow icon, (6) correct background colors per the brief. Deduct for: missing bubble tails, wrong colors, form-style input instead of pill, missing status bar or header.
**Pass signal:** PASS if all 6 elements are present and colors match spec. FAIL if bubble tails are absent, colors are wrong, or the input looks like a form field rather than an iOS message composer.

### S6: Config block is clearly forkable

**Given:** The Tester reads the HTML source
**When:** Looking for the configuration section
**Then:** There is a clearly delimited config block near the top of the script containing at minimum `CONTACT_NAME`, `INITIAL_MESSAGES`, and `AUTO_REPLY` — defined as simple variables or a config object, not buried in application logic
**Rubric:** The config block should be findable in under 10 seconds by a developer who has never seen the file. It should be separated from the rest of the logic by a comment or whitespace boundary. Values should be simple strings/arrays — not derived from complex logic.
**Pass signal:** PASS if CONTACT_NAME, INITIAL_MESSAGES, and AUTO_REPLY are all present in an isolated config section and could be changed without touching any other code. FAIL if configuration values are scattered through the logic or require understanding the full codebase to modify.

---

## Tester Output Format

```json
{
  "run": 1,
  "result": "PASS",
  "scenarios": [
    {
      "id": "S1",
      "tier": 1,
      "result": "PASS",
      "reason": "Outgoing bubbles: background rgb(0,122,255), color white. Incoming: background rgb(229,229,234), color black."
    }
  ],
  "spec_amendment": null
}
```
