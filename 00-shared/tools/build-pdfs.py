#!/usr/bin/env python3
"""
Build PDF lead magnets from each niche's LEAD-MAGNET.md.

Renders real HTML/CSS (xhtml2pdf) instead of fpdf2's plain-text output, using
the same brand system as the website (Fraunces / IBM Plex, cluster colors).

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

from markdown import markdown
from xhtml2pdf import pisa

ROOT = Path(__file__).resolve().parents[2]
FONT_DIR = Path(__file__).resolve().parent / "fonts"

NICHE_DIRS = sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name[:2].isdigit()])

CLUSTERS = {
    "finanz": {"accent": "#1f6f5c", "tint": "#eef4f0", "label": "Finanz & Vorsorge"},
    "business": {"accent": "#3d4f8f", "tint": "#eef0f7", "label": "Business & Digital"},
    "alltag": {"accent": "#b0602c", "tint": "#f8f0e8", "label": "Alltag & Lifestyle"},
}

NICHE_CLUSTER = {
    "01-affiliate-marketing": "finanz",
    "03-pdfs-guides": "finanz",
    "05-lead-generation-pkv": "finanz",
    "08-app-ideen-appstore": "finanz",
    "09-finanzielle-freiheit": "finanz",
    "11-immobilien-baufinanzierung": "finanz",
    "04-ki-integrationen-35plus": "business",
    "07-marketing-agency-traffic": "business",
    "12-selbststaendigkeit-business-setup": "business",
    "02-tiktok-shop": "alltag",
    "06-lead-generation-dropshipping": "alltag",
    "10-gesundheit-praevention-40plus": "alltag",
    "13-reisen-lifestyle-35plus": "alltag",
    "14-nachhaltigkeit-eco": "alltag",
}

AMBER = "#b8842e"
INK = "#1c2333"
MUTED = "#5b5a6e"
PAPER = "#f6f1e7"


def extract_cover_title(text: str) -> tuple[str, str]:
    """Returns (title, rest_of_text_without_h1)."""
    lines = text.splitlines()
    title = "Lead-Magnet"
    for i, line in enumerate(lines):
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
            lines = lines[:i] + lines[i + 1 :]
            break
    return title, "\n".join(lines)


def style_checkboxes(md: str) -> str:
    md = re.sub(r"\[ \]", '<span class="chk"></span>', md)
    md = re.sub(r"\[[xX]\]", '<span class="chk chk-done"></span>', md)
    return md


def md_to_html(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2].lstrip("\n")
    text = style_checkboxes(text)
    html = markdown(text, extensions=["fenced_code", "tables", "nl2br"], output_format="html")
    return html


def font_face_css() -> str:
    """One distinct family name per weight — xhtml2pdf's CSS parser handles
    numeric font-weight matching in @font-face inconsistently, so we sidestep
    weight-matching entirely."""

    def url(name: str) -> str:
        return (FONT_DIR / name).resolve().as_uri()

    return f"""
    @font-face {{ font-family: 'Fraunces'; src: url('{url("Fraunces-Regular.ttf")}'); }}
    @font-face {{ font-family: 'FrauncesSemiBold'; src: url('{url("Fraunces-SemiBold.ttf")}'); }}
    @font-face {{ font-family: 'FrauncesDisplay'; src: url('{url("Fraunces-Bold72.ttf")}'); }}
    @font-face {{ font-family: 'Plex'; src: url('{url("IBMPlexSans-Regular.ttf")}'); }}
    @font-face {{ font-family: 'PlexMedium'; src: url('{url("IBMPlexSans-Medium.ttf")}'); }}
    @font-face {{ font-family: 'PlexSemiBold'; src: url('{url("IBMPlexSans-SemiBold.ttf")}'); }}
    @font-face {{ font-family: 'PlexMono'; src: url('{url("IBMPlexMono-Regular.ttf")}'); }}
    @font-face {{ font-family: 'PlexMonoMedium'; src: url('{url("IBMPlexMono-Medium.ttf")}'); }}
    """


def render_html(title: str, body_html: str, cluster_key: str, az: str, kicker: str) -> str:
    c = CLUSTERS[cluster_key]
    return f"""<html>
<head><style>
{font_face_css()}
@page {{ size: A4; margin: 2.4cm 2.2cm 2.6cm 2.2cm; }}
body {{ font-family: 'Plex'; font-size: 10.5pt; color: {INK}; line-height: 1.55; }}

.cover-band {{ background-color: {c['accent']}; height: 14pt; width: 100%; margin: -2.4cm -2.2cm 2.6cm -2.2cm; width: 21cm; }}
.cover-brand {{ font-family: 'FrauncesSemiBold'; font-size: 15pt; color: {INK}; }}
.cover-brand span {{ color: {AMBER}; }}
.cover-kicker {{ font-family: 'PlexMono'; font-size: 9pt; letter-spacing: 2pt; color: {MUTED}; margin-top: 60pt; }}
.cover-title {{ font-family: 'FrauncesDisplay'; font-size: 32pt; color: {INK}; margin-top: 14pt; line-height: 1.15; }}
.cover-az {{ font-family: 'PlexMono'; font-size: 10pt; color: {c['accent']}; margin-top: 20pt; }}
.cover-foot {{ font-family: 'PlexMono'; font-size: 8.5pt; color: {MUTED}; margin-top: 200pt; }}

h1 {{ font-family: 'FrauncesSemiBold'; font-size: 19pt; color: {INK}; margin-top: 22pt; margin-bottom: 8pt; border-bottom: 1pt solid {c['accent']}; padding-bottom: 6pt; }}
h2 {{ font-family: 'FrauncesSemiBold'; font-size: 14pt; color: {c['accent']}; margin-top: 16pt; margin-bottom: 6pt; }}
h3 {{ font-family: 'PlexSemiBold'; font-size: 11.5pt; color: {INK}; margin-top: 12pt; margin-bottom: 4pt; }}
p {{ margin: 6pt 0; }}
strong {{ color: {INK}; }}
em {{ color: {c['accent']}; font-style: normal; }}

ul, ol {{ margin: 6pt 0 6pt 14pt; padding: 0; }}
li {{ margin-bottom: 4pt; }}
.chk {{ display: inline-block; width: 8pt; height: 8pt; border: 1pt solid {INK}; margin-right: 5pt; }}
.chk-done {{ background-color: {c['accent']}; border-color: {c['accent']}; }}

table {{ width: 100%; border-collapse: collapse; margin: 10pt 0; font-size: 9.5pt; }}
th {{ background-color: {c['tint']}; color: {INK}; font-family: 'PlexSemiBold'; text-align: left; padding: 5pt 7pt; border-bottom: 1pt solid {c['accent']}; }}
td {{ padding: 5pt 7pt; border-bottom: 0.5pt solid #ddd; vertical-align: top; }}

blockquote {{ background-color: {c['tint']}; border-left: 2pt solid {c['accent']}; margin: 10pt 0; padding: 8pt 12pt; color: {INK}; }}

.footer-note {{ font-family: 'PlexMono'; font-size: 7.5pt; color: {MUTED}; margin-top: 24pt; border-top: 0.5pt solid #ddd; padding-top: 8pt; }}
</style></head>
<body>

<div class="cover-band"></div>
<div class="cover-brand">Empire<span>&middot;</span>Expansion</div>
<div class="cover-kicker">{kicker}</div>
<div class="cover-title">{title}</div>
<div class="cover-az">Aktenzeichen {az} &middot; {c['label']}</div>
<div class="cover-foot">ecom28.de &middot; Kostenloser Download &middot; Stand 2026</div>

<div style="page-break-before: always;"></div>
{body_html}

<div class="footer-note">Empire Expansion &middot; ecom28.de &middot; Dieser Guide ersetzt keine individuelle Rechts-, Steuer- oder Finanzberatung.</div>

</body>
</html>"""


def build_pdf(input_path: Path, output_path: Path, cluster_key: str, az: str, kicker: str) -> None:
    text = input_path.read_text(encoding="utf-8")
    title, rest = extract_cover_title(text)
    body_html = md_to_html(rest)
    html = render_html(title, body_html, cluster_key, az, kicker)

    with open(output_path, "wb") as out:
        result = pisa.CreatePDF(html, dest=out)
    if result.err:
        raise RuntimeError(f"{result.err} rendering error(s)")


def main() -> int:
    print(f"Building lead-magnet PDFs in {ROOT}\n")
    errors = []

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
        except Exception as e:
            print(f"[ERR] {niche.name}: {e}")
            errors.append((niche.name, str(e)))

    # Extra paid product for PDFs/guides niche
    paid = ROOT / "03-pdfs-guides" / "PAID-PRODUCT.md"
    if paid.exists():
        out = paid.parent / "paid-product.pdf"
        try:
            build_pdf(paid, out, "finanz", "03", kicker="Bezahlter Guide")
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
