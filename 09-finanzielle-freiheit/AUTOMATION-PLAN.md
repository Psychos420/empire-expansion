# Automation-Plan: Finanzielle Freiheit / Vermögensaufbau / FIRE

**Ziel:** Möglichst viele Prozesse automatisieren, um Skalierung bei gleichzeitig hoher Qualität und Compliance zu ermöglichen.

---

## 1. Grundsatz: Automatisierbare vs. menschliche Prozesse

### Automatisierbar (hoher ROI)
- Lead-Generierung und E-Mail-Nurturing
- Kurszugang und Onboarding
- Terminbuchung für Webinare/Coaching
- Zahlungsabwicklung und Rechnungsstellung
- Affiliate-Tracking und Auszahlungen
- Content-Veröffentlichung
- Social-Media-Recycling
- Reporting und KPI-Dashboards

### Menschlich notwendig (niedriger ROI bei Automatisierung)
- Live-Q&A und Coaching
- Komplexe individuelle Finanzfragen
- Content-Erstellung (zumindest der Kern)
- Community-Moderation (zunächst)
- Partnerbeziehungen und Verhandlungen
- Strategische Entscheidungen

---

## 2. Tool-Stack

### 2.1 Marketing & Funnel

| Funktion | Tool | Alternativen | Kosten/Monat (ca.) |
|---|---|---|---|
| E-Mail-Marketing | **ConvertKit** | ActiveCampaign, Brevo | 29–79 EUR |
| Landing Pages | **Carrd** | Webflow, Unbounce | 19–49 EUR |
| Webseite | **Webflow** | WordPress, Ghost | 29–79 EUR |
| Formulare | **Tally** | Typeform, Jotform | 0–29 EUR |
| Webinar | **Zoom Webinar** | Livestorm, WebinarJam | 79–149 EUR |
| SEO-Tools | **Ahrefs** | Ubersuggest, SE Ranking | 99–199 EUR |
| Social-Media-Planung | **Metricool** | Buffer, Hootsuite | 0–49 EUR |
| Design | **Canva Pro** | Adobe Express | 12 EUR |

### 2.2 Produkte & Kurse

| Funktion | Tool | Alternativen | Kosten/Monat (ca.) |
|---|---|---|---|
| Kursplattform | **Teachable** | Thinkific, Podia, Kajabi | 39–119 EUR |
| Community | **Circle** | Skool, Discord, Mighty Networks | 39–99 EUR |
| Coaching-Termine | **Calendly** | Acuity, TidyCal | 0–16 EUR |
| Dateien/Assets | **Notion** | Google Drive, Dropbox | 0–18 EUR |

### 2.3 Zahlungen & Finanzen

| Funktion | Tool | Alternativen | Kosten/Monat (ca.) |
|---|---|---|---|
| Zahlungsabwicklung | **Stripe** | PayPal, Mollie | Transaktionsgebühren |
| Affiliate-Tracking | **Rewardful** | FirstPromoter, Tapfiliate | 29–79 EUR |
| Buchhaltung | ** lexoffice** | sevDesk, Fastbill | 20–40 EUR |
| Rechnungen | Stripe + lexoffice | PayPal, sevDesk | 0–20 EUR |

### 2.4 Tools & Apps (Entwicklung)

| Funktion | Tool | Alternativen | Kosten/Monat (ca.) |
|---|---|---|---|
| No-Code-App | **Bubble** | FlutterFlow, Softr | 29–129 EUR |
| Datenbank | **Supabase** | Firebase, Airtable | 0–25 EUR |
| Automation | **Make** | Zapier, n8n | 0–16 EUR |
| Analytics | **Plausible** | Google Analytics 4 | 9 EUR |
| Heatmaps | **Microsoft Clarity** | Hotjar | Kostenlos |

### 2.5 KI-Assistenz

| Funktion | Tool | Einsatzzweck |
|---|---|---|
| Content-Erstellung | Claude / ChatGPT | E-Mail-Entwürfe, Blog-Outlines, Social Posts |
| Video-Editing | Descript | Schnitt, Untertitel, Clips |
| Thumbnails | Canva + KI | YouTube-Thumbnails |
| Transkription | Whisper / Descript | Podcast-/Video-Transkription |
| Recherche | Perplexity / WebSearch | Marktdaten, Wettbewerber |

---

## 3. Automatisierte Workflows

### Workflow 1: Lead-zu-Kunde (vollautomatisch)

```
Besucher klickt auf Lead Magnet
        ↓
Landing Page (Carrd)
        ↓
E-Mail-Formular (ConvertKit)
        ↓
Doppeltes Opt-in + Segmentierung
        ↓
Welcome-Sequence (7 E-Mails)
        ↓
Tripwire-Angebot (97-EUR-Kurs)
        ↓
Kauf → Stripe → Teachable-Zugang
        ↓
Onboarding-Sequence
        ↓
Upsell-Core-Offer (497 EUR)
```

**Automation-Tool:** ConvertKit Automation + Stripe + Teachable + Make (für erweiterte Logik)

### Workflow 2: Content-Produktion und Verbreitung

```
YouTube-Video produzieren
        ↓
Descript erstellt Clips + Untertitel
        ↓
Canva erstellt Thumbnails / Quote-Cards
        ↓
Metricool plant Posts für LinkedIn, YouTube Shorts, Instagram
        ↓
Blog-Artikel aus Transkript generieren (KI)
        ↓
E-Mail-Newsletter senden
```

**Ziel:** Ein Video = 5+ Content-Assets.

### Workflow 3: Webinar-Funnel

```
Registrierung über Landing Page
        ↓
Reminder-E-Mails (T-1, T-2h, T-15min)
        ↓
Webinar-Durchführung (Zoom)
        ↓
Replay-E-Mail (48h verfügbar)
        ↓
Angebot mit Countdown-Timer
        ↓
Follow-up-Sequence für Nicht-Käufer
```

### Workflow 4: Kunden-Onboarding

```
Kaufbestätigung
        ↓
Zugangsdaten zu Teachable + Circle
        ↓
Willkommens-E-Mail mit Roadmap
        ↓
Tag-basierte Erinnerungen (Modul 1, Modul 2...)
        ↓
Automatisierte Umfrage nach 14 Tagen
        ↓
Zertifikat / Abschluss-E-Mail
        ↓
Upsell-Sequenz
```

### Workflow 5: Affiliate-Provisionen

```
Partner erhält Tracking-Link (Rewardful)
        ↓
Klick + Cookie (30–60 Tage)
        ↓
Kauf über Stripe
        ↓
Provision automatisch berechnet
        ↓
Auszahlung monatlich/sechsmonatlich
        ↓
Dashboard für Partner
```

---

## 4. Technische Architektur (MVP)

```
[Website / Landing Pages]     → Webflow / Carrd
           ↓
[Forms / Lead Capture]        → ConvertKit / Tally
           ↓
[E-Mail Automation]           → ConvertKit
           ↓
[Payment & Invoicing]         → Stripe + lexoffice
           ↓
[Course Delivery]             → Teachable
           ↓
[Community]                   → Circle
           ↓
[Affiliate]                   → Rewardful
           ↓
[Analytics]                   → Plausible + Google Sheets Dashboard
```

**Geschätzte monatliche Tool-Kosten MVP:** 250–400 EUR/Monat.

---

## 5. Skalierungs-Architektur (Langfristig)

```
[Empire Wealth Dashboard]     → Bubble / FlutterFlow + Supabase
           ↓
[APIs zu Brokern]             → CSV-Import zuerst, später APIs
           ↓
[User Accounts]               → Supabase Auth
           ↓
[Kursplattform]               → Eigenentwicklung oder Teachable
           ↓
[Community]                   → Circle / Eigenentwicklung
           ↓
[Payment]                     → Stripe
           ↓
[Affiliate]                   → Rewardful / Eigenentwicklung
           ↓
[Automation]                  → Make / n8n
           ↓
[AI-Assistant]                → Claude API für Finanzfragen (Bildung)
```

---

## 6. Limits und Risiken der Automation

### 6.1 Compliance-Limits
- **Keine automatisierte Anlageberatung:** KI oder Automation dürfen keine personalisierten Anlageempfehlungen geben.
- **Haftungsausschluss:** Jeder automatisierte Content muss den Haftungsausschluss enthalten.
- **Datenschutz:** Keine Speicherung sensibler Finanzdaten ohne Einwilligung und Verschlüsselung.
- **Affiliate-Kennzeichnung:** Automatisierte E-Mails mit Affiliate-Links müssen als Werbung gekennzeichnet sein.

### 6.2 Qualitäts-Limits
- KI-generierte Inhalte müssen geprüft werden.
- Community-Moderation erfordert menschliche Aufsicht.
- Live-Events (Q&A, Coaching) lassen sich nicht vollständig automatisieren.

### 6.3 Technische Limits
- Broker-APIs im DACH-Raum sind oft eingeschränkt oder kostenpflichtig.
- CSV-Import ist zunächst akzeptabel, aber langfristig weniger attraktiv.
- Hohe Nutzerzahlen erfordern später eigenes Hosting.

---

## 7. Automation-Roadmap

| Phase | Zeitraum | Fokus |
|---|---|---|
| **MVP** | 0–30 Tage | E-Mail-Funnel, Landing Page, Kurszugang |
| **Skalierung** | 30–90 Tage | Webinar-Automation, Affiliate-Tracking, Content-Recycling |
| **Optimierung** | 90–180 Tage | A/B-Tests, Segmentierung, Advanced Analytics |
| **Produkt-Erweiterung** | 180+ Tage | Empire Wealth Dashboard, KI-Assistant, API-Integrationen |

---

## 8. Geschätzte Einsparungen durch Automation

| Prozess | Manueller Aufwand/Woche | Automatisierter Aufwand/Woche | Einsparung |
|---|---|---|---|
| Lead-Nurturing | 10h | 1h | 90 % |
| Kurs-Onboarding | 5h | 0,5h | 90 % |
| Content-Verbreitung | 8h | 2h | 75 % |
| Rechnungsstellung | 3h | 0,5h | 83 % |
| Affiliate-Tracking | 4h | 0,5h | 88 % |
| Reporting | 2h | 0,5h | 75 % |

**Gesamteinsparung:** ca. 25 Stunden/Woche bei Vollautomatisierung.
