# Strategic Initiative Brief: Workbook

> A WhatsApp-native operating system for the trades — where skilled workers build a verified proof-of-work portfolio, agree on job scope and price, and get paid reliably.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Feature List:** [`features.md`](features.md)
**Feature Briefs:** [`whatsapp-ingestion.md`](whatsapp-ingestion.md), [`trust-engine.md`](trust-engine.md), [`worker-payments.md`](worker-payments.md)

---

## The Opportunity

Skilled trade and construction labor — a workforce in the tens of millions globally, heavily immigrant — has no portable, digital record of its work. Reputation travels by word of mouth, locked inside a single employer or foreman relationship. When a worker moves to a new city, contractor, or trade, that history disappears. From the contractor side, General Contractors face a documented global labor shortage and hire largely blind: no verified skill record, no work history, no accountability layer beyond a phone call to a reference who may or may not pick up.

This is a two-sided data vacuum. On the supply side, workers have no way to build equity from their daily labor. On the demand side, GCs carry hiring risk on every new crew member with no systemic way to reduce it.

## Why Now

Three forces are converging:

1. **The labor shortage is structural, not cyclical.** The construction industry faces a persistent skilled labor gap driven by aging workforce retirement and underinvestment in trade training. GCs are actively looking for better ways to source and vet labor — the demand-side pain is acute.

2. **WhatsApp is already the infrastructure.** The smartphone is already in the worker's pocket. WhatsApp has deep penetration in the communities that make up much of the US and global construction labor force. The distribution channel exists — the product just needs to show up inside it.

3. **Computer vision and AI are now capable at the edge.** Assessing construction photo quality, mapping visual consistency across a job sequence, and extracting metadata from images (GPS, timestamps) are now tractable problems with commodity API access. The "Truth Engine" that makes the verification meaningful is buildable by a small team.

## Why Us

The moat is not the interface — it's the data and the network. Every verified photo record created by a worker is behavioral data that cannot be purchased, licensed, or synthesized. Competitive entrants face the same cold-start problem we do, but we can get there first by meeting workers on WhatsApp rather than asking them to change their behavior. Traditional workforce platforms (LinkedIn, Indeed, staffing agencies) are structurally unable to reach this population — their acquisition models assume email addresses, résumés, and internet-native behavior. We enter where those tools cannot.

## What We're Building

A WhatsApp-native platform that serves the full job lifecycle for a skilled trades worker. Workers document their work with Before, Progress, and Completed photos — an AI Trust Engine verifies the record and builds a portable Reference Book. Before a job starts, the worker can agree on scope, price, and start date via WhatsApp and have that agreement confirmed by the client in writing. When the job is complete, the bot offers to invoice the client directly and tracks payment status — all without leaving the conversation. Contractors and homeowners access verified workers through the marketplace; the worker's phone number is their account across all of it.

## What We're Not Doing

- Not building payroll, tax handling, or employment classification tooling
- Not targeting white-collar, office, or remote workers
- Not replacing HR systems or integrating with ATS platforms in this phase
- Not building a native mobile app — the interface is WhatsApp, full stop

## Success Looks Like

| Metric | Target | Timeframe |
|---|---|---|
| Verified workers with 10+ records in their Reference Book | 500 | 6 months post-launch |
| Monthly worker retention (active photo submissions) | ≥ 40% | 6 months post-launch |
| Jobs invoiced through Workbook (vs. off-platform) | ≥ 50% of completed jobs | 6 months post-launch |
| Paying GC or homeowner accounts sourcing through the marketplace | 10 | 12 months post-launch |

## Biggest Unknowns

1. **Can the AI Trust Engine work in the real world?** Construction sites are messy, lighting is poor, and fraud is motivated. Does computer vision produce reliable quality signals in these conditions — or does it produce noise that erodes trust in the verification?

2. **Will clients pay through Workbook rather than cash?** Workers want to use the payment flow — the incentive is clear. But the client has to cooperate. Many homeowners and small contractors prefer cash for informal work. Does the convenience of a payment link change their behavior, or do we hit a ceiling where the client side opts out regardless?

3. **What is the GC's actual evidence threshold?** Before a contractor pays for or acts on a Workbook verification, what level of proof do they need to trust it? And who inside the GC organization is the actual buyer — the foreman, the HR team, the owner?
