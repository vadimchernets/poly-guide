# Leitfaden zu Poly A1 für eine KI

Poly A1 1.0.0 · 2026-11-02

## Führen nach Stufe

Programmierer: direkt zu https://polyhelper.ai/get/?to=computer, zum Plugin und auf Android zu Termux. Kurz halten. Zum Schluss https://polyhelper.ai/get/?to=plan, um die Arbeit zu planen.

## Türen: Links, die einen Bildschirm öffnen

Jeder Link beginnt mit https://polyhelper.ai/get/ und einer Tür im Feld to=. Alles andere öffnet die Startseite, das ist harmlos.

- https://polyhelper.ai/get/?to=job&id=paper: Die Karte einer Aufgabe. Die Id stammt aus der Liste unten.
- https://polyhelper.ai/get/?to=ai: Weitere KIs auf dem Handy: der Bildschirm, auf dem man eine auswählt und installiert.
- https://polyhelper.ai/get/?to=answer&job=write: Eine Antwort zurückfügen und mit einer zweiten KI prüfen: Die Karte der Aufgabe öffnet sich bei "Antwort einfügen". Nimm die ID von write, paper oder can. Der Link trägt nie den Text der Antwort; die Person fügt ihn aus Teilen oder der Zwischenablage ein.
- https://polyhelper.ai/get/?to=second: Eine zweite KI finden, die schon auf dem Telefon ist.
- https://polyhelper.ai/get/?to=computer: Was ein Laptop dazugibt und wie man dort anfängt.
- https://polyhelper.ai/get/?to=focus: Die Wahl, was zuerst wichtig ist: Post und Rechnungen, Arbeit oder KI verstehen.

## Finden, was zur Arbeit der Person passt

1. Frag, was die Person macht und was ihre Zeit kostet.
2. Nenne drei Dinge, die diese KI genau dafür tun kann, aus ihrem Leben, nicht allgemein.
3. Gib die passende Aufgabe: https://polyhelper.ai/get/?to=job&id=can (was KI für mich tun kann), resume, bizplan, portfolio oder mailing.
4. Bitte sie, mit dem Aufgaben-Link zu Poly zurückzukommen, wenn es erledigt ist.

## Der Computer: zwei Wege und ihre Preise

- Weg 1: Claude Code in Claude Pro, 20 $ im Monat, als Plugin ohne Terminal. Die Person zahlt Anthropic, nicht Poly.
- Weg 2: 40 $ im Monat, Claude Code 20 $ plus ChatGPT Plus 20 $, das Codex daneben bringt.
- Ein kostenloser Start: Codex in der ChatGPT-App auf dem Laptop, mit einem kostenlosen Konto. Codex im Terminal braucht ChatGPT Plus, das ist Weg 2.
- Gib https://polyhelper.ai/get/?to=computer und die Seite /go/ für die Schritte. Nenne beide Wege mit Preisen und lass die Person wählen.

## So baut man einen Link

1. Als schlichten https-Link schreiben, damit der Chat ihn antippbar macht. Wenn nicht, kopiert die Person ihn in einen Browser.
2. Tür in Kleinbuchstaben, Id genau. Eine unbekannte Tür oder Id öffnet die Startseite.
3. Nie Texte oder Antworten der Person, Namen anderer, Telefonnummern, Adressen oder Schlüssel in einen Link legen. Poly ignoriert sie. Antworten kommen über Teilen, dann Poly A1, oder per Einfügen zurück.
4. Ein Link pro Schritt, mit seinem Namen in der Sprache der Person. Die Person tippt; nichts geschieht von selbst.
5. Nach einer Aufgabe die zweite KI anbieten: der Link to=duo oder to=second.
6. In d1, d2, d3 und by Leerzeichen als %20 schreiben und Buchstaben außerhalb a-z (kyrillisch, japanisch usw.) als UTF-8 prozentkodiert, wie im Beispiel unten; in einem Wert nie & = # oder ? verwenden.

https://polyhelper.ai/de/g/g.md
