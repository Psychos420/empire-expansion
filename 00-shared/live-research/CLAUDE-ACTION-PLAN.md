# Claude Action Plan — Empire Expansion Quality Upgrade Sprint
**Erstellt:** 2026-07-14 von Kimi (Session 11)  
**Status:** 🔴 DRINGEND — Nutzer ist mit Website + PDFs unzufrieden  
**Ziel:** Landing Pages + PDFs so überzeugend machen, dass sie 14.000 € in Woche 1 rechtfertigen

---

## Wichtig für Claude

> **Der Nutzer hat explizit gesagt:** „Ich bin mit der Website und den PDFs etc noch nicht zufrieden. Bitte im agentswarm ausbauen und Claude helfen, dies so überzeugend zu machen wie es nur geht!!!"

Das bedeutet: Der bisherige Fokus auf „Funktionalität" (Formulare funktionieren, Links sind gesetzt) reicht nicht. Es braucht einen **Upgrade-Sprint auf Verkaufspsychologie + Visuelles Design**.

---

## Phase 1: Sofortmaßnahmen (P0 — Heute)

### 1.1 Landing Pages: Mockups + Bilder einfügen

**Problem:** Jede Landing Page hat nur Text-Platzhalter wie „[Mockup: PDF-Checkliste]". Das wirkt wie eine unfertige Baustelle.

**Lösung:**
1. Erstelle für jede Top-5-Nische ein **visuelles Mockup** des Lead-Magneten:
   - Ein Deckblatt-Preview (mit Titel, Farben, Branding)
   - Eine aufgeklappte Seite mit Checkliste
   - Ein „3D-Stack"-Bild (mehrere Seiten überlappend)
2. Nutze **Canva Free** oder HTML/CSS-Generator-Skripte, um diese Mockups zu erstellen.
3. Speichere sie als `mockup-hero.png` in jedem Nischen-Ordner.
4. Ersetze den Text-Platzhalter in der Landing Page durch das echte Bild.

**Beispiel für 01-Affiliate:**
```html
<!-- Statt: -->
<div class="mockup">[Mockup: PDF-Checkliste Titelblatt + aufgeklappte Checkliste]</div>

<!-- Jetzt: -->
<div class="mockup-img">
  <img src="mockup-hero.png" alt="Der Finanzielle Freiheit-Check für 40+ — 12 Seiten, kostenlos" 
       style="max-width:100%; border-radius:12px; box-shadow:0 10px 40px rgba(0,0,0,0.15);">
</div>
```

### 1.2 Testimonials: Entweder entfernen oder glaubwürdiger machen

**Problem:** „M. K., 42, Selbstständig" und „S. B., 48, Angestellter" sind offensichtlich fiktiv. Das zerstört Vertrauen sofort.

**Option A (empfohlen):** Entferne alle fiktiven Testimonials. Ersetze durch:
- **Nutzungsstatistiken:** „Bisher 500+ Downloads" (aber nur wenn wahr)
- **Prozess-Garantien:** „DSGVO-konform, keine Werbung, jederzeit abbestellbar"
- **Transparenz-Statements:** „Kein Versicherungsfachchinesisch, keine versteckten Kosten"

**Option B:** Wenn Testimonials bleiben sollen, nutze zumindest **realistischere Namen und Berufsbezeichnungen** plus ein Foto-Placeholder. Aber ohne echte Fotos bleibt es schwierig.

**Empfehlung an Nutzer:** Sammle echte Testimonials von den ersten 5–10 Leads, die sich anmelden. Bis dahin: Keine fiktiven Zitate.

### 1.3 Social Proof durch Daten ersetzen

**Beispiele für bessere Social Proof-Elemente:**

| Nische | Statt... | Besser... |
|--------|----------|-----------|
| 01 Affiliate | „500+ Downloads 2025" | „12-seitiger Check, der in 15 Minuten Klarheit bringt" |
| 05 PKV | „500+ Downloads 2025" + „15–25 % Einsparung" | „2026: 60 % der Privatversicherten betroffen. Prüfen Sie, ob Sie dabei sind." + Quelle verlinken |
| 04 KI | „Geschäftsführer, B2B-Dienstleistung" | „In 5 Minuten 12 Fragen zu Ihren Prozessen" |

---

## Phase 2: Design-Upgrade (P1 — Heute/Morgen)

### 2.1 Nischen-spezifische Farbschemas

**Problem:** Alle Nischen haben exakt dieselben Farben (Dunkelblau + Coral-Pink).

**Lösung:** Definiere für jeden Cluster ein Farbschema und passe die CSS-Variablen an.

| Cluster | Primär | Sekundär | Akzent | Grund |
|---------|--------|----------|--------|-------|
| **Finanz & Vorsorge** (01, 03, 05, 08, 09, 11) | #1a5f4a (Dunkelgrün) | #c9a227 (Gold) | #f4f3ee (Cremeweiß) | Vertrauen, Reichtum, Stabilität |
| **Business & Digital** (04, 07, 12) | #2d3a8c (Königsblau) | #00d4aa (Tech-Grün) | #f8fafc (Cool-Weiß) | Professionalität, Innovation |
| **Alltag & Lifestyle** (02, 06, 10, 13, 14) | #c45c3e (Terrakotta) | #5a9e6e (Natur-Grün) | #faf6f1 (Warm-Weiß) | Lebensfreude, Natur, Gesundheit |

**Umsetzung:** Erstelle für jede Nische eine `custom-theme.css`, die die CSS-Variablen überschreibt. Im `<head>` der Landing Page einbinden.

### 2.2 Sticky CTA auf allen mobilen Seiten

**Problem:** Nur 04-KI hat eine Sticky CTA. Die anderen Nischen verlieren Mobile-User, die nach unten scrollen.

**Lösung:** Kopiere den Sticky-CTA-Code aus 04-KI in alle anderen Landing Pages.

```html
<div class="sticky-cta">
  <a href="#form" class="cta-button">[NISCHEN-SPEZIFISCHER CTA]</a>
</div>
```

### 2.3 Meta Pixel + GA4 Tracking endlich einbauen

**Problem:** Tracking-Platzhalter sind seit Woche 1 nur Kommentare. Ohne Tracking kein Retargeting, keine Conversion-Optimierung.

**Lösung:**
1. Erstelle Meta Pixel (wenn noch nicht geschehen — Stop-Punkt? Nein, Pixel ist kostenlos)
2. Erstelle GA4 Property
3. Ersetze die Kommentar-Platzhalter durch echte Tracking-Codes
4. Events: `PageView`, `Lead`, `InitiateCheckout` (für Stripe/PayPal-Links)

---

## Phase 3: PDF-Redesign (P1 — Morgen)

### 3.1 Problem: fpdf2 + Arial ist kein Design

**Aktuell:** PDFs werden aus Markdown mit fpdf2 gebaut. Das Ergebnis ist schwarzer Text auf weißem Grund mit Arial 11pt.

**Ziel:** Professionelle Lead-Magnete, die wie aus einem Verlag aussehen.

### 3.2 Sofort-Lösung: HTML → PDF über Headless Chrome

**Empfohlener Ansatz:**
1. Erstelle für jeden Lead-Magneten ein **HTML-Template** mit professionellem CSS:
   - Cover-Page mit Hintergrundfarbe/Gradient, Titel, Subtitle, Branding
   - Inhaltsverzeichnis mit Seitenzahlen
   - Kapitel-Seiten mit farbigen Überschriften, Infoboxen, Zitate
   - Checklisten mit gestalteten Checkboxen (SVG oder Unicode ✓)
   - Footer mit Seitenzahl, Disclaimer, Impressum-Link
2. Nutze **Playwright/Chrome Headless** oder **weasyprint**, um HTML → PDF zu konvertieren.
3. Alternative: **Canva Free** — manuelle Erstellung der ersten 5 PDFs, dann als Template duplizieren.

**Warum das wichtig ist:** Ein Lead-Magnet ist der erste physische Kontakt mit der Marke. Wenn das PDF billig aussieht, wirkt die gesamte Marke billig.

### 3.3 Cover-Page-Template (HTML/CSS)

Jedes PDF braucht ein Cover mit:
- Titel (groß, bold, Brand-Farbe)
- Untertitel (mittel, secondary color)
- „Kostenloser Download / Empire Expansion" Branding
- Datum / Version
- Visuelles Element (Icon, Pattern, oder nische-spezifische Grafik)

---

## Phase 4: Copy-Upgrade (P1 — Morgen/Übermorgen)

### 4.1 Headlines mit aktuellen Zahlen

| Nische | Alte Headline | Neue Headline (mit Kimi-Daten) |
|--------|---------------|--------------------------------|
| 05 PKV | „PKV für Beamte 2026" | „2026: 60 % der Privatversicherten zahlen mehr — prüfen Sie Ihren Tarif in 10 Minuten" |
| 11 Immobilien | „Baufi-Readiness-Check" | „Bauzinsen bei 3,39 % — Experten erwarten Anstieg im Herbst. Prüfen Sie jetzt Ihre Readiness" |
| 04 KI | „KI-Potenzial-Check" | „Wo verliert Ihr Unternehmen 5–40 Stunden/Woche? Der 5-Minuten-Check" |
| 09 FIRE | „FIRE-Schnellcheck für 35+" | „Ihre Rente reicht nicht? 10 Fragen, die Ihre Rentenlücke aufdecken" |

### 4.2 Preis-Teaser bei 04-KI korrigieren

**Problem:** „Setup ab 1.990 €" ist abschreckend für einen ersten Kontakt.

**Lösung:** Preis-Ankertaktik:
- Statt: „Setup ab 1.990 €"
- Besser: „Marktpreis für KI-Implementierung: 3.000–5.000 €. Unser Einstieg: 299 € Erstgespräch + individuelles Konzept"
- Oder: „Kostenloser KI-Check → Dann entscheiden Sie, ob der 299 €-Starter für Sie passt"

---

## Phase 5: Agent-Swarm-Strategie (P2 — Laufend)

### Wie Claude und Kimi parallel arbeiten

| Aufgabe | Wer | Wann | Output |
|---------|-----|------|--------|
| Markt-Recherche, Zahlen, Trends | Kimi | Kontinuierlich | `MARKET-UPDATES.md`, `TREND-ALERTS.md` |
| Landing Page Design-Upgrade | Claude | Heute | Neue CSS, Mockups, Farbschemas |
| PDF-Redesign | Claude | Morgen | Neue HTML-Templates, Headless-PDF-Build |
| Copy-Upgrade mit aktuellen Zahlen | Claude | Heute/Morgen | Neue Headlines, Social Proof, CTA-Texte |
| Qualitäts-Check nach jedem Upgrade | Kimi | Nach jedem Sprint | `KIMI-QUALITY-AUDIT-REPORT.md` Update |
| Neue Anfragen an Kimi | Claude | Bei Bedarf | `REQUEST-FOR-KIMI.md` |

### Kommunikationsprotokoll

1. Claude liest bei jedem Start: `KIMI-QUALITY-AUDIT-REPORT.md`, `MARKET-UPDATES.md`, `REQUEST-FOR-KIMI.md`
2. Kimi aktualisiert nach jeder Recherche: `KIMI-LIVE-RESEARCH.md`, `MARKET-UPDATES.md`
3. Claude dokumentiert seine Upgrades in: `CLAUDE-SESSION-LOG.md`
4. Wenn Claude Daten braucht, die Kimi nicht hat: `REQUEST-FOR-KIMI.md` mit konkreter Frage

---

## Phase 6: Sofortige Aktionen für die nächste Session

### Claude, bei deiner nächsten Session sofort:

1. **Lies diesen Action Plan** + `KIMI-QUALITY-AUDIT-REPORT.md`
2. **Starte mit P0:** Erstelle Mockup-Bilder für die Top-5-Nischen (Canva Free oder HTML/CSS)
3. **Entferne fiktive Testimonials** oder ersetze sie durch datenbasierten Social Proof
4. **Passe die Headlines an** mit den aktuellen Zahlen aus `MARKET-UPDATES.md` (Update 7)
5. **Füge Sticky CTAs** zu allen Landing Pages hinzu
6. **Ersetze "500+ Downloads 2025"** durch aktuelle, ehrliche Aussagen
7. **Dokumentiere alles** in `CLAUDE-SESSION-LOG.md`

---

## Nutzer-Stop-Punkte in diesem Sprint

| Stop-Punkt | Grund | Wann nötig |
|------------|-------|------------|
| **PayPal Business Konto eröffnen** | Zahlungsdaten | Sobald Landing Pages überzeugend sind |
| **Echte Testimonials sammeln** | Authentizität | Nach den ersten 5–10 Leads |
| **Meta Pixel + GA4 einrichten** | Tracking-Setup | Kein Stop-Punkt, aber Nutzer sollte wissen, dass Tracking läuft |
| **Domain/DNS-Änderungen** | Technische Kontrolle | Nur falls erneut nötig |

---

> **Ziel:** In 2–3 Sessions sollen die Top-5-Nischen so überzeugend aussehen, dass der Nutzer sagt: „Das sieht aus wie ein echtes, professionelles Unternehmen." Nicht mehr: „Das sieht aus wie eine Template-Übung."

*Action Plan erstellt von Kimi. Claude: Bitte diesen Plan als Roadmap für die nächsten Sessions nutzen. Bei Fragen → `REQUEST-FOR-KIMI.md`.*
