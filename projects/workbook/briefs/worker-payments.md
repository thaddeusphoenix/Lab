# Project Feature Brief: Worker Payments

> A WhatsApp-native flow for agreeing on scope and price, confirming a start date, sending an invoice, and tracking payment — so the worker gets paid reliably and has a written record of every job.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Skilled trade worker — handyman, tile setter, plumber, electrician, painter — working directly for homeowners or small contractors.

**Pain:** Getting paid is unreliable, and disputes are unwinnable. Jobs are agreed verbally. Scope drifts because neither party wrote anything down. Invoices are informal — a text message, a handshake, or nothing at all. When a client delays or refuses payment, the worker has no written agreement to point to and no professional process to escalate through. The only leverage is to stop coming back — which also means losing the relationship and any unpaid balance. Workers absorb this risk silently because they have no alternative infrastructure.

**Evidence:** The mechanics lien system — a legal remedy that allows contractors to place a claim on a property for unpaid work — exists specifically because payment disputes are endemic in construction. That system is designed for licensed contractors with legal access; the informal trades worker has no equivalent. Payment apps like Venmo and Zelle are used informally but provide no scope agreement, no invoice record, and no professional context. The problem is not that workers lack phones — it is that no tool in their reach connects agreement → documentation → payment in one place.

## The Proposed Solution

A WhatsApp-native job agreement and invoicing flow embedded directly in the worker's existing Workbook conversation. Four steps, all via chat:

**1. Scope agreement.** The worker initiates a new job in Workbook. The bot collects three things: a brief description of the work, the agreed price, and the start date. It composes a plain-language summary and sends it to the client's phone number via WhatsApp: *"Marco has sent you a job agreement. He'll [description] for $[price], starting [date]. Reply YES to confirm."* The client's reply creates a timestamped written agreement stored in Workbook — visible to both parties.

**2. Invoice trigger.** When the worker marks a job as Completed, the bot prompts: *"Ready to invoice [client name] for $[price]?"* If yes, it generates a payment link (via Stripe) and sends it to the client: *"Your job with Marco is complete. Pay $[price] here: [link]."* The worker's bank account is where the funds land.

**3. Payment tracking.** The worker can ask "payment status" at any time and receive a current status: pending, paid, or overdue. If payment is not received within a configurable window (default: 7 days), the bot sends the client a single automated reminder. The worker sees all of this in their Workbook conversation — no separate app.

## Why This, Why Now

Payments solve the retention problem the portfolio alone cannot. The portfolio's value is deferred — a worker builds records today and might access better jobs months from now. Payment is immediate — a worker invoices today and gets paid this week. That changes the incentive structure entirely: Workbook becomes something the worker reaches for on every job, not occasionally. It also changes the strategic position of the platform. Embedding in the transaction — owning the moment when money moves — creates a moat that reputation and discovery cannot. A worker who has used Workbook to agree on scope and get paid on ten jobs has a payment history, a job record, and a portfolio all in one place. Leaving means starting over on all three.

## Out of Scope

- Payroll processing, tax withholding, or 1099 generation
- Escrow or milestone-based payment schedules
- Dispute resolution or chargeback management
- Multi-currency or international payment rails (US-first)
- Client-side Workbook accounts — clients interact only via WhatsApp message and payment link, no sign-up required

## Success Looks Like

1. **Invoice adoption:** ≥ 50% of workers who complete a job in Workbook use the invoice flow at least once within the first 30 days
2. **Invoice-to-payment conversion:** ≥ 65% of invoices sent through Workbook are paid within 14 days
3. **Payment stickiness:** Workers who invoice once use the flow on ≥ 70% of subsequent completed jobs

## Biggest Unknowns

1. **Will clients pay through a link from an unfamiliar platform?** The worker trusts Workbook; the client has never heard of it. They receive a WhatsApp message from a number they don't recognize and a payment link. What is the trust signal that gets them to click and pay — and what makes them abandon it? This is the highest-risk assumption in the feature and needs to be tested with real clients before building the payment infrastructure.

2. **Are clients able to pay digitally?** In markets where informal trades workers are most active, their clients — homeowners, landlords, small property managers — often prefer cash for informal work. Whether this is preference, habit, or a deliberate tax choice varies. If a significant portion of the client base actively resists digital payment, the conversion ceiling may be structural rather than a UX problem.

3. **What regulatory exposure does payment facilitation create?** Collecting and disbursing payments on behalf of workers implicates money transmitter licensing, KYC/AML obligations, and 1099-K reporting thresholds. These requirements vary by state and scale with transaction volume. The regulatory path needs to be mapped before the feature is built, not after it reaches volume.
