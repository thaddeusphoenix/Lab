"""
Tool implementations for Deep Dispatch.

These are plain Python functions — not LLM tools. The agent pipeline calls them
directly. Only the source selection and deep research steps involve Gemini.

  load_manifest       — reads sources/manifest.json
  build_context       — loads source file content into a single string
  to_pdf              — converts markdown report to PDF (fpdf2, pure Python)
  send_to_remarkable  — pushes the PDF to reMarkable via rmapi
"""

import json
import os
import re
import subprocess
from pathlib import Path

from fpdf import FPDF

SOURCES_DIR = Path(__file__).parent / "sources"
REPORTS_DIR = Path(__file__).parent / "reports"

# ── Sources ───────────────────────────────────────────────────────────────────

def load_manifest() -> list[dict]:
    """Read the NotebookLM sources manifest."""
    path = SOURCES_DIR / "manifest.json"
    if not path.exists():
        return []
    with open(path) as f:
        return json.load(f)


def build_context(selected_ids: list[str], projects: list[dict]) -> str:
    """Load source file content for each selected project ID."""
    if not selected_ids:
        return ""

    parts = []
    for source_id in selected_ids:
        project = next((p for p in projects if p["id"] == source_id), None)
        if not project:
            continue
        file_path = Path(__file__).parent / project["file"]
        if not file_path.exists():
            print(f"  ⚠ Source file not found: {project['file']}")
            continue
        content = file_path.read_text(encoding="utf-8")
        parts.append(f"=== Source: {project['title']} ===\n{content}")

    if not parts:
        return ""

    return (
        "The following are personal knowledge sources relevant to this question. "
        "Treat them as additional context alongside your web research:\n\n"
        + "\n\n".join(parts)
    )


# ── PDF ───────────────────────────────────────────────────────────────────────

def _slugify(text: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug[:60].rstrip("-")


def _classify_line(line: str) -> tuple[str, str]:
    """Return (type, text) for a markdown line."""
    if line.startswith("### "):
        return "h3", line[4:]
    if line.startswith("## "):
        return "h2", line[3:]
    if line.startswith("# "):
        return "h1", line[2:]
    if line.startswith("- ") or line.startswith("* "):
        return "li", "- " + line[2:]
    if re.match(r"^\d+\. ", line):
        return "li", "- " + re.sub(r"^\d+\. ", "", line)
    if line.startswith("> "):
        return "quote", line[2:]
    if line.strip() == "" or line.strip() == "---":
        return "blank", ""
    return "body", line


def to_pdf(markdown_content: str, question: str) -> Path:
    """Convert a markdown report to a clean PDF for reMarkable (pure Python, no system deps)."""
    REPORTS_DIR.mkdir(exist_ok=True)
    pdf_path = REPORTS_DIR / f"{_slugify(question)}.pdf"

    # Strip markdown links to plain text: [text](url) → text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", markdown_content)
    # Strip bold/italic markers
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    # Normalize Unicode to latin-1 safe characters
    text = (text
        .replace("\u2022", "-").replace("\u2023", "-").replace("\u25e6", "-")
        .replace("\u2018", "'").replace("\u2019", "'")
        .replace("\u201c", '"').replace("\u201d", '"')
        .replace("\u2014", "--").replace("\u2013", "-")
        .replace("\u2026", "...").replace("\u00b7", "-")
    )
    text = text.encode("latin-1", errors="replace").decode("latin-1")
    # Remove trailing whitespace and collapse runs of 3+ blank lines to 2
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    pdf = FPDF()
    pdf.set_margins(20, 20, 20)
    pdf.add_page()

    W = pdf.epw  # effective page width (respects margins)
    consecutive_blanks = 0

    for raw_line in text.split("\n"):
        kind, line = _classify_line(raw_line)
        line = line.strip()
        if not line and kind != "blank":
            continue

        consecutive_blanks = 0
        if kind == "h1":
            pdf.set_font("Helvetica", "B", 18)
            pdf.ln(4)
            pdf.multi_cell(W, 10, line)
            pdf.ln(2)
        elif kind == "h2":
            pdf.set_font("Helvetica", "B", 14)
            pdf.ln(6)
            pdf.multi_cell(W, 8, line)
            pdf.ln(1)
        elif kind == "h3":
            pdf.set_font("Helvetica", "BI", 12)
            pdf.ln(4)
            pdf.multi_cell(W, 7, line)
        elif kind in ("li", "quote"):
            pdf.set_font("Helvetica", "I" if kind == "quote" else "", 11)
            pdf.multi_cell(W, 6, line)
        elif kind == "blank":
            consecutive_blanks += 1
            if consecutive_blanks <= 1:
                pdf.ln(3)
            continue
        else:
            pdf.set_font("Helvetica", "", 11)
            pdf.multi_cell(W, 6, line)

    pdf.output(str(pdf_path))
    print(f"  PDF: {pdf_path.name}")
    return pdf_path


# ── reMarkable delivery ───────────────────────────────────────────────────────

RMAPI = Path.home() / ".local" / "bin" / "rmapi"


def send_to_remarkable(pdf_path: Path, subject: str) -> None:
    """Push the PDF to reMarkable using rmapi."""
    # --content-only overwrites an existing document on the device
    # without recreating it (preserves annotations if any)
    result = subprocess.run(
        [str(RMAPI), "put", str(pdf_path)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        if "already exists" in result.stderr:
            subprocess.run(
                [str(RMAPI), "put", "--content-only", str(pdf_path)],
                check=True,
            )
        else:
            raise subprocess.CalledProcessError(result.returncode, result.args)
    print(f"  Delivered: {pdf_path.name}")
