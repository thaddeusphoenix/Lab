# Project Feature Brief: Scope & Invoice Tool

> Trades workers get stiffed because jobs start without written agreements and end without formal invoices — this tool generates both as plain text, ready to send in any conversation, with no backend and no accounts.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-23
**Parent Initiative:** [`strategic-initiative-brief.md`](strategic-initiative-brief.md)

---

## The Problem

**User:** Skilled trade worker — handyman, tile setter, plumber, painter, electrician — working directly for homeowners or small contractors.

**Pain:** The informal payment process has two failure points. First, jobs start without a written agreement — scope drifts, clients claim they expected something different, and the worker has nothing to point to. Second, jobs end with an informal ask for payment — a text message, a conversation, a hope — that the client can ignore without consequence. Workers know both of these are problems. They do not have a professional, frictionless way to fix either one that does not require registering for tools built for licensed contractors.

**Evidence:** Workers already use WhatsApp and SMS to communicate with clients about work. The behavior of sending text confirmations and payment requests exists — it is just unstructured. The tool does not need to create a new behavior. It needs to structure an existing one.

## The Proposed Solution

A Progressive Web App installed from a link with no App Store and no sign-up. Workers save it to their phone's home screen and open it like any app.

**New job flow:** Worker enters client name, job description, price, and start date. The app generates a scope agreement in plain text:

> *"Hi [name] — confirming our agreement: [description] for $[price], starting [date]. Reply YES to confirm."*

Worker taps Share, which opens their native messaging app (WhatsApp, SMS, or any other) with the text pre-filled. Client replies YES in the thread. That reply is the written confirmation — timestamped, stored on both phones, requiring no third party.

**Invoice flow:** When the worker marks the job complete, the app generates an invoice in plain text:

> *"Hi [name] — the [description] is finished. Invoice: $[price]. Please let me know when you've sent payment."*

Worker sends it the same way. One tap, straight into the conversation.

**Local ledger:** All jobs are stored in the app with their current status — Active, Invoiced, Paid, or Overdue. The worker sees everything at a glance. Nothing leaves the phone. There is no sync, no backup, no cloud.

## Why This, Why Now

This is the cheapest possible version of the payment reliability hypothesis. No infrastructure, no legal review, no KYC strategy, no account registration, no third-party dependency. A single developer can build it in under a week. It can be in front of real workers within days of the decision to build. If the core assumption — that a structured text invoice changes client payment behavior — turns out to be wrong, almost nothing was spent finding out. If it turns out to be right, everything built next has a validated foundation.

## Out of Scope

- Payment processing of any kind — the tool generates an invoice, it does not collect money
- Photo capture, portfolio building, or proof-of-work documentation
- Cloud sync, backup, or cross-device access — local storage only
- Account creation or registration with any service
- Automated reminders or scheduled outbound messages
- Sharing or exporting job records in any format
- Multi-worker use — one installation per worker, no team features

## Success Looks Like

1. At least 20 workers send the scope agreement text on a real job within 30 days of first use
2. At least 20 workers send the invoice text on a completed job within 30 days of first use
3. Workers who use both the scope agreement and invoice on a job report fewer payment disputes than jobs where they did not — measured via direct follow-up with a small cohort

## Biggest Unknowns

1. **Does the invoice text need to look different from a regular message to create social pressure?** The hypothesis depends on the invoice feeling formal — a professional request, not a casual ask. But if the client sees it in the same WhatsApp thread as every other message, does the formatting register? The message design needs to be tested with real clients, not assumed.

2. **What happens to the local data when a worker gets a new phone?** Workers change phones, lose phones, and switch devices. Local storage is not portable. A worker who has six months of job history on their old phone has nothing on their new one. This is not a blocker for v1 — but it is the natural pressure point that will push toward cloud storage eventually. The brief should be honest that local storage is a constraint for now, not a permanent design principle.
