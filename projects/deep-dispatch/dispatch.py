"""
Deep Dispatch — a Gemini-powered research agent.

Usage:
    python dispatch.py "What is the current state of spatial computing hardware?"

The agent runs in three stages:

  Stage 1 — Source selection (Gemini, JSON output)
    Gemini reads your NotebookLM sources manifest and identifies which projects
    are relevant to the research question. You confirm before they're included.

  Stage 2 — Deep research (Gemini + Google Search grounding)
    Gemini runs a comprehensive web research session with your selected sources
    injected as context. Google Search grounding provides live, cited web access.

    NOTE: Google Search grounding and custom function calling cannot be combined
    in a single Gemini call — this is why the pipeline uses two separate calls.

  Stage 3 — Delivery (Python, no LLM)
    The report is converted to a styled PDF and emailed to your reMarkable.
    The document appears on your device within seconds.
"""

import json
import os
import sys
from typing import Optional

from dotenv import load_dotenv
from google import genai
from google.genai import types

from tools import build_context, load_manifest, send_to_remarkable, to_pdf

load_dotenv()

# Swap to a more capable model (e.g. gemini-2.5-pro) for deeper research.
SELECTION_MODEL = "gemini-2.0-flash"
RESEARCH_MODEL = "gemini-2.0-flash"


# ── Stage 1: Source selection ─────────────────────────────────────────────────

SOURCE_SELECTION_PROMPT = """\
A user wants to research the following question:

"{question}"

These are their available NotebookLM knowledge projects:
{project_list}

Return a JSON array of project IDs that would meaningfully contribute to this
research. Be selective — only include sources directly relevant to the question.
If none are relevant, return an empty array: []
"""


def select_sources(client: genai.Client, question: str, projects: list[dict]) -> list[str]:
    """Ask Gemini which NotebookLM sources are relevant to the question."""
    if not projects:
        return []

    project_list = "\n".join(
        f"- id: \"{p['id']}\"  title: \"{p['title']}\"  topics: {p['topics']}"
        for p in projects
    )

    response = client.models.generate_content(
        model=SELECTION_MODEL,
        contents=SOURCE_SELECTION_PROMPT.format(
            question=question,
            project_list=project_list,
        ),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
        ),
    )

    try:
        ids = json.loads(response.text)
        return ids if isinstance(ids, list) else []
    except (json.JSONDecodeError, AttributeError):
        return []


# ── Stage 2: Deep research ────────────────────────────────────────────────────

RESEARCH_PROMPT = """\
You are a deep research agent. Your task is to research the following question
thoroughly, using web search to find current, credible sources.

{source_context}

Research question:
{question}

Write a comprehensive research report in markdown. Structure it as:

# [Descriptive title]

## Executive Summary
2–3 sentences capturing the core answer.

## Key Findings
Detailed findings with subsections as needed. Cite your sources inline.

## Analysis
What this means, implications, open questions.

## Sources
A numbered list of all sources used, with URLs.
"""


def deep_research(client: genai.Client, question: str, source_context: str) -> str:
    """Run Gemini with Google Search grounding to produce a research report."""
    prompt = RESEARCH_PROMPT.format(
        question=question,
        source_context=source_context,
    )

    response = client.models.generate_content(
        model=RESEARCH_MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            tools=[types.Tool(google_search=types.GoogleSearch())],
            temperature=0.3,
        ),
    )

    return response.text


# ── Main pipeline ─────────────────────────────────────────────────────────────

def run(question: str) -> None:
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    print(f"\nQuestion: {question}\n")

    # Stage 1a: Load manifest
    projects = load_manifest()
    print(f"[1/3] Source selection ({len(projects)} project(s) in manifest)")

    # Stage 1b: Ask Gemini which sources are relevant
    selected_ids: list[str] = []
    if projects:
        suggested = select_sources(client, question, projects)

        if suggested:
            print(f"      Relevant: {', '.join(suggested)}")
            answer = input("      Include these? [Y/n] ").strip().lower()
            if answer != "n":
                selected_ids = suggested
        else:
            print("      No sources selected as relevant")

    # Stage 1c: Load source content
    source_context = build_context(selected_ids, projects)
    if source_context:
        print(f"      Loaded {len(selected_ids)} source(s) into context")

    # Stage 2: Deep research
    print("\n[2/3] Running deep research...")
    report = deep_research(client, question, source_context)
    print("      Done")

    # Stage 3: Deliver
    print("\n[3/3] Delivering to reMarkable...")
    pdf_path = to_pdf(report, question)
    send_to_remarkable(pdf_path, question)

    print(f"\nDone. Check your reMarkable.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: python dispatch.py "your research question"')
        sys.exit(1)

    run(" ".join(sys.argv[1:]))
