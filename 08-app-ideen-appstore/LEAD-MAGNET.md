# Lead-Magnet: „Rentenlücke-Rechner“ als Web-App

## Lead-Magnet-Name

**„Rentenlücke-Rechner: Wie viel Rente bekommen Sie wirklich?“**

## Ziel

Schnellstmöglich qualifizierte Leads für „VermoegenPlaner“ generieren, bevor die native App im Store landet. Der Rechner liefert sofortigen, persönlichen Nutzen und erfasst dabei E-Mail-Adresse, Alter und Einkommen für die weitere Kommunikation.

## Format

Interaktive Web-App (single-page), die in 2 Minuten eine individuelle Rentenlücken-Berechnung liefert. Kein PDF, kein Download nötig – sofortiges Ergebnis im Browser.

## Warum dieser Lead-Magnet?

- **Hoher Intent**: „Rente“ und „Rentenlücke“ sind stark frequentierte Suchbegriffe bei 35+
- **Emotionaler Pain Point**: Fast jeder Berufstätige fragt sich, ob die Altersvorsorge reicht
- **Sofortiger Nutzen**: Das Ergebnis ist sofort sichtbar und teilbar
- **Gute Qualifizierung**: Wer den Rechner nutzt, hat echtes Interesse an Finanzplanung
- **Einfache Umsetzung**: Keine Bank-APIs, keine komplexen Algorithmen

## Nutzer-Flow

1. **Landing Page**: Headline „Berechnen Sie Ihre Rentenlücke in 2 Minuten“
2. **Eingabe** (5 Felder):
   - Geburtsjahr
   - Geschätztes jährliches Bruttoeinkommen
   - Geschätzte bereits erworbene Rentenjahre
   - Gewünschtes Renteneintrittsalter
   - E-Mail-Adresse
3. **Berechnung**: Sofortige Schätzung auf Basis vereinfachter deutscher Rentenformel
4. **Ergebnis-Seite**:
   - Geschätzte monatliche Netto-Rente
   - Empfohlene monatliche Zusatzsparrate
   - Visualisierung der Lücke
   - CTA: „Auf die Warteliste für VermoegenPlaner setzen“ + PDF-Download „Der 5-Schritte-Rentenplan“
5. **Danke-Seite**: Hinweis auf Bestätigungs-E-Mail, nächste Schritte

## Berechnungslogik (vereinfacht)

> Hinweis: Keine offizielle Rentenversicherungs-Berechnung. Vereinfachte Schätzung für Orientierung.

```textrentenpunkte_pro_jahr = (bruttoeinkommen / durchschnittseinkommen) * 1.0
gesamtpunkte = rentenpunkte_pro_jahr * rentenjahre
monatliche_brutto_rente = gesamtpunkte * aktueller_rentenwert (z. B. 39,32 €)
netto_rente = monatliche_brutto_rente * 0.88  (pauschale Abzüge für Steuern/KV)
rentenluecke = gewuenschte_netto_rente - netto_rente
empfohlene_sparrate = rentenluecke * faktor_entwertung
```

**Eingaben, die im Frontend sichtbar sind:**
- Durchschnittseinkommen: 45.358 € (jährlich, aktueller Durchschnitt D)
- Aktueller Rentenwert West: 39,32 € / Ost: 37,94 €
- Ziel-Netto-Rente (voreingestellt): 70 % des letzten Nettoeinkommens

## Erfasste Daten

| Feld | Verwendung |
|------|------------|
| E-Mail-Adresse | Hauptkommunikationskanal, Warteliste |
| Geburtsjahr | Alterssegmentierung, Rentenberechnung |
| Bruttoeinkommen | Preissegmentierung, individuelle Empfehlungen |
| Rentenjahre | Berechnung |
| Renteneintrittsalter | Berechnung |
| Zeitstempel | Lead-Warming, E-Mail-Timing |

## Angebot nach der Berechnung

Sofortiger Upsell auf Warteliste:

> „Gut, dass Sie jetzt wissen, wo Sie stehen. VermoegenPlaner hilft Ihnen, diese Lücke Schritt für Schritt zu schließen – mit Checklisten, Remindern und einem klaren Plan. Tragen Sie sich auf die Warteliste ein und testen Sie die Beta gratis.“

**Zusätzliches Geschenk (Double-Opt-In-Belohnung):**
PDF „Der 5-Schritte-Rentenplan für Berufstätige 35+“

## technische Umsetzung (ohne externe APIs)

- **Frontend**: Statische HTML/CSS/JS-Seite (oder Carrd/Webflow mit Embed)
- **Berechnung**: Client-seitiges JavaScript
- **Formular**: Tally, Typeform oder selbstgebautes Formular
- **E-Mail-Erfassung**: Brevo oder ConvertKit Formular-Integration
- **PDF-Download**: Manuell erstellte PDF, Download-Link nach Bestätigung
- **Hosting**: Netlify, Vercel oder Carrd-Pro
- **Tracking**: Google Analytics 4 + Meta Pixel (optional, mit Consent)

## Compliance

- Checkbox „Ich möchte den Rentenplan per E-Mail erhalten und akzeptiere die Datenschutzerklärung.“
- Keine Weitergabe der Daten an Dritte
- Keine Speicherung sensibler Daten ohne Einwilligung
- Hinweis: „Keine rechtsverbindliche Rentenberechnung. Nur zur Orientierung.“

## Erfolgskriterien

| KPI | Ziel Woche 2 | Ziel Woche 4 |
|-----|--------------|--------------|
| Landing-Page-Besucher | 200 | 500 |
| Rechner-Nutzungen | 100 | 300 |
| Leads (E-Mail) | 50 | 100 |
| Conversion LP → Lead | > 20 % | > 25 % |
| E-Mail-Bestätigungsrate | > 70 % | > 80 % |

## Nächster Schritt

Den Rechner als erste Web-App in einer Landing Page live stellen und mit der 5-teiligen E-Mail-Sequenz verknüpfen.
