#!/bin/bash
# v3 edit of the Sat 17 quote reel (16 Oct 2026), run in the Higgsfield sandbox in /home/user/daily/reel/v3.
# Inputs from the 15 Oct build: clip.mp4 (H3 keyframe clip), vo.mp3 (ElevenLabs eleven_v4, take 2), music.mp3, wm2.png
# (the real wordmark). No new generation: 0 credits. Fixes from FINAL.v1 and FINAL.v2 reviews: voice from 0.05 s, a one-line
# hook super in the clear band above the owner's head (y 274 to 370), 80 px caption cards of 1 to 3 words inside the
# Reels safe zone, crimson #B31217 highlights, end-card music held, compressor + gain + oversampled limiter to -14 LUFS.
set -e
cd /home/user/daily/reel/v3
# audio: end-card music x1.8, light compressor, then gain to about -14 LUFS and a 4x-oversampled limiter
ffmpeg -y -v error -i vo.mp3 -i music.mp3 -filter_complex "
[0:a]atrim=start=0.05,asetpts=PTS-STARTPTS,apad,atrim=0:13.6,asplit=2[vo][sc];
[1:a]atrim=0:13.6,afade=t=in:d=0.8,volume='if(gte(t,10.2),1.8,1)':eval=frame,afade=t=out:st=13.1:d=0.5,volume=0.30[mu];
[mu][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];
[vo][duck]amix=inputs=2:duration=first:normalize=0,acompressor=threshold=0.08:ratio=2.5:attack=15:release=250:makeup=1[a]" \
 -map "[a]" -ar 48000 mix_1.8.wav
I=$(ffmpeg -hide_banner -i mix_1.8.wav -af loudnorm=print_format=json -f null - 2>&1 | sed -n '/{/,/}/p' | python3 -c "import json,sys;print(json.load(sys.stdin)['input_i'])")
G=$(python3 -c "print(round(-13.4-($I),2))")
ffmpeg -y -v error -i mix_1.8.wav -af "volume=${G}dB,aresample=192000,alimiter=limit=0.80:attack=1:release=50:level=false,aresample=48000" n_1.8.wav
# picture
F=/usr/share/fonts/truetype/higgsfield/Montserrat-ExtraBold.ttf
DARK="box=1:boxcolor=0x1F1F1F@0.6:boxborderw=22"
RED="box=1:boxcolor=0xB31217@1:boxborderw=22"
# k0 "është për tani," k1 "jo përgjithmonë." k2 "Ke kaluar" k3 "edhe të tjera." k4 "Mbylle për sot," k5 "pusho,"
# k6 "dhe nesër" k7 "fillo nga një" k8 "gjë e vogël."; h1 "Kjo javë e vështirë"; ce1-3 the end card lines
C=( "k0 1.04 2.08 D" "k1 2.10 3.55 R" "k2 3.57 4.05 D" "k3 4.05 5.70 D" "k4 5.71 6.85 D" "k5 6.87 7.83 D" "k6 7.85 8.43 D" "k7 8.43 9.17 D" "k8 9.17 10.85 D" )
dt=",drawtext=fontfile=$F:textfile=h1.txt:fontsize=66:fontcolor=0xF8F6EF:box=1:boxcolor=0x1F1F1F@0.6:boxborderw=16:x=96:y=290:enable='lt(t,3.0)'"
for c in "${C[@]}"; do set -- $c; st=$DARK; [ "$4" = R ] && st=$RED
  dt="$dt,drawtext=fontfile=$F:textfile=$1.txt:fontsize=80:fontcolor=0xF8F6EF:$st:x=459-tw/2:y=1054:enable='between(t,$2,$3)'"
done
END=10.9
dt="$dt,drawbox=x=0:y=0:w=iw:h=ih:color=0x0E0E0E@0.62:t=fill:enable='gte(t,$END)'"
dt="$dt,drawtext=fontfile=$F:textfile=ce1.txt:fontsize=72:fontcolor=0xF8F6EF:x=96:y=640:enable='gte(t,$END)'"
dt="$dt,drawtext=fontfile=$F:textfile=ce2.txt:fontsize=72:fontcolor=0xF8F6EF:x=96:y=740:enable='gte(t,$END)'"
dt="$dt,drawtext=fontfile=$F:textfile=ce3.txt:fontsize=72:fontcolor=0xF8F6EF:$RED:x=96:y=850:enable='gte(t,$END)'"
ffmpeg -y -v error -i clip.mp4 -loop 1 -i wm2.png -i n_1.8.wav -filter_complex "
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,tpad=stop_mode=clone:stop_duration=3,trim=0:13.6,setpts=PTS-STARTPTS${dt}[base];
[1:v]scale=-1:84,format=rgba[w];
[base][w]overlay=x=96:y=1040:shortest=0:enable='gte(t,$END)'[v]" \
 -map "[v]" -map 2:a -t 13.6 -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -ar 48000 -movflags +faststart ss-2026-10-17-reel-v3.mp4
# cover: the 0.3 s frame with the hook in three lines at 92 px (cv1 "Kjo javë e vështirë", cv2 "është për tani,", cv3 "jo përgjithmonë.")
ffmpeg -y -v error -ss 0.3 -i clip.mp4 -frames:v 1 -vf "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,drawtext=fontfile=$F:textfile=cv1.txt:fontsize=92:fontcolor=0xF8F6EF:box=1:boxcolor=0x1F1F1F@0.6:boxborderw=20:x=80:y=330,drawtext=fontfile=$F:textfile=cv2.txt:fontsize=92:fontcolor=0xF8F6EF:box=1:boxcolor=0x1F1F1F@0.6:boxborderw=20:x=80:y=460,drawtext=fontfile=$F:textfile=cv3.txt:fontsize=92:fontcolor=0xF8F6EF:box=1:boxcolor=0xB31217@1:boxborderw=20:x=80:y=590" -q:v 2 ss-2026-10-17-reel-v3-cover.jpg
