"""
Tool implementations for Deep Dispatch.

These are plain Python functions — not LLM tools. The agent pipeline calls them
directly. Only the source selection and deep research steps involve Gemini.

  load_manifest   — reads sources/manifest.json
  build_context   — loads source file content into a single string
  to_pdf          — converts markdown report to PDF (weasyprint)
  send_to_remarkable — emails the PDF to the reMarkable device
"""

import json
import os
import re
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

import markdown
from weasyprint import HTML

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

# CSS tuned for reMarkable's e-ink display: clean serif, generous line height,
# good contrast, no decorative elements that don't render well on e-ink.
REMARKABLE_CSS = """
body {
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 13pt;
    line-height: 1.75;
    max-width: 680px;
    margin: 60px auto;
    color: #111;
}
h1 { font-size: 20pt; margin-bottom: 0.4em; line-height: 1.3; }
h2 { font-size: 15pt; margin-top: 2em; border-bottom: 1px solid #bbb; padding-bottom: 6px; }
h3 { font-size: 13pt; margin-top: 1.5em; font-style: italic; }
p  { margin: 0.8em 0; }
a  { color: #333; text-decoration: none; }
code { font-family: 'Courier New', monospace; font-size: 11pt;
       background: #f4f4f4; padding: 1px 5px; }
pre  { background: #f4f4f4; padding: 12px; overflow-x: auto; }
blockquote { border-left: 3px solid #999; margin-left: 0;
             padding-left: 1em; color: #555; }
ul, ol { padding-left: 1.6em; }
li { margin: 0.3em 0; }
hr { border: none; border-top: 1px solid #ccc; margin: 2em 0; }
"""


def _slugify(text: str) -> str:
    slug = re.sub(r"[^\w\s-]", "", text.lower())
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug[:60].rstrip("-")


def to_pdf(markdown_content: str, question: str) -> Path:
    """Convert a markdown report to a styled PDF for reMarkable."""
    REPORTS_DIR.mkdir(exist_ok=True)
    pdf_path = REPORTS_DIR / f"{_slugify(question)}.pdf"

    html_body = markdown.markdown(markdown_content, extensions=["extra", "toc"])
    full_html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{REMARKABLE_CSS}</style>
</head><body>
{html_body}
</body></html>"""

    HTML(string=full_html).write_pdf(pdf_path)
    print(f"  PDF: {pdf_path.name}")
    return pdf_path


# ── reMarkable delivery ───────────────────────────────────────────────────────

def send_to_remarkable(pdf_path: Path, subject: str) -> None:
    """Email the PDF to the reMarkable device's registered email address."""
    gmail_address = os.environ["GMAIL_ADDRESS"]
    gmail_password = os.environ["GMAIL_APP_PASSWORD"]
    remarkable_email = os.environ["REMARKABLE_EMAIL"]

    msg = MIMEMultipart()
    msg["From"] = gmail_address
    msg["To"] = remarkable_email
    msg["Subject"] = subject[:100]
    msg.attach(MIMEText("Delivered by Deep Dispatch.", "plain"))

    with open(pdf_path, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={pdf_path.name}")
    msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(gmail_address, gmail_password)
        server.sendmail(gmail_address, remarkable_email, msg.as_string())

    print(f"  Sent to: {remarkable_email}")
