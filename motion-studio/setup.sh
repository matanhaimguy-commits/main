#!/usr/bin/env bash
# Prepare a fresh session for video work. Cloud containers are wiped between sessions; run this first.
#   bash motion-studio/setup.sh            core: renderer deps, Python audio libs, reference repos, GSAP, HyperFrames CLI
#   bash motion-studio/setup.sh lemo       + a working Lemo-Opuscar library at ~/lemo (node deps, Python core, patched tools)
#   bash motion-studio/setup.sh voice      + Kokoro scratch voice (offline TTS; final client VO stays ElevenLabs)
#   bash motion-studio/setup.sh music      + real-instrument sampler packs (large; credit lines in knowledge/lemo-opuscar.md)
# Safe to run again: every step skips what is already there.
set -euo pipefail
STUDIO=$(cd "$(dirname "$0")" && pwd)
ROOT=$(dirname "$STUDIO")
HF_VERSION=0.8.150      # HyperFrames CLI version tested here (knowledge/hyperframes.md)
GSAP_VERSION=3.14.2     # the GSAP version HyperFrames scaffolds and registry items expect
LEMO=${LEMO_HOME:-$HOME/lemo}   # short path on purpose: Kokoro's espeak data path must stay under 160 bytes
say() { printf '\n== %s\n' "$*"; }

core() {
  say "renderer (Playwright, preinstalled Chromium)"
  (cd "$STUDIO" && [ -d node_modules/playwright ] || npm install --no-audit --no-fund --loglevel=error)

  say "Python audio and font libraries"
  python3 -c "import numpy, scipy, librosa, soundfile, fontTools" 2>/dev/null \
    || pip install -q numpy scipy librosa soundfile fonttools brotli 2>&1 | grep -v -i warning || true

  say "reference repos (references/)"
  bash "$ROOT/references/fetch.sh"

  say "GSAP $GSAP_VERSION, vendored (CDNs are blocked here)"
  if [ ! -f "$STUDIO/vendor/gsap.min.js" ]; then
    tmp=$(mktemp -d)
    (cd "$tmp" && npm pack -q "gsap@$GSAP_VERSION" >/dev/null && tar xzf "gsap-$GSAP_VERSION.tgz")
    mkdir -p "$STUDIO/vendor" && cp "$tmp/package/dist/gsap.min.js" "$STUDIO/vendor/"
    rm -rf "$tmp"
  fi

  say "HyperFrames CLI $HF_VERSION"
  HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 npx -y "hyperframes@$HF_VERSION" --version

  cat <<EOF

Ready. In this shell, before using HyperFrames:
  export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 HYPERFRAMES_SKIP_SKILLS=1
  export HYPERFRAMES_BROWSER_PATH=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
  HF="npx -y hyperframes@$HF_VERSION"
After every 'hyperframes init' or 'add', point GSAP at the vendored copy:
  mkdir -p assets/vendor && cp $STUDIO/vendor/gsap.min.js assets/vendor/
  grep -rl 'cdn.jsdelivr.net/npm/gsap' --include='*.html' . | xargs -r sed -i 's#https://cdn.jsdelivr.net/npm/gsap@$GSAP_VERSION/dist/gsap.min.js#assets/vendor/gsap.min.js#'
EOF
}

venv() {  # Python 3.12 venv inside the Lemo library (uv when present)
  if [ ! -x "$LEMO/.venv/bin/python" ]; then
    if command -v uv >/dev/null; then uv venv -q --python python3.12 "$LEMO/.venv"; else python3.12 -m venv "$LEMO/.venv"; fi
  fi
}
pipr() {  # install a requirements file into the Lemo venv
  if command -v uv >/dev/null; then uv pip install -q --python "$LEMO/.venv/bin/python" -r "$1"
  else "$LEMO/.venv/bin/python" -m pip install -q -r "$1"; fi
}

lemo() {
  say "Lemo-Opuscar working library at $LEMO (a copy; references/ stays untouched)"
  [ -f "$LEMO/AGENTS.md" ] || cp -r "$ROOT/references/lemo-opuscar" "$LEMO"
  (cd "$LEMO" && [ -d node_modules ] || npm install --no-audit --no-fund --loglevel=error)
  venv && pipr "$LEMO/requirements.txt"
  # Patched copies beside the originals (knowledge/lemo-opuscar.md section 6.5):
  #   mux on ffmpeg 6.1 wrongly rejects films under ~58 s; slow WebGL frames exceed the 30 s screenshot timeout
  sed 's/^DEC=\$(echo "\$M" | grep/DEC=$(ffmpeg -hide_banner -nostats -progress pipe:2 -i "$A" -f null - 2>\&1 | grep/' \
    "$LEMO/core/render/mux.sh" > "$LEMO/core/render/mux_fixed.sh"
  sed "s/type: 'jpeg', quality: 92 }/type: 'jpeg', quality: 92, timeout: 0 }/" "$LEMO/core/render/still.mjs" > "$LEMO/core/render/still_nt.mjs"
  sed "s/type: 'jpeg', quality: 95 }/type: 'jpeg', quality: 95, timeout: 0 }/" "$LEMO/core/render/video.mjs" > "$LEMO/core/render/video_nt.mjs"
  cat <<EOF

Lemo ready. Use the preinstalled browser, never its installer:
  export PLAYWRIGHT_CHROME=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell
  cd $LEMO && node core/render/still.mjs <project> 3 2.5 --size 1080x1920
Demo fonts are not in git: fetch them before rendering a demo (knowledge/lemo-opuscar.md 6.5, item 1).
EOF
}

voice() {
  [ -f "$LEMO/AGENTS.md" ] || lemo
  say "Kokoro scratch voice"
  venv && pipr "$LEMO/requirements-voice.txt"
  (cd "$LEMO" && sh tools/fetch.sh voice)
}

music() {
  [ -f "$LEMO/AGENTS.md" ] || lemo
  say "sampler (real instruments)"
  venv && pipr "$LEMO/requirements-music.txt"
  (cd "$LEMO" && sh tools/fetch.sh instruments vsco2ce)
  echo "More packs: sh tools/fetch.sh instruments salamander|karoryfer|vcsl|freepats (piano and drums need CC BY credit lines)"
}

core
for tier in "$@"; do
  case "$tier" in
    lemo) lemo ;; voice) voice ;; music) music ;;
    *) echo "unknown tier: $tier (lemo, voice, music)"; exit 1 ;;
  esac
done
