# AUTOMATION-PLAN.md — TikTok Shop Automation & Tool-Stack

> Welche Teile lassen sich automatisieren? Konkrete Tool-Stack-Empfehlung, Workflows und klare Grenzen: Was bleibt menschlich?

---

## 1. Automatisierungs-Philosophie

**Grundsatz:** Automatisieren, was repetitiv und skalierbar ist. Menschlich bleibt, was Vertrauen, Kreativität und strategische Entscheidungen erfordert.

| Automatisieren | Menschlich bleiben |
|----------------|--------------------|
| Content-Produktion ( erste Fassung) | Strategische Positionierung, finale Freigabe |
| E-Mail/SMS-Follow-ups | Persönliche Antworten auf komplexe Fragen |
| Daten-Reporting & Alerts | Interpretation und Entscheidungen |
| Bestandsabgleich & Fulfillment-Updates | Kundenbeschwerden, Retouren- Eskalationen |
| Lead-Qualifizierung (erste Stufe) | Verkaufsgespräche, Beratungstermine |
| Social Listening & Trend-Scraping | Kreative Konzeptentwicklung |

---

## 2. Empfohlener Tool-Stack

### 2.1 Übersicht

| Kategorie | Tool | Kosten (ca.) | Zweck |
|-----------|------|--------------|-------|
| **KI-Assistenten** | Kimi, Claude, ChatGPT | €20–€60/Monat | Scripte, Texte, Analysen, Strategie |
| **Automation** | n8n (self-hosted) oder Make | €0–€50/Monat | Workflows zwischen Tools |
| **E-Mail-Marketing** | ConvertKit / Brevo / Klaviyo | €0–€100/Monat | Sequenzen, Automation |
| **Landing Pages** | Carrd / Webflow / Shopify | €20–€50/Monat | Conversion-Seiten |
| **CRM** | Notion / HubSpot / Pipedrive | €0–€50/Monat | Lead- & Kundenmanagement |
| **SMS/WhatsApp** | ManyChat / Trengo | €20–€100/Monat | Direkter Dialog |
| **Terminbuchung** | Calendly / TidyCal | €0–€20/Monat | Termine |
| **Video-Schnitt** | CapCut / Descript | €0–€30/Monat | Kurzvideos |
| **Design** | Canva Pro | €15/Monat | Thumbnails, Social Graphics |
| **Analytics** | TikTok Seller Center + Google Sheets / Looker Studio | €0 | Reporting |
| **Scraping / Research** | Apify / ScraperAPI + Kimi/Claude | €50–€150/Monat | Trend- & Wettbewerbsdaten |
| **Fulfillment** | byrd / Salesupply / eigener 3PL | Variabel | Lager, Versand, Retouren |
| **Zahlungen** | Stripe / PayPal | Transaktionsgebühren | Checkout |

### 2.2 Tool-Auswahl-Logik

- **n8n statt Zapier/Make (für technisch versierte Teams):** Open Source, kostengünstiger, datenschutzfreundlicher (self-hosted in der EU möglich).
- **ConvertKit/Brevo:** Gute Automatisierung, DSGVO-freundlich, angemessen für Start.
- **Carrd:** Schnelle, günstige Landing Pages; später Webflow oder Shopify.
- **Notion:** CRM-Light für Start; später HubSpot oder Pipedrive.

---

## 3. Automatisierbare Workflows

### 3.1 Workflow: Ideenfindung & Content-Produktion

```
Schritt 1: Trend-Scraping (Apify / TikTok API / manuelle Suche)
    │
    ▼
Schritt 2: KI-Analyse (Kimi/Claude): Top 10 Trends für 35+ filtern
    │
    ▼
Schritt 3: Script-Generator (KI): Hook, Problem, Lösung, CTA
    │
    ▼
Schritt 4: Storyboard / Shot-List erstellen (Canva / Notion)
    │
    ▼
Schritt 5: Video-Produktion (Mensch / Creator)
    │
    ▼
Schritt 6: Schnitt & Untertitel (CapCut / Descript)
    │
    ▼
Schritt 7: Scheduling & Veröffentlichung (TikTok nativ oder Buffer/Later)
    │
    ▼
Schritt 8: Performance-Tracking (Google Sheets / Looker Studio)
```

**KI-Prompt-Beispiel für Scripts:**
```
Erstelle ein 45-sekündiges TikTok-Script für [Produkt] für eine Zielgruppe von Frauen 40+. 
Struktur: Hook (3 Sek.), Problem (10 Sek.), Lösung mit Produkt (20 Sek.), 
Social Proof (8 Sek.), Call-to-Action (4 Sek.).
Tonfall: kompetent, warm, keine Jugendsprache.
```

### 3.2 Workflow: Lead-Erfassung & E-Mail-Sequenz

```
Trigger: Formular-Submission auf Landing Page
    │
    ▼
Aktion 1: Kontakt in E-Mail-Tool (ConvertKit/Brevo) taggen
    │
    ▼
Aktion 2: Lead-Magnet per E-Mail senden
    │
    ▼
Aktion 3: CRM-Eintrag in Notion/HubSpot
    │
    ▼
Aktion 4: Start E-Mail-Sequenz (Tag 0, 1, 2, 4, 7, 10, 14)
    │
    ▼
Aktion 5: Bei Klick auf Produktlink → SMS/WhatsApp-Sequenz starten
    │
    ▼
Aktion 6: Bei Kauf → Post-Purchase-Sequenz + CRM-Update
```

### 3.3 Workflow: TikTok-Shop-Bestellung → Fulfillment

```
Trigger: Neue Bestellung im TikTok Seller Center
    │
    ▼
Aktion 1: Bestellung an Fulfillment-Dienstleister (byrd / 3PL)
    │
    ▼
Aktion 2: Rechnung / Lieferschein erstellen (Lexoffice / SevDesk via n8n)
    │
    ▼
Aktion 3: Käufer in E-Mail-CRM eintragen + taggen
    │
    ▼
Aktion 4: Post-Purchase-E-Mail-Sequenz starten
    │
    ▼
Aktion 5: Tracking-Information an Kunden senden
    │
    ▼
Aktion 6: Nach Lieferung: Review-Request + UGC-Einladung
```

### 3.4 Workflow: Creator-Affiliate-Management

```
Schritt 1: Scraper findet potenzielle Micro-Influencer (30–50 Jahre, Nische)
    │
    ▼
Schritt 2: KI filtert passende Creator nach Engagement, Content-Fit
    │
    ▼
Schritt 3: Personalisierte Outreach-E-Mail/WhatsApp generieren
    │
    ▼
Schritt 4: Vertrag & Affiliate-Link erstellen
    │
    ▼
Schritt 5: Produkt zuschicken
    │
    ▼
Schritt 6: Erinnerung nach 7/14 Tagen, Content anfordern
    │
    ▼
Schritt 7: Performance tracken (Sales, Views, ROAS)
    │
    ▼
Schritt 8: Top-Creator automatisch identifizieren & Bonus anbieten
```

### 3.5 Workflow: Social Listening & Trend-Monitoring

```
Schritt 1: Tägliches Scraping von TikTok-Trends (Hashtags, Sounds, Top-Videos)
    │
    ▼
Schritt 2: KI kategorisiert Trends nach Relevanz für 35+
    │
    ▼
Schritt 3: Slack/Discord/Notion-Benachrichtigung mit Top 3 Trends
    │
    ▼
Schritt 4: Content-Team entscheidet: adaptieren, ignorieren, innovieren
    │
    ▼
Schritt 5: Schnelle Content-Produktion für Top-Trend
```

### 3.6 Workflow: Reporting & Alerts

```
Schritt 1: Täglicher Daten-Export aus TikTok Seller Center
    │
    ▼
Schritt 2: n8n/Make verarbeitet Daten in Google Sheets / Notion
    │
    ▼
Schritt 3: Looker Studio Dashboard aktualisiert sich automatisch
    │
    ▼
Schritt 4: Alerts bei Abweichungen (z. B. ROAS <2, Retourenquote >15 %)
    │
    ▼
Schritt 5: Wöchentlicher Report an Entscheider
```

---

## 4. Konkrete Automatisierungs-Anwendungen

### 4.1 Content-Erstellung (KI-gestützt)

| Aufgabe | Tool | Automatisierungsgrad |
|---------|------|----------------------|
| Recherche & Ideen | Kimi/Claude + WebSearch | 80 % |
| Script-Schreiben | Kimi/Claude | 70 % (menschliches Polishing) |
| Thumbnail-Design | Canva + KI | 60 % |
| Untertitel | CapCut / Descript | 90 % |
| Video-Schnitt (Templates) | CapCut | 50 % |
| Hashtag-Recherche | KI + TikTok-Suche | 70 % |
| Cross-Posting | Buffer / Later / n8n | 90 % |

### 4.2 Kundenkommunikation

| Aufgabe | Tool | Automatisierungsgrad |
|---------|------|----------------------|
| Willkommens-E-Mail | ConvertKit/Brevo | 100 % |
| Post-Purchase-Sequenz | ConvertKit/Brevo | 100 % |
| Tracking-Benachrichtigungen | n8n + Versanddienstleister | 95 % |
| Review-Requests | E-Mail/SMS Automation | 100 % |
| Erste Kundenanfragen | Chatbot (Tidio / ManyChat) | 60 % |
| Komplexe Anfragen | Mensch | 0 % (menschlich) |
| Beschwerden / Retouren | Mensch + Tool-Unterstützung | 30 % |

### 4.3 E-Commerce-Operationen

| Aufgabe | Tool | Automatisierungsgrad |
|---------|------|----------------------|
| Bestellimport TikTok → ERP/Fulfillment | n8n / API | 95 % |
| Bestandsabgleich | ERP / Seller Center | 90 % |
| Rechnungsstellung | Lexoffice / SevDesk + n8n | 90 % |
| Retouren-Abwicklung | Fulfillment-Partner | 80 % |
| Preis-Monitoring | Scraper + Alerts | 70 % |
| Produkt-Listing-Optimierung | KI + Seller Center | 60 % |

### 4.4 Lead-Qualifizierung

| Aufgabe | Tool | Automatisierungsgrad |
|---------|------|----------------------|
| E-Mail-Adresse erfassen | Landing Page | 100 % |
| Erste Segmentierung (Quiz) | Typeform / ScoreApp | 100 % |
| Scoring (Interaktion, Klicks) | CRM / E-Mail-Tool | 80 % |
| Terminbuchung | Calendly | 100 % |
| Verkaufsgespräch | Mensch | 0 % |

---

## 5. Limits: Was bleibt menschlich?

### 5.1 Strategie & Positionierung
- Entscheidung über Nischen, Marken, Preise.
- Interpretation von Marktdaten und Trends.
- Langfristige Partnerschaften und Verhandlungen.

### 5.2 Kreative Leitung
- Finale Freigabe von Content.
- Entwicklung neuer Formate und Kampagnenideen.
- Umgang mit viralem Content und Krisenkommunikation.

### 5.3 Kundenbeziehungen
- Persönliche Antworten auf komplexe Fragen.
- Verkaufsgespräche für hochpreisige Angebote.
- Beschwerdenmanagement und Retouren-Eskalationen.

### 5.4 Compliance & Recht
- Prüfung von Produktclaims, Impressum, AGB.
- DSGVO-Konformität.
- Vertragsprüfung mit Lieferanten und Creatorn.

---

## 6. Datenschutz & DSGVO

### 6.1 Maßnahmen
- **E-Mail-Double-Opt-In** bei Lead-Generierung.
- **Transparente Datenschutzerklärung** auf Landing Pages.
- **EU-Server** für E-Mail-Tool, CRM und Automation (n8n self-hosted).
- **Keine Weitergabe** von Kundendaten an Dritte ohne Einwilligung.
- **Löschfristen** für nicht aktive Kontakte.

### 6.2 Tool-Checkliste DSGVO

| Tool | EU-Server | DPA verfügbar | Hinweis |
|------|-----------|---------------|---------|
| n8n (self-hosted) | Ja | Nicht nötig | Beste Option |
| ConvertKit | Ja | Ja | Prüfen |
| Brevo | Ja | Ja | Gute DSGWO-Option |
| Mailchimp | Teilweise | Ja | Datentransfer beachten |
| HubSpot | Ja | Ja | Enterprise-Features nötig |
| Calendly | USA | Ja | DPA abschließen |

---

## 7. Implementierungs-Reihenfolge

### Phase 1: Grundlagen (Woche 1–2)
- [ ] TikTok Seller Center eingerichtet
- [ ] E-Mail-Tool + Landing-Page-Tool gewählt
- [ ] n8n/Make-Account eingerichtet
- [ ] TikTok Pixel installiert
- [ ] CRM-Struktur definiert

### Phase 2: Erste Automationen (Woche 3–4)
- [ ] Lead-Magnet → E-Mail-Sequenz
- [ ] TikTok-Shop-Bestellung → Willkommens-E-Mail
- [ ] Review-Request nach 7 Tagen
- [ ] Täglicher Sales-Report

### Phase 3: Skalierung (Woche 5–8)
- [ ] Creator-Affiliate-Workflow
- [ ] Social Listening / Trend-Alerts
- [ ] KI-gestützte Content-Produktion
- [ ] Segmentierung und personalisierte Sequenzen

### Phase 4: Optimierung (ab Woche 9)
- [ ] A/B-Testing-Workflows
- [ ] Vorhersagemodelle für Churn/CLV
- [ ] Automatisierte Reporting-Dashboards
- [ ] Integration mit anderen Empire-Bereichen

---

## 8. Kostenübersicht Automation (Monatlich)

| Phase | Tools | Geschätzte Kosten/Monat |
|-------|-------|-------------------------|
| **Start** | n8n, Brevo/ConvertKit, Carrd, Canva, CapCut | €50–€100 |
| **Wachstum** | + HubSpot/Notion, ManyChat, Apify | €150–€300 |
| **Skalierung** | + Fulfillment, erweitertes CRM, Looker Studio | €300–€800 |

---

*Tool-Empfehlungen basieren auf aktuellen Marktstandards (2026). Vor endgültiger Auswahl sollten DSGVO, Preise und Integrationen geprüft werden.*
