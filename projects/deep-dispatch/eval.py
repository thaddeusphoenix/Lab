"""
Eval — quality scoring for Deep Dispatch research reports.

Runs in two layers to minimize API cost:

  Layer 1 — Deterministic checks (free)
    Verifies structure, source citations, and length without any API calls.
    A report that fails here gets flagged immediately.

  Layer 2 — LLM scoring (one cheap API call)
    Sends only the first ~1500 chars of the report to Gemini and asks for
    three scores (1–5): Relevance, Faithfulness, Quality.
    Total cost: fractions of a cent per eval.

Usage (standalone):
    python eval.py "your research question" reports/your-report.md

Returns an EvalResult with an overall score (1–5) and per-dimension breakdown.
A score below 3 is considered low quality — dispatch.py will prompt before delivering.
"""

import json
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

EVAL_MODEL = "gemini-2.5-flash"

# Sections the research prompt instructs the model to produce
REQUIRED_SECTIONS = ["Executive Summary", "Key Findings", "Sources"]

# How much of the report to send to the LLM scorer (keeps cost low)
EVAL_EXCERPT_CHARS = 1500


@dataclass
class EvalResult:
    passed_structure: bool
    source_count: int
    word_count: int
    relevance: int       # 1–5
    faithfulness: int    # 1–5
    quality: int         # 1–5
    note: str
    score: float         # average of the three LLM scores

    def display(self) -> str:
        bar = lambda n: "█" * n + "░" * (5 - n)
        lines = [
            f"  Structure   {'✓' if self.passed_structure else '✗'}  "
            f"({len(REQUIRED_SECTIONS)} required sections {'found' if self.passed_structure else 'missing'})",
            f"  Sources     {'✓' if self.source_count >= 3 else '✗'}  ({self.source_count} cited)",
            f"  Words       {self.word_count}",
            f"",
            f"  Relevance   {bar(self.relevance)}  {self.relevance}/5",
            f"  Faithfulness {bar(self.faithfulness)} {self.faithfulness}/5",
            f"  Quality     {bar(self.quality)}  {self.quality}/5",
            f"",
            f"  Overall     {self.score:.1f}/5  — {self.note}",
        ]
        return "\n".join(lines)


# ── Layer 1: Deterministic checks ────────────────────────────────────────────

def _check_structure(report: str) -> bool:
    """Return True if all required section headers are present."""
    return all(section in report for section in REQUIRED_SECTIONS)


def _count_sources(report: str) -> int:
    """Count URLs in the report as a proxy for cited sources."""
    return len(re.findall(r"https?://\S+", report))


def _word_count(report: str) -> int:
    return len(report.split())


# ── Layer 2: LLM scoring ──────────────────────────────────────────────────────

EVAL_PROMPT = """\
You are a research quality evaluator. Score this research report excerpt on three dimensions.

Research question: {question}

Report excerpt (first {chars} characters):
---
{excerpt}
---

Score each dimension 1–5 using these definitions:
- 5: Excellent. Clearly addresses the dimension with strong evidence.
- 4: Good. Mostly addresses the dimension with minor gaps.
- 3: Adequate. Partially addresses the dimension.
- 2: Weak. Significant gaps or issues.
- 1: Poor. Fails to address the dimension.

Dimensions:
- relevance: Does the report directly answer the research question?
- faithfulness: Are claims grounded in cited sources (not hallucinated)?
- quality: Is the writing clear, well-structured, and useful?

Return ONLY a JSON object with this exact shape:
{{"relevance": N, "faithfulness": N, "quality": N, "note": "one sentence summary"}}
"""


def _llm_score(question: str, report: str) -> dict:
    """Ask Gemini to score the report. Returns dict with relevance/faithfulness/quality/note."""
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    excerpt = report[:EVAL_EXCERPT_CHARS]

    response = client.models.generate_content(
        model=EVAL_MODEL,
        contents=EVAL_PROMPT.format(
            question=question,
            chars=EVAL_EXCERPT_CHARS,
            excerpt=excerpt,
        ),
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0,  # deterministic scoring
        ),
    )

    try:
        return json.loads(response.text)
    except (json.JSONDecodeError, AttributeError):
        return {"relevance": 3, "faithfulness": 3, "quality": 3, "note": "eval scoring failed"}


# ── Public interface ──────────────────────────────────────────────────────────

def evaluate(question: str, report: str) -> EvalResult:
    """Run both eval layers and return an EvalResult."""
    passed_structure = _check_structure(report)
    source_count = _count_sources(report)
    word_count = _word_count(report)

    scores = _llm_score(question, report)

    relevance = int(scores.get("relevance", 3))
    faithfulness = int(scores.get("faithfulness", 3))
    quality = int(scores.get("quality", 3))
    note = scores.get("note", "")

    # Penalize structurally broken reports
    if not passed_structure:
        relevance = min(relevance, 2)
    if source_count < 3:
        faithfulness = min(faithfulness, 2)

    overall = (relevance + faithfulness + quality) / 3

    return EvalResult(
        passed_structure=passed_structure,
        source_count=source_count,
        word_count=word_count,
        relevance=relevance,
        faithfulness=faithfulness,
        quality=quality,
        note=note,
        score=overall,
    )


# ── Standalone CLI ────────────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage: python eval.py "research question" path/to/report.md')
        sys.exit(1)

    question = sys.argv[1]
    report_path = Path(sys.argv[2])

    if not report_path.exists():
        print(f"Report not found: {report_path}")
        sys.exit(1)

    report = report_path.read_text(encoding="utf-8")
    print(f"\nEvaluating: {report_path.name}\n")
    result = evaluate(question, report)
    print(result.display())
