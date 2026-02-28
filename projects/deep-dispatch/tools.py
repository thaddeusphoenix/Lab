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

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

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
    """Convert a markdown report to a clean PDF for reMarkable (ReportLab, proper text flow)."""
    REPORTS_DIR.mkdir(exist_ok=True)
    pdf_path = REPORTS_DIR / f"{_slugify(question)}.pdf"

    # Strip markdown links: [text](url) → text (URLs not clickable on reMarkable)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", markdown_content)
    # Strip bold/italic/code markers
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    # Truncate bare URLs that would overflow — not usable on e-ink anyway
    text = re.sub(r"https?://\S{50,}", lambda m: m.group(0)[:50] + "...", text)
    # Collapse runs of 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    def esc(s: str) -> str:
        """Escape HTML special characters for ReportLab Paragraph."""
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

    # Paragraph styles
    h1 = ParagraphStyle("h1", fontName="Helvetica-Bold",   fontSize=18, leading=22, spaceBefore=14, spaceAfter=6)
    h2 = ParagraphStyle("h2", fontName="Helvetica-Bold",   fontSize=14, leading=18, spaceBefore=12, spaceAfter=4)
    h3 = ParagraphStyle("h3", fontName="Helvetica-BoldOblique", fontSize=12, leading=16, spaceBefore=8, spaceAfter=3)
    body = ParagraphStyle("body", fontName="Helvetica",    fontSize=11, leading=15, spaceAfter=4)
    li   = ParagraphStyle("li",   fontName="Helvetica",    fontSize=11, leading=14, spaceAfter=3, leftIndent=18)
    quot = ParagraphStyle("quot", fontName="Helvetica-Oblique", fontSize=11, leading=14, spaceAfter=3, leftIndent=30)

    story = []
    for raw_line in text.split("\n"):
        kind, line = _classify_line(raw_line)
        line = line.strip()
        if not line and kind != "blank":
            continue

        if kind == "blank":
            story.append(Spacer(1, 8))
        elif kind == "h1":
            story.append(Paragraph(esc(line), h1))
        elif kind == "h2":
            story.append(Paragraph(esc(line), h2))
        elif kind == "h3":
            story.append(Paragraph(esc(line), h3))
        elif kind == "li":
            story.append(Paragraph(esc(line), li))
        elif kind == "quote":
            story.append(Paragraph(esc(line), quot))
        else:
            story.append(Paragraph(esc(line), body))

    doc = SimpleDocTemplate(
        str(pdf_path),
        pagesize=letter,
        leftMargin=inch,
        rightMargin=inch,
        topMargin=inch,
        bottomMargin=inch,
    )
    doc.build(story)
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
