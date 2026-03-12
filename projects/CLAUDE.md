# Projects

One directory per project. All work lives in `projects/<name>/`.

## Project Structure

```
projects/<name>/
├── README.md                           # Phase, brief links, problem/solution summary
├── briefs/                             # Discovery documents and build loop inputs
│   ├── strategic-initiative-brief.md   # Initiative-level alignment doc
│   ├── prd.md                          # Product requirements
│   ├── <feature-name>.md               # Feature brief (Writer input)
│   └── <feature-name>-scenarios.md     # Acceptance scenarios (Tester input only)
├── discover/                           # Prototypes, personas, research artifacts
├── build/                              # Build loop output artifacts
└── reports/                            # Research observations, daily reports, exports
```

## Phases

| Phase | Leading Persona | Exit criteria |
|---|---|---|
| **Discover** | Product Manager | Clear problem statement + evidence + viable solution direction |
| **Build** | Tech Lead | Working software meeting acceptance criteria |
| **Launch** | Delivery Manager | Production-ready, messaging clear, support prepared |
| **Grow** | Customer Success Manager | Measurable adoption, feedback feeding next cycle |

## Status

Project README always shows current phase. Brief status flows: Draft → Aligned → Active → Shipped → Closed.
