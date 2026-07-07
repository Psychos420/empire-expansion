# Empire Expansion — Autonomer Launch-Controller für Claude Code

**Mission:** Starte alle 14 Nischen so weit wie möglich ohne menschlichen Eingriff.  
**Stop-Regeln:** Claude darf den Nutzer nur dann ansprechen, wenn es um **Zahlungsdaten, persönliche Kontakte, Rechtsform/Geschäftsadresse, Video-Aufnahmen oder finale Freigaben von Ausgaben > 50 €** geht. Alles andere macht Claude selbstständig.

---

## 1. Wann Claude den Nutzer FRAGEN muss

| Situation | Grund |
|-----------|-------|
| Eingabe von Kreditkarten/Bankdaten (Stripe, PayPal, Brevo, Domain-Kauf) | Sicherheit |
| Eingabe persönlicher Kontakte für Outreach (LinkedIn, WhatsApp, E-Mail) | DSGVO / Privatsphäre |
| Eingabe der offiziellen Geschäftsadresse / Rechtsform | Rechtliche Korrektheit |
| Aufnahme von Videos für TikTok/Instagram/Reels | Kann nicht automatisch |
| Live-Interaktion in Facebook-/LinkedIn-Gruppen (Antworten, DMs) | Menschliche Authentizität |
| Telefonate mit Maklern / Kunden | Kann nicht automatisch |
| Ausgaben über 50 € pro Nische | Budget-Freigabe |
| Finale Veröffentlichung von bezahlten Ads | Freigabe |

## 2. Was Claude SELBSTSTÄNDIG macht

- Dateien lesen, prüfen, aktualisieren
- Skripte ausführen (PDFs bauen, Landing Pages patchen, Reports generieren)
- Texte generieren: E-Mails, Posts, Outreach-Vorlagen, Scripts
- Technische Konfiguration vorbereiten (HTML, JSON, Markdown)
- Struktur und Tracking dokumentieren
- Tests durchführen (Links, Formulare, Downloads)
- Wiederkehrende Tasks automatisieren

---

## 3. Zentrale Steuerdatei

Claude liest bei jedem Start automatisch:

1. `EMPIRE-WEEK-1-SPRINT-BLUEPRINT.md` — Gesamtziel und Prioritäten
2. `EMPIRE-SETUP-GUIDE.md` — Tool-Setup
3. `EMPIRE-AUTONOMOUS-LAUNCH.md` — diese Datei
4. `00-shared/tools/empire-autopilot.py` — das Ausführungsskript
5. `empire-config.json` (wird vom Nutzer oder Claude erstellt) — alle URLs, Keys, Links

---

## 4. Der Autopilot-Befehl

Wenn der Nutzer sagt: **„Claude, führe den Empire Launch aus"**, dann führt Claude sofort folgende Sequenz aus:

### Phase A: Vorbereitung (autonom)

1. Liest `empire-config.json`.
2. Falls nicht vorhanden: Erstellt `empire-config-template.json` mit Platzhaltern und informiert den Nutzer, welche 3–5 Werte er eintragen muss (Brevo-Form-URL, Cal.com-Links, Stripe-Links).
3. Prüft alle 14 Ordner auf Vollständigkeit.
4. Baut alle PDFs neu mit `regenerate-pdfs.bat` bzw. `.sh`.
5. Prüft alle Landing Pages auf fehlende `lead-magnet.pdf`-Links.

### Phase B: Landing Pages aktivieren (autonom)

1. Ersetzt in allen `landing-page.html`:
   - `{{FORM_ACTION}}` durch die echte Brevo-Form-URL (pro Nische aus `empire-config.json`)
   - `{{CAL_LINK}}` durch den Cal.com-Terminlink
   - `{{STRIPE_LINK}}` / `{{PAYPAL_LINK}}` durch Zahlungslinks
   - Platzhalter für Impressum/Datenschutz durch generische Textbausteine
2. Fügt Meta Pixel + GA4 Platzhalter-Comments bei Bedarf hinzu.
3. Testet alle internen Links.

### Phase C: Content & Outreach vorbereiten (autonom)

1. Generiert pro Nische:
   - 7 LinkedIn-Posts
   - 5 Facebook-Gruppen-Posts
   - 3 WhatsApp/LinkedIn-Outreach-Vorlagen
   - 1 E-Mail-Broadcast
2. Speichert diese in `00-shared/generated-content/YYMMDD-niche-name/`.
3. Erstellt eine tägliche Posting-Checkliste.

### Phase D: Zusammenfassung & menschliche Stop-Punkte

Claude erstellt einen `LAUNCH-STATUS-REPORT.md` und zeigt dem Nutzer:
- Was automatisch erledigt ist
- Welche 3–5 manuellen Schritte jetzt nötig sind
- Welche Links live sind
- Welche Inhalte bereitliegen

---

## 5. Konfigurationsdatei: `empire-config.json`

Claude erstellt diese Vorlage. Der Nutzer füllt nur die Werte aus, die er bereits hat.

```json
{
  "brand": {
    "name": "Empire Expansion",
    "domain": "empire-expansion.de",
    "email": "hallo@empire-expansion.de"
  },
  "tools": {
    "brevo": {
      "account_name": "Empire Expansion",
      "sender_email": "hallo@empire-expansion.de"
    },
    "cal": {
      "base_url": "https://empire-expansion.cal.com"
    },
    "stripe": {
      "account_email": ""
    },
    "paypal": {
      "account_email": ""
    },
    "github": {
      "username": "",
      "repo": "empire-expansion"
    }
  },
  "niches": {
    "01-affiliate-marketing": {
      "brevo_form_url": "",
      "cal_link": "",
      "stripe_link": "",
      "affiliate_links": {
        "zahnzusatz": "",
        "depot": "",
        "pkv": ""
      }
    },
    "02-tiktok-shop": {
      "brevo_form_url": "",
      "cal_link": "",
      "stripe_link": "",
      "product_price": 29
    },
    "03-pdfs-guides": {
      "brevo_form_url": "",
      "cal_link": "",
      "stripe_tripwire_link": "",
      "stripe_upsell_link": ""
    },
    "04-ki-integrationen-35plus": {
      "brevo_form_url": "",
      "cal_link": "https://empire-expansion.cal.com/ki-check",
      "stripe_starter_link": "",
      "stripe_business_link": ""
    },
    "05-lead-generation-pkv": {
      "brevo_form_url": "",
      "cal_link": "https://empire-expansion.cal.com/pkv-check",
      "ppl_partner_email": ""
    },
    "06-lead-generation-dropshipping": {
      "brevo_form_url": "",
      "cal_link": "",
      "stripe_link": "",
      "lead_partner_email": ""
    },
    "07-marketing-agency-traffic": {
      "brevo_form_url": "",
      "cal_link": "https://empire-expansion.cal.com/strategie-call",
      "stripe_sprint_link": ""
    },
    "08-app-ideen-appstore": {
      "brevo_form_url": "",
      "cal_link": "https://empire-expansion.cal.com/renten-check",
      "stripe_check_link": "",
      "stripe_beta_link": ""
    },
    "09-finanzielle-freiheit": {
      "brevo_form_url": "",
      "cal_link": "https://empire-expansion.cal.com/fire-check",
      "stripe_strategy_link": ""
    },
    "10-gesundheit-praevention-40plus": {
      "brevo_form_url": "",
      "cal_link": "",
      "stripe_reset_link": "",
      "stripe_program_link": ""
    },
    "11-immobilien-baufinanzierung": {
      "brevo_form_url": "",
      "cal_link": "https://empire-expansion.cal.com/baufi-check",
      "stripe_guide_link": "",
      "stripe_call_link": ""
    },
    "12-selbststaendigkeit-business-setup": {
      "brevo_form_url": "",
      "cal_link": "https://empire-expansion.cal.com/strategie-call",
      "stripe_plan_link": ""
    },
    "13-reisen-lifestyle-35plus": {
      "brevo_form_url": "",
      "cal_link": "",
      "stripe_guide_link": "",
      "stripe_concept_link": ""
    },
    "14-nachhaltigkeit-eco": {
      "brevo_form_url": "",
      "cal_link": "",
      "stripe_b2c_link": "",
      "stripe_b2b_link": "",
      "stripe_audit_link": ""
    }
  }
}
```

---

## 6. Befehle für den Nutzer

| Befehl | Was passiert |
|--------|--------------|
| `Claude, führe den Empire Launch aus` | Startet die komplette autonome Sequenz |
| `Claude, baue alle PDFs neu` | Führt `regenerate-pdfs` aus |
| `Claude, prüfe alle Landing Pages` | Findet fehlende Links / Platzhalter |
| `Claude, generiere Content für Woche 1` | Erstellt Posts & Outreach für alle 14 Nischen |
| `Claude, erstelle den Launch-Status-Report` | Zeigt aktuellen Stand |
| `Claude, bereite die Top-5-Nischen live vor` | Fokus auf 01, 04, 05, 07, 09 |

---

## 7. Grundsatz

> **Ziel ist nicht Perfektion. Ziel ist Momentum.**  
> Claude macht alles, was technisch und inhaltlich möglich ist, selbst. Der Nutzer liefert nur das, was wirklich nur ein Mensch kann: Entscheidungen, Zahlungsdaten, persönliches Netzwerk und authentische Kommunikation.
