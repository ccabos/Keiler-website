# UHC Keiler – Website

Die neue Seite für [uhc-keiler.de](https://uhc-keiler.de). Statisch gebaut mit
[Hugo](https://gohugo.io), versioniert auf GitHub, ausgeliefert von Cloudflare
Workers. Kein CMS, keine Datenbank, keine Plugins.

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

Dann http://localhost:1313 aufrufen. Für einmaliges Bauen:
`bash scripts/build.sh` – das Skript holt sich bei Bedarf die richtige
Hugo-Version selbst. Das Ergebnis landet in `public/` (nicht eingecheckt).

## Cloudflare Workers einrichten

Die Seite läuft als Worker, der nur die gebaute Seite aus `public/`
ausliefert. Die Einstellungen dafür stehen in `wrangler.jsonc`, gebaut wird
mit `scripts/build.sh`. Das Skript lädt die Hugo-Version aus `HUGO_VERSION`
(Vorgabe 0.164.0) selbst herunter, man ist also nicht darauf angewiesen,
was Cloudflare vorinstalliert hat.

Einmalig im Cloudflare-Dashboard:

1. **Workers & Pages → Create → Import a repository**, GitHub verbinden und
   `keiler-website` auswählen.
2. Einstellungen:

   | Einstellung | Wert |
   |---|---|
   | Project name | `keiler-website` (muss zu `name` in `wrangler.jsonc` passen) |
   | Build command | `bash scripts/build.sh` |
   | Deploy command | `npx wrangler deploy` |
   | Root directory | leer lassen |

3. **Deploy**. Danach ist die Seite unter
   `keiler-website.<konto>.workers.dev` zu sehen.

Ab dann baut Cloudflare bei jedem Commit auf `main` neu.

Die eigene Domain kommt erst am Ende dazu (Schritt 9 im Konzept): unter
**Settings → Domains & Routes → Add → Custom domain** `uhc-keiler.de` und
`www.uhc-keiler.de` eintragen. Voraussetzung ist, dass das DNS der Domain bei
Cloudflare liegt. Vor dem Umstellen der Nameserver prüfen, dass die
MX-Einträge für die E-Mail übernommen wurden.

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
