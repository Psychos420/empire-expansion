# Qualifikations-Formular: PKV-Leads für Beamte

## Zweck
Dieses Formular dient der Lead-Qualifizierung nach dem Download des Lead-Magnets. Es erfasst die wichtigsten Datenpunkte, um Leads in Hot/Warm/Cold zu segmentieren und den passenden nächsten Schritt auszulösen.

---

## Formular-Logik

| Schritt | Inhalt | Bedingung |
|---------|--------|-----------|
| 1 | Basisdaten + Download | Immer |
| 2 | Erweiterte Qualifizierung | Optional, nach Download angeboten |
| 3 | Terminbuchung | Für Hot/Warm Leads |

---

## Schritt 1: Basisdaten (Pflicht)

### Persönliche Daten

| Feld | Typ | Pflicht | Verwendung |
|------|-----|---------|------------|
| Vorname | Text | Ja | Personalisierung |
| Nachname | Text | Ja | Lead-Profil, Makler-Übergabe |
| E-Mail-Adresse | E-Mail | Ja | Sequenz, Download |
| Telefonnummer | Tel | Nein | Terminvereinbarung, SMS |

### Berufliche Daten

| Feld | Typ | Pflicht | Verwendung |
|------|-----|---------|------------|
| Alter | Zahl | Ja | Lead-Scoring, Tarif-Einschätzung |
| Berufsgruppe | Dropdown | Ja | Segmentierung |
| Bundesland | Dropdown | Nein | Beihilfesatz ermitteln |
| Beamtenstatus | Dropdown | Nein | Beamter auf Lebenszeit / Probezeit / Anwärter |

**Berufsgruppe-Optionen:**
- Beamter (höherer Dienst)
- Beamter (gehobener Dienst)
- Beamter (einfacher Dienst)
- Beamtenanwärter
- Selbstständig
- Angestellt (JAEG überschritten)
- Angestellt (unter JAEG)
- Rentner / Pensionär
- Sonstiges

**Beamtenstatus-Optionen:**
- Beamter auf Lebenszeit
- Beamter auf Probe
- Beamtenanwärter
- Pensionierter Beamter
- Nicht beamtet

---

## Schritt 2: Erweiterte Qualifizierung (optional)

### Aktuelle Versicherungssituation

| Feld | Typ | Optionen |
|------|-----|----------|
| Aktuelle Krankenversicherung | Dropdown | Gesetzlich versichert (GKV), Privat versichert (PKV), Beihilfe + PKV, Beihilfe + GKV, Sonstiges |
| Aktueller PKV-Anbieter (falls vorhanden) | Text | Freitext |
| Aktueller Monatsbeitrag (ca.) | Zahl | In Euro |
| Zufriedenheit mit aktuellem Tarif | Radio | Sehr zufrieden / Zufrieden / Neutral / Unzufrieden / Sehr unzufrieden |

### Einkommen & Beihilfe

| Feld | Typ | Hinweis |
|------|-----|---------|
| Bruttojahreseinkommen (ca.) | Dropdown | <50k / 50k–70k / 70k–100k / 100k–150k / >150k |
| Beihilfesatz (ca.) | Dropdown | 50% / 60% / 70% / 80% / Unsicher |
| Familienstand | Dropdown | Ledig / Verheiratet / Verpartnert / Geschieden |
| Kinder im Haushalt | Zahl | 0 / 1 / 2 / 3+ |
| Kinderwunsch / Familienplanung | Radio | Ja / Nein / Unsicher |

### Interesse & Timing

| Feld | Typ | Optionen |
|------|-----|----------|
| Thema des Interesses | Multi-Select | Erstwechsel in PKV, Tarifoptimierung, Restkostenversicherung prüfen, Zahnzusatz, Krankenhauszusatz, Familienmitversicherung |
| Geplanter Entscheidungszeitpunkt | Dropdown | Sofort / Innerhalb 1 Monat / Innerhalb 3 Monate / Innerhalb 12 Monate / Noch unklar |
| Bevorzugte Kontaktart | Radio | E-Mail / Telefon / Videocall |
| Wunschtermin | Date-Picker | Optional |

---

## Lead-Scoring-Regeln

| Kriterium | Punkte |
|-----------|--------|
| Alter 35–55 | +10 |
| Alter 30–34 oder 56–60 | +5 |
| Beamter (höherer/gehobener Dienst) | +20 |
| Beamtenanwärter | +10 |
| Selbstständig | +10 |
| Angestellt oberhalb JAEG | +10 |
| Einkommen >70k €/Jahr | +15 |
| Einkommen 50k–70k €/Jahr | +5 |
| Interesse an Vollversicherung | +15 |
| Interesse an Zusatzversicherung | +5 |
| Telefonnummer hinterlegt | +10 |
| Entscheidung „Sofort" oder „Innerhalb 1 Monat" | +15 |
| Entscheidung „Innerhalb 3 Monate" | +5 |
| Öffnet Willkommens-E-Mail | +5 |
| Klickt in E-Mail auf Termin-CTA | +10 |

---

## Lead-Segmente

| Segment | Score | Nächster Schritt |
|---------|-------|------------------|
| **Hot Lead** | ≥70 | Sofortiger Anruf / Terminbuchung innerhalb 24h |
| **Warm Lead** | 40–69 | E-Mail-Nurturing + SMS-Reminder, Termin-CTA nach 3 Tagen |
| **Cold Lead** | <40 | Newsletter-Liste, langfristiges Nurturing, saisonale Kampagnen |

---

## Compliance & Datenschutz

### Pflicht-Checkboxen

- [ ] **Datenschutz:** Ich akzeptiere die Datenschutzerklärung und stimme der Verarbeitung meiner Daten zum Zweck der Zusendung der Checkliste und der Kontaktaufnahme zu.
- [ ] **Download-Consent:** Ich möchte die kostenlose Checkliste per E-Mail erhalten.

### Optionale Checkboxen

- [ ] **Telefonkontakt:** Ich bin damit einverstanden, dass mich ein lizenzierter Versicherungsmakler telefonisch kontaktieren darf.
- [ ] **Marketing:** Ich möchte zukünftig per E-Mail über PKV-Themen informiert werden (jederzeit abmeldbar).

### Hinweistexte

> **Wichtig:** Dieses Formular dient ausschließlich der Lead-Qualifizierung. Es ersetzt keine medizinische, steuerliche oder versicherungsrechtliche Beratung. Eine individuelle Beratung erfolgt nur durch lizenzierte Versicherungsmakler oder Versicherungsberater.

---

## Makler-Übergabe-Briefing

Bei Übergabe eines Hot Leads an den lizenzierten Makler:

| Feld | Wert |
|------|------|
| Name | [Vorname] [Nachname] |
| Kontakt | [E-Mail], [Telefon] |
| Alter | [Alter] |
| Beruf | [Berufsgruppe], [Beamtenstatus] |
| Bundesland | [Bundesland] |
| Aktuelle KV | [Aktuelle Krankenversicherung] |
| Beihilfesatz | [Beihilfesatz] |
| Interesse | [Thema des Interesses] |
| Timing | [Entscheidungszeitpunkt] |
| Lead-Score | [Score] |
| Quelle | [Landing Page / Meta Ad / Google Ad] |

---

## Tool-Empfehlungen

| Zweck | Tool |
|-------|------|
| Formular & CRM | GoHighLevel |
| Erweiterte Formulare | Typeform, Jotform |
| Terminbuchung | Calendly, GoHighLevel Calendar |
| Lead-Scoring | GoHighLevel Workflows, n8n |
| Datenschutz | DSGVO-Texte juristisch prüfen lassen |

---

## A/B-Test-Ideen

| Element | Variante A | Variante B |
|---------|------------|------------|
| Formularlänge | 4 Pflichtfelder | 8 Pflichtfelder |
| Telefonfeld | Optional | Pflicht |
| Einkommensfrage | Offen (Dropdown) | Versteckt im zweiten Schritt |
| CTA | „Checkliste laden" | „Kostenlosen PKV-Check starten" |

---

*Stand: Juli 2026 | Qualifikations-Formular für Empire-Expansion PKV-Lead-Generation.*
