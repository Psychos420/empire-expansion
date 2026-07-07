# Automation-Plan: Marketing Agency Traffic

## Strategische Grundlage

> **„Wiederhole nie etwas dreimal, das ein System einmal tun kann."**

Dieser Plan definiert, welche Teile der Agentur automatisiert werden und welche menschlich bleiben. Ziel ist es, **Skalierbarkeit bei hoher Qualität** zu erreichen.

---

## Automatisierungsgrade

| Grad | Bedeutung | Beispiele |
|------|-----------|-----------|
| **Vollautomatisch** | Kein menschlicher Eingriff nötig | Reporting, E-Mail-Follow-ups, Lead-Scoring, Content-Distribution |
| **Halbautomatisch** | Menschlicher Trigger oder Review nötig | Content-Erstellung (KI-Entwurf + Mensch prüft), Anzeigen-Launch |
| **Unterstützend** | Tool unterstützt menschliche Arbeit | Verkaufsgespräche, Strategieentwicklung, Kundenbeziehung |
| **Menschlich** | Keine sinnvolle Automatisierung möglich | Komplexe Verhandlungen, kreative Konzeption, Krisenkommunikation |

---

## Tool-Stack-Empfehlung

### Kern-Stack (Start)

| Kategorie | Tool | Zweck | Kosten (ca.) |
|-----------|------|-------|--------------|
| **CRM & Pipeline** | GoHighLevel oder Pipedrive | Leads, Kunden, Termine, Deals | 97–297 €/Monat |
| **E-Mail-Marketing** | Brevo oder ActiveCampaign | Automation, Newsletter, Sequenzen | 0–79 €/Monat |
| **WhatsApp/SMS** | GoHighLevel + WhatsApp Business API | Direkte Follow-ups | 0–50 €/Monat + Nachrichtenkosten |
| **Automation** | n8n (self-hosted) oder Make | Workflows zwischen Tools | 0–16 €/Monat (n8n) / 9 €+ (Make) |
| **KI-Assistenten** | Kimi / Claude | Content, Audits, Berichte, E-Mail-Entwürfe | 20–60 €/Monat |
| **Landing Pages** | Webflow / Swipe Pages | Conversion-optimierte Seiten | 0–39 €/Monat |
| **Ads Management** | Google Ads, Meta Ads, LinkedIn Campaign Manager | Paid Traffic | ab Ad Spend |
| **Tracking & Analytics** | Google Analytics 4, Looker Studio, Meta Pixel | Messung und Reporting | kostenlos |
| **Terminbuchung** | Cal.com oder Calendly | Selbstbuchung durch Leads | 0–12 €/Monat |
| **Projektmanagement** | Notion oder ClickUp | Aufgaben, Dokumentation, SOPs | 0–10 €/Monat |

### Erweiterter Stack (Scale)

| Kategorie | Tool | Zweck |
|-----------|------|-------|
| **KI-Content-Machine** | Kimi/Claude + Airtable/Make | Massenproduktion von Content-Entwürfen |
| **SEO/GEO** | Ahrefs oder SE Ranking | Keyword-Recherche, Rank-Tracking |
| **Social Media Management** | Metricool oder Buffer | Planung, Veröffentlichung, Reporting |
| **Reputation Management** | LocalViking oder BrightLocal | Google-Business-Profile-Management |
| **Call Tracking** | CallRail oder Retreaver | Telefon-Leads messen |
| **Heatmaps & CRO** | Hotjar oder Microsoft Clarity | Landing-Page-Optimierung |

---

## Konkrete Workflows

### Workflow 1: Lead-Capture → CRM → Nurturing

```
Landing-Page-Formular
    ↓
CRM (GoHighLevel / Pipedrive)
    ↓
Tagging & Lead-Scoring (n8n)
    ↓
Willkommens-E-Mail (Brevo)
    ↓
WhatsApp/SMS-Willkommen (optional)
    ↓
7-Tage-Nurturing-Sequenz starten
    ↓
Bei Klick/Öffnung → Score erhöhen
Bei Terminbuchung → aus Sequenz nehmen
```

**Automatisierungsgrad:** Vollautomatisch

---

### Workflow 2: Content-Produktion & Distribution

```
Thema/Keyword (Mensch definiert)
    ↓
KI erstellt Entwurf (Blog, LinkedIn-Post, E-Mail, Video-Skript)
    ↓
Mensch reviewt und finalisiert
    ↓
Scheduling via Metricool/Buffer
    ↓
Veröffentlichung auf Website, LinkedIn, E-Mail, YouTube
    ↓
Performance-Tracking in Looker Studio
```

**Automatisierungsgrad:** Halbautomatisch

---

### Workflow 3: Ads-Reporting & Optimierung

```
Google Ads / Meta Ads / LinkedIn Ads API
    ↓
Daten sammeln (n8n oder Make)
    ↓
In Google Sheets oder Data Warehouse speichern
    ↓
Looker Studio Dashboard aktualisieren
    ↓
Wöchentliche E-Mail an Kunden mit KPIs
    ↓
Bei Abweichung > 20 % → Alert an Account Manager
```

**Automatisierungsgrad:** Vollautomatisch (Alert halbautomatisch)

---

### Workflow 4: Kunden-Onboarding

```
Vertrag unterschrieben (DigitalSignature-Tool)
    ↓
Rechnung erstellt (sevDesk oder FastBill)
    ↓
Willkommens-E-Mail mit nächsten Schritten
    ↓
Aufgaben in ClickUp/Notion erstellen
    ↓
Zugänge anfordern (automatisierter E-Mail-Text)
    ↓
Kickoff-Termin vorschlagen (Cal.com)
    ↓
Erstes Strategie-Dokument (KI-Template + Mensch)
```

**Automatisierungsgrad:** Halbautomatisch

---

### Workflow 5: Lead-Scoring & Sales-Alert

```
Lead füllt Formular aus
    ↓
Punkte basierend auf:
   - Branche (Dienstleister = +10)
   - Unternehmensgröße (+5 bis +20)
   - Seitenbesuche (+5 pro Besuch)
   - E-Mail-Öffnungen (+2)
   - Klicks (+5)
   - Terminbuchung (+50)
    ↓
Bei Score > 40 → E-Mail/SMS an Vertrieb
    ↓
Vertrieb ruft an oder schreibt persönlich
```

**Automatisierungsgrad:** Vollautomatisch (Alert)

---

### Workflow 6: Rezensionsmanagement (lokale Unternehmen)

```
Kunde abgeschlossen / Termin beendet
    ↓
Automatische SMS/E-Mail mit Bewertungslink
    ↓
Bei 4–5 Sternen → Danke-Nachricht
    ↓
Bei 1–3 Sterne → Alert an Inhaber + Entschuldigungs-Workflow
```

**Automatisierungsgrad:** Vollautomatisch

---

### Workflow 7: WhatsApp/SMS-Follow-up

```
Lead nicht reagiert nach 48h
    ↓
WhatsApp-Nachricht mit persönlichem Hinweis
    ↓
Keine Reaktion nach weiteren 72h
    ↓
SMS mit direktem Kalender-Link
    ↓
Keine Reaktion nach 7 Tagen
    ↓
In „Langfristig-Nurturing"-Sequenz verschieben
```

**Automatisierungsgrad:** Vollautomatisch

---

## Was bleibt menschlich?

| Bereich | Warum menschlich? |
|---------|-------------------|
| **Verkaufsgespräche** | Vertrauen, Einwände, Verhandlung |
| **Strategieentwicklung** | Kontext, Kreativität, langfristige Planung |
| **Kreative Konzeption** | Branding, emotionale Ansprache |
| **Kundenbeziehung** | Loyalität, Upselling, Konfliktlösung |
| **Komplexe Anzeigen-Optimierung** | Interpretation von Daten, strategische Anpassungen |
| **Qualitätskontrolle KI-Output** | Faktenprüfung, Tonalität, Compliance |
| **Krisenkommunikation** | Schnelle, sensible Entscheidungen |

---

## KI-Einsatz im Detail

### Kimi / Claude für

| Aufgabe | Nutzen |
|---------|--------|
| **Blog-Artikel** | Entwürfe in 5–10 Min. statt 3–4 Stunden |
| **E-Mail-Sequenzen** | Variationen für A/B-Tests |
| **Landing-Page-Texte** | Conversion-optimierte Kopien |
| **Video-Skripte** | Struktur und Sprechtexte |
| **Kunden-Audits** | Analyse von Websites/Ads-Konten |
| **Reporting-Kommentare** | Automatische Einordnung von KPI-Schwankungen |
| **Chatbot-Antworten** | Wissensdatenbank für Support |

### Wichtig: KI-Governance

- Alle KI-Outputs werden vor Veröffentlichung von einem Menschen geprüft.
- Faktencheck für alle Behauptungen.
- Keine KI-generierten Inhalte ohne menschliche Finalisierung an Kunden.

---

## Limits der Automatisierung

1. **Keine vollautomatische Kaltakquise ohne Opt-in** – DSGVO-Konformität erfordert Einwilligung.
2. **Keine automatischen Versprechen** – „Garantierte Ergebnisse" sind rechtlich heikel.
3. **Keine KI-Kundenkommunikation ohne Review** – bei komplexen Anfragen immer menschlich.
4. **Keine vollautomatische Budget-Steuerung** – Ad-Spend-Änderungen menschlich freigeben.

---

## Zusammenfassung

Mit dem vorgeschlagenen Stack und den Workflows lässt sich **60–70 % des operativen Tagesgeschäfts automatisieren**. Der Mensch konzentriert sich auf Strategie, Verkauf, Kundenbeziehung und Qualitätskontrolle. Das ermöglicht Skalierung ohne proportionalen Personalkostenanstieg.

---

*Letzte Aktualisierung: Juli 2026*
