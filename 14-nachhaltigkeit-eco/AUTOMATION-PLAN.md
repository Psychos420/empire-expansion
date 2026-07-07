# Automation-Plan: Nachhaltigkeit & Eco-Produkte

**Ziel:** Maximale Skalierung bei minimalem manuellem Aufwand. Alle wiederholbaren Prozesse werden durch Tools und Workflows automatisiert.

---

## 1. Übergeordneter Tool-Stack

| Bereich | Tool | Zweck |
|---|---|---|
| **Shop-System** | Shopify | E-Commerce-Plattform, Checkout, Produktdaten |
| **E-Mail-Marketing** | Klaviyo | Automations-Flows, Segmentierung, Newsletter |
| **Abo-Management** | Recharge oder Seal Subscriptions | Wiederkehrende Zahlungen, Abo-Steuerung |
| **Paid Ads** | Meta Ads Manager, Google Ads, TikTok Ads Manager | Traffic-Generierung |
| **Social Media Management** | Metricool oder Later | Planung, Cross-Posting, Analytics |
| **CRM / Projektmanagement** | Notion + Airtable | Wissen, Planung, Datenbanken |
| **Chatbot / Support** | Tidio oder Gorgias | Automatisierter Kundenservice |
| **Bewertungen** | Judge.me oder Loox | Social Proof, automatisierte Review-Anfragen |
| **Versand / Fulfillment** | Sendcloud oder Shippo | Versandlabels, Tracking, Retouren |
| **Dropshipping-Anbindung** | DSers, Syncee oder direkte API | Produktimport, Bestellweiterleitung |
| **Affiliate-Management** | Refersion oder UpPromote | Partnerprogramm, Provisionen |
| **Analytics** | Google Analytics 4, Triple Whale oder Northbeam | Attribution, Umsatztracking |
| **Zapier / Make** | Workflow-Automatisierung | Verbindung zwischen Tools |
| **Canva / CapCut** | Content-Erstellung | Bilder, Videos für Social Ads |

---

## 2. Automatisierte Workflows

### Workflow 1: Lead-Erfassung & E-Mail-Nurturing

**Trigger:** Nutzer lädt Lead-Magnet herunter oder meldet sich für Newsletter an.

**Ablauf:**
1. Shopify / Landing-Page erfasst E-Mail-Adresse.
2. Klaviyo fügt Kontakt zur Liste „Eco-Leads“ hinzu und taggt nach Interesse.
3. Automatische Willkommens-E-Mail mit PDF + Shop-Link.
4. 6-teilige Nurturing-Sequenz über 14 Tage:
   - Tag 2: Problem vertiefen
   - Tag 4: Lösung präsentieren
   - Tag 6: Social Proof
   - Tag 8: Produktvorstellung
   - Tag 11: Angebot/Rabatt
   - Tag 14: Letzter Call-to-Action
5. Nicht-Käufer wandern in Retargeting-Listen für Meta/TikTok/Google.

**Tools:** Shopify, Klaviyo, Meta Pixel, TikTok Pixel, Google Tag Manager.

---

### Workflow 2: Bestellabwicklung & Fulfillment

**Trigger:** Kunde bezahlt Bestellung.

**Ablauf:**
1. Shopify empfängt Zahlung.
2. Bestellung wird automatisch an Fulfillment-Partner oder Dropshipping-Lieferant weitergeleitet.
3. Versandlabel wird erstellt (Sendcloud/Shippo).
4. Tracking-E-Mail wird automatisch versendet.
5. Lieferstatus wird im Kundenkonto aktualisiert.
6. 7 Tage nach Lieferung: Automatische Review-Anfrage.

**Tools:** Shopify, Sendcloud/Shippo, DSers/Syncee, Klaviyo, Judge.me.

---

### Workflow 3: Abo-Management

**Trigger:** Kunde kauft Abo oder wandeln sich vom Einmalkauf zum Abo um.

**Ablauf:**
1. Recharge/Seal erstellt wiederkehrende Zahlung.
2. Klaviyo sendet Abo-Willkommens-E-Mail mit Verwaltungslink.
3. 3 Tage vor jeder Lieferung: Erinnerungs-E-Mail mit Inhalt/Verschiebe-Option.
4. Fehlgeschlagene Zahlung: Automatisierte Retry-Logik + E-Mail an Kunden.
5. Kündigung: Exit-Survey + Win-Back-Angebot (z. B. 20 % Rabatt für 3 Monate).

**Tools:** Recharge/Seal Subscriptions, Klaviyo.

---

### Workflow 4: Retention & Cross-Sell

**Trigger:** Kauf abgeschlossen.

**Ablauf:**
1. Tag 3: Nutzungstipps per E-Mail.
2. Tag 10: Impact-Update („Sie haben X g Plastik vermieden“).
3. Tag 21: Abo-Angebot mit 10 % Rabatt.
4. Tag 45: Cross-Sell-E-Mail passend zum gekauften Set.
5. Tag 90: Persönlicher Impact-Report + VIP-Produktangebot.

**Tools:** Klaviyo, Shopify, Custom Impact-Rechner.

---

### Workflow 5: Kundenservice-Automation

**Trigger:** Kunde stellt Frage per Chat/E-Mail.

**Ablauf:**
1. Chatbot beantwortet häufige Fragen automatisch (Versand, Abo, Rückgabe, Zertifikate).
2. Komplexe Anfragen werden an menschlichen Support weitergeleitet.
3. E-Mail-Vorlagen für Standardanfragen (Tracking, Retouren, Rechnungen).
4. Eskalation an Tier-2-Support bei Beschwerden oder Chargeback-Risiko.

**Tools:** Tidio/Gorgias, Klaviyo, Shopify.

---

### Workflow 6: Content-Produktion & Publishing

**Trigger:** Wöchentlicher Content-Plan.

**Ablauf:**
1. Canva/CapCut: Erstellung von Bildern und Videos aus Templates.
2. Metricool/Later: Planung und automatisches Posting auf Instagram, Facebook, Pinterest, TikTok.
3. Blog-Artikel werden aus bestehenden E-Mail- und Video-Inhalten adaptiert.
4. User-Generated Content wird automatisch gesammelt und freigegeben.

**Tools:** Canva, CapCut, Metricool, Later, Zapier.

---

### Workflow 7: Affiliate- & Influencer-Management

**Trigger:** Affiliate bewirbt Produkt.

**Ablauf:**
1. Refersion/UpPromote generiert individuelle Tracking-Links.
2. Affiliate-Partner erhält Marketing-Material (Bilder, Texte, Banner).
3. Verkäufe werden automatisch attributiert.
4. Provisionen werden monatlich berechnet und ausgezahlt.
5. Top-Affiliates erhalten automatisch VIP-Boni.

**Tools:** Refersion/UpPromote, Shopify, PayPal/Stripe.

---

### Workflow 8: Reporting & Controlling

**Trigger:** Täglich/Wöchentlich/Monatlich.

**Ablauf:**
1. Google Analytics 4 sammelt Website-Daten.
2. Triple Whale/Northbeam aggregiert Paid-Social-Daten.
3. Airtable/Notion-Dashboard zeigt KPIs:
   - Umsatz, CAC, ROAS, CLV, Abo-Anteil
   - Bestseller, Retourenquote, Support-Tickets
4. Wöchentlicher automatisierter Bericht per E-Mail an das Team.

**Tools:** Google Analytics 4, Triple Whale, Northbeam, Airtable, Notion, Zapier.

---

## 3. Limits & manuelle Eingriffspunkte

### Was NICHT automatisiert werden sollte

| Bereich | Grund |
|---|---|
| **Produktauswahl & Qualitätskontrolle** | Nachhaltigkeit muss geprüft werden; Automatisierung birgt Greenwashing-Risiko |
| **Kundenbeschwerden & Eskalationen** | Persönlicher Kontakt schafft Vertrauen |
| **Inhaltliche Claims & Zertifizierungen** | Green Claims Directive erfordert menschliche Prüfung |
| **Partnerschaften mit Lieferanten** | Verhandlungen und Audits erfordern persönliche Beziehungen |
| **Kreative Strategie** | Branding und Storytelling brauchen menschliche Ideen |

### Wichtige Kontrollpunkte

- **Wöchentlich:** Ad-Performance, E-Mail-Open-Rates, Support-Tickets
- **Monatlich:** Lieferanten-Qualität, Zertifikats-Überprüfung, Finanzbericht
- **Vierteljährlich:** Tool-Stack-Review, Automatisierungs-Effizienz, Compliance-Check

---

## 4. Skalierungs-Roadmap für Automation

| Phase | Zeitraum | Fokus |
|---|---|---|
| **Phase 1: Grundlagen** | Tag 1–30 | Shopify, Klaviyo, Meta Pixel, Google Analytics, Versand |
| **Phase 2: Abo & Retention** | Tag 31–60 | Recharge/Seal, Post-Purchase-Flows, Review-Automation |
| **Phase 3: Multi-Channel** | Tag 61–90 | TikTok Shop, Pinterest, Affiliate-Programm, Content-Planung |
| **Phase 4: Optimierung** | Monat 4–6 | Advanced Analytics, Personalisierung, B2B-Automatisierung |

---

## 5. Fazit

Automation ist das Rückgrat der Skalierung. Durch den Einsatz von Shopify, Klaviyo, Recharge und einer schlanken Zapier-/Make-Integration kann Empire Eco Essentials mit überschaubarem Team einen hohen Umsatz und eine starke Kundenbindung aufbauen. **Der Mensch bleibt bei strategischen Entscheidungen, Qualitätskontrolle und kreativer Markenführung zentral.**
