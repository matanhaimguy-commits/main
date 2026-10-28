#!/usr/bin/env bash
# Creates the WORDS funnels in the hub once HUB_TOKEN is set and the EN 02 post is live.
#   bash create.sh <hub-business-slug> <en02-post-id>
# Find the slug with: python3 growth-engine/tools/hub.py clients (the business whose Instagram is @straightscale_).
# The post ID comes from the hub item after the post goes out (or the Instagram media ID).
set -euo pipefail
slug="$1"; post="$2"
here="$(cd "$(dirname "$0")" && pwd)"
hub="$here/../../../../../growth-engine/tools/hub.py"
tmp="$(mktemp -d)"
url="$(python3 "$hub" upload "$slug" "$here/../WORDS.pdf" | tail -1)"
case "$url" in https://*) ;; *) echo "upload failed: $url" >&2; exit 1 ;; esac
for f in words words-dm; do
  sed -e "s#__WORDS_PDF_URL__#$url#" -e "s#__EN02_POST_ID__#$post#" "$here/$f.funnel.json" > "$tmp/$f.json"
  python3 "$hub" funnel "$slug" "$tmp/$f.json"
done
echo "Check the result: no 'error' issues above, then test from a tester account before live."
