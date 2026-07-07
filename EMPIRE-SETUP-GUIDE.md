# Empire Expansion — Setup-Guide
**Zweck:** Schritt-für-Schritt-Anleitung für die ersten drei zentralen Tools: Brevo (E-Mail), Cal.com (Terminbuchung) und GitHub Pages (Hosting).  
**Ziel:** Nach diesem Guide sind die technischen Grundlagen live, damit die ersten Landing Pages Leads sammeln und Termine buchen können.

---

## 1. Unternehmensname / Markenname

### Empfohlener Account-Name (für Tools, nicht Rechtsform)

| Kontext | Name |
|---------|------|
| **Brevo Sender-Name** | `Empire Expansion` |
| **Cal.com Profil-Name** | `Empire Expansion` |
| **GitHub Organization (optional)** | `empire-expansion` |
| **Domain (empfohlen)** | `empire-expansion.de` |
| **Absender-E-Mail** | `hallo@empire-expansion.de` |

> **Wichtig:** Du brauchst keine eingetragene Firma, um Brevo oder Cal.com zu nutzen. Gib einfach `Empire Expansion` als Firmennamen an. Sobald du eine GmbH/UG hast, kannst du den Namen in den Einstellungen ändern.

### Alternative Domains (falls empire-expansion.de nicht verfügbar ist)

- `empire-expansion.com`
- `empire-x.de`
- `mein-empire.de`
- `empire-dach.de`
- `empire-start.de`

**Tipp:** Kaufe die Domain direkt bei **Cloudflare Registrar** oder **Hetzner** (ca. 10–15 €/Jahr). Cloudflare hat den Vorteil, dass du DNS-Einträge für Brevo, Cal.com und GitHub Pages kostenlos und schnell setzen kannst.

---

## 2. Brevo — E-Mail-Marketing & Automation

### Schritt 1: Account anlegen

1. Gehe zu **brevo.com**.
2. Klicke auf **"Kostenlos starten"** oder **"Sign up free"**.
3. Erstelle einen Account mit deiner E-Mail-Adresse.
4. Beim Onboarding gibst du ein:
   - **Firmenname:** `Empire Expansion`
   - **Branche:** `Marketing / Beratung / Sonstiges`
   - **Anzahl Kontakte:** `Weniger als 500` (kannst du später ändern)
   - **Website:** `https://empire-expansion.de` (oder GitHub-Pages-URL als Platzhalter)

### Schritt 2: Domain verifizieren (sehr wichtig für Zustellbarkeit)

1. In Brevo oben rechts auf dein Profil → **Senders & IP** → **Domains**.
2. Klicke auf **"Add a domain"**.
3. Gib deine Domain ein: `empire-expansion.de`.
4. Brevo zeigt dir DNS-Einträge (SPF, DKIM, DMARC).
5. Melde dich bei **Cloudflare** (oder wo du die Domain gekauft hast) an.
6. Gehe zu **DNS** → **Records** → füge die Einträge von Brevo hinzu.
7. Warte 5–60 Minuten, dann klicke in Brevo auf **"Authenticate"**.

> **Ohne Domain-Authentifizierung landen deine E-Mails im Spam.** Das ist der wichtigste Schritt.

### Schritt 3: Absender-E-Mail erstellen

1. Gehe zu **Senders & IP** → **Senders**.
2. Klicke **"Add a sender"**.
3. E-Mail: `hallo@empire-expansion.de`
4. Name: `Empire Expansion`
5. Bestätige die Absender-E-Mail über den Link, den Brevo an dich sendet.

### Schritt 4: Listen & Kontakte anlegen

1. Gehe zu **Contacts** → **Lists**.
2. Erstelle eine Liste pro Nische:
   - `01-affiliate-marketing`
   - `02-tiktok-shop`
   - `03-pdfs-guides`
   - `04-ki-integrationen`
   - `05-pkv-leads`
   - `06-dropshipping`
   - `07-agency`
   - `08-app-ideen`
   - `09-finanzielle-freiheit`
   - `10-gesundheit`
   - `11-immobilien`
   - `12-selbststaendigkeit`
   - `13-reisen`
   - `14-nachhaltigkeit`
3. Optional: Erstelle ein globales Segment `Alle Empire Leads`.

### Schritt 5: Double-Opt-In-Formular erstellen

1. Gehe zu **Contacts** → **Forms** → **Create a subscription form**.
2. Wähle **"Embedded form"**.
3. Ordne das Formular der passenden Liste zu (z. B. `01-affiliate-marketing`).
4. Füge Felder hinzu:
   - E-Mail (Pflicht)
   - Vorname (optional)
   - DSGVO-Checkbox (Pflicht)
5. Speichere das Formular.
6. Kopiere den **HTML-Code** oder die **Form-Action-URL**.
7. Füge die URL in die `landing-page.html` der jeweiligen Nische ein (ersetze `{{FORM_ACTION}}`).

### Schritt 6: Automation / Willkommens-Sequenz einrichten

1. Gehe zu **Automation** → **Create a workflow**.
2. Trigger: **A contact is added to a list**.
3. Wähle die passende Liste.
4. Füge eine **E-Mail**-Aktion hinzu:
   - Betreff: "Hier ist dein kostenloser [Lead-Magnet-Name]"
   - Inhalt: Kurzer Text + Download-Link zum PDF (`lead-magnet.pdf`)
5. Füge weitere E-Mails hinzu (Tag 1, Tag 2, Tag 3, Tag 5, Tag 7).
6. Aktiviere den Workflow.

---

## 3. Cal.com — Terminbuchung

### Schritt 1: Account anlegen

1. Gehe zu **cal.com**.
2. Klicke auf **"Get started"** oder **"Sign up"**.
3. Erstelle einen Account mit deiner E-Mail-Adresse.
4. Beim Onboarding:
   - **Name:** `Empire Expansion`
   - **Kalender-Verbindung:** Verbinde Google Kalender oder Outlook.
   - **Verfügbarkeit:** Setze deine verfügbaren Zeiten (z. B. Mo–Fr 10–18 Uhr).

### Schritt 2: Event-Typen anlegen

1. In Cal.com auf **Event Types** klicken.
2. Klicke **"New event type"**.
3. Erstelle mindestens diese Event-Typen:

| Event-Name | Dauer | Verwendung |
|------------|-------|------------|
| `Kostenloser Strategie-Call` | 20 Min | 04 KI, 07 Agency, 09 FIRE, 12 Selbstständigkeit |
| `PKV-Check` | 15 Min | 05 PKV |
| `Baufi-Check` | 20 Min | 11 Immobilien |
| `Rentenlücke-Check` | 20 Min | 08 App-Ideen |

4. Pro Event-Typ:
   - Setze Titel und Beschreibung.
   - Setze den Link (z. B. `empire-expansion.cal.com/ki-check`).
   - Aktiviere **E-Mail-Bestätigung**.
   - Füge ggf. Fragen hinzu (z. B. "Was ist Ihr größtes Problem?").

### Schritt 3: Buchungslink in Landing Pages einfügen

1. Kopiere den Link des Event-Typs.
2. Füge ihn in die jeweilige `landing-page.html` ein:
   - Im CTA-Button: `<a href="https://empire-expansion.cal.com/ki-check" class="cta-button">Termin buchen</a>`
   - In der E-Mail-Sequenz: Text-Link oder Button.

### Schritt 4: Testlauf

1. Öffne den Buchungslink im Inkognito-Fenster.
2. Buche einen Testtermin.
3. Prüfe, ob:
   - Die Bestätigungs-E-Mail ankommt.
   - Der Termin in deinem Kalender erscheint.
   - Du eine Benachrichtigung bekommst.

---

## 4. GitHub Pages — Landing Pages kostenlos hosten

### Schritt 1: GitHub-Account erstellen

1. Gehe zu **github.com**.
2. Klicke auf **"Sign up"**.
3. Erstelle einen Account mit deiner E-Mail-Adresse.
4. Wähle einen Benutzernamen, z. B. `empire-expansion` oder deinen persönlichen Namen.

### Schritt 2: Neues Repository erstellen

1. Nach dem Login klicke oben rechts auf das **+** → **New repository**.
2. Repository-Name: `empire-expansion`
3. Wähle **Public** (kostenlos).
4. Klicke **"Create repository"**.

### Schritt 3: Dateien hochladen

#### Variante A: Per Drag & Drop (einfachster Start)

1. Im Repository klicke auf **"uploading an existing file"**.
2. Ziehe alle Projektordner und Dateien in das Fenster.
3. Achte darauf, dass die Struktur erhalten bleibt:
   ```
   empire-expansion/
   ├── index.html
   ├── 01-affiliate-marketing/
   │   ├── landing-page.html
   │   └── lead-magnet.pdf
   ├── 02-tiktok-shop/
   │   ├── landing-page.html
   │   └── lead-magnet.pdf
   ...
   ```
4. Schreibe als Commit-Nachricht: `Initial upload`.
5. Klicke **"Commit changes"**.

#### Variante B: Per Git-Befehl (für Updates)

```bash
cd C:/Users/aksoy/Claude/Projects/Empire-Expansion
git init
git add .
git commit -m "Initial Empire Expansion upload"
git branch -M main
git remote add origin https://github.com/DEIN_USERNAME/empire-expansion.git
git push -u origin main
```

### Schritt 4: GitHub Pages aktivieren

1. Im Repository oben auf **Settings** klicken.
2. Links im Menü auf **Pages** klicken.
3. Unter **Source** wähle **Deploy from a branch**.
4. Wähle **Branch: main** und Ordner **/ (root)**.
5. Klicke **"Save"**.
6. Warte 1–5 Minuten.
7. Deine Seite ist dann erreichbar unter:  
   `https://DEIN_USERNAME.github.io/empire-expansion/`

### Schritt 5: Eigene Domain verbinden (optional, aber empfohlen)

1. Im Repository gehe zu **Settings** → **Pages**.
2. Unter **Custom domain** gib ein: `empire-expansion.de`.
3. Klicke **"Save"**.
4. In deinem Domain-Provider (Cloudflare/Hetzner) setze einen CNAME-Eintrag:
   - **Type:** CNAME
   - **Name:** `@` oder `www`
   - **Target:** `DEIN_USERNAME.github.io`
5. Aktiviere in GitHub Pages **Enforce HTTPS** (nach einigen Minuten möglich).

### Schritt 6: URLs testen

1. Öffne `https://DEIN_USERNAME.github.io/empire-expansion/` → Das ist der Hub.
2. Teste eine Landing Page:  
   `https://DEIN_USERNAME.github.io/empire-expansion/01-affiliate-marketing/landing-page.html`
3. Teste ein PDF:  
   `https://DEIN_USERNAME.github.io/empire-expansion/01-affiliate-marketing/lead-magnet.pdf`

---

## 5. Schnell-Checkliste: Tag-1-Setup

- [ ] Brevo-Account erstellt (`Empire Expansion`)
- [ ] Domain registriert (z. B. `empire-expansion.de`)
- [ ] Brevo-DNS-Einträge gesetzt und verifiziert
- [ ] Absender-E-Mail `hallo@empire-expansion.de` bestätigt
- [ ] 14 Listen in Brevo angelegt
- [ ] Erstes Formular für 01 Affiliate erstellt und in `landing-page.html` eingefügt
- [ ] Cal.com-Account erstellt (`Empire Expansion`)
- [ ] Kalender verbunden und Verfügbarkeit gesetzt
- [ ] Erster Event-Typ erstellt (z. B. Kostenloser Strategie-Call)
- [ ] GitHub-Account erstellt
- [ ] Repository `empire-expansion` erstellt
- [ ] Dateien hochgeladen
- [ ] GitHub Pages aktiviert
- [ ] Hub + erste Landing Page getestet

---

## 6. Wichtige Hinweise

- **Domain zuerst:** Ohne eigene Domain funktioniert Brevo nur eingeschränkt. Investiere die 10–15 €.
- **Keine gekauften Listen:** Brevo verbietet den Import gekaufter E-Mail-Adressen. Nutze nur Leads, die sich über deine Landing Pages anmelden.
- **DSGVO:** Jede Landing Page braucht eine Datenschutzerklärung und ein Impressum. Für den Start reichen generische Textbausteine, die du anpasst.
- **Cal.com Free vs. Pro:** Der kostenlose Plan reicht für den Start. Pro kostet ~10 $/Monat und bietet mehr Branding-Optionen.
- **GitHub Pages Limits:** Kostenlos, 1 GB Speicher, öffentliche Repositories. Für 14 Landing Pages und PDFs mehr als ausreichend.

---

**Nächster Schritt nach diesem Guide:** Gehe zum [EMPIRE-WEEK-1-SPRINT-BLUEPRINT](./EMPIRE-WEEK-1-SPRINT-BLUEPRINT.md) und starte Tag 1.
