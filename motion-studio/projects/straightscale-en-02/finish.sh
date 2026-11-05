#!/usr/bin/env bash
# ./finish.sh        : mix voice + music (ducked from the word timings, audio/mix.py) + sfx, master to -14 LUFS / -1.5 dBTP -> audio/mix.wav
# ./finish.sh mux v1 : also mux with out/silent.mp4 into deliver/v1/
# Before: ~/lemo/.venv/bin/python audio/score.py (music.wav, sfx.wav from audio/events.json)
set -euo pipefail
DUR=42.15
# voice: audio/vo.wav (Kokoro af_heart, audio/tts_kokoro.py), padded to the film length, centred
ffmpeg -loglevel error -y -i audio/vo.wav -af "aresample=48000,highpass=f=80,equalizer=f=250:width_type=o:w=1.2:g=-2.5,equalizer=f=3500:width_type=o:w=1.4:g=1.5,apad=whole_dur=$DUR,atrim=0:$DUR,pan=stereo|c0=c0|c1=c0" \
  -c:a pcm_s24le audio/vo_st.wav
# score EQ: clear the low mids under the voice, soften the top where the voice's consonants live
ffmpeg -loglevel error -y -i audio/music.wav -af "highpass=f=40,equalizer=f=220:width_type=o:w=1.4:g=-7,equalizer=f=3000:width_type=o:w=1.5:g=-3" \
  -c:a pcm_s24le audio/music_eq.wav
python3 audio/mix.py
ffmpeg -hide_banner -i audio/mix_raw.wav -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null - 2>&1 \
  | sed -n '/{/,/}/p' > audio/loudnorm.json
AF=$(python3 -c "
import json; m = json.load(open('audio/loudnorm.json'))
print(f\"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true\")")
ffmpeg -loglevel error -y -i audio/mix_raw.wav -af "$AF" -ar 48000 -c:a pcm_s24le audio/mix.wav
echo "audio/mix.wav written"
[ "${1:-}" = mux ] || exit 0
V=${2:-v1}; D=deliver/$V; mkdir -p "$D"
ffmpeg -loglevel error -y -i out/silent.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k \
  -movflags +faststart -shortest "$D/straightscale_en02_9x16.mp4"
echo "$D: $(ls "$D" | tr '\n' ' ')"
