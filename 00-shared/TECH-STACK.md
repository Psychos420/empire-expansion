# Empire Expansion — Einheitlicher Tech-Stack

Dieses Dokument definiert den gemeinsamen Tech-Stack für alle 14 Expansionsbereiche. Entscheidungen sind bewusst konkret getroffen, um Zeit zu sparen und Synergien zu ermöglichen. Alternativen sind nur dann aufgeführt, wenn sie für einen bestimmten Bereich deutlich besser passen.

---

## Übersicht

| Funktion | Primärempfehlung | Alternative | Schätzkosten/Monat |
|---|---|---|---|
| Landing Pages | **Carrd** (schnell) / **Webflow** (skalierbar) | Framer, WordPress + Elementor, Shopify | 19–39 € |
| E-Mail/SMS/WhatsApp Marketing | **Brevo** | ActiveCampaign, Klaviyo, Mailchimp | 0–50 € |
| CRM & Funnel | **GoHighLevel** | HubSpot, Pipedrive | 97–297 $ |
| Automation | **n8n** (self-hosted via Docker) | Make, Zapier | 0–20 € |
| Zahlungen | **Stripe** + **PayPal** | Gumroad, Payhip | Transaktionsgebühren |
| Analytics | **Google Analytics 4** + **Looker Studio** | Plausible, PostHog | 0 € |
| Hosting/Domains | **Cloudflare** (DNS) + **Hetzner** (Server) | Vercel, Netlify, Hostinger | 5–15 € |
| KI-Assistenten | **Kimi** / **Claude** | OpenAI API, Perplexity | 20–100 € |
| Design/Assets | **Figma** + **Canva Pro** | Adobe Express, Penpot | 0–15 € |

---

## 1. Landing Pages

**Zweck:** Lead-Magnet-Seiten, Sales Pages, Waitlist-Seiten und Micro-Sites für alle Bereiche.

**Empfehlung:**
- **Carrd** für schnelle 1-Seiten-Landing-Pages und Lead-Magnet-Seiten.
- **Webflow** für skalierbare, SEO-freundliche Bereichs-Websites.

**Warum:** Carrd ist schnell, günstig und ausreichend für die meisten Funnels. Webflow bietet mehr Designkontrolle und CMS-Funktionen, wenn ein Bereich langfristig wächst.

**Alternativen:**
- **Framer:** Gute Wahl, wenn Design-First-Ansatz und interaktive Prototypen wichtig sind.
- **WordPress + Elementor:** Nur wenn bestehende WP-Infrastruktur vorhanden ist.
- **Shopify:** Für E-Commerce-Bereiche (TikTok Shop, Dropshipping) notwendig.

**Kosten:**
- Carrd Pro Standard: ~19 $/Jahr (nicht pro Monat).
- Webflow Basic Site: ~18 $/Monat.

**Einrichtungsschritte:**
1. Account bei Carrd/Webflow erstellen.
2. Domain bei Cloudflare verwalten und verbinden.
3. Template aus `LANDING-PAGE-TEMPLATE.md` kopieren.
4. Formular mit Brevo oder GoHighLevel verbinden.
5. Conversion-Tracking (GA4 + Meta Pixel) einbauen.

---

## 2. E-Mail / SMS / WhatsApp Marketing

**Zweck:** Lead-Nurturing, Follow-ups, Broadcasts, Automation-Sequenzen und Newsletter.

**Empfehlung:** **Brevo**

**Warum:** Gute DSGVO-Compliance (EU-Server), integriertes SMS, faires Preismodell für kleine Listen, gute Automation.

**Alternativen:**
- **ActiveCampaign:** Stärker im CRM und Automation, aber teurer.
- **Klaviyo:** Beste Wahl für E-Commerce (TikTok Shop, Dropshipping).
- **Mailchimp:** Einfach, aber teuer bei Wachstum und weniger flexibel.
- **WhatsApp Business API:** Über Brevo, GoHighLevel oder Twilio/360dialog.

**Kosten:**
- Brevo Starter: 0 €/Monat bis 300 Kontakte/Tag E-Mails.
- Brevo Business: ~20 €/Monat für wachsende Listen.

**Einrichtungsschritte:**
1. Brevo-Account anlegen, Domain authentifizieren (SPF, DKIM, DMARC).
2. Listen pro Bereich anlegen (z. B. `01-affiliate`, `05-pkv-leads`).
3. Double-Opt-In-Formulare erstellen.
4. Willkommens-Sequenz aus `EMAIL-SEQUENCE-TEMPLATE.md` importieren.
5. Webhook für n8n einrichten (siehe `AUTOMATION-ORCHESTRATION.md`).

---

## 3. CRM

**Zweck:** Kontaktverwaltung, Pipeline-Tracking, Terminbuchung, Verkaufsautomatisierung.

**Empfehlung:** **GoHighLevel**

**Warum:** All-in-One für CRM, Funnel, E-Mail/SMS, Terminbuchung und White-Label-Agentur. Ideal, wenn mehrere Bereiche und später Agenturkunden verwaltet werden.

**Alternativen:**
- **HubSpot:** Sehr mächtig, aber teuer bei Skalierung.
- **Pipedrive:** Reinrassiges Sales-CRM, günstig, aber ohne Marketing-Features.

**Kosten:**
- GoHighLevel Starter: 97 $/Monat.
- GoHighLevel Unlimited: 297 $/Monat (für mehrere Sub-Accounts).

**Einrichtungsschritte:**
1. Account anlegen, eigene Domain verbinden.
2. Pro Bereich einen Sub-Account oder eine Pipeline anlegen.
3. Lead-Formulare, Terminbuchungskalender und SMS-Follow-ups konfigurieren.
4. Mit n8n verbinden für Cross-Bereich-Orchestrierung.
5. Benutzerdefinierte Felder für Bereichs-Tagging erstellen.

---

## 4. Automation

**Zweck:** Workflows zwischen Tools, Datenfluss zwischen Bereichen, Trigger-Logik, Reporting.

**Empfehlung:** **n8n** (self-hosted)

**Warum:** Open Source, sehr günstig, DSGVO-konform hostbar, extrem leistungsfähig. Keine Limits bei Workflow-Anzahl oder Ausführungen wie bei SaaS-Alternativen.

**Alternativen:**
- **Make:** Visuell sehr intuitiv, gute Wahl für schnelle Prototypen.
- **Zapier:** Einfach, aber teuer bei vielen Zaps und hohem Volumen.

**Kosten:**
- n8n self-hosted auf Hetzner/VPS: ~5 €/Monat Server.
- n8n Cloud: ab ~20 €/Monat.

**Einrichtungsschritte:**
1. n8n via Docker auf Hetzner/VPS installieren oder n8n Cloud nutzen.
2. Credentials für Brevo, GoHighLevel, Google Sheets, Stripe hinterlegen.
3. Zentralen Lead-Eingangs-Workflow bauen (siehe `AUTOMATION-ORCHESTRATION.md`).
4. Pro Bereich Trigger-Workflows anlegen.
5. Webhook-URLs in Landing Pages und Formularen hinterlegen.

---

## 5. Zahlungen

**Zweck:** Low-Ticket-Produkte (PDFs, Guides, Templates), Abos, Dienstleistungsrechnungen.

**Empfehlung:** **Stripe** + **PayPal**

**Warum:** Stripe ist der Standard für digitale Produkte und Abos. PayPal erhöht Conversion bei der Zielgruppe 35+ deutlich.

**Alternativen:**
- **Gumroad:** Einfach für digitale Produkte, höhere Gebühren.
- **Payhip:** Gut für Downloads und Memberships.
- **GoHighLevel Payments:** Integrierte Zahlungen, praktisch für Agentur/Termin-Modelle.

**Kosten:**
- Stripe: 1,5 % + 0,25 € pro Transaktion (EU-Karten).
- PayPal: 2,49 % + 0,35 € pro Transaktion.

**Einrichtungsschritte:**
1. Stripe-Account verifizieren (Geschäftsdaten, Bankkonto).
2. Produkte/Preise anlegen (einmalig oder wiederkehrend).
3. Checkout-Links oder eingebettete Stripe-Checkout-Formulare auf Landing Pages integrieren.
4. PayPal als zusätzliche Zahlungsmethode anbieten.
5. Webhook an n8n senden für Käufer-Automation.

---

## 6. Analytics

**Zweck:** Traffic-Tracking, Conversion-Messung, Kanalperformance, Berichte.

**Empfehlung:** **Google Analytics 4** + **Looker Studio**

**Warum:** Kostenlos, tief integriert mit Google Ads, einfach zu teilen. Looker Studio für übersichtliche Dashboards.

**Alternativen:**
- **Plausible:** Datenschutzfreundlich, einfach, aber weniger tief.
- **PostHog:** Produkt-Analytics, gut für Apps und Web-Apps.

**Kosten:**
- GA4: 0 €.
- Looker Studio: 0 €.

**Einrichtungsschritte:**
1. GA4-Property pro Bereich oder einer zentralen Property mit benutzerdefinierten Ereignissen.
2. Ereignisse für Lead, Kauf, Terminbuchung etc. einrichten.
3. Meta Pixel / LinkedIn Insight Tag ergänzen.
4. Looker Studio-Dashboard mit GA4, Sheets und Stripe-Daten verbinden.
5. Wöchentliches Reporting nach `KPI-DASHBOARD.md`.

---

## 7. Hosting / Domains

**Zweck:** Domains verwalten, DNS, Server für n8n und zukünftige Web-Apps.

**Empfehlung:** **Cloudflare** (DNS/CDN/Security) + **Hetzner** (Server)

**Warum:** Cloudflare bietet kostenlosen DNS, DDoS-Schutz und schnelles CDN. Hetzner ist kostengünstig und DSGVO-konform für self-hosted Tools.

**Alternativen:**
- **Vercel / Netlify:** Hervorragend für Web-Apps und statische Seiten.
- **Hostinger:** Günstige All-in-One-Hosting-Pakete.

**Kosten:**
- Cloudflare: 0 € (Free Plan).
- Hetzner CX11: ~5 €/Monat.

**Einrichtungsschritte:**
1. Domains bei einem Registrar kaufen (z. B. Namecheap, Hetzner, Cloudflare Registrar).
2. Nameserver auf Cloudflare umstellen.
3. DNS-Einträge für Landing Pages, n8n, Web-Apps setzen.
4. Server bei Hetzner bestellen, Docker installieren.
5. SSL/TLS auf „Full (strict)“ in Cloudflare stellen.

---

## 8. KI-Assistenten

**Zweck:** Content-Erstellung, Recherche, Copywriting, Code, Ideen, Analyse.

**Empfehlung:** **Kimi** + **Claude**

**Warum:** Beide sind stark im deutschen Sprachraum, bei langen Kontexten und bei komplexen Anweisungen. Kimi besonders gut für lange Dokumente und Code-Claude für präzise, sichere Ausgaben.

**Alternativen:**
- **OpenAI API (GPT-4o / o3-mini):** Für automatisierte Workflows über API.
- **Perplexity:** Für Recherche und Quellenangaben.

**Kosten:**
- Kimi Pro: ~20 $/Monat.
- Claude Pro: ~20 $/Monat.
- OpenAI API: nutzungsbasiert.

**Einrichtungsschritte:**
1. Abos für Kimi und Claude einrichten.
2. Pro Bereich eigene Projekte/Threads anlegen.
3. Wichtige Prompt-Templates in Notion oder direkt in `00-shared` dokumentieren.
4. API-Keys für automatisierte Workflows (OpenAI) in n8n hinterlegen.

---

## 9. Design / Assets

**Zweck:** Visuelle Gestaltung von Landing Pages, E-Mails, Social-Media-Content, Lead-Magneten.

**Empfehlung:** **Figma** + **Canva Pro**

**Warum:** Figma für UI/UX-Design und komplexe Layouts, Canva für schnelle Social-Media-Grafiken und PDF-Lead-Magneten.

**Alternativen:**
- **Adobe Express:** Gute Canva-Alternative im Adobe-Ökosystem.
- **Penpot:** Open-Source-Figma-Alternative.

**Kosten:**
- Figma: 0 € (Starter) / 12 $/Monat (Professional).
- Canva Pro: ~15 €/Monat.

**Einrichtungsschritte:**
1. Figma-Team für Empire Expansion anlegen.
2. Gemeinsame Design-Bibliothek (Farben, Typografie, Komponenten) aufbauen.
3. Canva Pro-Team einrichten, Markenkit hinterlegen.
4. Vorlagen für Social Posts, E-Mail-Header, PDF-Cover erstellen.

---

## Tech-Stack-Entscheidungsmatrix

| Wenn du das brauchst... | Nutze das |
|---|---|
| Schnell eine Landing Page live | Carrd |
| Skalierbare SEO-Website | Webflow |
| E-Mail-Listen + Automation | Brevo |
| CRM + Terminbuchung + SMS | GoHighLevel |
| Automation zwischen allen Tools | n8n |
| Digitale Zahlungen | Stripe + PayPal |
| Auswertung und Dashboards | GA4 + Looker Studio |
| Domains + DNS + Sicherheit | Cloudflare |
| Server für self-hosted Tools | Hetzner |
| Content und Copy | Kimi / Claude |
| Design und Assets | Figma + Canva |

---

## Minimaler Start-Stack (Monat 1)

Für den Start reichen diese Tools:

1. **Carrd** — Landing Pages
2. **Brevo** — E-Mail-Marketing
3. **n8n Cloud / self-hosted** — Automation
4. **Stripe + PayPal** — Zahlungen
5. **GA4 + Looker Studio** — Analytics
6. **Kimi / Claude** — Content & Copy
7. **Canva Pro** — Grafiken und PDFs

Gesamtkosten: **ca. 50–100 €/Monat** bei geringem Volumen.

---

## Skalierungs-Stack (ab Monat 3)

Wenn erste Umsätze fließen und mehrere Bereiche parallel laufen:

1. **Webflow** — für größere Bereichs-Websites
2. **GoHighLevel** — CRM + Funnel + SMS
3. **n8n self-hosted** — umfangreiche Workflows
4. **Klaviyo** — für E-Commerce-Bereiche
5. **Figma Professional** — Design-System
6. **Hetzner + Cloudflare** — Hosting-Infrastruktur
