#!/usr/bin/env bash
# StraightScale 06 "The 108-hour week": rebuild everything from source, in order.
#   ./finish.sh audio          events -> score -> master (audio/mix.wav, -14 LUFS, true peak ceiling -2.0 dBTP pre-AAC)
#   ./finish.sh render         HyperFrames delivery renders, 60 fps, silent: out/silent_9x16.mp4, out/silent_4x5.mp4
#   ./finish.sh draft          fast 30 fps drafts of both formats with the mix muxed in (out/draft_*.mp4)
#   ./finish.sh deliver vN     mux the masters into deliver/vN/ (+ viewing copy if > 30 MB, poster, contact sheet)
#   ./finish.sh all vN         audio + render + deliver
set -euo pipefail
cd "$(dirname "$0")"
P=$PWD
export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 HYPERFRAMES_SKIP_SKILLS=1
export HYPERFRAMES_BROWSER_PATH=${HYPERFRAMES_BROWSER_PATH:-/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell}
HF="npx -y hyperframes@0.8.150"
NAME=straightscale-06-108-hour-week
TP=${TP:--2.0}
LUFS() { ffmpeg -hide_banner -nostats -i "$1" -af ebur128 -f null - 2>&1 | sed -n 's/^ *I: *\(-*[0-9.]*\) LUFS/\1/p' | tail -1; }

audio() {
  bash tools/make45.sh >/dev/null
  node ../../tools/events.mjs "$P/film" > audio/events.json
  ~/lemo/.venv/bin/python audio/score.py
  # 1. gain toward the target through a transparent look-ahead limiter (pulses and the logo hit are the peaks)
  I0=$(LUFS audio/mix_raw.wav); G=$(python3 -c "print(round(-14.0 - float('$I0'), 2))")
  for k in 1 2 3; do
    ffmpeg -loglevel error -y -i audio/mix_raw.wav -af "volume=${G}dB,alimiter=limit=0.66:attack=3:release=80:level=0:asc=1" -c:a pcm_s24le audio/mix_lim.wav
    IL=$(LUFS audio/mix_lim.wav); G=$(python3 -c "print(round($G + (-14.2 - float('$IL')), 2))")
  done
  # 2. two-pass loudnorm, linear, to -14 LUFS with the true-peak ceiling $TP
  ffmpeg -hide_banner -i audio/mix_lim.wav -af loudnorm=I=-14:TP=$TP:LRA=11:print_format=json -f null - 2>&1 | sed -n '/{/,/}/p' > audio/loudnorm.json
  AF=$(python3 -c "
import json; m = json.load(open('audio/loudnorm.json'))
print(f\"loudnorm=I=-14:TP=$TP:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true\")")
  ffmpeg -loglevel error -y -i audio/mix_lim.wav -af "$AF,aresample=48000" -c:a pcm_s24le audio/mix.wav
  echo "raw $I0 LUFS -> limiter $IL LUFS -> audio/mix.wav $(LUFS audio/mix.wav) LUFS"
}

render() {
  bash tools/make45.sh >/dev/null
  (cd film && $HF render --quality delivery --fps 60 --output "$P/out/silent_9x16.mp4" 2>&1 | tr '\r' '\n' | grep -E 'rendered in|Error|error' | tail -3)
  (cd film-4x5 && $HF render --quality delivery --fps 60 --output "$P/out/silent_4x5.mp4" 2>&1 | tr '\r' '\n' | grep -E 'rendered in|Error|error' | tail -3)
}

draft() {
  bash tools/make45.sh >/dev/null
  (cd film && $HF render --quality draft --output "$P/out/draft_silent_9x16.mp4" 2>&1 | tr '\r' '\n' | grep -E 'rendered in' | tail -1)
  (cd film-4x5 && $HF render --quality draft --output "$P/out/draft_silent_4x5.mp4" 2>&1 | tr '\r' '\n' | grep -E 'rendered in' | tail -1)
  for F in 9x16 4x5; do
    ffmpeg -loglevel error -y -i out/draft_silent_$F.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest out/draft_$F.mp4
  done
}

deliver() {
  V=$1; D=deliver/$V; mkdir -p "$D"
  for F in 9x16 4x5; do
    ffmpeg -loglevel error -y -i out/silent_$F.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k \
      -movflags +faststart "$D/$NAME-$F.mp4"
  done
  SZ=$(stat -c %s "$D/$NAME-9x16.mp4")
  if [ "$SZ" -gt 30000000 ]; then
    ffmpeg -loglevel error -y -i "$D/$NAME-9x16.mp4" -c:v libx264 -preset slow -crf 23 -pix_fmt yuv420p -c:a copy -movflags +faststart "$D/$NAME-9x16-view.mp4"
  fi
  ls -la "$D"
}

case "${1:-all}" in
  audio) audio ;;
  render) render ;;
  draft) draft ;;
  deliver) deliver "${2:?version, e.g. v1}" ;;
  all) audio; render; deliver "${2:-v1}" ;;
  *) echo "usage: $0 audio|render|draft|deliver vN|all vN"; exit 1 ;;
esac
