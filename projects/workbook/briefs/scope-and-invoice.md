# Project Feature Brief: Scope & Invoice Tool

> Trades workers get stiffed because jobs start without written agreements and end without formal invoices — this tool generates both via text message, with no accounts and no registration required to start.

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

A text-message interface backed by a thin AI server. The worker texts a phone number — no app required to start, no sign-up form, no account.

**Enrollment:** On first text, the worker receives a welcome message and a single confirmation prompt. One reply and they are set up. Their phone number is their identity.

**New job flow:** Worker texts the number in natural language — "I have a tile job, $800, starting Monday for Carlos." The AI parses the message and replies with a formatted scope agreement:

> *"Got it. Here's your scope agreement — forward this to Carlos: 'Hi Carlos — confirming our agreement: tile bathroom floor for $800, starting Monday, Feb 24. Reply YES to confirm.'"*

Worker copies and sends it to the client. Client's YES reply in the thread is the written confirmation — timestamped, stored on both phones.

**Invoice flow:** Worker texts "done with the Carlos job." The AI replies with a ready-to-send invoice:

> *"Here's your invoice — forward this to Carlos: 'Hi Carlos — the tile floor is finished. Invoice: $800. Let me know when you've sent payment.'"*

**Local ledger:** The AI tracks job status in conversation. The worker can text "what do I have outstanding?" and receive a plain-text summary of all active and unpaid jobs. The question of where this data is persisted — on the server transiently, or in a local app on the device — is an open engineering decision (see Biggest Unknowns).

## Why This, Why Now

This is the cheapest possible version of the payment reliability hypothesis. The worker needs no app, no account, and no training — they already know how to send a text. The server is thin: it processes a message and sends one back. If the core assumption — that a structured text invoice changes client payment behavior — turns out to be wrong, almost nothing was spent finding out. If it turns out to be right, everything built next has a validated foundation.

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

1. **Does the invoice text need to look different from a regular message to create social pressure?** The hypothesis depends on the invoice feeling formal — a professional request, not a casual ask. But if the client sees it forwarded into the same WhatsApp thread as every other message, does the formatting register? The message design needs to be tested with real clients, not assumed.

2. **Where does job data live, and does it require an App Store download?** The current direction is local storage on the device. With a pure SMS interface, the server processes each message but has no persistent state — the conversation history is the only record. A companion app could maintain a structured local ledger, but requires an App Store download, which reintroduces friction and potentially an account. The alternative is that the AI server holds a minimal session state — enough to answer "what's outstanding?" — without permanently storing worker data. Engineering needs to answer which of these is viable before the architecture is decided.

3. **What happens to job history when the worker texts from a new number?** The phone number is the worker's identity. If they get a new number, their history is gone. If they lose their phone and the data was local-only, same result. This is acceptable for v1 but needs to be communicated clearly so workers do not expect continuity they will not get.
