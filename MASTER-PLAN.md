# Empire Expansion — Masterplan

## Vision

Aufbau eines automatisierten Geschäftsökosystems für die Zielgruppe **35+** in DACH. Jedes Geschäftsfeld generiert Leads, Umsatz und Daten für die anderen Felder. Der Mensch entscheidet; Agenten und Workflows führen aus.

---

## Strategische Säulen

1. **Audience First:** E-Mail-/SMS-/WhatsApp-Listen sind das wichtigste Asset. Jeder Bereich füttert diese Listen.
2. **Automation by Default:** 70–90 % wiederkehrender Arbeit laufen über n8n/Make, Kimi/Claude und CRM-Automation.
3. **Low-Ticket → High-Ticket:** Günstige Einstiegsprodukte (PDFs, TikTok-Shop-Artikel) finanzieren Traffic und qualifizieren für teurere Angebote (PKV, KI-Agentur, Agentur).
4. **Datengetriebene Entscheidungen:** Jeder Bereich misst CAC, LTV, Conversion-Rate und ROAS.
5. **Compliance & Vertrauen:** Besonders bei Finanzen, Versicherung und Gesundheit: transparente Inhalte, klare Disclaimer, DSGVO-konforme Prozesse.

---

## Ausführungsplan — Parallel-Start aller 14 Bereiche

**Entscheidung (überschreibt frühere Phasenlogik):** Alle 14 Bereiche starten gleichzeitig, nicht sequenziell. Jeder Ordner (`01-affiliate-marketing` bis `14-nachhaltigkeit-eco`) hat bereits Landing Page, Lead-Magnet, E-Mail-Sequenz und Anbindung an den zentralen `00-shared/n8n-lead-router.json`. Steuerung erfolgt nicht über Reihenfolge, sondern über **Owner-Aufmerksamkeit nach Tier** (siehe [PRIORITIZATION-MATRIX.md](./PRIORITIZATION-MATRIX.md)):

- **Tier A** (PKV, Affiliate, Finanzielle Freiheit, KI-Integrationen, Marketing Agency Traffic): bekommt zuerst Ad-Budget und wöchentliche Owner-Reviews.
- **Tier B** (PDFs, Immobilien, Selbstständigkeit, App-Ideen, Gesundheit, TikTok Shop): läuft automatisiert an, Owner-Freigabe nur bei Ausgaben/Compliance.
- **Tier C** (Nachhaltigkeit, Dropshipping, Reisen/Lifestyle): organisch/automatisiert, kein Paid-Budget in Monat 1, monatliches Review.

### Woche 1 — Foundation (alle 14 parallel)

| Aufgabe | Umfang | Erfolgskriterium |
|---|---|---|
| Lead-Magnet pro Bereich finalisieren (liegt je Ordner in `LEAD-MAGNET.md`) | 14 Bereiche | 14 PDFs/Checklisten final |
| Landing Page live schalten (`landing-page.html` je Ordner, aus `00-shared/LANDING-PAGE-TEMPLATE.md`) | 14 Bereiche | 14 Landing Pages live |
| E-Mail-Provider + Sequenzen aktivieren (`EMAIL-SEQUENCE.md` je Ordner) | 14 Bereiche | Alle Willkommens-Sequenzen aktiv |
| Zentralen n8n-Lead-Router deployen (`00-shared/n8n-lead-router.json`) | 1× zentral | Router läuft, routet Leads nach Tag in richtige Liste/Sequenz |
| Rechtliche Basis-Textbausteine (Impressum, Datenschutz, Haftungsausschluss je Nische) | 14 Bereiche | Compliance-Check bestanden (Owner-Freigabe Pflicht) |

### Woche 2–4 — Traffic & erste Conversions, differenziert nach Tier

| Tier | Aktion | Ziel Ende Monat 1 |
|---|---|---|
| A | Meta/LinkedIn-Testkampagnen (20–30 €/Tag je Bereich), Partnerprogramme beantragen (Awin, financeAds, Ottonova, Baufinanzierungs-Vermittler), erste Beratungstermine buchen | ≥250 Leads/Bereich, erste Umsätze in allen 5 |
| B | Organischer Content nach `CONTENT-PLAN.md`, kein/wenig Paid-Budget, Funnel-Optimierung | ≥100 Leads/Bereich |
| C | Nur organischer Content, Cross-Tagging in Finanz-/Business-/Consumer-Cluster (siehe Matrix) | Traffic-Test, keine Umsatzerwartung Monat 1 |

### Monat 2–6 — Skalierung nach Daten, nicht nach Plan

Nach 30 Tagen echte KPI-Daten (CPL, CAC, ROAS aus `00-shared/KPI-DASHBOARD.md`) auswerten und Budget von schlecht performenden Tier-A/B-Bereichen auf gut performende Tier-B/C-Bereiche umschichten — die Tier-Einstufung ist ein Startpunkt, keine feste Regel. Cross-Sell-Cluster (Finanz, Business, Consumer, Content) ab Monat 2 aktiv verknüpfen, damit ein Lead aus einem Bereich automatisch für die anderen passenden Bereiche getaggt wird.

---

## Gemeinsamer Tech-Stack

| Funktion | Tool-Empfehlung | Alternative |
|---|---|---|
| Landing Pages | Carrd / WordPress + Elementor / Webflow | Framer, Shopify |
| E-Mail/SMS Marketing | Brevo / ActiveCampaign | Klaviyo, Mailchimp |
| CRM & Funnel | GoHighLevel | HubSpot, Pipedrive |
| Automation | n8n (self-hosted) | Make, Zapier |
| KI-Assistenten | Kimi / Claude | OpenAI API |
| Zahlungen | Stripe + PayPal | Gumroad, Payhip |
| Analytics | Google Analytics 4 + Looker Studio | Plausible, PostHog |
| App-Monetarisierung | RevenueCat | Stripe Billing |
| Projekt-Management | Notion / Linear | ClickUp, Asana |

---

## Zentrale KPIs

| KPI | Ziel Monat 1 | Ziel Monat 3 | Ziel Monat 6 |
|---|---|---|---|
| Gesamte Leads | 500 | 3.000 | 10.000 |
| E-Mail-Liste | 400 | 2.500 | 8.000 |
| Umsatz gesamt | 2.000 € | 15.000 € | 50.000 € |
| Gesamt-CAC | < 5 € | < 4 € | < 3 € |
| LTV/CAC | > 3 | > 4 | > 5 |
| Automatisierungsgrad | 60 % | 75 % | 85 % |

---

## Rollenverteilung Mensch vs. Agent

| Aufgabe | Mensch | Agent/Workflow |
|---|---|---|
| Strategie & Priorisierung | ✓ |  |
| Endgültige Freigaben (Budget, Deals, Posts) | ✓ |  |
| Compliance-Check (PKV, Finanzen, Gesundheit) | ✓ | Unterstützung |
| Kundenbeziehung & Verkaufsgespräche | ✓ | Vorbereitung |
| Marktrecherche |  | ✓ |
| Content-Erstellung (Erstentwürfe) |  | ✓ |
| Funnel-Technik & Automation |  | ✓ |
| Reporting & Datenanalyse |  | ✓ |
| A/B-Test-Ideen generieren | Unterstützung | ✓ |

---

## Risiken & Gegenmaßnahmen

| Risiko | Gegenmaßnahme |
|---|---|
| 14 Bereiche parallel überfordern Owner-Zeit | Tier-System (siehe Matrix) — volle Aufmerksamkeit nur auf Tier A, Tier B/C laufen automatisiert |
| Abhängigkeit von Plattformen | E-Mail-Liste als zentrales Asset aufbauen |
| Compliance bei PKV/Finanzen/Gesundheit/Immobilien | Disclaimer, keine unlizenzierte Beratung, Dokumentation je Nische in `EXECUTION-ROADMAP.md` |
| Burnout durch manuelle Prozesse | Zentraler n8n-Lead-Router + Automation-Stack vor Skalierung etablieren |
| Schlechte Conversion | Wöchentliche A/B-Tests, datenbasierte Budget-Allokation, Tier-Neubewertung nach 30 Tagen |
| Budget verstreut sich zu dünn über 14 Bereiche | Paid-Budget nur für Tier A in Monat 1, Tier B/C organisch |

---

## Nächste Aktion

1. Woche 1 (alle 14 parallel) abarbeiten: Lead-Magnete finalisieren, Landing Pages live, E-Mail-Sequenzen aktiv, n8n-Router deployen (Details: [PRIORITIZATION-MATRIX.md](./PRIORITIZATION-MATRIX.md)).
2. Owner-Freigaben für Tier A zuerst einholen (Partnerprogramme, Ad-Budget, Compliance-Texte).
3. Nach 30 Tagen: echte KPI-Daten gegen die Tier-Einstufung prüfen und Budget/Aufmerksamkeit neu verteilen.
