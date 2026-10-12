#!/usr/bin/env bash
# ./finish.sh : mix voice + music (ducked under the voice) + sfx, master to -14 LUFS / -1 dBTP,
# mux with out/silent.mp4, write deliver/.
set -euo pipefail
# voice: the approved take with 2.5 s of silence cut in after "StraightScale." (36.75 s), padded to 50 s
ffmpeg -loglevel error -y -i audio/vo_v1.mp3 -filter_complex \
  "[0:a]aresample=44100,asplit[a][b];[a]atrim=0:36.75,asetpts=PTS-STARTPTS[p1];[b]atrim=start=36.75,asetpts=PTS-STARTPTS[p2];\
   aevalsrc=0:d=2.5:s=44100[gap];[p1][gap][p2]concat=n=3:v=0:a=1,apad=whole_dur=50,atrim=0:50,pan=stereo|c0=c0|c1=c0[o]" \
  -map "[o]" -c:a pcm_s24le audio/vo.wav
ffmpeg -loglevel error -y -i audio/music.wav -i audio/sfx.wav -i audio/vo.wav -filter_complex \
  "[0:a]volume=0.3[m];[2:a]asplit[v][key];[m][key]sidechaincompress=threshold=0.02:ratio=6:attack=15:release=350[md];\
   [1:a]volume=0.4[s];[md][s][v]amix=inputs=3:normalize=0,alimiter=limit=0.95[a]" \
  -map "[a]" -c:a pcm_s24le audio/mix_raw.wav
ffmpeg -hide_banner -i audio/mix_raw.wav -af loudnorm=I=-14:TP=-1:LRA=11:print_format=json -f null - 2>&1 \
  | sed -n '/{/,/}/p' > audio/loudnorm.json
AF=$(python3 -c "
import json; m = json.load(open('audio/loudnorm.json'))
print(f\"loudnorm=I=-14:TP=-1:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true\")")
ffmpeg -loglevel error -y -i audio/mix_raw.wav -af "$AF" -ar 48000 -c:a pcm_s24le audio/mix.wav
mkdir -p deliver
ffmpeg -loglevel error -y -i out/silent.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k \
  -movflags +faststart -shortest deliver/straightscale_reel_9x16_vo.mp4
../../review.sh deliver/straightscale_reel_9x16_vo.mp4 16.4
cp out/contact.png deliver/contact.png
ffmpeg -loglevel error -y -ss 11.0 -i deliver/straightscale_reel_9x16_vo.mp4 -frames:v 1 deliver/poster.png
echo "deliver/: $(ls deliver | tr '\n' ' ')"
