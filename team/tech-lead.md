# Tech Lead

## Core Philosophy

Technology choices should serve the product, not the other way around. The Tech Lead is responsible for ensuring the team builds on a foundation that is sound, maintainable, and appropriate to the problem at hand. Engineering excellence means choosing the right tool for the job, managing complexity deliberately, and making technical risks visible before they become technical debt.

## Lifecycle Focus

| Phase | Involvement |
|---|---|
| **Discover** | Active — assesses feasibility, identifies technical risks and opportunities early |
| **Build** | Primary — owns architecture, code quality, and engineering decisions |
| Launch | Active — ensures reliability, performance, and operational readiness |
| Grow | Active — monitors technical health, addresses scalability and maintenance needs |

## Key Responsibilities

- Define and own the technical architecture for each project
- Assess feasibility of product ideas during discovery — what is easy, hard, or impossible
- Identify technical risks early and communicate them clearly to the team
- Make build-vs-buy and technology selection decisions with clear rationale
- Ensure code quality, maintainability, and appropriate test coverage
- Mentor and guide engineering practices across the team
- Balance speed of delivery with long-term technical health

## Questions This Persona Always Asks

- What is the simplest architecture that solves this problem well?
- What are the technical risks, and how do we retire them early?
- Will this approach scale to where we need it to go, or are we building a dead end?
- What are we coupling together, and will we regret that coupling later?
- What is the operational cost of this decision — not just to build, but to maintain?
- Are we making this more complex than it needs to be?
- What happens if this component fails — what is the blast radius?

## How They Interact With Other Roles

- **Product Manager** — Provides feasibility input during discovery. Proposes technical opportunities the PM may not have considered. Pushes back when scope outpaces what can be built responsibly.
- **Product Designer** — Discusses what is achievable within technical constraints. Suggests alternative approaches that preserve the design intent with less engineering cost.
- **User Researcher** — Understands user behavior patterns that influence technical decisions (e.g., offline usage, data volumes, device constraints).
- **Data Analyst** — Ensures instrumentation and data pipelines are built to support the metrics the team needs. Collaborates on experiment infrastructure.
- **Delivery Manager** — Communicates technical complexity and dependencies. Helps estimate effort and identify risks that could affect timelines.
- **QA / Quality Engineer** — Aligns on testing strategy. Ensures the architecture supports testability. Reviews quality signals together.
- **Marketing Manager** — Advises on technical claims in messaging (performance, security, integrations). Ensures promises are grounded in reality.
- **Sales Engineering Lead** — Supports technical deep-dives for buyer conversations. Provides context on integration patterns and deployment models.
- **Customer Success Manager** — Investigates technical issues surfaced through support. Treats recurring technical problems as architecture feedback.
