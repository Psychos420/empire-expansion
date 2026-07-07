# 00-shared — Gemeinsames Fundament für Empire Expansion

Dieses Verzeichnis enthält die zentralen Standards, Templates und den Tech-Stack, die alle 14 Expansionsbereiche des Empire-Expansion-Projekts nutzen. Ziel ist eine einheitliche Basis, damit jeder Bereich schneller startet, Leads und Daten nahtlos zwischen den Bereichen fließen und der Automatisierungsgrad kontinuierlich steigt.

---

## Was ist `00-shared`?

`00-shared` ist das **Single Source of Truth** für:

- Den einheitlichen Tech-Stack
- Wiederverwendbare Marketing-Templates (E-Mail-Sequenzen, Landing Pages, Funnels)
- Automation-Standards und Vernetzungslogik
- KPI-Definitionen und Reporting-Rhythmen
- Copy-Formeln und Design-Prinzipien

Es ist kein eigenständiger Bereich, sondern das **Betriebssystem** für alle anderen Bereiche.

---

## Wie die 14 Bereiche `00-shared` nutzen

Jeder Bereichsordner (`01-affiliate-marketing` bis `14-nachhaltigkeit-eco`) hat seine eigene Strategie, aber alle greifen auf `00-shared` zurück:

| Dokument in `00-shared` | Nutzung in den Bereichen |
|---|---|
| `TECH-STACK.md` | Tool-Auswahl für Landing Page, CRM, Automation, Zahlungen etc. |
| `EMAIL-SEQUENCE-TEMPLATE.md` | Basis für Willkommens- und Nurture-Sequenzen, mit Bereichs-Platzhaltern anpassen |
| `LANDING-PAGE-TEMPLATE.md` | Struktur und Copy für alle Landing Pages und Lead-Magnet-Seiten |
| `FUNNEL-BLUEPRINT.md` | Generischer Funnel-Aufbau für Lead-Generierung, Low-Ticket und High-Ticket |
| `KPI-DASHBOARD.md` | Welche Kennzahlen gemessen werden, Zielwerte für Monat 1/3/6 |
| `AUTOMATION-ORCHESTRATION.md` | Vernetzung der Workflows über n8n/Make zwischen den Bereichen |

---

## Grundsätze

1. **Audience First:** E-Mail-/SMS-/WhatsApp-Listen sind das wichtigste Asset. Jeder Bereich baut diese Listen auf.
2. **Automation by Default:** 70–90 % wiederkehrender Arbeit laufen über n8n/Make, Kimi/Claude und CRM-Automation.
3. **Low-Ticket → High-Ticket:** Günstige Einstiegsprodukte finanzieren Traffic und qualifizieren für teurere Angebote.
4. **Datengetriebene Entscheidungen:** Jeder Bereich misst CAC, LTV, Conversion-Rate und ROAS.
5. **Compliance & Vertrauen:** Transparente Inhalte, klare Disclaimer, DSGVO-konforme Prozesse — besonders in Finanzen, Versicherung und Gesundheit.

---

## Dateien in diesem Verzeichnis

- `README.md` — Diese Datei
- `TECH-STACK.md` — Einheitlicher Tech-Stack mit Zweck, Empfehlungen, Alternativen, Kosten und Einrichtung
- `EMAIL-SEQUENCE-TEMPLATE.md` — 5-teilige Willkommens-E-Mail-Sequenz (Deutsch) mit Platzhaltern
- `LANDING-PAGE-TEMPLATE.md` — Struktur einer High-Converting Landing Page
- `FUNNEL-BLUEPRINT.md` — Generischer Funnel von Traffic bis High-Ticket
- `KPI-DASHBOARD.md` — KPI-Tracking und Zielwerte
- `AUTOMATION-ORCHESTRATION.md` — Vernetzung der Automation zwischen den Bereichen

---

## Schnellstart für neue Bereiche

1. Diese README lesen.
2. `TECH-STACK.md` lesen und Tools einrichten.
3. Für den ersten Lead-Magneten `LANDING-PAGE-TEMPLATE.md` und `EMAIL-SEQUENCE-TEMPLATE.md` kopieren und anpassen.
4. Funnel nach `FUNNEL-BLUEPRINT.md` aufbauen.
5. KPIs aus `KPI-DASHBOARD.md` im Tracking hinterlegen.
6. Automation nach `AUTOMATION-ORCHESTRATION.md` mit dem zentralen Orchestrator verbinden.

---

## Änderungen an `00-shared`

Wenn ein Bereich ein besseres Template, eine neue Automation oder einen zusätzlichen KPI entwickelt, der für alle relevant ist, wird das hier dokumentiert. `00-shared` lebt mit dem Ökosystem.
