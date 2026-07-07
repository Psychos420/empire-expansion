# E-Mail-Sequenz: Schlaf & Erholung

## Entscheidung

**Tool:** Klaviyo oder Brevo  
**Trigger:** Anmeldung über Lead-Magnet-Formular auf Landing Page  
**Segmentierung:** Optional nach Problemfeld (Nacken/Rücken, Einschlafen, nächtliches Erwachen, Stress)

---

## Sequenz-Überblick

| Tag | E-Mail | Ziel |
|---|---|---|
| 0 | Willkommen + Download | Liefern, Vertrauen aufbauen, Rabatt zeigen |
| 1 | Das größte Schlafproblem über 40 | Engagement, Story, erster Tipp |
| 2 | Produktempfehlung passend zum Problem | Erster Verkauf |
| 3 | Kundenstory + Bewertung | Zweifel abbauen |
| 4 | Warenkorb-Abbruch-Recovery (nur bei Abbruch) | Conversion retten |
| 5 | Letzte Chance Rabatt | Dringlichkeit, Verkauf |

Zusätzlich: **Warenkorb-Abbruch-Recovery-Flow** für Shop-Besucher, die nicht über Lead-Magnet gekommen sind.

---

## E-Mail 1 – Tag 0: Willkommen + Download

**Absender:** SchlafKlar Team  
**Betreff:** Ihr 7-Tage-Schlafplan ist drin 🌙  
**Vorschautext:** Plus 10 % Rabatt für Ihre erste Bestellung.

**Body:**

---

Hallo `{{ first_name | default: 'da' }}`,

schön, dass Sie dabei sind.

Hier ist Ihr kostenloser Guide:

**[→ „Besser schlafen in 7 Tagen" herunterladen](LINK)**

Sie haben auch direkt Ihren persönlichen 10 % Willkommensrabatt erhalten:

**Code: SCHLAF7**  
Gültig bis: `{{ event.discount_deadline | default: 'in 7 Tagen' }}`

Was Sie als Nächstes tun können:
1. Den Guide herunterladen und Tag 1 heute Abend starten.
2. Ihr größtes Schlafproblem im Hinterkopf behalten – in den nächsten Tagen schicken wir Ihnen passende Tipps und Produkte.
3. Wenn Sie Fragen haben, antworten Sie einfach auf diese E-Mail.

Gute Nacht beginnt mit einem klaren Plan.

Ihr SchlafKlar-Team

P.S. Alle Produkte im Guide kommen aus der EU und werden von uns auf Qualität geprüft. Bei Nichtgefallen: 30 Tage Probeschlafen, kostenlose Retoure.

---

## E-Mail 2 – Tag 1: Das größte Schlafproblem über 40

**Absender:** SchlafKlar Team  
**Betreff:** Der Fehler, der Menschen ab 40 den Schlaf raubt  
**Vorschautext:** Er lässt sich leicht korrigieren.

**Body:**

---

Hallo `{{ first_name | default: 'Sie' }}`,

gestern haben Sie den 7-Tage-Plan heruntergeladen. Heute sprechen wir über den häufigsten Fehler:

**Unregelmäßige Schlafzeiten.**

Viele Menschen gehen unter der Woche um 23 Uhr ins Bett, am Wochenende aber erst um 1 Uhr. Ihr Körper versteht das nicht. Er braucht Rhythmus – nicht nur am Montag, sondern jeden Tag.

**Ihre Aufgabe für heute:**
- Gehen Sie heute und die nächsten 7 Tage zur gleichen Zeit ins Bett.
- Stehen Sie morgens zur gleichen Zeit auf – auch am Wochenende.
- Setzen Sie einen Wecker fürs Zubettgehen.

Das klingt simpel. Aber genau deshalb wirkt es.

Morgen zeigen wir Ihnen, warum Ihr Schlafzimmer möglicherweise das Problem ist – und wie Sie es in 20 Minuten optimieren.

Bis dann,  
Ihr SchlafKlar-Team

P.S. Wenn Sie schon jetzt wissen, dass Ihr Kissen oder Ihre Matratze mitspielt: **[Hier finden Sie geprüfte Produkte](LINK)** mit 10 % Rabatt (Code SCHLAF7).

---

## E-Mail 3 – Tag 2: Produktempfehlung passend zum Problem

**Absender:** SchlafKlar Team  
**Betreff:** Das passt zu Ihrem Schlafproblem  
**Vorschautext:** Basierend auf Ihrer Auswahl beim Download.

**Body (dynamisch nach Segment):**

---

Hallo `{{ first_name | default: 'Sie' }}`,

Sie haben bei Ihrer Anmeldung angegeben, dass Sie vor allem mit **„Nacken-/Rückenschmerzen"** zu kämpfen haben.

Dann ist Ihr Kissen der wichtigste Hebel.

Die meisten Kissen sind entweder zu hoch, zu niedrig oder verlieren nach wenigen Monaten die Stützkraft. Das Ergebnis: Der Nacken liegt die ganze Nacht schief, Muskeln verkrampfen, Schmerzen am Morgen sind vorprogrammiert.

**Unsere Empfehlung für Sie:**

**Ergonomisches Nackenstützkissen – EUR 59,90**
- Memory-Foam passt sich Kopf und Nacken an
- Ergonomische Höhe für Rücken- und Seitenschläfer
- Atmungsaktiver Bezug, waschbar
- 30 Tage Probeschlafen

**[→ Jetzt mit 10 % Rabatt sichern – Code SCHLAF7](LINK)**

Wenn Sie zusätzlich Ihre Liegefläche verbessern möchten, ergänzt unser **Matratzen-Topper (EUR 129,90)** das Kissen ideal.

Ihr Rabattcode **SCHLAF7** gilt noch bis `{{ event.discount_deadline }}`.

Gute Nacht,  
Ihr SchlafKlar-Team

---

**Alternative Segmente (nur Produktteil ändern):**
- **Einschlafprobleme:** White-Noise-Gerät + Schlafmaske + Lavendel-Spray
- **Nächtliches Erwachen:** Gewichtsdecke + Schlafmaske
- **Stress/Gedankenkarussell:** Gewichtsdecke + Lavendel-Spray + Entspannungs-Tipps
- **Schnarchen/Atmung:** Positionskissen + Schlafmaske

---

## E-Mail 4 – Tag 3: Kundenstory + Bewertung

**Absender:** SchlafKlar Team  
**Betreff:** „Ich dachte, ich brauche eine neue Matratze"  
**Vorschautext:** Sabine (52) erzählt, was wirklich geholfen hat.

**Body:**

---

Hallo `{{ first_name | default: 'Sie' }}`,

Sabine K. (52) aus München hatte fast zwei Jahre lang morgens Nackenschmerzen.

„Ich war kurz davor, 1.200 EUR für eine neue Matratze auszugeben", erzählt sie. „Dann habe ich das Nackenstützkissen von SchlafKlar getestet. Nach drei Nächten waren die Schmerzen spürbar weniger. Nach zwei Wochen praktisch weg."

Was Sie aus Sabines Geschichte mitnehmen können:
- Nicht immer ist die teuerste Lösung die richtige.
- Oft liegt das Problem direkt am Kissen – dem meist unterschätzten Schlafprodukt.
- Ein 30-tägiger Probeschlaf kostet nichts, aber kann viel ersparen.

**[→ Auch das Nackenkissen testen – 10 % Rabatt mit SCHLAF7](LINK)**

Wir freuen uns, wenn auch Sie bald von Ihrer besseren Nacht erzählen.

Gute Nacht,  
Ihr SchlafKlar-Team

P.S. Haben Sie Fragen zu einem Produkt? Antworten Sie einfach auf diese E-Mail – wir lesen jede Nachricht persönlich.

---

## E-Mail 5 – Tag 5: Letzte Chance Rabatt

**Absender:** SchlafKlar Team  
**Betreff:** Ihr 10 % Rabatt läuft in 24 Stunden ab  
**Vorschautext:** Code SCHLAF7 – letzte Chance.

**Body:**

---

Hallo `{{ first_name | default: 'Sie' }}`,

noch 24 Stunden können Sie Ihren Willkommensrabatt nutzen.

**Code: SCHLAF7**  
**Gültig bis:** `{{ event.discount_deadline }}`  
**Rabatt:** 10 % auf Ihre erste Bestellung

Falls Sie sich noch unsicher sind:

- **30 Tage Probeschlafen:** Nicht zufrieden? Volle Rückerstattung.
- **Kostenlose Retoure:** Wir holen das Produkt ab.
- **2 Jahre Gewährleistung:** Qualität, die hält.
- **EU-Lieferung:** 2–5 Tage, keine Zollüberraschungen.

**Unser Tipp für den Einstieg:**
Das **Schlaf-Set „Starter"** mit Nackenkissen, Schlafmaske und Lavendel-Spray für **EUR 99,90** statt EUR 114,70.

**[→ Rabatt jetzt einlösen – Code SCHLAF7](LINK)**

Danach verfällt der Rabatt.

Gute Nacht,  
Ihr SchlafKlar-Team

---

## Warenkorb-Abbruch-Recovery-Flow

### Trigger
- Kunde legt Produkt in Warenkorb
- Kunde gibt E-Mail im Checkout ein oder ist bereits angemeldet
- Kunde verlässt Seite ohne Kauf

### E-Mail 1 – 1 Stunde nach Abbruch

**Betreff:** Haben Sie etwas vergessen?  
**Vorschautext:** Ihr Schlaf-Set wartet noch auf Sie.

**Body:**

---

Hallo `{{ first_name | default: 'Sie' }}`,

Sie haben sich ein Produkt von SchlafKlar angesehen, aber den Kauf nicht abgeschlossen.

Hier ist Ihr Warenkorb:

`{{ event.cart_items }}`

Falls Sie noch Fragen haben oder etwas nicht geklappt hat: Antworten Sie einfach auf diese E-Mail.

**[→ Warenkorb abschließen](LINK)**

Gute Nacht,  
Ihr SchlafKlar-Team

---

### E-Mail 2 – 24 Stunden nach Abbruch

**Betreff:** Noch 24 Stunden: 10 % auf Ihren Warenkorb  
**Vorschautext:** Code SCHLAF7 – Ihr Rabatt gilt noch.

**Body:**

---

Hallo `{{ first_name | default: 'Sie' }}`,

Ihr Warenkorb ist noch gespeichert.

Nutzen Sie Ihren Code **SCHLAF7** und sichern Sie sich 10 % Rabatt auf:

`{{ event.cart_items }}`

**[→ Jetzt mit Rabatt bestellen](LINK)**

Gültig noch 24 Stunden.

Ihr SchlafKlar-Team

---

### E-Mail 3 – 48 Stunden nach Abbruch

**Betreff:** Letzte Erinnerung: Ihr Rabatt läuft ab  
**Vorschautext:** Sichern Sie sich 10 % Rabatt.

**Body:**

---

Hallo `{{ first_name | default: 'Sie' }}`,

dies ist die letzte Erinnerung:

Ihr Warenkorb bei SchlafKlar ist noch verfügbar, aber Ihr 10 % Rabatt **SCHLAF7** läuft in wenigen Stunden ab.

**[→ Warenkorb jetzt sichern](LINK)**

Denken Sie daran: 30 Tage Probeschlafen, kostenlose Retoure, 2 Jahre Gewährleistung.

Ihr SchlafKlar-Team

---

## SMS/WhatsApp-Varianten (optional)

| Zeitpunkt | Nachricht |
|---|---|
| 1h nach Abbruch | „Hallo, Ihr Schlaf-Set wartet noch. Hier geht's weiter: [Link] – SchlafKlar" |
| 24h nach Abbruch | „Nur noch heute: 10 % Rabatt auf Ihren Warenkorb mit Code SCHLAF7. [Link]" |

---

## Nurturing-Sequenz (für Nicht-Käufer nach Tag 7)

| Woche | Thema | Ziel |
|---|---|---|
| Woche 2 | „3 Minuten Entspannung vor dem Schlaf" | Engagement |
| Woche 3 | „Wie Sie Ihr Schlafzimmer in 20 Minuten optimieren" | Education |
| Woche 4 | Kundenstory + weiches Angebot | Conversion |
| Woche 5 | Neues Produkt/Bundle vorstellen | Verkauf |

---

## Segmentierungsregeln

| Segment | Kriterium | Inhalte |
|---|---|---|
| Nacken/Rücken | Auswahl im Formular | Nackenkissen, Topper |
| Einschlafen | Auswahl im Formular | White-Noise, Maske, Spray |
| Nächtliches Erwachen | Auswahl im Formular | Gewichtsdecke, Maske |
| Stress | Auswahl im Formular | Gewichtsdecke, Entspannung |
| Käufer | Hat gekauft | Bedienungsanleitung, Pflege, Cross-Sell |
| Inaktiv | Keine Öffnung 30 Tage | Re-Engagement, neuer Lead-Magnet |

---

## Nächste Schritte

1. Klaviyo/Brevo Account anlegen und Listen-Segmentierung einrichten
2. E-Mail-Templates in Tool importieren und Testsendungen durchführen
3. Warenkorb-Abbruch-Trigger konfigurieren
4. SMS/WhatsApp-Channel optional hinzuschalten
