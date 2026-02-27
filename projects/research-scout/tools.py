"""
Tool implementations and schemas for Research Scout.

Each tool has two parts:
  1. A Python function that does the actual work
  2. A JSON schema entry in TOOL_SCHEMAS that tells the model what the tool does

The model decides when and how to call tools. This file defines the menu.
"""

import os
from pathlib import Path

import httpx
from bs4 import BeautifulSoup
from tavily import TavilyClient


# ── Tool implementations ──────────────────────────────────────────────────────

def search(query: str) -> str:
    """Search the web using Tavily and return formatted results."""
    client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
    response = client.search(query, max_results=5)

    formatted = []
    for result in response["results"]:
        formatted.append(
            f"**{result['title']}**\n"
            f"URL: {result['url']}\n"
            f"{result['content']}"
        )
    return "\n\n---\n\n".join(formatted)


def fetch_page(url: str) -> str:
    """Fetch the text content of a web page, stripping HTML."""
    try:
        resp = httpx.get(url, follow_redirects=True, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        text = soup.get_text(separator="\n", strip=True)
        # Truncate to avoid blowing up the context window
        return text[:8000]
    except Exception as e:
        return f"Error fetching {url}: {e}"


def write_report(filename: str, content: str) -> str:
    """Write the final report to disk. Calling this ends the research session."""
    reports_dir = Path(__file__).parent / "reports"
    reports_dir.mkdir(exist_ok=True)

    if not filename.endswith(".md"):
        filename += ".md"

    path = reports_dir / filename
    path.write_text(content, encoding="utf-8")
    return f"Report written to: {path}"


# ── Tool schemas ──────────────────────────────────────────────────────────────
# These are the JSON definitions passed to the Anthropic API.
# The model reads these to understand what each tool does and what inputs it takes.

TOOL_SCHEMAS = [
    {
        "name": "search",
        "description": (
            "Search the web for information on a topic. "
            "Returns titles, URLs, and snippets from the most relevant pages. "
            "Use this to discover sources before deciding which ones to read in full."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query",
                }
            },
            "required": ["query"],
        },
    },
    {
        "name": "fetch_page",
        "description": (
            "Fetch the full text content of a web page by URL. "
            "Use this when a search snippet is not enough and you need the full source."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "The URL of the page to fetch",
                }
            },
            "required": ["url"],
        },
    },
    {
        "name": "write_report",
        "description": (
            "Write the final research report to disk as a markdown file. "
            "Call this when you have gathered enough information and are ready to synthesize. "
            "This ends the research session — only call it once."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "Filename for the report, kebab-case, ending in .md (e.g. 'agent-failure-modes.md')",
                },
                "content": {
                    "type": "string",
                    "description": "The full markdown content of the report",
                },
            },
            "required": ["filename", "content"],
        },
    },
]

# Maps tool names to their implementations. Used in the dispatch loop in scout.py.
TOOL_DISPATCH = {
    "search": search,
    "fetch_page": fetch_page,
    "write_report": write_report,
}
