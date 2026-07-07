# Zero-Budget-Launch: Schlaf & Erholung (SchlafKlar)

Ziel: diese Woche live gehen, ohne einen Euro auszugeben. Paid Ads, Testbestellungen, Shopify Basic & Co. kommen erst, wenn Umsatz aus dem Ökosystem finanziert.

---

## 1. Sofort einsatzbereit (kein Zutun nötig)

| Datei | Status |
|---|---|
| `landing-page.html` | Fertige, responsive Landing Page: Hero, Lead-Formular, Problem/Benefits, Produktvorschau, Trust-Signale, Testimonials, FAQ, finaler CTA. Kann direkt gehostet werden. **Einzige offene Stelle:** `action="{{FORM_ACTION}}"` im `<form>` – Platzhalter muss durch die echte Brevo-Formular-URL ersetzt werden (siehe Abschnitt 3). |
| `EMAIL-SEQUENCE.md` | 5 E-Mails (Tag 0–5) + 3-teiliger Warenkorb-Abbruch-Flow + SMS/WhatsApp-Varianten + Segmentierungsregeln – vollständig ausformuliert, copy-paste-fertig für Brevo. |
| `LEAD-MAGNET.md` | Titel, Struktur und vollständiger Text für alle 15 Seiten des PDF-Guides „Besser schlafen in 7 Tagen" final. Nur noch Layout (Canva, kostenlos) fehlt – kein Copy-Aufwand mehr. |
| `STORE-CONCEPT.md` | Marke *SchlafKlar*, USP, Zielgruppe, 10-Produkt-Sortiment mit VK/EK/Marge final entschieden. |
| `SUPPLIER-RESEARCH.md` | Anforderungskatalog, Kontakt-E-Mail-Vorlage, Lieferanten-Bewertungs-Template und 5 konkrete Rechercheansätze fertig – direkt nutzbar. |
| `WEEK-1-TASKS.md` | Kompletter Tagesplan mit Zeitaufwand pro Aufgabe. |

Alles oben ist **Text/Konzept final** – nichts davon muss neu geschrieben oder umpositioniert werden.

---

## 2. Erste 3 Content-Stücke — fertig ausformuliert

Basis: Content-Säulen aus `GO-TO-MARKET.md` (Problem-Aufmerksamkeit → Bildung/Vertrauen → Produktlösung) + Inhalte aus `LEAD-MAGNET.md`. Direkt für Instagram/Facebook copy-paste-fertig.

### Post 1 – Problem-Aufmerksamkeit

```
🌙 Jeder 3. Deutsche über 40 schläft schlecht. Die wenigsten wissen, woran es wirklich liegt.

Es ist selten „nur das Alter". Die häufigsten Gründe, warum der Schlaf ab 40 schwerer fällt:

😓 Hormonelle Veränderungen
🌀 Stress & Gedankenkarussell am Abend
🛏️ Ein Kissen, das nicht mehr zum eigenen Körper passt
📱 Blaues Licht am Abend – Handy, Tablet, TV
☕ Koffein oder Alkohol zu spät am Tag

Die gute Nachricht: Jeder dieser Punkte lässt sich beeinflussen – ohne teure Gadgets, ohne Medikamente.

Wir haben daraus einen praktischen 7-Tage-Plan gemacht: ein Fokus pro Tag, sofort umsetzbar.

👉 Trag dich in die Warteliste ein, dann bekommst du den Plan als Erstes kostenlos: [LINK]

Welcher Punkt trifft bei dir am ehesten zu? Schreib's in die Kommentare. 👇

#BesserSchlafen #SchlafabVierzig #SchlafKlar
```

### Post 2 – Bildung & Vertrauen

```
🌙 Der Fehler, der vielen Menschen ab 40 den Schlaf raubt (und leicht zu korrigieren ist)

Unter der Woche um 23 Uhr ins Bett, am Wochenende erst um 1 Uhr?

Der Körper versteht das nicht. Er braucht Rhythmus – jeden Tag, nicht nur montags bis freitags.

Unsere Empfehlung für die nächsten 7 Tage:

✅ Jeden Abend zur gleichen Zeit ins Bett
✅ Jeden Morgen zur gleichen Zeit aufstehen – auch am Wochenende
✅ Einen festen „Zubettgeh-Wecker" stellen, nicht nur einen Weckwecker

Klingt simpel. Wirkt aber genau deshalb.

Das ist Tag 1 unseres kostenlosen 7-Tage-Schlafplans „Besser schlafen in 7 Tagen" – ein Fokus pro Tag, ganz ohne teure Gadgets.

👉 Jetzt kostenlos in die Warteliste eintragen: [LINK]

Gute Nacht,
Euer SchlafKlar-Team
```

### Post 3 – Marke & Lead-Magnet-Launch

```
🌙 Endlich wieder durchschlafen – ganz ohne teure Matratze oder Wundermittel.

Wir sind SchlafKlar: geprüfte Schlafprodukte aus der EU für alle, die morgens ohne Nacken- oder Rückenschmerzen aufwachen wollen – und keine Lust auf 3 Wochen Lieferzeit aus Fernost haben.

Bevor es das erste Produkt gibt, schenken wir dir etwas Wichtigeres: unseren kostenlosen Guide „Besser schlafen in 7 Tagen – der praktische Plan für Menschen ab 40".

Was dich erwartet:
📘 12–16 Seiten, 1 klarer Fokus pro Tag
🛌 Konkrete Aufgaben statt vage Tipps
✅ Eine Checkliste „Mein Schlafumfeld" zum Abhaken
🎁 10 % Willkommensrabatt für den Start, sobald unser Shop live geht

👉 Trag dich jetzt kostenlos ein und sei unter den Ersten: [LINK]

Kein Spam. Nur das, was wirklich hilft, besser zu schlafen.

Euer SchlafKlar-Team
```

---

## 3. Die EINE externe Sache, die der Mensch selbst tun muss

Drei kostenlose Accounts, nichts weiter:

| # | Was | Wofür | Kosten |
|---|---|---|---|
| a | **Brevo-Free-Account** anlegen (brevo.com) | E-Mail-Sequenz aus `EMAIL-SEQUENCE.md` als Kampagne/Automation importieren, Anmeldeformular erstellen, dessen Formular-Endpoint-URL in `landing-page.html` bei `action="{{FORM_ACTION}}"` einsetzen | 0 € (Free-Tarif bis 300 E-Mails/Tag) |
| b | **GitHub Pages** oder **Carrd Free** Account | `landing-page.html` hosten und live schalten (GitHub Pages: Datei ist bereits fertiges HTML, kein Umbau nötig – einfach Repo + Pages aktivieren. Carrd Free: nur falls du lieber im Carrd-Baukasten arbeitest) | 0 € |
| c | **Shopify-Kostenlostestphase** starten | Nur um Store-Name/Domain zu reservieren und eine simple Vorab-/Warteliste-Seite einzurichten – **kein Tarif abschließen, keine Produkte importieren** | 0 € (Trial) |

**Wichtig – nicht Teil dieser Woche:** Ein echter Lieferantenvertrag (Dropshipping-Kooperation) ist ein späterer Schritt mit realen Konditionen/Kosten. Diese Woche werden nur die 3 Kontakt-E-Mails aus `SUPPLIER-RESEARCH.md` verschickt – keine Testbestellung, keine Zahlung.

---

## 4. Diese Woche ohne Budget möglich (Checkliste)

- [ ] Markenname final bestätigen (SchlafKlar / NachtKraft / RuheReich) + Domain-Verfügbarkeit kostenlos prüfen (noch nicht kaufen)
- [ ] Lead-Magnet-PDF in **Canva Free** gestalten und exportieren (Text ist in `LEAD-MAGNET.md` bereits fertig)
- [ ] Landing Page hosten (GitHub Pages/Carrd Free) + Formular mit Brevo verbinden
- [ ] Brevo-Account einrichten, 5 E-Mails + Warenkorb-Abbruch-Flow aus `EMAIL-SEQUENCE.md` importieren
- [ ] 3 EU-Lieferanten per E-Mail anschreiben (Vorlage in `SUPPLIER-RESEARCH.md`) – nur E-Mail, keine Bestellung
- [ ] Shopify-Kostenlostestphase starten, einfache Vorab-/Warteliste-Seite einrichten (kein Tarif)
- [ ] Die 3 Content-Stücke aus Abschnitt 2 organisch auf Instagram/Facebook posten
- [ ] DPMA-Markenrecherche + LUCID-Pflicht-Check durchführen (beide kostenlos)

**Bewusst ausgeschlossen (kostenpflichtig, kommt später):** Shopify-Bezahltarif, PageFly/GemPages, Canva Pro, Testbestellungen bei Lieferanten, E-Recht24-Abo, Paid Ads.
