# App-Concept: „VermoegenPlaner“ — Finanz-Navigator für Berufstätige 35–55

## Produktvision

„VermoegenPlaner“ ist der unabhängige Finanz-Navigator für Berufstätige zwischen 35 und 55 Jahren in Deutschland, Österreich und der Schweiz (DACH). Die App bündelt Wissen, Planungswerkzeuge und Checklisten zu den Themen Rente, Vermögensaufbau, Steueroptimierung und Versicherungen – ohne Anlageberatung, dafür mit klarer Handlungsorientierung.

## Zielgruppe

- **Primär**: Berufstätige, 35–55 Jahre, Haushaltseinkommen 60.000–150.000 € brutto/Jahr
- **Berufe**: Angestellte, Beamte, Selbstständige, Führungskräfte
- **Pain Points**:
  - Unklarheit über die eigene Rentensituation („Wie viel Rente bekomme ich wirklich?“)
  - Vermögensaufbau wird aufgeschoben, weil man nicht weiß, wo man anfangen soll
  - Angst vor Fehlentscheidungen bei PKV, ETF-Sparplan oder Lebensversicherung
  - Überflutung durch Finanz-Content, aber kein persönlicher Fahrplan
- **Ziel**: Innerhalb von 30 Minuten einen klaren Überblick über die eigene finanzielle Lage und konkrete nächste Schritte

## Kern-Features (MVP-Scope)

### 1. Rentenlücke-Rechner
- Eingabe: Alter, Bruttoeinkommen, Rentenversicherungsjahre, gewünschtes Renteneintrittsalter
- Ausgabe: Geschätzte gesetzliche Rente, individuelle Lücke, empfohlene monatliche Sparrate
- Keine Verbindung zu echten Rentenkonten – alles Schätzung auf Basis offizieller Rentenformeln

### 2. Vermögens-Score (Quiz)
- 10 Fragen zu Einkommen, Rücklagen, Schulden, Absicherung, Anlageverhalten
- Ergebnis: Persönlicher Score plus Einordnung (z. B. „Aufholbedarf“, „Solide“, „Aufgestellt“)
- Konkrete Handlungsempfehlungen basierend auf dem Ergebnis

### 3. Finanz-Planer / To-Do-Modul
- Persönliche Finanz-Roadmap mit Meilensteinen
- Vorgefertigte Checklisten: „Notgroschen aufbauen“, „PKV prüfen“, „ETF-Sparplan starten“, „Steuererklärung optimieren“
- Fortschrittsanzeige und wöchentliche Erinnerungen

### 4. Wissens-Bibliothek
- Kuratierte Artikel und Guides zu DACH-relevanten Themen
- Fokus auf: Rente, Steuern, ETF, PKV, Absicherung
- Alle Inhalte sind nicht als Anlageberatung gekennzeichnet

### 5. Vergleichs-Checklisten (Affiliate-fähig)
- PKV-Vergleichs-Checkliste
- ETF-Sparplan-Vergleichs-Checkliste
- Versicherungs-Checkliste
- Mit externen Vergleichs-Links als Affiliate-Option (später)

## Unique Selling Proposition (USP)

> „Der einzige Finanz-Planer, der speziell für Berufstätige 35+ in DACH entwickelt wurde – unabhängig, ohne Anlageberatung und mit sofort umsetzbaren nächsten Schritten.“

**Differenzierung gegenüber Wettbewerbern:**
- Kein Zahlungs-Drittanbieter wie Finanzguru, Moneylover (kein Bank-Login nötig)
- Keine Anlageberatung wie bei vielen Robo-Advisors
- DACH-spezifisch: Deutsche Rentenformeln, Steuerregeln, PKV-Logik
- Fokus auf Planung statt Tracking

## Monetarisierung

### Freemium-Modell

| Plan | Preis | Inhalt |
|------|-------|--------|
| **Free** | Kostenlos | Rentenlücke-Rechner, Vermögens-Score, 5 Checklisten, Basis-Wissens-Bibliothek |
| **Premium** | 12,99 €/Monat oder 99,99 €/Jahr (≈ 36 % Ersparnis) | Alle Rechner, unbegrenzte Checklisten, persönliche Roadmap, PDF-Reports, monatliche Finanz-Checkups |
| **Premium Plus** | 199 €/Jahr | Premium + 1x jährlicher 30-Minuten-Online-Check mit Finanzcoach (Kalendly-Integration) |

### Zusatz-Einnahmequellen
- **Affiliate-Provisionen**: PKV-, ETF-Sparplan-, Versicherungsvergleiche
- **B2B-Lizenzen**: Für Unternehmen als Mitarbeiter-Benefit (ab 10 Lizenzen)
- **1:1-Coachings**: Über integrierte Terminbuchung

## MVP-Scope für Woche 1–4

**Ziel vor Store-Launch:** Erst eine Web-App als Lead-Magnet und Validierungsinstrument. Der native App-Store-Launch folgt erst nach erfolgreicher Lead-Generierung.

### MVP der nativen App (später)
- Rentenlücke-Rechner
- Vermögens-Score
- Finanz-Planer mit 5 Checklisten
- Wissens-Bibliothek mit 10 Artikeln
- Premium-Paywall nach 7 Tagen Testphase
- Tracking via RevenueCat (Sub) + Mixpanel/PostHog (Events)

### Nicht im MVP
- Bank-API-Integration
- Echte Steuerberechnung mit ELSTER-Anbindung
- Community-Feature
- B2B-Portal
- Automatische Portfolio-Steuerung

## Marken-Tonalität

- **Seriös, aber nicht steif**: Klare Sprache, keine Fachjargon-Flut
- **Aufmunternd**: „Sie sind nicht zu spät dran – aber je früher, desto besser.“
- **Transparent**: Keine versteckten Kosten, keine falschen Versprechen
- **DACH-Fokus**: Zahlen, Gesetze und Beispiele für Deutschland, Österreich, Schweiz

## Erfolgskriterien für das MVP

| KPI | Ziel Woche 4 | Ziel Tag 90 |
|-----|--------------|-------------|
| Wartelisten-/Lead-Erfassungen | 100 | 2.000 |
| Landing-Page-Conversion | > 15 % | > 25 % |
| E-Mail-Öffnungsrate | > 30 % | > 35 % |
| Beta-Tester für native App | 20 | 200 |
| Zahlende Nutzer | 0 (noch kein Store-Launch) | 30 |

## Compliance-Hinweis

- Alle Inhalte enthalten einen Disclaimer: „Keine Anlageberatung, keine Steuerberatung, keine Rechtsberatung.“
- Keine individuelle Anlageempfehlung, sondern allgemeine Informationen
- Keine medizinischen oder versicherungsrechtlichen Zusagen
- DSGVO-konforme Datenerfassung von Beginn an
- Bei Finanz-Affiliate-Partnerschaften: Offenlegung der Provisionsbeziehung

## Nächster Schritt

1. Lead-Magnet „Rentenlücke-Rechner“ als Web-App bauen
2. Landing Page mit Warteliste online stellen
3. 5-teilige E-Mail-Sequenz für Wartelisten-Anmeldungen aktivieren
