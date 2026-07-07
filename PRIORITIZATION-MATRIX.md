# Empire Expansion — Priorisierungsmatrix (14 Bereiche, Parallel-Start)

**Update:** Entscheidung getroffen — alle 14 Bereiche starten **parallel**, nicht phasenweise. Diese Matrix dient nicht mehr der Startreihenfolge, sondern der **Prioritäts-Tier-Einordnung**: wo geht die knappe Owner-Zeit (Freigaben, Budget-Entscheidungen, Compliance-Checks) zuerst hin, wo läuft es weitgehend automatisiert im Hintergrund mit.

Bewertung nach fünf Kriterien (Skala 1–5): Marktreife, Marge pro Lead/Sale, Automatisierbarkeit, Synergie im Ökosystem, Zeit bis erster Umsatz (5 = am schnellsten).

| Bereich | Marktreife | Marge | Automatisierbarkeit | Synergie | Zeit bis Umsatz | **Gesamt** | **Tier** |
|---|---:|---:|---:|---:|---:|---:|:---|
| Lead Generation PKV | 5 | 5 | 4 | 5 | 3 | **22** | **A** |
| Affiliate Marketing | 5 | 4 | 5 | 5 | 2 | **21** | **A** |
| Finanzielle Freiheit 35+ | 4 | 4 | 5 | 5 | 3 | **21** | **A** |
| KI-Integrationen 35+ | 4 | 5 | 4 | 4 | 3 | **20** | **A** |
| Marketing Agency Traffic | 4 | 4 | 4 | 5 | 3 | **20** | **A** |
| PDFs & Guides | 4 | 3 | 5 | 5 | 2 | **19** | B |
| Immobilien & Baufinanzierung | 4 | 5 | 3 | 4 | 3 | **19** | B |
| Selbstständigkeit / Business-Setup | 3 | 4 | 4 | 5 | 3 | **19** | B |
| App-Ideen & App Store | 3 | 4 | 3 | 4 | 4 | **18** | B |
| Gesundheit & Prävention 40+ | 4 | 3 | 4 | 3 | 3 | **17** | B |
| TikTok Shop | 3 | 3 | 4 | 4 | 2 | **16** | B |
| Nachhaltigkeit & Eco | 2 | 3 | 4 | 3 | 2 | **14** | C |
| Lead Generation Dropshipping | 3 | 2 | 4 | 3 | 2 | **14** | C |
| Reisen & Lifestyle 35+ | 3 | 2 | 4 | 2 | 2 | **13** | C |

**Hinweis:** Werte für 09–14 sind Arbeitsannahmen ohne echte Traffic-/Conversion-Daten — nach den ersten 30 Tagen mit echten CPL/CAC/ROAS-Zahlen aus dem KPI-Dashboard neu bewerten und Tabelle korrigieren.

---

## Was Tier bedeutet, wenn ALLES parallel läuft

Da kein Bereich mehr wartet, ersetzt „Tier" die alte „Phase". Alle 14 Ordner bekommen sofort Landing Page, Lead-Magnet, E-Mail-Sequenz und n8n-Routing (siehe `00-shared/`). Der Unterschied liegt nur in **wie viel Owner-Aufmerksamkeit** und **wie viel Budget** jeder Bereich in Woche 1–4 bekommt:

### Tier A — höchste Owner-Priorität (5 Bereiche)
**PKV, Affiliate Marketing, Finanzielle Freiheit, KI-Integrationen, Marketing Agency Traffic**

- Bekommen zuerst Ad-Budget (Meta/LinkedIn Testkampagnen)
- Owner prüft/genehmigt hier zuerst: Partnerprogramm-Anträge, Preisgestaltung, Kundengespräche
- Wöchentliches Review mit Owner (nicht nur Dashboard-Check)

### Tier B — Standard-Automatisierung (6 Bereiche)
**PDFs, Immobilien, Selbstständigkeit, App-Ideen, Gesundheit, TikTok Shop**

- Läuft nach Setup weitgehend automatisiert (Content-Kalender, E-Mail-Sequenzen, n8n)
- Owner-Freigabe nur bei Ausgaben > Schwellenwert oder Compliance-Fragen
- Review alle 2 Wochen

### Tier C — Monitoring, geringste Priorität (3 Bereiche)
**Nachhaltigkeit, Dropshipping, Reisen/Lifestyle**

- Content läuft organisch/automatisiert, kein Paid-Budget in Monat 1
- Monatliches Review; nur hochziehen, wenn Daten (CPL, Conversion) besser sind als angenommen

---

## Cross-Selling-Cluster (nutzt Parallel-Start aus)

Da alle Bereiche gleichzeitig Leads sammeln, lohnt sich sofortiges Cross-Tagging über den zentralen `n8n-lead-router.json` (siehe `00-shared/`):

- **Finanz-Cluster:** Finanzielle Freiheit → PKV → Immobilien/Baufinanzierung → Affiliate (ETF-Broker)
- **Business-Cluster:** Selbstständigkeit/Business-Setup → KI-Integrationen → Marketing Agency Traffic
- **Consumer-Cluster:** TikTok Shop → Dropshipping → Reisen/Lifestyle → Nachhaltigkeit
- **Content-Cluster (Lead-Magnet-Distribution):** PDFs & Guides → App-Ideen (gleicher Traffic, unterschiedliches Format)

Ein Lead aus Tier C kann sofort für Tier A qualifiziert und automatisch getaggt werden — das ist der Sinn des zentralen Routers, nicht Sequenzierung.

---

## Risiko-Einschätzung

| Bereich | Haupt-Risiko | Gegenmaßnahme |
|---|---|---|
| PKV | Regulatorik/Compliance | Disclaimer, keine Versicherungsberatung ohne Lizenz, nur Lead-Vermittlung |
| Affiliate | Abhängigkeit von Partnerprogrammen | Mehrere Netzwerke + eigene E-Mail-Liste |
| Finanzielle Freiheit | Keine Anlageberatung ohne Lizenz | Nur Bildungsinhalte, Haftungsausschluss, keine Einzelwertempfehlungen |
| KI-Agentur | Lange Sales-Cycles | Niedrigschwellige Pakete + schnelle Erfolgsnachweise |
| Agency | Abhängigkeit von wenigen Kunden | Standardisierte Produkte statt Custom-Stunden |
| PDFs | Geringe Conversion ohne Distribution | Funnel + Paid-Traffic ab Tag 1 |
| Immobilien | Vermittlerregister §34i GewO / Beratungspflichten | Nur Lead-Vermittlung, kein Beratungsversprechen ohne Zulassung |
| Selbstständigkeit | Haftungsfragen bei Setup-Beratung | Klare Abgrenzung: Information statt Rechts-/Steuerberatung |
| App-Ideen | Hohe Entwicklungskosten | MVP zuerst als Web-App validieren |
| Gesundheit | Heilversprechen/HWG-Verstöße | Keine Heilaussagen, nur Prävention/Lifestyle, Disclaimer |
| TikTok Shop | Algorithmus-/Plattformrisiko | Mehrkanal-Strategie + E-Mail-Liste |
| Nachhaltigkeit | Greenwashing-Vorwurf | Nur belegbare Aussagen, Quellen offenlegen |
| Dropshipping | Lieferketten/Retouren | EU-Sourcing, klare AGB |
| Reisen/Lifestyle | Niedrige Marge pro Lead | Cross-Sell in Finanz-/Business-Cluster als Hauptzweck, nicht Standalone-Umsatz |

---

## Empfohlene erste Aktion

**Diese Woche:** Owner-Zeit nach Tier verteilen — volle Aufmerksamkeit auf die 5 Tier-A-Bereiche (Freigaben, erstes Ad-Budget, Partnerprogramm-Anmeldungen), Tier B/C laufen über die in jedem Ordner hinterlegte `EXECUTION-ROADMAP.md` / `WEEK-1-TASKS.md` weitgehend selbstständig an.
