#!/usr/bin/env bash
# ./finish.sh : mix music + sfx, master to -14 LUFS / -1 dBTP, mux with out/silent.mp4, write deliver/.
set -euo pipefail
ffmpeg -loglevel error -y -i audio/music.wav -i audio/sfx.wav -filter_complex \
  "[0:a]volume=0.8[m];[1:a]volume=0.7[s];[m][s]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]" \
  -map "[a]" -c:a pcm_s24le audio/mix_raw.wav
ffmpeg -hide_banner -i audio/mix_raw.wav -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 \
  | sed -n '/{/,/}/p' > audio/loudnorm.json
AF=$(python3 -c "
import json; m = json.load(open('audio/loudnorm.json'))
print(f\"loudnorm=I=-14:TP=-1:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true\")")
ffmpeg -loglevel error -y -i audio/mix_raw.wav -af "$AF" -ar 48000 -c:a pcm_s24le audio/mix.wav
mkdir -p deliver
ffmpeg -loglevel error -y -i out/silent.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k \
  -movflags +faststart -shortest deliver/straightscale_reel_9x16.mp4
../../review.sh deliver/straightscale_reel_9x16.mp4 7.9
cp out/contact.png deliver/contact.png
ffmpeg -loglevel error -y -ss 10.3 -i deliver/straightscale_reel_9x16.mp4 -frames:v 1 deliver/poster.png
echo "deliver/: $(ls deliver | tr '\n' ' ')"
