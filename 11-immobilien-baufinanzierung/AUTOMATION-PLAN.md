# Automation-Plan: Immobilien & Baufinanzierung

## Ziel der Automation
80 % des Front-Office-Prozesses automatisieren, ohne die persönliche Beratungsqualität zu reduzieren. Der Mensch bleibt dort, wo Vertrauen, Haftung und Komplexität es erfordern.

---

## Tool-Stack

### Marketing & Lead-Generierung
| Aufgabe | Tool-Empfehlung | Alternative |
|---------|----------------|-------------|
| Landingpage | Webflow / Carrd / WordPress | Framer |
| Formulare & Quiz | Typeform / Tally | Jotform |
| E-Mail-Marketing | Kit (ConvertKit) | ActiveCampaign, Brevo |
| CRM | HubSpot (kostenlos) | Pipedrive, Airtable |
| Ads | Google Ads, Meta Ads | LinkedIn Ads |
| Terminbuchung | Calendly / TidyCal | SavvyCal |

### KI & Dokumentenverarbeitung
| Aufgabe | Tool-Empfehlung | Alternative |
|---------|----------------|-------------|
| KI-Text & E-Mails | OpenAI GPT-4 / Claude | Google Gemini |
| Dokumenten-Upload & Analyse | Custom GPT / Make / n8n + OCR | Azure Document Intelligence |
| Chatbot / FAQ-Bot | Chatbase / Voiceflow | Intercom Fin |
| Lead-Scoring | HubSpot + Make/n8n | ActiveCampaign |

### Vertrieb & Beratung
| Aufgabe | Tool-Empfehlung | Alternative |
|---------|----------------|-------------|
| Videocalls | Zoom / Google Meet | Microsoft Teams |
| Vertragsmanagement | HelloSign / DocuSign | Adobe Sign |
| Rechnung & Buchhaltung | Lexoffice / FastBill | SevDesk |
| Wissensspeicher | Notion / Obsidian | Confluence |

### Affiliate & Partner
| Aufgabe | Tool-Empfehlung | Alternative |
|---------|----------------|-------------|
| Affiliate-Tracking | Rewardful / FirstPromoter | Tapfiliate |
| Partnerbank-Vergleich | Interner Rechner / API | Manuelle Pflege |

---

## Kern-Workflows

### Workflow 1: Lead-Erfassung & Qualifizierung
1. Nutzer klickt auf Anzeige oder Content-Link.
2. Landingpage zeigt Lead-Magnet „Immobilien-Readiness-Score".
3. Formular wird ausgefüllt.
4. E-Mail-Adresse landet in Kit + CRM.
5. KI bereitet automatischen Score-Ergebnis-Report.
6. Lead wird getaggt (z.B. „selbstständig", „investor", „erstkäufer").
7. Nurture-Serie startet.

**Automation-Tool**: Typeform → Kit → HubSpot → Make/n8n → GPT-4.

### Workflow 2: Dokumenten-Vorbereitung vor Beratung
1. Kunde lädt Gehaltsabrechnungen, Steuerbescheid, Grundbuchauszug hoch.
2. OCR extrahiert relevante Daten.
3. KI erstellt Finanzierungsübersicht (Einkommen, Eigenkapital, Belastbarkeit).
4. Berater erhält vorstrukturierte Datei vor dem Termin.
5. Berater validiert und ergänzt.

**Automation-Tool**: Upload-Formular → Google Drive / Dropbox → n8n → Azure OCR / GPT-4 → Notion/CRM.

### Workflow 3: Termin-Nachbereitung & Angebot
1. Nach dem Gespräch trägt Berater Eckdaten ins CRM ein.
2. KI generiert individuelles Angebotsschreiben / Finanzierungsstrategie-PDF.
3. PDF wird per E-Mail versandt.
4. Follow-up-Sequenz startet (z.B. nach 3, 7, 14 Tagen).

**Automation-Tool**: HubSpot → Make → GPT-4 → HelloSign / E-Mail.

### Workflow 4: Anschlussfinanzierungs-Erinnerung
1. Kunde mit abgeschlossener Finanzierung wird im CRM erfasst.
2. Ablaufdatum der Zinsbindung wird gespeichert.
3. Automatische Erinnerung 12, 9, 6 Monate vor Ablauf.
4. Lead wird erneut in Funnel geschickt.

**Automation-Tool**: HubSpot Workflows / Kit Automation.

### Workflow 5: Content-Wiederverwertung
1. Monatliches Webinar/Video wird aufgezeichnet.
2. KI erstellt daraus:
   - 5 LinkedIn-Posts
   - 3 E-Mail-Auszüge
   - 1 Blogartikel
   - 5 YouTube Shorts-Scripts
3. Redakteur prüft und veröffentlicht.

**Automation-Tool**: Video-Upload → Whisper-Transkription → GPT-4 → Notion → Buffer/Hypefury.

---

## Limits der Automation

| Bereich | Automation | Mensch |
|---------|-----------|--------|
| Lead-Generierung | ✅ Hoch | Strategie & Kreatives |
| Erst-Qualifizierung | ✅ Hoch | Ausnahmen & Komplexfälle |
| Dokumenten-Check | ✅ Vorbereitung | Validierung & Haftung |
| Finanzierungsberatung | ⚠️ Unterstützung | Beratung durch zugelassenen Vermittler |
| Anlageberatung | ❌ Nicht erlaubt | Nur lizenzierter Anlageberater |
| Vertragsabschluss | ⚠️ Dokumente | Unterschrift & Berater-Freigabe |
| Beschwerden/Rückfragen | ⚠️ Erste Ebene | Eskalation an Mensch |

## Regulatorische Automation-Grenzen
- **Keine automatisierte Kreditvergabe** ohne menschliche Prüfung.
- **Keine automatisierte Anlageempfehlung** für Investment-Immobilien.
- **DSGVO-konforme Datenspeicherung** aller Lead- und Kundendaten.
- **Protokollierung** automatisierter Empfehlungen für Compliance.

---

## Kosten-Schätzung Tool-Stack (monatlich)

| Tool | Kosten/Monat |
|------|--------------|
| Webflow / Landingpage | 20–50 € |
| Typeform / Tally | 0–30 € |
| Kit / ActiveCampaign | 30–100 € |
| HubSpot CRM | 0–50 € |
| Calendly | 0–15 € |
| Make / n8n | 0–30 € |
| OpenAI API | 20–100 € |
| Zoom | 0–15 € |
| **Gesamt** | **ca. 100–400 €/Monat** |

---

*Nächster Schritt: n8n- oder Make-Account einrichten und ersten Workflow „Readiness-Score → E-Mail" bauen.*
