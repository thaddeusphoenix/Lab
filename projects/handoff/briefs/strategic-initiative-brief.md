# Strategic Initiative Brief: Handoff

> An offline-first, voice-activated field execution layer for hyperscale construction sites — subcontractors log progress in natural language, an agent validates and updates the P6 master schedule, and the Site Superintendent gets real-time visibility without chasing anyone or becoming a data entry clerk.

**Status:** Aligned
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-03-11
**Related Feature Briefs:** [`schedule-update-flow.md`](schedule-update-flow.md)

---

## The Opportunity

Construction is one of the largest industries in the world and one of the least digitized at the point of execution. The problem is not that construction teams lack software — Procore, Primavera P6, and MS Project are widely deployed. The problem is that these tools were built for the office. They require structured data entry from people whose hands are full, on job sites with poor connectivity, in conditions where sitting down to fill out a form is not an option.

The result: the Site Superintendent becomes a data collection intermediary. Instead of managing the site, they spend their day chasing status updates from subcontractors, manually translating what they hear into schedule fields, and hunting for gaps before they become delays. This is the execution capacity problem. "Gaps between trades" — idle time during handoffs between subcontractors — account for an estimated 65% of major project delays. On a hyperscale site with 5,000 workers, even small per-worker time losses aggregate into material schedule slippage. The math is simple: pennies of wasted time, multiplied across thousands of people, every day, for years.

The market gap is field reporting — specifically, day-to-day progress updates and daily recaps. This is the workflow where current software demands structured input from people who cannot provide it, and where the absence of real data creates cascading schedule risk downstream.

## Why Now

Three forces converge:

1. **Fast GTM for data centers.** Hyperscale data center construction is at historic highs and is acutely schedule-constrained. Owners and GCs are actively looking for tools that compress timelines. This is a buying moment with a clear, concentrated customer base.

2. **Large data flow creates agentic leverage.** The volume of daily updates on a hyperscale site — across trades, zones, and shifts — is too large for any human to synthesize in real time. It is exactly the right scale for an agent. Agentic tools create disproportionate value here precisely because the data problem is too big to solve manually.

3. **Voice AI and offline-first architecture are ready.** Noise-robust speech transcription can now handle construction environments reliably. Progressive Web Apps with local-first sync remove the connectivity excuse. The infrastructure required to make this work in the field exists today.

The key differentiation is not the technology — it is the input model. Standard tools demand daily reporting into structured fields. Agentic tools accept unstructured reporting and produce structured schedule updates. That shift unlocks a behavior that no amount of training or compliance pressure has been able to unlock.

## Why Us

We can build a working prototype — P6 schedule pull, text/voice input, agent reconciliation — in 30 days. The Concept stage is a 30-day sprint. That speed is the moat. We are not competing on enterprise sales cycles or deep integrations. We are competing on the ability to put something real in front of a Site Superintendent faster than any incumbent can respond.

The "Use Case of 1" principle applies here: we win if one superintendent managing one trade finds this more useful than the alternative. That proof point is what drives the pilot and the commercial conversation.

## Who We're Building For

**Buyer:** Project Executive or VP of Operations — the person who signs the check and is accountable for schedule outcomes.

**Primary user:** Site Superintendent — the person who owns daily execution and is currently stuck chasing status.

**Secondary users:** Specialty Foremen (sub-trade leads who log updates) and Project Managers (who consume schedule data for billing and coordination).

## What We're Building

A field execution layer that sits between the master schedule and the people executing it. Specialty Foremen log progress via offline async self-reporting — natural language text or voice, on their phone, no connectivity required. An agent validates, suggests, flags, and proposes updates to the P6 schedule. The Site Superintendent reviews the agent's proposals in a human-in-the-loop approval flow and accepts or overrides. Approved updates sync to P6.

The data layer: BIM Core Object Library for validating what was reported against what exists in the model; P6 Schedule Activity Data as the agent's action surface; SMS and email as communication channels for foremen who won't open an app.

The agent's job is not to automate decisions — it is to eliminate the data entry burden and surface the right decisions to the right human at the right moment. Accuracy over guesswork. The value of friction is real: human-in-the-loop moments are not a limitation, they are the product.

## What We're Not Doing

- No replacement of P6 or Procore — we feed those systems and surface actions within them
- No drone or BIM scanning in the first release — that is a later phase
- No payment, invoicing, or contract management
- No bidding, procurement, or RFP tooling
- No general contractor portfolio management
- No safety, incident, or compliance workflows

## Success Looks Like

| Metric | Target | Timeframe |
|---|---|---|
| Pilot customers live | 3 sites, 3 users, 30 days each | 90 days post-prototype |
| Pilot-to-production contracts signed | ≥ 1 | End of pilot phase |
| Superintendent-reported reduction in schedule chase time | ≥ 30% | 60 days post-pilot |
| P6 schedule update latency (field report → schedule sync) | < 4 hours | At pilot launch |

## Roadmap

| Stage | Duration | What ships |
|---|---|---|
| **Concept** | 30 days | P6 schedule pull; agent generates AI suggestions from daily updates and drone data |
| **Prototype** | 30 days | Connect-and-update P6 flow for Superintendents; email/text communication flows for Foremen |
| **Pilot** | 60 days | 3 customers, 3 users, 30 days, pilot-to-production contract; sales demos by PM |
| **Scale** | 90 days | First 3 co-implemented with project team; next 3 with product oversight only |

## Biggest Unknowns

1. **Will foremen self-report without prompting?** The hypothesis is that async, low-friction voice or text logging removes the friction barrier. But if foremen need a daily nudge via SMS to actually report, the product needs an outbound trigger layer. This should be tested in the prototype stage with a Wizard-of-Oz SMS prompt before building the automation.

2. **What is the acceptable accuracy threshold for P6 updates?** The "accuracy over guesswork" principle is clear, but the specific threshold at which a Superintendent trusts agent-proposed updates without reviewing every one is unknown. Too many false positives erode trust fast. We need to instrument the human-in-the-loop approval rate from day one of the pilot.

3. **What does the P6 data access path look like?** Most hyperscale sites have P6 managed by the GC's scheduler. The Superintendent may not have write access. The agent's ability to "update" P6 may require working through the scheduler as an intermediary — which changes the workflow model significantly. This must be confirmed with a real site before the prototype is locked.
