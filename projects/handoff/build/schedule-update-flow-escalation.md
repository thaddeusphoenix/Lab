# Escalation Report: schedule-update-flow
_Generated: 2026-03-11_

Loop ran 5 iterations without passing all scenarios.
Bring to PM (Wintermute). The spec has a structural problem requiring human judgment.

---

## Most common cause

The brief's Proposed Solution and the acceptance scenarios describe different things. Resolve the contradiction at the source before re-running.

---

## Brief (with all amendments applied)

```
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


## Amendments — Run 4 (2026-03-11)

The output artifact must not be truncated under any circumstances. The file must be complete and syntactically valid JavaScript with no cut-off string literals, function bodies, or statements. Specifically: the handleSend() function must be fully written including the agent reply construction, appendBubble call for the incoming message, chatHistory update, and renderActivityList() call; all UI helper functions (showContactList, openChat, autoResize, toggleSend, openOverride, closeOverride, confirmOverride) must be fully present; and the DOMContentLoaded init block must be present and complete, wiring all event listeners. If output length is a constraint, reduce the number of CSS comment lines and shorten activity names in P6_SCHEDULE — never truncate JavaScript function bodies or the init block. The file must pass a JavaScript syntax check with zero errors before submission.

```

---

## Tester Results per Run

### Run 1: FAIL
- **S1** (FAIL): The HTML output is truncated — the file ends mid-attribute inside the textarea element. The app is incomplete and cannot be rendered or evaluated. No DOM assertions can be made for the Superintendent View, activity rows, trade/activity/zone/status elements, or any interactive behavior.
- **S2** (FAIL): Cannot evaluate — output is truncated before the agent mapping logic, message submission handler, or Superintendent View activity rows are defined.
- **S3** (FAIL): Cannot evaluate — output is truncated before the activity list and gap/missing state rendering logic are present in the DOM.
- **S4** (FAIL): Cannot evaluate — the approve button click handler and state-change logic are absent due to truncation.
- **S5** (FAIL): Cannot evaluate — the agent/mapping logic JavaScript is absent from the truncated output. No keyword extraction, fuzzy match, or NL resolution code is present to assess.
- **S6** (FAIL): Cannot evaluate — the Superintendent View activity cards with pending/approved/gap visual states are defined in CSS but the rendered activity list and its state logic are absent due to truncation.
- **S7** (FAIL): The Foreman View header and message thread structure are partially present and show correct chat bubble CSS and nav bar. However, the foreman selector uses a <select> dropdown with a <label> element — both are explicitly prohibited form elements per the brief. The message input textarea is incomplete (truncated). Full pass cannot be awarded on a partial render, and the <select>/<label> form elements are a definitive failure against the no-form-elements constraint regardless.

**Amendment applied:** The output artifact must be a complete, self-contained, renderable single HTML file with no truncation. All JavaScript logic must be present including: (1) the stubbed P6 schedule dataset (minimum 5 activities, 2+ trades), (2) the agent natural-language-to-activity mapping function using keyword/token extraction — not exact string match — covering zone, trade type, and completion percentage tokens, (3) the message send handler that triggers the mapping and updates the Superintendent View state, (4) the approve button click handler that transitions activity state from pending to approved and removes the approve button, and (5) the full Superintendent View activity list render. Additionally: the Foreman View must contain zero form elements — remove the foreman <select> dropdown and its <label>. If foreman identity selection is needed for the prototype, implement it as tappable name chips or inline text buttons styled as chat contact rows, not as a <select> or any labeled form input.

### Run 2: FAIL
- **S1** (FAIL): The JavaScript is truncated mid-function inside tokenize(). The render function for the activity list is never defined or called, so the #activity-list div remains empty. No activity rows are present in the DOM.
- **S2** (FAIL): The tokenize() function is cut off before its body completes. The agent mapping function, send handler, and superintendent view update logic are all absent due to truncation. No mapping occurs when a foreman submits a message.
- **S3** (FAIL): Gap detection CSS classes (status-gap) and data model are defined, but the render function that would apply these classes to activity cards is missing due to JS truncation. No gap/no-report visual distinction appears in the DOM.
- **S4** (FAIL): The approve button click handler (and the render logic that inserts approve buttons) is absent due to JS truncation. No approve buttons are rendered and no state transition logic exists.
- **S5** (FAIL): The zoneAliases and tradeAliases arrays on each activity are well-constructed and would support keyword extraction, but the tokenize() function is cut off before completion and the matching logic that uses these arrays is entirely absent. Cannot confirm any natural language variant resolves correctly.
- **S6** (FAIL): CSS for three distinct visual states (pending: orange left border, gap: red left border + dark red background, approved: green left border + reduced opacity) is defined and would be visually distinguishable. However, no activity cards are rendered due to JS truncation, so the visual treatment cannot be evaluated in context.
- **S7** (PASS): Foreman View uses tappable .foreman-row chips (no <select>, no <label> elements present anywhere). Chat bubble layout with .bubble-row.outgoing (right-aligned, blue) and .bubble-row.incoming (left-aligned, gray) is defined in CSS. Compose bar with textarea and circular send button is pinned to bottom via flexbox. Contact header reads 'Messages'. Structure is visually consistent with iOS Messages conventions.

**Amendment applied:** The output artifact must be a complete, non-truncated single HTML file. The JavaScript must not be cut off at any point. Specifically, all of the following functions must be fully present and syntactically complete: (1) tokenize(str) — full body returning a token array; (2) mapMessageToActivity(text, foremanId) — uses zone and trade alias arrays to score and return the best-matching P6 activity without exact string matching; (3) extractPercentage(text) — returns a numeric completion value from natural language; (4) renderActivityList() — iterates P6_SCHEDULE and inserts activity cards into #activity-list with correct CSS status classes (status-pending, status-gap, status-approved) and approve/override buttons on pending cards; (5) the send button click handler that calls mapMessageToActivity, updates the matched activity's status to 'pending' and proposedPct, appends outgoing and incoming bubbles to the thread, and calls renderActivityList(); (6) approveActivity(activityId) — transitions status from pending to approved and re-renders; (7) bulkApprove() — approves all pending activities; (8) the contact list render that populates foreman rows on load. The file must render a fully functional prototype when opened in a browser with no missing logic.

### Run 3: FAIL
- **S1** (FAIL): The JavaScript is truncated mid-string at the completionWords object literal ('mostly done': 80, 'mostly). The renderActivityList() function, mapMessageToActivity(), send handler, approveActivity(), and bulkApprove() are all absent from the file. The prototype will throw a syntax error on load and render no activity cards.
- **S2** (FAIL): The send button handler and mapMessageToActivity() function are never reached in the file — JS is cut off before these functions are defined. Submitting a foreman message cannot trigger any activity state change.
- **S3** (FAIL): Gap detection depends on renderActivityList() applying status-gap CSS class to unlogged activities. That function is absent due to truncation. Cannot assert DOM state.
- **S4** (FAIL): approveActivity() is never defined in the truncated output. The approve button click handler does not exist. State transition from pending to approved is impossible.
- **S5** (FAIL): Zone alias arrays and trade alias arrays are well-structured and would support keyword extraction. tokenize() is syntactically complete. However mapMessageToActivity() is entirely absent from the truncated file and cannot be evaluated for correctness against the 3 test inputs.
- **S6** (PASS): CSS defines visually distinct treatments: status-gap has red border (#ff453a) and red badge, status-pending has orange border (#ff9f0a) and orange badge, status-approved has green border (#30d158) and green badge. Stats bar with colored dot chips provides at-a-glance summary. Pending cards would show approve/override buttons as primary actions. The three states are sufficiently distinct by color and iconography assuming JS renders correctly.
- **S7** (PASS): Foreman View uses chat bubble layout with .bubble.outgoing (right-aligned, blue) and .bubble.incoming (left-aligned, grey). Input bar is pinned to bottom with textarea and circular send button. Contact list uses .contact-row tappable chips — no <select>, no <label>, no form elements. Nav bar shows contact name and role. Structurally indistinguishable from iOS Messages.

**Amendment applied:** The output artifact must not be truncated under any circumstances. The JavaScript block must be complete and syntactically valid — no string literals, object literals, arrays, or function bodies may be cut off. To enforce this: write all JavaScript functions in the following fixed order, completing each fully before starting the next: (1) all constant data (P6_SCHEDULE, FOREMEN arrays), (2) tokenize(str), (3) extractPercentage(text), (4) mapMessageToActivity(text, foremanId), (5) renderActivityList(), (6) approveActivity(activityId), (7) bulkApprove(), (8) handleSend(), (9) all UI helper functions (showContactList, openChat, autoResize, toggleSend, openOverride, closeOverride, confirmOverride), (10) the DOMContentLoaded init block. If the file would exceed output length at any point, reduce CSS verbosity and remove decorative comments — never truncate JavaScript logic. The file must parse without errors when run through a JavaScript syntax checker.

### Run 4: FAIL
- **S1** (FAIL): The JavaScript block is truncated mid-statement at `replyText = "Got it, " + currentForeman.` — this creates a syntax error that prevents the entire script from executing, meaning renderActivityList() is never called and no activity cards are rendered in the DOM.
- **S2** (FAIL): The send button handler (handleSend) is cut off before completion due to script truncation. The mapping logic and state update never execute, so no pending update is created in the Superintendent View.
- **S3** (FAIL): Gap state CSS and initial data are correctly defined, but renderActivityList() never runs due to the JavaScript syntax error from truncation, so no activity cards with gap indicators are rendered.
- **S4** (FAIL): approveActivity() function body is fully present, but the DOMContentLoaded init block is missing due to truncation, so no event listeners are attached and the approve button click handler is never wired.
- **S5** (PASS): The mapMessageToActivity function uses ZONE_ALIASES (including 'north','south' mapped to zone4, 'two' mapped to zone2) and TRADE_ALIASES (including 'conduit','rough-in' for electrical; 'duct','ductwork' for mechanical). Test case 1 ('north side electrical rough-in') scores zone4+electrical → maps to A-1001. Test case 3 ('conduit in zone 4') scores electrical+zone4 → maps to A-1001/A-1002. Test case 2 ('MEP on level two') — 'mep' is not in any trade alias array and 'level 2' is not in zone2 aliases (only 'level 1' is absent; 'two' is present) — 'two' matches zone2 but no trade match for MEP; however foreman bonus may disambiguate. At minimum 2 of 3 resolve correctly through keyword extraction, not exact match.
- **S6** (PASS): Three visually distinct states defined in CSS: gap=red dot+red label+red border note, pending=amber dot+amber label+green approve button as primary CTA, approved=green dot+green label. Pending items have prominent approve/override action row; gap items show a warning note. The visual hierarchy communicates attention priority without requiring a legend.
- **S7** (PASS): Foreman View is a chat bubble interface: .bubble-row.out is right-aligned (align-self:flex-end), .bubble-row.in is left-aligned. Input bar is fixed at bottom with textarea and adjacent send button. Chat header shows contact name and trade subtitle. Zero form elements — no <select>, no <label>, no dropdowns. Contact selection uses .contact-row div chips. Visually matches native messaging app conventions.

**Amendment applied:** The output artifact must not be truncated under any circumstances. The file must be complete and syntactically valid JavaScript with no cut-off string literals, function bodies, or statements. Specifically: the handleSend() function must be fully written including the agent reply construction, appendBubble call for the incoming message, chatHistory update, and renderActivityList() call; all UI helper functions (showContactList, openChat, autoResize, toggleSend, openOverride, closeOverride, confirmOverride) must be fully present; and the DOMContentLoaded init block must be present and complete, wiring all event listeners. If output length is a constraint, reduce the number of CSS comment lines and shorten activity names in P6_SCHEDULE — never truncate JavaScript function bodies or the init block. The file must pass a JavaScript syntax check with zero errors before submission.

### Run 5: FAIL
- **S1** (PASS): P6_SCHEDULE contains 6 activities across 4 trades; renderActivityList() iterates all and creates cards with act-id, act-name, act-trade, and act-status-badge elements
- **S2** (FAIL): The JavaScript is truncated — appendBubble() is cut off mid-function and the DOMContentLoaded init block is absent. The send button has no event listener wired, so submitting 'Zone 4 electrical conduit is 80% done' produces no DOM change. The mapping logic itself is correct but cannot execute.
- **S3** (PASS): Activities initialize with status:'gap' receiving CSS class 'status-gap' and red border-left (#dc3545) plus badge '⚠️ No Report'; logged activities receive 'status-pending' with yellow treatment — visually distinct
- **S4** (FAIL): approveActivity() and renderActivityList() are present and correct, but the approve button onclick fires approveActivity() only if the button is rendered, which requires the init block to have run renderActivityList() on load — which it cannot because DOMContentLoaded is truncated and never present
- **S5** (PASS): mapMessageToActivity uses zone alias arrays and trade alias arrays with substring matching. Input 1 ('north side electrical rough-in') hits zone4 alias 'north' (+5) and trade Electrical (+4), maps to A1001. Input 3 ('conduit in zone 4') hits 'zone 4' substring (+5) and 'conduit' trade alias (+4), maps correctly. Input 2 ('MEP on level two') misses — 'two' not in level2 aliases and 'mep' not in any trade alias — but 2 of 3 pass the rubric threshold.
- **S6** (PASS): Three states are visually distinct: gap=red left border + red '⚠️ No Report' badge, pending=yellow border + yellow badge + prominent green Approve and blue Override buttons, approved=green border + green badge with no action buttons. Summary chips provide at-a-glance counts. Pending items draw the eye via action buttons.
- **S7** (FAIL): The JavaScript is truncated: appendBubble() is cut off after 'wrap.className = "bubble-wrap " + dir;' and the DOMContentLoaded init block is entirely absent. The file does not parse as syntactically valid JavaScript. The chat UI structure and CSS are correct (right/left bubble alignment, bottom-pinned input, no form elements), but the prototype cannot function — no bubbles render, no messages send, no event listeners are wired.

**Amendment applied:** The output artifact must be a complete, non-truncated, syntactically valid single HTML file. The JavaScript must not be cut off at any point. The following functions must be fully present with complete bodies: appendBubble(dir, text, time) — creates and appends a bubble-wrap div with correct class, bubble div, and time span to #message-thread, then scrolls thread to bottom; and the DOMContentLoaded init block — which must wire: (a) the send button click to handleSend(), (b) the msg-input keydown Enter to handleSend(), (c) the msg-input input event to autoResize() and toggleSend(), (d) the bulk-approve-btn click to bulkApprove(), (e) the chat-back button click to showContactList(), and (f) call renderActivityList() and the contact list population function on load. If output length is a constraint, further reduce CSS (remove all transition declarations, collapse shorthand properties) and shorten activity names to under 25 characters — never truncate any JavaScript function body or the init block. The file must open in a browser and immediately render the contact list and Superintendent activity list with no console errors.
