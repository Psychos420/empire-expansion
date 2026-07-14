#!/usr/bin/env python3
"""
Build PDF lead magnets from each niche's LEAD-MAGNET.md (and PAID-PRODUCT.md).

Professional xhtml2pdf pipeline with:
  - Cluster-branded cover pages (full-page colour background)
  - Chapter pages with coloured stripe
  - Styled infoboxes, checklists, stat-bars, tables
  - CTA page at end with {{STRIPE_LINK}} placeholder
  - Centred page numbers in footer (xhtml2pdf native <pdf:pagefooter>)

Usage:
    cd C:/Users/aksoy/Claude/Projects/Empire-Expansion
    .venv/Scripts/python 00-shared/tools/build-pdfs.py

Outputs:
    01-affiliate-marketing/lead-magnet.pdf
    02-tiktok-shop/lead-magnet.pdf
    ...
    03-pdfs-guides/paid-product.pdf   (extra paid guide)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Tuple

from markdown import markdown
from xhtml2pdf import pisa

ROOT = Path(__file__).resolve().parents[2]
FONT_DIR = Path(__file__).resolve().parent / "fonts"

NICHE_DIRS = sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name[:2].isdigit()])

# ── Cluster definitions ──────────────────────────────────────────────────────
CLUSTERS = {
    "finanz":  {
        "accent": "#1f6f5c",
        "tint":   "#eef4f0",
        "light":  "#d4e8e0",
        "label":  "Finanz & Vorsorge",
    },
    "business": {
        "accent": "#3d4f8f",
        "tint":   "#eef0f7",
        "light":  "#d4dceb",
        "label":  "Business & Digital",
    },
    "alltag":  {
        "accent": "#b0602c",
        "tint":   "#f8f0e8",
        "light":  "#ecd9c5",
        "label":  "Alltag & Lifestyle",
    },
}

NICHE_CLUSTER: dict[str, str] = {
    "01-affiliate-marketing":              "finanz",
    "03-pdfs-guides":                      "finanz",
    "05-lead-generation-pkv":              "finanz",
    "08-app-ideen-appstore":               "finanz",
    "09-finanzielle-freiheit":             "finanz",
    "11-immobilien-baufinanzierung":       "finanz",
    "04-ki-integrationen-35plus":          "business",
    "07-marketing-agency-traffic":         "business",
    "12-selbststaendigkeit-business-setup": "business",
    "02-tiktok-shop":                      "alltag",
    "06-lead-generation-dropshipping":     "alltag",
    "10-gesundheit-praevention-40plus":    "alltag",
    "13-reisen-lifestyle-35plus":          "alltag",
    "14-nachhaltigkeit-eco":               "alltag",
}

# ── Palette constants ────────────────────────────────────────────────────────
AMBER    = "#b8842e"
INK      = "#1c2333"
MUTED    = "#5b5a6e"
PAPER    = "#f6f1e7"
WHITE    = "#ffffff"
GRAY600  = "#666666"
GRAY400  = "#999999"
GRAY200  = "#dddddd"
GRAY100  = "#f5f5f5"

# ── Font helpers ────────────────────────────────────────────────────────────

def _font_uri(name: str) -> str:
    return (FONT_DIR / name).resolve().as_uri()


def font_face_css() -> str:
    """Return @font-face declarations for all local fonts."""
    return f"""
    @font-face {{ font-family: 'Fraunces';        src: url('{_font_uri("Fraunces-Regular.ttf")}'); }}
    @font-face {{ font-family: 'FrauncesSemiBold'; src: url('{_font_uri("Fraunces-SemiBold.ttf")}'); }}
    @font-face {{ font-family: 'FrauncesDisplay';  src: url('{_font_uri("Fraunces-Bold72.ttf")}'); }}
    @font-face {{ font-family: 'Plex';             src: url('{_font_uri("IBMPlexSans-Regular.ttf")}'); }}
    @font-face {{ font-family: 'PlexMedium';      src: url('{_font_uri("IBMPlexSans-Medium.ttf")}'); }}
    @font-face {{ font-family: 'PlexSemiBold';     src: url('{_font_uri("IBMPlexSans-SemiBold.ttf")}'); }}
    @font-face {{ font-family: 'PlexMono';        src: url('{_font_uri("IBMPlexMono-Regular.ttf")}'); }}
    @font-face {{ font-family: 'PlexMonoMedium';  src: url('{_font_uri("IBMPlexMono-Medium.ttf")}'); }}
    """


# ── Markdown → HTML helpers ─────────────────────────────────────────────────

def extract_cover_title(text: str) -> Tuple[str, str]:
    """Return (title, rest_of_text_without_first_meaningful_h1).
    
    Skips filename-only headings like '# LEAD-MAGNET.md' and '# PAID-PRODUCT.md'.
    """
    lines = text.splitlines()
    title = "Lead-Magnet"
    skip_idx = -1
    FILENAME_HEADINGS = {"lead-magnet.md", "paid-product.md", "readme.md", "index.md"}
    for i, line in enumerate(lines):
        if line.startswith("# "):
            candidate = line.lstrip("# ").strip()
            if candidate.lower() in FILENAME_HEADINGS:
                continue
            title = candidate
            skip_idx = i
            break
    # Remove all skipped filename headings + the chosen title line
    remove = set()
    for i, line in enumerate(lines):
        if line.startswith("# "):
            candidate = line.lstrip("# ").strip()
            if candidate.lower() in FILENAME_HEADINGS or i == skip_idx:
                remove.add(i)
    lines = [line for i, line in enumerate(lines) if i not in remove]
    return title, "\n".join(lines)


def extract_subtitle(text: str) -> Tuple[str, str]:
    """Extract first meaningful > quote or first paragraph as subtitle.
    
    Skips markdown formatting instructions (lines starting with '**Format:**', etc.).
    """
    lines = text.splitlines()
    subtitle = ""
    skip_idx = -1
    FORMAT_PREFIXES = ("format:", "zielgruppe:", "titel:", "subheadline:", "name:", "claim:")
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("> "):
            candidate = stripped.lstrip("> ").strip()
            # Strip markdown bold/italic markers before checking prefix
            clean = candidate.lower().replace("**", "").replace("*", "")
            if not clean.startswith(FORMAT_PREFIXES):
                subtitle = candidate
                skip_idx = i
                break
        elif stripped and not stripped.startswith("#") and not stripped.startswith("|"):
            # First non-empty, non-header, non-table line (max 120 chars)
            clean = stripped.lower().replace("**", "").replace("*", "")
            if len(stripped) <= 120 and not clean.startswith(FORMAT_PREFIXES):
                subtitle = stripped
                break
    if skip_idx >= 0:
        lines = lines[:skip_idx] + lines[skip_idx + 1:]
    return subtitle, "\n".join(lines)


def style_checkboxes(md: str) -> str:
    """Replace markdown checkbox syntax with HTML spans for later styling."""
    md = re.sub(r"\[ \]", '<span class="chkbox-unchecked">\xe2\x98\x90</span>', md)
    md = re.sub(r"\[[xX]\]", '<span class="chkbox-checked">\xe2\x98\x91</span>', md)
    return md


def md_to_html(text: str) -> str:
    """Convert markdown to HTML, stripping YAML front matter if present."""
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2].lstrip("\n")
    text = style_checkboxes(text)
    html = markdown(text, extensions=["fenced_code", "tables", "nl2br"], output_format="html")
    return html


# ── HTML post-processing ────────────────────────────────────────────────────

def postprocess_body_html(body_html: str, accent: str, tint: str) -> str:
    """
    Transform raw markdown HTML into styled xhtml2pdf components:
      - H1 → chapter pages
      - H2/H3 → styled headings
      - blockquote → infobox
      - tables → styled tables with optional stat-bars
      - ul/ol with chkbox spans → styled checklists
    """

    # 1. H1 → chapter page (skip page-break on first H1 since cover already has page-break-after)
    h1_count = [0]
    def h1_repl(m: re.Match) -> str:
        h1_count[0] += 1
        title = m.group(1).strip()
        page_break = 'page-break-before: always;' if h1_count[0] > 1 else ''
        return f'''<div style="{page_break} margin-top: 0; padding-top: 0;"></div>
<div class="chapter-stripe" style="background-color: {accent}; height: 8pt; width: 100%; margin-bottom: 24pt;"></div>
<div class="chapter-number" style="font-family: 'PlexMono'; font-size: 10pt; color: {accent}; letter-spacing: 1.5pt; text-transform: uppercase; margin-bottom: 6pt;">Kapitel</div>
<h1 style="font-family: 'FrauncesSemiBold'; font-size: 22pt; color: {INK}; margin-top: 0; margin-bottom: 16pt; line-height: 1.2; border-bottom: none; padding-bottom: 0;">{title}</h1>
'''

    body_html = re.sub(r"<h1>(.*?)</h1>", h1_repl, body_html, flags=re.IGNORECASE)

    # 2. H2 → styled
    body_html = re.sub(
        r"<h2>(.*?)</h2>",
        rf'<h2 style="font-family: \'FrauncesSemiBold\'; font-size: 15pt; color: {accent}; margin-top: 18pt; margin-bottom: 8pt; line-height: 1.25;">\1</h2>',
        body_html,
        flags=re.IGNORECASE,
    )

    # 3. H3 → styled
    body_html = re.sub(
        r"<h3>(.*?)</h3>",
        rf'<h3 style="font-family: \'PlexSemiBold\'; font-size: 12pt; color: {INK}; margin-top: 14pt; margin-bottom: 6pt; line-height: 1.3;">\1</h3>',
        body_html,
        flags=re.IGNORECASE,
    )

    # 4. blockquote → infobox
    def bq_repl(m: re.Match) -> str:
        inner = m.group(1).strip()
        return f'''<div style="background-color: {tint}; border-left: 4pt solid {accent}; padding: 10pt 14pt; margin: 12pt 0; border-radius: 0 4pt 4pt 0;">
<div style="font-family: 'PlexSemiBold'; font-size: 9.5pt; color: {accent}; text-transform: uppercase; letter-spacing: 0.8pt; margin-bottom: 6pt;">Hinweis</div>
<div style="font-family: 'Plex'; font-size: 10pt; color: {INK}; line-height: 1.5;">{inner}</div>
</div>'''

    body_html = re.sub(r"<blockquote>\s*<p>(.*?)</p>\s*</blockquote>", bq_repl, body_html, flags=re.IGNORECASE | re.DOTALL)
    # Also handle multi-paragraph blockquotes
    body_html = re.sub(
        r"<blockquote>(.*?)</blockquote>",
        lambda m: f'''<div style="background-color: {tint}; border-left: 4pt solid {accent}; padding: 10pt 14pt; margin: 12pt 0; border-radius: 0 4pt 4pt 0;">
<div style="font-family: 'PlexSemiBold'; font-size: 9.5pt; color: {accent}; text-transform: uppercase; letter-spacing: 0.8pt; margin-bottom: 6pt;">Hinweis</div>
<div style="font-family: 'Plex'; font-size: 10pt; color: {INK}; line-height: 1.5;">{m.group(1)}</div>
</div>''',
        body_html,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 5. Tables → styled + stat-bar detection
    def table_repl(m: re.Match) -> str:
        table_html = m.group(1)
        # Try to detect percentage columns for stat bars
        has_stats = re.search(r"(\d+[\.,]?\d*)\s*%", table_html) is not None

        if has_stats:
            def stat_repl(cell_m: re.Match) -> str:
                cell = cell_m.group(0)
                pct_match = re.search(r"(\d+[\.,]?\d*)\s*%", cell)
                if pct_match:
                    pct_val = float(pct_match.group(1).replace(",", "."))
                    pct_str = pct_match.group(0)
                    bar_html = f'''<div style="margin-top: 4pt;">
<div style="font-family: 'PlexMono'; font-size: 8pt; color: {GRAY600}; margin-bottom: 2pt;">{pct_str}</div>
<div style="background-color: {GRAY200}; height: 4pt; width: 100%; border-radius: 2pt;">
<div style="background-color: {accent}; height: 4pt; width: {min(pct_val, 100)}%; border-radius: 2pt;"></div>
</div>
</div>'''
                    cell = cell.replace(pct_str, bar_html)
                return cell

            table_html = re.sub(r"<td>.*?</td>", stat_repl, table_html, flags=re.IGNORECASE | re.DOTALL)

        return f'''<table style="width: 100%; border-collapse: collapse; margin: 10pt 0; font-size: 9.5pt; page-break-inside: auto;">
{table_html}
</table>'''

    body_html = re.sub(r"<table>(.*?)</table>", table_repl, body_html, flags=re.IGNORECASE | re.DOTALL)

    # Style table headers / cells
    body_html = body_html.replace("<th>", f'<th style="background-color: {tint}; color: {INK}; font-family: \'PlexSemiBold\'; text-align: left; padding: 5pt 7pt; border-bottom: 1.5pt solid {accent}; vertical-align: top;">')
    body_html = body_html.replace("<td>", f'<td style="padding: 5pt 7pt; border-bottom: 0.5pt solid {GRAY200}; vertical-align: top; font-family: \'Plex\'; font-size: 9.5pt; color: {INK};">')

    # 6. Checklists: ul/ol that contain chkbox spans
    def list_repl(m: re.Match) -> str:
        tag = m.group(1)
        inner = m.group(2)
        if "chkbox" in inner:
            inner = re.sub(
                r"<li>(.*?)</li>",
                lambda li: f'''<div style="display: block; margin: 5pt 0; padding-left: 4pt;">
<div style="display: inline-block; width: 14pt; vertical-align: top; font-family: \'PlexMono\'; font-size: 11pt; color: {accent}; text-align: center;">{li.group(1).replace("<p>", "").replace("</p>", "")}</div>
</div>''',
                inner,
                flags=re.IGNORECASE | re.DOTALL,
            )
            return f'<div style="background-color: {GRAY100}; border: 0.5pt solid {GRAY200}; border-radius: 4pt; padding: 8pt 12pt; margin: 10pt 0;">\n{inner}\n</div>'
        else:
            inner = re.sub(
                r"<li>(.*?)</li>",
                lambda li: f'<li style="margin-bottom: 4pt; font-family: \'Plex\'; font-size: 10pt; color: {INK}; line-height: 1.5;">{li.group(1)}</li>',
                inner,
                flags=re.IGNORECASE | re.DOTALL,
            )
            return f'<{tag} style="margin: 6pt 0 6pt 18pt; padding: 0;">\n{inner}\n</{tag}>'

    body_html = re.sub(r"<(ul|ol)>(.*?)</\1>", list_repl, body_html, flags=re.IGNORECASE | re.DOTALL)

    # 7. Clean up stray <p> tags inside checklist divs
    body_html = re.sub(r'<div style="display: inline-block[^"]*">\s*<p>(.*?)</p>\s*</div>', r'<div style="display: inline-block; width: 14pt; vertical-align: top; font-family: \'PlexMono\'; font-size: 11pt; color: ' + accent + r'; text-align: center;">\1</div>', body_html, flags=re.IGNORECASE | re.DOTALL)

    # 8. Style paragraphs
    body_html = re.sub(
        r"<p>(.*?)</p>",
        lambda m: f'<p style="font-family: \'Plex\'; font-size: 10.5pt; color: {INK}; line-height: 1.55; margin: 6pt 0;">{m.group(1)}</p>',
        body_html,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 9. Style code blocks
    body_html = re.sub(
        r"<code>(.*?)</code>",
        lambda m: f'<code style="font-family: \'PlexMono\'; font-size: 9pt; background-color: {GRAY100}; padding: 1pt 3pt; border-radius: 2pt; color: {INK};">{m.group(1)}</code>',
        body_html,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 10. Style pre blocks
    body_html = re.sub(
        r"<pre>(.*?)</pre>",
        lambda m: f'<pre style="font-family: \'PlexMono\'; font-size: 8.5pt; background-color: {GRAY100}; padding: 8pt; border-radius: 3pt; border: 0.5pt solid {GRAY200}; color: {INK}; line-height: 1.4; overflow: hidden;">{m.group(1)}</pre>',
        body_html,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # 11. Style em and strong
    body_html = body_html.replace("<em>", f'<em style="color: {accent}; font-style: normal; font-family: \'PlexSemiBold\';">')
    body_html = body_html.replace("<strong>", f'<strong style="color: {INK}; font-family: \'PlexSemiBold\';">')

    return body_html


# ── CTA page builder ────────────────────────────────────────────────────────

def build_cta_page(niche_name: str, cluster_key: str) -> str:
    """Generate a CTA page at the end of each PDF."""
    c = CLUSTERS[cluster_key]

    # Extract product name from niche directory name
    product_name = niche_name.split("-", 1)[1].replace("-", " ").title()

    # Prices from live-research — no fabricated numbers
    price = "ab 97 \u20ac"
    if "pkv" in niche_name:
        price = "kostenloser 15-Minuten-Check"
    elif "ki" in niche_name or "agency" in niche_name or "business" in niche_name:
        price = "ab 299 \u20ac"
    elif "fire" in niche_name or "immobilie" in niche_name or "app" in niche_name:
        price = "Strategiegespr\u00e4ch ab 199 \u20ac"
    elif "affiliate" in niche_name:
        price = "kostenloser Download"
    elif "dropshipping" in niche_name or "tiktok" in niche_name or "gesundheit" in niche_name or "reisen" in niche_name or "nachhaltigkeit" in niche_name:
        price = "ab 49 \u20ac"

    return f'''
<div style="page-break-before: always;"></div>
<div style="position: absolute; top: -2cm; left: -2.2cm; right: -2.2cm; bottom: -2.4cm; background-color: {c['accent']}; color: {WHITE}; text-align: center;">
    <div style="padding-top: 60pt;">
        <div style="font-family: 'PlexMono'; font-size: 9pt; letter-spacing: 2pt; color: rgba(255,255,255,0.7); text-transform: uppercase; margin-bottom: 20pt;">N\u00e4chster Schritt</div>
        <div style="font-family: 'FrauncesDisplay'; font-size: 28pt; line-height: 1.15; margin-bottom: 16pt; color: {WHITE};">{product_name}</div>
        <div style="font-family: 'PlexMedium'; font-size: 14pt; color: rgba(255,255,255,0.9); margin-bottom: 40pt;">{price}</div>
        <div style="background-color: {WHITE}; color: {c['accent']}; font-family: 'PlexSemiBold'; font-size: 12pt; padding: 12pt 24pt; display: inline-block; border-radius: 4pt; margin-bottom: 30pt;">
            Jetzt sichern &rarr; {{STRIPE_LINK}}
        </div>
        <div style="font-family: 'Plex'; font-size: 9pt; color: rgba(255,255,255,0.6); line-height: 1.5; max-width: 80%; margin: 0 auto;">
            eCom28 GmbH &middot; Bremen &middot; HRB 39329 HB<br>
            Dieser Guide ersetzt keine individuelle Beratung.
        </div>
    </div>
</div>
'''


# ── Full HTML renderer ───────────────────────────────────────────────────────

def render_full_html(
    title: str,
    subtitle: str,
    body_html: str,
    cluster_key: str,
    az: str,
    kicker: str,
    niche_name: str,
) -> str:
    c = CLUSTERS[cluster_key]
    cover_bg = c["accent"]

    # Cover page
    cover_html = f'''<div style="position: absolute; top: -2cm; left: -2.2cm; right: -2.2cm; bottom: -2.4cm; background-color: {cover_bg}; color: {WHITE}; text-align: center;">
    <div style="padding-top: 80pt;">
        <div style="font-family: 'PlexMono'; font-size: 9pt; letter-spacing: 2.5pt; color: rgba(255,255,255,0.6); text-transform: uppercase; margin-bottom: 24pt;">{kicker}</div>
        <div style="font-family: 'FrauncesDisplay'; font-size: 28pt; line-height: 1.12; margin-bottom: 14pt; color: {WHITE};">{title}</div>
        <div style="font-family: 'Plex'; font-size: 12pt; color: rgba(255,255,255,0.85); line-height: 1.5; max-width: 75%; margin: 0 auto 40pt auto;">{subtitle}</div>
        <div style="font-family: 'PlexMono'; font-size: 10pt; color: rgba(255,255,255,0.5); margin-top: 60pt;">
            Aktenzeichen {az} &middot; {c['label']}<br>
            eCom28 GmbH &middot; ecom28.de
        </div>
        <div style="font-family: 'FrauncesSemiBold'; font-size: 13pt; color: rgba(255,255,255,0.4); margin-top: 8pt;">
            Empire<span style="color: {AMBER};">&middot;</span>Expansion
        </div>
    </div>
</div>
<div style="page-break-after: always;"></div>'''

    # CTA page
    cta_html = build_cta_page(niche_name, cluster_key)

    # Footer disclaimer (only on last content page, before CTA)
    footer_html = f'''<div style="font-family: 'PlexMono'; font-size: 7.5pt; color: {GRAY400}; margin-top: 30pt; border-top: 0.5pt solid {GRAY200}; padding-top: 8pt; text-align: center;">
    Empire Expansion &middot; ecom28.de &middot; Dieser Guide ersetzt keine individuelle Rechts-, Steuer- oder Finanzberatung.
</div>'''

    # xhtml2pdf native page-footer for page numbers
    page_footer = f'''<pdf:pagefooter name="empireFooter">
    <div style="text-align: center; font-family: 'PlexMono'; font-size: 8pt; color: {GRAY400}; margin-top: 6pt;">
        <pdf:pagenumber/>
    </div>
</pdf:pagefooter>'''

    return f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{font_face_css()}

@page {{
    size: A4;
    margin: 2cm 2.2cm 2.4cm 2.2cm;
}}

body {{
    font-family: 'Plex';
    font-size: 10.5pt;
    color: {INK};
    line-height: 1.55;
    margin: 0;
    padding: 0;
}}

a {{ color: {c['accent']}; text-decoration: none; }}

hr {{
    border: none;
    border-top: 0.5pt solid {GRAY200};
    margin: 16pt 0;
}}

.chkbox-unchecked {{
    font-family: 'PlexMono';
    font-size: 11pt;
    color: {GRAY400};
    display: inline-block;
    width: 14pt;
    text-align: center;
    vertical-align: top;
}}

.chkbox-checked {{
    font-family: 'PlexMono';
    font-size: 11pt;
    color: {c['accent']};
    display: inline-block;
    width: 14pt;
    text-align: center;
    vertical-align: top;
}}

</style>
</head>
<body>

{page_footer}

{cover_html}

{body_html}

{footer_html}

{cta_html}

</body>
</html>'''


# ── PDF builder ─────────────────────────────────────────────────────────────

def build_pdf(input_path: Path, output_path: Path, cluster_key: str, az: str, kicker: str) -> None:
    text = input_path.read_text(encoding="utf-8")
    title, rest = extract_cover_title(text)
    subtitle, rest = extract_subtitle(rest)
    body_html = md_to_html(rest)
    body_html = postprocess_body_html(body_html, CLUSTERS[cluster_key]["accent"], CLUSTERS[cluster_key]["tint"])

    niche_name = input_path.parent.name
    html = render_full_html(title, subtitle, body_html, cluster_key, az, kicker, niche_name)

    with open(output_path, "wb") as out:
        result = pisa.CreatePDF(html, dest=out)
    if result.err:
        raise RuntimeError(f"{result.err} rendering error(s)")


# ── Main ────────────────────────────────────────────────────────────────────

def main() -> int:
    print(f"Building lead-magnet PDFs in {ROOT}\n")
    errors = []
    built = []

    for niche in NICHE_DIRS:
        lead_magnet = niche / "LEAD-MAGNET.md"
        if not lead_magnet.exists():
            print(f"SKIP {niche.name}: no LEAD-MAGNET.md")
            continue

        cluster_key = NICHE_CLUSTER.get(niche.name, "finanz")
        az = niche.name[:2]
        out = niche / "lead-magnet.pdf"
        try:
            build_pdf(lead_magnet, out, cluster_key, az, kicker="Kostenloser Lead-Magnet")
            print(f"[OK] {out.relative_to(ROOT)}")
            built.append((niche.name, "lead-magnet"))
        except Exception as e:
            print(f"[ERR] {niche.name}: {e}")
            errors.append((niche.name, str(e)))

    # Paid products
    for niche in NICHE_DIRS:
        paid = niche / "PAID-PRODUCT.md"
        if not paid.exists():
            continue
        cluster_key = NICHE_CLUSTER.get(niche.name, "finanz")
        az = niche.name[:2]
        out = niche / "paid-product.pdf"
        try:
            build_pdf(paid, out, cluster_key, az, kicker="Bezahltes Produkt")
            print(f"[OK] {out.relative_to(ROOT)}")
            built.append((niche.name, "paid-product"))
        except Exception as e:
            print(f"[ERR] {niche.name} paid-product: {e}")
            errors.append((f"{niche.name} paid-product", str(e)))

    print(f"\nBuilt: {len(built)} PDFs")
    if errors:
        print(f"Errors: {len(errors)}")
        for name, err in errors:
            print(f"  {name}: {err}")
        return 1

    print("\nAll PDFs built successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
