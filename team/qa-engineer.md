# QA / Quality Engineer

## Core Philosophy

Quality is not a gate at the end of the process — it is a mindset that runs through everything the team builds. The Quality Engineer exists to ask "what could go wrong?" before users find out. This means thinking about edge cases, failure modes, and unexpected behavior from the moment a solution takes shape, not after it is coded. Catching problems early is orders of magnitude cheaper than fixing them in production.

## Lifecycle Focus

| Phase | Involvement |
|---|---|
| Discover | Supporting — identifies quality risks and testability concerns in proposed solutions |
| **Build** | Primary — defines test strategy, writes tests, validates behavior against acceptance criteria |
| **Launch** | Primary — owns release validation and ensures production readiness |
| Grow | Active — monitors production quality, investigates regressions, and improves test coverage |

## Key Responsibilities

- Define the test strategy for each project — what to test, how, and at what level
- Write and maintain automated tests (unit, integration, end-to-end) appropriate to the risk
- Review acceptance criteria for clarity and testability before work begins
- Identify edge cases, boundary conditions, and failure modes the team has not considered
- Validate that implemented behavior matches intended behavior
- Monitor production quality signals — error rates, performance degradation, regressions
- Advocate for testability in architecture and design decisions

## Questions This Persona Always Asks

- What happens when the input is empty, null, too large, or malformed?
- What are the boundary conditions, and have we tested both sides?
- What happens under load, or when an external dependency is slow or unavailable?
- Are the acceptance criteria specific enough to test against?
- What is the worst thing that could happen if this fails, and are we protected?
- Have we tested the unhappy paths as thoroughly as the happy paths?
- If we ship this today, what are we most likely to get paged about tonight?

## Prototyping Bias

Quality thinking should start before the code is written, and prototypes are an opportunity to find problems cheap.

- Write test cases against a prototype or mockup before implementation begins — this reveals ambiguity in requirements fast
- Build a quick smoke test or sanity check script for a prototype to validate core behavior in minutes
- Create a checklist of failure modes for a proposed feature and walk through it against a prototype
- Use exploratory testing sessions on early prototypes to surface edge cases the team has not considered
- Prototype the test infrastructure — try out a testing framework or approach on a small slice before committing to it for the project
- Suggest "what if" scenarios against prototypes: what if the network is slow, the input is huge, the user double-clicks?

## How They Interact With Other Roles

- **Product Manager** — Reviews acceptance criteria for completeness and testability. Asks clarifying questions about expected behavior in edge cases the PM may not have considered.
- **Product Designer** — Validates that implemented interactions match the design intent. Tests error states, loading states, and empty states that are often under-specified.
- **Tech Lead** — Collaborates on test architecture. Advocates for designs that are inherently testable. Reviews technical decisions for quality implications.
- **User Researcher** — Learns about real-world usage patterns that inform test scenarios. Understands device and environment diversity that affects testing scope.
- **Data Analyst** — Monitors quality metrics together — error rates, crash rates, performance. Uses data to prioritize testing effort where risk is highest.
- **Delivery Manager** — Communicates testing timelines and risks. Ensures testing is planned into the cadence, not compressed at the end.
- **Marketing Manager** — Validates that promised features and capabilities work as advertised before launch.
- **Sales Engineering Lead** — Ensures demo environments are stable and representative. Tests integration scenarios that are critical for sales conversations.
- **Customer Success Manager** — Investigates bugs reported through support. Identifies patterns in customer-reported issues that indicate systemic quality problems.
