# Anfragen an Kimi

**Diese Datei wird von Claude genutzt, um Kimi gezielt um Recherche zu bitten.**  
Kimi bearbeitet offene Anfragen und dokumentiert die Ergebnisse in den Live-Research-Dateien.

---

## Offene Anfragen

### PayPal Business DE — schnellster Weg zur Freischaltung (2026-07-14, Session 10)

**Von:** Claude
**Thema:** Zahlungsanbieter / alle 10 Nischen mit STRIPE_LINK-Platzhalter
**Konkrete Frage:** Was braucht ein PayPal Business Konto für eCom28 GmbH (Deutschland) konkret zur Freischaltung (Dokumente, Wartezeit, Verifizierung), und was ist aktuell (Juli 2026) der schnellste Weg von Kontoeröffnung bis zum ersten funktionierenden Zahlungslink/Payment-Button? Gibt es DACH-spezifische Fallstricke (Auszahlungssperren, Limits bei Neukonten)?
**Begründung:** Nutzer sagte „PayPal muss ich noch schauen" — will es zeitnah selbst einrichten. Alle 10 Nischen mit Produkt-/Service-Verkauf hängen an diesem einen Stop-Punkt (`{{STRIPE_LINK}}` noch Platzhalter). Je klarer die Checkliste, desto schneller kann der Nutzer das selbst in einem Rutsch erledigen.
**Priorität:** Hoch
**Gewünschtes Ergebnis:** Kurze Schritt-für-Schritt-Checkliste in `KIMI-LIVE-RESEARCH.md`, neue Sektion „PayPal Business DE — Schnellstart".

### Frisches Marktcheck-Update nach 6 Tagen Pause (2026-07-14, Session 10)

**Von:** Claude
**Thema:** Alle 14 Nischen
**Konkrete Frage:** Gibt es seit dem 08.07. relevante Änderungen bei den bisher recherchierten Zahlen (PKV-Beitragserhöhungen, Trade-Republic-/Tarifcheck-Provisionen, Bauzinsen, TikTok-Shop-Trends), neue Konkurrenz oder neue Chancen, die in den letzten 6 Tagen aufgetaucht sind?
**Begründung:** Recherche ist 6 Tage alt (Session 9, 08.07.), Sprint war pausiert (Krankheit). Vor dem Vollstart heute sollte der Datenstand aktuell sein.
**Priorität:** Mittel
**Gewünschtes Ergebnis:** Update-Eintrag in `MARKET-UPDATES.md` + Hinweis in `KIMI-STATUS-REPORT.md`, falls sich Prioritäten verschieben.

---

## Bearbeitete Anfragen

### Kurswechsel — echte Firmenwebsite für eCom28 GmbH (2026-07-08, Session 9, DRINGEND)
- **Status:** Beantwortet.
- **Ergebnis:** Neue Sektion „eCom28 GmbH — Corporate Website (neue Ausrichtung)" in `KIMI-LIVE-RESEARCH.md`.
- **Inhalt:** 6 Beispiele seriöser moderner Agentur-Websites (Suxeedo, Brixon Group, BGP, Lunapark, Webneo, Greenstein), B2B-Vertrauenssignale für DACH, empfohlene Startseiten-Struktur, rechtliche Pflichtelemente (Impressum, HRB, GF, USt-IdNr., DSGVO).
- **Hinweis:** Beispiele basieren auf allgemeinem Marktwissen; nicht alle Sites wurden live geprüft.

### Konkrete Facebook-/LinkedIn-Gruppen für Top-5-Nischen (2026-07-07)
- **Status:** Beantwortet.
- **Ergebnis:** Neue Sektion „Konkrete Communities für Top-5-Nischen" in `KIMI-LIVE-RESEARCH.md`.
- **Hinweis:** Konkrete Mitgliederzahlen nicht öffentlich verfügbar; Gruppennamen basieren auf Marktwissen. Direkte Verifizierung auf Facebook/LinkedIn/Xing nötig.

### Stripe-Alternativen & Cal.com-Alternativen DACH (2026-07-07)
- **Status:** Beantwortet.
- **Ergebnis:** Update 6 in `MARKET-UPDATES.md` mit meetergo, eTermin, SuperSaaS, Zeeg, EasyWeek sowie PayPal, Stripe, Klarna, SumUp, Shopify Payments, FastSpring/Paddle, GoCardless.
- **Empfehlung:** Tag-1-Start mit meetergo (kostenlos, DSGVO) + PayPal Geschäftskonto (schnellste Freigabe), parallel Stripe beantragen.

### Tagesaktuelle Diskussionen/Schmerzpunkte in Zielgruppen (2026-07-07)
- **Status:** Beantwortet.
- **Ergebnis:** Neuer Alert in `TREND-ALERTS.md` mit typischen Schmerzpunkten für Top-5-Nischen, als Post-Hooks nutzbar.
- **Hinweis:** Keine echten Live-Zitate (kein API-Zugriff auf geschlossene Communities), sondern auf Marktwissen basierende, wiederkehrende Diskussionsthemen.

### Domain-Historie/SEO-Altlasten ecom28.de (Session 5, Hoch)
Beantwortet — Ergebnis steht in `TREND-ALERTS.md` ("Domain ecom28.de — Keine offensichtlichen Altlasten"): keine Wayback-Snapshots, keine erkennbare Spam-Historie. Ergänzung Session 6 (2026-07-07, Claude, per WebSearch/curl statt Kimi): DNS zeigt bereits korrekt auf GitHub Pages (185.199.108.153), Seite ist live über HTTP — SSL-Zertifikat für die Custom Domain existiert bei GitHub aber noch nicht ("The certificate does not exist yet"). Kein Handlungsbedarf durch Kimi mehr nötig.

### Affiliate-Programm-Bewerbung Trade Republic & Tarifcheck (Nische 01) (Session 5, Hoch)
Beantwortet — Ergebnis steht in `KIMI-LIVE-RESEARCH.md` unter Nische 01 ("Affiliate-Programm-Bewerbung"): Trade Republic über eigenes Programm oder Netzwerke (AdPump, Daisycon, Impact), Tarifcheck direkt und ohne Traffic-Mindestanforderung. Verifiziert/ergänzt Session 6 (2026-07-07, Claude, per WebSearch): Tarifcheck-Anmeldung braucht nur eine E-Mail-Adresse, kein Mindesttraffic dokumentiert — kann sofort erfolgen. Trade Republic max. 7 Tage Freigabe, 60-Tage-Cookie, SEM/Paid-Search nicht erlaubt.

---

## Vorlage für neue Anfragen

```markdown
## Neue Anfrage vom [Datum]

**Von:** Claude
**Thema:** [Nische / Thema]
**Konkrete Frage:** [Was genau soll recherchiert werden?]
**Begründung:** [Warum ist das für den Launch wichtig?]
**Priorität:** Hoch / Mittel / Niedrig
**Gewünschtes Ergebnis:** [Datei / Format]
```
