#!/usr/bin/env bash
# ./finish.sh [mux vN]
#   1. audio/score.py: music + foley from the film's own events (audio/events.json)
#   2. audio/mix.py: balance, gentle EQ, peak guard -> audio/mix_raw.wav
#   3. two-pass loudnorm to -14 LUFS / -2.0 dBTP (margin for AAC; target after encode <= -1.5 dBTP), then a linear trim
#      so ebur128 reads -14.0 -> audio/mix.wav
#   4. with "mux vN": mux out/silent.mp4 (9:16) and out/silent_45.mp4 (4:5) into deliver/vN/
set -euo pipefail
cd "$(dirname "$0")"
~/lemo/.venv/bin/python audio/score.py
python3 audio/mix.py
ffmpeg -hide_banner -i audio/mix_raw.wav -af loudnorm=I=-14:TP=-2.0:LRA=11:print_format=json -f null - 2>&1 \
  | sed -n '/{/,/}/p' > audio/loudnorm.json
AF=$(python3 -c "
import json; m = json.load(open('audio/loudnorm.json'))
print(f\"loudnorm=I=-14:TP=-2.0:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true\")")
ffmpeg -loglevel error -y -i audio/mix_raw.wav -af "$AF" -ar 48000 -c:a pcm_s24le audio/mix_ln.wav
# v2: loudnorm's own meter and ebur128 disagree by ~0.4 LU on this mix; trim linearly so ebur128 (what audio_qa and the
# reviewer use) reads -14.0 LUFS. A negative trim only lowers the true peak.
TRIM=$(ffmpeg -hide_banner -nostats -i audio/mix_ln.wav -af ebur128 -f null - 2>&1 | grep -A3 Summary | sed -n 's/.*I: *\(-[0-9.]*\) LUFS.*/\1/p' | python3 -c "import sys; print(round(-14.0 - float(sys.stdin.read().split()[0]), 2))")
echo "ebur128 trim $TRIM dB"
ffmpeg -loglevel error -y -i audio/mix_ln.wav -af "volume=${TRIM}dB" -ar 48000 -c:a pcm_s24le audio/mix.wav
python3 -c "import json; m=json.load(open('audio/loudnorm.json')); print('raw', m['input_i'], 'LUFS', m['input_tp'], 'dBTP; type', m['normalization_type'])"
[ "${1:-}" = mux ] || exit 0
V=${2:-v1}; D=deliver/$V; mkdir -p "$D"
ffmpeg -loglevel error -y -i out/silent.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k \
  -movflags +faststart -shortest "$D/one-message-9x16.mp4"
ffmpeg -loglevel error -y -i out/silent_45.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k \
  -movflags +faststart -shortest "$D/one-message-4x5.mp4"
echo "$D: $(ls "$D" | tr '\n' ' ')"
