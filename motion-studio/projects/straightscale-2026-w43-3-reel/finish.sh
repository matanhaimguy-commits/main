#!/usr/bin/env bash
# ./finish.sh [mux vN] : music + effects (no voice) -> master -14 LUFS / -1.5 dBTP -> audio/mix.wav;
#   with "mux vN": join out/seg*.mp4 into out/silent.mp4 and mux into deliver/vN/.
set -euo pipefail
DUR=$(python3 -c "import json; print(json.load(open('audio/events.json'))['duration'])")
# effects sit 4 dB under the music; the score's low mids are eased so the clicks read on phone speakers
ffmpeg -loglevel error -y -i audio/music.wav -i audio/sfx.wav -filter_complex \
  "[0:a]highpass=f=55,equalizer=f=170:width_type=o:w=1.0:g=-4,equalizer=f=280:width_type=o:w=1.0:g=-3[m];[1:a]volume=-4dB[f];[m][f]amix=inputs=2:normalize=0,atrim=0:$DUR[o]" \
  -map "[o]" -ar 48000 -c:a pcm_s24le audio/mix_raw.wav
ffmpeg -hide_banner -i audio/mix_raw.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 | sed -n '/{/,/}/p' > audio/loudnorm.json
AF=$(python3 -c "
import json; m = json.load(open('audio/loudnorm.json'))
print(f\"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true\")")
ffmpeg -loglevel error -y -i audio/mix_raw.wav -af "$AF" -ar 48000 -c:a pcm_s24le audio/mix.wav
echo "audio/mix.wav written"
[ "${1:-}" = mux ] || exit 0
V=${2:-v1}; D=deliver/$V; mkdir -p "$D"
printf "file 'seg0.mp4'\nfile 'seg1.mp4'\nfile 'seg2.mp4'\n" > out/segs.txt
ffmpeg -loglevel error -y -f concat -safe 0 -i out/segs.txt -c copy out/silent.mp4
ffmpeg -loglevel error -y -i out/silent.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k \
  -movflags +faststart -shortest "$D/straightscale_w43_3_reel_9x16.mp4"
echo "$D: $(ls "$D" | tr '\n' ' ')"
