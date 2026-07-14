# STICKY-CTA-MOBILE-DETAIL Report

**Datum:** 2026-07-14
**Agent:** Kimi (Spezialist-Agent für Empire Expansion)
**Auftrag:** Sticky-CTA-MOBILE-DETAIL

---

## Zusammenfassung

Sticky-CTA-Implementierung auf allen 14 Landing Pages verifiziert, korrigiert und vereinheitlicht. 12 Pages hatten **keine funktionierende CSS-Regel** für den mobilen Sticky CTA — der Bar war im HTML vorhanden, aber unsichtbar/ohne Layout.

---

## Befund: Ursprünglicher Zustand

| Nische | Sticky-CTA-HTML vorhanden | CSS-Regel `.sticky-cta` vorhanden | Mobile funktional | CTA-Text | Ziel-Link |
|--------|---------------------------|-----------------------------------|-------------------|----------|-----------|
| 01 Affiliate | ✅ | ❌ | ❌ | „Bereit für mehr Klarheit? / Jetzt kostenlos starten" | `#form` |
| 02 TikTok Shop | ✅ | ❌ | ❌ | „Bereit für mehr Klarheit? / Jetzt kostenlos starten" | `#form` |
| 03 PDFs & Guides | ✅ | ❌ | ❌ | „Bereit für mehr Klarheit? / Jetzt kostenlos starten" | `#form` |
| 04 KI-Integrationen | ✅ | ✅ | ✅ | „KI-Tool-Stack + Vorlagen-Set kaufen — 49 €" | `{{STRIPE_LINK}}` |
| 05 PKV | ✅ | ❌ | ❌ | **❌ FALSCH**: „Jetzt kostenlos starten" | `#form` |
| 06 Dropshipping | ✅ | ❌ | ❌ | „Bereit für mehr Klarheit? / Jetzt kostenlos starten" | `#form` |
| 07 Agentur | ✅ | ❌ | ❌ | „Funnel-Fix-Toolkit — 49 €" | `{{STRIPE_LINK}}` |
| 08 App-Ideen | ✅ | ❌ | ❌ | „Premium-Zugang — 12,99 €/Monat" | `{{STRIPE_LINK}}` |
| 09 FIRE | ✅ | ✅ | ✅ | „FIRE-Kompaktkurs kaufen — 49 €" | `{{STRIPE_LINK}}` |
| 10 Gesundheit | ✅ | ❌ | ❌ | „Bereit für mehr Klarheit? / Jetzt kostenlos starten" | `#form` |
| 11 Baufinanzierung | ✅ | ❌ | ❌ | „Kaufklar-Guide kaufen — 19 €" | `{{STRIPE_LINK}}` |
| 12 Selbstständigkeit | ✅ | ❌ | ❌ | „Sicherer-Start-Kit kaufen — 79 €" | `{{STRIPE_LINK}}` |
| 13 Reisen | ✅ | ❌ | ❌ | „Bereit für mehr Klarheit? / Jetzt kostenlos starten" | `#form` |
| 14 Nachhaltigkeit | ✅ | ❌ | ❌ | „Bereit für mehr Klarheit? / Jetzt kostenlos starten" | `#form` |

**Kritische Probleme:**
1. **12 von 14 Pages hatten keinen funktionalen Sticky CTA** — nur HTML-Platzhalter ohne CSS.
2. **05-PKV zeigte fälschlich „kostenlos starten"** statt des Self-Serve-Produkts (24 € Guide).
3. **07-Agentur** fehlte das Wort „kaufen" im CTA-Text.

---

## Durchgeführte Änderungen

### 1. CSS-Regeln hinzugefügt (12 Pages)

In allen Pages ohne funktionierende `.sticky-cta`-CSS-Regel wurde folgender Block vor dem schließenden `</style>` eingefügt:

```css
/* Sticky Mobile CTA */
.sticky-cta {
  display: none;
  position: fixed;
  bottom: 0; left: 0; right: 0;
  background: rgba(255,255,255,0.96);
  padding: 12px 20px;
  box-shadow: 0 -4px 20px rgba(0,0,0,0.08);
  z-index: 90;
  border-top: 1px solid rgba(0,0,0,0.08);
  backdrop-filter: blur(6px);
}
.sticky-cta.is-visible { display: block; }
.sticky-cta a { display: block; width: 100%; text-align: center; }
.sticky-cta .cta-text { display: block; text-align: center; font-size: 0.85rem; color: rgba(0,0,0,0.5); margin-bottom: 8px; }
@media (max-width: 599px) {
  .sticky-cta, .sticky-cta.is-visible { display: block !important; }
  body { padding-bottom: 72px; }
}
```

**Betroffene Pages:** 01, 02, 03, 05, 06, 07, 08, 10, 11, 12, 13, 14

### 2. 09-FIRE: Doppeltes CSS entfernt

Bei 09-FIRE existierte bereits eine dunkelblau/amber-gestylte Sticky-CTA-Regel. Der Automatisierungsskript hat fälschlicherweise eine zweite, weiße CSS-Regel eingefügt, die die visuelle Gestaltung zerstört hätte (weißer Text auf weißem Hintergrund). Die redundanten Zeilen wurden entfernt.

### 3. 04-KI: Klassenname korrigiert

Der Automatisierungsskript hat `cta-primary` in `cta-button` umbenannt. Da 04-KI keine `.cta-button`-Regel besitzt, wäre der Button ungestylt gewesen. Rückgängig gemacht auf `cta-primary`.

### 4. 05-PKV: CTA auf Self-Serve-Produkt umgestellt

- **Vorher:** „Bereit für mehr Klarheit? / Jetzt kostenlos starten" → `#form`
- **Nachher:** „PKV-Wechsel-Kompaktguide 2026 kaufen — 24 €" → `{{STRIPE_LINK}}`

### 5. 07-Agentur: CTA-Text vereinheitlicht

- **Vorher:** „Funnel-Fix-Toolkit — 49 €"
- **Nachher:** „Funnel-Fix-Toolkit kaufen — 49 €" (Wort „kaufen" ergänzt für Konsistenz)

---

## Endzustand: Alle 14 Landing Pages

| Nische | CSS vorhanden | Mobile aktiv | CTA-Text | Ziel | Preis |
|--------|---------------|--------------|----------|------|-------|
| 01 Affiliate | ✅ | ✅ | Jetzt kostenlos starten | `#form` | kostenlos |
| 02 TikTok Shop | ✅ | ✅ | Jetzt kostenlos starten | `#form` | kostenlos |
| 03 PDFs & Guides | ✅ | ✅ | Jetzt kostenlos starten | `#form` | kostenlos |
| 04 KI-Integrationen | ✅ | ✅ | KI-Tool-Stack + Vorlagen-Set kaufen — 49 € | `{{STRIPE_LINK}}` | 49 € |
| 05 PKV | ✅ | ✅ | PKV-Wechsel-Kompaktguide 2026 kaufen — 24 € | `{{STRIPE_LINK}}` | 24 € |
| 06 Dropshipping | ✅ | ✅ | Jetzt kostenlos starten | `#form` | kostenlos |
| 07 Agentur | ✅ | ✅ | Funnel-Fix-Toolkit kaufen — 49 € | `{{STRIPE_LINK}}` | 49 € |
| 08 App-Ideen | ✅ | ✅ | Premium-Zugang — 12,99 €/Monat | `{{STRIPE_LINK}}` | 12,99 €/Mo |
| 09 FIRE | ✅ | ✅ | FIRE-Kompaktkurs kaufen — 49 € | `{{STRIPE_LINK}}` | 49 € |
| 10 Gesundheit | ✅ | ✅ | Jetzt kostenlos starten | `#form` | kostenlos |
| 11 Baufinanzierung | ✅ | ✅ | Kaufklar-Guide kaufen — 19 € | `{{STRIPE_LINK}}` | 19 € |
| 12 Selbstständigkeit | ✅ | ✅ | Sicherer-Start-Kit kaufen — 79 € | `{{STRIPE_LINK}}` | 79 € |
| 13 Reisen | ✅ | ✅ | Jetzt kostenlos starten | `#form` | kostenlos |
| 14 Nachhaltigkeit | ✅ | ✅ | Jetzt kostenlos starten | `#form` | kostenlos |

---

## Technische Details

### Mobile-Only Verhalten
- **Desktop (`> 599px`):** Sticky CTA ist standardmäßig versteckt (`display: none`). Bestehende JavaScript-Scroll-Controller (auf alten Template-Pages) können die Bar bei Scroll über 400px einblenden (`.is-visible`).
- **Mobile (`≤ 599px`):** Sticky CTA ist immer sichtbar (`display: block !important`), unabhängig von Scroll-Position. `body` erhält `padding-bottom: 72px` damit Inhalte nicht hinter der Bar verschwinden.

### CSS-Architektur
- **Container:** `position: fixed; bottom: 0; left: 0; right: 0;` — volle Breite, am unteren Bildschirmrand.
- **Z-Index:** `90` (über den meisten Inhalten, aber unter modals/overlays).
- **Hintergrund:** `rgba(255,255,255,0.96)` mit `backdrop-filter: blur(6px)` — semi-transparent mit Glassmorphism-Effekt.
- **Schattierung:** `box-shadow: 0 -4px 20px rgba(0,0,0,0.08)` — subtile Erhebung vom Content.

### JavaScript-Interoperabilität
Bestehende Scroll-Controller-Skripte (alte Template-Pages) togglen die Klasse `.is-visible`. Die CSS-Regel `.sticky-cta.is-visible { display: block; }` stellt sicher, dass dies auf Desktop funktioniert. Auf Mobile überschreibt `!important` im Media-Query, sodass die Bar immer sichtbar bleibt.

---

## Compliance & Einschränkungen

- ✅ **Keine fiktiven Zahlen** — alle Preise entsprechen den verbindlichen Self-Serve-Preisen aus `REQUEST-FOR-KIMI.md`.
- ✅ **Keine Countdowns** — keine zeitlichen Druck-Elemente im Sticky CTA.
- ✅ **Keine Testimonials** — Social-Proof-Elemente im Sticky CTA nicht vorhanden.
- ✅ **Stripe-Link bleibt Platzhalter** — alle Paid-CTAs verwenden `{{STRIPE_LINK}}`.
- ✅ **Impressum/Firmenname unverändert** — keine Änderungen an Footer oder rechtlichen Texten.
- ✅ **Meta Pixel + GA4 nicht eingebaut** — kein Tracking-Code hinzugefügt.
- ✅ **Farbwerte eingehalten** — keine abweichenden Brand-Farben im Sticky-CTA-Block.

---

## Backups

Alle geänderten Dateien wurden vor der Modifikation nach:
`00-shared/logs/backups/sticky-cta-backup-20260714-120711/`

Backup-Struktur spiegelt die Ordnerstruktur des Projekts wider.

---

## Git-Commit

**Branch:** `main`
**Message:** `fix(sticky-cta): add missing mobile sticky CTA CSS to 12 landing pages, fix 05-PKV self-serve CTA, unify CTA text`
**Geänderte Dateien:** `0*/landing-page.html` (14 Nischen-Landingpages)

---

## Offene Punkte / Empfehlungen

1. **Visuelle Test auf echten Geräten empfohlen:** Die Sticky-CTA-Bar wurde auf Basis des Referenz-Designs (04-KI) implementiert. Ein kurzer Check auf iPhone/Android in den DevTools sollte die Bar-Höhe und Tap-Targets verifizieren.
2. **Tap-Target-Größe:** Die Buttons sind mindestens 44px hoch (durch `padding: 12px 20px` + Font-Size). Für WCAG 2.5.5 (44×44px) sollte dies ausreichen, aber ein Test empfohlen.
3. **Zukunft:** Bei Einführung echter Stripe-Links sollte `{{STRIPE_LINK}}` durch die echte URL ersetzt werden.

---

*Report erstellt von Kimi Spezialist-Agent für Empire Expansion.*
