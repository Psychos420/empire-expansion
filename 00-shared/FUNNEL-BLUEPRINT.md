# Funnel-Blueprint — Generischer Empire-Expansion-Funnel

Dieses Dokument beschreibt den standardisierten Funnel, der in allen 14 Expansionsbereichen eingesetzt wird. Er ist bewusst modular aufgebaut, sodass jeder Bereich ihn an seine Zielgruppe, sein Angebot und seine Margen anpassen kann.

---

## Funnel-Übersicht

```
TRAFFIC
   │
   ▼
LEAD-MAGNET (kostenlos / Low-Ticket)
   │
   ▼
WILLKOMMENS-SEQUENZ (E-Mail / SMS / WhatsApp)
   │
   ▼
NURTURE & AUTHORITY (Content, Case Studies, Angebote)
   │
   ▼
LOW-TICKET-ANGEBOT (9–49 €)
   │
   ▼
HIGH-TICKET / TERMIN / UPSELL
   │
   ▼
RETENTION & CROSS-SELL (Ökosystem-Logik)
```

---

## Phase 1 — Traffic

**Ziel:** Die richtigen Menschen auf die Landing Page bringen.

### Traffic-Quellen

| Quelle | Beste für | Status |
|---|---|---|
| **Paid Social** (Meta Ads) | Skalierbare Lead-Generierung, schnelle Tests | Start sofort |
| **SEO / Content** | Langfristiger, kostengünstiger Traffic | Aufbau Monat 2+ |
| **Organic Social** (TikTok, LinkedIn, YouTube Shorts) | Vertrauen, Reichweite, geringe Kosten | Parallel |
| **Partner / Affiliate** | Qualifizierter Traffic | Ab Monat 2 |
| **E-Mail-Liste (andere Bereiche)** | Cross-Sell, wärmste Leads | Ab Monat 1 |

### Traffic-Zielwerte

| Metrik | Monat 1 | Monat 3 | Monat 6 |
|---|---:|---:|---:|
| Cost per Lead (CPL) | < 5 € | < 4 € | < 3 € |
| Landing-Page-Conversion | > 30 % | > 40 % | > 45 % |
| Click-Through-Rate (CTR) Ads | > 1 % | > 1,5 % | > 2 % |

---

## Phase 2 — Lead-Magnet

**Ziel:** Im Austausch gegen Kontaktdaten einen ersten Wert liefern.

### Typen von Lead-Magneten

- **Checkliste** — schnell konsumierbar, hohe Wahrnehmung
- **PDF-Guide** — tieferer Wert, längere Bindung
- **Rechner / Tool** — interaktiv, Daten-Rückfluss
- **Webinar / Video** — Authority-Aufbau
- **Kostenloser Test / Audit** — sehr qualifizierte Leads

### Lead-Magnet-Beispiele pro Bereich

| Bereich | Lead-Magnet |
|---|---|
| Affiliate Marketing | „Finanzielle Vorsorge 40+" Checkliste |
| TikTok Shop | „Mature Skin Routine" Guide |
| PDFs & Guides | „Rente mit 65 sicher" Checkliste |
| KI-Integrationen 35+ | „KI-Potenzial-Check" |
| Lead Generation PKV | „PKV-Wechsel-Checkliste 2026" |
| Lead Generation Dropshipping | „Schlaf & Erholung" Produkt-Guide |
| Marketing Agency Traffic | „Traffic-Audit-Checkliste" |
| App-Ideen | „App-Ideen-Validierungs-Canvas" |
| Finanzielle Freiheit | „Freiheits-Rechner" |
| Gesundheit 40+ | „Gesundheits-Check 40+" |
| Immobilien/Baufinanzierung | „Baufinanzierungs-Checkliste" |
| Selbstständigkeit Setup | „Business-Setup-Checkliste" |
| Reisen Lifestyle 35+ | „Langzeitreise-Planer" |
| Nachhaltigkeit Eco | „Eco-Living Starter-Kit" |

### Automation-Punkte

- Formular-Submission → n8n Webhook
- n8n → Tagging + Listeneintrag in Brevo / GoHighLevel
- Double-Opt-In auslösen
- Willkommens-E-Mail #1 senden
- Benachrichtigung an zuständigen Bereichs-Owner (optional)

---

## Phase 3 — E-Mail-Nurture

**Ziel:** Vertrauen aufbauen, Authority etablieren, erste Objections abbauen.

### Standard-Sequenz (5 E-Mails)

Siehe `EMAIL-SEQUENCE-TEMPLATE.md`.

### Zusätzliche Kanäle

| Kanal | Einsatz |
|---|---|
| **E-Mail** | Haupt-Nurture-Kanal, Content, Angebote |
| **SMS** | Kurze Erinnerungen, Termin-Bestätigungen, Flash-Angebote |
| **WhatsApp** | Persönlicher Dialog, FAQ, Kundenservice |

### Automation-Punkte

- E-Mail-Öffnung / Klick → Tagging und Scoring
- Nicht-Öffner → Re-Engagement-Sequenz
- Klick auf Low-Ticket-Link → Interessenten-Tag + Follow-up
- Termin-Buchung → Kalender-Trigger + Erinnerungen

---

## Phase 4 — Low-Ticket

**Ziel:** Ersten Umsatz generieren, Käufer-Liste aufbauen, Vertrauen durch Investition stärken.

### Low-Ticket-Preisspanne

- **7–19 €:** PDFs, Templates, kleine Guides
- **19–49 €:** umfangreichere Playbooks, Tools, Mini-Kurse

### Beispiele pro Bereich

| Bereich | Low-Ticket-Angebot |
|---|---|
| Affiliate Marketing | Vergleichs-Guide „PKV, ETF, Zahnzusatz" 9 € |
| TikTok Shop | Beauty-PDF Bundle 7 € |
| PDFs & Guides | Premium-Guide „Rente mit 65" 12 € |
| KI-Integrationen 35+ | „KI-Setup-Guide für Solopreneure" 19 € |
| Lead Generation PKV | „PKV-Vergleichsrechner-Zugang" 9 € |
| Lead Generation Dropshipping | „Sourcing-Checkliste" 7 € |
| Marketing Agency Traffic | „Lead-Generator-Playbook" 29 € |
| App-Ideen | „MVP-Planungs-Guide" 14 € |
| Finanzielle Freiheit | „Investment-Guide" 19 € |
| Gesundheit 40+ | „Präventions-Guide" 9 € |
| Immobilien/Baufinanzierung | „Finanzierungs-Guide" 14 € |
| Selbstständigkeit Setup | „Gründungs-Guide" 19 € |
| Reisen Lifestyle 35+ | „Reise-Guide" 12 € |
| Nachhaltigkeit Eco | „Nachhaltigkeits-Guide" 9 € |

### Automation-Punkte

- Kauf → Stripe-Webhook → n8n
- n8n → Zugangsdaten/Download per E-Mail
- Käufer-Tag in Brevo / GoHighLevel
- Upsell-Sequenz starten
- Hinweis an Support/Vertrieb bei High-Ticket-Potenzial

---

## Phase 5 — High-Ticket / Termin

**Ziel:** Den Käufer oder qualifizierten Lead in ein Beratungsgespräch, eine Dienstleistung oder ein hochpreisiges Produkt überführen.

### High-Ticket-Beispiele

- PKV-Beratungstermin
- KI-Agentur-Projekt
- Marketing-Agentur-Paket
- App-Entwicklung
- Coaching / Beratung

### Qualifizierungsfragen

Vor dem Termin sollte ein kurzer Fragebogen oder ein Quiz abgefragt werden:

1. Aktuelle Situation (z. B. „Bist du Beamter / Selbstständiger / Angestellter?")
2. Größte Herausforderung
3. Zeitrahmen
4. Budget-Vorstellung
5. Entscheidungsberechtigung

### Automation-Punkte

- Terminbuchung → Kalender-Integration (GoHighLevel / Calendly)
- Erinnerungs-E-Mail/SMS 24h und 1h vor Termin
- Nach dem Termin: Follow-up mit Angebot oder nächstem Schritt
- Kein-Show-Sequenz: Erneute Einladung nach 3 Tagen

---

## Phase 6 — Retention & Cross-Sell (Ökosystem-Logik)

**Ziel:** Bestehende Kunden und Leads in andere Bereiche des Ökosystems überführen.

### Cross-Sell-Möglichkeiten

| Ursprünglicher Bereich | Passende Cross-Sell-Bereiche |
|---|---|
| Finanzielle Freiheit | PKV-Leads, Affiliate-Produkte, Immobilien |
| Gesundheit 40+ | PKV-Leads, Affiliate (Zahnzusatz), Nachhaltigkeit |
| Selbstständigkeit Setup | KI-Agentur, Marketing Agency Traffic |
| Reisen Lifestyle 35+ | Finanzielle Freiheit, Gesundheit, Nachhaltigkeit |
| PDFs & Guides | Affiliate-Produkte, Low-Ticket, Coaching |
| PKV-Leads | Finanzielle Freiheit, Gesundheit, Immobilien |
| KI-Integrationen 35+ | Marketing Agency Traffic, Selbstständigkeit Setup |
| App-Ideen | Marketing Agency Traffic, KI-Agentur |

### Automation-Punkte

- Käufer/Lead-Tag aus Bereich X → Trigger für Sequenz aus Bereich Y
- n8n prüft Interessen-Tags und verschiebt Lead in passende Liste
- Monatlicher Cross-Sell-Newsletter mit relevanten Angeboten
- Reaktivierung von inaktiven Leads mit neuem Lead-Magneten

---

## Funnel-KPIs

| Metrik | Definition | Ziel Monat 1 | Ziel Monat 3 | Ziel Monat 6 |
|---|---|---:|---:|---:|
| Opt-in-Rate | Leads / Landing-Page-Besucher | > 30 % | > 40 % | > 45 % |
| E-Mail-Öffnungsrate (Willkommen) | > 50 % | > 55 % | > 60 % |
| E-Mail-Klickrate | Klicks / Öffnungen | > 8 % | > 10 % | > 12 % |
| Low-Ticket-Conversion | Käufer / Leads | > 3 % | > 5 % | > 7 % |
| Terminbuchungsrate | Termine / qualifizierte Leads | > 5 % | > 8 % | > 10 % |
| Show-Up-Rate | Terminwahrscheinlichkeit | > 60 % | > 70 % | > 75 % |
| Close-Rate High-Ticket | Abschlüsse / Termine | > 15 % | > 20 % | > 25 % |
| CAC | Kosten pro Neukauf/Lead | < 5 € | < 4 € | < 3 € |
| LTV/CAC | Lebenszeitwert / Akquisitionskosten | > 3 | > 4 | > 5 |

---

## Funnel-Optimierungs-Checkliste

- [ ] Headline testen (mindestens 2 Varianten)
- [ ] Lead-Magnet-Format testen (Checkliste vs. Guide vs. Tool)
- [ ] CTA-Text und Button-Farbe testen
- [ ] Formularlänge minimieren
- [ ] Danke-Seite mit nächstem Angebot optimieren
- [ ] E-Mail-Betreffzeilen A/B-testen
- [ ] Sendezeit optimieren
- [ ] SMS/WhatsApp als zusätzlichen Kanal testen
- [ ] Retargeting für Landing-Page-Besucher ohne Opt-in
- [ ] Exit-Intent-Popup einrichten

---

## Funnel-Beispiel: PKV-Leads

1. **Traffic:** Meta Ads mit Headline „Beamte: PKV-Wechsel 2026 — in 10 Minuten klären"
2. **Lead-Magnet:** Kostenlose „PKV-Wechsel-Checkliste 2026"
3. **Nurture:** 5-teilige Willkommens-Sequenz + wöchentlicher Newsletter
4. **Low-Ticket:** „PKV-Vergleichsrechner-Zugang" für 9 €
5. **High-Ticket:** Kostenloser PKV-Beratungstermin mit lizenziertem Vermittler
6. **Cross-Sell:** Finanzielle Freiheit, Gesundheit 40+, Zahnzusatz-Affiliate

---

## Funnel-Beispiel: KI-Agentur

1. **Traffic:** LinkedIn Posts + Paid Ads „KI für Dienstleister 35+"
2. **Lead-Magnet:** „KI-Potenzial-Check" (5 Fragen, individuelles Ergebnis)
3. **Nurture:** Case Studies + Erklär-Content per E-Mail
4. **Low-Ticket:** „KI-Setup-Guide für Solopreneure" 19 €
5. **High-Ticket:** Kostenloses Beratungsgespräch für KI-Integration
6. **Cross-Sell:** Marketing Agency Traffic, Selbstständigkeit Setup
