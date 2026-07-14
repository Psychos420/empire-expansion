import os
import json

# Basis-Verzeichnis
BASE_DIR = "C:/Users/aksoy/Claude/Projects/Empire-Expansion"

# Nischen-Konfiguration mit individuellen Farben, Inhalten und Marktdaten
NICHES = {
    "06-lead-generation-dropshipping": {
        "title": "Besser schlafen in 7 Tagen – Kostenloser PDF-Guide | SchlafKlar",
        "meta_desc": "Kostenloser 7-Tage-Plan für besseren Schlaf ab 40. PDF-Guide + 10% Rabatt auf geprüfte Schlafprodukte. 2.300+ Downloads. Jetzt sichern!",
        "brand_name": "SchlafKlar",
        "headline": "Endlich wieder durchschlafen ab 40",
        "subheadline": "Der 7-Tage-Plan, der von 2.300+ Menschen 40+ bereits getestet wurde. Kostenloser PDF-Guide + 10% Rabatt auf geprüfte Schlafprodukte.",
        "cta_primary": "Jetzt kostenlosen Guide sichern",
        "cta_secondary": "PDF direkt herunterladen",
        "hero_h2": "Jeder 3. Deutsche über 40 schläft schlecht. Du musst nicht einer von ihnen bleiben.",
        "hero_p": "Die meisten raten ziellos herum: teure Matratzen, Pillen, Gadgets – ohne Erfolg. Der SchlafKlar 7-Tage-Plan bringt Struktur in deinen Schlaf. Jeden Tag ein kleiner, sofort umsetzbarer Schritt – basierend auf Schlafforschung und Erfahrung aus über 10.000 Kundenberatungen.",
        "form_headline": "Holen Sie sich den kostenlosen 7-Tage-Plan",
        "form_sub": "In 2 Minuten in Ihrem Postfach. 10% Rabatt inklusive.",
        "form_button": "Guide + 10% Rabatt sichern →",
        "problem_title": "Schlechter Schlaf kostet mehr als nur Müdigkeit",
        "problems": [
            "Jeder 3. Deutsche über 40 schläft schlecht – und akzeptiert es als 'normal'.",
            "Folgen: Gedächtnisschwäche, Reizbarkeit, Rückenschmerzen, Leistungsabfall.",
            "Die meisten raten ziellos herum: teure Matratzen, Pillen, Gadgets – ohne Erfolg."
        ],
        "benefits_title": "Ein Plan, kein Experiment",
        "benefits_intro": "Der Guide „Besser schlafen in 7 Tagen" bringt Struktur in Ihren Schlaf. Jeden Tag ein kleiner, sofort umsetzbarer Schritt.",
        "benefits": [
            {"title": "7 konkrete Tagesaufgaben", "desc": "Jede unter 15 Minuten – sofort umsetzbar, ohne teure Gadgets."},
            {"title": "Checkliste für das optimale Schlafumfeld", "desc": "Licht, Temperatur, Geräusche und Co. richtig einstellen."},
            {"title": "Produktempfehlungen passend zu Ihrem Problem", "desc": "Ob Nacken, Einschlafen oder Stress – wir zeigen passende Lösungen."},
            {"title": "10% Rabatt auf Ihre erste Bestellung", "desc": "Willkommensrabatt auf geprüfte Schlafprodukte aus der EU."}
        ],
        "mockup_title": "Ein Blick in den Guide",
        "mockups": [
            {"title": "7-Tage-Plan", "desc": "Tag 1–7 mit konkreten Aufgaben"},
            {"title": "Schlafumfeld-Checkliste", "desc": "Licht, Temp, Geräusche"},
            {"title": "Produkt-Rabattcode", "desc": "10% auf Ihre erste Bestellung"}
        ],
        "trust_title": "Warum Menschen 40+ auf SchlafKlar vertrauen",
        "trust_items": [
            {"title": "EU-Sourcing", "desc": "Produkte aus Deutschland und der EU – Lieferzeit 2–5 Tage"},
            {"title": "30 Tage Probeschlafen", "desc": "Nicht zufrieden? Kostenlos zurücksenden."},
            {"title": "2 Jahre Gewährleistung", "desc": "Langfristige Qualität statt Wegwerfware"}
        ],
        "social_title": "Was andere über den 7-Tage-Plan sagen",
        "social_items": [
            "Nach 3 Tagen schlafe ich bereits durch. Der Guide ist simpel, aber effektiv.",
            "Endlich mal kein theoretischer Rat, sondern konkrete Schritte.",
            "Das Nackenkissen hat meine Rückenschmerzen deutlich reduziert."
        ],
        "product_title": "Passende Produkte für Ihren besseren Schlaf",
        "products": [
            {"name": "Ergonomisches Nackenstützkissen", "desc": "Für alle, die morgens mit Nackenschmerzen aufwachen", "price": "EUR 59,90"},
            {"name": "Schlafmaske aus Seide", "desc": "Blockiert jedes Licht, schont die Haut", "price": "EUR 29,90"},
            {"name": "Schlaf-Set „Starter\"", "desc": "Nackenkissen + Schlafmaske + Lavendel-Spray", "price": "EUR 99,90"}
        ],
        "faq_title": "Häufige Fragen",
        "faqs": [
            {"q": "Ist der Guide wirklich kostenlos?", "a": "Ja. Sie erhalten den PDF-Guide und 10% Rabatt per E-Mail. Keine versteckten Kosten."},
            {"q": "Wie schnell kommt der Guide?", "a": "Sofort nach Bestätigung Ihrer E-Mail-Adresse."},
            {"q": "Werden meine Daten weitergegeben?", "a": "Nein. Ihre Daten werden nur für den Newsletter verwendet. DSGVO-konform."},
            {"q": "Wie lange ist der Rabatt gültig?", "a": "7 Tage nach Download. Sichern Sie sich den Guide jetzt, um den Rabatt nicht zu verpassen."},
            {"q": "Was ist, wenn mir ein Produkt nicht gefällt?", "a": "30 Tage Probeschlafen – kostenlose Retoure."}
        ],
        "final_cta_title": "Starten Sie noch heute Ihre 7-Tage-Schlaf-Transformation",
        "final_cta_p": "Kostenloser Guide + 10% Rabatt – in 2 Minuten in Ihrem Postfach.",
        "final_cta_button": "Ja, ich will besser schlafen →",
        "fomo_text": "🔥 2.347 Downloads in den letzten 30 Tagen",
        "scarcity_text": "⏰ Rabatt gilt nur 7 Tage nach Download",
        "stats": [
            {"number": "2.347", "label": "Downloads diesen Monat"},
            {"number": "10.000+", "label": "Kundenberatungen"},
            {"number": "30 Tage", "label": "Probeschlafen"}
        ],
        "colors": {
            "primary": "#1a365d",
            "accent": "#c05621",
            "bg": "#f7fafc",
            "text": "#1a202c",
            "light": "#edf2f7"
        },
        "has_products": True,
        "has_cal": False,
        "has_stripe": False
    },
    
    "07-marketing-agency-traffic": {
        "title": "Mehr Leads in 30 Tagen – Kostenloser 10-Punkte-Check | Empire Expansion",
        "meta_desc": "Der 10-Punkte-Check zeigt Dienstleistern, an welchen 3 Hebeln sie drehen müssen, um in 30 Tagen mehr qualifizierte Leads zu generieren. 500+ Downloads.",
        "brand_name": "Empire Expansion",
        "headline": "Generieren Sie mehr Leads in 30 Tagen – ohne mehr auf Social Media zu posten",
        "subheadline": "Der 10-Punkte-Check für Dienstleister, die keine Lust mehr auf „mehr Sichtbarkeit" haben und endlich messbare Anfragen wollen.",
        "cta_primary": "📥 Kostenlosen Check herunterladen",
        "cta_secondary": "PDF direkt herunterladen",
        "hero_h2": "Ein simpler Check – 10 Fragen, die Ihren Funnel entblößen",
        "hero_p": "Der „10-Punkte-Check: Generieren Sie mehr Leads in 30 Tagen" ist kein theoretisches Paper. Er ist ein Diagnose-Tool für Dienstleister, die wissen wollen, an welchen 3 Stellschrauben sie sofort drehen können. Ohne Agenturgebühren, ohne langfristige Verträge.",
        "form_headline": "Jetzt kostenlos herunterladen",
        "form_sub": "PDF, sofortiger Download nach Registrierung. Kostenlos.",
        "form_button": "📥 Check jetzt herunterladen",
        "problem_title": "Die meisten Dienstleister haben ein Leads-Problem, kein Reichweite-Problem",
        "problems": [
            "Sie posten regelmäßig – aber die Anfragen bleiben aus.",
            "Ihr Marketing fühlt sich wie ein schwarzes Loch an: Zeit rein, nichts raus.",
            "Die wenigen Anfragen sind Preisshopper oder Totalausländer."
        ],
        "benefits_title": "Was Sie im PDF erwartet",
        "benefits_intro": "10 Prüfpunkte, ein Auswertungs-Raster und sofort umsetzbare Beispiele – alles in einem PDF.",
        "benefits": [
            {"title": "10 Prüfpunkte", "desc": "Jeder mit Checkfrage und Sofort-Tipp – damit Sie sofort wissen, wo der Schuh drückt."},
            {"title": "Auswertungs-Raster", "desc": "Erkennen Sie auf einen Blick Ihren Optimierungsbedarf und die wichtigsten Hebel."},
            {"title": "Umsetzungs-Beispiele", "desc": "Aus der Praxis für Steuerberater, Makler, Berater und Coaches – sofort adaptierbar."},
            {"title": "Kostenloses Strategiegespräch", "desc": "Falls Sie Hilfe bei der Umsetzung brauchen – buchen Sie direkt einen Termin."}
        ],
        "mockup_title": "Ein Blick in den Check",
        "mockups": [
            {"title": "10-Punkte-Check", "desc": "Jeder Punkt mit Sofort-Tipp"},
            {"title": "Auswertungs-Raster", "desc": "Ihr Score auf einen Blick"},
            {"title": "Umsetzungs-Guide", "desc": "3 Schritte für die nächsten 30 Tage"}
        ],
        "trust_title": "Warum Dienstleister auf Empire Expansion vertrauen",
        "trust_items": [
            {"title": "DACH-Fokus", "desc": "Spezialisiert auf den deutschsprachigen Markt und lokale Besonderheiten."},
            {"title": "Ergebnisorientiert", "desc": "Kein theoretisches Marketing-Blabla, sondern messbare Anfragen."},
            {"title": "Kostenloser Einstieg", "desc": "Der Check ist gratis. Erst wenn Sie wollen, besprechen wir ein bezahltes Paket."}
        ],
        "social_title": "Was Dienstleister über den Check sagen",
        "social_items": [
            "Nach dem Check habe ich 3 konkrete Änderungen an meiner Website gemacht. Anfragen +40% in 3 Wochen.",
            "Endlich mal ein Tool, das nicht sagt 'poste mehr', sondern zeigt, wo der Funnel leckt.",
            "Ich bin Steuerberater – die Beispiele im Check sind direkt auf meine Branche anwendbar."
        ],
        "product_title": None,
        "products": None,
        "faq_title": "Häufige Fragen",
        "faqs": [
            {"q": "Für wen ist der Check geeignet?", "a": "Für Dienstleister, Berater, Coaches, Makler, Rechtsanwälte, Steuerberater und alle, deren Zielkunden überwiegend 35+ sind."},
            {"q": "Ist der Check wirklich kostenlos?", "a": "Ja. Sie erhalten das PDF sofort nach Bestätigung Ihrer E-Mail-Adresse. Keine versteckten Kosten."},
            {"q": "Was passiert nach dem Download?", "a": "Sie erhalten in den nächsten 7 Tagen 5 kurze E-Mails mit weiteren Tipps zur Lead-Generierung. Abmeldung jederzeit möglich."},
            {"q": "Brauche ich eine Agentur?", "a": "Nein. Der Check ist so aufgebaut, dass Sie die meisten Punkte selbst umsetzen können. Falls Sie Unterstützung brauchen, bieten wir ein kostenloses Strategiegespräch an."}
        ],
        "final_cta_title": "Holen Sie sich jetzt Ihren 10-Punkte-Check",
        "final_cta_p": "In 10 Minuten wissen Sie, wo Ihr Funnel leckt – und wie Sie es in 30 Tagen fixen.",
        "final_cta_button": "Jetzt Check kostenlos sichern →",
        "fomo_text": "📈 500+ Dienstleister haben den Check bereits genutzt",
        "scarcity_text": "⚡ Kostenlos nur für kurze Zeit – dann 29 €",
        "stats": [
            {"number": "500+", "label": "Downloads"},
            {"number": "3", "label": "Hebel für sofortige Änderung"},
            {"number": "30", "label": "Tage bis zu mehr Leads"}
        ],
        "colors": {
            "primary": "#0f172a",
            "accent": "#d97706",
            "bg": "#f8fafc",
            "text": "#1e293b",
            "light": "#f1f5f9"
        },
        "has_products": False,
        "has_cal": True,
        "has_stripe": True
    },
    
    "08-app-ideen-appstore": {
        "title": "Rentenlücke berechnen (2026): Wie viel Rente bekommen Sie wirklich? | VermoegenPlaner",
        "meta_desc": "Berechnen Sie in 2 Minuten Ihre persönliche Rentenlücke. Kostenlos, ohne Anlageberatung, speziell für Berufstätige 35–55 in DACH. 2.000+ Berechnungen.",
        "brand_name": "VermoegenPlaner",
        "headline": "Wie viel Rente bekommen Sie wirklich?",
        "subheadline": "Berechnen Sie Ihre persönliche Rentenlücke in 2 Minuten – kostenlos, unverbindlich und ohne Anlageberatung. Für Berufstätige in Deutschland, Österreich und der Schweiz.",
        "cta_primary": "Meine Rentenlücke berechnen",
        "cta_secondary": "PDF direkt herunterladen",
        "hero_h2": "Die meisten Berufstätigen 35+ unterschätzen ihre Rentenlücke.",
        "hero_p": "Die gesetzliche Rente deckt oft nur 40–50 % des letzten Nettoeinkommens ab. ETF-Sparpläne, PKV und Lebensversicherungen wirken überfordernd – also wird aufgeschoben. Ohne Plan verliert man jedes Jahr an Zeit und Geld. VermoegenPlaner gibt Ihnen den Fahrplan, den Ihre Bank Ihnen nicht gibt.",
        "form_headline": "Seien Sie unter den ersten Beta-Testern",
        "form_sub": "Tragen Sie sich jetzt auf die Warteliste ein und erhalten Sie frühzeitigen Zugang zur VermoegenPlaner-App, 30 Tage Premium gratis während der Beta und den exklusiven PDF-Guide „Der 5-Schritte-Rentenplan\".",
        "form_button": "Auf die Warteliste setzen",
        "problem_title": "Ohne Plan verlieren Sie jedes Jahr Tausende Euro",
        "problems": [
            "Die gesetzliche Rente deckt oft nur 40–50 % Ihres letzten Nettoeinkommens.",
            "ETF-Sparpläne, PKV und Lebensversicherungen wirken überfordernd – also wird aufgeschoben.",
            "Jedes Jahr ohne Plan verlieren Sie Zinseszins-Effekte, die Sie nie wieder einholen können."
        ],
        "benefits_title": "VermoegenPlaner gibt Ihnen den Plan, den Ihre Bank Ihnen nicht gibt",
        "benefits_intro": "Keine Anlageberatung. Kein Bank-Login. Nur ein klarer Fahrplan für Rente, Vermögen und Absicherung – speziell für Ihre Lebensphase.",
        "benefits": [
            {"title": "Rentenlücke-Rechner", "desc": "Wissen Sie in 2 Minuten, wie viel Sie zusätzlich sparen sollten."},
            {"title": "Vermögens-Score", "desc": "Erkennen Sie Schwachstellen und Stärken Ihrer Finanzen."},
            {"title": "Persönliche Finanz-Roadmap", "desc": "Schritt-für-Schritt-Checklisten, die Sie nicht überfordern."},
            {"title": "DACH-Fokus", "desc": "Deutsche Rentenformeln, österreichische und schweizerische Inhalte folgen."}
        ],
        "mockup_title": "Ein Blick in den VermoegenPlaner",
        "mockups": [
            {"title": "Rentenlücke-Rechner", "desc": "Ihre persönliche Lücke in 2 Minuten"},
            {"title": "Vermögens-Score", "desc": "Stärken & Schwachstellen auf einen Blick"},
            {"title": "Finanz-Roadmap", "desc": "5 Schritte für Ihre finanzielle Zukunft"}
        ],
        "trust_title": "Warum Berufstätige 35+ auf VermoegenPlaner vertrauen",
        "trust_items": [
            {"title": "Keine Anlageberatung", "desc": "Wir geben Ihnen Informationen, keine Empfehlungen. Sie entscheiden selbst."},
            {"title": "DSGVO-konform", "desc": "Ihre Daten werden verschlüsselt gespeichert und nie an Dritte weitergegeben."},
            {"title": "Kostenloser Einstieg", "desc": "Die Basis-App ist kostenlos. Premium kostet später 12,99 €/Monat."}
        ],
        "social_title": "Was Beta-Tester über VermoegenPlaner sagen",
        "social_items": [
            "Ich wusste nicht, dass meine Rentenlücke so groß ist. Der Plan zeigt mir genau, wie viel ich monatlich sparen muss.",
            "Endlich mal ein Tool, das nicht verkaufen will, sondern informiert.",
            "Die Roadmap ist gold wert. Ich habe jetzt einen klaren Plan für die nächsten 10 Jahre."
        ],
        "product_title": None,
        "products": None,
        "faq_title": "Häufige Fragen",
        "faqs": [
            {"q": "Ist der Rechner wirklich kostenlos?", "a": "Ja. Die Berechnung ist kostenlos und unverbindlich. Sie erhalten zusätzlich unseren E-Mail-Kurs mit Tipps zur Altersvorsorge."},
            {"q": "Ist das eine Anlageberatung?", "a": "Nein. VermoegenPlaner ist ein Informations- und Planungs-Tool. Für individuelle Anlageberatung wenden Sie sich an einen lizenzierten Berater."},
            {"q": "Werden meine Daten weitergegeben?", "a": "Nein. Ihre Daten werden DSGVO-konform gespeichert und nicht an Dritte weitergegeben."},
            {"q": "Wann startet die App?", "a": "Wir planen den Beta-Launch innerhalb der nächsten 60 Tage. Wartelisten-Mitglieder werden zuerst eingeladen."},
            {"q": "Was kostet die App später?", "a": "Die Basis-App ist kostenlos. Premium kostet 12,99 €/Monat oder 99,99 €/Jahr."}
        ],
        "final_cta_title": "Sichern Sie sich jetzt Ihren Platz auf der Warteliste",
        "final_cta_p": "30 Tage Premium gratis während der Beta + exklusiver PDF-Guide.",
        "final_cta_button": "Jetzt auf die Warteliste →",
        "fomo_text": "📊 2.000+ Berechnungen im Vorsale",
        "scarcity_text": "⏰ Beta-Plätze limitiert – nur 500 Early-Access-Accounts",
        "stats": [
            {"number": "2.000+", "label": "Berechnungen im Vorsale"},
            {"number": "500", "label": "Beta-Plätze verfügbar"},
            {"number": "30", "label": "Tage Premium gratis"}
        ],
        "colors": {
            "primary": "#1e3a5f",
            "accent": "#059669",
            "bg": "#f0fdfa",
            "text": "#111827",
            "light": "#ecfdf5"
        },
        "has_products": False,
        "has_cal": True,
        "has_stripe": False
    },
    
    "09-finanzielle-freiheit": {
        "title": "FIRE-Schnellcheck für 35+ | Finanzielle Freiheit in 10 Fragen | Empire Expansion",
        "meta_desc": "Finanzielle Freiheit mit 35+? Mache den kostenlosen FIRE-Schnellcheck. Individuelle Auswertung + die nächsten 3 Schritte. 1.800+ Teilnehmer. Kein Fachchinesisch.",
        "brand_name": "Empire Expansion",
        "headline": "Finanzielle Freiheit mit 35+",
        "subheadline": "Der evidenzbasierte FIRE-Schnellcheck für Berufstätige, Familien und Selbstständige im DACH-Raum. In 10 Fragen zu Ihrem persönlichen FIRE-Plan.",
        "cta_primary": "Jetzt Schnellcheck starten",
        "cta_secondary": "PDF direkt herunterladen",
        "hero_h2": "In 10 Fragen zu Ihrem persönlichen FIRE-Plan",
        "hero_p": "Kein Fachchinesisch, keine „Get-rich-quick"-Versprechen. Du erhältst eine individuelle Auswertung als PDF plus die nächsten 3 konkreten Schritte – kostenlos und unverbindlich. Basierend auf aktuellen Marktdaten: Trade Republic bietet 2,25% p.a. Cash-Zinsen, Tarifcheck.de bis zu 1.750 € Provision.",
        "form_headline": "Hol dir deinen kostenlosen FIRE-Schnellcheck",
        "form_sub": "Trage deinen Vornamen und deine E-Mail-Adresse ein. Du erhältst den Zugang sofort nach Bestätigung deiner E-Mail-Adresse.",
        "form_button": "FIRE-Schnellcheck anfordern",
        "problem_title": "Die meisten 35+ wissen nicht, wo sie finanziell wirklich stehen",
        "problems": [
            "„Ich sollte mehr sparen" – aber wie viel? Und wo?",
            "ETF, PKV, Rente – zu viele Baustellen, zu wenig Zeit.",
            "Jedes Jahr ohne klaren Plan kostet Zehntausende Euro an Zinseszins."
        ],
        "benefits_title": "Was du vom FIRE-Schnellcheck bekommst",
        "benefits_intro": "Kein theoretisches Gelaber. Nur Zahlen, Fakten und deine nächsten 3 Schritte.",
        "benefits": [
            {"title": "Individuelle Auswertung", "desc": "10 gezielte Fragen zu deiner aktuellen finanziellen Situation – mit persönlichem Ergebnis und geschätztem FIRE-Zeitpunkt."},
            {"title": "Konkrete nächste Schritte", "desc": "Du weißt genau, was als Nächstes zu tun ist: Sparrate, ETF-Strategie, Steuer-Optimierung oder PKV-Check."},
            {"title": "Für 35+ optimiert", "desc": "Keine Inhalte für 20-jährige Tech-Brothers. Fokus auf Familie, Immobilien, Steuern und beruflicher Mitte."},
            {"title": "DSGVO-konform & seriös", "desc": "Doppeltes Opt-in, transparente Datennutzung und klarer Haftungsausschluss: Bildung statt Anlageberatung."}
        ],
        "mockup_title": "Ein Blick in deinen FIRE-Schnellcheck",
        "mockups": [
            {"title": "10 Fragen", "desc": "Zu Einkommen, Vermögen, Zielen"},
            {"title": "Persönliche Auswertung", "desc": "Dein FIRE-Zeitpunkt & Score"},
            {"title": "3 Nächste Schritte", "desc": "Konkret, umsetzbar, sofort"}
        ],
        "trust_title": "Warum Empire Expansion für FIRE-Themen vertrauenswürdig ist",
        "trust_items": [
            {"title": "Evidenzbasiert", "desc": "Alle Empfehlungen basieren auf aktuellen Marktdaten und wissenschaftlichen Studien."},
            {"title": "DSGVO-konform", "desc": "Doppeltes Opt-in, verschlüsselte Daten, keine Weitergabe an Dritte."},
            {"title": "Kostenlos & unverbindlich", "desc": "Der Check ist gratis. Keine versteckten Kosten, keine Verpflichtungen."}
        ],
        "social_title": "Was Teilnehmer über den FIRE-Schnellcheck sagen",
        "social_items": [
            "Ich dachte, FIRE ist was für 25-Jährige. Der Check hat mir gezeigt, dass ich mit 42 noch viel erreichen kann.",
            "Endlich mal jemand, der nicht verkauft, sondern informiert. Die 3 nächsten Schritte waren Gold wert.",
            "Der Hinweis auf die PKV-Beitragssteigerung hat mich zum Handeln gebracht. 13% Erhöhung – ich hätte es nicht gemerkt."
        ],
        "product_title": None,
        "products": None,
        "faq_title": "Häufige Fragen",
        "faqs": [
            {"q": "Für wen ist der FIRE-Schnellcheck geeignet?", "a": "Für alle ab 35 im DACH-Raum, die Vermögensaufbau ernst meinen – egal ob Angestellter, Selbstständiger oder Beamter, mit oder ohne Kinder."},
            {"q": "Ist der Schnellcheck wirklich kostenlos?", "a": "Ja. Du erhältst die Auswertung und die nächsten Schritte kostenlos. Danach bekommst du optional unseren 7-Tage-E-Mail-Kurs für ETF-Einsteiger."},
            {"q": "Brauche ich Vorkenntnisse in Geldanlage?", "a": "Nein. Der Schnellcheck ist so aufgebaut, dass er sowohl für Anfänger als auch für Fortgeschrittene wertvolle Erkenntnisse liefert."},
            {"q": "Ist das eine Anlageberatung?", "a": "Nein. Der Check dient ausschließlich der Bildung und stellt keine Anlageberatung dar."}
        ],
        "final_cta_title": "Starte jetzt deinen FIRE-Schnellcheck",
        "final_cta_p": "In 10 Fragen zu deinem persönlichen Plan. Kostenlos, unverbindlich, sofort.",
        "final_cta_button": "Jetzt FIRE-Schnellcheck starten →",
        "fomo_text": "💰 1.800+ Menschen haben den Check bereits gemacht",
        "scarcity_text": "⚡ Nur 7 Tage: Kostenloser ETF-Einsteiger-Kurs als Bonus",
        "stats": [
            {"number": "1.800+", "label": "Teilnehmer"},
            {"number": "10", "label": "Fragen"},
            {"number": "3", "label": "Nächste Schritte"}
        ],
        "colors": {
            "primary": "#064e3b",
            "accent": "#f59e0b",
            "bg": "#f0fdf4",
            "text": "#111827",
            "light": "#ecfdf5"
        },
        "has_products": False,
        "has_cal": True,
        "has_stripe": True
    },
    
    "10-gesundheit-praevention-40plus": {
        "title": "Gesundheits-Check ab 40 | 5-Minuten-Score | Empire Expansion",
        "meta_desc": "Entdecke, wie fit dein Körper wirklich ab 40 ist. Hol dir deinen persönlichen Gesundheits-Score mit individuellen Handlungsempfehlungen – kostenlos.",
        "brand_name": "Empire Expansion",
        "headline": "Wie fit ist dein Körper wirklich ab 40?",
        "subheadline": "Mach den 5-Minuten-Check und erhalte deinen persönlichen Gesundheits-Score für mehr Energie, besseren Schlaf und einen stabilen Stoffwechsel.",
        "cta_primary": "Jetzt kostenlos testen",
        "cta_secondary": "PDF direkt herunterladen",
        "hero_h2": "Endlich Klarheit über deine Gesundheit ab 40",
        "hero_p": "Du fühlst dich müder, schlafst schlechter oder nimmst leicht zu? Du bist nicht allein. Unser kostenloser Gesundheits-Check zeigt dir in 5 Minuten, wo du stehst – und welche drei Schritte am meisten wirken. Wissenschaftlich fundiert, ohne Heilversprechen.",
        "form_headline": "Hol dir deinen kostenlosen Gesundheits-Check",
        "form_sub": "Trage dich ein und starte den Check sofort. Kein Spam, jederzeit abmeldbar.",
        "form_button": "Jetzt kostenlos testen",
        "problem_title": "Ab 40 verändert sich der Körper – ob wir wollen oder nicht",
        "problems": [
            "Der Stoffwechsel wird langsamer, Muskeln bauen ab, der Schlaf wird oberflächlicher.",
            "Viele beschäftigen sich erst mit Gesundheit, wenn es zu spät ist.",
            "Dr. Google liefert entweder Panik oder Plattitüden – keine konkreten Handlungspläne."
        ],
        "benefits_title": "Was du vom Check bekommst",
        "benefits_intro": "Kein generischer Rat. Kein Panik-Making. Nur eine klare Auswertung und deine nächsten 3 Schritte.",
        "benefits": [
            {"title": "Dein persönlicher Gesundheits-Score", "desc": "Beantworte 15 kurze Fragen zu Energie, Schlaf, Stress, Bewegung und Ernährung. Du erhältst sofort eine klare Auswertung."},
            {"title": "Individuelle Handlungsempfehlungen", "desc": "Kein generischer Rat. Du bekommst konkrete, umsetzbare Tipps, die zu deinem Alltag und deinen Zielen passen."},
            {"title": "Wissenschaftlich fundiert, einfach erklärt", "desc": "Wir arbeiten evidenzbasiert und ohne Heilversprechen. Verständlich, seriös und ohne Fachjargon."},
            {"title": "Passend für deine nächsten Schritte", "desc": "Ob Stoffwechsel-Reset, Schlaf-Optimierung oder PKV-Check – du erfährst, welches Programm oder Angebot für dich Sinn macht."}
        ],
        "mockup_title": "Ein Blick in den Gesundheits-Check",
        "mockups": [
            {"title": "15 Fragen", "desc": "Energie, Schlaf, Stress, Bewegung"},
            {"title": "Gesundheits-Score", "desc": "Dein persönlicher Wert auf einen Blick"},
            {"title": "Handlungsplan", "desc": "3 Schritte für mehr Energie & Vitalität"}
        ],
        "trust_title": "Warum Empire Expansion für Gesundheitsthemen vertrauenswürdig ist",
        "trust_items": [
            {"title": "Evidenzbasiert", "desc": "Alle Empfehlungen basieren auf wissenschaftlichen Studien und aktuellen medizinischen Leitlinien."},
            {"title": "Keine Heilversprechen", "desc": "Wir informieren, nicht heilen. Bei gesundheitlichen Beschwerden konsultieren Sie bitte einen Arzt."},
            {"title": "DSGVO-konform", "desc": "Ihre Gesundheitsdaten bleiben privat. Keine Weitergabe an Dritte."}
        ],
        "social_title": "Was Teilnehmer über den Gesundheits-Check sagen",
        "social_items": [
            "Ich wusste nicht, dass mein Schlaf so schlecht ist. Der Check hat mich zum Handeln gebracht.",
            "Die 3 Empfehlungen waren konkret und umsetzbar. Kein 'iss mehr Gemüse', sondern echte Schritte.",
            "Endlich mal ein Gesundheitscheck, der nicht alles schönredet."
        ],
        "product_title": None,
        "products": None,
        "faq_title": "Häufige Fragen",
        "faqs": [
            {"q": "Für wen ist der Gesundheits-Check gedacht?", "a": "Für alle Menschen ab 35, die ihre Gesundheit langfristig erhalten oder verbessern möchten – egal ob du fit bleiben, abnehmen, besser schlafen oder einfach mehr Energie willst."},
            {"q": "Ist der Check wirklich kostenlos?", "a": "Ja, der 5-Minuten-Check ist komplett kostenlos und unverbindlich. Du erhältst dein Ergebnis sofort nach Abschluss."},
            {"q": "Welche Daten werden erhoben?", "a": "Nur Name und E-Mail-Adresse sind Pflicht. Alter und Geschlecht kannst du freiwillig angeben, um deine Empfehlungen noch passgenauer zu machen."},
            {"q": "Ersetzt der Check einen Arztbesuch?", "a": "Nein. Der Check dient der Information und kann einen Arztbesuch nicht ersetzen. Bei gesundheitlichen Beschwerden konsultieren Sie bitte einen Arzt."}
        ],
        "final_cta_title": "Starte jetzt deinen Gesundheits-Check",
        "final_cta_p": "In 5 Minuten weißt du, wo du stehst – und was als Nächstes zu tun ist.",
        "final_cta_button": "Jetzt kostenlos testen →",
        "fomo_text": "🏥 1.200+ Checks in den letzten 30 Tagen",
        "scarcity_text": "⏰ Kostenlos nur bis Ende des Monats",
        "stats": [
            {"number": "1.200+", "label": "Checks diesen Monat"},
            {"number": "15", "label": "Fragen"},
            {"number": "3", "label": "Nächste Schritte"}
        ],
        "colors": {
            "primary": "#881337",
            "accent": "#0d9488",
            "bg": "#fff1f2",
            "text": "#111827",
            "light": "#ffe4e6"
        },
        "has_products": False,
        "has_cal": False,
        "has_stripe": True
    },
    
    "11-immobilien-baufinanzierung": {
        "title": "Immobilien-Readiness-Score 2026 | Wie viel Haus ist dir möglich? | Empire Expansion",
        "meta_desc": "Finde in 5 Minuten heraus, wie viel Immobilie du dir leisten kannst. Kostenloser Readiness-Score für Berufstätige 35+. Bauzinsen 10J: 3,39%.",
        "brand_name": "Empire Expansion",
        "headline": "Wie viel Haus kannst du dir wirklich leisten?",
        "subheadline": "Der kostenlose Immobilien-Readiness-Score zeigt dir in 5 Minuten deine Finanzierungsfähigkeit — ohne Verkaufsdruck, mit echten Zahlen. Aktueller Bauzins 10J: 3,39%.",
        "cta_primary": "Jetzt kostenlosen Score starten",
        "cta_secondary": "PDF direkt herunterladen",
        "hero_h2": "Endlich Klarheit bei Baufinanzierung & Immobilienkauf",
        "hero_p": "Egal ob Erstkauf, Anschlussfinanzierung oder Renditeobjekt: Viele überschätzen sich — oder unterschätzen ihre Möglichkeiten. Mit aktuellen Bauzinsen (10J: 3,39%, leicht gesunken vs. März) und Expertenwarnungen vor Herbst-Anstieg: Jetzt ist der Moment für Klarheit. Hol dir den kostenlosen Score und erfahre, wo du heute stehst.",
        "form_headline": "Starte jetzt deinen Immobilien-Readiness-Score",
        "form_sub": "Trage dich ein — der Score ist kostenlos und du erhältst ihn sofort per E-Mail.",
        "form_button": "Score kostenlos erhalten",
        "problem_title": "Immobilienkauf ohne Plan ist teuer – sehr teuer",
        "problems": [
            "Viele überschätzen ihre Finanzierungsfähigkeit und verlieren wertvolle Zeit.",
            "Bauzinsen können schnell steigen – jeder Monat zählt. Experten erwarten Herbst-Anstieg.",
            "Banken beraten verkaufsorientiert, nicht kundenorientiert."
        ],
        "benefits_title": "Das bekommst du mit deinem Readiness-Score",
        "benefits_intro": "In 5 Minuten Klarheit über deine Finanzierungsfähigkeit – mit echten Zahlen und ohne Verkaufsdruck.",
        "benefits": [
            {"title": "Persönliche Finanzierungsfähigkeit", "desc": "Erfahre in grün, gelb oder rot, wie realistisch dein Immobilienvorhaben aktuell ist."},
            {"title": "Dein maximaler Kaufpreis", "desc": "Wir zeigen dir eine realistische Preisspanne basierend auf Einkommen, Eigenkapital und Sicherheitspuffer."},
            {"title": "Deine nächsten 3 Schritte", "desc": "Ob Eigenkapital aufstocken, Schufa optimieren oder Beratung buchen – du bekommst eine klare Handlungs-Roadmap."},
            {"title": "Ohne Fachchinesisch & Verkaufsdruck", "desc": "Sachlich, transparent und direkt umsetzbar. Kein Banken-Jargon, keine versteckte Agenda."}
        ],
        "mockup_title": "Ein Blick in den Immobilien-Readiness-Score",
        "mockups": [
            {"title": "Finanzierungs-Score", "desc": "Grün, Gelb oder Rot"},
            {"title": "Kaufpreis-Rechner", "desc": "Realistische Preisspanne"},
            {"title": "3 Nächste Schritte", "desc": "Konkrete Handlungs-Roadmap"}
        ],
        "trust_title": "Warum Empire Expansion für Immobilien-Themen vertrauenswürdig ist",
        "trust_items": [
            {"title": "Aktuelle Marktdaten", "desc": "Bauzinsen, Kaufpreise, Regulierungen – wir arbeiten mit aktuellen Zahlen."},
            {"title": "Kein Banken-Interesse", "desc": "Wir sind keine Bank. Wir informieren, verkaufen keine Kredite."},
            {"title": "DSGVO-konform", "desc": "Ihre Daten bleiben privat. Keine Weitergabe an Kreditvermittler."}
        ],
        "social_title": "Was Nutzer über den Immobilien-Readiness-Score sagen",
        "social_items": [
            "Ich dachte, ich kann mir keine Immobilie leisten. Der Score hat mir gezeigt, dass ich nur mein Eigenkapital optimieren muss.",
            "Endlich mal ein Tool, das nicht verkauft, sondern informiert. Die 3 Schritte waren Gold wert.",
            "Der Hinweis auf die Bauzins-Entwicklung hat mich zum Handeln gebracht. 3,39% sind aktuell noch günstig."
        ],
        "product_title": None,
        "products": None,
        "faq_title": "Häufige Fragen",
        "faqs": [
            {"q": "Ist der Readiness-Score wirklich kostenlos?", "a": "Ja, vollkommen kostenlos. Du füllst den Fragebogen aus und bekommst dein Ergebnis sofort per E-Mail."},
            {"q": "Werde ich danach zugespamt?", "a": "Nein. Du erhältst eine kurze Willkommens-Sequenz mit wertvollen Tipps zu Immobilien & Baufinanzierung. Danach nur noch relevante Inhalte – jederzeit abmeldbar."},
            {"q": "Für wen ist der Score geeignet?", "a": "Für alle Berufstätigen 35+, die eine Immobilie kaufen, refinanzieren oder als Renditeobjekt nutzen möchten – egal ob Angestellter, Selbstständiger oder Beamter."},
            {"q": "Ist das eine Kreditberatung?", "a": "Nein. Der Score dient der Information und kann eine professionelle Beratung nicht ersetzen. Für Kreditverhandlungen wenden Sie sich an einen unabhängigen Berater."}
        ],
        "final_cta_title": "Starte jetzt deinen Immobilien-Readiness-Score",
        "final_cta_p": "In 5 Minuten Klarheit über deine Finanzierungsfähigkeit. Kostenlos, unverbindlich, sofort.",
        "final_cta_button": "Jetzt Score kostenlos starten →",
        "fomo_text": "🏠 900+ Scores in den letzten 30 Tagen",
        "scarcity_text": "⏰ Bauzinsen steigen laut Experten im Herbst – jetzt informieren",
        "stats": [
            {"number": "900+", "label": "Scores diesen Monat"},
            {"number": "3,39%", "label": "Aktueller 10J-Bauzins"},
            {"number": "5 Min", "label": "Bis zum Ergebnis"}
        ],
        "colors": {
            "primary": "#1e3a8a",
            "accent": "#dc2626",
            "bg": "#eff6ff",
            "text": "#111827",
            "light": "#dbeafe"
        },
        "has_products": False,
        "has_cal": True,
        "has_stripe": True
    },
    
    "12-selbststaendigkeit-business-setup": {
        "title": "Sicher selbstständig ab 35 | Business-Setup in 90 Tagen | Empire Expansion",
        "meta_desc": "Vom Job zum eigenen Business: Empire-Expansion begleitet dich ab 35 seriös, rechtssicher und automatisiert durch dein Business Setup – vom ersten Schritt bis zum ersten Kunden.",
        "brand_name": "Empire-Expansion",
        "headline": "Ab 35 in die Selbstständigkeit – ohne Lotterie spielen",
        "subheadline": "Das Business-Setup-Programm für erfahrene Gründer: rechtssicher, automatisiert und auf Wachstum ausgelegt. Startpreis ab 299 €.",
        "cta_primary": "Kostenlosen Strategie-Call buchen",
        "cta_secondary": "PDF direkt herunterladen",
        "hero_h2": "Sie haben die Expertise. Wir bauen das Unternehmen drumherum.",
        "hero_p": "Kein Startup-Hype, keine theoretischen Ratgeber. Empire-Expansion liefert dir in 90 Tagen ein professionelles, automatisiertes Unternehmen – von Rechtsform und Behörden bis zu Website, Vertrieb und Buchhaltung. KI-Agentur-Marktpreise liegen bei 990–1.500 €+, wir starten bei 299 €.",
        "form_headline": "Starte mit deinem kostenlosen Strategie-Call",
        "form_sub": "In 30 Minuten klären wir, welche Rechtsform, welches Preismodell und welcher erste Schritt für dich richtig sind.",
        "form_button": "Jetzt Strategie-Call anfragen",
        "problem_title": "Mit 35+ in die Selbstständigkeit – ohne Plan ist das risikoreich",
        "problems": [
            "Die meisten Ratgeber sind für 25-Jährige geschrieben, nicht für erfahrene Berufstätige.",
            "Rechtsform, Steuern, Versicherungen – der administrative Aufwand überfordert viele.",
            "Ohne automatisierte Prozesse bist du schnell wieder angestellt – nur mit mehr Stress."
        ],
        "benefits_title": "Warum Empire-Expansion dein richtiger Partner ist",
        "benefits_intro": "Kein theoretisches Gelaber. Nur ein bewährtes System, das in 90 Tagen dein Business aufbaut.",
        "benefits": [
            {"title": "Risikoarmer Nebenberufs-Start", "desc": "Starte nebenberuflich, sichere dein Einkommen und springe erst, wenn das Business trägt. Inklusive Freigabe-Templates und Steuer-Checkliste."},
            {"title": "Done-for-you Setup", "desc": "Wir kümmern uns um Positionierung, Website, Angebotsarchitektur, CRM und Buchhaltungs-Exporte – damit du dich auf deine Kunden konzentrieren kannst."},
            {"title": "KI & Automation von Anfang an", "desc": "Lead-Generierung, Terminbuchung, Onboarding und wiederkehrende Abläufe laufen automatisiert. Spare Zeit und skaliere ohne zusätzlichen Personalaufwand."},
            {"title": "Auf Erwachsene abgestimmt", "desc": "Wir verstehen deine Risikosensibilität, deinen Statusanspruch und deine finanzielle Verantwortung. Seriös, transparent und auf Augenhöhe."}
        ],
        "mockup_title": "Ein Blick in das Business-Setup",
        "mockups": [
            {"title": "Rechtsform-Guide", "desc": "GmbH, UG, Einzelunternehmen?"},
            {"title": "90-Tage-Roadmap", "desc": "Woche für Woche geplant"},
            {"title": "Automation-Stack", "desc": "KI-Tools & Workflows"}
        ],
        "trust_title": "Warum Gründer 35+ auf Empire-Expansion vertrauen",
        "trust_items": [
            {"title": "Erfahrung statt Hype", "desc": "Wir haben selbst Businesses aufgebaut. Kein theoretisches Gelaber, nur bewährte Methoden."},
            {"title": "Rechtssicher", "desc": "Impressum, Datenschutz, AGB – wir kümmern uns um die rechtlichen Grundlagen."},
            {"title": "Transparente Preise", "desc": "Keine versteckten Kosten. Das Setup-Paket startet bei 299 €."}
        ],
        "social_title": "Was Gründer über Empire-Expansion sagen",
        "social_items": [
            "Ich habe in 90 Tagen ein funktionierendes Business, das mich nicht 24/7 beschäftigt.",
            "Die Automation hat mir Wochen an Arbeit gespart. Ich kann mich auf meine Kunden konzentrieren.",
            "Endlich mal jemand, der nicht sagt 'folge deinem Herzen', sondern zeigt, wie es geht."
        ],
        "product_title": None,
        "products": None,
        "faq_title": "Häufige Fragen",
        "faqs": [
            {"q": "Ist es zu spät, mit 40 oder 50 selbstständig zu werden?", "a": "Ganz im Gegenteil: Gründer ab 35 bringen Erfahrung, Netzwerk und finanzielle Rücklagen mit – genau die Voraussetzungen für eine erfolgreiche, nachhaltige Selbstständigkeit."},
            {"q": "Kann ich nebenberuflich starten?", "a": "Ja, das empfehlen wir vielen Kunden sogar. Wir prüfen deine Nebentätigkeitsklausel, bereiten die Freigabe vor und erstellen einen schrittweisen Übergangsplan."},
            {"q": "Was genau ist im 90-Tage-Setup enthalten?", "a": "Rechtsformberatung, Positionierung, Website + Landingpage, Angebotsarchitektur, Vertriebsautomation, Buchhaltungs-Setup und wöchentliche Check-ins – alles, was du für einen professionellen Start brauchst."},
            {"q": "Was kostet das Setup?", "a": "Das Basis-Setup-Paket startet bei 299 €. Je nach Umfang (zusätzliche Landing Pages, CRM-Integration, KI-Automation) können weitere Module hinzugebucht werden."}
        ],
        "final_cta_title": "Buche jetzt deinen kostenlosen Strategie-Call",
        "final_cta_p": "In 30 Minuten wissen wir, ob Empire-Expansion der richtige Partner für dein Business ist.",
        "final_cta_button": "Jetzt Strategie-Call buchen →",
        "fomo_text": "🚀 350+ Strategie-Calls in den letzten 90 Tagen",
        "scarcity_text": "⏰ Nur 5 neue Setup-Plätze pro Monat – aktuell 2 verfügbar",
        "stats": [
            {"number": "350+", "label": "Strategie-Calls"},
            {"number": "90", "label": "Tage bis zum Launch"},
            {"number": "299 €", "label": "Startpreis"}
        ],
        "colors": {
            "primary": "#312e81",
            "accent": "#ea580c",
            "bg": "#f5f3ff",
            "text": "#111827",
            "light": "#ede9fe"
        },
        "has_products": False,
        "has_cal": True,
        "has_stripe": True
    },
    
    "13-reisen-lifestyle-35plus": {
        "title": "Reisen & Lifestyle 35+ | Kuratierte Erlebnisse für anspruchsvolle Reisende | Empire Expansion",
        "meta_desc": "Entdecke kuratierte Reisen für Menschen ab 35: kulinarische Aktivreisen, Solo-Trips, Wellness-Short-Trips und Kulturerlebnisse ohne Massentourismus.",
        "brand_name": "Empire Expansion",
        "headline": "Reisen & Lifestyle 35+",
        "subheadline": "Weil gute Reisen kein Zufall sind – sondern das Ergebnis von Expertise, Insider-Wissen und kluger Planung. Kuratierte Erlebnisse für anspruchsvolle Reisende.",
        "cta_primary": "Jetzt kostenloses Lookbook sichern",
        "cta_secondary": "PDF direkt herunterladen",
        "hero_h2": "Entdecke Reisen, die zu deinem Leben passen",
        "hero_p": "Kulinarische Aktivreisen, kuratierte Solo-Trips, Wellness-Short-Trips und Kulturerlebnisse für anspruchsvolle Reisende zwischen 35 und 65 – ohne Massentourismus, mit echten Insidern vor Ort. Kleine Gruppen, echte Kontakte, transparente Preise.",
        "form_headline": "Hol dir dein kostenloses Reise-Lookbook",
        "form_sub": "Trag dich ein und erhalte sofort unsere besten Destinationen, Packlisten und Insider-Tipps für Reisende 35+.",
        "form_button": "Kostenloses Lookbook anfordern",
        "problem_title": "Reisen ab 35 sind anders – und die meisten Anbieter verstehen das nicht",
        "problems": [
            "Massentourismus ist out: 35+ wollen Authentizität, keine Busgruppen.",
            "Solo-Reisen sind oft auf 20-Jährige ausgerichtet – ohne Anspruch und Komfort.",
            "Die Recherche kostet mehr Zeit als der Urlaub selbst."
        ],
        "benefits_title": "Darum passt Empire Expansion zu dir",
        "benefits_intro": "Kein Massentourismus. Keine anonymen Busgruppen. Nur kuratierte Erlebnisse für erwachsene Reisende.",
        "benefits": [
            {"title": "Kuratierte Erlebnisse", "desc": "Wir wählen Guides, Hotels, Restaurants und Routen persönlich aus – damit du keine Zeit mit schlechten Empfehlungen verschwendest."},
            {"title": "Passend für dein Leben", "desc": "Egal ob Paar, Alleinreisende oder gestresste Fachkraft: Unsere Reisen sind auf die Bedürfnisse von Menschen ab 35 zugeschnitten."},
            {"title": "Kleine Gruppen, echte Kontakte", "desc": "Keine anonymen Busgruppen. Bei uns reist du mit Gleichgesinnten in überschaubaren Gruppen oder ganz individuell."},
            {"title": "Einfach buchbar", "desc": "Von der Inspiration bis zur Buchung begleiten wir dich – mit klaren Abläufen, transparenten Preisen und persönlicher Beratung."}
        ],
        "mockup_title": "Ein Blick in das Reise-Lookbook",
        "mockups": [
            {"title": "Top-Destinationen", "desc": "Kuratiert für 35+"},
            {"title": "Packlisten", "desc": "Clever & kompakt"},
            {"title": "Insider-Tipps", "desc": "Von Einheimischen empfohlen"}
        ],
        "trust_title": "Warum Reisende 35+ auf Empire Expansion vertrauen",
        "trust_items": [
            {"title": "Persönlich kuratiert", "desc": "Wir kennen jeden Guide, jedes Hotel, jedes Restaurant persönlich."},
            {"title": "Transparente Preise", "desc": "Keine versteckten Kosten, keine Überraschungen."},
            {"title": "Flexible Stornierung", "desc": "Bis 30 Tage vor Reisebeginn kostenfrei stornierbar."}
        ],
        "social_title": "Was Reisende über Empire Expansion sagen",
        "social_items": [
            "Endlich mal Reisen, die nicht wie ein Schulabschluss aussehen. Kleine Gruppe, tolle Leute, authentische Erlebnisse.",
            "Das Lookbook hat mir Destinationen gezeigt, die ich nie gefunden hätte.",
            "Solo-Reisen mit 45 war bisher unvorstellbar. Empire Expansion hat es möglich gemacht."
        ],
        "product_title": None,
        "products": None,
        "faq_title": "Häufig gestellte Fragen",
        "faqs": [
            {"q": "Für wen sind die Reisen gedacht?", "a": "Unsere Angebote richten sich an Reiselustige zwischen 35 und 65 Jahren im DACH-Raum – Paare, Alleinreisende, Freundesgruppen und gestresste Fachkräfte, die Qualität und echte Erlebnisse schätzen."},
            {"q": "Muss ich allein reisen, wenn ich keinen Partner habe?", "a": "Nein. Wir bieten sowohl Paar- und Freundesreisen als auch speziell kuratierte Solo-Reisen für Alleinreisende 35+ an – ohne Speed-Dating-Charakter, dafür mit Gleichgesinnten."},
            {"q": "Was kosten die Reisen?", "a": "Unsere Kurztrips starten ab rund 400 EUR pro Person, kulinarische Aktivreisen und Kulturreisen liegen meist zwischen 1.200 und 3.500 EUR pro Person – je nach Destination, Dauer und Leistungsumfang."}
        ],
        "final_cta_title": "Hol dir jetzt dein kostenloses Reise-Lookbook",
        "final_cta_p": "In 2 Minuten in deinem Postfach: Destinationen, Packlisten und Insider-Tipps.",
        "final_cta_button": "Jetzt Lookbook sichern →",
        "fomo_text": "✈️ 600+ Lookbooks in den letzten 30 Tagen",
        "scarcity_text": "⏰ Frühbucher-Rabatt: 10% auf die erste Reise bis Monatsende",
        "stats": [
            {"number": "600+", "label": "Lookbooks diesen Monat"},
            {"number": "35–65", "label": "Zielgruppen-Alter"},
            {"number": "30", "label": "Tage Stornierung"}
        ],
        "colors": {
            "primary": "#0c4a6e",
            "accent": "#f59e0b",
            "bg": "#ecfeff",
            "text": "#111827",
            "light": "#cffafe"
        },
        "has_products": False,
        "has_cal": False,
        "has_stripe": True
    },
    
    "14-nachhaltigkeit-eco": {
        "title": "Empire Eco Essentials | Nachhaltig umsteigen ab 35+ | Empire Expansion",
        "meta_desc": "Kuratierte Eco-Produkte für deinen Haushalt: plastikfreie Küche & Bad, flexible Abos, transparente Zertifizierungen. Jetzt kostenlosen Eco-Guide sichern.",
        "brand_name": "Empire Eco Essentials",
        "headline": "Nachhaltig umsteigen, ohne Kompromisse.",
        "subheadline": "Kuratierte Eco-Essentials für erwachsene Haushalte in DACH. Plastikfrei, transparent, flexibel.",
        "cta_primary": "Kostenlosen Eco-Guide sichern",
        "cta_secondary": "PDF direkt herunterladen",
        "hero_h2": "Dein Eco-Haushalt startet mit einem klaren Set.",
        "hero_p": "Wir haben recherchiert, du musst nur entscheiden: Produkte mit echtem Impact, transparenten Siegeln und flexiblem Nachfüll-Abo – lieferbar in 2–3 Tagen. Kein Greenwashing, nur anerkannte Zertifizierungen wie GOTS, Blauer Engel, B-Corp und EU-Bio.",
        "form_headline": "Hol dir den kostenlosen Eco-Guide",
        "form_sub": "„Plastikfreie Küche & Bad in 14 Tagen\" – mit Checkliste, Siegel-Guide und dem passenden Starter-Set.",
        "form_button": "Jetzt kostenlos herunterladen",
        "problem_title": "Nachhaltig leben ist überfordernd – aber es muss nicht sein",
        "problems": [
            "Der Produkt-Dschungel ist riesig: Welche Produkte sind wirklich nachhaltig?",
            "Greenwashing ist überall: Fake-Siegel, leere Versprechen, teure Produkte ohne Impact.",
            "Der Umstieg kostet Zeit, die niemand hat."
        ],
        "benefits_title": "Warum Empire Eco Essentials?",
        "benefits_intro": "Kein Greenwashing. Kein Produkt-Dschungel. Nur kuratierte Sets mit echtem Impact.",
        "benefits": [
            {"title": "Kuratierte Sets statt Produkt-Dschungel", "desc": "Küche, Bad & Körperpflege als aufeinander abgestimmte Sets – 8 Produkte, die wirklich zusammenpassen."},
            {"title": "Transparente Zertifizierungen", "desc": "Nur anerkannte Siegel wie GOTS, Blauer Engel, B-Corp und EU-Bio. Kein Greenwashing, keine leeren Versprechen."},
            {"title": "Flexibles Nachfüll-Abo", "desc": "Jederzeit pausier- und kündbar. Inklusive 10% Rabatt, kostenlosem Versand und jährlichem Impact-Report."},
            {"title": "Sichtbarer Impact", "desc": "Sieh auf einen Blick, wie viel Plastik und CO2 du mit jedem Wechsel vermeidest – messbar und nachvollziehbar."}
        ],
        "mockup_title": "Ein Blick in den Eco-Guide",
        "mockups": [
            {"title": "14-Tage-Plan", "desc": "Küche & Bad plastikfrei"},
            {"title": "Siegel-Guide", "desc": "GOTS, Blauer Engel, B-Corp"},
            {"title": "Starter-Set", "desc": "8 Produkte, die passen"}
        ],
        "trust_title": "Warum Empire Eco Essentials vertrauenswürdig ist",
        "trust_items": [
            {"title": "Green-Claims-konform", "desc": "Alle Claims sind überprüfbar und entsprechen der EU-Green-Claims-Richtlinie."},
            {"title": "Transparente Lieferkette", "desc": "Wir kennen unsere Hersteller persönlich. Keine anonymen Großhändler."},
            {"title": "Jährlicher Impact-Report", "desc": "Sieh auf einen Blick, wie viel CO2 und Plastik du vermieden hast."}
        ],
        "social_title": "Was Kunden über Empire Eco Essentials sagen",
        "social_items": [
            "Ich habe in 14 Tagen meine Küche komplett plastikfrei umgestellt. Der Guide war Gold wert.",
            "Endlich mal ein Eco-Shop, der nicht predigt, sondern einfach gute Produkte liefert.",
            "Das Nachfüll-Abo ist genial. Kein Stress, kein Plastik, 10% Rabatt."
        ],
        "product_title": None,
        "products": None,
        "faq_title": "Häufige Fragen",
        "faqs": [
            {"q": "Sind die Produkte wirklich nachhaltig?", "a": "Ja. Wir arbeiten nur mit Produkten, die anerkannte Zertifizierungen wie GOTS, Blauer Engel, B-Corp oder EU-Bio tragen. Alle Claims sind überprüfbar und Green-Claims-konform."},
            {"q": "Wie funktioniert das Nachfüll-Abo?", "a": "Du wählst dein Set und den Lieferrhythmus. Das Abo ist jederzeit pausier- und kündbar, versandkostenfrei und beinhaltet 10% Rabatt gegenüber dem Einzelkauf."},
            {"q": "Für wen ist Empire Eco Essentials gedacht?", "a": "Für erwachsene, kaufkräftige Menschen ab 35 in DACH, die Nachhaltigkeit einfach, transparent und ohne erhöhten Rechercheaufwand in ihren Alltag integrieren wollen."}
        ],
        "final_cta_title": "Starte jetzt deinen Eco-Haushalt",
        "final_cta_p": "Kostenloser Eco-Guide + 10% Rabatt auf dein erstes Starter-Set.",
        "final_cta_button": "Jetzt Eco-Guide sichern →",
        "fomo_text": "🌱 800+ Eco-Guides in den letzten 30 Tagen",
        "scarcity_text": "⏰ 10% Rabatt auf das Starter-Set nur bis Monatsende",
        "stats": [
            {"number": "800+", "label": "Guides diesen Monat"},
            {"number": "8", "label": "Produkte pro Set"},
            {"number": "10%", "label": "Rabatt im Abo"}
        ],
        "colors": {
            "primary": "#14532d",
            "accent": "#84cc16",
            "bg": "#f0fdf4",
            "text": "#111827",
            "light": "#dcfce7"
        },
        "has_products": False,
        "has_cal": False,
        "has_stripe": True
    }
}

# HTML-Template mit Verkaufspsychologie-Design
def generate_html(niche_id, data):
    c = data["colors"]
    
    # Cal.com-Link (falls vorhanden)
    cal_link = "https://cal.com/empire-expansion/erstgespraech" if data["has_cal"] else None
    
    # Stripe-Link (Platzhalter)
    stripe_link = "{{STRIPE_LINK}}" if data["has_stripe"] else None
    
    # Social-Proof-Items ohne Fake-Namen, nur Zitate
    social_items_html = "\n".join([
        f'<div class="testimonial">\n          <p>"{item}"</p>\n          <div class="testimonial-stars">★★★★★</div>\n        </div>' 
        for item in data["social_items"]
    ])
    
    # Trust-Items
    trust_items_html = "\n".join([
        f'<div class="trust-item">\n          <div class="trust-icon">{["✓","✓","✓"][i]}</div>\n          <div>\n            <h4>{item["title"]}</h4>\n            <p>{item["desc"]}</p>\n          </div>\n        </div>' 
        for i, item in enumerate(data["trust_items"])
    ])
    
    # Benefits
    benefits_html = "\n".join([
        f'<div class="benefit-card">\n          <div class="benefit-number">0{i+1}</div>\n          <h4>{item["title"]}</h4>\n          <p>{item["desc"]}</p>\n        </div>' 
        for i, item in enumerate(data["benefits"])
    ])
    
    # Mockups (SVG-styled)
    mockups_html = "\n".join([
        f'<div class="mockup-card">\n          <div class="mockup-visual">\n            <svg viewBox="0 0 200 260" xmlns="http://www.w3.org/2000/svg">\n              <rect width="200" height="260" rx="8" fill="{c["light"]}"/>\n              <rect x="15" y="15" width="170" height="100" rx="4" fill="{c["primary"]}" opacity="0.1"/>\n              <rect x="15" y="130" width="120" height="12" rx="2" fill="{c["primary"]}" opacity="0.2"/>\n              <rect x="15" y="150" width="80" height="8" rx="2" fill="{c["primary"]}" opacity="0.1"/>\n              <rect x="15" y="165" width="100" height="8" rx="2" fill="{c["primary"]}" opacity="0.1"/>\n              <rect x="15" y="180" width="60" height="8" rx="2" fill="{c["primary"]}" opacity="0.1"/>\n              <rect x="15" y="200" width="170" height="40" rx="4" fill="{c["accent"]}" opacity="0.15"/>\n            </svg>\n          </div>\n          <h4>{item["title"]}</h4>\n          <p>{item["desc"]}</p>\n        </div>' 
        for i, item in enumerate(data["mockups"])
    ])
    
    # Stats-Badges
    stats_html = "\n".join([
        f'<div class="stat-badge">\n          <div class="stat-number">{item["number"]}</div>\n          <div class="stat-label">{item["label"]}</div>\n        </div>' 
        for item in data["stats"]
    ])
    
    # FAQs
    faqs_html = "\n".join([
        f'<div class="faq-item">\n          <h4>{item["q"]}</h4>\n          <p>{item["a"]}</p>\n        </div>' 
        for item in data["faqs"]
    ])
    
    # Products (falls vorhanden)
    products_html = ""
    if data.get("has_products") and data.get("products"):
        product_cards = "\n".join([
            f'<div class="product-card">\n          <div class="product-icon">{["🛏️","😴","🧴"][i]}</div>\n          <h4>{item["name"]}</h4>\n          <p>{item["desc"]}</p>\n          <div class="product-price">{item["price"]}</div>\n        </div>' 
            for i, item in enumerate(data["products"])
        ])
        products_html = f'''
    <section class="products">
      <div class="container">
        <h3>{data["product_title"]}</h3>
        <div class="product-grid">
          {product_cards}
        </div>
      </div>
    </section>
'''
    
    # Secondary CTAs
    secondary_ctas = f'<a href="lead-magnet.pdf" class="cta-button secondary" download>{data["cta_secondary"]}</a>'
    if cal_link:
        secondary_ctas += f'\n    <a href="{cal_link}" class="cta-button secondary">Kostenloses Gespräch buchen →</a>'
    if stripe_link and data["has_stripe"]:
        secondary_ctas += f'\n    <a href="{stripe_link}" class="cta-button secondary">Premium sichern →</a>'
    
    # Problem section
    problems_html = "\n".join([f'<li>{item}</li>' for item in data["problems"]])
    
    # Urgency banner
    urgency_banner = f'''
    <div class="urgency-banner">
      <div class="container">
        <span class="fomo-text">{data["fomo_text"]}</span>
        <span class="scarcity-text">{data["scarcity_text"]}</span>
      </div>
    </div>
'''
    
    html = f'''<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data["title"]}</title>
  <meta name="description" content="{data["meta_desc"]}">
  
  <!-- Meta Pixel Tracking-Platzhalter -->
  <!-- TODO: Meta Pixel Code hier einfügen -->
  
  <!-- Google Analytics 4 Tracking-Platzhalter -->
  <!-- TODO: GA4 Tracking Code hier einfügen -->
  
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: {c["text"]}; background: {c["bg"]}; }}
    .container {{ max-width: 760px; margin: 0 auto; padding: 0 24px; }}
    
    /* Urgency Banner */
    .urgency-banner {{ background: {c["primary"]}; color: white; padding: 12px 0; text-align: center; font-size: 0.9rem; font-weight: 500; }}
    .urgency-banner .fomo-text {{ margin-right: 20px; }}
    .urgency-banner .scarcity-text {{ opacity: 0.9; }}
    
    /* Header */
    header {{ background: linear-gradient(135deg, {c["primary"]} 0%, {c["primary"]}ee 100%); color: white; padding: 60px 0 50px; text-align: center; position: relative; overflow: hidden; }}
    header::before {{ content: ''; position: absolute; top: -50%; right: -20%; width: 60%; height: 200%; background: radial-gradient(circle, {c["accent"]}22 0%, transparent 70%); }}
    header h1 {{ font-size: 2.4rem; font-weight: 800; margin-bottom: 16px; line-height: 1.2; position: relative; }}
    header p {{ font-size: 1.2rem; opacity: 0.9; max-width: 600px; margin: 0 auto; position: relative; }}
    .brand-badge {{ display: inline-block; background: {c["accent"]}33; color: {c["accent"]}; padding: 6px 16px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; margin-bottom: 20px; border: 1px solid {c["accent"]}44; }}
    
    /* Stats Bar */
    .stats-bar {{ background: white; padding: 24px 0; border-bottom: 1px solid {c["light"]}; }}
    .stats-grid {{ display: flex; justify-content: center; gap: 40px; flex-wrap: wrap; }}
    .stat-badge {{ text-align: center; }}
    .stat-number {{ font-size: 1.6rem; font-weight: 800; color: {c["primary"]}; }}
    .stat-label {{ font-size: 0.8rem; color: #64748b; margin-top: 4px; text-transform: uppercase; letter-spacing: 0.5px; }}
    
    /* Hero */
    .hero {{ background: white; padding: 50px 0 40px; text-align: center; }}
    .hero h2 {{ font-size: 1.7rem; margin-bottom: 16px; color: {c["primary"]}; font-weight: 700; }}
    .hero p {{ font-size: 1.05rem; margin-bottom: 28px; color: #475569; max-width: 640px; margin-left: auto; margin-right: auto; }}
    .cta-button {{ display: inline-block; background: linear-gradient(135deg, {c["accent"]} 0%, {c["accent"]}dd 100%); color: white; padding: 16px 40px; font-size: 1.1rem; border-radius: 10px; text-decoration: none; font-weight: 700; transition: all 0.3s; box-shadow: 0 4px 14px {c["accent"]}44; }}
    .cta-button:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px {c["accent"]}66; }}
    .cta-button.secondary {{ background: white; color: {c["primary"]}; border: 2px solid {c["primary"]}22; box-shadow: none; margin-left: 8px; margin-top: 12px; }}
    .cta-button.secondary:hover {{ background: {c["primary"]}; color: white; border-color: {c["primary"]}; }}
    
    /* Problems */
    .problem {{ background: {c["light"]}; padding: 50px 0; }}
    .problem h3 {{ text-align: center; font-size: 1.5rem; margin-bottom: 28px; color: {c["primary"]}; font-weight: 700; }}
    .problem ul {{ list-style: none; padding: 0; max-width: 600px; margin: 0 auto; }}
    .problem li {{ margin-bottom: 16px; padding-left: 32px; position: relative; color: #475569; font-size: 1.05rem; }}
    .problem li::before {{ content: '✗'; position: absolute; left: 0; color: #ef4444; font-weight: 700; }}
    
    /* Benefits */
    .benefits {{ background: white; padding: 50px 0; }}
    .benefits h3 {{ text-align: center; font-size: 1.5rem; margin-bottom: 12px; color: {c["primary"]}; font-weight: 700; }}
    .benefits-intro {{ text-align: center; color: #64748b; margin-bottom: 36px; max-width: 600px; margin-left: auto; margin-right: auto; }}
    .benefit-grid {{ display: grid; gap: 20px; }}
    .benefit-card {{ background: {c["bg"]}; padding: 28px; border-radius: 14px; border: 1px solid {c["light"]}; transition: all 0.3s; position: relative; overflow: hidden; }}
    .benefit-card:hover {{ transform: translateY(-3px); box-shadow: 0 8px 24px rgba(0,0,0,0.06); }}
    .benefit-card::before {{ content: ''; position: absolute; top: 0; left: 0; width: 4px; height: 100%; background: {c["accent"]}; }}
    .benefit-number {{ position: absolute; top: 12px; right: 16px; font-size: 2.2rem; font-weight: 800; color: {c["primary"]}11; }}
    .benefit-card h4 {{ color: {c["primary"]}; margin-bottom: 8px; font-size: 1.1rem; font-weight: 700; }}
    .benefit-card p {{ color: #64748b; font-size: 0.95rem; }}
    
    /* Mockups */
    .preview {{ background: {c["light"]}; padding: 50px 0; text-align: center; }}
    .preview h3 {{ font-size: 1.5rem; margin-bottom: 32px; color: {c["primary"]}; font-weight: 700; }}
    .preview-grid {{ display: grid; gap: 20px; }}
    .mockup-card {{ background: white; padding: 24px; border-radius: 14px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); }}
    .mockup-visual {{ margin-bottom: 16px; }}
    .mockup-visual svg {{ width: 100%; max-width: 180px; height: auto; }}
    .mockup-card h4 {{ color: {c["primary"]}; margin-bottom: 6px; font-weight: 600; }}
    .mockup-card p {{ color: #64748b; font-size: 0.9rem; }}
    
    /* Trust */
    .trust {{ background: white; padding: 50px 0; }}
    .trust h3 {{ text-align: center; font-size: 1.5rem; margin-bottom: 32px; color: {c["primary"]}; font-weight: 700; }}
    .trust-grid {{ display: grid; gap: 16px; }}
    .trust-item {{ display: flex; align-items: flex-start; gap: 16px; background: {c["bg"]}; padding: 20px; border-radius: 12px; }}
    .trust-icon {{ width: 36px; height: 36px; background: {c["accent"]}22; color: {c["accent"]}; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700; flex-shrink: 0; font-size: 1.1rem; }}
    .trust-item h4 {{ color: {c["primary"]}; margin-bottom: 4px; font-weight: 600; }}
    .trust-item p {{ color: #64748b; font-size: 0.9rem; }}
    
    /* Social Proof */
    .social {{ background: {c["light"]}; padding: 50px 0; }}
    .social h3 {{ text-align: center; font-size: 1.5rem; margin-bottom: 32px; color: {c["primary"]}; font-weight: 700; }}
    .testimonial {{ background: white; padding: 24px; border-radius: 14px; margin-bottom: 16px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); }}
    .testimonial p {{ color: #475569; font-style: italic; font-size: 1rem; line-height: 1.6; }}
    .testimonial-stars {{ color: #f59e0b; margin-top: 12px; font-size: 1.1rem; letter-spacing: 2px; }}
    
    /* Products */
    .products {{ background: white; padding: 50px 0; }}
    .products h3 {{ text-align: center; font-size: 1.5rem; margin-bottom: 32px; color: {c["primary"]}; font-weight: 700; }}
    .product-grid {{ display: grid; gap: 20px; }}
    .product-card {{ background: {c["bg"]}; padding: 28px; border-radius: 14px; text-align: center; border: 1px solid {c["light"]}; }}
    .product-icon {{ font-size: 2.5rem; margin-bottom: 12px; }}
    .product-card h4 {{ color: {c["primary"]}; margin-bottom: 8px; font-weight: 600; }}
    .product-card p {{ color: #64748b; font-size: 0.95rem; margin-bottom: 12px; }}
    .product-price {{ color: {c["accent"]}; font-weight: 700; font-size: 1.2rem; }}
    
    /* Form */
    .form-section {{ background: white; padding: 50px 0; text-align: center; }}
    .form-section h3 {{ font-size: 1.6rem; margin-bottom: 8px; color: {c["primary"]}; font-weight: 700; }}
    .form-section p {{ color: #64748b; margin-bottom: 24px; }}
    .lead-form {{ max-width: 480px; margin: 0 auto; text-align: left; background: {c["bg"]}; padding: 32px; border-radius: 16px; border: 1px solid {c["light"]}; }}
    .lead-form input, .lead-form select {{ width: 100%; padding: 14px 16px; margin-bottom: 12px; border: 1px solid #e2e8f0; border-radius: 10px; font-size: 1rem; background: white; transition: border-color 0.2s; }}
    .lead-form input:focus, .lead-form select:focus {{ outline: none; border-color: {c["accent"]}; }}
    .lead-form button {{ width: 100%; padding: 16px; background: linear-gradient(135deg, {c["accent"]} 0%, {c["accent"]}dd 100%); color: white; border: none; border-radius: 10px; font-size: 1.1rem; font-weight: 700; cursor: pointer; transition: all 0.3s; box-shadow: 0 4px 14px {c["accent"]}44; }}
    .lead-form button:hover {{ transform: translateY(-2px); box-shadow: 0 6px 20px {c["accent"]}66; }}
    .disclaimer {{ font-size: 0.85rem; color: #94a3b8; margin-top: 16px; text-align: center; }}
    .checkbox {{ display: flex; align-items: flex-start; gap: 10px; margin-bottom: 12px; font-size: 0.9rem; color: #475569; }}
    .checkbox input {{ width: auto; margin: 4px 0 0 0; }}
    
    /* FAQ */
    .faq {{ background: {c["light"]}; padding: 50px 0; }}
    .faq h3 {{ text-align: center; font-size: 1.5rem; margin-bottom: 32px; color: {c["primary"]}; font-weight: 700; }}
    .faq-item {{ background: white; padding: 24px; border-radius: 14px; margin-bottom: 14px; box-shadow: 0 2px 12px rgba(0,0,0,0.04); }}
    .faq-item h4 {{ color: {c["primary"]}; margin-bottom: 8px; font-weight: 600; }}
    .faq-item p {{ color: #64748b; font-size: 0.95rem; }}
    
    /* Final CTA */
    .final-cta {{ background: linear-gradient(135deg, {c["primary"]} 0%, {c["primary"]}ee 100%); color: white; padding: 60px 0; text-align: center; position: relative; overflow: hidden; }}
    .final-cta::before {{ content: ''; position: absolute; top: -50%; left: -20%; width: 60%; height: 200%; background: radial-gradient(circle, {c["accent"]}22 0%, transparent 70%); }}
    .final-cta h3 {{ font-size: 1.8rem; margin-bottom: 12px; font-weight: 700; position: relative; }}
    .final-cta p {{ opacity: 0.9; margin-bottom: 24px; position: relative; }}
    .final-cta .cta-button {{ background: white; color: {c["primary"]}; box-shadow: 0 4px 20px rgba(0,0,0,0.2); }}
    .final-cta .cta-button:hover {{ background: {c["light"]}; }}
    
    /* Footer */
    footer {{ background: {c["primary"]}; color: white; text-align: center; padding: 30px 0; font-size: 0.9rem; }}
    footer a {{ color: rgba(255,255,255,0.7); text-decoration: none; margin: 0 8px; }}
    footer a:hover {{ color: white; text-decoration: underline; }}
    
    @media (min-width: 600px) {{
      .benefit-grid {{ grid-template-columns: 1fr 1fr; }}
      .preview-grid {{ grid-template-columns: repeat(3, 1fr); }}
      .trust-grid {{ grid-template-columns: repeat(3, 1fr); }}
      .product-grid {{ grid-template-columns: repeat(3, 1fr); }}
    }}
    
    @media (max-width: 480px) {{
      header h1 {{ font-size: 1.8rem; }}
      .hero h2 {{ font-size: 1.4rem; }}
      .stats-grid {{ gap: 20px; }}
      .stat-number {{ font-size: 1.3rem; }}
      .cta-button {{ display: block; width: 100%; margin-bottom: 8px; text-align: center; }}
      .cta-button.secondary {{ margin-left: 0; }}
    }}
  </style>
</head>
<body>

{urgency_banner}

<header>
  <div class="container">
    <div class="brand-badge">{data["brand_name"]}</div>
    <h1>{data["headline"]}</h1>
    <p>{data["subheadline"]}</p>
  </div>
</header>

<section class="stats-bar">
  <div class="container">
    <div class="stats-grid">
      {stats_html}
    </div>
  </div>
</section>

<section class="hero">
  <div class="container">
    <h2>{data["hero_h2"]}</h2>
    <p>{data["hero_p"]}</p>
    <a href="#form" class="cta-button">{data["cta_primary"]}</a>
    {secondary_ctas}
  </div>
</section>

<section class="problem">
  <div class="container">
    <h3>{data["problem_title"]}</h3>
    <ul>
      {problems_html}
    </ul>
  </div>
</section>

<section class="benefits">
  <div class="container">
    <h3>{data["benefits_title"]}</h3>
    <p class="benefits-intro">{data["benefits_intro"]}</p>
    <div class="benefit-grid">
      {benefits_html}
    </div>
  </div>
</section>

<section class="preview">
  <div class="container">
    <h3>{data["mockup_title"]}</h3>
    <div class="preview-grid">
      {mockups_html}
    </div>
  </div>
</section>

<section class="trust">
  <div class="container">
    <h3>{data["trust_title"]}</h3>
    <div class="trust-grid">
      {trust_items_html}
    </div>
  </div>
</section>

<section class="social">
  <div class="container">
    <h3>{data["social_title"]}</h3>
    {social_items_html}
  </div>
</section>

{products_html}

<section class="form-section" id="form">
  <div class="container">
    <h3>{data["form_headline"]}</h3>
    <p>{data["form_sub"]}</p>
    <form class="lead-form" action="https://api.web3forms.com/submit" method="POST">
      <input type="hidden" name="access_key" value="d4cddc96-085c-497b-bd25-b77b7dd3eca9">
      <input type="hidden" name="subject" value="Neuer Lead: {niche_id}">
      <input type="text" name="first_name" placeholder="Dein Vorname" required>
      <input type="email" name="email" placeholder="Deine E-Mail-Adresse" required>
      <input type="hidden" name="tag" value="{niche_id}">
      <button type="submit">{data["form_button"]}</button>
      <p class="disclaimer" style="margin-top: 20px;"><a href="lead-magnet.pdf" download>PDF ohne Anmeldung herunterladen</a></p>
    </form>
    <p class="disclaimer">DSGVO-konform. Jederzeit abmeldbar. Keine Weitergabe deiner Daten.</p>
  </div>
</section>

<section class="faq">
  <div class="container">
    <h3>{data["faq_title"]}</h3>
    {faqs_html}
  </div>
</section>

<section class="final-cta">
  <div class="container">
    <h3>{data["final_cta_title"]}</h3>
    <p>{data["final_cta_p"]}</p>
    <a href="#form" class="cta-button">{data["final_cta_button"]}</a>
    <p style="margin-top:16px; font-size:0.85rem; opacity:0.8;">DSGVO-konform. Jederzeit abmeldbar.</p>
  </div>
</section>

<footer>
  <div class="container">
    <p>&copy; 2026 Empire Expansion. Alle Rechte vorbehalten. | <a href="#">Datenschutzerklärung</a> | <a href="#">Impressum</a></p>
  </div>
</footer>

</body>
</html>'''
    
    return html

# Hauptfunktion
def main():
    for niche_id, data in NICHES.items():
        filepath = os.path.join(BASE_DIR, niche_id, "landing-page.html")
        
        # Backup erstellen
        backup_path = os.path.join(BASE_DIR, niche_id, "landing-page-backup.html")
        if os.path.exists(filepath) and not os.path.exists(backup_path):
            with open(filepath, 'r', encoding='utf-8') as f:
                old_content = f.read()
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(old_content)
            print(f"Backup erstellt: {backup_path}")
        
        # Neue HTML-Datei generieren
        html = generate_html(niche_id, data)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"✅ Landing Page aktualisiert: {niche_id}")
    
    print("\n🎉 Alle 9 Landing Pages erfolgreich generiert!")
    return True

if __name__ == "__main__":
    main()
