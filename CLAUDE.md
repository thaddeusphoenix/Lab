# lab

This is a monorepo where coding projects are built using a team-based product development model. Each project lives in `projects/` and is developed through a structured lifecycle with input from specialized team personas.

## Team Personas

The `team/` directory contains persona files that represent distinct thinking modes. Each persona defines a role, its core philosophy, lifecycle focus, key responsibilities, and the questions it always asks.

When working in this repo, consult the relevant persona files to inform your thinking at the right moments:

| Persona | File | When to consult |
|---|---|---|
| Product Manager | `team/product-manager.md` | Defining what to build, why it matters, and how to prioritize |
| Product Owner | `team/product-owner.md` | Daily team check-ins, backlog health, PM summary reports, and unblocking delivery |
| Product Designer | `team/product-designer.md` | Designing interactions, interfaces, and user experiences |
| Tech Lead | `team/tech-lead.md` | Making architecture decisions, assessing feasibility, choosing technologies |
| User Researcher | `team/user-researcher.md` | Understanding users, validating assumptions, interpreting research |
| Data Analyst | `team/data-analyst.md` | Defining metrics, analyzing data, measuring outcomes |
| Delivery Manager | `team/delivery-manager.md` | Planning work, managing scope, coordinating delivery |
| QA Engineer | `team/qa-engineer.md` | Testing strategy, quality validation, release readiness |
| Marketing Manager | `team/marketing-manager.md` | Positioning, messaging, go-to-market planning |
| Sales Engineering Lead | `team/sales-engineering-lead.md` | Technical sales enablement, demo readiness, integration concerns |
| Customer Success Manager | `team/customer-success-manager.md` | Adoption, retention, customer feedback loops |

Read the persona file before acting in its domain. Use the questions each persona asks to pressure-test decisions.

## Prototyping Bias

Default to building something small and concrete over debating in the abstract. Every team member — regardless of role — should look for ways to prototype quickly to validate assumptions or get feedback. A prototype can be code, but it can also be a sketch, a fake screenshot, a spreadsheet model, a landing page, a five-minute user test, or a Wizard-of-Oz simulation. The goal is to learn fast, not to build perfectly.

When in doubt, ask: **"What is the cheapest thing we could build or fake to learn whether this is worth doing?"**

Each persona file includes a section on prototyping approaches specific to that role's domain. Consult it whenever a decision feels uncertain or a debate is going in circles — the answer is usually "build something and find out."

### Prototype Fidelity Levels

Every prototype has a fidelity level. Name it explicitly so the team knows what they're looking at and what kind of feedback to give.

| Level | Name | What it is | Feedback to seek |
|---|---|---|---|
| **Paper** | Napkin sketch | Very fake and flimsy. Sketches, scripts, fake screenshots, written flows. Nothing works — it just communicates an idea. | "Does this concept make sense? Are we solving the right problem?" |
| **Cardboard** | Looks real-ish | Somewhat functional. Clickable mockups, simulated workflows, hardcoded demos. Feels like the thing but is held together with tape. | "Does the flow feel right? What's confusing? What's missing?" |
| **Plastic** | Functional but limited | Works in a real sense but scoped to a narrow slice. Real inputs, real outputs, but only for the happy path or a single use case. | "Does this actually work? Is the core interaction viable?" |
| **Metal** | Nearly production | Fully functional, handles edge cases, styled, tested. Just short of shipping — may lack scale, polish, or integrations. | "Is this ready? What's blocking launch?" |

When creating a prototype, label it with its fidelity level (e.g., "Cardboard prototype" in the file or README). This sets expectations and prevents over-investing in feedback on the wrong things.

## Workflow: Discover-Build-Launch-Grow

Every project moves through four phases. Each phase has a purpose and a set of personas that lead or contribute.

### Discover

Define the problem, research users, and assess feasibility before committing to build.

- **What happens:** Problem definition, user research, opportunity assessment, technical feasibility, data analysis of the landscape
- **Key personas:** Product Manager (lead), Product Designer, Tech Lead, User Researcher, Data Analyst
- **Exit criteria:** A clear problem statement, evidence that the problem is real, and confidence that a viable solution exists

### Build

Implement, test, and iterate toward a solution that meets the defined outcomes.

- **What happens:** Architecture decisions, implementation, design refinement, testing, scope management
- **Key personas:** Tech Lead (lead), Product Designer, QA Engineer, Delivery Manager, Data Analyst
- **Exit criteria:** Working software that meets acceptance criteria with appropriate test coverage

### Launch

Prepare for release and ensure everything is ready for users.

- **What happens:** Release validation, go-to-market readiness, positioning, documentation, demo preparation
- **Key personas:** Delivery Manager (lead), QA Engineer, Marketing Manager, Sales Engineering Lead
- **Exit criteria:** Software is production-ready, messaging is clear, and support channels are prepared

### Grow

Drive adoption, monitor health, and feed learnings back into the next cycle.

- **What happens:** Adoption tracking, retention analysis, customer feedback collection, iteration planning
- **Key personas:** Customer Success Manager (lead), Data Analyst, Marketing Manager, Sales Engineering Lead
- **Exit criteria:** Measurable adoption, feedback incorporated into the next Discover phase

## Discovery Documents

Every initiative or project begins with a written brief before any build work starts. These are ~1-page alignment documents — a dashboard for quickly orienting any team member or stakeholder on the problem, the opportunity, and the rationale for building.

There are two types. Use whichever fits the scope:

| Document | Use when | Focus | Template |
|---|---|---|---|
| **Strategic Initiative Brief** | Large, multi-feature initiative with a meaningful market bet | Market opportunity, why now, why us | `templates/strategic-initiative-brief.md` |
| **Project Feature Brief** | A single feature or smaller-scoped project | Problem to be solved, proposed solution, success criteria | `templates/project-feature-brief.md` |

A Project Feature Brief can reference a parent Strategic Initiative Brief. A Strategic Initiative Brief links out to its child Feature Briefs as they are created.

Both documents live in the project directory, typically at `projects/<project-name>/briefs/`. Status progresses Draft → Aligned → Active as the team validates the direction.

The brief is the first artifact created in Discover and the last thing updated before moving to Build. If the team cannot align on the brief, they are not ready to build.

## Skills

Skills are modular, reusable workflows for recurring actions in the lab. Each skill lives in its own directory under `skills/` as a `SKILL.md` file.

A skill is not a checklist — it is a pipeline with distinct stages. Every skill follows the same five-stage structure: **Gather → Explore → Discuss → Plan → Document.** Each stage has a purpose and a set of questions or actions. The goal is to move quickly and purposefully, not to be exhaustive.

| Skill | File | Use when |
|---|---|---|
| Write a Brief | `skills/write-a-brief/SKILL.md` | Starting a project or feature and need to capture problem + direction before building |
| Run Discovery | `skills/run-discovery/SKILL.md` | Opening a new project or moving through the Discover phase |
| Create a Prototype | `skills/create-prototype/SKILL.md` | A decision is uncertain or an assumption needs to be tested before building |

### Skill File Format

Each `SKILL.md` starts with YAML frontmatter:

```yaml
---
name: skill-name
description: Use when [trigger condition]. [One sentence on what it produces.]
---
```

The description must be trigger-oriented — it tells the reader *when* to reach for the skill, not just *what* it is. Content follows: Quick Start → Workflow (Gather → Explore → Discuss → Plan → Document) → Checklist. Keep it under 100 lines.

When a decision feels uncertain or a debate is going in circles, look for a skill before writing more prose.

## Repo Conventions

- **Monorepo layout:** `team/` for persona definitions, `projects/` for individual project directories, `templates/` for document templates, `skills/` for reusable workflow skills
- **File naming:** kebab-case for all files and directories (e.g., `sales-engineering-lead.md`, `my-project/`)
- **Commits:** Use concise commit messages that focus on the "why" rather than the "what"
