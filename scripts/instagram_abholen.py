#!/usr/bin/env python3
"""Holt die letzten Instagram-Beiträge und legt sie fest ins Repository.

Aufgerufen von .github/workflows/instagram.yml. Nutzt ausschliesslich die
Standardbibliothek – nichts zu installieren, nichts, was veralten kann.

Ergebnis:
  data/instagram.json          – Liste der Beiträge fuer das Hugo-Template
  static/bilder/instagram/*    – die Bilder als lokale Kopie

Grundsatz: Bei jedem Fehler bricht das Skript ab, ohne vorhandene Daten
anzufassen. Der letzte gute Stand bleibt damit immer stehen.
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ANZAHL = 12
WURZEL = Path(__file__).resolve().parent.parent
DATEN = WURZEL / "data" / "instagram.json"
BILDER = WURZEL / "static" / "bilder" / "instagram"

FELDER = "id,caption,media_type,media_url,thumbnail_url,permalink,timestamp"
MONATE = ("Januar", "Februar", "März", "April", "Mai", "Juni", "Juli",
          "August", "September", "Oktober", "November", "Dezember")


def hole(url):
    with urllib.request.urlopen(url, timeout=30) as antwort:
        return json.load(antwort)


def token_verlaengern(token):
    """Schiebt die 60-Tage-Frist bei jedem Lauf nach hinten."""
    url = ("https://graph.instagram.com/refresh_access_token"
           "?grant_type=ig_refresh_token&access_token=" + token)
    try:
        hole(url)
    except urllib.error.URLError as fehler:
        # Kein Abbruchgrund: Der Abruf selbst kann trotzdem funktionieren.
        print(f"Hinweis: Token konnte nicht verlaengert werden ({fehler}).")


def datum_deutsch(zeitstempel):
    zeit = datetime.fromisoformat(zeitstempel.replace("+0000", "+00:00"))
    zeit = zeit.astimezone(timezone.utc)
    return f"{zeit.day}. {MONATE[zeit.month - 1]} {zeit.year}"


def main():
    nutzer = os.environ.get("IG_USER_ID", "").strip()
    token = os.environ.get("IG_ACCESS_TOKEN", "").strip()
    if not nutzer or not token:
        sys.exit("IG_USER_ID und IG_ACCESS_TOKEN muessen gesetzt sein.")

    url = (f"https://graph.instagram.com/{nutzer}/media"
           f"?fields={FELDER}&limit={ANZAHL}&access_token={token}")

    try:
        antwort = hole(url)
    except urllib.error.URLError as fehler:
        sys.exit(f"Abruf fehlgeschlagen, vorhandener Stand bleibt: {fehler}")

    BILDER.mkdir(parents=True, exist_ok=True)
    beitraege = []
    behalten = set()

    for eintrag in antwort.get("data", []):
        # Bei Videos ist media_url die Videodatei – wir wollen das Standbild.
        quelle = (eintrag.get("thumbnail_url")
                  if eintrag.get("media_type") == "VIDEO"
                  else eintrag.get("media_url"))
        if not quelle:
            continue

        name = f"{eintrag['id']}.jpg"
        ziel = BILDER / name
        behalten.add(name)

        if not ziel.exists():
            try:
                with urllib.request.urlopen(quelle, timeout=60) as bild:
                    ziel.write_bytes(bild.read())
            except urllib.error.URLError as fehler:
                print(f"Bild {eintrag['id']} uebersprungen: {fehler}")
                behalten.discard(name)
                continue

        beitraege.append({
            "id": eintrag["id"],
            "bild": f"/bilder/instagram/{name}",
            "permalink": eintrag.get("permalink", ""),
            "text": (eintrag.get("caption") or "").strip(),
            "datum": datum_deutsch(eintrag["timestamp"]),
        })

    if not beitraege:
        sys.exit("Keine Beitraege erhalten, vorhandener Stand bleibt unveraendert.")

    # Bilder aufraeumen, die nicht mehr im Feed stehen.
    for datei in BILDER.glob("*.jpg"):
        if datei.name not in behalten:
            datei.unlink()

    DATEN.parent.mkdir(parents=True, exist_ok=True)
    DATEN.write_text(
        json.dumps(beitraege, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"{len(beitraege)} Beitraege geschrieben.")

    token_verlaengern(token)


if __name__ == "__main__":
    main()
