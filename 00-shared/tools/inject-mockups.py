#!/usr/bin/env python3
"""
Empire Expansion — Landing Page Mockup Injector
Replaces [Mockup: ...] placeholders with professional SVG PDF mockups
and updates market data in all landing pages.

Usage:
    cd C:/Users/aksoy/Claude/Projects/Empire-Expansion
    .venv/Scripts/python 00-shared/tools/inject-mockups.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

NICHE_COLORS = {
    "01-affiliate-marketing":       {"primary": "#16213e", "accent": "#ffb800", "label": "Gold"},
    "02-tiktok-shop":               {"primary": "#8338ec", "accent": "#ff0080", "label": "Magenta"},
    "03-pdfs-guides":               {"primary": "#2d3436", "accent": "#ff6b35", "label": "Orange"},
    "04-ki-integrationen-35plus":   {"primary": "#006266", "accent": "#00b8a9", "label": "Teal"},
    "05-lead-generation-pkv":       {"primary": "#003366", "accent": "#0094d6", "label": "Medizin"},
    "06-lead-generation-dropshipping":{"primary": "#2a2a2a", "accent": "#2ed573", "label": "Grün"},
    "07-marketing-agency-traffic":  {"primary": "#1e1e1e", "accent": "#e74c3c", "label": "Rot"},
    "08-app-ideen-appstore":        {"primary": "#353b48", "accent": "#9b59b6", "label": "Lila"},
    "09-finanzielle-freiheit":      {"primary": "#16213e", "accent": "#ffb800", "label": "Gold"},
    "10-gesundheit-praevention-40plus":{"primary": "#004d40", "accent": "#00e676", "label": "Health"},
    "11-immobilien-baufinanzierung":{"primary": "#3e2723", "accent": "#8d6e63", "label": "Braun"},
    "12-selbststaendigkeit-business-setup":{"primary": "#212121", "accent": "#ff9800", "label": "Amber"},
    "13-reisen-lifestyle-35plus":   {"primary": "#1565c0", "accent": "#00b0ff", "label": "Ocean"},
    "14-nachhaltigkeit-eco":        {"primary": "#1b5e20", "accent": "#4caf50", "label": "Eco"},
}

NICHE_TITLES = {
    "01-affiliate-marketing": "Der Finanzielle Freiheit-Check für 40+",
    "02-tiktok-shop": "TikTok Shop Masterguide 2026",
    "03-pdfs-guides": "PDF-Profit-Strategie 2026",
    "04-ki-integrationen-35plus": "KI-Automatisierung für Ihr Business",
    "05-lead-generation-pkv": "PKV-Wechsel-Checkliste 2026",
    "06-lead-generation-dropshipping": "Dropshipping Launch-Plan 2026",
    "07-marketing-agency-traffic": "Traffic-Agentur Start-Guide",
    "08-app-ideen-appstore": "App-Store Goldmine 2026",
    "09-finanzielle-freiheit": "Der Finanzielle Freiheit-Check für 40+",
    "10-gesundheit-praevention-40plus": "Gesundheit-Check für 40+",
    "11-immobilien-baufinanzierung": "Bauzins-Checkliste Juli 2026",
    "12-selbststaendigkeit-business-setup": "Business-Setup Guide 2026",
    "13-reisen-lifestyle-35plus": "Reise-Freiheits-Guide 2026",
    "14-nachhaltigkeit-eco": "Eco-Profit Strategie 2026",
}

NICHE_SUBTITLES = {
    "01-affiliate-marketing": "Kostenloser PDF-Check für Berufstätige 40+",
    "05-lead-generation-pkv": "Beihilfe + Restkostenversicherung = optimale Absicherung",
    "11-immobilien-baufinanzierung": "Bauzinsen 3,39%: Jetzt sichern vor dem Herbst-Anstieg",
    "09-finanzielle-freiheit": "10M Kunden vertrauen diesem System. Starten Sie jetzt.",
    "07-marketing-agency-traffic": "Bis 1.750 EUR Provision pro Lead - wöchentliche Auszahlung",
    "04-ki-integrationen-35plus": "KI-Agentur ab 299 EUR statt 990-1.500 EUR Marktpreis",
}


def generate_mockup_svg(niche_key: str) -> str:
    """Generate a professional inline SVG mockup of the PDF cover."""
    colors = NICHE_COLORS.get(niche_key, NICHE_COLORS["01-affiliate-marketing"])
    title = NICHE_TITLES.get(niche_key, "Lead-Magnet")
    subtitle = NICHE_SUBTITLES.get(niche_key, "Kostenloser PDF-Download")
    
    svg = f'''<!-- Professional PDF Mockup -->
<div style="max-width: 320px; margin: 0 auto 24px; filter: drop-shadow(0 12px 24px rgba(0,0,0,0.15)); transform: rotate(-1deg);">
<svg viewBox="0 0 320 420" xmlns="http://www.w3.org/2000/svg" style="width:100%; height:auto; border-radius: 8px;">
  <defs>
    <filter id="shadow" x="-10%" y="-10%" width="130%" height="130%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="{colors["primary"]}" flood-opacity="0.2"/>
    </filter>
  </defs>
  
  <!-- Document background -->
  <rect x="0" y="0" width="320" height="420" rx="6" fill="#ffffff" filter="url(#shadow)"/>
  
  <!-- Top accent bar -->
  <rect x="0" y="0" width="320" height="8" rx="6" fill="{colors["accent"]}"/>
  <rect x="0" y="8" width="320" height="4" fill="{colors["accent"]}"/>
  
  <!-- Right side accent block -->
  <rect x="220" y="0" width="100" height="160" rx="6" fill="{colors["accent"]}" opacity="0.9"/>
  
  <!-- Empire Expansion logo area -->
  <text x="20" y="32" font-family="system-ui, -apple-system, sans-serif" font-size="9" font-weight="700" fill="{colors["primary"]}">EMPIRE EXPANSION</text>
  
  <!-- Free badge -->
  <rect x="20" y="45" width="120" height="18" rx="9" fill="{colors["accent"]}"/>
  <text x="80" y="57" font-family="system-ui, -apple-system, sans-serif" font-size="8" font-weight="700" fill="#ffffff" text-anchor="middle">KOSTENLOSER DOWNLOAD</text>
  
  <!-- Main title -->
  <text x="20" y="110" font-family="Georgia, serif" font-size="18" font-weight="700" fill="{colors["primary"]}">{title}</text>
  
  <!-- Subtitle -->
  <text x="20" y="140" font-family="system-ui, -apple-system, sans-serif" font-size="10" fill="#666666">{subtitle}</text>
  
  <!-- Bottom dark bar with details -->
  <rect x="0" y="340" width="320" height="80" rx="6" fill="{colors["primary"]}"/>
  <text x="20" y="365" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="#ffffff" opacity="0.9">ecom28.de | hallo@ecom28.de</text>
  <text x="20" y="382" font-family="system-ui, -apple-system, sans-serif" font-size="8" fill="#ffffff" opacity="0.9">cal.com/empire-expansion</text>
  <text x="20" y="400" font-family="system-ui, -apple-system, sans-serif" font-size="7" fill="#ffffff" opacity="0.6">Teil des Empire-Expansion-Oekosystems</text>
  
  <!-- Decorative page lines -->
  <line x1="20" y1="170" x2="180" y2="170" stroke="#e0e0e0" stroke-width="1"/>
  <line x1="20" y1="185" x2="160" y2="185" stroke="#e0e0e0" stroke-width="1"/>
  <line x1="20" y1="200" x2="190" y2="200" stroke="#e0e0e0" stroke-width="1"/>
  <line x1="20" y1="215" x2="140" y2="215" stroke="#e0e0e0" stroke-width="1"/>
  <line x1="20" y1="230" x2="170" y2="230" stroke="#e0e0e0" stroke-width="1"/>
  <line x1="20" y1="245" x2="150" y2="245" stroke="#e0e0e0" stroke-width="1"/>
  <line x1="20" y1="260" x2="180" y2="260" stroke="#e0e0e0" stroke-width="1"/>
  <line x1="20" y1="275" x2="160" y2="275" stroke="#e0e0e0" stroke-width="1"/>
  <line x1="20" y1="290" x2="190" y2="290" stroke="#e0e0e0" stroke-width="1"/>
  <line x1="20" y1="305" x2="170" y2="305" stroke="#e0e0e0" stroke-width="1"/>
  
  <!-- Checklist checkbox simulation -->
  <rect x="20" y="178" width="6" height="6" fill="none" stroke="{colors["primary"]}" stroke-width="0.5" rx="1"/>
  <rect x="20" y="193" width="6" height="6" fill="none" stroke="{colors["primary"]}" stroke-width="0.5" rx="1"/>
  <rect x="20" y="208" width="6" height="6" fill="none" stroke="{colors["primary"]}" stroke-width="0.5" rx="1"/>
  <rect x="20" y="223" width="6" height="6" fill="none" stroke="{colors["primary"]}" stroke-width="0.5" rx="1"/>
  <rect x="20" y="238" width="6" height="6" fill="none" stroke="{colors["primary"]}" stroke-width="0.5" rx="1"/>
  <rect x="20" y="253" width="6" height="6" fill="none" stroke="{colors["primary"]}" stroke-width="0.5" rx="1"/>
  <rect x="20" y="268" width="6" height="6" fill="none" stroke="{colors["primary"]}" stroke-width="0.5" rx="1"/>
  <rect x="20" y="283" width="6" height="6" fill="none" stroke="{colors["primary"]}" stroke-width="0.5" rx="1"/>
  <rect x="20" y="298" width="6" height="6" fill="none" stroke="{colors["primary"]}" stroke-width="0.5" rx="1"/>
  
  <!-- Checkmark in some boxes -->
  <path d="M22 180 l1 1.5 l2 -2.5" stroke="{colors["accent"]}" stroke-width="0.8" fill="none" stroke-linecap="round"/>
  <path d="M22 210 l1 1.5 l2 -2.5" stroke="{colors["accent"]}" stroke-width="0.8" fill="none" stroke-linecap="round"/>
  <path d="M22 240 l1 1.5 l2 -2.5" stroke="{colors["accent"]}" stroke-width="0.8" fill="none" stroke-linecap="round"/>
  <path d="M22 270 l1 1.5 l2 -2.5" stroke="{colors["accent"]}" stroke-width="0.8" fill="none" stroke-linecap="round"/>
  
  <!-- Corner fold effect -->
  <polygon points="320,0 320,30 290,0" fill="{colors["primary"]}" opacity="0.1"/>
</svg>
</div>'''
    return svg


def inject_mockup(html_path: Path, niche_key: str) -> bool:
    """Replace mockup placeholders with professional SVG."""
    if not html_path.exists():
        return False
    
    text = html_path.read_text(encoding="utf-8")
    
    # Don't double-inject
    if '<svg viewBox="0 0 320 420"' in text:
        print(f"  SKIP {niche_key}: mockup already present")
        return True
    
    # Find and replace mockup placeholder
    mockup_patterns = [
        r'<div class="mockup">\s*\[Mockup:[^\]]*\]\s*(?:<br>\s*<span class="badge">[^<]*</span>)?\s*</div>',
        r'\[Mockup:[^\]]*\]',
    ]
    
    svg = generate_mockup_svg(niche_key)
    replaced = False
    
    for pattern in mockup_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            text = re.sub(pattern, svg, text, count=1, flags=re.IGNORECASE)
            replaced = True
            break
    
    if not replaced:
        # If no placeholder found, insert after hero h2
        hero_h2 = re.search(r'(<h2>.*?</h2>\s*<p>.*?</p>)', text, re.DOTALL)
        if hero_h2:
            insert_pos = hero_h2.end()
            text = text[:insert_pos] + "\n" + svg + text[insert_pos:]
            replaced = True
    
    if replaced:
        html_path.write_text(text, encoding="utf-8")
        print(f"  OK {niche_key}: mockup injected")
    else:
        print(f"  WARN {niche_key}: no mockup placeholder found")
    
    return replaced


def update_market_data(html_path: Path, niche_key: str) -> bool:
    """Add market data badges to specific niches."""
    if not html_path.exists():
        return False
    
    text = html_path.read_text(encoding="utf-8")
    
    # Don't double-inject
    if 'market-data-badge' in text:
        return True
    
    badge_html = ""
    if niche_key == "05-lead-generation-pkv":
        badge_html = '''<div class="market-data-badge" style="background: #003366; color: white; padding: 12px 16px; border-radius: 8px; margin: 16px 0; text-align: center; font-size: 0.9rem;">
      <strong>AKTUELLE MARKTLAGE 2026:</strong> ~60% der Privatversicherten betroffen. Ø 10-13% Erhöhung, teils bis 40% (VKB). <strong>Jetzt handeln.</strong>
    </div>'''
    elif niche_key == "11-immobilien-baufinanzierung":
        badge_html = '''<div class="market-data-badge" style="background: #3e2723; color: white; padding: 12px 16px; border-radius: 8px; margin: 16px 0; text-align: center; font-size: 0.9rem;">
      <strong>BAUZINSEN JULI 2026:</strong> 10J-Festsatz 3,39%. Leicht gesunken vs. März, aber Experten erwarten Herbst-Anstieg. <strong>Jetzt sichern.</strong>
    </div>'''
    elif niche_key == "09-finanzielle-freiheit":
        badge_html = '''<div class="market-data-badge" style="background: #16213e; color: white; padding: 12px 16px; border-radius: 8px; margin: 16px 0; text-align: center; font-size: 0.9rem;">
      <strong>TRADE REPUBLIC 2026:</strong> 10 Millionen Kunden, 150 Mrd. EUR AUM. Cash-Zins 2,25% p.a. <strong>Jetzt starten.</strong>
    </div>'''
    elif niche_key == "07-marketing-agency-traffic":
        badge_html = '''<div class="market-data-badge" style="background: #1e1e1e; color: white; padding: 12px 16px; border-radius: 8px; margin: 16px 0; text-align: center; font-size: 0.9rem;">
      <strong>TARIFCHECK.DE 2026:</strong> Bis 1.750 EUR Provision pro Lead, wöchentliche Auszahlung. <strong>Jetzt aufbauen.</strong>
    </div>'''
    elif niche_key == "04-ki-integrationen-35plus":
        badge_html = '''<div class="market-data-badge" style="background: #006266; color: white; padding: 12px 16px; border-radius: 8px; margin: 16px 0; text-align: center; font-size: 0.9rem;">
      <strong>KI-AGENTUR MARKT 2026:</strong> Marktpreis 990-1.500 EUR+. Empire Expansion ab 299 EUR. <strong>Jetzt automatisieren.</strong>
    </div>'''
    
    if badge_html:
        # Insert before the first CTA button in hero section
        cta_pattern = re.compile(r'(<a href="#form" class="cta-button">.*?</a>)', re.IGNORECASE | re.DOTALL)
        match = cta_pattern.search(text)
        if match:
            insert_pos = match.start()
            text = text[:insert_pos] + badge_html + "\n    " + text[insert_pos:]
            html_path.write_text(text, encoding="utf-8")
            print(f"  OK {niche_key}: market data badge added")
            return True
    
    return False


def main():
    print("=" * 60)
    print("EMPIRE EXPANSION — Landing Page Mockup Injector")
    print("Injecting SVG mockups and market data badges")
    print("=" * 60)
    
    niches = sorted([d for d in ROOT.iterdir() if d.is_dir() and d.name[:2].isdigit()])
    total = 0
    
    for niche in niches:
        html_path = niche / "landing-page.html"
        niche_key = niche.name
        print(f"\n[{niche_key}]")
        
        if inject_mockup(html_path, niche_key):
            total += 1
        
        update_market_data(html_path, niche_key)
    
    print(f"\n{'=' * 60}")
    print(f"Done: {total} landing pages updated with mockups")
    print("=" * 60)


if __name__ == "__main__":
    main()
