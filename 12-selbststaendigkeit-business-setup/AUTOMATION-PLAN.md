# Automation-Plan: Selbstständigkeit & Business Setup

**Ziel:** Wiederkehrende, standardisierbare Prozesse weitgehend automatisieren, damit Empire-Expansion skalieren kann, ohne proportional mehr Personal einzustellen.

**Prinzip:** Menschliche Beratung dort, wo es zählt (Strategie, Positionierung, komplexe Entscheidungen). Automation bei repetitiven, regelbasierten Aufgaben (Onboarding, Dokumente, Erinnerungen, Datenübertragung).

---

## 1. Tool-Stack

### 1.1 Kern-Plattformen

| Kategorie | Tool | Zweck |
|-----------|------|-------|
| **Automation-Engine** | n8n (self-hosted) | Komplexe Workflows, KI-Integration, Datensouveränität, niedrige Kosten |
| **Fallback Automation** | Make | Visuelle Workflows, schnellere Einrichtung für einfache Prozesse |
| **E-Mail-Marketing** | ConvertKit / ActiveCampaign | Lead-Nurturing, Newsletter, Kampagnen |
| **CRM** | HubSpot Free / Pipedrive | Kundenverwaltung, Pipeline, Verkaufsautomatisierung |
| **Kundenportal / Projektmanagement** | Notion / ClickUp | Dokumentation, Aufgaben, Kundenzugang |
| **Terminbuchung** | Calendly | Strategie-Calls, Onboarding, Check-ins |
| **Zahlungen** | Stripe | Einmalzahlungen, Abonnements, Ratenzahlungen |
| **Kommunikation** | Slack + Loom | Interne Kommunikation, asynchrone Video-Updates |
| **Dokumente & Verträge** | PandaDoc | Angebote, Verträge, E-Signatur |
| **KI-Assistenten** | OpenAI API / Claude API | Textgenerierung, Businesspläne, E-Mail-Entwürfe |

### 1.2 Sekundäre Tools

| Kategorie | Tool | Zweck |
|-----------|------|-------|
| Website / Landingpages | Webflow / WordPress | Content, Conversion |
| SEO | Ahrefs / SurferSEO | Keyword-Recherche, Content-Optimierung |
| Social Media | Taplio / AuthoredUp | LinkedIn-Planung, Analyse |
| Webinar | Zoom Webinar / Livestorm | Lead-Generierung |
| Analytics | Google Analytics 4 + Looker Studio | Tracking, Dashboards |
| Formulare | Typeform / Tally | Lead-Erfassung, Onboarding |
| Cloud-Speicher | Google Drive / Dropbox | Dokumentenaustausch |

---

## 2. Workflows

### 2.1 Lead-Generierung & Capture

**Trigger:** Besucher gibt E-Mail auf Landingpage ein.

**Workflow:**
1. Formular-Submission → CRM-Eintrag mit Tag „Lead-Magnet: [Name]“
2. E-Mail-Adresse an ConvertKit/ActiveCampaign übergeben
3. Willkommens-E-Mail mit Lead-Magnet senden
4. Tagging basierend auf Lead-Quelle (LinkedIn, Google Ads, Blog etc.)
5. Lead-Score erhöhen bei Klicks/Öffnungen
6. Benachrichtigung an Sales-Team bei hohem Score

**Automation-Tool:** n8n + ConvertKit + HubSpot

---

### 2.2 E-Mail-Nurturing

**Trigger:** Neuer Lead triggert Welcome-Sequence.

**Workflow:**
1. Tag-basierte Sequenz starten (z. B. 35+ Berater vs. Nebenerwerbsgründer)
2. Zeitgesteuerte E-Mails versenden
3. Bei Klick auf Webinar-Link → Tag „Webinar-Interessent“
4. Bei Buchung Strategie-Call → Sequenz pausieren, Tag „Hot Lead“
5. Bei Nicht-Öffnung nach 30 Tagen → Re-Engagement-Campaign

**Automation-Tool:** ConvertKit / ActiveCampaign

---

### 2.3 Webinar-Registrierung & Follow-up

**Trigger:** Registrierung für Webinar.

**Workflow:**
1. CRM-Eintrag + Kalendereintrag
2. Bestätigungs-E-Mail mit Zoom-Link
3. Erinnerungs-E-Mails (24h, 1h vor Beginn)
4. Nach Webinar:
   - Anwesende → Replay + Angebots-E-Mail
   - Nicht-Anwesende → Replay + neuer Terminvorschlag
5. Alle Registrierten → 7-Tage-Follow-up-Sequence

**Automation-Tool:** Zoom + ConvertKit + n8n

---

### 2.4 Terminbuchung & Strategie-Call-Vorbereitung

**Trigger:** Terminbuchung über Calendly.

**Workflow:**
1. CRM-Eintrag aktualisieren / anlegen
2. Kalendereinladung an Kunden und Berater
3. Erinnerung 24h und 1h vor Termin
4. Fragebogen an Kunden senden (Vorab-Informationen)
5. Nach Termin: automatische Danke-E-Mail + Angebot (falls verkauft)

**Automation-Tool:** Calendly + HubSpot + PandaDoc + n8n

---

### 2.5 Verkauf & Angebot

**Trigger:** Strategie-Call als „gewonnen“ markiert.

**Workflow:**
1. Angebot aus Template in PandaDoc generieren
2. E-Mail mit Angebot an Kunden senden
3. Erinnerung nach 3 Tagen bei nicht unterschriebenem Angebot
4. Nach Unterschrift: Zahlungslink (Stripe) versenden
5. Nach Zahlungseingang: Onboarding-Workflow starten
6. Rechnung automatisch erstellen (Buchhaltungssoftware)

**Automation-Tool:** HubSpot + PandaDoc + Stripe + n8n + Buchhaltungssoftware

---

### 2.6 Kunden-Onboarding

**Trigger:** Zahlungseingang bestätigt.

**Workflow:**
1. Willkommens-E-Mail mit Zugangsdaten zum Kundenportal
2. Onboarding-Formular senden
3. Kick-off-Termin automatisch buchen
4. Notion-/ClickUp-Projekt aus Template duplizieren
5. Aufgaben an Kunden und Berater zuweisen
6. Erinnerungen bei nicht erledigten Aufgaben

**Automation-Tool:** Stripe + Notion/ClickUp + Calendly + n8n

---

### 2.7 Projekt-Durchführung

**Trigger:** Meilenstein erreicht / fällig.

**Workflow:**
1. Wöchentliche Status-E-Mail an Kunden
2. Erinnerung an anstehende Check-in-Termine
3. Automatische Erstellung von Status-Reports
4. Dokumente in Kundenordner ablegen
5. Bei Verzögerung: Eskalation an Projektleiter

**Automation-Tool:** ClickUp/Notion + n8n + E-Mail

---

### 2.8 Inhaltsproduktion (Content Engine)

**Trigger:** Wöchentlich / monatlich.

**Workflow:**
1. KI generiert Blog-Artikel-Entwurf aus Keyword
2. Redakteur prüft und finalisiert
3. Aus Blog-Artikel automatisch:
   - LinkedIn-Post generieren
   - Newsletter-Text extrahieren
   - YouTube-Skript-Idee ableiten
4. Veröffentlichung planen
5. Performance-Tracking

**Automation-Tool:** OpenAI/Claude API + n8n + Buffer/Taplio

---

### 2.9 Buchhaltungs-Exporte

**Trigger:** Monatlich / bei Zahlungseingang.

**Workflow:**
1. Stripe-Zahlungen sammeln
2. Rechnungen generieren
3. Belege in Buchhaltungssoftware (z. B. lexoffice, sevDesk) importieren
4. Monatlichen Umsatz-Report an Geschäftsführung senden

**Automation-Tool:** Stripe + n8n + Buchhaltungssoftware

---

### 2.10 Empfehlungsprogramm

**Trigger:** Kunde erfolgreich abgeschlossen.

**Workflow:**
1. Automatische Anfrage für Case Study / Testimonial
2. Empfehlungslink generieren
3. Belohnung bei erfolgreicher Vermittlung auszahlen
4. Danke-E-Mail und Update über Prämienstand

**Automation-Tool:** HubSpot + n8n + Stripe/PayPal

---

## 3. KI-Einsatz im Automation-Plan

| Anwendungsfall | KI-Tool | Nutzen |
|----------------|---------|--------|
| Businessplan-Entwürfe | Claude / GPT-4 | Reduziert Erstellungszeit von Stunden auf Minuten |
| E-Mail-Entwürfe | Claude / GPT-4 | Personalisierte Sequenzen schneller erstellen |
| Angebotsvorlagen | Claude / GPT-4 | Branchenspezifische Vorlagen generieren |
| LinkedIn-Content | Claude + Taplio | Ideen und Entwürfe automatisch |
| Kundenanfragen beantworten | GPT-4 basierter Chatbot | 24/7 Erstlevel-Support |
| Meeting-Notizen | Otter.ai / Fireflies | Automatische Zusammenfassungen |
| Dokumentenprüfung | KI-gestützte Tools | Erste Prüfung von Onboarding-Formularen |

---

## 4. Limits & Menschliche Kontrollpunkte

### Was NIEMALS automatisiert wird

1. **Rechtsberatung:** Rechtsform-Empfehlungen müssen von qualifizierten Beratern / Kooperationspartnern erfolgen. Empire gibt Orientierung, keine Rechtsberatung.
2. **Steuerberatung:** Steuerliche Empfehlungen durch Steuerberater-Partner.
3. **Individuelle Positionierung:** Jede Positionierung erfordert menschliche Strategie-Session.
4. **Verkaufsgespräche:** Hochpreisige Pakete (4.900 €+) werden persönlich verkauft.
5. **Komplexe Kundenkonflikte:** Eskalationen werden persönlich gelöst.

### Menschliche Kontrollpunkte

| Prozessschritt | Menschliche Aufgabe |
|----------------|---------------------|
| Strategie-Call | Beratung, Verkauf, Positionierung |
| Angebotserstellung | Freigabe, Anpassung |
| Kick-off | Persönliche Beziehung aufbauen |
| Positionierung | Strategie-Workshop |
| Website-Launch | Qualitätskontrolle |
| Rechtsform-Empfehlung | Durch Kooperationspartner |
| Abschluss-Call | Testimonial-Anfrage, Upsell |

---

## 5. Kosten- und Skalierbarkeitsbetrachtung

### Geschätzte monatliche Tool-Kosten (Startphase)

| Tool | Kosten/Monat |
|------|-------------|
| n8n (self-hosted auf Hetzner) | ca. 15–30 € |
| Make (Fallback) | ca. 10–50 € |
| ConvertKit / ActiveCampaign | ca. 30–100 € |
| HubSpot Free / Pipedrive | 0–50 € |
| Calendly | ca. 10–20 € |
| Notion / ClickUp | ca. 10–20 € |
| PandaDoc | ca. 20–50 € |
| OpenAI API | ca. 50–200 € |
| Webflow / WordPress Hosting | ca. 20–50 € |
| Zoom Webinar | ca. 60–150 € |
| **Gesamt** | **ca. 225–720 €/Monat** |

*Hinweis: Kosten steigen mit Anzahl der Kontakte und Workflows. In der Startphase sind die unteren Werte realistisch.*

### Skalierungseffekt

| Phase | Kunden/Monat | Automation-Anteil | Personalbedarf |
|-------|-------------|-------------------|----------------|
| Start | 3–5 | 60 % | 1–2 Personen |
| Wachstum | 10–20 | 75 % | 2–3 Personen |
| Skala | 30–50 | 85 % | 4–6 Personen |
| Scale | 100+ | 90 % | 8–12 Personen |

---

## 6. Sicherheit & Compliance

### Datenschutz

- Selbst-gehostete n8n-Instanz auf Hetzner (Serverstandort Deutschland / EU)
- DSGVO-konforme E-Mail-Tools
- Auftragsverarbeitungsverträge (AVV) mit allen Tools
- Keine Weitergabe von Kundendaten an KI ohne Einwilligung

### Datensicherheit

- Zugänge mit 2FA
- Regelmäßige Backups der Workflows und Kundendaten
- Zugriffsrechte rollenbasiert
- Logging kritischer Automatisierungen

---

## 7. Zusammenfassung

Der Automation-Plan ermöglicht es Empire-Expansion, **mehr Kunden bei gleichbleibender Qualität zu bedienen**. Die Architektur ist so gebaut, dass menschliche Expertise dort eingesetzt wird, wo sie den größten Mehrwert schafft – bei Strategie, Beratung und komplexen Entscheidungen. Alles andere läuft über automatisierte Workflows.

**Top-3-Automatisierungen für den sofortigen Start:**
1. Lead-Capture + Welcome-Sequence
2. Terminbuchung + Call-Vorbereitung
3. Onboarding-Workflow nach Zahlungseingang
