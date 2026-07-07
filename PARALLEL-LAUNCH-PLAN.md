# Empire Expansion — Parallel-Launch-Plan

> Alle 14 Bereiche werden gleichzeitig gestartet. Dieser Plan beschreibt, wie wir das ohne Chaos schaffen: gemeinsame Infrastruktur zuerst, dann tägliche Micro-Sprints pro Bereich.

---

## Prinzipien für den Parallel-Start

1. **Shared Tech-Stack zuerst.** Einmal einrichten, alle Bereiche nutzen.
2. **Lead-Magnet-First.** Jeder Bereich braucht sofort einen Lead-Magneten — das ist der schnellste Weg zu Leads.
3. **Daily Micro-Sprints.** Pro Bereich 1–2 Stunden Arbeit pro Tag, strikt nach `WEEK-1-TASKS.md`.
4. **Centralized Reporting.** Jeden Abend 15-Minuten-Standup: Was ist heute live gegangen, wo blockiert es, was morgen Priorität.
5. **Automation von Tag 1.** Jeder Funnel bekommt E-Mail-Automatisierung, bevor Traffic läuft.

---

## Woche 1 — Launch-Woche (Tag 1–7)

### Tag 1 — Infrastruktur-Setup

| Aufgabe | Verantwortlich | Output |
|---|---|---|
| Domain/Subdomain-Struktur festlegen | Mensch | Entscheidung: eine Hauptdomain + Subdomains pro Bereich? |
| Brevo-Account einrichten | Agent/Mensch | Liste, Double-Opt-In, Segment-Tags |
| GoHighLevel oder Brevo-CRM einrichten | Agent/Mensch | Lead-Pipelines, Tags |
| n8n-Server/Cloud-Instanz bereitstellen | Agent/Mensch | Login, erste Test-Workflows |
| Carrd/Webflow-Konto + Grundkonfiguration | Agent/Mensch | Templates vorhanden |
| Stripe + PayPal verbinden | Mensch | Zahlungslinks für Low-Ticket-Produkte |
| Zentrale Tracking-Struktur (GA4, Meta Pixel) | Agent | Tracking-Plan aus 00-shared |

### Tag 2 — Lead-Magneten finalisieren

| Bereich | Lead-Magnet | Status-Ziel Tag 2 |
|---|---|---|
| 01 Affiliate | „Der Finanzielle Freiheit-Check für 40+" | Text fertig, Design begonnen |
| 02 TikTok Shop | „Die Glow-ab-40-Checkliste" | Text fertig |
| 03 PDFs/Guides | „Die 5-teilige Checkliste: Rente mit 65 sicher" | PDF-Design fertig |
| 04 KI-Agentur | „KI-Potenzial-Check für den Mittelstand" | Fragen + Score-Logik fertig |
| 05 PKV | „PKV-Wechsel-Checkliste 2026 für Beamte" | Text fertig |
| 06 Dropshipping | „Besser schlafen in 7 Tagen" | Text fertig |
| 07 Agency | „Der 10-Punkte-Check: Mehr Leads in 30 Tagen" | Text fertig |
| 08 App | „Rentenlücke-Rechner" als Web-App | Formular + Formel fertig |
| 09 Finanzielle Freiheit | „FIRE-Schnellcheck" | Text fertig |
| 10 Gesundheit | „5-Minuten-Gesundheits-Check ab 40" | Text fertig |
| 11 Immobilien | „Immobilien-Readiness-Score" | Text fertig |
| 12 Selbstständigkeit | „7-Schritte-Plan zur sicheren Selbstständigkeit ab 35" | Text fertig |
| 13 Reisen | „Welcher Reisetyp bist du ab 35?" Quiz | Fragen fertig |
| 14 Nachhaltigkeit | „Eco-Starter-Guide" | Text fertig |

### Tag 3 — Landing Pages bauen

- Jeder Bereich bekommt eine Landing Page nach `00-shared/LANDING-PAGE-TEMPLATE.md`.
- Formular mit Brevo verbinden.
- Danke-Seite mit Download-Link.
- Meta Pixel + GA4 Events installieren.

### Tag 4 — E-Mail-Sequenzen aktivieren

- 5-teilige Willkommens-Sequenz pro Bereich aus `EMAIL-SEQUENCE.md` in Brevo einpflegen.
- Tags und Segmentierung einrichten.
- Test-Opt-ins durchführen.

### Tag 5 — Traffic-Tests starten

- Organische Kanäle: LinkedIn, TikTok/Shorts, SEO-Blog.
- Kleine Paid-Tests: 10–20 €/Tag pro Bereich (max. 200 €/Tag Gesamt).
- Ziel: erste Conversions und CPL-Daten sammeln.

### Tag 6 — Optimierung + Reporting

- Landing Pages mit schlechter Conversion (< 20 %) verbessern.
- E-Mail-Open-Rates prüfen.
- Lead-Qualität bewerten.

### Tag 7 — Wochen-Review

- KPI-Review gegen `00-shared/KPI-DASHBOARD.md`.
- Entscheidung: Welche 3–5 Bereiche laufen am besten? Dort Budget erhöhen.
- Woche 2 planen.

---

## Wochen-Ziele

| KPI | Ziel Woche 1 | Ziel Woche 2 | Ziel Woche 4 |
|---|---|---|---|
| Live Landing Pages | 14 | 14 | 14 |
| Aktive E-Mail-Sequenzen | 14 | 14 | 14 |
| Leads gesamt | 300 | 800 | 2.500 |
| Umsatz gesamt | 500 € | 2.000 € | 8.000 € |
| Bereiche mit ersten Sales | 3–5 | 5–8 | 8–10 |

---

## Täglicher Ablauf

### Morgens (30 Min)
- Dashboard checken: neue Leads, Conversion-Raten, Ausgaben.
- Blocker identifizieren.

### Tagsüber (fokussierte Blöcke)
- **Block 1:** 3 Bereiche bearbeiten (jeweils 1–2 Stunden).
- **Block 2:** 3 weitere Bereiche.
- **Block 3:** 2–3 weitere Bereiche + Automation.

### Abends (15 Min)
- Tages-Update: Was wurde live gebracht?
- Nächste Tagesprioritäten setzen.

---

## Ressourcenbedarf

| Ressource | geschätzter Bedarf |
|---|---|
| Menschliche Arbeitszeit | 6–8 h/Tag für Steuerung, Entscheidungen, Compliance |
| Agent/Automation-Zeit | 24/7 verfügbar für Content, E-Mails, Reporting |
| Paid-Traffic-Budget | 1.500 €/Woche (alle Bereiche zusammen) |
| Tool-Kosten/Monat | 300–500 € (Brevo, n8n, GoHighLevel, Hosting) |

---

## Risiken beim Parallel-Start

| Risiko | Gegenmaßnahme |
|---|---|
| Zu viel Aufmerksamkeitssplitting | Strikter Tagesplan, nur 1–2 Bereiche pro Block |
| Qualitätsverlust | Templates aus `00-shared/` nutzen, Checklisten |
| Budget-Überziehung | Tägliches Paid-Budget-Cap pro Bereich |
| Technische Komplexität | Einheitlicher Stack, zentraler Lead-Router |
| Compliance bei PKV/Finanzen | Disclaimer vor jedem Live-Gang prüfen |

---

## Nächste Aktion

1. Bestätige den Parallel-Start.
2. Ich richte den gemeinsamen Tech-Stack ein (Domain, Brevo, n8n, Tracking).
3. Wir starten Tag 1 sofort.
