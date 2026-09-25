---
nr: 128
titel: "The Sales System I Use To Book 4397 Sales Calls For My Agency"
url: https://www.youtube.com/watch?v=nlogfkOfcSo
dauer_min: 11.2
themen: [Kundengewinnung & Outreach, Operations & Systeme]
---

# The Sales System I Use To Book 4397 Sales Calls For My Agency

**Worum es geht:** Schritt-für-Schritt-Anleitung, wie man Instagram-DMs mit einem Keyword per ManyChat automatisch beantwortet, taggt und über Zapier als Lead in einer Notion-Datenbank (Leads-/Setting-OS) ablegt – inklusive Slack-Benachrichtigung. (Derselbe Inhalt ist auch Teil von Nr. 123.)

## Kernaussagen
- "DM me [Keyword]"-Aktionen verpuffen oft, weil DMs im Posteingang untergehen und niemand trackt – ohne Daten weiß man nicht, ob etwas funktioniert ([00:44](https://www.youtube.com/watch?v=nlogfkOfcSo&t=44s)).
- ManyChat (ab ~15 $/Monat) automatisiert Antworten auf Keywords in DMs oder Kommentaren ([01:24](https://www.youtube.com/watch?v=nlogfkOfcSo&t=84s)).
- Antworten bewusst menschlich und schlicht halten; zu viele Buttons wirken unpersönlich und können der Leadgewinnung schaden ([03:28](https://www.youtube.com/watch?v=nlogfkOfcSo&t=208s)).
- Mit dem automatischen Eintrag entstehen automatisch auch Daten (Opt-ins pro Woche/Monat, Leads pro Stufe) – Grundlage für Entscheidungen und für die Führung eines Teams ([08:11](https://www.youtube.com/watch?v=nlogfkOfcSo&t=491s)).

## Frameworks & Konzepte
- **ManyChat-Setup:** Trigger "User sends a message" mit Bedingung "Message **is**" (nicht "contains", sonst lösen normale Sätze aus), Keyword auch mit Ausrufezeichen hinterlegen → Aktion: Tag setzen → kurze Smart Delay → Antwort wie "Danke für deine Nachricht, erzähl mir mehr über dein Business".
- **Zapier-Zap:** Trigger ManyChat "New Tagged User" (Tag wählen, mit echter Test-DM testen) → Notion "Create Database Item" in der Leads-Datenbank: Name, Status "initiated", Quelle "Instagram Opt-in", Datum (Zapier-Platzhalter für "jetzt"), Opt-in-Wort aus dem Tag, Instagram-Handle.
- **Häufige Stolperfalle:** In Notion muss Zapier unter Settings → Connections und zusätzlich an der konkreten Datenbank (••• → Connections) freigegeben sein; eindeutiger Datenbankname hilft beim Finden.
- **Zusatzaktionen:** Slack-Nachricht in einen #optins-Kanal (Keyword, Link zum ManyChat-Livechat), für Kunden auch SMS- oder E-Mail-Benachrichtigung "Neuer Lead".

## Zahlen & Beispiele
- Laut Austin mit diesem System über 335 Agenturen unterstützt; eigene Agentur bei ~223.000 $/Monat.

## Konkrete Umsetzung
- Pro Kampagne/Creative ein eigenes Keyword und einen eigenen Tag anlegen, damit sich Leads der Quelle zuordnen lassen.
- Zap mit einer Test-DM prüfen und kontrollieren, ob der Eintrag korrekt in der Leads-Datenbank und im Dashboard erscheint.
- Leads anschließend im Notion-Board durch die Stufen (initiated → … → booked/signed) bewegen.
