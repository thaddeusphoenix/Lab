---
name: write-a-brief
description: Use when starting a new project or feature and you need to capture the problem, opportunity, and solution direction before any build work begins. Use a Strategic Initiative Brief for large, multi-feature market bets. Use a Project Feature Brief for a single feature or scoped problem.
---

## Quick Start

Identify whether this is an initiative (use `templates/strategic-initiative-brief.md`) or a single feature (use `templates/project-feature-brief.md`). Create the file at `projects/<name>/briefs/`.

## Workflow

### 1. Gather — Understand the scope

- Is this a market bet or a feature problem?
- Who is the user and what is the pain?
- What evidence exists that the problem is real?

### 2. Explore — Research before writing

- Consult `team/product-manager.md` for the PM lens
- Consult `team/user-researcher.md` if user behavior is unclear
- Look at any existing briefs in the project's `briefs/` directory for context

### 3. Discuss — Pressure-test the direction

Run the brief through the Four Risks Audit before writing:

| Risk | Question |
|---|---|
| Value | Does solving this actually matter to the user? |
| Usability | Can the user understand and use this without training? |
| Feasibility | Can we build it with what we have? |
| Business Viability | Does this create a sustainable value exchange? |

### 4. Plan — Draft the brief

Fill in the template top-to-bottom. Every section matters:
- **One-line summary** — forces clarity; write this last
- **The Problem** — User / Pain / Evidence, not the solution
- **Out of Scope** — as important as what's in scope
- **Biggest Unknowns** — what must be true for this to work

### 5. Document — Link and set status

- Set status to `Draft`
- If a Feature Brief, add `Parent Initiative` link
- If a Strategic Initiative Brief, link to child Feature Briefs as they are written
- Update the project's `README.md` to reference the brief

## Checklist

- [ ] Correct template used for scope (initiative vs feature)
- [ ] File created at `projects/<name>/briefs/`
- [ ] Four Risks Audit considered
- [ ] "Out of Scope" section is explicit
- [ ] At least one "Biggest Unknown" that would invalidate the direction
- [ ] Status set to `Draft`
- [ ] README updated with link to brief
