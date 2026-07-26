# UHC Keiler – Konzept für die neue Website

*Stand: 26. Juli 2026*

---

## 1. Ausgangslage

Die bestehende Seite läuft auf WordPress 6.1.1 (Dezember 2022) ohne HTTPS. Der letzte
Beitrag stammt vom Oktober 2022, die Ergebnisse enden 2017, die Fotogalerien 2019.

Konkrete Baustellen:

- **Sicherheit:** WordPress seit über drei Jahren ohne Updates, kein SSL-Zertifikat,
  Login-Link öffentlich in der Seitenleiste
- **Recht:** Kein Impressum, keine Datenschutzerklärung auffindbar
- **Kaputte Inhalte:** Auf „Die Aktiven" steht roher Shortcode-Code sichtbar im Text
  (`[vc_row]`, `[team_member …]`) – Reste eines nicht mehr aktiven Page Builders.
  Die Spielerfotos werden nicht angezeigt.
- **Toter Instagram-Feed:** Zeigt seit rund drei Jahren Platzhalter statt Bildern,
  der Zugangstoken ist abgelaufen
- **Struktur:** Fast alles läuft über Kategorie-Archive. Menüpunkte wie „Termine",
  „Wir über uns" und „Adressen etc." zeigen auf einzelne Blogbeiträge von 2009.
- **Karteileichen:** Kategorien „Büchertipps", „Latest", „Newsflash", „Uncategorized"
  aus einem längst ersetzten News-Theme

---

## 2. Grundidee

**Die Website wird das Langzeitgedächtnis der Keiler. Instagram bleibt der Alltagskanal, SpielerPlus die Termin-App, Sixpack-liga.de die Ergebnisseite**

Das erklärt die Aufteilung: Alles Kurzlebige – Termine, Ergebnisse, News – wandert
dorthin, wo es ohnehin schon stattfindet oder besser aufgehoben ist. Was auf der
Website bleibt, ist das, was Bestand haben soll.

Der Nebeneffekt ist der eigentliche Gewinn: Eine Seite ohne kurzlebige Inhalte braucht
keine laufende Pflege. Genau daran ist die alte Seite gescheitert – nicht an der
Technik, sondern daran, dass ständige Pflege nötig war und irgendwann ausblieb.

---

## 3. Struktur der neuen Seite

Alles passt auf **eine durchscrollende Startseite** plus zwei Rechtsseiten:

| Abschnitt | Inhalt |
|---|---|
| Kopf | Mannschaftsfoto, Name, kurzer Claim |
| Wer wir sind | Ein Absatz: was, wo, seit wann |
| **Chronik** | Das Herzstück – die Geschichte der Keiler |
| Mannschaftsfotos | Über die Jahre, Vornamen höchstens in Bildunterschriften |
| Instagram | Eingebetteter Feed |
| Ergebnisse | Sixpack-tabelle (Link oder Einbettung – siehe offene Punkte) |
| Kontakt | E-Mail, Hinweis „Neue Spieler willkommen" |
| Fußzeile | Impressum, Datenschutzerklärung |

Wenn die Chronik umfangreich wird, bekommt sie eine eigene Unterseite. Das entscheidet
sich beim Schreiben.

---

## 4. Die Entscheidungen im Einzelnen

| # | Bereich | Entscheidung |
|---|---|---|
| 1 | Aktueller Kader | **Weglassen.** Damit entfällt die kaputte Shortcode-Seite ersatzlos. |
| 2 | Passive & Ehemalige | **Keine Namenslisten.** Stattdessen Mannschaftsfotos, gelegentlich ein aktuelles ergänzt. Vornamen höchstens in Bildunterschriften. |
| 3 | Termine | **Weglassen.** Läuft über SpielerPlus, inklusive Zu- und Absagen. |
| 4 | Ergebnisse aktuell | **Sixpack-tabelle.** Link oder Einbettung – offen. |
| 5 | Ergebnis-Archiv 2007–2017 | **Weglassen.** Bleibt im Backup erhalten. |
| 6 | Fotoarchiv (62 Galerien) | **Offen** – Auswahl oder weglassen. |
| 7 | Event-Berichte | **Weglassen.** News laufen über Instagram. |
| 8 | Wir über uns | **Ausführlich, mit Chronik.** Der Schwerpunkt der neuen Seite. |
| 9 | Sitzungsprotokolle | **Intern behalten**, nicht öffentlich. Dienen als Chronik-Quelle. |
| 10 | Interner Bereich | **Weglassen.** SpielerPlus und WhatsApp decken das ab. |
| 11 | Instagram | **Feed einbetten**, aber ausfallsicher gebaut (siehe Technik). |
| 12 | Kontakt | **E-Mail** plus Hinweis „Neue Spieler willkommen". |

---

## 5. Umgang mit den Altdaten

**Nichts wird gelöscht, vieles wird nur nicht mehr veröffentlicht.**

1. **Vollexport** der WordPress-Inhalte plus Mediendateien, privat abgelegt
2. **Materialsammlung für die Chronik** wird aus dem Export gezogen, bevor etwas
   entfällt – Daten, Ereignisse, Ergebnisse, Fotos mit Datum
3. **Protokolle** getrennt in einem internen Ordner, ebenfalls als Chronik-Quelle
4. **Alte URLs** werden auf die neue Startseite umgeleitet, statt ins Leere zu laufen

### Bereits gefundene Ankerpunkte für die Chronik

Aus der bestehenden Seite und dem Instagram-Kanal:

- **2007–2017** – Ergebnisse durchgehend dokumentiert
- **2013** – Protokolle der Mannschaftssitzungen beginnen
- **2018** – Aufstieg in die Gruppe Titan
- **2018** – Peter gibt die Rolle des Oberkeilers an Arne ab
- **2018** – Keiler-Anton-Cup, Frischlingsfest, Kinderfest im UHC
- **2019** – Keiler-Anton-Cup, Segelwochenende Harlingen–Terschelling,
  Strandsegeln in St. Peter-Ording, Spiel gegen die Prinzen am 10.9.
- **2022** – Erste Pokalrunde 2:0 gegen die Alstersticks, 20. Prinzen Herbstcup,
  Kart-Racing, Winterhockey
- **2023** – Paddle Tennis, acht selbstgebaute Kindertore für den UHC,
  Begegnung mit UHC-Weltmeister Hannes Müller

Das ist das Gerüst. Was fehlt, sind die Jahre vor 2018 und alles, was nie
aufgeschrieben wurde.

---

## 6. Offene Punkte für die Mannschaft

1. **Namen:** Dürfen eure Namen auf der Seite genannt werden? Vorschalg: nur Vornamen.
2. **Siypack-tabelle:** Nur verlinken oder direkt einbetten?
3. **Fotoarchiv:** Auswahl retten oder ganz weglassen – *und wer sortiert?*
4. **Chronik:** Wer steuert Erinnerungen, Fotos und Material bei?

Punkt 4 ist der wichtigste. Ohne Zulieferung entsteht die Chronik aus dem Gedächtnis
einer einzigen Person.

Punkt 3 wird oft unterschätzt: „Auswahl" heißt, dass jemand 62 Galerien durchsehen
und aussortieren muss.

---

## 7. Technik

| Baustein | Wahl | Warum |
|---|---|---|
| Generator | **Hugo** | Ein einzelnes Programm ohne Abhängigkeiten. Keine Updates nötig, keine Paketverrottung. |
| Versionierung | **GitHub**, privates Repo in einer Organisation „UHC Keiler" | Hängt nicht an einem Privatkonto. Übergabe später ist ein Klick. |
| Hosting | **Cloudflare Pages** | Kostenlos auch für private Organisations-Repos, HTTPS automatisch, baut bei jeder Änderung, die auf GitHub eingecheckt wird. |
| Bearbeitung | Direkt in der GitHub-Weboberfläche | Kein CMS-Layer, der verrotten kann. Geht auch vom Handy. |
| Instagram | GitHub Action, holt den Feed täglich ab und legt die Bilder fest ins Repository | Bei einer Störung bleibt der letzte Stand stehen, statt Platzhalter anzuzeigen. |

**Zum Instagram-Feed:** Der alte Feed lud die Bilder live im Browser über eine
Schnittstelle mit ablaufendem Token. Genau das ist kaputtgegangen. Die neue Variante
holt die Bilder einmal täglich im Hintergrund und speichert sie. Für Besucher sieht
das identisch aus – aber ein Ausfall bei Instagram friert die Seite nur ein, statt
sie zu beschädigen.

**Zu Cloudflare:** Pages und Workers werden gerade zusammengeführt, für neue Projekte
empfiehlt Cloudflare inzwischen Workers. Pages bleibt vollständig unterstützt, es gibt
keine Frist. Falls doch einmal umgestellt werden muss, betrifft das eine
Konfigurationsdatei, nicht die Inhalte.

---

## 8. Umsetzungsschritte

1. **Backup und Export** – WP-Admin → *Werkzeuge → Daten exportieren → Alle Inhalte*.
   Zusätzlich Datenbank und `wp-content` über den Hoster sichern.
2. **Materialsammlung** aus dem Export ziehen: Zeitstrahl, Ereignisse, Fotos mit Datum
3. **Umfrage** in der WhatsApp-Gruppe stellen (vier Punkte aus Abschnitt 6)
4. **Grundgerüst** aufsetzen: Repository, Hugo, Cloudflare Pages, Testadresse
5. **Impressum und Datenschutzerklärung** erstellen
6. **Chronik schreiben** – der eigentliche Aufwand
7. **Fotos** nach Umfrageergebnis übertragen
8. **Instagram-Automatik** einrichten
9. **Domain umziehen**, Weiterleitungen setzen, alte Seite abschalten

Die Schritte 1 bis 5 lassen sich parallel zur laufenden alten Seite erledigen.
Erst Schritt 9 ist der Umschaltmoment.

---

## 9. Aufwandseinschätzung

| Was | Aufwand |
|---|---|
| Technik komplett (Schritte 1, 4, 8, 9) | Ein Wochenende |
| Impressum und Datenschutz | Ein bis zwei Stunden mit Generator |
| Fotoauswahl | Abhängig von der Umfrage, mit Helfern ein Abend |
| **Chronik** | **Mehrere Abende – Schreibarbeit, keine Bastelei** |

Laufende Wartung danach: praktisch keine. Kein Update-Rhythmus, keine Plugins,
keine Tokens, die ablaufen.

---

## 10. Was übrig bleibt, wenn niemand mehr hinschaut

Das ist der eigentliche Prüfstein, denn genau dieser Fall ist eingetreten.

Bei der alten Seite hieß „ungepflegt" irgendwann: veraltet, angreifbar, kaputt.
Bei der neuen heißt es: eingefroren. Die Inhalte liegen als lesbare Textdateien
im Repository, die Seite ist reines HTML, es gibt nichts, was ablaufen oder
gehackt werden kann.

Eine eingefrorene Chronik ist ein völlig akzeptabler Zustand.
