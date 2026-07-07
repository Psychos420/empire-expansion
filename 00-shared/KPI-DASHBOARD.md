# KPI-Dashboard — Was wir tracken, wie oft und welche Ziele wir anstreben

Dieses Dokument definiert die zentralen KPIs für das Empire-Expansion-Ökosystem. Jeder der 14 Bereiche trackt diese Kennzahlen in seinem Bereich und liefert sie an das zentrale Reporting.

---

## Reporting-Rhythmen

| Bericht | Frequenz | Verantwortlich | Werkzeug |
|---|---|---|---|
| **Tägliches Health-Check** | Täglich | Bereichs-Owner | Brevo / GoHighLevel / Meta Ads Manager |
| **Wochen-Review** | Wöchentlich (Montag) | Bereichs-Owner + Lead | Looker Studio / Notion |
| **Monats-Review** | Monatlich | Lead | Looker Studio-Dashboard |
| **Quartals-Strategie** | Quartalsweise | Lead + Bereichs-Owner | Präsentation auf Basis der Dashboards |

---

## 1. Traffic-KPIs

| KPI | Definition | Tool | Ziel M1 | Ziel M3 | Ziel M6 |
|---|---|---:|---:|---:|---:|
| **Website-Sessions** | Anzahl Besuche aller Landing Pages | GA4 | 5.000 | 25.000 | 80.000 |
| **Unique Visitors** | Einzelne Besucher | GA4 | 4.000 | 20.000 | 65.000 |
| **Traffic-Quellen-Anteil** | Anteil Paid / Organic / Social / Direct / E-Mail | GA4 | dokumentieren | dokumentieren | dokumentieren |
| **CTR Ads** | Klicks / Impressionen | Meta Ads / LinkedIn | > 1 % | > 1,5 % | > 2 % |
| **CPM** | Kosten pro 1.000 Impressionen | Meta Ads / LinkedIn | < 10 € | < 8 € | < 6 € |

---

## 2. Lead-Generierung

| KPI | Definition | Tool | Ziel M1 | Ziel M3 | Ziel M6 |
|---|---|---:|---:|---:|---:|
| **Leads gesamt** | Neue Opt-ins (E-Mail/Telefon) | Brevo / GoHighLevel | 500 | 3.000 | 10.000 |
| **Leads pro Bereich** | Neue Opt-ins je Bereich | Brevo / GoHighLevel | individuell | individuell | individuell |
| **Landing-Page-Conversion** | Opt-ins / Besucher | GA4 + Landing-Page-Tool | > 30 % | > 40 % | > 45 % |
| **Cost per Lead (CPL)** | Ad Spend / Leads | Ads Manager + Sheets | < 5 € | < 4 € | < 3 € |
| **Lead-Qualität-Score** | Bewertung durch Verhalten/Fragebogen | n8n / GoHighLevel | einführen | etablieren | optimieren |

---

## 3. E-Mail / SMS / WhatsApp Marketing

| KPI | Definition | Tool | Ziel M1 | Ziel M3 | Ziel M6 |
|---|---|---:|---:|---:|---:|
| **E-Mail-Liste gesamt** | Aktive Kontakte | Brevo / GoHighLevel | 400 | 2.500 | 8.000 |
| **Open Rate** | Geöffnet / Zugestellt | Brevo | > 40 % | > 45 % | > 50 % |
| **Click Rate** | Klicks / Zugestellt | Brevo | > 5 % | > 7 % | > 10 % |
| **Welcome-Open Rate** | Öffnungen E-Mail #1 | Brevo | > 50 % | > 55 % | > 60 % |
| **SMS-Öffnungsrate** | Geöffnet / Versendet | Brevo / Twilio | > 80 % | > 85 % | > 90 % |
| **WhatsApp-Response-Rate** | Antworten / Versendet | WhatsApp API | > 15 % | > 20 % | > 25 % |
| **Unsubscribe-Rate** | Abmeldungen / Versendet | Brevo | < 0,5 % | < 0,4 % | < 0,3 % |

---

## 4. Umsatz & Conversion

| KPI | Definition | Tool | Ziel M1 | Ziel M3 | Ziel M6 |
|---|---|---:|---:|---:|---:|
| **Umsatz gesamt** | Brutto-Umsatz aller Bereiche | Stripe + Sheets | 2.000 € | 15.000 € | 50.000 € |
| **Low-Ticket-Umsatz** | Umsatz durch PDFs, Guides, Tools | Stripe | 500 € | 4.000 € | 12.000 € |
| **High-Ticket-Umsatz** | Umsatz durch Beratung, Agentur, Projekte | Stripe + CRM | 1.500 € | 11.000 € | 38.000 € |
| **Low-Ticket-Conversion** | Käufer / Leads | Stripe + Brevo | > 3 % | > 5 % | > 7 % |
| **Terminbuchungsrate** | Termine / qualifizierte Leads | GoHighLevel | > 5 % | > 8 % | > 10 % |
| **Show-Up-Rate** | Wahrgenommene Termine / Gebuchte Termine | GoHighLevel | > 60 % | > 70 % | > 75 % |
| **Close-Rate High-Ticket** | Abschlüsse / Termine | GoHighLevel | > 15 % | > 20 % | > 25 % |

---

## 5. Kosten & Profitabilität

| KPI | Definition | Tool | Ziel M1 | Ziel M3 | Ziel M6 |
|---|---|---:|---:|---:|---:|
| **Customer Acquisition Cost (CAC)** | Gesamtkosten / Neue Kunden | Sheets / Looker Studio | < 20 € | < 15 € | < 10 € |
| **CAC Lead** | Ad Spend + Toolkosten / Neue Leads | Sheets / Looker Studio | < 5 € | < 4 € | < 3 € |
| **Lifetime Value (LTV)** | Durchschnittlicher Umsatz pro Kunde | Stripe + CRM | > 60 € | > 80 € | > 100 € |
| **LTV/CAC** | LTV geteilt durch CAC | Sheets / Looker Studio | > 3 | > 4 | > 5 |
| **ROAS** | Umsatz / Ad Spend | Meta Ads + Stripe | > 2 | > 3 | > 4 |
| **Toolkosten-Quote** | Toolkosten / Umsatz | Sheets | < 20 % | < 15 % | < 10 % |

---

## 6. Automation & Operations

| KPI | Definition | Tool | Ziel M1 | Ziel M3 | Ziel M6 |
|---|---|---:|---:|---:|---:|
| **Automatisierungsgrad** | % wiederkehrender Prozesse, die automatisiert laufen | n8n + Dokumentation | 60 % | 75 % | 85 % |
| **n8n-Workflows** | Anzahl aktiver Workflows | n8n | > 10 | > 25 | > 50 |
| **Workflow-Fehlerrate** | Fehlgeschlagene Runs / Gesamtruns | n8n | < 5 % | < 3 % | < 2 % |
| **Manuelle Eingriffe pro Woche** | Geschätzte manuelle Handlungen | Notion | dokumentieren | reduzieren | minimieren |
| **DSGVO-Konformität** | Double-Opt-In-Rate, Datenschutzerklärung | Brevo / Cookie-Tool | 100 % | 100 % | 100 % |

---

## 7. Inhalte & Engagement

| KPI | Definition | Tool | Ziel M1 | Ziel M3 | Ziel M6 |
|---|---|---:|---:|---:|---:|
| **Content-Stücke pro Woche** | Posts, Videos, E-Mails, Blog-Artikel | Notion | > 5 | > 10 | > 15 |
| **Organic Reach** | Reichweite ohne Paid Ads | Social-Plattformen | dokumentieren | dokumentieren | dokumentieren |
| **Engagement-Rate** | Interaktionen / Follower | Social-Plattformen | > 2 % | > 3 % | > 4 % |
| **Lead-Magnet-Downloads** | Downloads / Opt-ins | Brevo | dokumentieren | dokumentieren | dokumentieren |

---

## Zentrale Zielwerte — Zusammenfassung

| KPI | Ziel Monat 1 | Ziel Monat 3 | Ziel Monat 6 |
|---|---:|---:|---:|
| Gesamte Leads | 500 | 3.000 | 10.000 |
| E-Mail-Liste | 400 | 2.500 | 8.000 |
| Umsatz gesamt | 2.000 € | 15.000 € | 50.000 € |
| Gesamt-CAC | < 5 € | < 4 € | < 3 € |
| LTV/CAC | > 3 | > 4 | > 5 |
| Automatisierungsgrad | 60 % | 75 % | 85 % |
| ROAS | > 2 | > 3 | > 4 |

---

## Looker Studio Dashboard-Struktur

### Seite 1: Executive Summary
- Umsatz gesamt (MTD, Vergleich Vormonat)
- Leads gesamt
- CAC und LTV/CAC
- Top-Performing-Bereiche

### Seite 2: Traffic & Conversion
- Sessions nach Quelle
- Landing-Page-Conversions
- CPL nach Kanal
- Top-Landing-Pages

### Seite 3: E-Mail & CRM
- Listenwachstum
- Open/Click Rates
- Käufer- vs. Nicht-Käufer-Listen
- Pipeline-Status High-Ticket

### Seite 4: Automation Health
- n8n-Workflow-Status
- Fehlerrate
- Manuelle Eingriffe

---

## Datenquellen

| Quelle | Nutzung |
|---|---|
| **Google Analytics 4** | Traffic, Conversions, Ereignisse |
| **Brevo** | E-Mail-Listen, Öffnungs-/Klickraten |
| **GoHighLevel** | CRM, Pipeline, Termine, SMS |
| **Stripe** | Umsatz, Käuferdaten, Refunds |
| **Meta Ads Manager** | Ad Spend, ROAS, CPL |
| **n8n** | Automation-Logs, Lead-Routing |
| **Google Sheets** | Manuelle Eingaben, berechnete KPIs |

---

## Reporting-Template (Wochen-Review)

```
Woche: [KW / Datum]
Bereich: [01–14 / Name]

Neue Leads: [Zahl]
CPL: [€]
Landing-Page-CR: [%]
E-Mail-Open-Rate: [%]
Low-Ticket-Umsatz: [€]
High-Ticket-Termine: [Zahl]
Umsatz gesamt: [€]
ROAS: [X]

Top-Erkenntnis: [1 Satz]
Nächste Aktion: [1 Satz]
```

---

## Best Practices

- KPIs **vor** Starten eines Bereichs definieren und im Tracking hinterlegen.
- Jede Landing Page bekommt eigene UTM-Parameter.
- Wöchentlich mindestens 30 Minuten für Daten-Review einplanen.
- Nicht alle KPIs gleichzeitig optimieren — Fokus auf den Engpass-KPI.
- Dashboards so einfach wie möglich halten, damit sie regelmäßig genutzt werden.
