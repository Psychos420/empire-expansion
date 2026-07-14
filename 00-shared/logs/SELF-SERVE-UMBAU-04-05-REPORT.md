# Self-Serve-Umbau-04-05 — Zusammenfassungs-Report

**Datum:** 2026-07-14  
**Agent:** Kimi (Subagent)  
**Aufgabe:** Self-Serve-Umbau der Landing Pages Nische 04 (KI-Integrationen) und Nische 05 (PKV)

---

## Was umgesetzt wurde

### Nische 04 — KI-Integrationen 35+ (Business: `#3d4f8f`)

**Dateien:** `index.html`, `landing-page.html`

| Änderung | Status |
|---|---|
| FOMO-Banner entfernt ("Nur 3 Erstgespräche diese Woche verfügbar" / "47 Unternehmer haben den Check bereits genutzt") | ✅ |
| Urgency-Box im Formular entfernt | ✅ |
| Social-Proof-Bar auf echte Produkte umgestellt (49 € Tool-Stack / 299 € Setup) | ✅ |
| Hero-CTA: Primär → `{{STRIPE_LINK}}` „KI-Tool-Stack + Vorlagen-Set kaufen — 49 € →" | ✅ |
| Sekundär-CTA: „Individuelles Setup ab 299 € buchen" (cal.com) | ✅ |
| Sticky-CTA auf Self-Serve umgestellt | ✅ |
| Price-Box auf Self-Serve-Produkt (49 €) umgestellt | ✅ |
| Formular-Header + Button auf Kauf-CTA umgestellt | ✅ |
| FAQ auf Self-Serve-Produkt und Produktvergleich umgestellt | ✅ |
| Hero-Note auf Garantie/Download umgestellt | ✅ |

### Nische 05 — PKV Lead Generation (Finanz: `#1f6f5c`)

**Dateien:** `index.html`, `landing-page.html`

| Änderung | Status |
|---|---|
| Urgency-Bar entfernt ("PKV-Alarm 2026") | ✅ |
| Farbschema auf Finanz `#1f6f5c` umgestellt (CSS-Variablen + hartkodierte Werte) | ✅ |
| Sticky-Nav-CTA auf `{{STRIPE_LINK}}` „Guide kaufen — 24 €" umgestellt | ✅ |
| Hero-CTA: Primär → `{{STRIPE_LINK}}` „PKV-Guide kaufen — 24 €" | ✅ |
| Sekundär-CTA: „Kostenlose Makler-Beratung →" (cal.com) | ✅ |
| Mockup-Caption auf Kauf umgestellt | ✅ |
| Scarcity-Box durch echte Marktdaten ersetzt (PKV-Verband, BaFin) | ✅ |
| Formular-Header + Button auf Kauf-CTA umgestellt | ✅ |
| Final-CTA auf Self-Serve + Makler-Beratung umgestellt | ✅ |
| FAQ „Kostenlos?" → Preis/Produkt umgestellt | ✅ |
| SVG-Farben im PDF-Mockup auf `#1f6f5c` / `#164c3e` angeglichen | ✅ |

---

## Commits

- **Commit:** `2a7b6cf` — `Self-Serve-Umbau Nischen 04 + 05: CTA-Struktur, Farben, Urgency-Entfernung`
- **Pushed:** `main` → `origin/main`

---

## Backups

- `04-ki-integrationen-35plus/*.backup-selfserve`
- `05-lead-generation-pkv/*.backup-selfserve`

---

## Offene Punkte / Hinweise für Claude

1. **Formular bleibt Web3Forms.** Die Formulare senden weiterhin Leads an Web3Forms. Für den Self-Serve-Checkout müssen die `{{STRIPE_LINK}}`-Buttons später durch echte Stripe/PayPal-Links ersetzt werden (Stop-Punkt laut Nutzer).

2. **CSS-Regeln für entfernte Klassen.** Die `.fomo-banner`- und `.urgency-box`-CSS-Regeln sind noch in den Stylesheets vorhanden (harmloser Dead Code), die zugehörigen HTML-Elemente wurden aber entfernt.

3. **Meta-Description noch alt.** Die `<meta name="description">` in 04 und 05 erwähnt teilweise noch den alten „kostenlosen Check" bzw. die „kostenlose Checkliste". Empfehlung: Kurz anpassen auf Self-Serve-Produkt.

4. **PDF-Mockup SVGs in 04.** Die SVG-Farben in 04 (`#00b8a9`, `#006266`) weichen leicht vom Business-Blau `#3d4f8f` ab. Sie sind nicht offensichtlich falsch, aber nicht 100 % konsistent mit dem Theme.

5. **Nische 05: Formular-Checkbox-Text.** Ein Checkbox-Label sagt noch: „Ich möchte den PKV-Guide per E-Mail erhalten." Das ist technisch korrekt, aber die Checkbox ist Teil des Web3Forms-Lead-Formulars, nicht des Checkout-Flows. Bei Stripe-Integration sollte das überdacht werden.

---

*Report erstellt. Bereit für Claude-Review.*
