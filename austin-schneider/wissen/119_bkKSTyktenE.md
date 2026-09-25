---
nr: 119
titel: "I Built An Entire Agency Onboarding System In 45 Minutes"
url: https://www.youtube.com/watch?v=bkKSTyktenE
dauer_min: 14.2
themen: [Operations & Systeme, Fulfillment & Kundenbindung]
---

# I Built An Entire Agency Onboarding System In 45 Minutes

**Worum es geht:** Wette mit seinem Content-Verantwortlichen: Austin baut für die Agentur eines Kunden ("Saint", ~30–40.000 $/Monat) in unter 45 Minuten ein komplett automatisiertes Onboarding mit Notion, Zapier, eSignatures und Gmail – und gewinnt.

## Kernaussagen
- Mit automatisiertem Onboarding kann eine Agentur mehr Kunden aufnehmen, sie länger halten und der Gründer kommt aus dem Tagesgeschäft ([00:00](https://www.youtube.com/watch?v=bkKSTyktenE&t=0s)).
- Benötigte Bausteine: Sales-Intake-Formular, Onboarding-Formular, Vertragsvorlage, Onboarding-Kalender, Onboarding-SOP/Checkliste ([01:21](https://www.youtube.com/watch?v=bkKSTyktenE&t=81s)).
- Das Onboarding-Formular so kurz wie möglich halten: aktuelle Situation, Ziele, Erfahrungen mit früheren Agenturen – der Rest kommt im Onboarding-Call ([02:51](https://www.youtube.com/watch?v=bkKSTyktenE&t=171s)).
- Automatisierung allein reicht nicht; auch das, was danach passiert, muss als Checkliste produktisiert sein ([05:22](https://www.youtube.com/watch?v=bkKSTyktenE&t=322s)).
- Jedes Formular mit Testdaten ausfüllen, damit man die Automationen testen kann ([02:37](https://www.youtube.com/watch?v=bkKSTyktenE&t=157s)).

## Frameworks & Konzepte
- **Ablauf:** Deal gewonnen → interner Sales-Intake (Kontaktdaten, Deliverables, Preis, Zahlungsbedingungen, Laufzeit) → Zapier erstellt Vertrag aus der Vorlage mit Platzhaltern (eSignatures) → nach Unterschrift Welcome-Mail mit Link zum Onboarding-Formular (Filter: Vertragstitel beginnt mit einem festen Präfix, damit andere Verträge keine Welcome-Mail auslösen) → ausgefülltes Onboarding-Formular löst Mail mit Buchungslink aus.
- **Notion-Automationen:** Neuer Sales-Intake → Kunde automatisch im Client-OS mit Status "to onboard" und Startdatum. Neues Onboarding-Formular → Onboarding-Task mit Checkliste (pro Punkt Platz für ein Loom-Training) im Aufgaben-Board. Optional Slack-Benachrichtigung.
- **ChatGPT als Abkürzung:** für Formularfragen, Vertragsentwurf (kein Rechtsrat), Checkliste und E-Mail-Texte.

## Konkrete Umsetzung
- Nacheinander: Formulare in Notion bauen und testen → Vertragsvorlage mit Platzhaltern → drei Zaps (Intake → Vertrag, unterschrieben → Welcome-Mail, Onboarding-Formular → Buchungsmail) → Notion-Automationen für Client-OS und Task.
- Zum Schluss den kompletten Durchlauf mit einem Testkunden durchspielen und prüfen, ob Vertrag, Mails, Kundeneintrag und Aufgabe korrekt erscheinen.
