# Project Feature Brief: Core Planning Loop

> Working parents lose money and miss spots because they are not prepared to act when registration opens — not because they don't know the deadline.

**Status:** Draft
**Owner:** Wintermute (Product Manager)
**Last updated:** 2026-02-27
**Platform:** Progressive Web App (PWA) — responsive web with push notifications and native share. Native mobile apps deferred until PMF is established.
**Parent Initiative:** [Camp Planner Strategic Initiative Brief](strategic-initiative-brief.md)

---

## The Problem

**User:** Working parents with school-age children who manage summer program enrollment across multiple programs, deadlines, and children.

**Pain:** The planning failure is not ignorance of deadlines — it is unpreparedness at the moment of action. Parents know registration opens on March 15. What they don't have, when March 15 arrives, is the registration link, the correct session selected, their payment method ready, and their account logged in. The result: missed spots, late registrations, and the stress of a problem that was visible weeks in advance but not acted on in time. Alongside this, parents have no single place to see whether their summer is actually covered week by week, or how their total spending tracks against a household budget.

**Evidence:** Validated by first research session (Sari Gelzer, 2026-02-26). Sari described setting alarms and preparing specifically to "be ready to click the button." She uses Notes and Google Calendar today — tools that store dates but provide no preparation context. She explicitly said she wished the app could "click the button for her."

---

## The Proposed Solution

A program tracking tool with three tightly connected views:

**Program list.** Parents add programs they're considering or registered for, with: name, dates, registration deadline, registration URL, cancellation deadline, cancellation policy, fee, and status (Considering / Registered / Waitlisted / Cancelled). This is the source of truth for all downstream views.

**Summer coverage.** A week-by-week grid showing which weeks are filled, which are tentative, and which are gaps. Color-coded by status. The goal is to make coverage gaps feel visceral — four empty weeks is more alarming as a visual than as a number.

**Decisions + Enrollment Prep.** A prioritized action list. When a registration deadline is more than 14 days out, the card shows the deadline and fee. When a deadline is within 14 days, the card becomes an **Enrollment Prep Card**: it surfaces the registration link, the fee, the specific session/week being registered for, and a three-item readiness checklist (account logged in, payment method ready, session selected). The parent arrives at the moment prepared to act.

**Budget tracking.** Parent sets a total summer budget. The tool displays committed spend (registered programs), potential spend (if all considering programs are enrolled), and remaining budget. No multi-user; no spouse sharing in v1.

---

## Why This, Why Now

Registration season for summer 2026 programs is already underway. Parents are in the middle of this problem right now. The tool does not need to solve the full planning workflow to be immediately useful — it needs to solve the most acute moment: being ready to register. Every week we wait is a week parents are managing this with Google Calendar and stress.

If we don't solve the enrollment moment, we are building a better to-do list. That is not a defensible product.

---

## Out of Scope

- **Program sharing** — a send-a-friend feature is planned but is a separate feature brief. Not part of the core loop.
- **URL auto-extraction** — pasting a URL to auto-fill program details is useful input assistance but is not required for v1 to work.
- **Waitlist management** — waitlisted programs can be tracked with a status label. Managing waitlist position, notifications, or conversion is deferred.
- **Balanced schedule tuning** — the coverage view answers "is this week filled?" not "is this week well-composed?" Activity-type balancing (active vs. brainy vs. arts) is a v2 feature.
- **Multi-child views** — the tool tracks one child at a time in v1. Switching between children is supported; combined views are not.
- **Multi-user / spouse sharing** — single-user in v1.
- **Program discovery** — parents add programs they already know about.

---

## Success Looks Like

1. A parent can add five programs with all relevant dates and links in under 10 minutes, and the coverage view immediately shows which weeks are filled and which are gaps.
2. When a registration deadline is within 14 days, the Enrollment Prep Card surfaces the correct registration link and checklist without the parent having to search for it.
3. A parent who sets a summer budget can see at a glance whether their current and potential commitments are within budget.

---

## Biggest Unknowns

1. **Will parents add the registration URL when logging a program?** The Enrollment Prep Card loses its core value if parents skip this field. We need to observe whether parents think to add the URL at program-entry time — potentially months before the deadline — or whether they add it only when the deadline is close. If they skip it, the checklist is still useful, but the direct link (the most valuable element) is missing.

2. **Does the three-item readiness checklist match how parents actually prepare?** The checklist (logged in, payment ready, session selected) is hypothetical. We should validate whether these are the right items, whether parents find them patronizing or genuinely useful, and whether they check them off or ignore them.
