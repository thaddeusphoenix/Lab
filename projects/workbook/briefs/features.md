# Workbook — Feature List

A complete map of the features needed to support the initiative. Grouped by phase. Links to briefs where they exist.

**Last updated:** 2026-02-23

---

## Phase 1 — Supply Foundation

The core loop. Workers can onboard, document work, build a verified portfolio, and share it. This is the minimum viable supply side.

| Feature | Description | Brief |
|---|---|---|
| **WhatsApp Ingestion Engine** | Worker onboarding, photo logging (Before / Progress / Completed), job bundling, Proximity Protocol initiation | [`whatsapp-ingestion.md`](whatsapp-ingestion.md) |
| **Trust Engine** | EXIF metadata verification, computer vision consistency checks, composite trust badge per job entry | [`trust-engine.md`](trust-engine.md) |
| **Proximity Protocol** | Detects co-present verified workers at the same GPS location; sends WhatsApp vouching request; feeds peer validation signal to Trust Engine | Embedded in ingestion + trust engine briefs — needs own brief |
| **Worker Profile & Reference Book** | Public-facing portfolio page showing verified jobs, trust badges, trade, and location; shareable via link generated in WhatsApp | Needed |

---

## Phase 2 — Transaction Layer

Workers can agree on scope and price, invoice clients, and get paid. The supply side becomes sticky and the platform embeds in the money flow.

| Feature | Description | Brief |
|---|---|---|
| **Worker Payments** | Scope agreement with client confirmation via WhatsApp, invoice generation, payment link delivery, payment status tracking | [`worker-payments.md`](worker-payments.md) |
| **Worker Payment Setup** | One-time flow for a worker to connect a bank account and complete identity verification (Stripe Connect) before they can receive payouts | Needed |
| **Notification & Reminder Engine** | Automated WhatsApp messages for: payment overdue reminders to clients, peer validation requests, badge updates, new inquiry alerts | Needed |

---

## Phase 3 — Demand Side & Marketplace

Contractors and homeowners can find, evaluate, and hire verified workers. This is where Workbook monetizes the demand side.

| Feature | Description | Brief |
|---|---|---|
| **GC & Homeowner Marketplace** | Searchable directory of verified workers; filterable by trade, location, and trust level; contact/hire flow for buyers | Needed |
| **Worker Discoverability** | How workers surface in the marketplace — skill tags, location radius, trust score ranking, availability signal | Needed |

---

## Platform

Internal and operational features that support reliability, safety, and scale. Not user-facing. Post-MVP.

| Feature | Description | Brief |
|---|---|---|
| **Admin & Trust Operations** | Internal tooling for fraud review, badge dispute adjudication, Trust Engine overrides, and manual worker verification | Needed |

---

## Summary

| Phase | Features | Briefed | Needs Brief |
|---|---|---|---|
| Phase 1 — Supply Foundation | 4 | 2 | 2 |
| Phase 2 — Transaction Layer | 3 | 1 | 2 |
| Phase 3 — Demand Side | 2 | 0 | 2 |
| Platform | 1 | 0 | 1 |
| **Total** | **10** | **3** | **7** |

---

## Sequencing Notes

- **Phase 1 must be complete before Phase 2.** Workers need a portfolio before they have anything to invoice for.
- **Worker Payment Setup blocks Worker Payments.** A worker cannot receive a payout until their bank account is connected. This UX likely requires a web view — the one exception to the WhatsApp-only interface.
- **Proximity Protocol can ship as part of the Trust Engine** in Phase 1 but may warrant its own brief if the peer validation mechanic becomes a primary growth mechanism.
- **The Marketplace (Phase 3) can begin as a manual, concierge operation** — a curated list shared with GCs, before any self-serve product is built. Don't build it until the supply side has enough verified workers to make it credible.
