# Workbook — Feature List

A complete map of the features in scope for the initiative. Grouped by phase.

**Last updated:** 2026-02-23

---

## Current Scope

All local storage. Communication via text message only. No accounts, no registration, no third-party services.

| Feature | Description | Brief |
|---|---|---|
| **Scope & Invoice Tool** | Local-first PWA: enter job details, generate a scope agreement text and invoice text, track payment status locally | [`scope-and-invoice.md`](scope-and-invoice.md) |

---

## Sequencing Notes

- This is a single-feature product in its current form. Build it, put it in front of real workers, and validate the core assumption: does a structured text invoice change client payment behavior?
- The natural next pressure point is local storage portability — workers lose phones. That is the signal to revisit cloud storage, not a reason to build it now.
- Marketplace, portfolio, and verification features are deprioritized below. They represent a valid direction if the payment behavior hypothesis is proven and a more ambitious build is warranted.

---

## Deprioritized

Features explored during earlier discovery. Not in scope for the current phase. Briefs are preserved for reference.

| Feature | Brief | Reason deprioritized |
|---|---|---|
| **WhatsApp Ingestion Engine** | [`whatsapp-ingestion.md`](whatsapp-ingestion.md) | Requires photo capture — text-only constraint |
| **Trust Engine** | [`trust-engine.md`](trust-engine.md) | Requires cloud CV APIs and backend infrastructure |
| **Proximity Protocol** | [`proximity-protocol.md`](proximity-protocol.md) | Requires server-side GPS matching and account identity |
| **Worker Profile & Reference Book** | [`worker-profile.md`](worker-profile.md) | Requires hosted web page and cloud data |
| **Worker Payments** | [`worker-payments.md`](worker-payments.md) | Requires Stripe, account registration, payment facilitation |
| **Worker Payment Setup** | [`worker-payment-setup.md`](worker-payment-setup.md) | Requires KYC and bank account registration |
| **Notification & Reminder Engine** | [`notification-reminder-engine.md`](notification-reminder-engine.md) | Requires server infrastructure for outbound messaging |
| **GC & Homeowner Marketplace** | [`gc-homeowner-marketplace.md`](gc-homeowner-marketplace.md) | Requires cloud backend and hosted directory |
| **Worker Discoverability** | [`worker-discoverability.md`](worker-discoverability.md) | Requires search infrastructure and hosted profiles |
| **Admin & Trust Operations** | [`admin-trust-operations.md`](admin-trust-operations.md) | Requires backend and Trust Engine infrastructure |
