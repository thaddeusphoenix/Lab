# Strategic Initiative Brief: Workbook

> A local-first text tool for trades workers — agree on job scope, send a text invoice, track what you're owed. No backend, no accounts, no registration.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Feature List:** [`features.md`](features.md)
**Feature Briefs:** [`scope-and-invoice.md`](scope-and-invoice.md)

---

## The Opportunity

Skilled trade workers — handymen, tile setters, plumbers, painters, electricians — start jobs on a handshake and invoice on a text message that says "hey, can you pay me?" When the client goes quiet, the worker has nothing to point to: no written agreement, no formal invoice, no paper trail. The only leverage is to stop coming back. They absorb this risk because building a more professional process has always required registering for tools designed for licensed contractors — Stripe, QuickBooks, Wave — that assume a bank account, an email address, and a business entity.

The opportunity is simpler than any of that. The worker already has a phone. The client is already in their contacts. The WhatsApp or SMS thread already serves as a timestamped, written record — it just needs better input. A structured text message agreeing on scope, and a structured text message invoicing for the work, is all that separates an informal handshake from a written record both parties can point to. No server required. No account required. The conversation thread is the ledger.

## Why Now

Two things make this the right moment:

1. **The infrastructure constraint is the insight.** Removing cloud, accounts, and registration doesn't limit the product — it defines it. A Progressive Web App that a worker saves to their home screen from a link, with no App Store and no sign-up, can be in a worker's hands the same day they hear about it. There is no onboarding funnel to lose them in.

2. **Text is already how this population communicates about work.** Workers already send informal job confirmations and payment requests via WhatsApp. The behavior exists. The tool just structures it.

## Why Us

We can build this in a week and put it in front of real workers. No infrastructure decisions, no legal review of payment facilitation, no KYC strategy. The constraint removes every blocker and compresses the feedback loop to days. If a structured text invoice changes client payment behavior — even slightly — that's the signal worth building on.

## What We're Building

A local-first Progressive Web App. Workers save it to their home screen from a link — no App Store, no login, no registration of any kind. They enter a job: client name, job description, price, start date. The app generates a scope agreement in plain text, ready to copy into any conversation. When the job is done, the app generates an invoice in plain text, ready to send the same way. Workers mark jobs as paid when money arrives. All data lives in local storage on the phone. There is no server, no database, no third-party service involved at any point.

The client does not need to download anything. They receive a text message. That is the entire product surface.

## What We're Not Doing

- No photos, portfolio building, or proof-of-work documentation
- No cloud backend, server, or database of any kind
- No account creation or service registration — not with Workbook, not with any third party
- No automated messaging or scheduled outbound reminders
- No payment processing, payment links, or bank account integration
- No marketplace, contractor-facing search, or hiring features

## Success Looks Like

| Metric | Target | Timeframe |
|---|---|---|
| Workers who use the scope agreement on at least one real job | 20 | 30 days post-launch |
| Workers who send a text invoice on at least one job | 20 | 30 days post-launch |
| Workers who return to log a second job | ≥ 50% of first-job users | 60 days post-launch |

## Biggest Unknowns

1. **Does a formal text invoice change client payment behavior?** The hypothesis is that a structured, professional-looking invoice message creates a social obligation that a casual "hey can you pay me" does not. This is the core assumption and it needs to be tested on real jobs with real clients before anything else is built.

2. **Will workers install even a zero-friction PWA?** Saving a web page to a home screen is not the same as downloading an app — but it is still a new behavior. If workers find the templates useful but just copy the format into their own messages without ever returning to the app, that is still a valid outcome — but it tells us the product is a template, not a tool.

3. **Does a written scope agreement prevent disputes, or just document them?** A written "yes" from the client is not legally binding in most informal labor contexts. If clients dispute payment after confirming scope in writing, the tool has documented the dispute but not resolved it. We need to understand whether workers feel more protected and whether clients actually honor their written confirmations.
