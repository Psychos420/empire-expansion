# Automation-Plan: Reisen & Lifestyle 35+

## Ziel der Automation

Jeder wiederkehrende Prozess im Bereich Reisen & Lifestyle 35+ soll skalierbar und weitgehend automatisiert ablaufen. Der Fokus liegt auf:

- Lead-Generierung ohne manuellen Aufwand
- Personalisierung durch Daten
- Reduzierung administrativer Buchungsarbeit
- Content-Wiederverwendung und -Verteilung

---

## Tool-Stack

### Kategorie: Webseite & Landingpages

| Tool | Zweck | Kosten (ca.) |
|------|-------|--------------|
| **Carrd** | Einfache Landingpages für Quiz, Lookbook, Beratung | 19–49 USD/Jahr |
| **Webflow** | Größere Website mit CMS | 14–39 USD/Monat |
| **WordPress + Elementor** | Flexible Content-Website | Hosting ab 5 USD/Monat |

**Empfehlung MVP:** Carrd für Quiz und Lookbook, später Webflow oder WordPress für Content-SEO.

### Kategorie: Quiz & Lead-Erfassung

| Tool | Zweck | Kosten (ca.) |
|------|-------|--------------|
| **Typeform** | Hochwertiges Quiz-Erlebnis | 25–50 USD/Monat |
| **Tally** | Kostenlose Alternative, sehr flexibel | Kostenlos / Pro 29 USD/Monat |
| **Involve.me** | Quiz + Lead-Magnets + Payment | 25–75 USD/Monat |

**Empfehlung MVP:** Tally (kostenlos) oder Typeform für bessere UX.

### Kategorie: E-Mail-Marketing & Automation

| Tool | Zweck | Kosten (ca.) |
|------|-------|--------------|
| **MailerLite** | E-Mail-Automatisierung, Landingpages | Kostenlos bis 1.000 Abonnenten, dann ab 10 USD/Monat |
| **Brevo (ehemals Sendinblue)** | Automation + CRM + SMS | Kostenlos bis 300 Mails/Tag |
| **ConvertKit** | Creator-fokussiert, gute Automation | Ab 9 USD/Monat |

**Empfehlung MVP:** MailerLite für einfachen Einstieg und gute Automation.

### Kategorie: Zahlungen & digitale Produkte

| Tool | Zweck | Kosten (ca.) |
|------|-------|--------------|
| **Stripe** | Kreditkartenzahlungen | 1,5% + 0,25 EUR pro Transaktion |
| **PayPal** | Zahlungen, Vertrauensfaktor | 2,49% + 0,35 EUR |
| **Gumroad** | Digitale Produkte einfach verkaufen | 10% Gebühr |

**Empfehlung MVP:** Stripe für Direktverkäufe, PayPal als Alternative, Gumroad für schnelle digitale Produkte.

### Kategorie: Terminbuchung

| Tool | Zweck | Kosten (ca.) |
|------|-------|--------------|
| **Calendly** | Beratungsgespräche buchen | Kostenlos / Pro 10 USD/Monat |
| **TidyCal** | Einmalzahlung, lebenslang | 29 USD einmalig |

**Empfehlung MVP:** Calendly kostenlos, später TidyCal.

### Kategorie: Automation & Workflows

| Tool | Zweck | Kosten (ca.) |
|------|-------|--------------|
| **Make** | Visuelle Automation (Zapier-Alternative) | Kostenlos bis 1.000 Ops/Monat |
| **Zapier** | Breite Integrationen | Kostenlos bis 100 Tasks/Monat |
| **n8n** | Open-Source-Alternative, selbst hosten | Kostenlos (außer Hosting) |

**Empfehlung MVP:** Make für einfache Workflows, später n8n bei wachsender Komplexität.

### Kategorie: Content-Planung & Social Media

| Tool | Zweck | Kosten (ca.) |
|------|-------|--------------|
| **Notion** | Content-Kalender, Datenbanken, Dokumentation | Kostenlos / Plus 8 USD/Monat |
| **Buffer** | Social-Media-Planung | Kostenlos / Pro 6 USD/Kanal/Monat |
| **Later** | Instagram/Pinterest-Planung | Kostenlos / Starter 16,50 USD/Monat |

**Empfehlung MVP:** Notion für Planung, Buffer kostenlos für den Start.

### Kategorie: Analytics & Tracking

| Tool | Zweck | Kosten (ca.) |
|------|-------|--------------|
| **Google Analytics 4** | Website-Tracking | Kostenlos |
| **Google Search Console** | SEO-Monitoring | Kostenlos |
| **Meta Pixel** | Retargeting | Kostenlos |
| **Plausible** | Datenschutzfreundliches Tracking | 9 USD/Monat |

### Kategorie: CRM

| Tool | Zweck | Kosten (ca.) |
|------|-------|--------------|
| **Airtable** | Leads, Buchungen, Partnerdaten | Kostenlos / Plus 20 USD/Monat |
| **Notion** | Einfaches CRM | Kostenlos |
| **HubSpot CRM** | Professionelles CRM | Kostenlos / Starter 18 USD/Monat |

---

## Automations-Workflows

### Workflow 1: Quiz → Lead → E-Mail-Sequenz

```
Nutzer startet Quiz (Typeform/Tally)
    ↓
E-Mail-Adresse wird erfasst
    ↓
Ergebnis wird berechnet (Genuss, Aktiv, Kultur, Entschleuniger)
    ↓
Daten an MailerLite übergeben (Make/Zapier)
    ↓
Nutzer landet auf Ergebnisseite
    ↓
Willkommens-E-Mail mit Ergebnis + Lookbook
    ↓
Tag-basierte E-Mail-Sequenz startet
```

### Workflow 2: Blog-Traffic → Newsletter-Anmeldung

```
Blog-Artikel wird gelesen
    ↓
Inline-CTA oder Exit-Intent-Pop-up
    ↓
Anmeldung für wöchentlichen Newsletter
    ↓
Bestätigungsmail (Double Opt-in)
    ↓
Willkommenssequenz mit Top-Inhalten
    ↓
Regelmäßiger Newsletter
```

### Workflow 3: Kauf digitales Produkt

```
Nutzer kauft Lookbook (Stripe/Gumroad)
    ↓
Zahlung bestätigt
    ↓
PDF wird automatisch per E-Mail versendet
    ↓
Tag „Käufer Lookbook“ im E-Mail-Tool
    ↓
Cross-Sell-Sequenz startet (nächstes Lookbook, Online-Kurs)
```

### Workflow 4: Beratungsgespräch buchen

```
Nutzer klickt „Persönliche Beratung“
    ↓
Calendly-Formular öffnet sich
    ↓
Termin wird gebucht
    ↓
Bestätigungsmail + Erinnerung
    ↓
Zoom-Link wird versendet
    ↓
CRM-Eintrag wird erstellt (Airtable/Notion)
    ↓
Follow-up nach dem Gespräch
```

### Workflow 5: Content-Wiederverwendung

```
Langform-Blog-Artikel oder Podcast
    ↓
Teaser für Instagram + Pinterest
    ↓
Kurzclip für TikTok/Reels
    ↓
3–5 Newsletter-Snippets
    ↓
Zitate für LinkedIn/XING
    ↓
Alles im Content-Kalender dokumentiert
```

### Workflow 6: Affiliate-Buchung tracken

```
Nutzer klickt Affiliate-Link im Blog/Newsletter
    ↓
Tracking über Affiliate-Plattform (z. B. Awin, Travelpayouts)
    ↓
Buchung wird getätigt
    ↓
Provision wird gutgeschrieben
    ↓
Monatliche Auswertung in Notion/Airtable
```

---

## Limits und manuelle Eingriffe

### Was NICHT automatisiert werden sollte

| Prozess | Grund |
|---------|-------|
| **Persönliche Beratung bei Premium-Reisen** | Vertrauen und Individualität erfordern menschlichen Kontakt |
| **Content-Erstellung** | KI kann unterstützen, aber echte Erfahrungen und Stimme müssen menschlich sein |
| **Krisenkommunikation** | Bei Stornierungen, Unwetter, politischen Ereignissen muss ein Mensch entscheiden |
| **Partnerauswahl vor Ort** | Lokale Guides und Hotels müssen persönlich geprüft werden |
| **Beschwerden und Rückfragen** | Kundenservice sollte persönlich bleiben |

### Automations-Grenzen

- **E-Mail-Sequenzen** sollten alle 4–6 Wochen auf Performance geprüft werden.
- **Quiz-Ergebnisse** müssen regelmäßig an neue Angebote angepasst werden.
- **Affiliate-Links** sollten mindestens quartalsweise auf Verfügbarkeit geprüft werden.

---

## Kostenübersicht MVP-Stack (monatlich)

| Tool | Kosten/Monat |
|------|--------------|
| Carrd Pro | ~3 USD |
| Tally / Typeform | 0–25 USD |
| MailerLite | 0–10 USD |
| Make / Zapier | 0–9 USD |
| Calendly | 0 USD |
| Stripe | Transaktionsgebühren |
| Notion | 0 USD |
| Buffer | 0 USD |
| Google Analytics | 0 USD |
| **Gesamt** | **0–50 USD/Monat** |

---

## Fazit

Der Automation-Plan ermöglicht es, mit minimalem Budget und geringem manuellem Aufwand einen professionellen Funnel aufzubauen. Die **Kern-Automatisierung** besteht aus Quiz → E-Mail-Tool → personalisierte Sequenz. Alles andere baut darauf auf. Wichtig: Automation ersetzt nicht Vertrauen und Qualität – sie skaliert sie.
