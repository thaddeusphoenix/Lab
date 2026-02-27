# Project Feature Brief: Research Scout

> A CLI-based AI agent that teaches the lab how to build agents by doing the most canonical thing an agent does: take a question, plan a research strategy, call tools, and write a report.

**Status:** Draft
**Owner:** Wintermute (PM)
**Last updated:** 2026-02-27
**Parent Initiative:** _(none — standalone learning project)_

---

## The Problem

**User:** The lab team
**Pain:** No hands-on experience building AI agents. The team cannot confidently architect, debug, or extend agent-based systems. As agentic AI becomes a core software capability, this is a growing gap.
**Evidence:** Stated directly. No existing agent projects in the lab. Future projects (Workbook Trust Engine, Camp Planner recommendations) will want this capability, but the team would be building on speculation rather than understanding.

## The Proposed Solution

Build a CLI-based AI agent using the Anthropic SDK — no frameworks, no magic — that accepts a research question, autonomously plans a search strategy, executes tool calls (web search, page fetch), and writes a structured report to disk. The codebase is intentionally small and readable. The artifact is the learning, not the product. Every pattern used — tool definition, the agentic loop, tool dispatch, result synthesis — should be visible in the code and explainable by anyone on the team after reading it.

## Why This, Why Now

Agentic AI is moving from experimental to expected. The lab is building products (Workbook, Camp Planner) that will want AI agent capabilities — but building on top of something the team doesn't understand is a compounding liability. A standalone learning project lets the team encounter the real patterns — and the real failure modes — without the pressure of a live product. Research Scout is the smallest vehicle that requires genuine agentic behavior: the agent must plan, act, observe, and revise, not just respond.

## Out of Scope

- Multi-agent orchestration (one agent, one loop — by design)
- Persistent memory or session state across runs
- Web UI or API surface — CLI only
- Production-grade error handling, retries, or logging infrastructure
- Deployment or hosting

## Success Looks Like

1. A working agent that takes a research question via CLI, calls tools autonomously, and writes a structured report to disk — without the user directing each step.
2. Every team member can read the agent code and accurately explain how the agentic loop works: where the model decides, how tools are dispatched, and how results feed back into the next step.
3. At least one documented "unexpected agent behavior" per run — moments where the agent surprises us. These are the real curriculum.

## Biggest Unknowns

1. **Search API selection:** Which search API (Tavily, Brave, Serper) gives the right balance of setup simplicity and result quality for a learning project? High setup friction hurts the learning goal.
2. **Scaffolding level:** How much structure is right? Too little and the agent fails trivially on bad search results. Too much scaffolding hides the patterns we're trying to teach.
