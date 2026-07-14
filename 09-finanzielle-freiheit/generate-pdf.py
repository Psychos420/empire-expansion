#!/usr/bin/env python3
"""
Professional FIRE Lead Magnet PDF Generator (reportlab)
"""
import sys
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "lead-magnet.pdf"
FONT_DIR = Path(__file__).resolve().parent.parent / "00-shared" / "tools" / "fonts"

def setup_fonts():
    fonts = []
    for name, fname in [("IBMMono", "IBMPlexMono-Regular.ttf"), ("IBMMonoBold", "IBMPlexMono-Medium.ttf")]:
        p = FONT_DIR / fname
        if p.exists():
            pdfmetrics.registerFont(TTFont(name, str(p)))
            fonts.append(name)
    win = Path("C:/Windows/Fonts")
    sys_map = {
        "SegoeUI": "segoeui.ttf",
        "SegoeUIBold": "segoeuib.ttf",
        "SegoeUIItalic": "segoeuii.ttf",
        "SegoeUISemiBold": "seguisb.ttf",
    }
    for name, fname in sys_map.items():
        p = win / fname
        if p.exists():
            try:
                pdfmetrics.registerFont(TTFont(name, str(p)))
                fonts.append(name)
            except Exception:
                pass
    return fonts

FONTS = setup_fonts()
BODY_FONT = "SegoeUI" if "SegoeUI" in FONTS else "Helvetica"
BODY_BOLD = "SegoeUIBold" if "SegoeUIBold" in FONTS else "Helvetica-Bold"
BODY_ITALIC = "SegoeUIItalic" if "SegoeUIItalic" in FONTS else "Helvetica-Oblique"
BODY_SEMI = "SegoeUISemiBold" if "SegoeUISemiBold" in FONTS else "Helvetica-Bold"
MONO_FONT = "IBMMono" if "IBMMono" in FONTS else "Courier"
MONO_BOLD = "IBMMonoBold" if "IBMMonoBold" in FONTS else "Courier-Bold"

def make_styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle("CoverTitle", fontName=BODY_BOLD, fontSize=32, leading=38, textColor=colors.HexColor("#0A2540"), alignment=TA_CENTER, spaceAfter=10))
    s.add(ParagraphStyle("CoverSub", fontName=BODY_FONT, fontSize=14, leading=18, textColor=colors.HexColor("#5b5a6e"), alignment=TA_CENTER, spaceAfter=30))
    s.add(ParagraphStyle("CoverMeta", fontName=MONO_FONT, fontSize=9, leading=12, textColor=colors.HexColor("#8a8a9a"), alignment=TA_CENTER, spaceAfter=6))
    s.add(ParagraphStyle("H1", fontName=BODY_BOLD, fontSize=22, leading=26, textColor=colors.HexColor("#0A2540"), spaceAfter=14, spaceBefore=8))
    s.add(ParagraphStyle("H2", fontName=BODY_SEMI, fontSize=16, leading=20, textColor=colors.HexColor("#0A2540"), spaceAfter=10, spaceBefore=14))
    s.add(ParagraphStyle("H3", fontName=BODY_SEMI, fontSize=13, leading=16, textColor=colors.HexColor("#1f6f5c"), spaceAfter=8, spaceBefore=10))
    s.add(ParagraphStyle("Body", fontName=BODY_FONT, fontSize=10.5, leading=15, textColor=colors.HexColor("#1c2333"), alignment=TA_JUSTIFY, spaceAfter=10))
    s.add(ParagraphStyle("BodyBold", fontName=BODY_BOLD, fontSize=10.5, leading=15, textColor=colors.HexColor("#1c2333"), spaceAfter=8))
    s.add(ParagraphStyle("Callout", fontName=BODY_FONT, fontSize=10, leading=14, textColor=colors.HexColor("#1c2333"), backColor=colors.HexColor("#eef4f0"), leftIndent=12, rightIndent=12, spaceAfter=10, borderPadding=10, borderColor=colors.HexColor("#1f6f5c"), borderWidth=0))
    s.add(ParagraphStyle("Disclaimer", fontName=MONO_FONT, fontSize=7.5, leading=10, textColor=colors.HexColor("#8a8a9a"), alignment=TA_LEFT, spaceAfter=4))
    s.add(ParagraphStyle("QuestionNum", fontName=MONO_BOLD, fontSize=11, leading=14, textColor=colors.HexColor("#1f6f5c"), spaceAfter=2))
    s.add(ParagraphStyle("QuestionText", fontName=BODY_SEMI, fontSize=11, leading=14, textColor=colors.HexColor("#0A2540"), spaceAfter=6))
    s.add(ParagraphStyle("CheckItem", fontName=BODY_FONT, fontSize=10, leading=14, textColor=colors.HexColor("#1c2333"), leftIndent=16, spaceAfter=4, bulletIndent=4))
    s.add(ParagraphStyle("StatNum", fontName=BODY_BOLD, fontSize=24, leading=26, textColor=colors.HexColor("#b8842e"), alignment=TA_CENTER))
    s.add(ParagraphStyle("StatLabel", fontName=MONO_FONT, fontSize=8, leading=10, textColor=colors.HexColor("#8a8a9a"), alignment=TA_CENTER, spaceAfter=4))
    return s

STYLES = make_styles()

def hr():
    return Table([[""]], colWidths=[160*mm], rowHeights=[1], style=TableStyle([("LINEBELOW", (0,0), (-1,-1), 1, colors.HexColor("#e0d8c6"))]))

def green_accent_line():
    return Table([[""]], colWidths=[160*mm], rowHeights=[3], style=TableStyle([("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#1f6f5c")), ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 0)]))

def checkbox(text):
    return Paragraph(f'<font name="{MONO_FONT}" color="#1f6f5c">&#x2611;</font>  {text}', STYLES["CheckItem"])

def callout(title, text):
    return Table([[Paragraph(f'<b>{title}</b>', STYLES["H3"])], [Paragraph(text, STYLES["Callout"])]], colWidths=[160*mm], style=TableStyle([("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#eef4f0")), ("LEFTPADDING", (0,0), (-1,-1), 12), ("RIGHTPADDING", (0,0), (-1,-1), 12), ("TOPPADDING", (0,0), (-1,-1), 10), ("BOTTOMPADDING", (0,0), (-1,-1), 10), ("VALIGN", (0,0), (-1,-1), "TOP")]))

def header_footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#1f6f5c"))
    canvas.setLineWidth(3)
    canvas.line(22*mm, A4[1]-18*mm, A4[0]-22*mm, A4[1]-18*mm)
    canvas.setFont(MONO_FONT, 7)
    canvas.setFillColor(colors.HexColor("#8a8a9a"))
    canvas.drawString(22*mm, 14*mm, "Empire Expansion - FIRE-Schnellcheck fuer 35+")
    canvas.drawRightString(A4[0]-22*mm, 14*mm, f"Seite {doc.page}")
    canvas.setFont(MONO_FONT, 6)
    canvas.setFillColor(colors.HexColor("#aaaaaa"))
    canvas.drawString(22*mm, 8*mm, "Nur Bildung, keine Anlageberatung. Stand: Juli 2026.")
    canvas.restoreState()

def cover_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont(MONO_FONT, 7)
    canvas.setFillColor(colors.HexColor("#8a8a9a"))
    canvas.drawCentredString(A4[0]/2, 18*mm, "Empire Expansion - 35+ Lead-Oekosystem")
    canvas.drawCentredString(A4[0]/2, 12*mm, "Kostenloser Lead-Magnet - Stand: Juli 2026")
    canvas.restoreState()

def build_pdf():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=22*mm, leftMargin=22*mm, topMargin=22*mm, bottomMargin=22*mm)
    story = []
    # Cover
    story.append(Spacer(1, 40*mm))
    story.append(Paragraph("Der FIRE-Schnellcheck", STYLES["CoverTitle"]))
    story.append(Paragraph("fuer 35+", STYLES["CoverTitle"]))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("Dein persoenlicher Vermoegensaufbau-Plan in 10 Fragen", STYLES["CoverSub"]))
    story.append(Spacer(1, 10*mm))
    story.append(hr())
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("In 15 Minuten erfaehrst du, wie weit du von finanzieller Unabhaengigkeit entfernt bist - und welche 3 Schritte als Naechstes wirken.", STYLES["Body"]))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("Basierend auf aktuellen Marktdaten Juli 2026:", STYLES["BodyBold"]))
    story.append(Spacer(1, 4*mm))
    story.append(Table([[Paragraph("10 Mio.", STYLES["StatNum"]), Paragraph("150 Mrd. EUR", STYLES["StatNum"]), Paragraph("2,25 %", STYLES["StatNum"])], [Paragraph("Kunden Trade Republic", STYLES["StatLabel"]), Paragraph("verwaltetes Vermoegen", STYLES["StatLabel"]), Paragraph("Cash-Zins p.a.", STYLES["StatLabel"])]], colWidths=[52*mm, 52*mm, 52*mm], style=TableStyle([("ALIGN", (0,0), (-1,-1), "CENTER"), ("VALIGN", (0,0), (-1,-1), "MIDDLE")])))
    story.append(Spacer(1, 10*mm))
    story.append(hr())
    story.append(Spacer(1, 10*mm))
    story.append(Paragraph("<b>Achtung:</b> Dieses Dokument dient ausschliesslich der Bildung und stellt keine Anlage-, Steuer- oder Versicherungsberatung dar. Bei komplexen Entscheidungen konsultieren Sie bitte einen unabhaengigen Honorarberater.", STYLES["Disclaimer"]))
    story.append(PageBreak())
    # Instructions
    story.append(Paragraph("So nutzt du diesen Check", STYLES["H1"]))
    story.append(green_accent_line())
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Dieser Schnellcheck ist kein Buch. Er ist ein Werkzeug. Wenn du ehrlich antwortest, bekommst du in 15 Minuten eine klare Standortbestimmung - unabhaengig davon, ob du gerade 0 EUR oder 200.000 EUR auf dem Konto hast.", STYLES["Body"]))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("<b>5-Minuten-Anleitung:</b>", STYLES["BodyBold"]))
    story.append(Spacer(1, 2*mm))
    story.append(checkbox("Schnapp dir einen Stift und ein Blatt Papier (oder oeffne ein Textdokument)."))
    story.append(checkbox("Gehe die 10 Fragen der Reihe nach durch. Es gibt keine falschen Antworten."))
    story.append(checkbox("Notiere zu jeder Frage deine Antwort kurz. Nur grobe Zahlen sind noetig."))
    story.append(checkbox("Nach Frage 10 zaehlst du deine Punkte zusammen und liest dein Ergebnisprofil."))
    story.append(checkbox("Wende die 3 konkreten naechsten Schritte aus deinem Profil heute noch an."))
    story.append(Spacer(1, 8*mm))
    story.append(callout("Hinweis zu den Zahlen", "Du brauchst keine perfekten Zahlen. Ein ungefaehrer Wert reicht vollkommen aus. Der Check lebt von der Ehrlichkeit, nicht von der Praezision."))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("<b>Die 4 Ergebnisprofile:</b>", STYLES["BodyBold"]))
    story.append(Spacer(1, 2*mm))
    story.append(Table([[Paragraph("Profil A", STYLES["BodyBold"]), Paragraph('"Starter" - Wenig Vermoegen, hohes Potenzial', STYLES["Body"])], [Paragraph("Profil B", STYLES["BodyBold"]), Paragraph('"Aufholer" - Solide Basis, Fehlallokation', STYLES["Body"])], [Paragraph("Profil C", STYLES["BodyBold"]), Paragraph('"Optimierer" - Vermoegen vorhanden, Steuern & Kosten analysieren', STYLES["Body"])], [Paragraph("Profil D", STYLES["BodyBold"]), Paragraph('"Coast-FIRE-Kandidat" - Fast unabhaengig, Feinabstimmung noetig', STYLES["Body"])]], colWidths=[28*mm, 130*mm], style=TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 8), ("TOPPADDING", (0,0), (-1,-1), 4), ("BOTTOMPADDING", (0,0), (-1,-1), 4)])))
    story.append(PageBreak())
    # Questions
    story.append(Paragraph("Der 10-Fragen-Check", STYLES["H1"]))
    story.append(green_accent_line())
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Beantworte jede Frage ehrlich. Notiere deine Punkte am Rand. Am Ende zaehlst du sie zusammen.", STYLES["Body"]))
    story.append(Spacer(1, 6*mm))
    for i, (q, opts, extra) in enumerate([
        ("Wie alt bist du und wie viele Jahre moechtest du noch arbeiten?", ["a) 35-39 Jahre, noch 25+ Jahre arbeiten (2 Punkte)", "b) 40-44 Jahre, noch 20-24 Jahre (3 Punkte)", "c) 45-49 Jahre, noch 15-19 Jahre (4 Punkte)", "d) 50+ Jahre, weniger als 15 Jahre (5 Punkte)"], "Je laenger dein Anlagehorizont, desto mehr Zeit hat Compound-Interest zu wirken. Aber auch mit 50+ laesst sich noch viel erreichen - nur die Strategie aendert sich."),
        ("Wie hoch ist dein monatliches Nettoeinkommen?", ["a) Unter 2.500 EUR (1 Punkt)", "b) 2.500-3.999 EUR (2 Punkte)", "c) 4.000-5.999 EUR (3 Punkte)", "d) 6.000-9.999 EUR (4 Punkte)", "e) 10.000 EUR+ (5 Punkte)"], "Der Standardtarif-Hoechstbeitrag fuer die PKV liegt bei 848,62 EUR/Monat. Bei 6.000 EUR+ Netto ist die PKV in der Regel steuerlich attraktiver als die GKV."),
        ("Wie hoch sind deine monatlichen Lebenshaltungskosten (Fixkosten)?", ["a) Unter 2.000 EUR (5 Punkte)", "b) 2.000-3.500 EUR (4 Punkte)", "c) 3.500-5.000 EUR (3 Punkte)", "d) 5.000-7.000 EUR (2 Punkte)", "e) Ueber 7.000 EUR (1 Punkt)"], None),
        ("Wie viel Vermoegen hast du aktuell insgesamt?", ["a) Negativ oder 0 EUR (1 Punkt)", "b) 1-50.000 EUR (2 Punkte)", "c) 50.001-150.000 EUR (3 Punkte)", "d) 150.001-400.000 EUR (4 Punkte)", "e) 400.000 EUR+ (5 Punkte)"], None),
        ("Wie viel kannst du monatlich langfristig anlegen (nach Notgroschen)?", ["a) 0 EUR oder negativ (1 Punkt)", "b) 1-300 EUR (2 Punkte)", "c) 301-800 EUR (3 Punkte)", "d) 801-1.500 EUR (4 Punkte)", "e) 1.500 EUR+ (5 Punkte)"], "Wer mit 35 jeden Monat 500 EUR anlegt und durchschnittlich 7 % Rendite erzielt, kommt mit 65 auf rund 612.000 EUR. Mit 800 EUR/Monat: ~980.000 EUR."),
        ("Welche Vermoegensbausteine hast du bereits?", ["a) Nur Girokonto / Tagesgeld (1 Punkt)", "b) Bausparvertrag oder Riester/Ruerup (2 Punkte)", "c) Depot mit ETF-/Fonds-Sparplan (3 Punkte)", "d) Depot + Immobilien (4 Punkte)", "e) Depot + Immobilien + Betriebsrente/Versicherung (5 Punkte)"], "Trade Republic verzeichnet 10 Mio. Kunden und 150 Mrd. EUR AUM. Cash-Zins 2,25 % p.a. Bauzinsen (10J) bei 3,39 % - leicht gesunken gegenueber Maerz, aber Experten erwarten Herbst-Anstieg."),
        ("Was ist dein groesstes finanzielles Sorgenkind?", ["a) Schulden oder keine Ruecklagen (1 Punkt)", "b) Zu wenig Anlageerfahrung / Angst vor Verlusten (2 Punkte)", "c) Falsche Produkte (teure Fonds, Riester, Bausparer) (3 Punkte)", "d) Keine Strategie / keine Uebersicht (4 Punkte)", "e) Steuer-Optimierung / Absicherung fehlt (5 Punkte)"], "~60 % der Privatversicherten sind von Beitragserhoehungen betroffen. OE 10-13 % Erhoehung, teils bis 40 % (VKB). Wer nicht prueft, zahlt zu viel."),
        ("Wie sicher fuehlst du dich bei Geldanlagen? (Skala 1-5)", ["a) 1 - Gar nicht sicher (1 Punkt)", "b) 2 - Etwas unsicher (2 Punkte)", "c) 3 - Mittel (3 Punkte)", "d) 4 - Sicher (4 Punkte)", "e) 5 - Sehr sicher (5 Punkte)"], "Sicherheit kommt durch Wissen, nicht durch Nichtstun. Ein Welt-ETF ist langfristig sicherer als ein Tagesgeldkonto bei 2,25 % mit Inflationsverlust."),
        ("Wie wichtig ist dir Flexibilitaet vor dem Renteneintritt?", ["a) Nicht wichtig, ich arbeite bis 67 (1 Punkt)", "b) Etwas wichtig, Teilzeit waere schoen (2 Punkte)", "c) Wichtig, ich moechte frueher reduzieren (3 Punkte)", "d) Sehr wichtig, Coast-FIRE ist das Ziel (4 Punkte)", "e) Extrem wichtig, vollstaendige Unabhaengigkeit (5 Punkte)"], "Ab einem bestimmten Vermoegen wachsen deine Investments so stark, dass du theoretisch gar nichts mehr sparen muesstest. Du arbeitest dann nur noch fuer den Lebensstil, nicht mehr fuer die Rente."),
        ("Welches Ziel ist dir am wichtigsten?", ["a) Familie absichern (1 Punkt)", "b) Mehr Zeit fuer mich (2 Punkte)", "c) Frueher in Rente (3 Punkte)", "d) Beruf runterschrauben (4 Punkte)", "e) Sicherheit und Unabhaengigkeit (5 Punkte)"], "Addiere jetzt alle Punkte zusammen. Dein Ergebnis liegt zwischen 10 und 50 Punkten. Wende dich an Seite 8, um dein Profil zu ermitteln."),
    ], start=1):
        story.append(Paragraph(f"Frage {i}", STYLES["QuestionNum"]))
        story.append(Paragraph(q, STYLES["QuestionText"]))
        for opt in opts:
            story.append(checkbox(opt))
        story.append(Spacer(1, 4*mm))
        if extra:
            if i in [1, 2, 5, 6, 7, 8, 9]:
                story.append(callout("Warum das zaehlt" if i==1 else ("Marktdaten Juli 2026" if i==2 else ("Zahlenbeispiel" if i==5 else ("Aktueller Marktkontext" if i==6 else ("PKV-Warnung 2026" if i==7 else ("Wichtig" if i==8 else "Coast-FIRE"))))), extra))
            else:
                story.append(Paragraph(f"<b>Faustregel fuer 35+:</b> {extra}" if i==3 else f"<b>Tipp:</b> {extra}" if i==4 else f"<b>Naechster Schritt:</b> {extra}", STYLES["Body"]))
            story.append(Spacer(1, 6*mm))
    story.append(PageBreak())
    # Profiles
    story.append(Paragraph("Auswertung - Dein Ergebnisprofil", STYLES["H1"]))
    story.append(green_accent_line())
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Addiere deine Punkte und finde dein Profil. Jedes Profil enthaelt eine Diagnose, einen geschätzten FIRE-Zeitrahmen und deine Top-3 naechsten Schritte.", STYLES["Body"]))
    story.append(Spacer(1, 8*mm))
    profiles = [
        ("Profil A - Starter (10-20 Punkte)", "Du stehst am Anfang oder hast bisher wenig gezielt gespart. Das ist kein Problem - mit 35+ hast du noch mindestens 20 Jahre Anlagehorizont. Das ist mehr als genug Zeit.", "55-65 Jahre (bei konsequentem Sparplan)", ["Notgroschen aufbauen: 3-6 Monatsgehaelter auf Tagesgeld (Trade Republic Cash-Zins 2,25 % p.a.)", "Ungenutzte Abos und doppelte Versicherungen kuendigen - sofortige Sparrate erhoehen", "Kostenloses Depot bei Trade Republic oder Scalable eroeffnen, ersten Welt-ETF-Sparplan einrichten"]),
        ("Profil B - Aufholer (21-32 Punkte)", "Du hast eine solide Basis, aber dein Vermoegen ist suboptimal allokiert. Vielleicht zu viel Tagesgeld, teure Fonds oder ein ungenutzter Bausparvertrag. Du hast Potenzial, das nur darauf wartet, freigesetzt zu werden.", "50-58 Jahre", ["Depot-Check: Teure aktive Fonds gegen kostenguenstige ETFs tauschen (TER &lt; 0,2 %)", "Sparer-Pauschbetrag voll ausschoepfen (2026: voraussichtlich 1.200-1.500 EUR/Jahr)", "PKV-Optimierung pruefen: ~60 % der PKV-Versicherten stehen 2026 vor Erhoehungen bis 40 %"]),
        ("Profil C - Optimierer (33-42 Punkte)", "Du hast bereits Vermoegen aufgebaut und verstehst die Grundlagen. Jetzt geht es um Steuer-Optimierung, Kosten-Minimierung und strategische Feinabstimmung. Kleinste Hebel haben hier den groessten Effekt.", "48-55 Jahre", ["Steuer-Hebel ziehen: Thesaurierende ETFs, Freistellungsauftrag, Verlustverrechnungstopf pruefen", "Bauzins-Monitoring: 10J bei 3,39 % (Juli 2026), leicht gesunken vs. Maerz - Experten erwarten Herbst-Anstieg", "Berufsunfaehigkeitsversicherung und Haftpflicht auf Aktualitaet pruefen"]),
        ("Profil D - Coast-FIRE-Kandidat (43-50 Punkte)", "Du bist fast finanziell unabhaengig. Dein Vermoegen waechst so stark, dass du theoretisch nur noch fuer den Lebensstil arbeiten muesstest. Feinabstimmung ist jetzt alles.", "45-52 Jahre (oder sofort mit reduziertem Lebensstil)", ["Entnahmestrategie entwickeln: 4 %-Regel, steueroptimierte Entnahmereihenfolge", "Vermoegensaufbau vs. Risiko-Minimierung: Anteil Anleihen/Immobilien erhoehen?", "Erbfolge planen: Schenkungen, Testament, Vorsorgevollmacht absichern"]),
    ]
    for title, desc, timeframe, steps in profiles:
        story.append(Paragraph(title, STYLES["H2"]))
        story.append(Paragraph(desc, STYLES["Body"]))
        story.append(Spacer(1, 2*mm))
        story.append(Paragraph(f"<b>Geschätzter FIRE-Zeitpunkt:</b> {timeframe}", STYLES["BodyBold"]))
        story.append(Spacer(1, 2*mm))
        story.append(Paragraph("<b>Top-3 naechste Schritte:</b>", STYLES["BodyBold"]))
        for s in steps:
            story.append(checkbox(s))
        story.append(Spacer(1, 8*mm))
    story.append(PageBreak())
    # 3-Pillar Strategy
    story.append(Paragraph("Die 3-Saeulen-Strategie fuer 35+", STYLES["H1"]))
    story.append(green_accent_line())
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Die meisten 35+ brauchen keine komplexe Renditejagd. Sie brauchen drei stabile Saeulen, die zusammenhalten. Wenn eine Saeule wackelt, bricht das ganze System ein.", STYLES["Body"]))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Saeule 1: Notgroschen & Liquiditaet", STYLES["H2"]))
    story.append(Paragraph("Bevor du auch nur einen Euro in ETFs steckst, musst du liquide sein. Sonst verkaufst du in der naechsten Krise mit Verlust.", STYLES["Body"]))
    story.append(Spacer(1, 2*mm))
    story.append(checkbox("Ziel: 3-6 Monatsgehaelter auf Tagesgeld oder Geldmarktfonds"))
    story.append(checkbox("Aktuell: Trade Republic Cash-Zins 2,25 % p.a., taeglich verfuegbar"))
    story.append(checkbox("Trenne Notgroschen und Depot physisch und psychisch: verschiedene Konten"))
    story.append(checkbox("Regel: Wenn du den Notgroschen antasten musst, stoppe alle Sparplaene sofort"))
    story.append(Spacer(1, 6*mm))
    story.append(callout("Wichtig fuer 35+", "Mit Familie und Immobilie sind deine Fixkosten hoeher. Rechne konservativ: 6 Monatsgehaelter sind oft realistischer als 3."))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Saeule 2: Langfristiger Vermoegensaufbau mit ETFs", STYLES["H2"]))
    story.append(Paragraph("Fuer die meisten 35+ ist ein breit gestreuter Welt-ETF der effizienteste Weg. Keine Einzelaktien, kein Timing, kein Stress.", STYLES["Body"]))
    story.append(Spacer(1, 2*mm))
    story.append(checkbox("Depot bei kostenguenstigem Broker: Trade Republic (10 Mio. Kunden, 150 Mrd. EUR AUM) oder Scalable Capital"))
    story.append(checkbox("Sparplan auf thesaurierenden Welt-ETF (z. B. MSCI World oder FTSE All-World)"))
    story.append(checkbox("Monatliche Disziplin: Automatische Ueberweisung am Tag nach Gehaltseingang"))
    story.append(checkbox("Freistellungsauftrag hinterlegen: Sparer-Pauschbetrag 2026 voraussichtlich 1.200-1.500 EUR/Jahr"))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("<b>Zahlenbeispiel:</b> Wer mit 35 jeden Monat 500 EUR anlegt und durchschnittlich 7 % Rendite erzielt, kommt mit 65 auf rund 612.000 EUR. Mit 800 EUR/Monat: ~980.000 EUR. Bei 1.000 EUR/Monat: ~1.225.000 EUR.", STYLES["Body"]))
    story.append(Spacer(1, 6*mm))
    story.append(callout("Hinweis fuer Fortgeschrittene", "Wer ueber 100.000 EUR im Depot hat, sollte die Vorabpauschale gegen Ausschuettungen pruefen. Thesaurierende ETFs sind bei hoeheren Betraegen meist steueroptimaler."))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Saeule 3: Steueroptimierung & Absicherung", STYLES["H2"]))
    story.append(Paragraph("Jeder Euro, den du an Steuern, Gebuuehren oder ineffizienten Versicherungen sparst, ist ein Euro, den du nicht erst anlegen musst. Fuer 35+ ist das wichtiger als Renditejagd.", STYLES["Body"]))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph("<b>Steuer-Hebel:</b>", STYLES["BodyBold"]))
    story.append(checkbox("Sparer-Pauschbetrag voll ausschoepfen"))
    story.append(checkbox("Thesaurierende ETFs nutzen (Vorabpauschale deutlich guenstiger als Ausschuettungen bei hoeheren Betraegen)"))
    story.append(checkbox("Freistellungsauftrag beim Broker hinterlegen"))
    story.append(checkbox("Verlustverrechnungstopf bei Depotwechsel beachten"))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("<b>Absicherung-Hebel:</b>", STYLES["BodyBold"]))
    story.append(checkbox("Berufsunfaehigkeitsversicherung pruefen - die wichtigste Absicherung fuer 35+"))
    story.append(checkbox("PKV optimieren: 2026 stehen ~60 % vor Erhoehungen, OE 10-13 %, teils bis 40 % (VKB). Standardtarif-Hoechstbeitrag 848,62 EUR/Monat."))
    story.append(checkbox("Haftpflicht- und Rechtsschutzversicherung auf Aktualitaet pruefen"))
    story.append(Spacer(1, 6*mm))
    story.append(callout("Regulatorischer Hinweis", "Dies ist Bildung, keine Steuer- oder Versicherungsberatung. Bei komplexen Faellen empfehlen wir einen unabhaengigen Berater. Bei Tarifcheck.de erhalten Vermittler bis 1.750 EUR Provision pro erfolgreicher Vermittlung."))
    story.append(PageBreak())
    # Next Steps
    story.append(Paragraph("Deine naechsten 3 Schritte", STYLES["H1"]))
    story.append(green_accent_line())
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Wissen ohne Handlung ist wertlos. Hier sind die 3 Dinge, die du heute noch tun kannst - egal welches Profil du bist:", STYLES["Body"]))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Schritt 1: In 10 Minuten deinen Status quo dokumentieren", STYLES["H2"]))
    story.append(checkbox("Oeffne dein Online-Banking und summiere alle regelmaessigen Ausgaben der letzten 3 Monate."))
    story.append(checkbox("Notiere dein aktuelles Gesamtvermoegen (Konten, Depots, Immobilienwert minus Schulden)."))
    story.append(checkbox("Schreibe auf, welches dein groesstes finanzielles Sorgenkind ist."))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Schritt 2: In 10 Minuten einen Hebel waehlen", STYLES["H2"]))
    story.append(checkbox("Nicht alles auf einmal. Suche dir den Punkt mit dem groessten Impact: hoehere Sparrate, guenstigerer Broker, Steuern optimieren oder BU/PKV pruefen."))
    story.append(checkbox("Wenn du nicht weisst, wo anfangen: Starte mit dem ungenutzten Abo oder der doppelten Versicherung. Das Erfolgserlebnis motiviert."))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("Schritt 3: In 10 Minuten eine winzige Aktion setzen", STYLES["H2"]))
    story.append(checkbox("Ein ungenutztes Abo kuendigen (5 Minuten)"))
    story.append(checkbox("Den Freistellungsauftrag beim Broker pruefen (3 Minuten)"))
    story.append(checkbox("Einen Termin fuer die PKV-Optimierung vereinbaren (2 Minuten)"))
    story.append(checkbox("Bei Trade Republic ein kostenloses Depot eroeffnen (10 Minuten)"))
    story.append(Spacer(1, 8*mm))
    story.append(callout("Merke dir", "Die besten Investoren sind nicht diejenigen, die alles wissen. Sie sind diejenigen, die konsequent kleine Schritte gehen. Ein Schritt pro Tag reicht."))
    story.append(Spacer(1, 8*mm))
    story.append(Paragraph("<b>Optionale naechste Schritte:</b>", STYLES["BodyBold"]))
    story.append(checkbox('7-Tage-E-Mail-Kurs "In 7 Tagen zum ersten ETF-Sparplan" - kostenlos nach Anmeldung'))
    story.append(checkbox("Kostenloses Erstgespraech buchen: Wir schauen uns deine Situation an und klaeren, was der beste naechste Schritt ist."))
    story.append(checkbox("ETF-Einsteigerkurs (97 EUR): 5 Module, 20 Kurzvideos, Schritt-fuer-Schritt-Anleitung, 14 Tage Geld-zurueck-Garantie"))
    story.append(PageBreak())
    # Disclaimer
    story.append(Paragraph("Haftungsausschluss & Affiliate-Hinweis", STYLES["H1"]))
    story.append(green_accent_line())
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Dieses Dokument wurde von Empire Expansion erstellt und dient ausschliesslich der <b>Bildung und Information</b>. Es stellt in keinem Fall eine Anlage-, Steuer-, Rechts- oder Versicherungsberatung dar.", STYLES["Body"]))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("<b>Keine Anlageberatung:</b> Alle Inhalte, Empfehlungen und Beispiele in diesem Dokument sind allgemeiner Natur und nicht auf die individuelle Situation des Lesers zugeschnitten. Sie ersetzen nicht die Beratung durch einen qualifizierten Honorarberater oder Steuerberater. Jede Anlageentscheidung obliegt allein dem Leser.", STYLES["Body"]))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("<b>Keine Gewaehrleistung:</b> Wir uebernehmen keine Haftung fuer die Richtigkeit, Vollstaendigkeit oder Aktualitaet der bereitgestellten Informationen. Marktdaten (z. B. Zinssaetze, Beitragssaetze, ETF-Renditen) koennen sich jederzeit aendern. Die verwendeten Daten entsprechen dem Stand Juli 2026.", STYLES["Body"]))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("<b>Affiliate-Hinweis:</b> Empire Expansion finanziert sich teilweise durch Affiliate-Provisionen. Wenn du ueber Links in diesem Dokument oder auf unseren Seiten ein Produkt oder eine Dienstleistung erwirbst, erhalten wir moeglicherweise eine Provision. Dies beeinflusst unsere Empfehlungen nicht. Alle Affiliate-Links werden als Werbung gekennzeichnet. Beispiel: Tarifcheck.de bietet bis 1.750 EUR Provision pro erfolgreicher Vermittlung.", STYLES["Body"]))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("<b>Keine Eigenwerbung fuer Empire-Dienstleistungen:</b> Die in diesem Dokument erwaehnten Kurse, Terminbuchungen und E-Mail-Sequenzen sind freiwillige Angebote. Es besteht kein Zwang, diese zu nutzen. Der Download des Schnellchecks ist vollstaendig kostenlos und unverbindlich.", STYLES["Body"]))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("<b>Urheberrecht:</b> (C) 2026 Empire Expansion. Alle Rechte vorbehalten. Vervielfaeltigung, Verbreitung oder oeffentliche Wiedergabe dieses Dokuments oder Teilen davon bedarf der ausdruecklichen schriftlichen Zustimmung von Empire Expansion.", STYLES["Body"]))
    story.append(Spacer(1, 8*mm))
    story.append(hr())
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("Kontakt", STYLES["H2"]))
    story.append(Paragraph("Empire Expansion", STYLES["Body"]))
    story.append(Paragraph("Verfahren 09 - Finanzielle Freiheit", STYLES["Body"]))
    story.append(Paragraph("E-Mail: finanzen@empire-expansion.de", STYLES["Body"]))
    story.append(Paragraph("Web: www.empire-expansion.de", STYLES["Body"]))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("Stand: Juli 2026 - Version 1.2", STYLES["Disclaimer"]))
    doc.build(story, onFirstPage=cover_footer, onLaterPages=header_footer)
    print(f"[OK] PDF generated: {OUT}")

if __name__ == "__main__":
    build_pdf()
