# Automations-Plan: Gesundheit & Prävention ab 40

## Ziel der Automatisierung

- Maximale Skalierung bei minimalem manuellem Aufwand
- Personalisierte Kundenerlebnisse ohne linearen Personaleinsatz
- Datenbasierte Steuerung aller Marketing- und Vertriebsprozesse
- Rechtssichere Abwicklung von Gesundheits- und Versicherungsinhalten

---

## 1. Tool-Stack

### 1.1 Marketing & Sales Automation

| Funktion | Tool | Zweck |
|---|---|---|
| E-Mail-Marketing & Automation | ActiveCampaign / ConvertKit | Lead-Nurturing, Sales-Flows, Segmentation |
| CRM | HubSpot (kostenlos) / ActiveCampaign CRM | Kontaktverwaltung, Pipeline, Deals |
| Landingpages | Webflow / WordPress + Elementor | Conversion-optimierte Seiten |
| Formulare & Quiz | Typeform / ActiveCampaign | Lead-Erfassung, Gesundheits-Check |
| Webinar | Zoom / Livestorm | Conversion-Events |
| Retargeting | Meta Ads, Google Ads | Wiedergewinnung von Leads |

### 1.2 E-Commerce & Membership

| Funktion | Tool | Zweck |
|---|---|---|
| Online-Shop / Checkout | Shopify / WooCommerce / Stripe | Produktverkauf, Abos |
| Membership / Kurse | Kajabi / Teachable / Circle | geschützte Inhalte, Community |
| Zahlungen | Stripe + PayPal + SEPA | wiederkehrende Zahlungen |
| Rechnung & Buchhaltung | sevDesk / FastBill | Automatische Rechnungen |
| Upsell / Order Bumps | CartHook / OneClickUpsell | AOV-Steigerung |

### 1.3 Content-Produktion

| Funktion | Tool | Zweck |
|---|---|---|
| Video-Schnitt | CapCut / Descript | Kurzvideos, Webinar-Clips |
| Grafik-Design | Canva | Social-Media-Posts, Ads |
| SEO / Content-Optimierung | Surfer SEO / Clearscope | SEO-Texte |
| Social-Media-Planung | Metricool / Later | Cross-Posting, Scheduling |

### 1.4 Daten, Tracking & Analyse

| Funktion | Tool | Zweck |
|---|---|---|
| Web-Analytics | Google Analytics 4 | Traffic, Conversions |
| Tag-Management | Google Tag Manager | Pixel, Events |
| Heatmaps | Hotjar / Microsoft Clarity | UX-Optimierung |
| Dashboard | Google Looker Studio / Notion | KPI-Überblick |

### 1.5 Kundenservice & Operations

| Funktion | Tool | Zweck |
|---|---|---|
| Helpdesk / Chat | Tidio / Intercom / Zendesk | Support-Automatisierung |
| FAQ / Wissensdatenbank | Notion / Help Scout | Selbstservice |
| Terminbuchung | Calendly / Acuity | Coachings, Beratungstermine |
| Dokumente / Verträge | DocuSign / HelloSign | PKV-Beratung, Einverständniserklärungen |

### 1.6 Affiliate & Partnerschaften

| Funktion | Tool | Zweck |
|---|---|---|
| Affiliate-Tracking | FirstPromoter / PartnerStack | Partnerprovisionen |
| Influencer-Management | AspireIQ / manuell | TikTok-Creator |
| Link-Management | Linktree / Bitly | Bio-Links, Tracking |

---

## 2. Kern-Workflows

### 2.1 Lead-Generierung-Workflow

```
Besucher kommt über Meta/TikTok/SEO
        ↓
Landingpage mit Gesundheits-Check
        ↓
Formular-Submit → ActiveCampaign Tag „Lead: Gesundheitscheck"
        ↓
Automatische Willkommens-E-Mail + PDF-Download
        ↓
Segmentierung nach Alter, Geschlecht, Score
        ↓
Start 10-Tage-Nurture-Flow
        ↓
Retargeting-Ads für Nicht-Öffner
```

**Automatisierung:** 95 % automatisch, 5 % manuell bei Support-Anfragen.

---

### 2.2 Sales-Conversion-Workflow

```
Lead öffnet 3+ E-Mails oder klickt auf Angebotslink
        ↓
Tag „Hot Lead" + Retargeting-Ads aktiviert
        ↓
Einladung Webinar / Erinnerung / Replay
        ↓
Angebots-E-Mail mit Countdown / Limited Offer
        ↓
Checkout-Zahlung → Stripe
        ↓
Willkommens-E-Mail + Onboarding-Flow
        ↓
Zugang zu Membership-Plattform
```

**Automatisierung:** 90 % automatisch, 10 % manuell bei Zahlungsproblemen.

---

### 2.3 Onboarding-Workflow

```
Kauf bestätigt
        ↓
Tag „Kunde: 12-Wochen-Programm"
        ↓
Willkommens-Video + Anleitung
        ↓
Tag 1: Programm-Start, Woche 1 freischalten
        ↓
Tag 3: Erste Check-in-E-Mail
        ↓
Wöchentlich: Neue Inhalte freischalten + Motivations-E-Mail
        ↓
Tag 30: Upsell Supplement-Abo
        ↓
Tag 60: Upsell Coaching oder PKV-Check
```

**Automatisierung:** 95 % automatisch.

---

### 2.4 Supplement-Abo-Workflow

```
Kunde kauft / abonniert Supplement
        ↓
Stripe-Subscription ausgelöst
        ↓
Bestellung an Fulfillment-Dienstleister / Lager
        ↓
Versandbenachrichtigung + Tracking
        ↓
Wöchentliche Erinnerung zur Einnahme
        ↓
Nach 30 Tagen: Feedback-E-Mail + Upsell-Cross-Sell
        ↓
Vor Ablauf: Erinnerung zur Verlängerung
```

**Automatisierung:** 90 % automatisch (Fulfillment ggf. extern).

---

### 2.5 PKV-Affiliate-Workflow

```
Kunde zeigt Interesse an PKV-Check
        ↓
Calendly-Terminbuchung mit Berater
        ↓
Vorab-Fragebogen (Einkommen, Beruf, aktuelle KV)
        ↓
Beratungsgespräch (manuell / lizenziert)
        ↓
Bei Abschluss: Provision ausgezahlt
        ↓
Follow-up-E-Mail mit Gesundheitsplan für PKV-Kunden
```

**Automatisierung:** 60 % automatisch, 40 % manuell (Beratung).

---

### 2.6 Content-Publikations-Workflow

```
Content-Idee → Redaktionsplan (Notion / Airtable)
        ↓
Produktion (Video / Text / Grafik)
        ↓
Review (Recht / Medizin / Marketing)
        ↓
Scheduling über Metricool / Later
        ↓
Veröffentlichung auf TikTok, Instagram, YouTube, Blog
        ↓
Performance-Tracking in Dashboard
        ↓
Woche 2/4: Repurposing (Blog → Video → Carousel)
```

**Automatisierung:** 70 % automatisch (Scheduling), 30 % manuell (Produktion, Review).

---

## 3. Integrationen

### Notwendige API-Verbindungen

| System A | System B | Zweck |
|---|---|---|
| ActiveCampaign | Stripe | Kauf-Trigger, Tags, Segmente |
| ActiveCampaign | Typeform | Quiz-Ergebnisse in CRM |
| Shopify/WooCommerce | Stripe | Zahlungen, Abos |
| Shopify | Fulfillment-Dienstleister | Versand |
| Meta Pixel | Landingpage | Conversion-Tracking |
| TikTok Pixel | Landingpage | Conversion-Tracking |
| GA4 | Alle Kanäle | Attribution |
| Zapier / Make | Diverse | Verbindung nicht nativer Tools |

---

## 4. Daten- und Privacy-Automatisierung

### DSGVO-Konformität

- Doppelte Opt-in-E-Mail-Bestätigung
- Einwilligungsmanagement mit Zeitstempel
- Gesundheitsdaten getrennt speichern, verschlüsselt
- Automatische Löschung nach Widerruf
- DSGVO-konformes Tracking (Consent-Mode v2)

### Tools
- Cookie-Banner: Usercentrics / Cookiebot
- Consent-Management: OneTrust / Usercentrics
- Datenschutz-Generator: eRecht24

---

## 5. Limits der Automatisierung

| Bereich | Automatisierbarkeit | Limit |
|---|---|---|
| Lead-Generierung | 95 % | Kreative Content-Produktion bleibt manuell |
| E-Mail-Nurturing | 95 % | Persönliche Anfragen brauchen Support |
| Verkauf | 90 % | Beratungsgespräche bei PKV manuell |
| Onboarding | 95 % | Technische Probleme brauchen Support |
| Coaching | 60 % | 1:1-Coaching erfordert Menschen |
| Medizinische Inhalte | 70 % | Review durch Experten notwendig |
| Kundenservice | 70 % | Komplexe Fälle brauchen Agenten |
| Fulfillment | 80 % | Qualitätskontrolle und Lager logistisch |

---

## 6. Kosten-Übersicht Tool-Stack (Monat)

| Tool | Geschätzte Kosten/Monat |
|---|---|
| ActiveCampaign | 50–150 € |
| Webflow / WordPress Hosting | 20–50 € |
| Shopify / WooCommerce | 30–100 € |
| Stripe Gebühren | 1,5–2,9 % Umsatz |
| Typeform | 25–50 € |
| Zoom / Livestorm | 20–100 € |
| Canva Pro | 12 € |
| Metricool / Later | 10–30 € |
| Hotjar | 0–40 € |
| Zapier / Make | 20–50 € |
| **Gesamt fix** | **ca. 200–700 €/Monat** |

---

## 7. Empfohlene Start-Architektur

Für die ersten 90 Tage reicht ein schlanker Stack:

1. **Webflow** für Landingpage
2. **ActiveCampaign** für E-Mail, CRM, Automation
3. **Typeform** für Gesundheits-Check
4. **Stripe** für Zahlungen
5. **Kajabi / Teachable** für Kursinhalte
6. **Meta + TikTok Ads** für Traffic
7. **GA4 + Tag Manager** für Tracking
8. **Notion** für Planung und Dokumentation

Diese Kombination ermöglicht einen voll automatisierten Funnel ab Lead bis Kauf mit überschaubaren Kosten.

---

*Hinweis: Tool-Auswahl sollte nach ersten Tests und Skalierung iterativ angepasst werden. Kosten sind Schätzungen basierend auf aktuellen Preisen.*
