# UHC Keiler – Website

Die neue Seite für [uhc-keiler.de](https://uhc-keiler.de). Statisch gebaut mit
[Hugo](https://gohugo.io), versioniert auf GitHub, ausgeliefert von Cloudflare
Pages. Kein CMS, keine Datenbank, keine Plugins.

Das Konzept dahinter steht in [`keiler-website-konzept.md`](keiler-website-konzept.md).

---

## Was wo liegt

| Pfad | Inhalt |
|---|---|
| `content/_index.md` | Der Absatz „Wer wir sind" auf der Startseite |
| `content/chronik.md` | Der Fließtext der Chronik |
| `content/impressum.md` | Impressum – **noch Platzhalter** |
| `content/datenschutz.md` | Datenschutzerklärung – **noch Platzhalter** |
| `data/chronik.yaml` | Der Zeitstrahl der Chronik |
| `data/mannschaftsfotos.yaml` | Welche Mannschaftsfotos gezeigt werden |
| `data/instagram.json` | Wird von der GitHub Action geschrieben, nicht von Hand |
| `static/bilder/` | Alle Bilddateien |
| `layouts/` | Die HTML-Vorlagen |
| `assets/css/main.css` | Das gesamte Aussehen, eine einzige Datei |
| `hugo.toml` | Titel, Claim, E-Mail, Instagram-Name, Sixpack-Link |

## Etwas ändern

Für Text und Zeitstrahl braucht es keine Werkzeuge: Datei auf github.com
öffnen, Stift anklicken, ändern, „Commit changes". Cloudflare baut die Seite
danach von selbst neu, das dauert etwa eine Minute. Geht auch vom Handy.

Bilder gehen genauso: In `static/bilder/` auf „Add file → Upload files".

## Lokal bauen

```
hugo server
```

Dann http://localhost:1313 aufrufen. Für einmaliges Bauen: `hugo --minify`,
das Ergebnis landet in `public/` (nicht eingecheckt).

## Cloudflare Pages einrichten

Beim Anlegen des Projekts im Cloudflare-Dashboard:

| Einstellung | Wert |
|---|---|
| Framework preset | Hugo |
| Build command | `hugo --minify` |
| Build output directory | `public` |
| Environment variable | `HUGO_VERSION` = `0.164.0` |

`HUGO_VERSION` ist wichtig: Ohne die Angabe nimmt Cloudflare eine sehr alte
Hugo-Version, mit der dieser Aufbau nicht baut.

## Noch offen

Die vier Fragen an die Mannschaft aus Abschnitt 6 des Konzepts:

1. **Namen** – dürfen Vornamen genannt werden? Betrifft die Bildunterschriften
   in `data/mannschaftsfotos.yaml`.
2. **Sixpack-Tabelle** – verlinken oder einbetten? Umschalter ist
   `sixpackEmbed` in `hugo.toml`.
3. **Fotoarchiv** – Auswahl aus den 62 Galerien oder weglassen, und wer sortiert?
4. **Chronik** – wer steuert Erinnerungen und Material bei?

Dazu technisch:

- Impressum und Datenschutzerklärung ausfüllen (Schritt 5)
- Mannschaftsfoto für den Kopf nach `static/bilder/` legen und `heroImage`
  in `hugo.toml` setzen
- Instagram-Automatik scharf schalten, siehe Kopf von
  `.github/workflows/instagram.yml`
- Weiterleitungen der alten WordPress-URLs (Schritt 9)
