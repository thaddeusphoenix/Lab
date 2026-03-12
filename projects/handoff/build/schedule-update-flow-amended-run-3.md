# Project Feature Brief: Schedule Update Flow

> The daily workflow that eliminates the Superintendent's data entry burden: Foremen log progress in natural language, an agent maps it to the P6 schedule and proposes updates, and the Superintendent approves or overrides in a single review screen.

**Status:** Aligned
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-11
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Site Superintendent on a hyperscale construction site

**Pain:** The Superintendent has no real-time view of where trades stand without asking. Every morning they conduct a "subcontractor chase" — calling or walking to each trade foreman to collect status updates, then manually translating what they hear into schedule fields in P6 or a spreadsheet. This turns a site management role into a data entry role. On a site with dozens of active trades, this consumes hours of the Superintendent's day and introduces a reporting lag that makes schedule risk invisible until it becomes schedule slippage.

**Evidence:** Field reporting / progress updates is the identified market gap in the product strategy. The 65% of major project delays attributable to "gaps between trades during handoffs" traces directly to this lag. Superintendents on large sites describe the daily status chase as their single biggest time drain.

---

## The Proposed Solution

A two-screen daily workflow. Screen 1 is the **Foreman View**: a native messaging app UI — modeled exactly on the iOS or Android default SMS/Messages app. A conversation thread where the foreman types a progress update in plain language and hits send, exactly like texting a colleague. No form fields, no dropdowns, no labels. Just a message bubble interface with a text input at the bottom and a send button. Previous messages appear as chat bubbles in the thread. Screen 2 is the **Superintendent View**: a reconciliation dashboard showing all active schedule activities for the day, the agent's interpretation of each foreman's log, the proposed P6 update, and a one-tap approve/override action. The agent does the mapping; the Superintendent makes the call.

For this build, the P6 schedule is represented as a stubbed JSON dataset. The agent's reconciliation logic maps natural language message text to schedule activities and flags missing or ambiguous reports. The output is a self-contained HTML prototype — no backend required.

---

## Why This, Why Now

This is the "Use Case of 1" entry point: one superintendent, one trade, one day's worth of updates. It is the smallest slice that validates the core hypothesis — that unstructured field input can be reliably mapped to structured schedule data by an agent, and that a Superintendent will trust and act on the agent's proposals.

If this slice works, every subsequent feature (drone integration, SMS channels, live P6 sync) has a validated core to build on. If it does not work — if the agent's mapping is too inaccurate or the Superintendent does not trust it — we learn that before investing in infrastructure.

---

## Design Constraints

- **Foreman View must look and feel exactly like a native messaging app** — iOS Messages or Android Messages. Chat bubbles, message thread, text input pinned to the bottom, send button. No form elements, no dropdowns, no labels, no required fields. The foreman should feel like they are sending a text message, not filling out a report.
- Outgoing messages (foreman's updates) appear as right-aligned bubbles. Agent responses (acknowledgment/confirmation) appear as left-aligned bubbles in the same thread.
- The messaging UI chrome should match native conventions: rounded bubbles, timestamp, contact name or "Site Bot" as the conversation header.

## Out of Scope

- Real voice transcription (text input stands in for this prototype)
- Live P6 API integration (schedule data is stubbed)
- Drone or BIM data inputs
- SMS or email channel delivery to foremen
- Multi-site or portfolio views
- User authentication or role management
- Offline sync mechanics (all state is in-memory for this build)

---

## Success Looks Like

1. A Superintendent can see all active schedule activities for a given day, each with a status derived from the foreman's log entry — without entering any data themselves.
2. A Foreman can submit a natural language progress update and have it correctly mapped to the right schedule activity in ≥ 8 out of 10 test cases covering typical field language.
3. The Superintendent's review screen clearly distinguishes: activities with agent-proposed updates pending approval, activities with no report logged (gap), and activities already approved — in a single view with no more than 3 interaction steps to approve a full day's updates.

---

## Biggest Unknowns

1. **How much ambiguity can the agent handle?** Foremen will not use consistent terminology. "Zone 4 North conduit" and "the electrical rough-in on the north side" refer to the same activity. The agent needs to resolve this reliably or the Superintendent loses trust immediately. We need to test the mapping accuracy against a realistic sample of natural language inputs before calling the prototype viable.

2. **What is the right human-in-the-loop interaction model?** Bulk approve-all is fast but may create rubber-stamping. Activity-by-activity review is thorough but slow. The right model — likely a flagged-items-only review with bulk approve for clean updates — needs to be tested with a real Superintendent or reasonable proxy before it is locked.

---

## Acceptance Scenarios

Defined in a separate document — create `schedule-update-flow-scenarios.md` in the same `briefs/` directory using `templates/acceptance-scenarios.md`.

**⚠ Firewall rule:** The brief is the Writer's input. The acceptance scenarios are the Tester's rubric. These must live in separate files. The Writer never receives the scenarios document. The Tester receives both. This separation is non-negotiable — if the Writer sees the scenarios, it optimizes for passing the test rather than solving the problem.

The brief is not ready to trigger a build loop until its companion scenarios document exists and is complete.


## Amendments — Run 1 (2026-03-11)

The output artifact must be a complete, self-contained, renderable single HTML file with no truncation. All JavaScript logic must be present including: (1) the stubbed P6 schedule dataset (minimum 5 activities, 2+ trades), (2) the agent natural-language-to-activity mapping function using keyword/token extraction — not exact string match — covering zone, trade type, and completion percentage tokens, (3) the message send handler that triggers the mapping and updates the Superintendent View state, (4) the approve button click handler that transitions activity state from pending to approved and removes the approve button, and (5) the full Superintendent View activity list render. Additionally: the Foreman View must contain zero form elements — remove the foreman <select> dropdown and its <label>. If foreman identity selection is needed for the prototype, implement it as tappable name chips or inline text buttons styled as chat contact rows, not as a <select> or any labeled form input.


## Amendments — Run 2 (2026-03-11)

The output artifact must be a complete, non-truncated single HTML file. The JavaScript must not be cut off at any point. Specifically, all of the following functions must be fully present and syntactically complete: (1) tokenize(str) — full body returning a token array; (2) mapMessageToActivity(text, foremanId) — uses zone and trade alias arrays to score and return the best-matching P6 activity without exact string matching; (3) extractPercentage(text) — returns a numeric completion value from natural language; (4) renderActivityList() — iterates P6_SCHEDULE and inserts activity cards into #activity-list with correct CSS status classes (status-pending, status-gap, status-approved) and approve/override buttons on pending cards; (5) the send button click handler that calls mapMessageToActivity, updates the matched activity's status to 'pending' and proposedPct, appends outgoing and incoming bubbles to the thread, and calls renderActivityList(); (6) approveActivity(activityId) — transitions status from pending to approved and re-renders; (7) bulkApprove() — approves all pending activities; (8) the contact list render that populates foreman rows on load. The file must render a fully functional prototype when opened in a browser with no missing logic.


## Amendments — Run 3 (2026-03-11)

The output artifact must not be truncated under any circumstances. The JavaScript block must be complete and syntactically valid — no string literals, object literals, arrays, or function bodies may be cut off. To enforce this: write all JavaScript functions in the following fixed order, completing each fully before starting the next: (1) all constant data (P6_SCHEDULE, FOREMEN arrays), (2) tokenize(str), (3) extractPercentage(text), (4) mapMessageToActivity(text, foremanId), (5) renderActivityList(), (6) approveActivity(activityId), (7) bulkApprove(), (8) handleSend(), (9) all UI helper functions (showContactList, openChat, autoResize, toggleSend, openOverride, closeOverride, confirmOverride), (10) the DOMContentLoaded init block. If the file would exceed output length at any point, reduce CSS verbosity and remove decorative comments — never truncate JavaScript logic. The file must parse without errors when run through a JavaScript syntax checker.
