# Automatisierungs-Plan: KI-Integrationen für Entscheider 35+

## Prinzip

Wir automatisieren so viel wie möglich im Marketing, Vertrieb und Betrieb — behalten aber menschliche Qualitätskontrolle bei strategischen, datenschutzrelevanten und kundenkritischen Punkten.

**Regel:**  
Automatisieren, was wiederholt, regelbasiert oder skalierbar ist.  
Menschlich bleiben, was Vertrauen, Kreativität und komplexe Entscheidungen erfordert.

---

## 1. Konkreter Tool-Stack

### Kategorie: KI-Modelle & Agenten

| Tool | Einsatz | Kosten (geschätzt) |
|------|---------|---------------------|
| **Kimi** | Content-Erstellung, Ideen, Dokumentation, E-Mail-Entwürfe | Teil des Ökosystems |
| **Claude** | Längere Texte, Analysen, komplexe Prompts | Ab ~20 $/Monat |
| **OpenAI API** | GPT-4o für KI-Agenten, Chatbots, Automatisierungen | Pay-per-Use |
| **Anthropic API** | Claude für Kundenkommunikation, Qualitätssicherung | Pay-per-Use |
| **Ollama / lokale LLMs** | Datenschutzkritische Kunden, On-Premise-Lösungen | Kostenlos – Hosting |

### Kategorie: Workflow-Automatisierung

| Tool | Einsatz | Kosten (geschätzt) |
|------|---------|---------------------|
| **n8n** | Selbst gehostete Workflows, komplexe KI-Agenten, Datenanbindung | Kostenlos self-hosted / Cloud ab 24 €/Monat |
| **Make** | Schnelle, visuelle Workflows, einfache Integrationen | Ab ~16 $/Monat |
| **Zapier** | Einfache Verbindungen, großes App-Ökosystem | Ab ~20 $/Monat |

**Empfehlung:**  
- **n8n** als Hauptwerkzeug für KI-Agenten und datenschutzsensible Kunden (self-hosted)
- **Make** als sekundäres Tool für schnelle, weniger kritische Workflows
- **Zapier** nur für sehr einfache, standardisierte Verbindungen

### Kategorie: Marketing & Lead-Generierung

| Tool | Einsatz | Kosten (geschätzt) |
|------|---------|---------------------|
| **Brevo** | E-Mail-Marketing, Automatisierungen, Newsletter | Ab 0–25 €/Monat |
| **ActiveCampaign** | Erweitertes CRM + E-Mail-Automatisierung | Ab 29 $/Monat |
| **Mailchimp** | Alternative für einfache Newsletter | Ab 13 $/Monat |
| **Calendly / Cal.com** | Terminbuchung | Calendly ab 10 $/Monat / Cal.com Open Source |
| **Typeform / Tally** | Lead-Magnet-Formulare, Umfragen | Typeform ab 25 €/Monat, Tally kostenlos |
| **HubSpot CRM** | Kostenloses CRM für Lead-Pipeline | Kostenlos |
| **Pipedrive** | Vertriebspipeline | Ab 15 €/Nutzer/Monat |

### Kategorie: Content & Design

| Tool | Einsatz | Kosten (geschätzt) |
|------|---------|---------------------|
| **Canva** | Grafiken, Social-Media-Posts, Präsentationen | Ab 0–15 €/Monat |
| **CapCut** | Video-Schnitt für Kurzvideos | Kostenlos |
| **Descript** | Podcast-/Video-Bearbeitung | Ab 12 $/Monat |
| **Notion** | Wissensmanagement, SOPs, Projektplanung | Ab 0–10 €/Monat |

### Kategorie: Kommunikation

| Tool | Einsatz | Kosten (geschätzt) |
|------|---------|---------------------|
| **WhatsApp Business API** | Automatisierte Kundenkommunikation | Pay-per-Use |
| **Twilio** | SMS, Telefonie-Integration | Pay-per-Use |
| **Slack** | Interne Kommunikation | Kostenlos |
| **Loom** | Video-Nachrichten für Kunden | Ab 0–15 $/Monat |

### Kategorie: Daten & Reporting

| Tool | Einsatz | Kosten (geschätzt) |
|------|---------|---------------------|
| **Google Looker Studio** | Dashboards, Reporting | Kostenlos |
| **Airtable** | Datenbanken, Projektmanagement | Ab 0–20 $/Monat |
| **Google Sheets** | Einfache Datenspeicherung, Listen | Kostenlos |
| **Supabase** | Datenbank für Kundenprojekte | Ab 0–25 $/Monat |

### Kategorie: Tracking & Analyse

| Tool | Einsatz | Kosten (geschätzt) |
|------|---------|---------------------|
| **Google Analytics 4** | Webseiten-Tracking | Kostenlos |
| **Google Tag Manager** | Tag-Verwaltung | Kostenlos |
| **Meta Pixel** | Facebook/Instagram-Tracking | Kostenlos |
| **LinkedIn Insight Tag** | LinkedIn-Tracking | Kostenlos |
| **Plausible / Fathom** | Datenschutzfreundliches Analytics | Ab 9 $/Monat |

---

## 2. Automatisierbare Workflows

### Workflow A: Lead-Generierung & Nurturing

```
Traffic (LinkedIn / Google / SEO)
    ↓
Landing Page (Typeform / Carrd)
    ↓
E-Mail in Brevo / ActiveCampaign
    ↓
Segmentierung nach Branche + Schmerzpunkt
    ↓
Automatisierte E-Mail-Sequenz (7–10 E-Mails)
    ↓
CTA: Termin buchen (Calendly)
    ↓
Reminder per E-Mail + WhatsApp
    ↓
CRM-Status aktualisieren (HubSpot / Pipedrive)
```

**Automatisierbarkeit:** 90 %  
**Menschlich:** Inhalt der E-Mail-Sequenz wird von Menschen erstellt und optimiert.

---

### Workflow B: Terminbuchung & Vorbereitung

```
Termin wird gebucht (Calendly)
    ↓
Bestätigungs-E-Mail + SMS/WhatsApp
    ↓
Vorab-Fragebogen wird versendet
    ↓
Antworten werden in CRM + Notion gespeichert
    ↓
Erinnerung 24h vorher
    ↓
Nach Termin: Follow-up-E-Mail mit Angebot
```

**Automatisierbarkeit:** 95 %  
**Menschlich:** Das eigentliche Gespräch.

---

### Workflow C: Content-Erstellung

```
Themenplanung (Notion / Airtable)
    ↓
KI erstellt Entwurf (Kimi / Claude)
    ↓
Menschliches Review + Anpassung
    ↓
KI erstellt Variationen (LinkedIn, Newsletter, Kurzvideo-Script)
    ↓
Design in Canva / Video in CapCut
    ↓
Scheduling (Buffer / Later / native Planung)
    ↓
Veröffentlichung
```

**Automatisierbarkeit:** 70 %  
**Menschlich:** Strategie, Review, finale Freigabe.

---

### Workflow D: Kunden-Onboarding

```
Vertrag + Zahlung bestätigt
    ↓
Willkommens-E-Mail mit Onboarding-Checkliste
    ↓
Kickoff-Termin automatisch gebucht
    ↓
Zugänge werden erstellt (n8n / Make)
    ↓
Prozessdokumentation wird angefordert
    ↓
Status-Updates per E-Mail an Kunden
    ↓
Go-Live-Reminder + Schulungstermin
```

**Automatisierbarkeit:** 80 %  
**Menschlich:** Kickoff-Call, technische Umsetzung, Schulung.

---

### Workflow E: KI-Agenten für Kundenkommunikation

```
Anfrage per E-Mail / WhatsApp / Webformular
    ↓
KI-Agent klassifiziert Anfrage (n8n + OpenAI / lokales LLM)
    ↓
Standardanfragen werden automatisch beantwortet
    ↓
Komplexe Anfragen werden an Menschen weitergeleitet
    ↓
Terminbuchung erfolgt automatisch
    ↓
Informationen werden in CRM aktualisiert
```

**Automatisierbarkeit:** 75–90 % (je nach Branche)  
**Menschlich:** Eskalationen, komplexe Beratung, Qualitätskontrolle.

---

### Workflow F: Reporting & KPI-Tracking

```
Datenquellen (CRM, Google Ads, LinkedIn, E-Mail-Tool)
    ↓
Daten werden per API abgeholt (n8n / Make)
    ↓
Daten in Google Sheets / Airtable / Supabase gespeichert
    ↓
Looker Studio Dashboard wird aktualisiert
    ↓
Wöchentlicher / monatlicher Report per E-Mail an Team + Kunden
```

**Automatisierbarkeit:** 95 %  
**Menschlich:** Interpretation der Daten, strategische Schlussfolgerungen.

---

### Workflow G: Rechnungsstellung & Buchhaltung

```
Monatlicher Abrechnungstag
    ↓
Rechnung automatisch erstellen (lexoffice / sevDesk / Fastbill)
    ↓
Rechnung per E-Mail versenden
    ↓
Zahlungserinnerung nach 14 Tagen
    ↓
Zahlungseingang prüfen
```

**Automatisierbarkeit:** 90 %  
**Menschlich:** Sonderfälle, Mahnungen, Vertragsanpassungen.

---

## 3. Was bleibt menschlich?

| Bereich | Warum menschlich? |
|---------|-------------------|
| **Verkaufsgespräche** | Vertrauensaufbau, Bedarfsanalyse, Einwände behandeln |
| **Strategieberatung** | Individuelle Geschäftslogik, komplexe Entscheidungen |
| **Technische Architektur** | Sicherheit, Skalierbarkeit, individuelle Kundenanforderungen |
| **Qualitätskontrolle KI-Ausgaben** | Halluzinationen vermeiden, Marke schützen |
| **Kundenbeziehung & Support** | Persönlicher Kontakt, Eskalationen, Vertrauen |
| **Content-Strategie & Positionierung** | Markenstimme, Innovation, Differenzierung |
| **Compliance & Datenschutz** | Rechtliche Verantwortung, Kundenberatung |
| **Kreative Konzeption** | Kampagnenideen, Storytelling, Design-Entscheidungen |

---

## 4. Technische Architektur-Empfehlung

### Für Standard-Kunden (Cloud-basiert)

```
Landing Page: Carrd / Webflow
E-Mail: Brevo
CRM: HubSpot (kostenlos)
Terminbuchung: Cal.com
Automatisierung: Make + n8n (Cloud)
KI: OpenAI API + Claude API
Reporting: Looker Studio
Dokumentation: Notion
```

### Für Datenschutz-kritische Kunden

```
Landing Page: Eigenes Hosting
E-Mail: Brevo mit EU-Servern oder selbst gehostet
CRM: HubSpot mit EU-Datenzentrum oder Pipedrive
Terminbuchung: Cal.com self-hosted
Automatisierung: n8n self-hosted
KI: Lokale Modelle (Ollama, Mistral, Llama) oder EU-APIs
Reporting: Looker Studio mit lokalen Datenquellen
Dokumentation: Notion oder selbst gehostetes Wiki
```

---

## 5. Skalierbarkeit & Wiederverwendbarkeit

### Wiederverwendbare Bausteine

| Baustein | Nutzen |
|----------|--------|
| **Template-Bibliothek für n8n-Workflows** | Schnellere Umsetzung, konsistente Qualität |
| **Prompt-Bibliothek** | Standardisierte KI-Ausgaben für wiederkehrende Aufgaben |
| **Lead-Magnet-Templates** | Neue Branchen schnell testen |
| **Landing-Page-Templates** | A/B-Tests und neue Kampagnen schnell aufsetzen |
| **Onboarding-Scripts** | Gleiche Qualität bei wachsender Kundenzahl |

### Skalierungshebel

1. **Produktisierung:** Wiederkehrende Workflows zu Standard-Paketen machen
2. **Template-Ansatz:** 80 % Standard, 20 % Individualisierung pro Kunde
3. **KI-gestützte Umsetzung:** Eigene Entwicklung mit KI beschleunigen
4. **Partnernetzwerk:** Freiberufler und White-Label-Partner für Spitzen
5. **Abo-Modelle:** Wiederkehrende Einnahsen reduzieren Akquisitionsdruck

---

## 6. Kostenübersicht Tool-Stack (geschätzt)

| Tool | Monatliche Kosten |
|------|-------------------|
| n8n Cloud / Self-Hosting | 0–50 € |
| Make | 0–50 € |
| Brevo / ActiveCampaign | 0–50 € |
| Cal.com / Calendly | 0–20 € |
| HubSpot CRM | 0 € |
| OpenAI / Claude API | 50–200 € |
| Typeform / Tally | 0–30 € |
| Canva Pro | 15 € |
| CapCut / Descript | 0–15 € |
| Twilio / WhatsApp API | 20–100 € |
| Looker Studio | 0 € |
| Notion | 0–10 € |
| Google Ads / LinkedIn Ads | 1.500–5.000 € |
| **Gesamt (ohne Ads)** | **~150–600 €/Monat** |
| **Gesamt (mit Ads)** | **~1.650–5.600 €/Monat** |

---

## 7. Risiken & Limits der Automatisierung

| Risiko | Mitigation |
|--------|------------|
| KI-Halluzinationen | Menschliches Review, RAG-Systeme, begrenzte Anwendungsfälle |
| Datenschutzverstöße | DSGVO-Check pro Workflow, EU-Hosting, Verträge |
| Überautomatisierung | Kundenbeziehung pflegen, persönliche Touchpoints beibehalten |
| Technische Ausfälle | Monitoring, Backups, Fallback-Prozesse |
| Wartungsaufwand | Monatliche Workflow-Reviews, Dokumentation |
| Kundenakzeptanz | Transparent kommunizieren, Schulung anbieten |

---

## 8. Fazit

Der Großteil des Marketings, Vertriebs und Betriebs lässt sich automatisieren. Der Schlüssel ist ein **modularer Stack** aus n8n/Make, Brevo/ActiveCampaign, Cal.com und KI-APIs.  
Menschliche Arbeit konzentriert sich auf **Verkauf, Strategie, Qualitätskontrolle und Kundenbeziehung**.  
So lässt sich ein hohes Maß an Skalierbarkeit bei gleichzeitig persönlichem Kundenerlebnis erreichen.
