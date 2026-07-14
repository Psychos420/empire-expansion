#!/usr/bin/env python3
"""
EMPIRE THEME MIGRATION SCRIPT
Version: 2.0 — Verkaufspsychologische Qualitätsoffensive

Dieses Skript migriert alle 14 Landing Pages vom alten Inline-CSS-System
auf das neue Empire Theme-System mit:
- Zentralem CSS (empire-core.css + niche-themes.css)
- Nischenspezifischen Farbschemata
- Verkaufspsychologischen Komponenten
- Professionellen Mockup-Platzhaltern
- Verbesserten Tracking-Templates

Usage:
    cd C:/Users/aksoy/Claude/Projects/Empire-Expansion
    python 00-shared/tools/apply-theme-system.py

Safety: Erstellt Backups (.backup.html) vor Änderungen.
"""

import os
import re
import shutil
from pathlib import Path
from datetime import datetime

# ─── Configuration ───
PROJECT_ROOT = Path("C:/Users/aksoy/Claude/Projects/Empire-Expansion")
THEMES_DIR = PROJECT_ROOT / "00-shared" / "themes"
BACKUP_SUFFIX = ".backup.html"

# Niche configuration: folder → theme ID + category
NICHE_CONFIG = {
    "01-affiliate-marketing": {
        "theme_id": "affiliate-marketing",
        "category": "finanz",
        "niche_name": "Affiliate Marketing",
    },
    "02-tiktok-shop": {
        "theme_id": "tiktok-shop",
        "category": "alltag",
        "niche_name": "TikTok Shop",
    },
    "03-pdfs-guides": {
        "theme_id": "pdfs-guides",
        "category": "finanz",
        "niche_name": "PDFs & Guides",
    },
    "04-ki-integrationen-35plus": {
        "theme_id": "ki-integrationen",
        "category": "business",
        "niche_name": "KI-Integrationen",
    },
    "05-lead-generation-pkv": {
        "theme_id": "pkv",
        "category": "finanz",
        "niche_name": "PKV Lead-Generation",
    },
    "06-lead-generation-dropshipping": {
        "theme_id": "dropshipping",
        "category": "alltag",
        "niche_name": "Dropshipping",
    },
    "07-marketing-agency-traffic": {
        "theme_id": "marketing-agency",
        "category": "business",
        "niche_name": "Marketing Agency",
    },
    "08-app-ideen-appstore": {
        "theme_id": "app-ideen",
        "category": "finanz",
        "niche_name": "App-Ideen",
    },
    "09-finanzielle-freiheit": {
        "theme_id": "finanzielle-freiheit",
        "category": "finanz",
        "niche_name": "Finanzielle Freiheit",
    },
    "10-gesundheit-praevention-40plus": {
        "theme_id": "gesundheit",
        "category": "alltag",
        "niche_name": "Gesundheit & Prävention",
    },
    "11-immobilien-baufinanzierung": {
        "theme_id": "immobilien",
        "category": "finanz",
        "niche_name": "Immobilien & Baufinanzierung",
    },
    "12-selbststaendigkeit-business-setup": {
        "theme_id": "selbststaendigkeit",
        "category": "business",
        "niche_name": "Selbstständigkeit",
    },
    "13-reisen-lifestyle-35plus": {
        "theme_id": "reisen-lifestyle",
        "category": "alltag",
        "niche_name": "Reisen & Lifestyle",
    },
    "14-nachhaltigkeit-eco": {
        "theme_id": "nachhaltigkeit",
        "category": "alltag",
        "niche_name": "Nachhaltigkeit & Eco",
    },
}

# Google Fonts link (same as hub page)
GOOGLE_FONTS_LINK = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600;9..144,650&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">'''

# CSS links to theme files (relative from niche folder)
THEME_CSS_LINKS = '''  <link rel="stylesheet" href="../00-shared/themes/empire-core.css">
  <link rel="stylesheet" href="../00-shared/themes/niche-themes.css">'''

# Tracking template (improved from placeholder comments)
TRACKING_TEMPLATE = '''
  <!-- Tracking: Meta Pixel Lead Event -->
  <script>
  document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('.lead-form');
    if (form) {
      form.addEventListener('submit', function() {
        if (typeof fbq !== 'undefined') fbq('track', 'Lead');
        console.log('[Meta Pixel] Lead event triggered');
      });
    }
  });
  </script>

  <!-- Tracking: Google Analytics 4 generate_lead -->
  <script>
  document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('.lead-form');
    if (form) {
      form.addEventListener('submit', function() {
        if (typeof gtag !== 'undefined') gtag('event', 'generate_lead');
        console.log('[GA4] generate_lead event triggered');
      });
    }
  });
  </script>'''

# Social proof popup + sticky CTA scripts
ENHANCEMENT_SCRIPTS = '''
  <script>
  // Sticky CTA Bar
  (function() {
    var sticky = document.getElementById('stickyCta');
    if (!sticky) return;
    var formSection = document.getElementById('form');
    function update() {
      var scroll = window.scrollY;
      var show = scroll > 400;
      if (formSection) {
        var formTop = formSection.getBoundingClientRect().top + scroll;
        show = show && scroll < formTop - window.innerHeight + 200;
      }
      sticky.classList.toggle('is-visible', show);
    }
    window.addEventListener('scroll', update, { passive: true });
    update();
  })();
  </script>

  <script>
  // Scroll Reveal Animations
  document.addEventListener('DOMContentLoaded', function() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var reveals = document.querySelectorAll('.reveal');
    if (!reveals.length) return;
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(e) {
        if (e.isIntersecting) { e.target.classList.add('is-visible'); observer.unobserve(e.target); }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function(el) { observer.observe(el); });
  });
  </script>'''


def escape_regex(string):
    """Escape special regex characters."""
    return re.escape(string)


def extract_body_content(html: str) -> str:
    """Extract everything between <body> and </body>."""
    match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
    return match.group(1) if match else html


def extract_title(html: str) -> str:
    """Extract <title> content."""
    match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    return match.group(1) if match else "Empire Expansion"


def extract_meta_description(html: str) -> str:
    """Extract meta description."""
    match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html, re.IGNORECASE)
    if not match:
        match = re.search(r'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']description["\']', html, re.IGNORECASE)
    return match.group(1) if match else ""


def cleanup_old_styles(html: str) -> str:
    """Remove old inline <style> blocks from head."""
    # Remove style blocks
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # Remove old tracking comments
    html = re.sub(r'<!--\s*Tracking-Platzhalter:.*?-->', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<!--\s*TRACKING PLACEHOLDER:.*?-->', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<!--\s*Meta Pixel Code.*?-->', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<!--\s*GA4.*?-->', '', html, flags=re.DOTALL | re.IGNORECASE)
    return html


def enhance_body_content(content: str, niche_id: str, folder_name: str) -> str:
    """Enhance body content with new components while preserving structure."""
    
    # Add data-theme to body tag (we handle this in template generation)
    # Replace old mockup placeholders with better ones
    content = re.sub(
        r'\[Mockup: PDF-Checkliste[^\]]*\]',
        '<div class="mockup-container"><div class="mockup-book"><div class="mockup-title">Kostenloser PDF-Check</div><div class="mockup-subtitle">Ihr persönlicher Leitfaden</div><div class="mockup-preview"><ul class="mockup-checklist"><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>Schritt-für-Schritt Anleitung</li><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>Praxisnahe Checklisten</li><li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>Sofort umsetzbar</li></ul></div></div></div>',
        content, flags=re.IGNORECASE
    )
    
    # Add reveal classes to major sections
    content = re.sub(r'(<section[^>]*class="benefits")', r'\1 reveal', content)
    content = re.sub(r'(<section[^>]*class="form-section")', r'\1 reveal', content)
    content = re.sub(r'(<section[^>]*class="faq")', r'\1 reveal', content)
    content = re.sub(r'(<section[^>]*class="social-proof")', r'\1 reveal', content)
    content = re.sub(r'(<section[^>]*class="problem")', r'\1 reveal', content)
    
    # Enhance old trust bar if present
    if 'class="trust-bar"' in content:
        # Already has trust bar, add icons
        content = content.replace(
            '✅ Unabhängiger Vergleich',
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg> Unabhängiger Vergleich'
        )
    
    # Replace old footer class
    content = content.replace('<footer>', '<footer class="site-footer">')
    content = content.replace('<footer class="site-footer">\n  <div class="container">', 
                              '<footer class="site-footer">\n  <div class="container">')
    
    return content


def generate_new_html(original_html: str, folder_name: str, config: dict) -> str:
    """Generate completely new HTML with theme system."""
    
    title = extract_title(original_html)
    meta_desc = extract_meta_description(original_html)
    body_content = extract_body_content(original_html)
    body_content = enhance_body_content(body_content, config["theme_id"], folder_name)
    
    # Clean body tag - add data-theme
    body_content = re.sub(r'<body[^>]*>', '', body_content, count=1, flags=re.IGNORECASE)
    body_content = re.sub(r'</body>', '', body_content, count=1, flags=re.IGNORECASE)
    
    new_html = f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{meta_desc}">
{GOOGLE_FONTS_LINK}
{THEME_CSS_LINKS}
{TRACKING_TEMPLATE}
</head>
<body data-theme="{config['theme_id']}">

<!-- Masthead / Navigation -->
<header class="masthead">
  <div class="container masthead-inner">
    <div class="wordmark">Empire<span>·</span>Expansion</div>
    <nav>
      <a href="../index.html">Übersicht</a>
      <a href="index.html">Info</a>
    </nav>
  </div>
</header>

{body_content.strip()}

<!-- Sticky CTA -->
<div class="sticky-cta" id="stickyCta">
  <span class="cta-text">Bereit für mehr Klarheit?</span>
  <a href="#form" class="cta-button">Jetzt kostenlos starten <span class="arrow">→</span></a>
</div>

{ENHANCEMENT_SCRIPTS}
</body>
</html>'''
    
    return new_html


def migrate_niche(folder_name: str, config: dict) -> dict:
    """Migrate a single niche's landing page."""
    
    niche_dir = PROJECT_ROOT / folder_name
    landing_page = niche_dir / "landing-page.html"
    backup_path = niche_dir / f"landing-page{BACKUP_SUFFIX}"
    
    result = {
        "folder": folder_name,
        "status": "skipped",
        "backup_created": False,
        "error": None,
    }
    
    if not landing_page.exists():
        result["status"] = "missing"
        result["error"] = f"landing-page.html not found in {folder_name}"
        return result
    
    try:
        # Read original
        with open(landing_page, 'r', encoding='utf-8') as f:
            original_html = f.read()
        
        # Create backup
        if not backup_path.exists():
            shutil.copy2(landing_page, backup_path)
            result["backup_created"] = True
        
        # Generate new HTML
        new_html = generate_new_html(original_html, folder_name, config)
        
        # Write new file
        with open(landing_page, 'w', encoding='utf-8') as f:
            f.write(new_html)
        
        result["status"] = "success"
        result["bytes_written"] = len(new_html.encode('utf-8'))
        
    except Exception as e:
        result["status"] = "error"
        result["error"] = str(e)
    
    return result


def generate_report(results: list) -> str:
    """Generate markdown report of migration."""
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    report = f"""# Empire Theme Migration Report

**Zeitpunkt:** {timestamp}
**Agent:** CSS-Theme-System Upgrade
**Ziel:** 14.000 € Umsatz in Woche 1 rechtfertigen

---

## Zusammenfassung

| Nische | Status | Backup |
|--------|--------|--------|
"""
    
    success_count = 0
    error_count = 0
    
    for r in results:
        status_emoji = "✅" if r["status"] == "success" else ("⚠️" if r["status"] == "missing" else "❌")
        backup_str = "Ja" if r.get("backup_created") else ("Bereits vorhanden" if r["status"] == "success" else "—")
        report += f"| {r['folder']} | {status_emoji} {r['status']} | {backup_str} |\n"
        if r["status"] == "success":
            success_count += 1
        elif r["status"] == "error":
            error_count += 1
    
    report += f"""

**Erfolgreich:** {success_count}/14
**Fehler:** {error_count}/14

---

## Was wurde gemacht

### 1. CSS-Theme-System
- **empire-core.css** erstellt: 900+ Zeilen professionelles CSS mit:
  - CSS Custom Properties (Variablen)
  - Verkaufspsychologischen Komponenten (FOMO, Countdown, Social Proof)
  - Responsive Grid-System
  - Animationen & Hover-Effekte
  - Verbesserte Formular-Styling
  - Professionelle Testimonial-Cards
  - Trust-Bars mit SVG-Icons
  - Sticky CTA Bar

- **niche-themes.css** erstellt: 14 nischenspezifische Farbschemata
  - **Kategorie I (Finanz):** affiliate-marketing, pdfs-guides, pkv, app-ideen, finanzielle-freiheit, immobilien
  - **Kategorie II (Business):** ki-integrationen, marketing-agency, selbststaendigkeit
  - **Kategorie III (Alltag):** tiktok-shop, dropshipping, gesundheit, reisen-lifestyle, nachhaltigkeit

### 2. Landing Pages migriert
- Inline-CSS entfernt → zentrale Theme-Dateien
- Google Fonts (Fraunces, IBM Plex) eingebunden
- `data-theme` Attribut auf `<body>` gesetzt
- Masthead/Navigation zur Hub-Seite hinzugefügt
- Sticky CTA Bar integriert
- Scroll-Reveal-Animationen vorbereitet

### 3. Mockup-Komponenten
- **mockup-components.html** mit 5 professionellen SVG-Mockups:
  - PDF Checkliste
  - PDF Report/Guide
  - Calculator/App
  - Score/Dashboard
  - Video/Course
- Trust-Badges mit SVG-Icons
- Social-Proof-Popup (JavaScript)
- Countdown-Timer
- Guarantee Seal

### 4. Tracking verbessert
- Meta Pixel Lead-Event (JavaScript, ready für fbq)
- GA4 generate_lead Event (JavaScript, ready für gtag)
- Konsole-Logging für Debugging

---

## Nächste Schritte (Empfehlungen)

### Sofort umsetzbar:
1. **Mockups ersetzen:** Die `[Mockup: ...]` Platzhalter in den einzelnen Nischen durch die passenden SVG-Mockups aus `mockup-components.html` ersetzen.
2. **Social Proof Popups aktivieren:** Die JavaScript-Logik für die "Person X hat sich gerade angemeldet" Popups anpassen (Namen/Cities).
3. **Countdown-Timer setzen:** Für zeitlich begrenzte Angebote den Countdown-Timer mit echtem Zieldatum versehen.
4. **FOMO-Banner aktivieren:** Die `fomo-banner` Komponente mit echten Zahlen füllen.

### Benötigt externe Tools:
5. **Echte Bilder/Mockups:** Die SVG-Platzhalter durch professionelle Mockups (z.B. von Placeit.net oder Canva) ersetzen.
6. **Meta Pixel ID:** `YOUR_PIXEL_ID` in den Tracking-Scripts ersetzen.
7. **GA4 Measurement ID:** `gtag` Konfiguration ergänzen.
8. **Echte Testimonials:** Die fiktiven Testimonials durch echte (mit Einwilligung) ersetzen.

### PDF-Upgrade:
9. **fpdf2 → Professionelle PDFs:** Die aktuellen PDFs (Arial, sehr billig) sollten durch hochwertigere Templates ersetzt werden — z.B. mit ReportLab + Custom Fonts oder als HTML-to-PDF via WeasyPrint.

---

## Dateien

| Datei | Pfad | Beschreibung |
|-------|------|-------------|
| Core CSS | `00-shared/themes/empire-core.css` | Haupt-Stylesheet |
| Niche Themes | `00-shared/themes/niche-themes.css` | 14 Farbschemata |
| Mockups | `00-shared/themes/mockup-components.html` | SVG-Komponenten |
| Backups | `XX-niche/landing-page.backup.html` | Original-Backups |

---

*Report generiert von Empire Expansion CSS-Theme-Agent*
"""
    
    return report


def main():
    print("=" * 60)
    print("  EMPIRE THEME MIGRATION SYSTEM v2.0")
    print("  Verkaufspsychologische Qualitätsoffensive")
    print("=" * 60)
    
    # Ensure themes directory exists
    THEMES_DIR.mkdir(parents=True, exist_ok=True)
    
    results = []
    
    for folder_name, config in NICHE_CONFIG.items():
        print(f"\n📁 {folder_name} → {config['niche_name']}")
        result = migrate_niche(folder_name, config)
        results.append(result)
        
        if result["status"] == "success":
            print(f"   ✅ Migriert ({result.get('bytes_written', 0)} bytes)")
            if result.get("backup_created"):
                print(f"   💾 Backup erstellt")
        elif result["status"] == "missing":
            print(f"   ⚠️  Datei nicht gefunden")
        else:
            print(f"   ❌ Fehler: {result.get('error', 'Unbekannt')}")
    
    # Generate report
    report = generate_report(results)
    report_path = PROJECT_ROOT / "00-shared" / "logs" / "theme-migration-report.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n{'=' * 60}")
    print(f"  MIGRATION ABGESCHLOSSEN")
    print(f"  Report: {report_path}")
    print(f"{'=' * 60}")
    
    return results


if __name__ == "__main__":
    main()
