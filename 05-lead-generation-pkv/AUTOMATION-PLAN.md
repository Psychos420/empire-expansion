# Automation-Plan: PKV Lead Generation

## Grundprinzip

> **Automatisieren, was skalierbar und regelbasiert ist. Menschlich bleiben, wo Vertrauen, Compliance und Komplexität es erfordern.**

Ziel ist es, **80 % des Lead-Gen-Funnels** zu automatisieren, ohne die Qualität der Beratung zu gefährden. Der Mensch konzentriert sich auf das **Beratungsgespräch**, die **Compliance-Prüfung** und die **strategische Weiterentwicklung**.

---

## 1. Automatisierbare Bereiche

### 1.1 Content-Erstellung

| Aufgabe | Automatisierungsgrad | Tools | Hinweise |
|---------|---------------------|-------|----------|
| Ideenfindung | 80 % | Kimi/Claude, Ahrefs, AnswerThePublic | AI generiert Vorschläge, Mensch priorisiert |
| Erstdraft-Artikel | 80 % | Kimi/Claude, Jasper, Copy.ai | AI erstellt Draft, Mensch redigiert |
| SEO-Optimierung | 70 % | Surfer SEO, Clearscope, NeuronWriter | AI-gestützte Keyword-Einbindung |
| Social-Media-Posts | 90 % | Kimi/Claude, Buffer, Hootsuite | Automatische Ableitung aus Longform-Content |
| Newsletter | 80 % | Kimi/Claude, ActiveCampaign, Mailchimp | AI generiert Varianten, Mensch finalisiert |
| Video-Scripts | 70 % | Kimi/Claude, Descript | AI erstellt Script, Mensch nimmt auf |

**Empfehlung:** AI als **Ersteller + Assistent**, nicht als Ersatz für menschliche Qualitätskontrolle. Jeder Content muss auf Faktentreue und Compliance geprüft werden.

### 1.2 Lead-Erfassung & Qualifizierung

| Aufgabe | Automatisierungsgrad | Tools |
|---------|---------------------|-------|
| Formular-Erfassung | 100 % | GoHighLevel, Typeform, Jotform |
| Lead-Validierung (E-Mail, Telefon) | 90 % | ZeroBounce, Phone Validator, n8n |
| Lead-Scoring | 90 % | GoHighLevel, HubSpot, n8n |
| Segmentierung | 100 % | GoHighLevel, ActiveCampaign, Make |
| Duplikaterkennung | 95 % | GoHighLevel, HubSpot |
| Anreicherung mit externen Daten | 70 % | n8n + APIs (z. B. LinkedIn, Firmendaten) |

### 1.3 E-Mail-Marketing & Nurturing

| Aufgabe | Automatisierungsgrad | Tools |
|---------|---------------------|-------|
| Willkommens-E-Mail | 100 % | GoHighLevel, ActiveCampaign, Mailchimp |
| Follow-up-Sequenzen | 100 % | GoHighLevel, ActiveCampaign |
| Personalisierte Content-Blöcke | 80 % | Dynamic Content, Merge Tags, AI |
| A/B-Testing | 90 % | ActiveCampaign, GoHighLevel |
| Öffnungs-/Klick-Tracking | 100 % | Alle gängigen E-Mail-Tools |
| Reaktivierungskampagnen | 100 % | GoHighLevel, n8n |

### 1.4 SMS / WhatsApp-Follow-up

| Aufgabe | Automatisierungsgrad | Tools |
|---------|---------------------|-------|
| Automatische Erinnerungen | 100 % | GoHighLevel, Twilio, MessageBird |
| Trigger-basierte Nachrichten | 100 % | GoHighLevel, n8n + WhatsApp Business API |
| Zwei-Wege-Kommunikation | 50 % | Chatbot + menschlicher Eingriff bei komplexen Fragen |

**Hinweis:** WhatsApp Business API erfordert genehmigte Vorlagen. Einsatz für Terminerinnerungen und Reaktivierung sinnvoll.

### 1.5 Terminbuchung

| Aufgabe | Automatisierungsgrad | Tools |
|---------|---------------------|-------|
| Online-Terminbuchung | 100 % | Calendly, GoHighLevel Calendar, Acuity |
| Kalender-Synchronisation | 100 % | Google Calendar, Outlook |
| Erinnerungen (E-Mail/SMS) | 100 % | GoHighLevel, Calendly |
| Videokonferenz-Links | 100 % | Zoom, Google Meet, Teams |
| No-Show-Reaktivierung | 100 % | GoHighLevel, n8n |

### 1.6 Berater-Vorbereitung

| Aufgabe | Automatisierungsgrad | Tools |
|---------|---------------------|-------|
| Lead-Briefing-Report | 90 % | Kimi/Claude, n8n, GoHighLevel |
| Tarif-Vorschlagsliste | 80 % | Interne Datenbank + AI |
| Gesprächsnotizen | 60 % | AI-Transkription (Otter.ai, Fireflies) |
| Angebotserstellung | 70 % | PandaDoc, DocuSign, n8n |

### 1.7 Reporting & Analyse

| Aufgabe | Automatisierungsgrad | Tools |
|---------|---------------------|-------|
| Dashboard-Updates | 100 % | Looker Studio, GoHighLevel Dashboards |
| KPI-Alerts | 100 % | n8n, Make, Slack |
| Lead-Quellen-Analyse | 100 % | Google Analytics 4, GoHighLevel |
| Conversion-Tracking | 100 % | Google Tag Manager, Meta Pixel |
| Wöchentliche Reports | 90 % | Kimi/Claude + Looker Studio |

### 1.8 Scraping & Marktüberwachung

| Aufgabe | Automatisierungsgrad | Tools |
|---------|---------------------|-------|
| Wettbewerber-Tarifüberwachung | 80 % | Python + Scrapy, n8n, Apify |
| Preisänderungen tracken | 80 % | n8n, Make, Monitoro |
| News & regulatorische Änderungen | 90 % | RSS-Feeds, Kimi/Claude-Zusammenfassung |
| Kundenbewertungen sammeln | 90 % | Scraping + Sentiment-Analyse |

---

## 2. Konkreter Tool-Stack

### Empfohlener Core-Stack

| Kategorie | Tool | Zweck | Geschätzte Kosten/Monat |
|-----------|------|-------|------------------------|
| **CRM & Automation** | GoHighLevel | Landing Pages, Funnel, E-Mail/SMS, CRM, Terminbuchung | 150–300 € |
| **Workflow-Automation** | n8n | Verbindung zwischen Tools, Scraping, komplexe Logik | 0–50 € (Self-Hosted) |
| **E-Mail-Marketing** | GoHighLevel (integriert) | Newsletter, Follow-up-Sequenzen | inklusive |
| **KI-Assistenten** | Kimi / Claude | Content, Berater-Briefings, Report-Erstellung | 20–100 € |
| **Landing Pages** | GoHighLevel / Webflow | High-Converting Pages | 20–50 € |
| **Tracking & Analytics** | Google Analytics 4 + Tag Manager | Tracking, Conversion-Messung | kostenlos |
| **Reporting** | Looker Studio | Dashboards, Reports | kostenlos |
| **Terminbuchung** | GoHighLevel Calendar / Calendly | Online-Termine | inklusive / 10 € |
| **WhatsApp/SMS** | GoHighLevel / Twilio | Follow-up, Erinnerungen | 20–100 € |
| **SEO-Tools** | Ahrefs / Surfer SEO | Keyword-Recherche, Content-Optimierung | 100–200 € |
| **Design** | Canva / Figma | Creatives, PDF-Lead-Magnete | 0–30 € |
| **Dokumente & Verträge** | PandaDoc / DocuSign | Angebotserstellung, Unterschrift | 20–50 € |

### Alternative Stacks

| Szenario | Alternative |
|----------|-------------|
| Budget-Stack | WordPress + Elementor + Mailchimp + n8n + Calendly |
| Enterprise-Stack | HubSpot + Salesforce + Marketo + Make |
| Einfacher Stack | GoHighLevel allein für 80 % der Anforderungen |

**Empfehlung für Empire Expansion:** Start mit **GoHighLevel + n8n + Kimi/Claude**. Dieser Stack deckt 90 % der Anforderungen ab, ist skalierbar und kosteneffizient.

---

## 3. Konkrete Workflows

### Workflow 1: Lead erfasst → Qualifiziert → Gescort

```
Formular-AbSendung (Landing Page)
    ↓
E-Mail-Validierung (ZeroBounce via n8n)
    ↓
Lead in CRM anlegen (GoHighLevel)
    ↓
Lead-Scoring berechnen (n8n)
    ↓
Segmentierung (Beamte / Selbstständige / Angestellte / Sonstige)
    ↓
Willkommens-E-Mail + Lead-Magnet senden
    ↓
Zugehörige Follow-up-Sequenz starten
    ↓
Bei Score >70: Aufgabe für Berater + SMS/WhatsApp an Lead
    ↓
Bei Terminbuchung: Erinnerungen + Berater-Briefing generieren
```

### Workflow 2: Content-Produktion

```
Keyword-Recherche (Ahrefs)
    ↓
AI generiert Outline (Kimi/Claude)
    ↓
Menschliche Freigabe Outline
    ↓
AI erstellt Erstdraft (Kimi/Claude)
    ↓
Menschliche Redaktion + Faktencheck
    ↓
SEO-Optimierung (Surfer SEO)
    ↓
Veröffentlichung (WordPress/Webflow)
    ↓
Automatische Social-Media-Posts (n8n + Buffer)
    ↓
Newsletter-Zusammenfassung (Kimi/Claude)
```

### Workflow 3: Wettbewerbs-Monitoring

```
Scraping-Watcher (n8n/Apify)
    ↓
Tarifänderungen erkennen
    ↓
AI-Zusammenfassung (Kimi/Claude)
    ↓
Alert an Slack/Teams
    ↓
Content-Update oder Kampagnenanpassung
```

### Workflow 4: Berater-Briefing vor Termin

```
Termin gebucht
    ↓
Lead-Daten aus CRM ziehen (n8n)
    ↓
AI generiert Berater-Briefing (Kimi/Claude)
    ↓
Tarif-Vorschläge aus Datenbank abrufen
    ↓
PDF-Briefing an Berater senden
    ↓
Gespräch findet statt
    ↓
Menschliche Notizen + AI-Transkription
    ↓
Automatisches Angebotspdf (PandaDoc)
```

---

## 4. Was bleibt menschlich?

### Unbedingt menschlich

| Bereich | Begründung |
|---------|------------|
| **Beratungsgespräch** | Komplexe, individuelle Entscheidung; Vertrauen entscheidend |
| **Compliance-Prüfung** | Versicherungsrecht, DSGVO, Wettbewerbsrecht |
| **Gesundheitsdaten** | Besondere Kategorien nach DSGVO, nie ungeprüft automatisieren |
| **Tarifempfehlung** | Individuelle Bedarfsanalyse erforderlich |
| **Beschwerdemanagement** | Persönlicher Kontakt bei Unzufriedenheit |
| **Content-Faktencheck** | Falsche Versicherungsinformationen können rechtliche Folgen haben |

### Teilweise menschlich

| Bereich | Automatisierungsgrad | Menschlicher Anteil |
|---------|---------------------|---------------------|
| **E-Mail-Antworten auf komplexe Fragen** | 50 % | AI-Entwurf, Mensch prüft/sendet |
| **Social-Media-Kommentare** | 70 % | AI-Entwürfe, Mensch moderiert |
| **Angebotserstellung** | 70 % | AI-Entwurf, Berater finalisiert |
| **Lead-Qualifizierung bei Edge Cases** | 60 % | Regeln + menschliche Review |

---

## 5. Limits & Risiken der Automation

| Risiko | Gegenmaßnahme |
|--------|---------------|
| **Falsche Versicherungsinformationen durch AI** | Faktencheck, Quellenangaben, keine medizinischen Beratungen |
| **DSGVO-Verstoß bei Gesundheitsdaten** | Keine Speicherung sensibler Daten ohne Einwilligung, AVV mit Tools |
| **Impersonalität trotz Automation** | Personalisierung, menschliche Beratung als Ergänzung |
| **Over-Automation** | Regelmäßige Review der Funnel-Performance |
| **Tool-Abhängigkeit** | Backups, Datenexport, keine Lock-in-Strategie |

---

## 6. Skalierungsplan für Automation

| Phase | Fokus | Ziel |
|-------|-------|------|
| **Monat 1** | CRM + Landing Page + E-Mail-Follow-up | Erste 100 Leads automatisiert erfassen |
| **Monat 2** | Lead-Scoring + SMS/WhatsApp + Terminbuchung | 50 % der Terminbuchungen automatisiert |
| **Monat 3** | Berater-Briefing + Angebotserstellung | Berater sparen 50 % Vorbereitungszeit |
| **Monat 4–6** | Content-Automation + SEO-Maschine | 4 Artikel/Woche mit AI-Unterstützung |
| **Monat 7–12** | Wettbewerbs-Monitoring + Advanced Analytics | Vollständiges Data-Driven-Operation |

---

*Stand: Juli 2026 | Automation-Plan für Empire Expansion PKV-Lead-Generation.*
