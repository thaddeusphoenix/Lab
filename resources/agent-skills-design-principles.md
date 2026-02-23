# Principles for Designing Agent Skills

Source: [3 Principles for Designing Agent Skills](https://engineering.block.xyz/blog/3-principles-for-designing-agent-skills) — Angie Jones, AI Enablement Lead at Block Engineering (February 15, 2026)

## What Are Agent Skills?

Skills are reusable knowledge packages that transform documentation into executable workflows. They are an open standard supported by Claude Code, Goose, GitHub Copilot, and other AI coding tools. A skill is a folder with a `SKILL.md` file containing instructions an agent can discover and load on demand. Skills can include supporting files like scripts, templates, and configuration files, making them portable across platforms.

The key shift: documentation goes from something you read to something your agent can execute.

## The Three Principles

### 1. Know What the Agent Should NOT Decide

Lock down anything requiring consistency. Use scripts with deterministic, binary outputs — pass/fail checks, fixed point values, hardcoded CLI commands, SQL queries, and naming conventions — rather than letting the LLM reason about them.

If a result must be consistent across every user who triggers the skill, don't let the agent compute it. Compute it yourself and tell the agent to treat it as immutable.

### 2. Know What the Agent SHOULD Decide

Agents excel at interpretation, action, and conversation. Delegate to the agent:

- **Interpretation** — explaining why something failed in context-specific language
- **Action** — generating tailored content by reading actual code or context
- **Conversation** — prioritizing recommendations based on stated constraints

This creates a two-zone architecture: scripts handle deterministic execution; agents handle reasoning and context-aware work.

### 3. Write a Constitution, Not a Suggestion

LLMs naturally soften results and add helpful caveats that undermine intended outcomes. A `SKILL.md` should include explicit, non-negotiable rules about output format, score handling, and check immutability — not loose guidance the agent can reinterpret.

The more specific the `SKILL.md`, the less the agent has to guess, and the more consistent the experience is for every user who triggers that skill.

## Bonus: Design for the Arc

Diagnostic and investigation skills benefit from creating conversation arcs. Rather than stopping at output, skills should enable follow-up actions. A report becomes context for the agent to help draft missing files, explain findings, or take next steps — turning diagnosis into action within a single session.

## Underlying Principle

Play to each system's strengths. Scripts for determinism. Agents for reasoning. The skill design determines which is which.
