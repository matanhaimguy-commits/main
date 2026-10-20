#!/usr/bin/env bash
# ./finish.sh [vN] : master audio/mix_raw.wav (from audio/score.py) to -14 LUFS / true peak -1.5 dBTP with a two-pass
# loudnorm, then (with vN) mux it with out/silent_9x16.mp4 and out/silent_4x5.mp4 into deliver/vN/.
set -euo pipefail
cd "$(dirname "$0")"
TP=${TP:--2.0}   # ceiling before AAC; the encode adds a few tenths, the delivered file must stay <= -1.5 dBTP
# 1. gain to the target and a transparent look-ahead limiter on the transients (pops, merge, thud), so the
#    second stage can reach -14 LUFS in linear mode without touching the true-peak ceiling
LUFS() { ffmpeg -hide_banner -nostats -i "$1" -af ebur128 -f null - 2>&1 | sed -n 's/^ *I: *\(-*[0-9.]*\) LUFS/\1/p' | tail -1; }
I0=$(LUFS audio/mix_raw.wav); G=$(python3 -c "print(round(-14.0 - float('$I0'), 2))")
for k in 1 2 3; do   # the limiter eats some loudness: re-aim the pre-gain until its output sits at about -14.2 LUFS
  ffmpeg -loglevel error -y -i audio/mix_raw.wav -af "volume=${G}dB,alimiter=limit=0.66:attack=3:release=80:level=0:asc=1" -c:a pcm_s24le audio/mix_lim.wav
  IL=$(LUFS audio/mix_lim.wav); G=$(python3 -c "print(round($G + (-14.2 - float('$IL')), 2))")
done
# 2. two-pass loudnorm (linear) to -14 LUFS, true peak ceiling $TP
ffmpeg -hide_banner -i audio/mix_lim.wav -af loudnorm=I=-14:TP=$TP:LRA=11:print_format=json -f null - 2>&1 \
  | sed -n '/{/,/}/p' > audio/loudnorm.json
AF=$(python3 -c "
import json; m = json.load(open('audio/loudnorm.json'))
print(f\"loudnorm=I=-14:TP=$TP:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true\")")
ffmpeg -loglevel error -y -i audio/mix_lim.wav -af "$AF,aresample=48000" -c:a pcm_s24le audio/mix.wav
echo "raw mix $I0 LUFS, limiter output $IL LUFS"
echo "audio/mix.wav written ($(python3 -c "import json; m=json.load(open('audio/loudnorm.json')); print('raw', m['input_i'], 'LUFS, TP', m['input_tp'])"))"
[ -n "${1:-}" ] || exit 0
V=$1; D=deliver/$V; mkdir -p "$D"
for F in 9x16 4x5; do
  ffmpeg -loglevel error -y -i out/silent_$F.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k \
    -movflags +faststart -shortest "$D/straightscale-05-three-things-$F.mp4"
done
ls -la "$D"
