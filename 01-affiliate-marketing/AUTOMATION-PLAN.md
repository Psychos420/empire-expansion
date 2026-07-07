# Automationsplan: Affiliate Marketing für 35+

## Grundphilosophie

> **Menschliche Strategie + KI-gestützte Ausführung = Skalierbarkeit ohne Qualitätsverlust.**

Wir automatisieren alles, was repetitiv, datenbasiert und skalierbar ist. Strategie, juristische Prüfung und kreative Richtung bleiben beim Menschen.

---

## Was lässt sich automatisieren?

| Bereich | Automatisierbarkeit | Werkzeuge |
|---------|---------------------|-----------|
| **Content-Recherche & Ideenfindung** | 80 % | Claude/Kimi, Perplexity, Ahrefs/SEMrush API |
| **Content-Erstellung (Erstentwürfte)** | 70 % | Claude API, ChatGPT, Jasper |
| **SEO-Optimierung (Meta, Struktur)** | 75 % | Surfer SEO, RankMath, Claude |
| **Link-Management & Tracking** | 90 % | n8n/Make, Affiliate-Netzwerk-APIs, UTM-Builder |
| **Lead-Capture & CRM** | 85 % | ActiveCampaign/Brevo, n8n, HubSpot CRM |
| **E-Mail/SMS/WhatsApp Follow-ups** | 90 % | ActiveCampaign, Brevo, n8n |
| **Social Media Publishing** | 80 % | Metricool, Buffer, n8n |
| **Content-Repurposing** | 75 % | OpusClip, HeyGen, Canva, n8n |
| **Reporting & Analytics** | 90 % | Google Sheets, Looker Studio, n8n |
| **Kundenbetreuung (FAQ)** | 60 % | Chatbot (n8n + Claude) |

---

## Empfohlener Tool-Stack

### Core-Stack (Monat 1–3)

| Funktion | Tool | Warum? | Kosten (geschätzt) |
|----------|------|--------|--------------------|
| **CMS** | WordPress + Kadence/GeneratePress | Flexibel, SEO-freundlich, volle Kontrolle | 10–20 €/Monat |
| **E-Mail-Marketing** | ActiveCampaign oder Brevo | Automation, Tagging, CRM-Integration | 20–50 €/Monat |
| **Automation** | n8n (self-hosted auf Hetzner) | Kostenlos, DSGVO-freundlich, extrem flexibel | 5–15 €/Monat Server |
| **KI-Texte** | Claude API + Kimi | Beste deutsche Textqualität | 20–100 €/Monat |
| **SEO-Recherche** | Ahrefs oder Ubersuggest | Keyword-Recherche, Wettbewerbsanalyse | 30–100 €/Monat |
| **Analytics** | Google Analytics 4 + Looker Studio | Kostenlos, mächtig | Kostenlos |
| **Cloud-Speicher/CRM** | Airtable oder Notion | Datenbanken, Content-Planung | 0–20 €/Monat |

### Erweiterter Stack (Monat 4–12)

| Funktion | Tool | Einsatz |
|----------|------|---------|
| **Social Publishing** | Metricool oder Buffer | Planung über alle Kanäle |
| **Video-Repurposing** | OpusClip | Long-Form-Video → Shorts |
| **Bilder & Grafiken** | Canva Pro + KI-Bildtools | Thumbnails, Social Grafiken |
| **Avatar/Video-KI** | HeyGen (optional) | Skalierbare Video-Produktion |
| **SMS/WhatsApp** | Brevo oder MessageBird | Hochpreisige Nischen |
| **Affiliate-Netzwerke** | Awin, financeAds, Adcell | Programme & Tracking |

---

## Konkrete Workflows

### Workflow 1: Content-Ideen-Pipeline

**Ziel:** Jede Woche neue, datenbasierte Content-Ideen generieren.

```
1. Trigger: Wöchentlich (z. B. Sonntag 18 Uhr)
2. n8n holt Daten:
   - Ahrefs: Keywords mit niedrigem KD, hohem Volumen
   - Google Trends: Trendthemen in DACH
   - Wettbewerber-Websites: Neue Artikel (RSS/Scraping)
3. Claude API analysiert Daten und schlägt 10 Content-Ideen vor.
4. Mensch wählt 3–5 Ideen aus und priorisiert.
5. n8n schreibt Ideen in Airtable/Notion Content-Kalender.
```

**Menschlicher Eingriff:** Auswahl, Priorisierung, kreative Richtung.

---

### Workflow 2: SEO-Artikel-Produktion

**Ziel:** Vom Keyword bis zum veröffentlichten Erstentwurf in unter 60 Minuten.

```
1. Trigger: Neue Zeile in Content-Kalender
2. n8n liest Keyword, Zielgruppe, Nische.
3. Perplexity/Claude recherchiert aktuelle Fakten.
4. Claude API erstellt:
   - Artikel-Outline
   - Erstentwurf (1.500–2.500 Wörter)
   - Meta-Titel & Meta-Beschreibung
   - FAQ-Block
   - Social-Snippets
5. Mensch prüft Fakten, fügt Erfahrung/Stimme hinzu, ergänzt Affiliate-Links.
6. n8n publiziert Entwurf in WordPress.
```

**Menschlicher Eingriff:** Faktencheck, Affiliate-Link-Einbindung, Feinschliff.

---

### Workflow 3: Lead-to-Customer Nurturing

**Ziel:** Jeder Lead erhält die richtige Sequenz zum richtigen Zeitpunkt.

```
1. Trigger: Neuer Newsletter-Subscriber (z. B. über Landingpage)
2. n8n erfasst Lead in ActiveCampaign/Brevo.
3. Tagging basierend auf Lead-Magnet/Quiz-Ergebnis:
   - „PKV-Interesse"
   - „ETF-Interesse"
   - „SmartHome-Interesse"
4. Automation startet passende E-Mail-Sequenz (7–21 Tage).
5. Bei Link-Klicks: Lead-Score erhöhen, ggf. SMS/WhatsApp-Follow-up.
6. Bei Affiliate-Link-Klick ohne Sale: Retargeting-Audience aktualisieren.
7. Bei Sale: Bestätigungs-E-Mail, Cross-Sell-Sequenz starten.
```

**Menschlicher Eingriff:** Sequenz-Strategie, Copy-Optimierung, A/B-Test-Ideen.

---

### Workflow 4: Social-Repurposing

**Ziel:** Aus einem Long-Form-Content werden automatisch mehrere Social-Snippets.

```
1. Trigger: Neuer Blog-Artikel oder YouTube-Video veröffentlicht
2. n8n extrahiert Key Takeaways (Claude API).
3. Erstellung von:
   - 5 Twitter/X-Posts
   - 3 LinkedIn-Posts
   - 2 Instagram-Captions
   - 1 TikTok/Reels-Script
4. Canva-Integration erstellt passende Grafiken (optional).
5. OpusClip schneidet YouTube-Video in Shorts (optional).
6. Metricool/Buffer veröffentlicht Posts nach Plan.
```

**Menschlicher Eingriff:** Finale Freigabe, Thumbnail-Auswahl, Anpassung an Plattform.

---

### Workflow 5: Affiliate-Link-Management & Reporting

**Ziel:** Immer aktuelle Links, transparente Umsatzübersicht.

```
1. Trigger: Täglich (n8n Scheduler)
2. n8n prüft Affiliate-Links auf Verfügbarkeit (HTTP-Status).
3. Falls Link tot: Benachrichtigung an Mensch.
4. n8n holt Umsatzdaten aus:
   - Awin API
   - financeAds API
   - Amazon Associates API
   - Direkte Partner-Dashboards (ggf. per Scraping)
5. Daten werden in Google Sheets/Airtable aggregiert.
6. Looker Dashboard aktualisiert sich automatisch.
7. Wöchentlicher Report per E-Mail.
```

**Menschlicher Eingriff:** Reaktion auf tote Links, Strategieentscheidungen basierend auf Daten.

---

### Workflow 6: Kundenbetreuung / FAQ-Chatbot

**Ziel:** Häufige Fragen automatisch beantworten, Mensch nur bei komplexen Fällen einschalten.

```
1. Trigger: Nutzer stellt Frage (Website-Chat, WhatsApp, E-Mail)
2. Claude API analysiert Frage und beantwortet anhand Knowledge Base.
3. Falls Konfidenz < 80 %: Ticket an Mensch.
4. Bei Finanz-/Rechtsfragen: Automatischer Hinweis „Keine Beratung, bitte Fachberater konsultieren."
5. Antwort wird gesendet.
```

**Menschlicher Eingriff:** Komplexe Fragen, Beschwerden, Rechtsfragen.

---

## Tool-Auswahl-Entscheidungen

### n8n vs. Make vs. Zapier

| Kriterium | n8n | Make | Zapier |
|-----------|-----|------|--------|
| Kosten | Kostenlos self-hosted | Ab 9 €/Monat | Ab 19,99 $/Monat |
| DSGVO | Self-Hosting möglich | Cloud-only | Cloud-only |
| Flexibilität | Sehr hoch (Code-Nodes) | Hoch | Mittel |
| Lernkurve | Mittel-hoch | Mittel | Niedrig |
| KI-Integration | Hervorragend | Gut | Gut |
| Skalierbarkeit | Sehr hoch | Hoch | Hoch |

**Empfehlung:** n8n (self-hosted auf Hetzner) als Hauptautomationstool. Für schnelle Integrationen ohne Server-Aufwand kann Make als Backup dienen.

### ActiveCampaign vs. Brevo

| Kriterium | ActiveCampaign | Brevo |
|-----------|----------------|-------|
| Automation | Sehr stark | Stark |
| CRM | Integriert | Grundlegend |
| Preis | Ab 29 €/Monat | Ab 0 €/Monat (limits) |
| SMS/WhatsApp | Zusatzmodul | Integriert |
| Einfachheit | Mittel | Hoch |

**Empfehlung:** Start mit **Brevo** (kostenlos bis 300 E-Mails/Tag, gute Automation). Wechsel zu ActiveCampaign/HubSpot, wenn Liste > 5.000 und komplexe Scoring-Workflows nötig sind.

---

## Was bleibt menschlich?

| Aufgabe | Warum menschlich? |
|---------|-------------------|
| **Strategie & Positionierung** | Marktverständnis, Risikoabwägung |
| **Rechtliche Prüfung** | UWG, DSGVO, GewO — keine Automation |
| **Faktencheck Finanz-/Gesundheitscontent** | Fehler können teuer sein |
| **Kreative Richtung & Stimme** | Markenpersönlichkeit muss authentisch sein |
| **Partnerschaftsverhandlungen** | Direkte Deals, Sonderkonditionen |
| **Community-Moderation** | Vertrauensaufbau, Konfliktlösung |
| **A/B-Test-Analyse & Entscheidung** | Kontextverständnis über Zahlen hinaus |

---

## Limits & Risiken der Automation

| Limit | Risiko | Gegenmaßnahme |
|-------|--------|---------------|
| KI-Halluzinationen | Falsche Fakten im Content | Menschlicher Faktencheck |
| Over-Automation | unpersönliche Kommunikation | Personalisierung, menschliche Fallbacks |
| DSGVO-Verstöße | Datenweitergabe ohne Grundlage | Klare Prozesse, Datenschutzerklärung |
| Tool-Abhängigkeit | Preiserhöhungen/Abschaltungen | Daten-Exporte, Backups |
| Compliance bei Finanzcontent | Abmahnungen | Rechtsprüfung vor Veröffentlichung |

---

## Zielbild: Automation-Anteil nach 12 Monaten

| Bereich | Ziel-Automation |
|---------|-----------------|
| Content-Recherche | 80 % |
| Erstentwürfe | 70 % |
| Link-Management | 90 % |
| Lead-Capture | 90 % |
| E-Mail-Nurturing | 90 % |
| Social Publishing | 80 % |
| Reporting | 95 % |
| FAQ-Bot | 60 % |

---

## Fazit

Automation ist der entscheidende Wettbewerbsvorteil. Mit **n8n, Claude API und einem schlanken E-Mail-Tool** können wir ein Affiliate-Geschäft betreiben, das einem Team von 3–4 Personen entspricht — aber mit einem Bruchteil des Aufwands. Der Mensch bleibt für Strategie, Qualität und Compliance verantwortlich.
