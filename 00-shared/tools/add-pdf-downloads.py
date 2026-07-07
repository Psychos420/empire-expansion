#!/usr/bin/env python3
"""
Fügt in jede landing-page.html einen direkten PDF-Download-Link hinzu,
ohne das bestehende Formular / den {{FORM_ACTION}}-Platzhalter zu entfernen.
- Erster Hero-CTA bekommt einen sekundären "PDF direkt herunterladen"-Link.
- Nach dem Formular-Submit-Button wird ein Fallback-Link eingefügt.
"""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SECONDARY_STYLE = """    .cta-button.secondary { background: #16213e; margin-left: 0; margin-top: 12px; }
    .cta-button.secondary:hover { background: #0f172a; }
"""


def process_file(folder: Path) -> bool:
    html_path = folder / "landing-page.html"
    pdf_path = folder / "lead-magnet.pdf"
    if not html_path.exists():
        print(f"  SKIP: {html_path} nicht gefunden")
        return False
    if not pdf_path.exists():
        print(f"  SKIP: {pdf_path} nicht gefunden")
        return False

    text = html_path.read_text(encoding="utf-8")
    pdf_name = "lead-magnet.pdf"

    # CSS für sekundären Button hinzufügen (falls noch nicht vorhanden)
    if ".cta-button.secondary" not in text:
        text = text.replace("</style>", SECONDARY_STYLE + "</style>", 1)

    # 1) Ersten Hero-CTA erweitern
    # Suche nach dem ersten <a href="#form" class="cta-button">...</a>
    hero_pattern = re.compile(
        r'(<a href="#form" class="cta-button">.*?</a>)',
        re.IGNORECASE | re.DOTALL,
    )
    hero_match = hero_pattern.search(text)
    if hero_match:
        existing = hero_match.group(1)
        # Nur einfügen, wenn noch nicht vorhanden
        if 'href="lead-magnet.pdf"' not in text[: hero_match.end() + 200]:
            download_link = f'\n    <a href="{pdf_name}" class="cta-button secondary" download>PDF direkt herunterladen</a>'
            text = text[: hero_match.end()] + download_link + text[hero_match.end() :]

    # 2) Nach dem ersten Submit-Button einen Fallback-Link einfügen
    submit_pattern = re.compile(r'(<button type="submit">.*?</button>)', re.IGNORECASE | re.DOTALL)
    submit_match = submit_pattern.search(text)
    if submit_match:
        if 'href="lead-magnet.pdf"' not in text[submit_match.end() - 100 : submit_match.end() + 300]:
            fallback = (
                '\n    <p class="disclaimer" style="margin-top: 20px;">'
                f'<a href="{pdf_name}" download>PDF ohne Anmeldung herunterladen</a></p>'
            )
            text = text[: submit_match.end()] + fallback + text[submit_match.end() :]

    html_path.write_text(text, encoding="utf-8")
    print(f"  OK: {folder.name}")
    return True


def main():
    folders = sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name[:2].isdigit()])
    for folder in folders:
        process_file(folder)


if __name__ == "__main__":
    main()
