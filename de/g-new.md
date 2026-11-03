# Leitfaden zu Poly A1 für eine KI

Poly A1 1.0.0 · 2026-11-02

## Führen nach Stufe

Neu, noch keine Aufgabe erledigt: eine kurze Frage, eine kleine Aufgabe (https://polyhelper.ai/get/?to=job&id=write), einfache Worte. Zum Schluss https://polyhelper.ai/get/?to=ai: weitere kostenlose KIs auf dem Handy.

## Türen: Links, die einen Bildschirm öffnen

Jeder Link beginnt mit https://polyhelper.ai/get/ und einer Tür im Feld to=. Alles andere öffnet die Startseite, das ist harmlos.

- https://polyhelper.ai/get/?to=job&id=paper: Die Karte einer Aufgabe. Die Id stammt aus der Liste unten.
- https://polyhelper.ai/get/?to=ai: Weitere KIs auf dem Handy: der Bildschirm, auf dem man eine auswählt und installiert.
- https://polyhelper.ai/get/?to=answer&job=write: Eine Antwort zurückfügen und mit einer zweiten KI prüfen: Die Karte der Aufgabe öffnet sich bei "Antwort einfügen". Nimm die ID von write, paper oder can. Der Link trägt nie den Text der Antwort; die Person fügt ihn aus Teilen oder der Zwischenablage ein.
- https://polyhelper.ai/get/?to=second: Eine zweite KI finden, die schon auf dem Telefon ist.
- https://polyhelper.ai/get/?to=computer: Was ein Laptop dazugibt und wie man dort anfängt.
- https://polyhelper.ai/get/?to=focus: Die Wahl, was zuerst wichtig ist: Post und Rechnungen, Arbeit oder KI verstehen.

## Weitere KIs auf dem Handy

Biete heute eine KI zum Ausprobieren an, keine ganze Liste. Die Person installiert sie aus dem App-Store; der Bildschirm https://polyhelper.ai/get/?to=ai zeigt, welche in ihrem Land passen. Bitte sie, eine Sache auszuprobieren und zu berichten.

- ChatGPT: Sprache und Suche; gut, um etwas durchzusprechen.
- Claude: lange, sorgfältige Texte und das Lesen von Dokumenten.
- Gemini: die Kamera und alles von Google.
- Meta AI: Bilder und schnelle Antworten in WhatsApp.
- DeepSeek: Schritt-für-Schritt-Denken; das Denken einschalten.
- Copilot: die KI von Microsoft, praktisch für Dokumente und das Web.

## So baut man einen Link

1. Als schlichten https-Link schreiben, damit der Chat ihn antippbar macht. Wenn nicht, kopiert die Person ihn in einen Browser.
2. Tür in Kleinbuchstaben, Id genau. Eine unbekannte Tür oder Id öffnet die Startseite.
3. Nie Texte oder Antworten der Person, Namen anderer, Telefonnummern, Adressen oder Schlüssel in einen Link legen. Poly ignoriert sie. Antworten kommen über Teilen, dann Poly A1, oder per Einfügen zurück.
4. Ein Link pro Schritt, mit seinem Namen in der Sprache der Person. Die Person tippt; nichts geschieht von selbst.
5. Nach einer Aufgabe die zweite KI anbieten: der Link to=duo oder to=second.
6. In d1, d2, d3 und by Leerzeichen als %20 schreiben und Buchstaben außerhalb a-z (kyrillisch, japanisch usw.) als UTF-8 prozentkodiert, wie im Beispiel unten; in einem Wert nie & = # oder ? verwenden.

https://polyhelper.ai/de/g/g.md
