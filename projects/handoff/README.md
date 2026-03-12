# Handoff

An offline-first, voice-activated field execution tool that lets subcontractors log progress by talking, while an agent reconciles updates against the master schedule in real time — giving Site Superintendents visibility without the chase.

**Phase: Discover → Build**
**Strategic Brief:** [`briefs/strategic-initiative-brief.md`](briefs/strategic-initiative-brief.md)
**Feature Brief:** [`briefs/schedule-update-flow.md`](briefs/schedule-update-flow.md)

## Problem

On hyperscale construction sites, "gaps between trades" during handoffs account for an estimated 65% of major project delays. Site Superintendents spend a disproportionate amount of their day chasing subcontractors for status updates rather than managing the site. Existing scheduling tools (Procore, Primavera, MS Project) were built for the office — not the field.

## Solution

A lightweight voice logging layer that sits between field crews and the master schedule. Subcontractors speak a status update into their phone; an agent transcribes, interprets, and maps it to the schedule in real time. The Superintendent sees a live reconciliation view — what was planned, what has been logged, where gaps are forming — without asking anyone.

## Four Risks Audit

| Risk | Level | Notes |
|---|---|---|
| **Value** | High | Schedule compression is directly measurable and high-stakes for GCs and owners |
| **Usability** | Medium | Voice must work in loud environments; offline sync must be invisible |
| **Feasibility** | Medium | Voice transcription is ready; schedule reconciliation requires format access (P6, MS Project) |
| **Business Viability** | Unknown | Superintendent is the user; buying motion runs through GC operations leadership |
