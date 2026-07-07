# Automation-Orchestration — Vernetzung der Bereiche über n8n/Make

Dieses Dokument beschreibt, wie Workflows zwischen den 14 Expansionsbereichen vernetzt werden. Ziel ist ein einheitliches, skalierbares Automation-System, bei dem Leads automatisch getaggt, segmentiert und in passende Sequenzen geschoben werden.

---

## Architektur-Prinzip

```
                    ┌─────────────────┐
                    │  ZENTRALER      │
     ALLE LEADS ───►│  LEAD-ROUTER    │
                    │    (n8n)        │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
   [Brevo-Listen]      [GoHighLevel]       [Google Sheets]
   [Tags]              [Pipelines]         [Reporting]
   [Sequenzen]         [Termine]           [Cross-Sell-Logik]
```

**Regel:** Jeder Lead landet zuerst im zentralen Router. Der Router entscheidet anhand von Quelle, Interesse und Verhalten, was passiert.

---

## Zentrale Workflows

### Workflow 1: Lead-Eingang (Universal Webhook)

**Trigger:**
- Landing-Page-Formular
- Popup
- Quiz
- App-Download
- WhatsApp/SMS-Eingang
- Kauf bei Stripe

**Aktionen:**
1. Lead-Daten normalisieren (E-Mail, Telefon, Name, Quelle, Bereich, Interesse)
2. Duplikate prüfen
3. Lead in zentrale Google Sheet-Log schreiben
4. Tagging und Segmentierung
5. Weiterleitung an Brevo + GoHighLevel
6. Trigger der richtigen Willkommens-Sequenz

**n8n-Nodes:**
- Webhook
- Set / Function (Daten-Mapping)
- Google Sheets
- Brevo (Add/Update Contact)
- GoHighLevel (Create/Update Contact)
- n8n Split In Batches (optional)

---

### Workflow 2: Bereichs-Zuweisung & Tagging

**Logik:**
Jeder Lead bekommt automatisch Tags:

| Tag | Bedeutung |
|---|---|
| `source:{bereich}` | Ursprünglicher Bereich, z. B. `source:03-pdfs` |
| `interest:{thema}` | Thematisches Interesse, z. B. `interest:finanzen` |
| `leadmagnet:{name}` | Heruntergeladener Lead-Magnet |
| `buyer:{status}` | `buyer:no`, `buyer:lowticket`, `buyer:highticket` |
| `engagement:{level}` | `engagement:hot`, `engagement:warm`, `engagement:cold` |
| `crosssell:{bereich}` | Bereits angebotene Cross-Sell-Bereiche |

**Beispiel:**
Ein Lead aus dem PDF-Bereich „Rente mit 65 sicher" bekommt:
- `source:03-pdfs`
- `interest:finanzen`
- `interest:rente`
- `leadmagnet:rente-checkliste`
- `buyer:no`
- `engagement:warm`

---

### Workflow 3: Cross-Sell-Orchestrierung

**Ziel:** Leads aus einem Bereich automatisch für passende andere Bereiche qualifizieren.

**Regeln:**

| Wenn Lead hat Tag... | Dann Cross-Sell in Bereich... | Nach Verzögerung |
|---|---|---|
| `interest:finanzen` | `09-finanzielle-freiheit`, `05-lead-generation-pkv`, `11-immobilien` | 7 Tage |
| `interest:gesundheit` | `10-gesundheit-praevention`, `05-lead-generation-pkv` | 7 Tage |
| `interest:business` | `12-selbststaendigkeit`, `04-ki-integrationen`, `07-marketing-agency` | 7 Tage |
| `interest:lifestyle` | `13-reisen-lifestyle`, `09-finanzielle-freiheit` | 10 Tage |
| `interest:eco` | `14-nachhaltigkeit-eco`, `10-gesundheit-praevention` | 10 Tage |
| `buyer:lowticket` | Bereiche mit nächst höherem Preisniveau | 14 Tage |

**Ablauf:**
1. n8n prüft täglich alle Leads auf Cross-Sell-Potenzial.
2. Passende Cross-Sell-E-Mail wird ausgewählt.
3. Lead wird in Ziel-Bereichs-Liste bei Brevo hinzugefügt.
4. Cross-Sell-Sequenz startet.
5. Tag `crosssell:{bereich}` wird gesetzt, um Doppelungen zu vermeiden.

---

### Workflow 4: Käufer-Automation

**Trigger:** Stripe-Kauf

**Aktionen:**
1. Käufer-Tag in Brevo/GoHighLevel setzen (`buyer:lowticket` oder `buyer:highticket`)
2. Kauf in Google Sheet loggen
3. Zugangsdaten/Download per E-Mail senden
4. Upsell-Sequenz starten
5. Bei High-Ticket-Kauf: Termin-Einladung senden
6. In Cross-Sell-Pool für komplementäre Bereiche aufnehmen

---

### Workflow 5: Termin-Automation

**Trigger:** Terminbuchung über GoHighLevel / Calendly

**Aktionen:**
1. Terminbestätigung per E-Mail + SMS
2. Erinnerung 24 Stunden vorher (E-Mail + SMS)
3. Erinnerung 1 Stunde vorher (SMS)
4. Nach dem Termin: Follow-up-E-Mail mit nächstem Schritt
5. Kein-Show: Reaktivierung nach 3 Tagen
6. Verkaufsstatus in CRM aktualisieren

---

### Workflow 6: Re-Engagement & List-Hygiene

**Trigger:** Zeitgesteuert (wöchentlich)

**Aktionen:**
1. Inaktive Leads identifizieren (keine Öffnung in 30/60/90 Tagen)
2. Re-Engagement-Kampagne starten
3. Wer nicht reagiert: Tag `cold` setzen, Versandfrequenz reduzieren
4. Nach 90 Tagen ohne Reaktion: Aus Liste entfernen oder in Winback-Pool

---

### Workflow 7: Reporting & Alerts

**Trigger:** Täglich / Wöchentlich

**Aktionen:**
1. KPIs aus Brevo, Stripe, GoHighLevel, GA4 aggregieren
2. In Google Sheets / Looker Studio schreiben
3. Wenn KPI außerhalb des Zielkorridors: Alert an Bereichs-Owner
4. Wöchentlicher Summary-Bericht an Lead

---

## Beispiel: Lead aus PDF-Bereich wird in Affiliate-Sequenz geschoben

**Szenario:**
Ein Besucher lädt im Bereich `03-pdfs-guides` die „Rente mit 65 sicher" Checkliste herunter.

**Ablauf:**

1. **Opt-in:**
   - E-Mail wird in Formular auf Carrd-Landing-Page eingegeben.
   - Webhook an n8n wird ausgelöst.

2. **n8n Router:**
   - Empfängt Lead: `email=test@example.com`, `source=03-pdfs`, `leadmagnet=rente-checkliste`
   - Setzt Tags: `source:03-pdfs`, `interest:finanzen`, `interest:rente`, `leadmagnet:rente-checkliste`, `buyer:no`, `engagement:warm`
   - Schreibt Lead in zentrales Log
   - Fügt Lead zu Brevo-Liste `03-pdfs` hinzu
   - Startet Willkommens-Sequenz `WELCOME-PDFS`

3. **Cross-Sell-Prüfung (nach 7 Tagen):**
   - n8n erkennt Tags `interest:finanzen` und `interest:rente`
   - Prüft, ob `crosssell:09-finanzielle-freiheit` bereits gesetzt
   - Falls nein: Fügt Lead zu Brevo-Liste `09-finanzielle-freiheit` hinzu
   - Startet Sequenz `CROSS-SELL-09-RENTEN-LEADS`
   - Setzt Tag `crosssell:09-finanzielle-freiheit`

4. **Parallel: Affiliate-Sequenz:**
   - Gleiche Prüfung für `interest:finanzen` → Liste `01-affiliate-marketing`
   - Startet Sequenz `CROSS-SELL-01-FINANZ-LEADS`
   - Enthält Affiliate-Empfehlungen zu ETF-Sparplänen, Zahnzusatz, PKV

5. **Ergebnis:**
   - Ein Lead aus dem PDF-Bereich wird gleichzeitig für Finanzielle Freiheit und Affiliate Marketing qualifiziert.
   - Keine manuelle Arbeit nötig.

---

## Tool-Integrationen in n8n

| Tool | Integration | Nutzung |
|---|---|---|
| **Brevo** | Offizieller n8n-Node | Kontakte, Listen, Sequenzen, Campaigns |
| **GoHighLevel** | Community-Node oder HTTP Request | CRM, Pipelines, Termine, SMS |
| **Stripe** | Offizieller n8n-Node | Zahlungen, Käufer, Subscriptions |
| **Google Sheets** | Offizieller n8n-Node | Logs, Reporting, Lookup-Tabellen |
| **Meta Conversions API** | HTTP Request | Conversion-Daten zurückspielen |
| **Slack / Telegram** | Offizieller n8n-Node | Alerts und Benachrichtigungen |
| **OpenAI / Kimi / Claude** | HTTP Request oder API-Node | Personalisierung, Lead-Scoring, Content |

---

## n8n Workflow-Checkliste

- [ ] Zentralen Webhook pro Bereich eingerichtet
- [ ] Datenfelder standardisiert (E-Mail, Name, Telefon, Quelle, Bereich, Interesse)
- [ ] Duplikatsprüfung aktiviert
- [ ] Tags konsistent vergeben
- [ ] Brevo-Listen pro Bereich angelegt
- [ ] GoHighLevel-Pipelines pro Bereich angelegt
- [ ] Cross-Sell-Regeln definiert und getestet
- [ ] Fehler-Handling mit Retry-Logik
- [ ] Logging in Google Sheets
- [ ] Alerting bei Workflow-Fehlern

---

## Skalierungsregeln

1. **Neuer Bereich hinzufügen:**
   - Neue Brevo-Liste anlegen
   - Neue GoHighLevel-Pipeline anlegen
   - Webhook im Router ergänzen
   - Tags dokumentieren
   - Cross-Sell-Regeln für den neuen Bereich definieren

2. **Neuer Cross-Sell-Pfad:**
   - Interessen-Tag definieren
   - Zielbereich und Sequenz festlegen
   - Verzögerung festlegen
   - Workflow testen

3. **Neues Tool hinzufügen:**
   - Prüfen, ob n8n-Node verfügbar
   - Credentials sicher hinterlegen
   - Test-Workflow bauen
   - Bestehende Workflows nur minimal anpassen

---

## Sicherheit & Compliance

- Keine sensiblen Daten in Logs speichern.
- API-Keys und Credentials nur in n8n-Credential-Vault.
- DSGVO: Double-Opt-In für alle E-Mail-Listen, jederzeit Abmeldung möglich.
- Bei Finanz/Versicherung: Keine Beratung automatisch senden, nur Lead-Vermittlung.
- Workflow-Änderungen dokumentieren.

---

## Nächste Schritte

1. n8n-Instanz aufsetzen (Cloud oder self-hosted).
2. Zentralen Lead-Eingangs-Workflow bauen.
3. Brevo- und GoHighLevel-Integration testen.
4. Erste Bereichs-Workflows für Phase 1 (Affiliate, PDFs, PKV) aktivieren.
5. Cross-Sell-Regeln für die ersten 3 Bereiche implementieren.
