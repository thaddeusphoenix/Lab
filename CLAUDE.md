# lab

A monorepo for building products using a team-based, AI-assisted model. Projects live in `projects/` and move through four phases: **Discover → Build → Launch → Grow.**

## Directories

| Directory | What's here |
|---|---|
| `team/` | 11 team persona files — read before acting in a role's domain |
| `projects/` | One directory per project. All work lives here. |
| `templates/` | Document templates for briefs, PRDs, and acceptance scenarios |
| `knowledge/` | Reference material on AI product development |
| `.claude/skills/` | Reusable workflow skills — 4 skills, invoke by name |

## Skills

| Skill | When to use |
|---|---|
| `write-a-brief` | Starting a project or feature — needs problem + direction before building |
| `run-discovery` | Opening a new project or moving through Discover phase |
| `create-prototype` | Decision is uncertain or assumption needs testing before building |
| `ai-build-loop` | Brief is Aligned, scenarios are complete — ready to execute the build loop |

## AI Build Loop

Every build in this lab runs through this loop — no exceptions.

```
[Human] → brief + scenarios
[Writer] → reads brief only → produces output
[Tester] → reads brief + scenarios + output → PASS/FAIL + spec_amendment
PASS → human reviews → ships
FAIL → amendment appended to brief → loop (max 5 runs)
```

**⚠ The Firewall:** The acceptance scenarios file must never be passed to the Writer. Brief and scenarios are always separate files. Violation invalidates the run.

See `.claude/skills/ai-build-loop/SKILL.md` for full protocol.

## Conventions

- **Naming:** kebab-case for all files and directories
- **Briefs:** `projects/<name>/briefs/` — brief and scenarios always as separate files
- **Prototypes:** `projects/<name>/discover/` — always label fidelity level (Paper / Cardboard / Plastic / Metal)
- **Commits:** Focus on "why" not "what"
