#!/usr/bin/env bash
# Baut die Seite nach public/. Wird von Cloudflare bei jedem Commit aufgerufen,
# funktioniert aber genauso lokal.
#
# Das Skript lädt die passende Hugo-Version selbst herunter, falls sie nicht
# schon installiert ist. So hängt der Build nicht davon ab, welche Hugo-Version
# Cloudflare gerade mitbringt.
set -euo pipefail

HUGO_VERSION="${HUGO_VERSION:-0.164.0}"

if command -v hugo >/dev/null 2>&1 && hugo version | grep -q "v${HUGO_VERSION}"; then
  HUGO=hugo
else
  case "$(uname -m)" in
    x86_64)        ARCH=amd64 ;;
    aarch64|arm64) ARCH=arm64 ;;
    *) echo "Unbekannte Architektur: $(uname -m)" >&2; exit 1 ;;
  esac
  DIR=".hugo-bin/${HUGO_VERSION}"
  if [ ! -x "${DIR}/hugo" ]; then
    echo "Lade Hugo ${HUGO_VERSION} herunter …"
    mkdir -p "${DIR}"
    curl -fsSL "https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux-${ARCH}.tar.gz" \
      | tar -xz -C "${DIR}" hugo
  fi
  HUGO="${DIR}/hugo"
fi

"${HUGO}" version
"${HUGO}" --minify
