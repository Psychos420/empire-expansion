# Wireframe: VermoegenPlaner — Grober Feature-Flow

## Grundprinzip

Die App ist in **drei Ebenen** aufgebaut:
1. **Erkennen** (Wo stehe ich?)
2. **Planen** (Was muss ich tun?)
3. **Umsetzen** (Wie komme ich voran?)

Jeder Screen hat maximal ein primäres Ziel. Keine überladenen Dashboards.

---

## 1. Onboarding-Flow (erster App-Start)

### Screen 1: Willkommen
- Logo + App-Name „VermoegenPlaner“
- Headline: „Ihr Finanz-Navigator für Berufstätige 35+“
- Subheadline: „In 3 Schritten zu Ihrem persönlichen Finanzplan.“
- CTA: „Plan starten“
- Sekundärlink: „Ich habe bereits ein Konto“

### Screen 2: Altersgruppe
- Frage: „In welchem Lebensabschnitt befinden Sie sich?“
- Optionen: 30–39 / 40–49 / 50–59 / 60+
- Hinweis: Daten bleiben lokal/DSGVO-konform

### Screen 3: Haupt-Thema wählen
- Frage: „Was beschäftigt Sie finanziell am meisten?“
- Optionen:
  - Rente / Rentenlücke
  - Vermögensaufbau
  - Steuern sparen
  - PKV / Versicherungen
  - Notgroschen / Sicherheit
- Mehrfachauswahl möglich

### Screen 4: Ziel definieren
- Frage: „Was möchten Sie in den nächsten 12 Monaten erreichen?“
- Beispiele:
  - „Ich will wissen, wie viel Rente ich bekomme.“
  - „Ich will einen ETF-Sparplan starten.“
  - „Ich will meine Versicherungen checken.“
- CTA: „Meinen Plan erstellen“

### Screen 5: Persönliches Dashboard (Ergebnis)
- Individueller Begrüßungstext
- Vorgeschlagener erster Schritt
- CTA: „Rentenlücke berechnen“ oder „Vermögens-Score starten“

---

## 2. Hauptnavigation (Bottom Tab Bar)

| Tab | Icon | Funktion |
|-----|------|----------|
| **Home** | Haus | Dashboard mit nächsten Schritten und Fortschritt |
| **Rechner** | Taschenrechner | Rentenlücke, Vermögens-Score, weitere Rechner |
| **Roadmap** | Karte | Persönliche Checklisten und Meilensteine |
| **Wissen** | Buch | Artikel, Guides, FAQ |
| **Profil** | Person | Einstellungen, Premium, Kontakt |

---

## 3. Home-Screen

### Oben
- Begrüßung: „Guten Morgen, [Vorname]“
- Aktueller Vermögens-Score (kleine Kachel)
- Fortschrittsbalken der Roadmap

### Mitte: „Ihr nächster Schritt“
- Eine prominente Karte mit dem empfohlenen nächsten To-Do
- Beispiel: „Berechnen Sie Ihre Rentenlücke – dauert 2 Minuten.“
- CTA: „Jetzt starten“

### Unten: Überblick
- Letzte Aktivitäten
- Gespeicherte Ergebnisse
- Kurzer Tipp des Tages

---

## 4. Rechner-Bereich

### Übersicht
- Liste verfügbarer Rechner
- Lock-Symbol bei Premium-Rechnern (mit Vorschau)

### Rentenlücke-Rechner
1. Eingabe-Screen
   - Geburtsjahr
   - Bruttoeinkommen/Jahr
   - Bereits erworbene Rentenjahre
   - Gewünschtes Renteneintrittsalter
   - Geschlecht (optional, für Rentenformel)
2. Berechnen-Button
3. Ergebnis-Screen
   - Geschätzte monatliche Netto-Rente
   - Empfohlene monatliche Zusatzsparrate
   - Balkendiagramm: Soll vs. Ist
   - CTA: „In Roadmap speichern“ / „Als PDF teilen“

### Vermögens-Score
1. Quiz-Screen (10 Fragen, eine pro Seite)
   - Einkommen, Rücklagen, Schulden, Absicherung, Anlageverhalten
2. Ergebnis-Screen
   - Score 0–100
   - Kategorie: „Aufholbedarf“, „Solide“, „Aufgestellt“
   - Drei konkrete Handlungsempfehlungen
   - CTA: „Roadmap erstellen“

---

## 5. Roadmap-Bereich

### Übersicht
- Meilensteine als vertikale Timeline
- Farbcodierung:
  - Grau: Noch nicht begonnen
  - Gelb: In Arbeit
  - Grün: Abgeschlossen

### Meilensteine (Beispiele)
1. **Notgroschen aufbauen**
   - Ziel: 3 Nettogehälter
   - Checkliste: Konto eröffnen, Dauerauftrag einrichten, Ziel erreichen
2. **Rentenlücke schließen**
   - Rechner nutzen, Sparrate ermitteln, ETF-Sparplan prüfen
3. **PKV prüfen**
   - Checkliste: Versicherungsunterlagen sichten, Vergleichsrechner nutzen
4. **Steuern optimieren**
   - Werbungskosten, Sonderausgaben, Riester/Betriebsrente prüfen
5. **Vermögensaufbau starten**
   - ETF-Sparplan, Depotwahl, Anlagestrategie

### Checklisten-Detail-Screen
- Titel des Meilensteins
- Fortschrittsbalken
- Aufgaben mit Checkboxen
- Info-Icon mit kurzer Erklärung pro Aufgabe
- CTA: „Nächsten Schritt starten“

---

## 6. Wissens-Bereich

### Übersicht
- Kategorien:
  - Rente
  - Vermögensaufbau
  - Steuern
  - PKV & Versicherungen
  - Notgroschen & Sicherheit
- Suchleiste oben

### Artikel-Detail
- Titel
- Lesezeit
- Text mit Zwischenüberschriften
- „Nicht als Anlageberatung“-Disclaimer
- Verwandte Checklisten / Rechner
- Teilen-Button

---

## 7. Profil-Bereich

### Oben
- Name, E-Mail, Mitglied seit
- Aktueller Plan: Free / Premium / Premium Plus

### Menüpunkte
- Abonnement verwalten
- Benachrichtigungen einstellen
- Gespeicherte Ergebnisse
- FAQ & Support
- Datenschutz & Impressum
- Abmelden

### Premium-Promo (für Free-Nutzer)
- Karte mit Vorteilen
- CTA: „7 Tage Premium testen“

---

## 8. Premium-Paywall

### Auslöser
- Nach 3 Nutzungen eines Premium-Rechners
- Beim Versuch, eine gesperrte Checkliste zu öffnen
- Nach Ablauf der 7-Tage-Testphase

### Screen
- Headline: „Schalten Sie Ihren vollen Finanzplan frei“
- Preise:
  - 12,99 €/Monat
  - 99,99 €/Jahr (Empfohlen – 36 % sparen)
- Feature-Liste:
  - Alle Rechner
  - Unbegrenzte Checklisten
  - PDF-Reports
  - Monatliche Finanz-Checkups
- CTA: „7 Tage kostenlos testen“
- Hinweis: Jederzeit kündbar

---

## 9. Push-Benachrichtigungen & Reminder

| Trigger | Nachricht |
|---------|-----------|
| 3 Tage nach Registrierung ohne Berechnung | „Haben Sie schon Ihre Rentenlücke berechnet? Dauert 2 Minuten.“ |
| Wöchentlich | „Ihr Finanz-Tipp der Woche: [Titel]“ |
| Roadmap-Meilenstein fällig | „Sie sind einen Schritt von Ihrem Notgroschen-Ziel entfernt.“ |
| Trial endet in 24h | „Ihre Premium-Testphase endet morgen – sichern Sie sich den Jahresplan.“ |
| Inaktivität 14 Tage | „Ihr Finanzplan wartet auf Sie. Hier geht's weiter.“ |

---

## 10. Web-App-Variante (Lead-Magnet)

### Rentenlücke-Rechner als Web-App
- Single-Page-Design
- Nur Rentenlücke-Rechner + Warteliste-CTA
- Keine Bottom Navigation
- Ergebnis-Seite mit PDF-Download und Warteliste-Formular

---

## Design-Notizen

- **Farben**: Dunkelblau (#1A2B4A), Weiß, Hellgrau, Akzent Grün (#2ECC71) oder Gold (#D4AF37)
- **Typografie**: Große Headlines, ausreichender Kontrast, keine Schriftgröße unter 16 px für Eingaben
- **Barrierefreiheit**: Klare Labels, ausreichende Abstände, hoher Kontrast
- **Mobile-First**: Alle Screens zuerst für 375 px Breite entworfen
- **Loading States**: Einfache Spinner, keine langen Wartezeiten

---

## Nicht im MVP

- Bank-API-Integration
- Community-Forum
- Live-Chat-Support
- B2B-Admin-Panel
- Mehrwährungs-Support (zunächst nur EUR/DE)
