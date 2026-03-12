#!/usr/bin/env python3
"""
Generate PDF for Agentic Reality-Reconciled Digital Twin PRD.
Renders an HTML template via Playwright (headless Chromium) for clean output.
"""

import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

OUT  = Path("projects/handoff/reports/agentic-digital-twin-prd.pdf")
HTML = Path("projects/handoff/reports/agentic-digital-twin-prd.html")

CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
  @page { margin: 54pt 64pt; }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    font-size: 10.5pt;
    line-height: 1.55;
    color: #1a1a1a;
    background: #fff;
  }

  /* ── Page layout ── */
  .page { width: 100%; }

  /* ── Title block ── */
  .doc-label {
    font-size: 9pt;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #0066CC;
    margin-bottom: 6pt;
  }
  h1.doc-title {
    font-size: 22pt;
    font-weight: 700;
    color: #1a1a1a;
    line-height: 1.2;
    margin-bottom: 8pt;
  }
  .doc-meta {
    font-size: 9pt;
    color: #888;
    border-top: 1px solid #e0e0e0;
    padding-top: 8pt;
    margin-bottom: 36pt;
  }

  /* ── Sections ── */
  .section { margin-bottom: 32pt; }

  h2.section-title {
    font-size: 12.5pt;
    font-weight: 700;
    color: #0066CC;
    border-bottom: 1.5px solid #0066CC;
    padding-bottom: 4pt;
    margin-bottom: 14pt;
  }

  h3 {
    font-size: 10.5pt;
    font-weight: 700;
    color: #1a1a1a;
    margin-top: 16pt;
    margin-bottom: 6pt;
  }

  p { margin-bottom: 8pt; }

  /* ── Tables ── */
  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 8pt;
    margin-bottom: 12pt;
    font-size: 9.5pt;
  }
  thead tr { background: #0066CC; color: #fff; }
  thead th {
    text-align: left;
    padding: 7pt 10pt;
    font-weight: 600;
    font-size: 9pt;
    letter-spacing: 0.02em;
  }
  tbody tr:nth-child(even) { background: #f7f9fc; }
  tbody tr:nth-child(odd)  { background: #ffffff; }
  tbody td {
    padding: 7pt 10pt;
    vertical-align: top;
    border-bottom: 1px solid #e8e8e8;
    color: #1a1a1a;
  }
  tbody td strong { font-weight: 600; }

  /* ── Lists ── */
  ul { margin: 6pt 0 10pt 0; padding-left: 0; list-style: none; }
  ul li {
    padding-left: 16pt;
    position: relative;
    margin-bottom: 5pt;
  }
  ul li::before {
    content: "•";
    position: absolute;
    left: 4pt;
    color: #0066CC;
  }
  ul.sub li::before { color: #888; content: "–"; }

  /* ── Callout box ── */
  .callout {
    background: #f0f6ff;
    border-left: 3px solid #0066CC;
    padding: 10pt 14pt;
    margin: 10pt 0 14pt;
    font-size: 9.5pt;
    color: #333;
    border-radius: 0 4pt 4pt 0;
  }

  /* ── Tags ── */
  .tag {
    display: inline-block;
    background: #e8f0fb;
    color: #0055aa;
    font-size: 8pt;
    font-weight: 600;
    padding: 2pt 6pt;
    border-radius: 3pt;
    margin-right: 4pt;
  }
  .tag.red   { background: #fdecea; color: #c00; }
  .tag.green { background: #e8f5e9; color: #2e7d32; }

  @media print {
    body { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    .section { page-break-inside: avoid; }
  }
</style>
</head>
<body>
<div class="page">

<!-- ── Title ────────────────────────────────────────────────────── -->
<div class="doc-label">Product Requirements Document</div>
<h1 class="doc-title">Agentic Reality-Reconciled Digital Twin</h1>
<div class="doc-meta">
  Status: <strong>Draft</strong> &nbsp;·&nbsp; Owner: Wintermute (PM) &nbsp;·&nbsp; Updated: 2026-03-11
</div>

<!-- ── 1. Strategic Context ──────────────────────────────────────── -->
<div class="section">
<h2 class="section-title">1. Strategic Context</h2>

<h3>Problem Statement</h3>
<table>
  <tbody>
    <tr><td style="width:18%;font-weight:600">User</td><td>Site Superintendent on a hyperscale construction site (Data Center EPC)</td></tr>
    <tr><td style="font-weight:600">Pain</td><td>Daily schedule updates rely on manual data collection — the Superintendent personally chases each subcontractor for status, translates verbal reports into P6 fields, and hunts for gaps before they become delays. Current software turns a site management role into a data entry role.</td></tr>
    <tr><td style="font-weight:600">Evidence</td><td>Gaps between trades during handoffs account for an estimated 65% of major project delays. Fast GTM requirements for Data Center EPCs make schedule protection the single most critical operational lever.</td></tr>
    <tr><td style="font-weight:600">Workaround</td><td>Morning walkdowns, radio check-ins, whiteboard trackers, and end-of-day manual P6 updates by the Superintendent or PM.</td></tr>
  </tbody>
</table>

<h3>User Personas</h3>
<table>
  <thead><tr><th>Persona</th><th>Role</th><th>Motivation</th><th>Job to Be Done</th></tr></thead>
  <tbody>
    <tr><td><strong>Project Executive / VP Ops</strong></td><td>Economic Buyer</td><td>Protect schedule and margin on flagship data center builds</td><td>Sign off on tools that demonstrably reduce schedule risk</td></tr>
    <tr><td><strong>Site Superintendent</strong></td><td>Primary User</td><td>Manage execution without drowning in data entry</td><td>Know where every trade stands without asking anyone</td></tr>
    <tr><td><strong>Specialty Foreman</strong></td><td>Secondary User</td><td>Log progress quickly and get back to work</td><td>Report status in seconds without opening an app</td></tr>
    <tr><td><strong>Project Manager</strong></td><td>Secondary User</td><td>Accurate billing and trade coordination data</td><td>Pull schedule actuals without chasing the Super</td></tr>
  </tbody>
</table>

<h3>Strategic Objectives</h3>
<table>
  <thead><tr><th>Objective</th><th>Target</th><th>Timeframe</th></tr></thead>
  <tbody>
    <tr><td>Problem validation</td><td>50% positive response rate on 100 outreach attempts</td><td>Concept (30 days)</td></tr>
    <tr><td>Pilot sign-ups</td><td>15 qualified prospects → 3 pilot deployments</td><td>Prototype (30 days)</td></tr>
    <tr><td>Pilot-to-production contracts</td><td>≥1 signed contract</td><td>End of pilot (60 days)</td></tr>
    <tr><td>Beta commercialization</td><td>15 customers, daily use, testimonials, financial agreements</td><td>Scale (90 days)</td></tr>
    <tr><td>Schedule improvement</td><td>≥30% reduction in superintendent chase time</td><td>60 days post-pilot</td></tr>
  </tbody>
</table>
</div>

<!-- ── 2. Data Specifications ─────────────────────────────────────── -->
<div class="section">
<h2 class="section-title">2. Data Specifications</h2>

<h3>Data Ingredient List</h3>
<table>
  <thead><tr><th>Source</th><th>Type</th><th>Volume / Window</th><th>Owner</th></tr></thead>
  <tbody>
    <tr><td><strong>Primavera P6</strong></td><td>Schedule activity data</td><td>Full project schedule; refreshed per sync cycle</td><td>GC Scheduler</td></tr>
    <tr><td><strong>BIM Core Object Library</strong></td><td>3D model objects</td><td>Full project model; updated per design revision</td><td>BIM Manager</td></tr>
    <tr><td><strong>Drone Reality Capture</strong></td><td>Point cloud / photogrammetry</td><td>Per flight (3 flights during pilot)</td><td>Terabase / Site</td></tr>
    <tr><td><strong>Foreman SMS / Email</strong></td><td>Unstructured natural language</td><td>Per shift; ≥1 update per active trade per day expected</td><td>Specialty Foreman</td></tr>
  </tbody>
</table>

<h3>Quality Thresholds</h3>
<table>
  <thead><tr><th>Metric</th><th>Threshold</th><th>Consequence if Unmet</th></tr></thead>
  <tbody>
    <tr><td>P6 freshness</td><td>Updated within current shift before agent sync</td><td>Agent suggestions flagged as stale; superintendent warned</td></tr>
    <tr><td>BIM completeness</td><td>Core objects present for all active activities</td><td>Agent cannot validate drone data; conflict surfaced to Super</td></tr>
    <tr><td>Foreman report rate</td><td>≥1 update per active trade per day</td><td>Activity marked as gap; async prompt sent to foreman</td></tr>
    <tr><td>Drone data quality</td><td>Point cloud coverage ≥80% of scanned area</td><td>Partial scan flagged; agent uses available data with caveat</td></tr>
  </tbody>
</table>

<h3>Data Supply Chain</h3>
<ul>
  <li><strong>P6:</strong> GC scheduler owns and maintains. Agent reads via API or scheduled export. If P6 is unavailable, agent queues updates and retries; superintendent is notified of the delay.</li>
  <li><strong>BIM:</strong> BIM Manager owns. Treated as ground truth for object validation. Discrepancies between BIM and field reports surface as conflicts — not agent errors.</li>
  <li><strong>Drone data:</strong> Ingested post-flight. Agent cannot act on drone data until ingest is complete. Partial or failed ingests are flagged, not silently skipped.</li>
  <li><strong>Foreman reports:</strong> Delivered via SMS or email. Ownership of report accuracy rests with the reporting foreman.</li>
</ul>
</div>

<!-- ── 3. Reasoning Architecture ─────────────────────────────────── -->
<div class="section">
<h2 class="section-title">3. Reasoning Architecture</h2>

<div class="callout">
  <strong>Core principle:</strong> The agent is a preparer, not an executor. It eliminates the data entry burden and surfaces the right decisions to the right human — it does not make schedule decisions autonomously.
</div>

<h3>Authority Boundaries</h3>
<table>
  <thead><tr><th>Capability</th><th style="width:22%">Disposition</th><th>Notes</th></tr></thead>
  <tbody>
    <tr><td>Map foreman report to schedule activity</td><td><span class="tag green">Autonomous</span></td><td>100% routing accuracy required; mismatches trigger clarification flow</td></tr>
    <tr><td>Estimate % complete from report</td><td><span class="tag green">Autonomous</span></td><td>Surfaced with confidence score; low-confidence queued for review</td></tr>
    <tr><td>Send async clarifying message to foreman</td><td><span class="tag green">Autonomous</span></td><td>Non-blocking; does not hold up draft update</td></tr>
    <tr><td>Flag gap (no report received)</td><td><span class="tag green">Autonomous</span></td><td>Sent to superintendent review queue within 15 min</td></tr>
    <tr><td>Flag source conflict (drone vs. foreman)</td><td><span class="tag green">Autonomous</span></td><td>Both versions drafted; conflict reason stated; Super picks</td></tr>
    <tr><td>Push AI draft update to superintendent queue</td><td><span class="tag green">Autonomous</span></td><td>Pre-populated suggestion; Super reads and edits before approving</td></tr>
    <tr><td><strong>Write approved update to P6</strong></td><td><span class="tag red">Requires Super approval — always</span></td><td>No exceptions. Never automated regardless of confidence level.</td></tr>
    <tr><td><strong>Override or roll back a P6 entry</strong></td><td><span class="tag red">Requires Super approval — always</span></td><td>Super can reverse any agent-proposed update after approval</td></tr>
  </tbody>
</table>

<h3>Decision Logic</h3>
<p><strong>When a foreman report is received:</strong></p>
<ul>
  <li>Map message to schedule activity. Must be near-100% confident or trigger async clarification to foreman.</li>
  <li>Estimate magnitude (% complete). Surface confidence score alongside estimate.</li>
  <li>If magnitude confidence is below threshold → queue for review and send async clarification to foreman.</li>
  <li>If drone data exists for same activity → compare. If sources agree, draft update. If sources conflict, draft both versions, flag the conflict with suspected reason, surface to superintendent.</li>
  <li>Push AI draft update to superintendent review queue within 15 minutes.</li>
</ul>

<p style="margin-top:10pt"><strong>Conflict classification — the agent must distinguish:</strong></p>
<ul>
  <li><strong>Source conflict:</strong> Sources disagree because one is reporting incorrectly (foreman over-reported, drone scan was partial). Expected and acceptable; surfaced gracefully. Not an agent reasoning failure.</li>
  <li><strong>Agent reasoning failure:</strong> Agent misread or misrouted the data. Not acceptable. Triggers review and tuning.</li>
</ul>

<h3>Confidence &amp; Clarification Flow</h3>
<p>Confidence is always surfaced transparently to the superintendent — never hidden or averaged away. The product operates async and offline-first; clarifications are sent to foremen as non-blocking follow-up messages. Nothing waits for a clarification reply before a draft update is queued. If a reply arrives before the superintendent reviews the queue, the draft is updated in place.</p>

<h3>Memory &amp; State</h3>
<ul>
  <li>Agent has access to full project schedule history within a project engagement.</li>
  <li>Per-project trade vocabulary (zone naming conventions, terminology) is learned and retained across the project duration.</li>
  <li>Cross-project learning is not in scope for the pilot. Each new project initializes without prior project context.</li>
</ul>
</div>

<!-- ── 4. Discovery & Prototyping ────────────────────────────────── -->
<div class="section">
<h2 class="section-title">4. Discovery &amp; Prototyping Approach</h2>

<h3>Discovery Partners</h3>
<ul>
  <li>Existing Terabase solar customers who are building data centers</li>
  <li>Site superintendents from any construction field</li>
  <li>Specialty foremen from any industry</li>
</ul>

<h3>Prototyping Approach</h3>
<p>Segmented prototyping follows a <strong>Question → Prototype → Sampling → Results</strong> flow. Three principles govern how prototypes are scoped and run:</p>
<ul>
  <li><strong>One question, multiple prototypes.</strong> A single open question can be explored through more than one prototype form — a clickable mockup and a Wizard-of-Oz simulation can run in parallel against the same question. The goal is to find the fastest signal, not to commit to one method.</li>
  <li><strong>Multiple questions, independent prototypes.</strong> Different open questions run on separate prototype tracks simultaneously. Prototypes do not need to be unified into a single artifact before learning begins. Each question gets the smallest thing needed to answer it.</li>
  <li><strong>Sampling does not require real users.</strong> Sampling can be conducted with actual users, but simulated use and modeled outcomes are valid — particularly when real users are inaccessible at the concept stage. Simulated sampling is explicitly not a shortcut: it is a deliberate choice about what kind of signal is needed at a given fidelity level.</li>
</ul>

<h3>Pilot-Ready Criteria</h3>
<p>We do not advance to a live pilot until all three conditions are met:</p>
<ul>
  <li>The buyer persona can name a specific dollar value the solution is worth to them</li>
  <li>The user personas can describe the workflow and articulate its value in their own words</li>
  <li>The internal team is operationally ready to support real-world data flows</li>
</ul>
</div>

<!-- ── 5. Functional Requirements ────────────────────────────────── -->
<div class="section">
<h2 class="section-title">5. Functional Requirements</h2>

<h3>Core Features</h3>
<ul>
  <li><strong>Offline Async Self-Reporting:</strong> Foremen log progress via SMS or email in natural language. No app required. No active connectivity required at time of submission.</li>
  <li><strong>Schedule Evaluation Flow:</strong> Agent reconciles field reports against P6 master schedule and generates draft updates for superintendent review.</li>
  <li><strong>Drone Scan and Update:</strong> Reality capture ingested post-flight; agent compares against BIM and self-reports to validate or flag.</li>
</ul>

<h3>User Stories</h3>
<table>
  <thead><tr><th>#</th><th>Given</th><th>When</th><th>Then</th></tr></thead>
  <tbody>
    <tr><td>1</td><td>A foreman has completed work in Zone 4</td><td>They text "Zone 4 electrical conduit done"</td><td>Agent routes to correct activity, drafts update, queues for Super review within 15 min</td></tr>
    <tr><td>2</td><td>Drone and foreman reports conflict on an activity</td><td>Agent processes both inputs</td><td>Super sees both versions with conflict reason; picks one; approved version syncs to P6</td></tr>
    <tr><td>3</td><td>A trade has not reported by mid-shift</td><td>Agent detects gap vs. schedule</td><td>Activity flagged; async prompt sent to foreman; Super sees gap in review queue</td></tr>
    <tr><td>4</td><td>Super reviews end-of-day queue</td><td>They approve, edit, or override each draft</td><td>Approved updates sync to P6 within 15 minutes; overrides logged</td></tr>
    <tr><td>5</td><td>A major site event changes the day's plan</td><td>Super makes large edits to multiple drafts</td><td>System accepts full edits without friction; no auto-approval of unchanged items</td></tr>
  </tbody>
</table>

<h3>Design Principles</h3>
<ul>
  <li><strong>Accuracy over guesswork.</strong> A confident wrong answer is worse than a transparent uncertain one.</li>
  <li><strong>Nail the Human-in-the-Loop moments.</strong> The superintendent approves all P6 writes — always, no exceptions. The value of friction is real.</li>
  <li><strong>Value with a use case of 1.</strong> Must work for one superintendent and one trade before scaling.</li>
  <li><strong>One-way reporting infrastructure.</strong> This is not a two-way communication tool. Critical issues go through official channels. Do not create the expectation of real-time response.</li>
</ul>

<h3>Out of Scope</h3>
<ul>
  <li>Real-time or two-way communication between foremen and superintendents</li>
  <li>Autonomous P6 writes of any kind, regardless of confidence level</li>
  <li>Cross-project model learning or portfolio-level analytics (pilot phase)</li>
  <li>Payment, invoicing, procurement, safety, or compliance workflows</li>
</ul>
</div>

<!-- ── 5. Evaluation & Performance ───────────────────────────────── -->
<div class="section">
<h2 class="section-title">6. Evaluation &amp; Performance Standards</h2>

<h3>Two-Axis Accuracy Model</h3>
<table>
  <thead><tr><th>Axis</th><th>Target</th><th>Below-Threshold Action</th></tr></thead>
  <tbody>
    <tr>
      <td><strong>Task routing accuracy</strong><br><span style="color:#888;font-size:9pt">Right activity mapped</span></td>
      <td>Near-100%. Wrong activity is never acceptable.</td>
      <td>Immediate clarification flow to foreman. Manual review queue. Tuning required.</td>
    </tr>
    <tr>
      <td><strong>Magnitude accuracy</strong><br><span style="color:#888;font-size:9pt">% complete estimate</span></td>
      <td>Best-effort with confidence score. Allowed to miss — uncertainty is surfaced.</td>
      <td>Low-confidence estimates queued for review. Async clarification sent to reporter.</td>
    </tr>
  </tbody>
</table>

<h3>Approval Ratio Target</h3>
<div class="callout">
  <strong>Target: 99/100</strong> draft updates accepted with minor edits on routine days.<br>
  Major edits on days with significant site events (weather, safety incident, scope change) are not product failures — they are expected exceptions.<br>
  Approval ratio below 99% on routine days requires investigation and model tuning before scale.
</div>

<h3>Golden Dataset</h3>
<table>
  <tbody>
    <tr><td style="width:24%;font-weight:600">Size</td><td>Minimum 100 labeled foreman messages across ≥5 trade types and ≥3 zone naming conventions</td></tr>
    <tr><td style="font-weight:600">Owner</td><td>PM in partnership with pilot site superintendent</td></tr>
    <tr><td style="font-weight:600">Validation</td><td>Domain expert labels correct activity and % complete. Agent must route correctly on ≥98 of 100 samples to pass.</td></tr>
    <tr><td style="font-weight:600">Required before</td><td>Pilot launch. No pilot without a passing golden dataset run.</td></tr>
  </tbody>
</table>
</div>

<!-- ── 7. Non-Functional Requirements ────────────────────────────── -->
<div class="section">
<h2 class="section-title">7. Non-Functional Requirements &amp; Guardrails</h2>

<h3>Latency Targets</h3>
<table>
  <thead><tr><th>Operation</th><th>Target</th><th>Worst-Case Bound</th></tr></thead>
  <tbody>
    <tr><td>Foreman report → superintendent review queue</td><td><strong>15 minutes</strong></td><td>30 min (degraded connectivity)</td></tr>
    <tr><td>Superintendent approval → P6 sync</td><td><strong>15 minutes</strong></td><td>30 min</td></tr>
    <tr><td>Drone ingest → agent suggestions available</td><td><strong>2 hours post-flight</strong></td><td>4 hours</td></tr>
    <tr><td>Async clarification → foreman delivery</td><td><strong>15 minutes</strong></td><td>30 min</td></tr>
  </tbody>
</table>

<h3>One-Way Design Contract</h3>
<p>This product is reporting infrastructure, not a communication platform. Foremen post updates; the agent processes them; the superintendent reviews and acts. There is no expectation of real-time response in either direction. If a situation is time-critical, it must be escalated through official channels (radio, phone, direct conversation). The product must never create the impression that it replaces those channels.</p>

<h3>The Escape Hatch</h3>
<ul>
  <li>Superintendent can override any agent-proposed update before or after approval.</li>
  <li>Approved P6 updates can be rolled back by the superintendent at any time; rollback is logged.</li>
  <li>If the agent cannot map a message with sufficient confidence, it surfaces the raw message to the superintendent rather than guessing silently.</li>
  <li>All agent actions are logged with timestamps and confidence scores.</li>
</ul>

<h3>Privacy &amp; Data Ownership</h3>
<ul>
  <li>Job site data is owned by the GC / project owner — not Terabase.</li>
  <li>Default data retention: project data deleted 90 days after project close, per customer contract.</li>
  <li>No foreman PII stored beyond message content and timestamp. Phone numbers hashed after delivery.</li>
</ul>
</div>

<!-- ── 7. Lifecycle & Maintenance ────────────────────────────────── -->
<div class="section">
<h2 class="section-title">8. Lifecycle &amp; Maintenance</h2>

<h3>Degradation Thresholds</h3>
<table>
  <thead><tr><th>Signal</th><th>Alert Threshold</th><th>Action</th></tr></thead>
  <tbody>
    <tr><td>Superintendent approval ratio</td><td>&lt;99% on 3+ consecutive routine days</td><td>Investigate; pause scale; tuning sprint</td></tr>
    <tr><td>Task routing accuracy</td><td>Any confirmed misroute in golden dataset re-run</td><td>Immediate tuning; do not advance pilot</td></tr>
    <tr><td>P6 sync failure rate</td><td>&gt;5% of approved updates fail to sync</td><td>Engineering escalation; manual sync fallback</td></tr>
    <tr><td>Foreman report rate</td><td>&lt;1 update/trade/day for 3+ consecutive days</td><td>PM outreach; product or adoption issue</td></tr>
  </tbody>
</table>

<h3>Roadmap &amp; Ownership</h3>
<table>
  <thead><tr><th>Stage</th><th>Duration</th><th>Milestone</th><th>Owner</th></tr></thead>
  <tbody>
    <tr><td>Concept</td><td>30 days</td><td>P6 pull live; AI suggestions from drone + BIM + daily updates</td><td>PM + Engineering</td></tr>
    <tr><td>Prototype</td><td>30 days</td><td>P6 update flow for Supers; SMS/email flows for Foremen</td><td>Engineering + PM</td></tr>
    <tr><td>Pilot</td><td>60 days</td><td>3 customers, 3 users, 3 drone flights; contract signed</td><td>PM + Customer</td></tr>
    <tr><td>Scale</td><td>90 days</td><td>First 3 co-implemented; next 3 partner-led</td><td>Partners + Product</td></tr>
  </tbody>
</table>

<h3>Monitoring Cadence</h3>
<table>
  <thead><tr><th>Signal</th><th>Cadence</th><th>Alert Threshold</th></tr></thead>
  <tbody>
    <tr><td>Approval ratio</td><td>Daily (pilot)</td><td>&lt;99% on routine day</td></tr>
    <tr><td>Task routing accuracy</td><td>Weekly golden dataset re-run</td><td>Any confirmed misroute</td></tr>
    <tr><td>Latency (report → queue)</td><td>Continuous</td><td>&gt;30 min average</td></tr>
    <tr><td>Foreman report rate</td><td>Daily</td><td>&lt;1 update/trade/day</td></tr>
    <tr><td>P6 sync success rate</td><td>Per sync cycle</td><td>&gt;5% failure rate</td></tr>
  </tbody>
</table>
</div>

<!-- ── Biggest Unknowns ───────────────────────────────────────────── -->
<div class="section">
<h2 class="section-title">Biggest Unknowns</h2>
<ul>
  <li><strong>Will foremen self-report without prompting?</strong> The async clarification flow assumes foremen respond. If they don't, gap detection is the only fallback. Wizard-of-Oz SMS testing needed before automating the prompt layer.</li>
  <li><strong>What is the P6 write-access path?</strong> At most hyperscale sites, P6 is owned by the GC's scheduler — not the superintendent. If updates must route through the scheduler, the approval workflow changes significantly.</li>
  <li><strong>What is the confidence threshold for queuing vs. routing?</strong> The numeric threshold requires empirical testing against the golden dataset before it can be hardcoded.</li>
  <li><strong>What does the sales demo need to close the room?</strong> The one moment that converts a Project Executive from interested to contracted is undefined. Must be identified during discovery before prototype stage.</li>
</ul>
</div>

</div><!-- /page -->
</body>
</html>"""

async def render():
    HTML.parent.mkdir(parents=True, exist_ok=True)
    HTML.write_text(CONTENT, encoding="utf-8")

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 816, "height": 1056})
        await page.goto(f"file://{HTML.resolve()}")
        await page.pdf(
            path=str(OUT),
            format="Letter",
            margin={"top": "72px", "bottom": "72px", "left": "86px", "right": "86px"},
            print_background=True,
        )
        await browser.close()

    HTML.unlink()  # clean up intermediate HTML
    print(f"PDF written → {OUT}")

if __name__ == "__main__":
    asyncio.run(render())
