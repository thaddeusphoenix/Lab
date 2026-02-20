# Lab

This is a monorepo where coding projects are built using a team-based product development model. Each project lives in `projects/` and is developed through a structured lifecycle with input from specialized team personas.

## Team Personas

The `team/` directory contains persona files that represent distinct thinking modes. Each persona defines a role, its core philosophy, lifecycle focus, key responsibilities, and the questions it always asks.

When working in this repo, consult the relevant persona files to inform your thinking at the right moments:

| Persona | File | When to consult |
|---|---|---|
| Product Manager | `team/product-manager.md` | Defining what to build, why it matters, and how to prioritize |
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

## Repo Conventions

- **Monorepo layout:** `team/` for persona definitions, `projects/` for individual project directories
- **File naming:** kebab-case for all files and directories (e.g., `sales-engineering-lead.md`, `my-project/`)
- **Commits:** Use concise commit messages that focus on the "why" rather than the "what"
