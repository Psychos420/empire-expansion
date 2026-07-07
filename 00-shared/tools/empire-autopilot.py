#!/usr/bin/env python3
"""
Empire Expansion — Autonomer Launch-Controller

Dieses Skript automatisert so weit wie möglich den Launch aller 14 Nischen:
- Prüft Ordnerstruktur und Assets
- Baut alle Lead-Magnet-PDFs neu
- Prüft Landing Pages auf Platzhalter
- Ersetzt Platzhalter, wenn empire-config.json vorhanden ist
- Generiert Outreach-Vorlagen und Content für Woche 1
- Erstellt einen Launch-Status-Report

Stop-Punkte (menschlicher Eingriff nötig):
- Zahlungsdaten (Stripe, PayPal, Brevo-Kauf)
- Persönliche Kontakte für Outreach
- Rechtsform/Geschäftsadresse
- Video-Aufnahmen
- Ausgaben > 50 €
"""

import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Windows-Konsole auf UTF-8 umstellen, damit Emojis korrekt ausgegeben werden
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[2]
TOOLS_DIR = ROOT / "00-shared" / "tools"
CONFIG_PATH = ROOT / "empire-config.json"
TEMPLATE_PATH = ROOT / "empire-config-template.json"
GENERATED_DIR = ROOT / "00-shared" / "generated-content"
REPORT_PATH = ROOT / "LAUNCH-STATUS-REPORT.md"

NICHE_FOLDERS = [
    "01-affiliate-marketing",
    "02-tiktok-shop",
    "03-pdfs-guides",
    "04-ki-integrationen-35plus",
    "05-lead-generation-pkv",
    "06-lead-generation-dropshipping",
    "07-marketing-agency-traffic",
    "08-app-ideen-appstore",
    "09-finanzielle-freiheit",
    "10-gesundheit-praevention-40plus",
    "11-immobilien-baufinanzierung",
    "12-selbststaendigkeit-business-setup",
    "13-reisen-lifestyle-35plus",
    "14-nachhaltigkeit-eco",
]

REQUIRED_FILES = ["README.md", "LEAD-MAGNET.md", "landing-page.html", "lead-magnet.pdf", "WEEK-1-TASKS.md"]

PLACEHOLDERS = ["{{FORM_ACTION}}", "{{CAL_LINK}}", "{{STRIPE_LINK}}", "{{PAYPAL_LINK}}", "{{META_PIXEL}}", "{{GA4_ID}}"]


def log(msg: str) -> None:
    print(f"[Empire Autopilot] {msg}")


def ensure_config() -> dict:
    """Liest Config oder erstellt Template und beendet sich."""
    if CONFIG_PATH.exists():
        log("✅ empire-config.json gefunden.")
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))

    log("⚠️  empire-config.json nicht gefunden. Erstelle Template...")
    template = {
        "brand": {
            "name": "Empire Expansion",
            "domain": "empire-expansion.de",
            "email": "hallo@empire-expansion.de"
        },
        "tools": {
            "brevo": {"account_name": "Empire Expansion", "sender_email": "hallo@empire-expansion.de"},
            "cal": {"base_url": "https://empire-expansion.cal.com"},
            "stripe": {"account_email": ""},
            "paypal": {"account_email": ""},
            "github": {"username": "", "repo": "empire-expansion"}
        },
        "niches": {folder: {"brevo_form_url": "", "cal_link": "", "stripe_link": ""} for folder in NICHE_FOLDERS}
    }
    TEMPLATE_PATH.write_text(json.dumps(template, indent=2), encoding="utf-8")
    log(f"📝 Template erstellt: {TEMPLATE_PATH}")
    log("⛔ STOP: Bitte fülle empire-config.json aus und starte erneut.")
    sys.exit(0)


def check_folders() -> dict:
    """Prüft alle Nischen-Ordner auf Vollständigkeit."""
    log("🔍 Prüfe Nischen-Ordner...")
    status = {}
    for folder in NICHE_FOLDERS:
        path = ROOT / folder
        folder_status = {"exists": path.exists(), "files": {}, "missing": []}
        for file in REQUIRED_FILES:
            exists = (path / file).exists()
            folder_status["files"][file] = exists
            if not exists:
                folder_status["missing"].append(file)
        status[folder] = folder_status
    return status


def rebuild_pdfs() -> bool:
    """Baut alle PDFs neu."""
    log("📄 Baue alle Lead-Magnet-PDFs neu...")
    build_script = TOOLS_DIR / "build-pdfs.py"
    if not build_script.exists():
        log("❌ build-pdfs.py nicht gefunden.")
        return False
    try:
        result = subprocess.run(
            [sys.executable, str(build_script)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True
        )
        log(result.stdout.strip()[-500:])  # Letzte 500 Zeichen
        log("✅ PDFs erfolgreich neu gebaut.")
        return True
    except subprocess.CalledProcessError as e:
        log(f"❌ Fehler beim PDF-Build: {e.stderr}")
        return False


def check_landing_pages() -> dict:
    """Findet Platzhalter in Landing Pages."""
    log("🌐 Prüfe Landing Pages auf Platzhalter...")
    findings = {}
    for folder in NICHE_FOLDERS:
        html_path = ROOT / folder / "landing-page.html"
        if not html_path.exists():
            continue
        text = html_path.read_text(encoding="utf-8")
        found = [ph for ph in PLACEHOLDERS if ph in text]
        findings[folder] = found
    return findings


def patch_landing_pages(config: dict) -> dict:
    """Ersetzt Platzhalter in Landing Pages durch echte Werte aus Config."""
    log("🔧 Patche Landing Pages mit Config-Werten...")
    results = {}
    for folder in NICHE_FOLDERS:
        html_path = ROOT / folder / "landing-page.html"
        if not html_path.exists():
            continue
        text = html_path.read_text(encoding="utf-8")
        original = text
        niche_config = config.get("niches", {}).get(folder, {})
        brand = config.get("brand", {})

        replacements = {
            "{{FORM_ACTION}}": niche_config.get("brevo_form_url", "{{FORM_ACTION}}"),
            "{{CAL_LINK}}": niche_config.get("cal_link", "{{CAL_LINK}}"),
            "{{STRIPE_LINK}}": niche_config.get("stripe_link", "{{STRIPE_LINK}}"),
            "{{PAYPAL_LINK}}": niche_config.get("paypal_link", "{{PAYPAL_LINK}}"),
            "{{BRAND_NAME}}": brand.get("name", "Empire Expansion"),
            "{{BRAND_EMAIL}}": brand.get("email", "hallo@empire-expansion.de"),
        }

        for placeholder, value in replacements.items():
            if value and placeholder != value:
                text = text.replace(placeholder, value)

        if text != original:
            html_path.write_text(text, encoding="utf-8")
            results[folder] = "patched"
        else:
            results[folder] = "no_change_or_missing_values"
    return results


def sync_index_html() -> None:
    """Kopiert landing-page.html nach index.html, damit GitHub Pages beim Aufruf des
    nackten Ordnerpfads (ohne Dateinamen) immer die aktuelle, gepatchte Seite zeigt."""
    log("🔗 Synchronisiere index.html mit landing-page.html...")
    for folder in NICHE_FOLDERS:
        src = ROOT / folder / "landing-page.html"
        dst = ROOT / folder / "index.html"
        if src.exists():
            shutil.copyfile(src, dst)
    log("✅ index.html synchronisiert.")


def generate_outreach_templates() -> None:
    """Generiert Outreach-Vorlagen für LinkedIn/WhatsApp/E-Mail."""
    log("✉️  Generiere Outreach-Vorlagen...")
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    date_str = datetime.now().strftime("%y%m%d")
    out_dir = GENERATED_DIR / f"{date_str}-outreach-templates"
    out_dir.mkdir(exist_ok=True)

    template = """# Outreach-Vorlagen für {folder}

## LinkedIn-Verbindungsanfrage
Hallo [Name],

ich arbeite aktuell an einem Projekt für [Zielgruppe] und helfe dabei, [Schmerzpunkt] zu lösen. Dein Profil passt gut in die Zielgruppe — würde mich freuen, dich hier zu vernetzen.

Liebe Grüße
[Dein Name]

## LinkedIn Direktnachricht (nach Akzeptanz)
Danke für die Verbindung, [Name].

Ich habe gerade einen kostenlosen [Lead-Magnet-Name] erstellt, der [ konkreter Nutzen ]. Falls das für dich relevant ist, schicke ich dir gerne den Link.

Liebe Grüße
[Dein Name]

## WhatsApp / persönliche Nachricht
Hey [Name],

ich habe gerade ein kleines Projekt gestartet: [Kurzbeschreibung]. Dachte, das könnte dich interessieren, weil [persönlicher Bezug]. Hier ist der Link zum kostenlosen [Lead-Magnet]: [URL]

Viel Spaß damit!

## Follow-up nach 48h
Hallo [Name],

hast du schon einen Blick riskiert? Falls du Fragen hast oder kurz sprechen möchtest, sag einfach Bescheid.

Liebe Grüße
[Dein Name]
"""

    for folder in NICHE_FOLDERS:
        (out_dir / f"{folder}.md").write_text(template.format(folder=folder), encoding="utf-8")
    log(f"✅ Outreach-Vorlagen gespeichert in {out_dir}")


def generate_content_plan() -> None:
    """Generiert einen einfachen Content-Plan für Woche 1."""
    log("📅 Generiere Content-Plan...")
    date_str = datetime.now().strftime("%y%m%d")
    out_dir = GENERATED_DIR / f"{date_str}-content-plan"
    out_dir.mkdir(exist_ok=True)

    plan = """# Empire Expansion — Content-Plan Woche 1

## Tägliche Mindestaktivität pro Nische
- 1 LinkedIn-Post (Mo–Fr)
- 3 sachliche Kommentare unter fremden Posts
- 1 Post in passender Facebook-Gruppe (nur wo erlaubt)

## Woche-1-Post-Themen (pro Nische anpassen)
| Tag | Thema | CTA |
|-----|-------|-----|
| Tag 1 | Persönliche Story: Warum dieses Thema wichtig ist | Link zur Landing Page |
| Tag 2 | Der größte Fehler, den ich bei [Thema] sehe | Kommentar + Link |
| Tag 3 | 3 schnelle Tipps für [Zielgruppe] | Lead-Magnet downloaden |
| Tag 4 | Kundenstory / hypothetisches Beispiel | Termin buchen |
| Tag 5 | Mythos vs. Wahrheit | Lead-Magnet downloaden |
| Tag 6 | Wochenrückblick + CTA | Termin buchen / Produkt |
| Tag 7 | Häufigste Frage beantworten | Link zur Landing Page |

## Hashtags (je Nische auswählen)
#Altersvorsorge #Rente #ETF #FinanzielleFreiheit #KI #Automatisierung #Mittelstand #Selbststaendigkeit #PKV #Beamte #Baufinanzierung #Gesundheit #Plastikfrei #SlowTravel #35plus #40plus

## LinkedIn-Post-Struktur
1. Hook (erste 2 Zeilen)
2. Kurze Story oder Problem
3. 3–5 Bulletpoints mit Lösung
4. Klaren CTA
5. 3–5 Hashtags
"""
    (out_dir / "CONTENT-PLAN-WEEK-1.md").write_text(plan, encoding="utf-8")
    log(f"✅ Content-Plan gespeichert in {out_dir}")


def generate_report(folder_status: dict, placeholders: dict, patched: dict, pdf_ok: bool) -> None:
    """Erstellt den Launch-Status-Report."""
    log("📊 Erstelle Launch-Status-Report...")
    lines = [
        "# Empire Expansion — Launch-Status-Report",
        f"**Erstellt:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Zusammenfassung",
        "",
        f"- PDFs neu gebaut: {'✅ Ja' if pdf_ok else '❌ Nein'}",
        f"- Landing Pages gepatched: {sum(1 for v in patched.values() if v == 'patched')} von {len(NICHE_FOLDERS)}",
        f"- Nischen mit fehlenden Dateien: {sum(1 for s in folder_status.values() if s['missing'])}",
        f"- Nischen mit noch vorhandenen Platzhaltern: {sum(1 for p in placeholders.values() if p)}",
        "",
        "## Ordner-Status",
        "",
        "| Nische | Vollständig | Fehlende Dateien |",
        "|--------|-------------|------------------|",
    ]
    for folder in NICHE_FOLDERS:
        s = folder_status[folder]
        status = "✅" if not s["missing"] else "❌"
        missing = ", ".join(s["missing"]) if s["missing"] else "-"
        lines.append(f"| {folder} | {status} | {missing} |")

    lines.extend([
        "",
        "## Platzhalter in Landing Pages",
        "",
        "| Nische | Noch vorhandene Platzhalter |",
        "|--------|-----------------------------|",
    ])
    for folder in NICHE_FOLDERS:
        ph = ", ".join(placeholders.get(folder, [])) if placeholders.get(folder) else "-"
        lines.append(f"| {folder} | {ph} |")

    lines.extend([
        "",
        "## Nächste manuelle Schritte",
        "",
        "1. `empire-config.json` ausfüllen (falls noch nicht geschehen).",
        "2. Brevo-Account anlegen und Domain verifizieren.",
        "3. Cal.com-Account anlegen und Terminbuchungslinks erstellen.",
        "4. GitHub-Repository anlegen und GitHub Pages aktivieren.",
        "5. Stripe/PayPal-Zahlungslinks für Produkt-/Dienstleistungs-Nischen erstellen.",
        "6. Persönliche Outreach-Listen für Top-5-Nischen erstellen.",
        "7. Erste LinkedIn-/Facebook-Posts veröffentlichen.",
        "",
        "---",
        "",
        "**Hinweis:** Dieser Report wird bei jedem Autopilot-Lauf neu generiert.",
    ])

    REPORT_PATH.write_text("\n".join(lines), encoding="utf-8")
    log(f"✅ Report gespeichert: {REPORT_PATH}")


def main():
    log("🚀 Starte Empire Autopilot...")
    config = ensure_config()
    folder_status = check_folders()
    pdf_ok = rebuild_pdfs()
    placeholders = check_landing_pages()
    patched = patch_landing_pages(config)
    sync_index_html()
    generate_outreach_templates()
    generate_content_plan()
    generate_report(folder_status, placeholders, patched, pdf_ok)
    log("✅ Autopilot-Sequenz abgeschlossen.")
    log(f"📄 Öffne {REPORT_PATH} für den nächsten Schritt.")


if __name__ == "__main__":
    main()
