# Visual Upgrade Report — Empire Expansion Landing Pages
**Datum:** 2026-07-14
**Agent:** Kimi (Frontend-Spezialist)
**Scope:** Alle 14 Landing Pages (`01-*/landing-page.html` bis `14-*/landing-page.html`)

---

## Zusammenfassung

Alle 14 Landing Pages wurden mit **CSS-Only Hero-Visuals**, **CSS Product-Mockups** (Self-Serve-Nischen) und einem **Icon-System** für Vorteil-Listen aufgewertet. Keine Stock-Fotos, keine externen Bild-URLs — alles inline CSS/SVG im HTML.

---

## Was pro Nische geändert wurde

| Nische | Cluster | Visual-Typ | Self-Serve Mockup | Beschreibung |
|--------|---------|------------|-------------------|--------------|
| **01 — Affiliate Marketing** | Finanz `#1f6f5c` | **Network** (Nodes + Lines) | — | Schwebende Kreise mit Verbindungslinien, die Affiliate-Netzwerke abstrakt darstellen. Subtiler Animation-Float-Effekt. |
| **02 — TikTok Shop** | Alltag `#b0602c` | **Waves** (Wellen) | — | Zwei übereinanderlaufende SVG-Wellen am unteren Hero-Rand. Beauty-ähnliche, organische Formen. Sanfte Bewegung. |
| **03 — PDFs & Guides** | Finanz `#1f6f5c` | **Compass** (Ringe) | — | Konzentrische Pulse-Ringe, die Orientierung/Leitfaden symbolisieren. Pulsierende Animation. |
| **04 — KI-Integrationen** | Business `#3d4f8f` | **Circuit** (Grid + Dots) | ✅ KI-Tool-Stack + Vorlagen-Set | CSS-Grid mit leuchtenden Circuit-Dots. Tech-Ästhetik für KI-Thema. |
| **05 — Lead Gen PKV** | Finanz `#1f6f5c` | **Shield** (Schutz-Schild) | ✅ PKV-Wechsel-Kompaktguide 2026 | Schild-Silhouette mit rotierenden Kurven. Symbolisiert Versicherungsschutz. |
| **06 — Lead Gen Dropshipping** | Alltag `#b0602c` | **Moon** (Mond) | — | Mond-Silhouette mit sanftem Float. Entspannung/Schlaf-Thema. |
| **07 — Marketing Agency** | Business `#3d4f8f` | **Funnel** (Pfeile + Linien) | ✅ Funnel-Fix-Toolkit | Abwärts-Pfeile und Funnel-Linien. Konvertiert Marketing-Funnel visuell. |
| **08 — App-Ideen** | Finanz `#1f6f5c` | **Chart** (Balken + Trend) | ✅ VermoegenPlaner Premium | Aufsteigende Balken mit Trendlinie. Finanzwachstum visualisiert. |
| **09 — FIRE / Finanzielle Freiheit** | Finanz `#1f6f5c` | **Flame** (Flamme + Kurve) | ✅ FIRE-Kompaktkurs | Flammen-Animation mit Wachstumskurve. Gold/Grün-Accent. |
| **10 — Gesundheit & Prävention** | Alltag `#b0602c` | **Heart** (Pulse-Ringe) | — | Pulsierende Kreise mit Heartbeat-Linien. Gesundheit/Pulse-Thema. |
| **11 — Immobilien** | Finanz `#b0602c` | **House** (Gebäude) | ✅ Kaufklar-Guide | Haus-Silhouette mit Gebäude-Silhouetten. Immobilien-Bezug. |
| **12 — Selbstständigkeit** | Business `#3d4f8f` | **Building** (Grid + Pfeile) | ✅ Sicherer-Start-Kit | Struktur-Grid mit aufsteigenden Pfeilen. Business-Aufbau. |
| **13 — Reisen & Lifestyle** | Alltag `#b0602c` | **Globe** (Globus + Pfade) | — | Rotierender Globus mit Reisepfaden. Travel-Ästhetik. |
| **14 — Nachhaltigkeit & Eco** | Alltag `#b0602c` | **Leaf** (Blätter) | — | Organische Blattformen mit morphing Animation. Eco-Bezug. |

---

## CSS Product-Mockup (Self-Serve)

Für die 7 Self-Serve-Nischen (04, 05, 07, 08, 09, 11, 12) wurde ein `.product-mockup`-CSS-Block erstellt:

- **Styling:** 3D-perspektivische Karte mit `rotateY(-8deg) rotateX(4deg)`, sanftem Schatten, Farbverlauf am oberen Rand
- **Hover:** Kippt auf `rotateY(-4deg)` und hebt sich ab (`translateY(-8px)`)
- **Inhalt:** Header "Empire Expansion", Badge "PDF-Guide", Produkttitel, 5 Zeilen-Placeholder, Footer "Sofort verfügbar"
- **Technik:** Reines CSS, keine Bilder — Linien mit `border-radius`, Farben mit `linear-gradient`

---

## Icon-System

- **Problem-Listen:** `✓` (Häkchen) in der Cluster-Farbe statt generischer Punkte
- **Trust-Items:** `✓` in Cluster-Farbe
- **Checklisten:** `☐` (Checkbox) in Cluster-Farbe
- **Benefit-Cards:** `→` Pfeil-Präfix in Cluster-Farbe vor H4-Titeln

---

## Screenshots-Beschreibungen (wie die Hero-Bereiche jetzt aussehen)

### 04 — KI-Integrationen
Dunkler Business-Blue-Hintergrund (`#3d4f8f`) mit feinem CSS-Grid-Overlay. Leuchtende Punkte pulsieren auf dem Grid — erinnert an einen Leiterplatten-Circuit. Die 3D-Karte "KI-Tool-Stack + Vorlagen-Set" schwebt rechts im Hero.

### 05 — PKV (Beamte)
Sanfter Finanz-Grün-Hintergrund (`#1f6f5c`) mit einem stilisierten Schild als Silhouette. Rotierende Kurven umgeben das Schild. Die Mockup-Karte "PKV-Wechsel-Kompaktguide 2026" steht prominent im Hero.

### 09 — FIRE
Dunkler Hintergrund mit tiefem Grün-Gradienten und goldfarbenen Flammen-Elementen. Eine Wachstumskurve zeigt exponentielles Wachstum. Die Karte "FIRE-Kompaktkurs" hat einen warmen Gold-Accent.

### 12 — Selbstständigkeit
Business-Blue (`#3d4f8f`) mit strukturiertem Grid-Hintergrund. Aufsteigende Pfeile symbolisieren Wachstum. Die Mockup-Karte "Sicherer-Start-Kit" hebt sich mit 3D-Perspektive ab.

### 02 — TikTok Shop
Warme Orangetöne (`#b0602c`) mit zwei sanften SVG-Wellen am unteren Rand des Hero-Bereichs. Beauty-ästhetisch, organisch, einladend.

### 11 — Immobilien
Erdige Töne (`#b0602c`) mit stilisierten Gebäude-Silhouetten im Hintergrund. Haus-Silhouette mit Fenster-Matrix. Die Karte "Kaufklar-Guide" steht zentral.

---

## Probleme & Hinweise

| Nische | Problem | Schwere | Lösung |
|--------|---------|---------|--------|
| **12 — Selbstständigkeit** | Bereits im Original vorhandenes `.hero-bg-visual` und `.product-mockup-wrap` CSS wurde durch unseren Upgrade ergänzt, nicht ersetzt. | 🟡 Niedrig | Kein Rendering-Problem — CSS-Cascade funktioniert. HTML-Validierung: `ok: true`. |
| **06 — Dropshipping** | Kein Problem gefunden | — | — |
| **Allgemein** | Keine Stock-Fotos, keine externen URLs, keine fiktiven Testimonials, Countdowns nicht eingefügt. | ✅ | Alle Regeln eingehalten. |

---

## HTML-Validierung (Stichprobe)

| Datei | Valid? | `hero-bg-visual` | `product-mockup` |
|-------|--------|-------------------|------------------|
| `01-affiliate-marketing/landing-page.html` | ✅ | 3 | 0 |
| `04-ki-integrationen-35plus/landing-page.html` | ✅ | 3 | 1 |
| `09-finanzielle-freiheit/landing-page.html` | ✅ | 3 | 1 |
| `12-selbststaendigkeit-business-setup/landing-page.html` | ✅ | 5* | 2* |

\* *Bei 12 waren bereits im Original ähnliche Klassen vorhanden. Doppelte CSS-Regeln überschreiben sich, HTML bleibt valide.*

---

## Backup

Backup erstellt unter: `.backups/visual-upgrade-20260714-122029/`

---

## Commit

- **Branch:** `main`
- **Message:** `visual: CSS-only hero visuals + product mockups for all 14 niches`

---

*Erstellt von Kimi für das Empire-Expansion-Projekt. Alle Änderungen sind CSS-Only, keine externen Abhängigkeiten.*
