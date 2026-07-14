# PDF-Redesign-Report — Empire Expansion Lead-Magnet Pipeline

**Datum:** 2026-07-14  
**Status:** ✅ Abgeschlossen  
**Tool:** xhtml2pdf (bestehende Pipeline, erweitert)  
**Backup:** `.backups/pdf-redesign-2026-07-14-1219/build-pdfs.py`

---

## 1. Was am Template geändert wurde

### 1.1 Titel- & Subtitle-Extraktion (Bugfixes)

| Problem | Lösung |
|---------|--------|
| `# LEAD-MAGNET.md` wurde als Cover-Titel genommen | `extract_cover_title()` überspringt jetzt filename-only Headings (`LEAD-MAGNET.md`, `PAID-PRODUCT.md`, `README.md`, `INDEX.md`) und entfernt sie aus dem Body |
| `**Format:** Interaktiver Online-Check + PDF-Report` wurde als Subtitle genommen | `extract_subtitle()` strippt Markdown-Bold-Marker (`**`) vor dem Prefix-Check und überspringt alle Format-/Zielgruppen-/Titel-/Subheadline-Blöcke |
| Erstes H1 erzeugte leere Seite nach Cover | `page-break-before` auf dem ersten H1 entfernt (da Cover bereits `page-break-after` hat) |

### 1.2 Cover-Seite — Full-Page Cluster-Branding

- **Technik:** `position: absolute; top: -2cm; left: -2.2cm; right: -2.2cm; bottom: -2.4cm;` um die Seitenränder zu überschreiben
- **Hintergrund:** Cluster-Farbe (`#1f6f5c` Finanz, `#3d4f8f` Business, `#b0602c` Alltag)
- **Kicker:** `Kostenloser Lead-Magnet` bzw. `Bezahltes Produkt` — PlexMono, 9pt, Uppercase, Letter-Spacing 2.5pt
- **Titel:** FrauncesDisplay, 28pt, Weiß, max. 75% Breite, zentriert
- **Subtitle:** Plex, 12pt, 85% Weiß-Opacity
- **Footer auf Cover:** Aktenzeichen + Cluster-Label + eCom28 GmbH + Empire·Expansion (Amber-Akzent)

### 1.3 Kapitelseiten — Farbiger Streifen + Nummerierung

- Jede H1-Überschrift wird zu einer Kapitelseite:
  - 8pt Farbiger Streifen oben (Cluster-Akzent)
  - "Kapitel"-Label in PlexMono, 10pt, Cluster-Farbe
  - Titel in FrauncesSemiBold, 22pt
  - Ab dem 2. H1: `page-break-before: always` (erstes H1 beginnt direkt nach Cover)

### 1.4 Infoboxen — Blockquotes → Styled Callouts

- Blockquotes werden zu abgerundeten Boxen mit:
  - Hintergrund: Cluster-Tint (`#eef4f0`, `#eef0f7`, `#f8f0e8`)
  - 4pt linker Rand in Cluster-Akzent
  - "Hinweis"-Label in PlexSemiBold, Uppercase
  - Inhalt in Plex, 10pt

### 1.5 Checklisten — Checkbox-Symbole

- Markdown `[ ]` → `☐` (unchecked), `[x]` → `☑` (checked)
- Checklist-Items werden in einem hellgrauen Rahmen (`#f5f5f5`) mit abgerundeten Ecken gruppiert
- Checkbox in PlexMono, 11pt, Cluster-Farbe für checked

### 1.6 Stat-Bars — Visuelle Prozentbalken

- Wenn Tabellenzellen Prozentwerte enthalten (z.B. "60%"):
  - Prozentwert wird in PlexMono, 8pt angezeigt
  - Horizontaler Balken: Hintergrund `#dddddd`, Fill in Cluster-Akzent, Höhe 4pt, abgerundet

### 1.7 CTA-Seite — Letzte Seite jedes PDFs

- Full-Page Cluster-Farbe (wie Cover, aber am Ende)
- "Nächster Schritt"-Label
- Produktname (aus Nischen-Ordner abgeleitet)
- Preis aus Live-Research (keine fiktiven Zahlen):
  - PKV: `kostenloser 15-Minuten-Check`
  - KI/Agency/Business: `ab 299 €`
  - FIRE/Immobilien/App: `Strategiegespräch ab 199 €`
  - Affiliate: `kostenloser Download`
  - Lifestyle/Dropshipping/TikTok/Gesundheit/Reisen/Eco: `ab 49 €`
- CTA-Button-Style: Weißer Hintergrund, Cluster-Farbe Text, abgerundet
- `{{STRIPE_LINK}}` Platzhalter unverändert
- eCom28 GmbH · Bremen · HRB 39329 HB

### 1.8 Fußzeile — Seitenzahlen

- xhtml2pdf-native `<pdf:pagefooter>` mit `<pdf:pagenumber/>`
- Zentriert, PlexMono, 8pt, `#999999`
- Disclaimer am Ende des Body-Content (vor CTA): Empire Expansion · ecom28.de · Haftungsausschluss

### 1.9 Typografie & Farben

| Element | Font | Größe | Farbe |
|---------|------|-------|-------|
| Cover-Titel | FrauncesDisplay | 28pt | Weiß |
| Kapitel-Titel | FrauncesSemiBold | 22pt | `#1c2333` |
| H2 | FrauncesSemiBold | 15pt | Cluster-Akzent |
| H3 | PlexSemiBold | 12pt | `#1c2333` |
| Body | Plex | 10.5pt | `#1c2333` |
| Code/Mono | PlexMono | 8.5–9pt | `#1c2333` |
| Tabellen-Header | PlexSemiBold | 9.5pt | Cluster-Tint Hintergrund |
| Tabellen-Zellen | Plex | 9.5pt | `#1c2333` |

**Cluster-Farben:**
- Finanz (`01, 03, 05, 08, 09, 11`): `#1f6f5c` (Grün)
- Business (`04, 07, 12`): `#3d4f8f` (Blau)
- Alltag (`02, 06, 10, 13, 14`): `#b0602c` (Orange/Braun)

---

## 2. Screenshots-Beschreibungen der neuen PDF-Seiten

### Seite 1 — Cover (alle Nischen)

- **Vollseitiger Hintergrund** in Cluster-Farbe (z.B. `#3d4f8f` Blau für KI)
- **Oben:** Kicker „KOSTENLOSER LEAD-MAGNET" in Mono-Schrift, klein, durchsichtig
- **Mitte:** Großer Titel in FrauncesDisplay (z.B. „Lead-Magnet: KI-Potenzial-Check für den Mittelstand") in Weiß
- **Untertitel:** Kurze Beschreibung in Plex, heller
- **Unten:** Aktenzeichen 04 · Business & Digital, eCom28 GmbH · ecom28.de, Empire·Expansion mit Amber-Punkt

### Seite 2 — Erstes Kapitel (04-KI)

- **Farbiger Streifen** oben (8pt, Blau `#3d4f8f`)
- **Kapitel-Label** „KAPITEL" in Mono, Blau
- **Titel:** „1. Name & Claim" in FrauncesSemiBold, 22pt
- **Infobox** (hellblauer Hintergrund `#eef0f7`, blauer linker Rand): Format, Zielgruppe, Zeitaufwand, Hemmschwelle
- **Body-Text** beginnt mit strukturierten Listen

### Seite 3–5 — Content-Seiten (04-KI)

- **H2-Überschriften** in Blau (z.B. „2. Struktur des Checks", „3. Die 12 Fragen")
- **Tabellen** mit blauem Header-Streifen und hellblauem Hintergrund
- **Listen** mit guter Einrückung und Plex-Body-Font

### Seite 6–9 — Checklisten & Tabellen (05-PKV)

- **Checkbox-Listen** in hellgrauen Boxen mit `☐` Symbolen
- **Tabellen** mit Stat-Bars (z.B. Beihilfesätze als horizontale Balken)
- **Infoboxen** für Compliance-Hinweise (grüner Rand für Finanz-Cluster)

### Seite 10 — CTA-Seite (04-KI)

- **Vollseitiger blauer Hintergrund** `#3d4f8f`
- **Oben:** „NÄCHSTER SCHRITT" in Mono
- **Mitte:** Produktname „Ki Integrationen 35Plus" in FrauncesDisplay
- **Preis:** „ab 299 €" in PlexMedium
- **Button-Style:** Weißer Block mit blauem Text „Jetzt sichern → {{STRIPE_LINK}}"
- **Unten:** eCom28 GmbH · Bremen · HRB 39329 HB

### Seite 11+ — Fußzeile

- **Zentrierte Seitenzahl** unten (PlexMono, 8pt, Grau)
- erscheint auf allen Content-Seiten via `<pdf:pagefooter>`

---

## 3. Test-Ergebnisse

### 3.1 Build-Status: 23/23 PDFs erfolgreich

| Nische | Cluster | Lead-Magnet | Paid-Product | Seiten (LM) | Status |
|--------|---------|-------------|--------------|-------------|--------|
| 01-affiliate-marketing | Finanz | ✅ | — | ~8 | OK |
| 02-tiktok-shop | Alltag | ✅ | — | ~6 | OK |
| 03-pdfs-guides | Finanz | ✅ | ✅ | ~6 | OK |
| **04-ki-integrationen-35plus** | **Business** | **✅** | **✅** | **11** | **OK** |
| **05-lead-generation-pkv** | **Finanz** | **✅** | **✅** | **7** | **OK** |
| 06-lead-generation-dropshipping | Alltag | ✅ | — | ~6 | OK |
| 07-marketing-agency-traffic | Business | ✅ | ✅ | ~9 | OK |
| 08-app-ideen-appstore | Finanz | ✅ | — | ~7 | OK |
| **09-finanzielle-freiheit** | **Finanz** | **✅** | **✅** | **8** | **OK** |
| 10-gesundheit-praevention-40plus | Alltag | ✅ | ✅ | ~6 | OK |
| 11-immobilien-baufinanzierung | Finanz | ✅ | ✅ | ~8 | OK |
| 12-selbststaendigkeit-business-setup | Business | ✅ | ✅ | ~8 | OK |
| 13-reisen-lifestyle-35plus | Alltag | ✅ | ✅ | ~6 | OK |
| 14-nachhaltigkeit-eco | Alltag | ✅ | — | ~6 | OK |

### 3.2 Detaillierte Prüfung der 3 Test-Nischen

#### 04-KI (Business / Blau)
- **Titel:** „Lead-Magnet: KI-Potenzial-Check für den Mittelstand"
- **Cover:** Blau `#3d4f8f`, Kicker, Titel, Subtitle, Aktenzeichen 04 · Business & Digital
- **Kapitel:** „1. Name & Claim", „2. Struktur des Checks", „3. Die 12 Fragen", „4. Auswertungslogik", etc.
- **Tabellen:** 12-Fragen-Struktur, Score-Einstufung, Top-3-Automatisierungsbereiche
- **CTA:** „Ki Integrationen 35Plus