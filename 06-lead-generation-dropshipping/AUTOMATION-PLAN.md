# Automation-Plan: Dropshipping für 35+

## Grundsatz

> **Automatisiere alles, was repetitiv, regelbasiert und skalierbar ist. Beherrsche manuell, was Vertrauen, Compliance und strategische Entscheidungen erfordert.**

Dieser Plan zeigt, welche Teile des Dropshipping-Geschäfts mit KI-Agenten (Kimi/Claude) und No-Code-/Low-Code-Tools (n8n, Make, Zapier) automatisiert werden können und wo Menschen unverzichtbar bleiben.

---

## Was lässt sich automatisieren?

| Bereich | Automatisierbarkeit | Tools |
|---|---|---|
| **Produktrecherche & Trendscouting** | Hoch | Kimi/Claude, Minea, AutoDS, PiPiADS, Exploding Topics |
| **Content-Erstellung (Text)** | Hoch | Kimi/Claude, Copy.ai, Jasper |
| **Content-Erstellung (Bild/Video)** | Mittel-hoch | Canva, Midjourney, Runway, CapCut, VidAU |
| **Shop-Einrichtung & Produktlistings** | Hoch | Shopify CSV-Import, AutoDS, DSers |
| **Preis- & Bestandsüberwachung** | Hoch | Prisync, Droppoint, AutoDS, n8n |
| **Bestellabwicklung & Tracking** | Hoch | Shopify + Lieferanten-API, n8n/Make/Zapier |
| **E-Mail-Marketing & Follow-ups** | Hoch | Klaviyo, Brevo, ActiveCampaign |
| **SMS / WhatsApp-Follow-ups** | Hoch | Brevo, Trengo, SleekFlow, n8n |
| **Warenkorb-Abbruch-Recovery** | Hoch | Klaviyo/Brevo + n8n |
| **Kundenservice (Level 1)** | Mittel-hoch | Kimi/Claude-Chatbot, Tidio, Gorgias, Zendesk AI |
| **Bewertungsanfragen** | Hoch | Automatisierte Review-Requests via E-Mail/SMS |
| **Reporting & Dashboards** | Hoch | Google Sheets, Looker Studio, n8n, Supermetrics |
| **Retouren-Management** | Mittel | Retourenportal, automatisierte Labels, manuelle Prüfung |
| **Compliance-Checks** | Mittel | Checklisten, automatisierte Dokumentenablage, manuelle Freigabe |

---

## Konkreter Tool-Stack

### Layer 1: KI-Agenten & Generative KI

| Aufgabe | Tool | Nutzen |
|---|---|---|
| Strategie, Copywriting, Analyse | **Kimi / Claude** | Berichte, E-Mail-Sequenzen, Anzeigentexte, Produktbeschreibungen |
| Bildgenerierung | **Midjourney / DALL-E / Canva AI** | Hero-Bilder, Social-Media-Grafiken |
| Videobearbeitung | **CapCut / Runway / VidAU** | UGC-Stil-Videos, automatische Untertitel |
| Chatbot / Kundenservice | **Claude API / OpenAI API** | Automatisierte Antworten auf häufige Fragen |

### Layer 2: E-Commerce & Shop-System

| Tool | Funktion |
|---|---|
| **Shopify** | Onlineshop, Checkout, Produktmanagement |
| **PageFly / GemPages** | Landing Pages |
| **Klaviyo / Brevo** | E-Mail- & SMS-Marketing |
| **Tidio / Gorgias / Zendesk** | Kundenservice-Chat |

### Layer 3: Sourcing & Fulfillment

| Tool | Funktion |
|---|---|
| **Spocket / BigBuy / Syncee** | EU-Lieferanten, schneller Import |
| **AutoDS / DSers** | Produktimport, Preis-/Bestandsüberwachung, Bestellautomatisierung |
| **CJ Dropshipping** | Fulfillment, Warehousing |

### Layer 4: Automation & Workflows

| Tool | Beste für | Kosten |
|---|---|---|
| **n8n** | Komplexe Workflows, Self-Hosting, Datenschutz, Kostenkontrolle | Kostenlos (Self-Hosted) / ab ca. EUR 20 (Cloud) |
| **Make (ehem. Integromat)** | Visuelle, komplexe Workflows, gute Shopify-Integration | ab ca. EUR 9/Monat |
| **Zapier** | Einfache Integrationen, große App-Bibliothek, schneller Start | ab ca. EUR 20/Monat |

> Empfehlung für Empire-Expansion: **n8n (Self-Hosted)** als primärer Automation-Engine, ergänzt durch **Make** für schnelle Shopify-Integrationen und **Zapier** nur für spezielle Apps ohne n8n-Node.

### Layer 5: Tracking & Reporting

| Tool | Funktion |
|---|---|
| **Google Analytics 4** | Website-Tracking, E-Commerce-Events |
| **Meta Pixel + CAPI** | Social-Ads-Tracking |
| **Looker Studio** | Dashboards, Reporting |
| **Google Sheets / Airtable** | Datenbanken, Listen, manuelle Übersichten |

---

## Konkrete Workflows

### Workflow 1: Lead-Magnet-Download → E-Mail-Sequenz

```
Landing Page Formular (Shopify / PageFly)
    ↓
Klaviyo / Brevo (Tag + Segment)
    ↓
Automatische Willkommens-E-Mail + PDF-Anhang/Link
    ↓
n8n: Prüfe Interesse (Schlaf/Rücken/Ergonomie)
    ↓
Trigger passende 7-Tage-Sequenz
    ↓
Tagging: „Lead – Schlaf“ oder „Lead – Rücken“
```

**Menschliche Kontrolle:** Strategie der Sequenz, Analyse der Öffnungsraten, Anpassung der Creatives.

### Workflow 2: Warenkorb-Abbruch → E-Mail + SMS

```
Shopify: Warenkorb abgebrochen
    ↓
n8n / Klaviyo: Warte 1 Stunde
    ↓
E-Mail 1: „Haben Sie eine Frage zu Ihrem Schlaf-Set?"
    ↓
Warte 23 Stunden
    ↓
E-Mail 2: „10 % Rabatt für die nächsten 24 Stunden"
    ↓
Optional: SMS/WhatsApp nach 6 Stunden
    ↓
Wenn Kauf: Stoppe Sequenz
```

**Menschliche Kontrolle:** Rabatt-Höhe, Inhalt der SMS, Analyse der Recovery-Rate.

### Workflow 3: Bestellung → Lieferant → Tracking

```
Shopify: Neue Bestellung
    ↓
Zahlung bestätigt
    ↓
AutoDS / n8n: Bestellung an Lieferanten-API weiterleiten
    ↓
Lieferant: Versandbestätigung + Tracking-Nummer
    ↓
n8n: Tracking-Nummer in Shopify aktualisieren
    ↓
Automatische Versand-E-Mail an Kunden
    ↓
SMS/WhatsApp: „Ihr Paket ist unterwegs“
    ↓
Nach 7 Tagen: Review-Request-E-Mail
```

**Menschliche Kontrolle:** Lieferanten-Qualität, Eskalation bei Problemen, Tracking-Fehler.

### Workflow 4: Preis- & Bestandsüberwachung

```
AutoDS / Prisync: Täglicher Scan
    ↓
Preisänderung oder Out-of-Stock erkannt
    ↓
n8n: Benachrichtigung an Slack/E-Mail
    ↓
Automatische Preisanpassung in Shopify (optional, mit Limits)
    ↓
Produkt auf „nicht verfügbar“ setzen, wenn Lieferant out of stock
```

**Menschliche Kontrolle:** Preislimits, Margenschutz, strategische Preisentscheidungen.

### Workflow 5: Content-Produktion

```
Kimi/Claude: Recherchiere Keyword/Thema
    ↓
Kimi/Claude: Schreibe Blog-Artikel / Ad-Copy / E-Mail
    ↓
Canva / Midjourney: Erstelle passendes Bild
    ↓
n8n: Veröffentliche Blog-Artikel in Shopify
    ↓
Meta Business Suite / Buffer: Plane Social-Media-Posts
    ↓
Google Sheets: Dokumentiere Content-Kalender
```

**Menschliche Kontrolle:** Faktenprüfung, Markenstimme, Compliance (z. B. bei Gesundheitsaussagen), Freigabe.

### Workflow 6: Kundenservice-Chatbot (Level 1)

```
Kunde stellt Frage (Tidio / Gorgias / Zendesk)
    ↓
KI-Chatbot (Claude API) prüft Wissensdatenbank
    ↓
Wenn Antwort vorhanden: Automatische Antwort
    ↓
Wenn nicht: Ticket an Mensch, priorisiert
    ↓
KI schlägt dem Agenten Antwortentwurf vor
```

**Menschliche Kontrolle:** Training der Wissensdatenbank, Eskalationen, komplexe Beschwerden.

---

## Was bleibt menschlich?

| Bereich | Warum menschlich? |
|---|---|
| **Strategie & Nischenwahl** | Marktgefühl, Risikoabwägung, langfristige Entscheidungen |
| **Lieferantenauswahl & Qualitätskontrolle** | Vertrauensaufbau, physische Produktprüfung |
| **Komplexer Kundenservice** | Beschwerden, Retouren-Probleme, individuelle Beratung |
| **Compliance & Recht** | Steuerberater, Rechtsanwalt, GPSR-Prüfung |
| **Kreative Strategie** | Branding, Storytelling, große Kampagnenideen |
| **Budget-Entscheidungen** | Ad-Spend-Steuerung, Skalierung |
| **Partnerschaften & Verhandlungen** | Lieferanten, Influencer, Kooperationen |

---

## Datenschutz & Compliance bei Automation

- **n8n Self-Hosted** für sensitive Kundendaten bevorzugen.
- **DSGVO-konforme E-Mail- und SMS-Tools** nutzen (Double-Opt-in, Einwilligungsmanagement).
- **Keine Kundendaten an öffentliche KI-APIs ohne Pseudonymisierung** weitergeben.
- **Automatisierte Löschung** von Daten nach Widerruf / Ablauf der Speicherfrist.
- **Dokumentation aller automatisierter Verarbeitungen** im Verzeichnis.

---

## Kosten-Übersicht Tool-Stack (geschätzt)

| Tool | Kosten/Monat |
|---|---|
| Shopify | EUR 36 |
| Klaviyo / Brevo | EUR 30–60 |
| n8n Self-Hosted | EUR 0–20 (Server) |
| Canva Pro | EUR 12 |
| AutoDS / Spocket | EUR 30–50 |
| Kundenservice-Tool | EUR 20–50 |
| Tracking / Analytics | EUR 0–30 |
| **Gesamt** | **ca. EUR 150–300/Monat** |

---

## Fazit

Die Automatisierung ist das Rückgrat der Skalierung. Mit einem Stack aus **Kimi/Claude, Shopify, n8n, Klaviyo/Brevo und AutoDS** lässt sich der Großteil des operativen Geschäfts automatisieren. Der Mensch konzentriert sich auf Strategie, Qualität, Kreativität und Compliance – genau die Bereiche, die den Unterschied für Kunden 35+ ausmachen.
