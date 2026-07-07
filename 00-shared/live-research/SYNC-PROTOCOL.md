:# Claude ↔ Kimi Sync-Protokoll

**Ziel:** Zwei Agenten arbeiten parallel am Empire-Expansion-Launch. Diese Datei definiert, wie sie sich abstimmen, ohne sich gegenseitig zu blockieren.

---

## Arbeitsbereiche

| Agent | Hauptaufgabe | Arbeitsverzeichnis |
|-------|--------------|-------------------|
| **Claude Code** | Technische Umsetzung, Landing Pages, Content-Generierung, Funnel-Optimierung, Ausführung des Autopiloten | `00-shared/generated-content/`, `00-shared/logs/CLAUDE-SESSION-LOG.md`, alle `landing-page.html`, `empire-config.json` |
| **Kimi** | Marktforschung, Trend-Monitoring, Wettbewerber-Analyse, strategische Empfehlungen, Datenaktualisierung | `00-shared/live-research/`, `REQUEST-FOR-KIMI.md` |

---

## Gemeinsame Dateien (beide lesen + schreiben)

| Datei | Zweck | Wer pflegt |
|-------|-------|------------|
| `EMPIRE-WEEK-1-SPRINT-BLUEPRINT.md` | Gesamtziel | Beide |
| `EMPIRE-AUTONOMOUS-LAUNCH.md` | Steuerregeln | Beide |
| `LAUNCH-STATUS-REPORT.md` | Aktueller Stand | Autopilot / Claude |
| `empire-config.json` | Konfiguration | Nutzer + Claude |

---

## Kommunikationskanal

Die Agenten kommunizieren **asynchron über Dateien**. Es gibt keinen direkten Chat.

### Kimi → Claude

Kimi hinterlegt Rechercheergebnisse in:
- `00-shared/live-research/KIMI-LIVE-RESEARCH.md`
- `00-shared/live-research/MARKET-UPDATES.md`
- `00-shared/live-research/COMPETITOR-SNAPSHOTS.md`
- `00-shared/live-research/TREND-ALERTS.md`

**Claude muss diese Dateien am Anfang jeder Session lesen und bei Änderungen berücksichtigen.**

### Claude → Kimi

Wenn Claude Marktdaten braucht, schreibt er in:
- `00-shared/live-research/REQUEST-FOR-KIMI.md`

Format:
```markdown
## Neue Anfrage vom [Datum]

**Von:** Claude
**Thema:** [Nische / Thema]
**Konkrete Frage:** [Was genau soll recherchiert werden?]
**Begründung:** [Warum ist das für den Launch wichtig?]
**Priorität:** Hoch / Mittel / Niedrig
```

Kimi bearbeitet diese Anfrage bei nächster Gelegenheit und schreibt das Ergebnis in die passende Live-Research-Datei.

---

## Update-Rhythmus

| Agent | Pflicht-Update |
|-------|----------------|
| Claude | Am Anfang jeder Session: Live-Research lesen. Am Ende jeder Session: Session-Log schreiben. |
| Kimi | Mindestens einmal pro Session oder auf explizite Anfrage: Live-Research aktualisieren. |

---

## Konfliktlösung

| Situation | Lösung |
|-----------|--------|
| Beide wollen dieselbe Datei bearbeiten | Claude hat Vorrang bei technischen Dateien (`landing-page.html`, `empire-config.json`). Kimi hat Vorrang bei Recherche-Dateien. |
| Unterschiedliche Strategieempfehlungen | Nutzer entscheidet. Bis dahin: Teste beide Varianten (A/B). |
| Kimi findet neue Daten, die Claude bereits umgesetzt hat | Claude aktualisiert seine Umsetzung basierend auf den neuen Daten. |
| Claude braucht sofortige Antwort von Kimi | Anfrage in `REQUEST-FOR-KIMI.md` mit Priorität „Hoch" markieren. |

---

## Lern-Loop

1. Claude testet eine Taktik.
2. Claude dokumentiert Ergebnis in `CLAUDE-SESSION-LOG.md`.
3. Kimi liest das Log und recherchiert, warum etwas funktioniert/nicht funktioniert.
4. Kimi gibt Empfehlungen in Live-Research-Dateien.
5. Claude integriert Empfehlungen in die nächste Iteration.

---

## Befehle für den Nutzer

| Befehl | Auswirkung |
|--------|------------|
| „Kimi, recherchiere [Thema]" | Kimi schreibt Anfrage selbst oder bearbeitet sie direkt. |
| „Claude, prüfe Kimis neueste Recherche" | Claude liest alle Live-Research-Dateien. |
| „Sync" | Beide Agenten lesen die gemeinsamen Dateien neu. |
| „Wer hat was zuletzt geändert?" | Beide Agenten prüfen `CLAUDE-SESSION-LOG.md` und Live-Research-Zeitstempel. |
