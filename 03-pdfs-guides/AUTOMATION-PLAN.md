# Automations-Plan — PDFs & Guides für 35+

## Grundsatz

Ziel ist es, **80–90 % aller Prozesse** im Bereich PDFs/Guides zu automatisieren. Der Mensch konzentriert sich auf Strategie, Qualitätskontrolle, kreative Richtung und persönliche Interaktionen mit hochwertigen Leads. Alles Wiederholbare, Skalierbare und Datenbasierte läuft über Agenten, Workflows und Tools.

---

## Tool-Stack-Empfehlung

### Kategorie: KI-gestützte Content-Erstellung

| Tool | Aufgabe | Kosten (ca.) |
|------|---------|--------------|
| **Claude (Anthropic)** | Langform-Texte, Guides, E-Mail-Sequenzen, Recherche | 20 $/Monat |
| **Kimi (Moonshot)** | Analyse, Strukturierung, deutsche Texte | Freemium / günstig |
| **ChatGPT** | Brainstorming, Varianten, schnelle Recherche | 20 $/Monat |
| **Midjourney / Ideogram** | Cover, Infografiken, Visuals | 10–30 $/Monat |
| **Canva AI** | Design, Layout, Templates | 12 $/Monat |

### Kategorie: Funnel & Vertrieb

| Tool | Aufgabe | Kosten (ca.) |
|------|---------|--------------|
| **Carrd / Webflow** | Landing Pages | 19–29 $/Monat |
| **Gumroad** | Verkauf digitaler Produkte | Gebühren 10 % |
| **Payhip** | EU-freundlicher Verkauf | 5 % Gebühr |
| **ThriveCart** | Upsells, One-Click-Bumps | Einmalkauf ca. 495 $ |
| **Stripe** | Zahlungsabwicklung | Transaktionsgebühren |

### Kategorie: E-Mail & Messenger

| Tool | Aufgabe | Kosten (ca.) |
|------|---------|--------------|
| **Brevo** | E-Mail-Marketing (bis 9.000 Mails/Monat kostenlos) | 0–25 €/Monat |
| **Klick-Tipp** | DACH-fokussiert, DSGVO-konform | 25–50 €/Monat |
| **ActiveCampaign** | Erweiterte Automation & CRM | 29 $/Monat |
| **360dialog** | WhatsApp Business API | 49 €/Monat + Nachrichtengebühren |
| **MessageBird / Twilio** | SMS & WhatsApp | Pay-per-Use |
| **Manychat** | WhatsApp/Instagram-Chatbots | 15 $/Monat |

### Kategorie: Automation & Workflows

| Tool | Aufgabe | Kosten (ca.) |
|------|---------|--------------|
| **n8n** | Selbstgehostete Automation | Kostenlos (Self-Hosted) oder 20 $/Monat |
| **Make** | Visuelle Workflow-Automation | 9–16 $/Monat |
| **Zapier** | Einfache Integrationen | 19 $/Monat |

### Kategorie: Tracking & Reporting

| Tool | Aufgabe | Kosten (ca.) |
|------|---------|--------------|
| **Google Analytics 4** | Webseiten-Tracking | Kostenlos |
| **Google Looker Studio** | Dashboards & Reports | Kostenlos |
| **Meta Pixel / CAPI** | Ad-Tracking | Kostenlos |
| **Plausible / Fathom** | DSGVO-konformes Tracking | 9–20 $/Monat |
| **Notion / Airtable** | Projektmanagement, Content-Kalender | Freemium |

---

## Empfohlener Start-Stack (Kosten: < 200 €/Monat)

| Tool | Kosten/Monat | Zweck |
|------|--------------|-------|
| Claude Pro | 20 $ | Content-Erstellung |
| Canva Pro | 12 $ | Design |
| Carrd Pro | 19 $/Jahr | Landing Pages |
| Brevo | 0 $ | E-Mail (bis 9.000 Mails) |
| Gumroad | Gebühren | Verkauf |
| n8n (Self-Hosted) | 0 $ | Automation |
| Google Analytics + Looker Studio | 0 $ | Tracking |
| Notion | 0 $ | Organisation |
| **Gesamt** | **~60–80 €/Monat + Gebühren** | — |

---

## Automatisierbare Workflows

### Workflow 1: Lead-Magnet-Erstellung (KI-gestützt)

| Schritt | Tool | Automation |
|---------|------|------------|
| 1. Recherche & Gliederung | Claude / Kimi | Prompt-basierte Erstellung |
| 2. Text verfassen | Claude / Kimi | Erster Entwurf automatisch |
| 3. Fakten prüfen | Mensch / Web-Suche | Manuell (30–60 Min.) |
| 4. Design & Layout | Canva | Template-basiert |
| 5. Cover erstellen | Midjourney / Canva | Automatisch |
| 6. Finalisieren | Mensch | Qualitätskontrolle |

**Zeitersparnis:** Von 2–3 Wochen auf 2–3 Tage reduzierbar.

### Workflow 2: Lead-Erfassung & Begrüßung

```
Landing-Page-Formular
       ↓
E-Mail-Tool (Brevo) → Double-Opt-In-E-Mail
       ↓
Bestätigung → Willkommens-E-Mail mit Download-Link
       ↓
Webhook an n8n/Make
       ↓
WhatsApp-Begrüßung (optional, bei Handynummer)
       ↓
CRM/Notion-Datenbank aktualisieren
       ↓
Retargeting-Pixel feuern (Meta, Google)
```

### Workflow 3: Nurturing-Sequenz

```
Tag 0: Willkommens-E-Mail + WhatsApp
Tag 1: Wert-E-Mail (Tipp/Story)
Tag 3: Wert-E-Mail + Video/Artikel
Tag 5: Soft-Sell Low-Ticket
Tag 7: Social Proof / Kundenstory
Tag 10: Direct-Sell + Rabatt
Tag 14: Last-Chance-E-Mail
```

**Automation:** E-Mail-Tool (Brevo/ActiveCampaign) + n8n für bedingte Logik (z. B. „Wenn gekauft, Sequenz stoppen").

### Workflow 4: Verkauf & Upsell

```
Kauf auf Gumroad/ThriveCart
       ↓
Zahlung bestätigen
       ↓
Produkt automatisch ausliefern
       ↓
E-Mail mit Download + Upsell-Angebot
       ↓
One-Click-Upsell-Seite (ThriveCart)
       ↓
Wenn abgelehnt → Downsell-Angebot
       ↓
Kunde in „Käufer"-Segment verschieben
       ↓
WhatsApp-Willkommensnachricht als Kunde
```

### Workflow 5: Retargeting & Lookalikes

```
Besucher Landing Page ohne Opt-in
       ↓
Meta Pixel erfasst Besucher
       ↓
Retargeting-Anzeige: „Holen Sie sich die Checkliste"
       ↓
Bei Opt-in: Lookalike-Audience erstellen
       ↓
Skalierung auf ähnliche Zielgruppen
```

### Workflow 6: Reporting & Optimierung

```
Datenquellen: Gumroad, Brevo, Meta Ads, Google Ads, WhatsApp
       ↓
n8n sammelt täglich Kennzahlen
       ↓
Google Sheets / Airtable als Datenbank
       ↓
Looker Studio generiert Dashboard
       ↓
Wöchentlicher Report per E-Mail an Entscheider
```

### Workflow 7: Content-Wiederverwertung

```
Langform-Guide
       ↓
Claude erstellt daraus:
   - 5 LinkedIn-Posts
   - 3 YouTube-Shorts-Scripts
   - 1 E-Mail-Sequenz
   - 10 Tweet/X-Posts
   - 1 Instagram-Carousel
       ↓
Canva erstellt passende Grafiken
       ↓
Buffer/Later plant Veröffentlichung
```

---

## Limits der Automatisierung

### Was bleibt menschlich?

| Bereich | Warum menschlich? |
|---------|-------------------|
| **Qualitätskontrolle** | Faktenprüfung, Rechtschreibung, rechtliche Risiken (Finanzen/Gesundheit) |
| **Strategie & Positionierung** | Entscheidungen über Nischen, Preise, Markenrichtung |
| **Kreative Richtung** | Cover-Design, Storytelling, emotionale Ansprache |
| **Hochpreisige Verkaufsgespräche** | 1:1-Beratungen, Coaching-Termine, B2B-Angebote |
| **Kundenbeschwerden & Rückfragen** | Persönlicher Support bei komplexen Fragen |
| **Inhaltliche Updates** | Steuer-, Rechts- und Gesundheits-Updates erfordern menschliche Prüfung |
| **Partnerschaften & Kooperationen** | Verhandlungen mit Affiliate-Partnern und Medien |

### Risiken der Über-Automatisierung

- **Impersonale Kommunikation:** 35+ merkt schnell, wenn Nachrichten maschinell wirken.
- **Fehlinformationen:** KI kann falsche Fakten produzieren — besonders bei Finanz- und Gesundheitsthemen gefährlich.
- **Compliance:** DSGVO, E-Commerce-Recht und Finanz-/Gesundheits-Regularien erfordern menschliche Kontrolle.
- **Markenimage:** Zu viel Automation kann Vertrauen zerstören.

---

## Mensch vs. Agent — Verantwortlichkeiten

| Aufgabe | Mensch | Agent/Automation |
|---------|--------|------------------|
| Strategie & Nischenwahl | ✓ | — |
| Inhaltskonzept & Gliederung | ✓ | Unterstützung |
| Erstentwurf Text | — | ✓ |
| Faktenprüfung & Compliance | ✓ | — |
| Design-Entscheidungen | ✓ | Umsetzung |
| Landing-Page-Setup | — | ✓ (nach Vorlage) |
| E-Mail-Sequenzen | Konzept & Review | ✓ (Entwurf & Versand) |
| WhatsApp-Nachrichten | Review & Eskalation | ✓ (Automation) |
| Ad-Kampagnen-Setup | Strategie | ✓ (Teilweise) |
| Ad-Optimierung | Review | ✓ (Datenbasiert) |
| Kunden-Support Level 1 | — | ✓ (Chatbot/FAQ) |
| Kunden-Support Level 2 | ✓ | — |
| Reporting | Interpretation | ✓ (Datensammlung) |

---

## Fazit

Empire-Expansion kann den Bereich PDFs/Guides weitgehend als **automatisierte Content-Maschine** betreiben. Der entscheidende Erfolgsfaktor ist die **Klärung der Verantwortlichkeiten:** KI und Automation übernehmen Erstellung, Vertrieb, Nurturing und Reporting; der Mensch sichert Qualität, Compliance und strategische Ausrichtung.
