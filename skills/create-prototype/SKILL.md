---
name: create-prototype
description: Use when a decision is uncertain, a debate is going in circles, or an assumption needs to be tested before building the real thing. Prototypes can be code, but also sketches, fake screenshots, written flows, or Wizard-of-Oz simulations.
---

## Quick Start

Ask: **"What is the cheapest thing we could build or fake to learn whether this is worth doing?"** Name the fidelity level before you start building. Add the prototype to `discover/` and link it from the project README.

## Fidelity Levels

| Level | Name | Build when |
|---|---|---|
| **Paper** | Napkin sketch | You need to communicate an idea, not test it |
| **Cardboard** | Looks real-ish | You need to test a flow or interaction |
| **Plastic** | Functional but limited | You need to validate the core mechanic works |
| **Metal** | Nearly production | You need to confirm readiness to ship |

Always name the fidelity level explicitly in the file or README. This sets expectations and prevents over-investing in feedback on the wrong things.

## Workflow

### 1. Gather — Identify the assumption to test

- What decision are you trying to make?
- What would prove this is right? What would prove it's wrong?
- Who needs to see this prototype and give feedback?

### 2. Explore — Look at what exists

- Check `discover/` for prior prototypes in the project
- Review the relevant user persona to ground the prototype in real behavior
- Consult `team/product-designer.md` for interaction patterns

### 3. Discuss — Choose the right fidelity

Choose the lowest fidelity that can answer the question:
- If testing a concept — use Paper
- If testing a flow or interaction — use Cardboard
- If testing whether the core mechanic actually works — use Plastic
- If testing readiness to ship — use Metal

### 4. Plan — Design for the question, not the product

- Scope the prototype to the single question it needs to answer
- Hard-code everything you can; only build what's necessary to test the assumption
- Define what feedback you want before you show it to anyone

### 5. Document — Label and link

- Add the prototype to `discover/` with a descriptive filename (e.g., `messages-prototype.html`)
- Label it with fidelity level in the file header or README entry
- Add it to the project README under a Prototypes table with: artifact, fidelity, description
- Note what was learned and whether the assumption was validated

## Checklist

- [ ] Assumption to test is clearly stated
- [ ] Fidelity level chosen and named explicitly
- [ ] Prototype scoped to the question, not the full product
- [ ] Added to `discover/` with descriptive filename
- [ ] Linked from project README with fidelity label
- [ ] Feedback sought matches the fidelity level
