#!/usr/bin/env bash
# Download the five reference repos, complete and unmodified, at the exact commits we reviewed.
# Cloud containers are wiped between sessions, so run this at the start of any video job:
#   bash references/fetch.sh          (skips repos that are already here)
# The clones are gitignored: they are reference material, not part of this repo's history.
set -euo pipefail
cd "$(dirname "$0")"
REFS=(
  "hyperframes            https://github.com/heygen-com/hyperframes          4120042ca3b8e4c6e09ab9b76ce988d56837687b"
  "onetake                https://github.com/feitangyuan/onetake             2f5fbd363a0aec22055fbf62489380065737c91d"
  "gbro-collage-broll     https://github.com/pyang5166/gbro-collage-broll    a1a4ee2e2abf7d44e460026b706d0c72c2cf8a91"
  "claude-animation-base  https://github.com/JohnHeibel/claudeanimationbase  0ac8bf2b31942376cb6b8c4074715595d512acd2"
  "lemo-opuscar           https://github.com/lemomo-ai/lemo-opuscar          227e00adfbbec1ef4b7065a4189c2e1c8be2fef4"
)
for row in "${REFS[@]}"; do
  read -r name url sha <<<"$row"
  if [ "$(git -C "$name" rev-parse HEAD 2>/dev/null)" = "$sha" ]; then echo "ok    $name"; continue; fi
  rm -rf "$name"
  mkdir "$name"
  git -C "$name" init -q
  git -C "$name" remote add origin "$url"
  # one commit only; LFS objects are not served by the session proxy, so they stay as pointers
  GIT_LFS_SKIP_SMUDGE=1 git -C "$name" fetch -q --depth 1 origin "$sha"
  GIT_LFS_SKIP_SMUDGE=1 git -C "$name" checkout -q FETCH_HEAD
  echo "got   $name @ ${sha:0:7}"
done
