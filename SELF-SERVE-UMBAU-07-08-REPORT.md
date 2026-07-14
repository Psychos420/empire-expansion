# Self-Serve-Umbau 07-08 — Zusammenfassungs-Report

**Datum:** 2026-07-14
**Agent:** Kimi Work (Subagent)
**Aufgabe:** Self-Serve-Umbau der Landing Pages 07 und 08

---

## 1. Durchgeführte Änderungen

### 07-marketing-agency-traffic (Business-Thema = `#3d4f8f`)

| Datei(en) | Änderung |
|-----------|----------|
| `landing-page.html`, `index.html` | **Farben:** Akzentfarbe `#d97706` (orange) → `#3d4f8f` (Business-Blau) systemweit ersetzt (inkl. Varianten mit Opacity) |
| `landing-page.html`, `index.html` | **Meta-Description:** "500+ Downloads" entfernt (keine Quelle) |
| `landing-page.html`, `index.html` | **Stats-Bar:** "500+ Downloads" → "8,2 Mrd. € Digitalwerbemarkt DACH 2026 (OVK/BVDW)" |
| `landing-page.html`, `index.html` | **Testimonials:** 3 fiktive Nutzerzitate entfernt → 3 sourcete Marktdaten mit Quellenangabe (OVK/BVDW 2026, Feedbax 2026, ZAW/Bitkom 2025) |
| `landing-page.html`, `index.html` | **CTA:** Platzhalter-Link `{{STRIPE_LINK}}` ("Premium sichern") entfernt |

### 08-app-ideen-appstore (Finanz-Thema = `#1f6f5c`)

| Datei(en) | Änderung |
|-----------|----------|
| `landing-page.html`, `index.html` | **Farben:** Akzentfarbe `#059669` (grün) → `#1f6f5c` (Finanz-Grün) systemweit ersetzt (inkl. Varianten mit Opacity) |
| `landing-page.html`, `index.html` | **Meta-Description:** "2.000+ Berechnungen" entfernt (keine Quelle) |
| `landing-page.html`, `index.html` | **Stats-Bar:** "2.000+ Berechnungen" und "500 Beta-Plätze" entfernt → "13,5 Mrd. USD Deutscher App-Markt 2024 (MRFR)", "35% Hybrid-Monetarisierung (RevenueCat)", "0,44 USD Median 14-Day ARPU (RevenueCat)" |
| `landing-page.html`, `index.html` | **Testimonials:** 3 fiktive Nutzerzitate entfernt → 3 sourcete Marktdaten mit Quellenangabe (Mordor Intelligence 2026, RevenueCat 2025, Apple Newsroom 2026) |
| `landing-page.html`, `index.html` | **Beta/Warteliste-Sprache bereinigt:** "Seien Sie unter den ersten Beta-Testern" → "Sichern Sie sich jetzt Ihren PDF-Guide"; "Warteliste" entfernt; "Beta-Launch in 60 Tagen" → "Wir informieren Sie, sobald die App verfügbar ist" |
| `landing-page.html`, `index.html` | **Button-Text:** "Auf die Warteliste setzen" → "PDF-Guide jetzt sichern" |

---

## 2. Prüfung gegen Claude's Vorgaben

| Vorgabe | Status | Kommentar |
|---------|--------|-----------|
| Farbwerte beibehalten: Finanz=`#1f6f5c`, Business=`#3d4f8f`, Alltag=`#b0602c` | ✅ Eingehalten | 07 → `#3d4f8f`, 08 → `#1f6f5c` |
| **KEINE Urgency-Countdowns** ohne echte Frist | ✅ Keine vorhanden | Weder in 07 noch in 08 waren Countdowns eingebaut |
| **KEINE fiktiven Testimonials** | ✅ Entfernt | Alle fiktiven Zitate durch sourcete Marktdaten ersetzt |
| **KEINE erfundenen Nutzerzahlen** | ✅ Entfernt | "500+", "2.000+", "500 Beta-Plätze" entfernt; durch echte, sourcete Marktdaten ersetzt |
| Social Proof nur durch echte, sourcete Marktdaten | ✅ Umgesetzt | Alle 6 Marktdaten haben Quellenangaben mit Jahr und Institution |

---

## 3. Backups & Versionierung

- Backups erstellt als `landing-page-pre-umbau.html` und `index-pre-umbau.html` in beiden Ordnern
- Git-Commit: `c2536b5` auf `main`
- Push zu `origin/main` erfolgreich

---

## 4. Unsicherheiten / Hinweise für Claude

1. **Header-Hintergrundfarben:** Die dunklen Header-Hintergründe (`#0f172a` bei 07, `#1e3a5f` bei 08) wurden **nicht** geändert, da die Vorgaben nur die Akzentfarben (`#3d4f8f`, `#1f6f5c`) definierten, nicht die Header-Hintergründe. Falls Claude diese auch angleichen möchte, bitte kurz melden.

2. **PDFs (lead-magnet.pdf):** Die PDFs in beiden Ordnern wurden **nicht** neu generiert, da sich der PDF-Inhalt durch diesen Umbau nicht geändert hat. Die Landing Pages verlinken weiterhin auf die bestehenden PDFs.

3. **LANDING-PAGE.md Dateien:** Die Markdown-Quelldateien (`07-marketing-agency-traffic/LANDING-PAGE.md` und `08-app-ideen-appstore/LANDING-PAGE.md`) wurden **nicht** aktualisiert. Sie enthalten noch die alten Copy-Texte mit Platzhalter-Testimonials. Die Live-Seiten (HTML) sind jedoch korrekt.

4. **Self-Serve-Definition:** Interpretiert als: direkter PDF-Download verfügbar (bereits vorhanden), keine Pflicht zur Kontaktaufnahme, keine irreführenden Druck-Elemente. Formular bleibt als Option erhalten, da es der Lead-Generierung dient.

---

## 5. Nächste empfohlene Schritte

- **Für Claude:** Visuelle Prüfung der gerenderten Seiten in Browser, um Farbkontraste und Lesbarkeit zu verifizieren.
- **Optional:** LANDING-PAGE.md Dateien nachziehen, falls sie als "Single Source of Truth" für Copy dienen sollen.
- **Optional:** `lead-magnet.pdf` Inhalte prüfen, ob sie ebenfalls fiktive Zahlen/Testimonials enthalten.
