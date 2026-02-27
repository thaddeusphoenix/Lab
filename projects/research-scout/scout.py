"""
Research Scout — a minimal AI agent.

This file contains the agentic loop: the core pattern where a model decides
what to do, calls tools, observes results, and decides again — until it's done.

Run it:
    python scout.py "What are the most common failure modes in AI agent systems?"
"""

import sys
import anthropic
from dotenv import load_dotenv

from tools import TOOL_SCHEMAS, TOOL_DISPATCH

load_dotenv()

SYSTEM_PROMPT = """You are a research agent. Given a research question, you work autonomously to find and synthesize information from the web.

Your process:
1. Plan — decide what search queries will best cover the question from multiple angles
2. Search — use the search tool to find relevant sources
3. Read — use fetch_page to read the most useful sources in full when snippets aren't enough
4. Synthesize — when you have enough, call write_report to produce a structured report

Rules:
- Run at least 2 searches before writing the report
- The report must have these sections: Summary, Key Findings, Sources
- Filename must be descriptive, kebab-case, ending in .md
- Call write_report exactly once, at the end
"""


def run(question: str) -> None:
    client = anthropic.Anthropic()

    # The message history. This is the agent's working memory for the session.
    messages = [{"role": "user", "content": question}]

    print(f"\nQuestion: {question}\n")

    # ── The agentic loop ──────────────────────────────────────────────────────
    #
    # This while loop is the core of how agents work:
    #   1. Send messages to the model
    #   2. Model returns a response — either text (done) or tool calls (keep going)
    #   3. Execute the tool calls, append results to message history
    #   4. Go back to step 1
    #
    # The loop exits when the model stops calling tools (stop_reason == "end_turn")
    # or when the agent calls write_report (our chosen terminal condition).

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=4096,
            system=SYSTEM_PROMPT,
            tools=TOOL_SCHEMAS,
            messages=messages,
        )

        # Append the model's response to history so it sees its own reasoning
        messages.append({"role": "assistant", "content": response.content})

        # Model decided it's done without calling any tools
        if response.stop_reason == "end_turn":
            print("\nAgent finished.")
            break

        # Model wants to call tools
        if response.stop_reason == "tool_use":
            tool_results = []
            terminal = False

            for block in response.content:
                if block.type != "tool_use":
                    continue  # skip text blocks in this pass

                # ── Dispatch ──────────────────────────────────────────────────
                # The model picked a tool by name. We look it up in TOOL_DISPATCH
                # and call the corresponding Python function with the model's inputs.

                tool_fn = TOOL_DISPATCH[block.name]
                print(f"→ {block.name}({_format_args(block.input)})")

                result = tool_fn(**block.input)

                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })

                if block.name == "write_report":
                    print(f"\n{result}")
                    terminal = True

            # Feed tool results back into the conversation
            messages.append({"role": "user", "content": tool_results})

            if terminal:
                break

        else:
            print(f"Unexpected stop_reason: {response.stop_reason}")
            break


def _format_args(inputs: dict) -> str:
    """Format tool inputs for display, truncating long values."""
    parts = []
    for k, v in inputs.items():
        v_str = repr(v)
        if len(v_str) > 60:
            v_str = v_str[:57] + "..."
        parts.append(f"{k}={v_str}")
    return ", ".join(parts)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python scout.py "your research question"')
        sys.exit(1)

    run(" ".join(sys.argv[1:]))
