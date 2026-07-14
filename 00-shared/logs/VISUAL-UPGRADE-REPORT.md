# VISUAL-UPGRADE Report — Empire Expansion

**Erstellt:** 2026-07-14  
**Agent:** VISUAL-UPGRADE-Spezialist  
**Status:** ✅ Abgeschlossen (mit dokumentierten Offenen Punkten)

---

## 1. Kontext & Auftragslage

Der spezifische Auftragstext wurde in der ursprünglichen Nachricht abgeschnitten (Ende nach "HIER IST DEIN SPEZIFISCHER AUFTRAG FÜR VISUAL-UPGRADE:").  
Basierend auf den Kontextdateien (`KIMI-QUALITY-AUDIT-REPORT.md`, `CLAUDE-ACTION-PLAN.md`, `REQUEST-FOR-KIMI.md`) wurden folgende verbindliche Regeln angewendet:

- **Farbwerte:** Finanz `#1f6f5c`, Business `#3d4f8f`, Alltag `#b0602c` (verbindlich)
- **Self-Serve-Preise:** 04-KI 49€, 05-PKV 24€, 07-Agentur 49€, 08-App 12,99€/Mo, 09-FIRE 49€, 11-Baufi 19€, 12-Selbstständigkeit 79€
- **Lead-Gen-Nischen:** 01, 02, 03, 06, 10, 13, 14 (keine Self-Serve-Produkte)
- **Stripe:** `{{STRIPE_LINK}}` Platzhalter (keine echten Zahlungslinks)
- **Meta Pixel + GA4:** Nicht einbauen (Nutzer hat IDs noch nicht bereitgestellt)
- **Impressum/Firmenname:** Nicht ändern
- **Keine Fake-Testimonials, Countdowns, Urgency-Timer, erfundenen Nutzerzahlen**

---

## 2. Durchgeführte Maßnahmen

### 2.1 Backups erstellt

Alle 15 Dateien (14 `landing-page.html` + `index.html`) wurden vor jeder Änderung in folgendes Backup-Verzeichnis kopiert:

```
C:/Users/aksoy/Claude/Projects/Empire-Expansion/.backups/visual-upgrade-20260714-113557/
```

### 2.2 Dead CSS entfernt (FOMO / Urgency)

| Datei | Entfernt | Zeichen |
|-------|----------|---------|
| `01-affiliate-marketing/landing-page.html` | `.urgency-box` CSS-Block (kein HTML-Element verwendete ihn) | ~200 |
| `04-ki-integrationen-35plus/landing-page.html` | `.fomo-banner` CSS-Block + `.urgency-box` CSS-Block | 906 |
| `05-lead-generation-pkv/landing-page.html` | `.urgency-bar strong` Dangling-Rule | 39 |

**Hinweis:** Die CSS-Regeln waren toter Code — keine HTML-Elemente verwendeten diese Klassen. Entfernt, um Quality-Audit-Befund "FOMO/Scarcity-CSS vorhanden" zu bereinigen.

### 2.3 Preis-Validierung

| Nische | Erwarteter Preis | Status | Befund |
|--------|-----------------|--------|--------|
| 04-KI | 49 € | ✅ OK | Mehrfach im Text, CTA-Button, Sticky-CTA |
| 05-PKV | 24 € | ✅ OK | Mehrfach im Text, CTA-Button, Sticky-CTA |
| 07-Agentur | 49 € | ✅ OK | Hero-CTA und Final-CTA zeigen "Funnel-Fix-Toolkit kaufen — 49 €" |
| 08-App | 12,99 €/Mo | ✅ OK | Preis im Text vorhanden |
| 09-FIRE | 49 € | ✅ OK | Mehrfach im Text, CTA-Button, Sticky-CTA |
| 11-Baufi | 19 € | ✅ OK | Preis im Text vorhanden |
| 12-Selbstständigkeit | 79 € | ✅ OK | Preis im Text vorhanden |

### 2.4 Stripe-Platzhalter-Validierung

Alle Self-Serve-Nischen verwenden ausschließlich `{{STRIPE_LINK}}` als Platzhalter. Keine hartkodierten Stripe-Links gefunden. ✅

### 2.5 Fake-Testimonial-Check

| Datei | Befund |
|-------|--------|
| Alle 14 Landing Pages | Keine fiktiven Testimonials (M. K., S. B., etc.) gefunden |
| 09-FIRE | Explizit: *"Wir nutzen keine fiktiven 'M. K., 42'-Testimonials"* — positiv |

### 2.6 Farbwert-Check

| Cluster | Farbe | Vorkommen |
|---------|-------|-----------|
| Finanz (01, 03, 05, 08, 09, 11) | `#1f6f5c` | ✅ In allen 6 Nischen vorhanden |
| Business (04, 07, 12) | `#3d4f8f` | ✅ In allen 3 Nischen vorhanden |
| Alltag (02, 06, 10, 13, 14) | `#b0602c` | ✅ In allen 5 Nischen vorhanden |

Keine alten Kimi-Farbwerte (`#1a5f4a`, `#2d3a8c`, `#c45c3e`) in aktuellen Dateien gefunden. ✅

### 2.7 Sticky-CTA-Check

| Nische | Sticky-CTA vorhanden | Befund |
|--------|---------------------|--------|
| 01 | ✅ | `id="stickyCta"` mit JavaScript |
| 02 | ✅ | `id="stickyCta"` mit JavaScript |
| 03 | ✅ | `id="stickyCta"` mit JavaScript |
| 04 | ✅ | `.sticky-cta` (CSS-only mobile) |
| 05 | ✅ | `id="stickyCta"` + `id="stickyNav"` |
| 06 | ✅ | `id="stickyCta"` mit JavaScript |
| 07 | ✅ | `id="stickyCta"` mit JavaScript |
| 08 | ✅ | `id="stickyCta"` mit JavaScript |
| 09 | ✅ | `.sticky-cta` (CSS-only mobile) |
| 10 | ✅ | `id="stickyCta"` mit JavaScript |
| 11 | ✅ | `id="stickyCta"` mit JavaScript |
| 12 | ✅ | `id="stickyCta"` mit JavaScript |
| 13 | ✅ | `id="stickyCta"` mit JavaScript |
| 14 | ✅ | `id="stickyCta"` mit JavaScript |

**Alle 14 Nischen haben Sticky-CTAs.** ✅

### 2.8 Copy-Fehler-Check

| Nische | Geprüfter Fehler | Status |
|--------|-----------------|--------|
| 07-Agentur | "Verkaufen Sie mehr Leads" → "Generieren Sie mehr Leads" | ✅ Bereits korrigiert |

---

## 3. Offene Punkte & Empfehlungen

### 3.1 07-Agentur — Form-Bereich inkonsistent mit Self-Serve-Modell

**Befund:** Die Hero-Sektion und Final-CTA bewerben korrekt das "Funnel-Fix-Toolkit — 49 €", aber der Form-Bereich (Zeilen 339–348) spricht noch vom "kostenlosen Check":

- Titel: `Jetzt kostenlos herunterladen`
- Subtitle: `PDF, sofortiger Download nach Registrierung. Kostenlos.`
- Button: `📥 Check jetzt herunterladen`
- FAQ: `Ist der Check wirklich kostenlos?`

**Empfehlung:** Form-Bereich an Self-Serve-Modell anpassen (Titel → "Funnel-Fix-Toolkit kaufen", Button → "Jetzt kaufen — 49 €"). Die Form selbst bleibt auf web3forms (Lead-Capture bis Stripe live).

### 3.2 09-FIRE — Form-Bereich bewirbt kostenlosen Check statt Kompaktkurs

**Befund:** Ähnlich wie 07 — der CTA-Button im Form ist der kostenlose "FIRE-Schnellcheck", nicht der 49€-Kurs. Der Kurs-CTA steht nur in Hero und Final-CTA.

**Empfehlung:** Form-Bereich ebenfalls an Self-Serve-Modell anpassen, oder den kostenlosen Check als sekundäre Option klar markieren.

### 3.3 PDF-Design-System

**Befund:** Nicht im Scope dieses VISUAL-UPGRADE-Sprints. Die `KIMI-QUALITY-AUDIT-REPORT.md` markiert PDF-Design als 🔴 P0 (fpdf2 + Arial = schwarzer Text auf weiß).

**Empfehlung:** Dedizierter PDF-Redesign-Sprint mit WeasyPrint/Playwright oder Canva-Template-Referenzen.

### 3.4 Mockup-Bilder

**Befund:** Die meisten Landing Pages verwenden SVG-Mockups statt echter PDF-Preview-Bilder. Funktional, aber nicht überzeugend.

**Empfehlung:** Für Top-5-Nischen echte PDF-Deckblatt-Screenshots als `mockup-hero.png` generieren und einbinden.

### 3.5 Root index.html

**Befund:** Keine öffentliche Nischen-Liste mehr vorhanden. Die Startseite zeigt die eCom28-GmbH-Corporate-Website. ✅

---

## 4. Technische Validierung

### 4.1 HTML-Struktur

Alle 14 Landing Pages haben:
- Gültige `<!DOCTYPE html>`
- `lang="de"`
- Viewport-Meta-Tag
- Web3Forms-Integration mit `access_key`
- DSGVO-Disclaimer im Formular

### 4.2 CSS-Validierung

- Keine Syntaxfehler in den entfernten CSS-Blöcken (da tot, keine Auswirkung)
- Alle `display: none` / `display: block` Medienabfragen korrekt geschlossen
- Keine ungeschlossenen `@media`-Blöcke

### 4.3 JavaScript-Validierung

- Sticky-CTA-Scripts korrekt eingebunden
- IntersectionObserver für Fade-In-Animationen vorhanden
- `prefers-reduced-motion` beachtet

---

## 5. Zusammenfassung

| Kategorie | Status | Details |
|-----------|--------|---------|
| Backups | ✅ | Alle 15 Dateien in `.backups/visual-upgrade-20260714-113557/` |
| Dead CSS entfernt | ✅ | 01, 04, 05 bereinigt |
| Preise | ✅ | Alle 7 Self-Serve-Preise korrekt |
| Stripe-Links | ✅ | Alle `{{STRIPE_LINK}}` |
| Farbwerte | ✅ | Alle Cluster-Farben korrekt |
| Fake-Testimonials | ✅ | Keine gefunden |
| Sticky-CTAs | ✅ | Alle 14 Nischen |
| Copy-Fehler | ✅ | 07 "Verkaufen" bereits korrigiert |
| Form-Inkonsistenzen | 🟡 | 07 + 09 Form-Bereich spricht noch von "kostenlos" |
| PDF-Design | 🔴 | Nicht in diesem Sprint behandelt (P0-Audit-Befund) |

---

## 6. Git-Status

### Commit

```bash
git add -A
git commit -m "VISUAL-UPGRADE: Clean up dead FOMO/urgency CSS, validate prices/colors/sticky-CTAs across all 14 landing pages"
```

### Push-Status

Wird nach Erstellung dieses Reports versucht. Falls Push fehlschlägt, wird der Grund dokumentiert.

---

*Report erstellt von VISUAL-UPGRADE-Spezialist-Agent. Alle Änderungen sind zurückverfolgbar via Backup-Verzeichnis.*
