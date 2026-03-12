# Templates

Document templates for the lab's two-track documentation system. Use whichever fits the scope.

## Template Reference

| Template | Use when | Status flow |
|---|---|---|
| `strategic-initiative-brief.md` | Large, multi-feature market bet | Draft → Aligned → Active → Closed |
| `project-feature-brief.md` | Single feature or scoped problem | Draft → Aligned → In Build → Shipped → Closed |
| `acceptance-scenarios.md` | Tester's rubric for the build loop — created when brief reaches Aligned | — |
| `prd.md` | Full product requirements — 7 sections, AI-specific sections skippable for non-AI products | Draft → Aligned → Active |

## Document Hierarchy

```
PRD  ─────────────────────────────────── project-level requirements (upstream)
  └── Feature Brief  ─────────────────── Writer input (build loop only)
        └── Acceptance Scenarios  ────── Tester input only (never in brief)
```

PRD governs. If a Feature Brief contradicts the PRD, the PRD wins.

## Discovery Documents

Every initiative begins with a brief before any build work starts.

- **Strategic Initiative Brief** — Large market bet. Covers opportunity, why now, why us. Lives at `projects/<name>/briefs/strategic-initiative-brief.md`.
- **Project Feature Brief** — Single feature. Covers problem, proposed solution, success criteria. Lives at `projects/<name>/briefs/<feature-name>.md`.

A Feature Brief can reference a parent Strategic Initiative Brief. A Strategic Initiative Brief links out to its child Feature Briefs as they are created.

The brief is the first artifact created in Discover and the last thing updated before Build. If the team cannot align on the brief, they are not ready to build.

## The Firewall

The acceptance scenarios file is the Tester's rubric — it is never the Writer's input.

- Brief and scenarios are always **two separate files**
- Writer reads only `[feature-name].md`
- Tester reads `[feature-name].md` + `[feature-name]-scenarios.md` + the output
- Merging them into one file invalidates any build loop run
