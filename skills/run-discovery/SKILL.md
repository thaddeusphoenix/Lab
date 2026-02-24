---
name: run-discovery
description: Use when starting a new project or moving an existing project through the Discover phase. Covers problem definition, user research, opportunity assessment, and setting exit criteria before committing to Build.
---

## Quick Start

Create `projects/<name>/` with a `briefs/` and `discover/` subdirectory. Write the Strategic Initiative Brief first. Do not start Build until exit criteria are met.

## Workflow

### 1. Gather — Frame the opportunity

- Write or update the Strategic Initiative Brief (`briefs/strategic-initiative-brief.md`)
- Define the user and the pain in one paragraph before writing anything else
- Identify what evidence exists and what evidence is missing

### 2. Explore — Understand the user

- Write at least one user persona in `discover/` (see `templates/` for structure)
- For each persona, define: who they are, how they work, what they need, what success looks like
- Consult `team/user-researcher.md` for research methods and interview questions

### 3. Discuss — Stress-test with the team

Bring in personas based on the phase:
- **Product Manager** — Is this the right problem? Is now the right time?
- **Tech Lead** — Is the proposed solution feasible with our constraints?
- **Product Designer** — Is there a usable path from the user's current behavior to this tool?
- **Data Analyst** — How will we know if this worked? Can we measure it?

### 4. Plan — Define the first feature

- Write a Project Feature Brief for the smallest thing worth building first
- Confirm the brief passes the Four Risks Audit
- Set clear, measurable exit criteria for Discover

### 5. Document — Finalize before Build

- Update the Strategic Initiative Brief with any pivots or scope changes
- Create a prototype if any assumption is uncertain — see the `create-prototype` skill
- Confirm exit criteria are met: clear problem statement, evidence it's real, confidence a solution exists
- Move status on all briefs from `Draft` to `Aligned`

## Discover Exit Criteria

Do not proceed to Build until all three are true:

1. A clear problem statement that names the user, the pain, and the evidence
2. At least one user persona written from research or direct observation
3. A Project Feature Brief with an explicit "Out of Scope" and at least one testable unknown

## Checklist

- [ ] Strategic Initiative Brief written and linked from project README
- [ ] At least one user persona in `discover/`
- [ ] Four Risks Audit completed
- [ ] First Feature Brief written with exit criteria
- [ ] Prototype created for any assumption that is uncertain
- [ ] All brief statuses set to `Aligned`
- [ ] Team consensus that problem is real and solution direction is viable
