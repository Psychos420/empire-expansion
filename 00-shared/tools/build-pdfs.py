#!/usr/bin/env python3
"""
Build PDF lead magnets from each niche's LEAD-MAGNET.md.

Usage:
    cd C:/Users/aksoy/Claude/Projects/Empire-Expansion
    .venv/Scripts/python 00-shared/tools/build-pdfs.py

Outputs:
    01-affiliate-marketing/lead-magnet.pdf
    02-tiktok-shop/lead-magnet.pdf
    ...
    03-pdfs-guides/paid-product.pdf   (extra paid guide)
"""

import re
import sys
from pathlib import Path

from fpdf import FPDF
from markdown import markdown

ROOT = Path(__file__).resolve().parents[2]
FONT_DIR = Path("C:/Windows/Fonts")

# (family, style, filename)
FONTS = [
    ("ArialUnicode", "", "arial.ttf"),
    ("ArialUnicode", "B", "arialbd.ttf"),
    ("ArialUnicode", "I", "ariali.ttf"),
    ("ArialUnicode", "BI", "arialbi.ttf"),
    ("Code", "", "consola.ttf"),
]

NICHE_DIRS = sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name[:2].isdigit()])


def add_fonts(pdf: FPDF) -> None:
    for family, style, filename in FONTS:
        path = FONT_DIR / filename
        if path.exists():
            pdf.add_font(family, style, str(path))
        else:
            print(f"WARN: font {path} not found, falling back to Helvetica")


def extract_cover_title(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line.lstrip("# ").strip()
    return "Lead-Magnet"


def _is_table_separator(row_cells: list[str]) -> bool:
    return all(
        re.fullmatch(r"[-:\s]+", c) for c in row_cells if c.strip()
    )


def flatten_markdown_tables(md: str) -> str:
    """
    Convert markdown tables to plain key/value paragraphs.
    fpdf2's write_html has severe problems rendering HTML tables that contain
    nested emphasis or long unbreakable content. Flattening keeps the PDF
    readable and avoids those crashes.
    """
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if "|" in line:
            block: list[str] = []
            while i < len(lines) and "|" in lines[i]:
                block.append(lines[i])
                i += 1
            out.extend(_table_block_to_lines(block))
        else:
            out.append(line)
            i += 1
    return "\n".join(out)


def _table_block_to_lines(block: list[str]) -> list[str]:
    rows: list[list[str]] = []
    for line in block:
        cells = [c.strip() for c in line.split("|")]
        # Drop empty cells caused by leading/trailing pipes
        if cells and cells[0] == "":
            cells = cells[1:]
        if cells and cells[-1] == "":
            cells = cells[:-1]
        rows.append(cells)

    # Remove separator row
    sep_idx = next(
        (idx for idx, row in enumerate(rows) if _is_table_separator(row)), None
    )
    if sep_idx is not None:
        header_rows = rows[:sep_idx]
        body_rows = rows[sep_idx + 1 :]
    else:
        header_rows = []
        body_rows = rows

    headers = header_rows[0] if header_rows else []
    result: list[str] = []
    if headers:
        result.append(" | ".join(headers))
        result.append("")

    for row in body_rows:
        if not row:
            continue
        if headers and len(row) == len(headers):
            parts = []
            for h, c in zip(headers, row):
                if c:
                    parts.append(f"**{h}:** {c}")
                else:
                    parts.append(h)
            result.append(" | ".join(parts))
        else:
            result.append(" | ".join(row))
    return result


def md_to_html(text: str) -> str:
    # Strip optional YAML frontmatter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2].lstrip("\n")

    text = flatten_markdown_tables(text)

    html = markdown(
        text,
        extensions=["fenced_code", "nl2br"],
        output_format="html",
    )

    # write_html in fpdf2 does not know <code>/<pre>; keep text readable.
    html = html.replace("<code>", "<em>").replace("</code>", "</em>")
    html = html.replace("<pre>", "<p>").replace("</pre>", "</p>")

    # Keep checkbox markers as plain ASCII so every font can render them.
    # We deliberately do NOT convert them to unicode symbols because Arial
    # is missing those glyphs in the Windows font files.
    html = html.replace("[ ]", "[  ]").replace("[x]", "[x]").replace("[X]", "[x]")

    # Replace arrows and other symbols that Arial may not contain.
    arrow_map = {
        "\u2192": "->",
        "\u2794": "->",
        "\u2190": "<-",
        "\u2191": "^",
        "\u2193": "v",
        "\u2013": "-",
        "\u2014": "-",
        "\u2610": "[ ]",
        "\u2611": "[x]",
        "\u2612": "[x]",
        "\u2713": "[x]",
        "\u2714": "[x]",
        "\u2705": "[OK]",
        "\u274c": "[X]",
    }
    for src, dst in arrow_map.items():
        html = html.replace(src, dst)

    # Flatten fill-in-line patterns like <strong><em>_</em></strong>___ that
    # confuse fpdf2's renderer. Replace with a plain underscore line.
    html = re.sub(r"<strong><em>_</em></strong>_+", "__________", html)
    html = re.sub(r"<strong><strong><em>_</em></strong>_+</strong>", "<strong>__________</strong>", html)
    # Also collapse accidental nested identical emphasis tags.
    html = re.sub(r"<strong>\s*<strong>(.*?)</strong>\s*</strong>", r"<strong>\1</strong>", html, flags=re.S)
    html = re.sub(r"<em>\s*<em>(.*?)</em>\s*</em>", r"<em>\1</em>", html, flags=re.S)

    # fpdf2 write_html supports <font face="...">; force a readable body font
    html = f'<font face="ArialUnicode">{html}</font>'
    return html


def build_pdf(input_path: Path, output_path: Path, subtitle: str = "") -> None:
    text = input_path.read_text(encoding="utf-8")
    title = extract_cover_title(text)
    html = md_to_html(text)

    pdf = FPDF(format="A4")
    add_fonts(pdf)

    # Cover page
    pdf.add_page()
    pdf.set_auto_page_break(auto=False)
    pdf.set_font("ArialUnicode", "B", 28)
    pdf.set_y(80)
    pdf.multi_cell(0, 16, title, align="C")
    if subtitle:
        pdf.set_font("ArialUnicode", "", 14)
        pdf.ln(8)
        pdf.multi_cell(0, 10, subtitle, align="C")
    pdf.set_font("ArialUnicode", "", 11)
    pdf.set_y(-60)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(0, 8, "Empire Expansion — 35+ Lead-Ökosystem\nKostenloser Lead-Magnet", align="C")
    pdf.set_text_color(0, 0, 0)

    # Content pages
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.set_font("ArialUnicode", "", 11)
    try:
        pdf.write_html(html)
    except Exception as e:
        print(f"  HTML render warning for {input_path}: {e}")
        # Fallback: write plain text blocks
        for line in text.splitlines():
            pdf.multi_cell(0, 6, line)

    pdf.output(str(output_path))


def main() -> int:
    print(f"Building lead-magnet PDFs in {ROOT}\n")
    errors = []

    for niche in NICHE_DIRS:
        lead_magnet = niche / "LEAD-MAGNET.md"
        if not lead_magnet.exists():
            print(f"SKIP {niche.name}: no LEAD-MAGNET.md")
            continue

        out = niche / "lead-magnet.pdf"
        try:
            build_pdf(lead_magnet, out, subtitle="Kostenloser Download")
            print(f"[OK] {out.relative_to(ROOT)}")
        except Exception as e:
            print(f"[ERR] {niche.name}: {e}")
            errors.append((niche.name, str(e)))

    # Extra paid product for PDFs/guides niche
    paid = ROOT / "03-pdfs-guides" / "PAID-PRODUCT.md"
    if paid.exists():
        out = paid.parent / "paid-product.pdf"
        try:
            build_pdf(paid, out, subtitle="Paid Guide - ETF-Strategie fuer 40+")
            print(f"[OK] {out.relative_to(ROOT)}")
        except Exception as e:
            print(f"[ERR] paid-product: {e}")
            errors.append(("paid-product", str(e)))

    if errors:
        print("\nErrors:")
        for name, err in errors:
            print(f"  {name}: {err}")
        return 1

    print("\nAll PDFs built successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
