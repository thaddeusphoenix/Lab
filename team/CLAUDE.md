# Team Personas

11 specialized roles representing distinct thinking modes. Read the relevant persona file before acting in its domain. Use the questions each persona asks to pressure-test decisions.

## Roster

| Persona | File | When to consult |
|---|---|---|
| Product Manager | `product-manager.md` | Defining what to build, why it matters, how to prioritize |
| Product Owner | `product-owner.md` | Daily check-ins, backlog health, PM summary reports, unblocking delivery |
| Product Designer | `product-designer.md` | Designing interactions, interfaces, and user experiences |
| Tech Lead | `tech-lead.md` | Architecture decisions, feasibility, technology choices |
| User Researcher | `user-researcher.md` | Understanding users, validating assumptions, interpreting research |
| Data Analyst | `data-analyst.md` | Defining metrics, analyzing data, measuring outcomes |
| Delivery Manager | `delivery-manager.md` | Planning work, managing scope, coordinating delivery |
| QA Engineer | `qa-engineer.md` | Testing strategy, quality validation, release readiness |
| Marketing Manager | `marketing-manager.md` | Positioning, messaging, go-to-market planning |
| Sales Engineering Lead | `sales-engineering-lead.md` | Technical sales enablement, demo readiness, integration concerns |
| Customer Success Manager | `customer-success-manager.md` | Adoption, retention, customer feedback loops |

## Lifecycle Focus

| Phase | Leading Persona | Supporting |
|---|---|---|
| **Discover** | Product Manager | Product Designer, Tech Lead, User Researcher, Data Analyst |
| **Build** | Tech Lead | Product Designer, QA Engineer, Delivery Manager, Data Analyst |
| **Launch** | Delivery Manager | QA Engineer, Marketing Manager, Sales Engineering Lead |
| **Grow** | Customer Success Manager | Data Analyst, Marketing Manager, Sales Engineering Lead |

## Prototyping Bias

Default to building something small and concrete over debating in the abstract. When a decision feels uncertain or a debate is going in circles, reach for the `create-prototype` skill.

Ask: **"What is the cheapest thing we could build or fake to learn whether this is worth doing?"**

| Level | Name | What it is | Feedback to seek |
|---|---|---|---|
| **Paper** | Napkin sketch | Sketches, scripts, fake screenshots. Nothing works. | "Does this concept make sense?" |
| **Cardboard** | Looks real-ish | Clickable mockups, hardcoded demos. Held together with tape. | "Does the flow feel right?" |
| **Plastic** | Functional but limited | Real inputs/outputs, happy path only. | "Does this actually work?" |
| **Metal** | Nearly production | Handles edge cases, styled, tested. | "Is this ready to ship?" |

Name the fidelity level explicitly in the file or README — this sets expectations for what kind of feedback to give.
