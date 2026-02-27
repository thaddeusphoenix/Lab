# Research Scout

A CLI-based AI agent that takes a research question, plans a search strategy, calls tools autonomously, and writes a structured report to disk.

**Phase: Discover → Build**
**Brief:** [`briefs/project-feature-brief.md`](briefs/project-feature-brief.md)

## Why This Exists

Research Scout is a learning project. The goal is not the agent — it is the team's understanding of how to build agents. Every pattern in the codebase (tool definition, the agentic loop, tool dispatch, synthesis) is intentionally visible. No frameworks. Bare metal Anthropic SDK so the seams show.

## Stack

- Python 3.11+
- Anthropic SDK (direct API — no LangChain, no LangGraph)
- Model: `claude-sonnet-4-6`
- Search: Tavily API
- Output: Markdown files written to disk

## What an Agent Run Looks Like

```
$ python scout.py "What are the most common failure modes in AI agent systems?"

Planning research strategy...
→ search("AI agent failure modes")
→ fetch_page("https://...")
→ search("agentic loop reliability 2025")
→ fetch_page("https://...")
→ write_report("agent-failure-modes.md")

Report written to: reports/agent-failure-modes.md
```

## Patterns This Project Teaches

| Pattern | Where to see it |
|---|---|
| Tool definition | `tools.py` — each tool is a Python function + JSON schema |
| Agentic loop | `scout.py` — the `while` loop that runs until the agent calls `write_report` |
| Tool dispatch | `scout.py` — mapping tool names to function calls |
| Result synthesis | The model's final tool call — turning raw search results into a structured report |
| Prompt design | `scout.py` — the system prompt that shapes agent behavior |
