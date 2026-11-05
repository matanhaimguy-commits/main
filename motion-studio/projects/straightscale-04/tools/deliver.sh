#!/usr/bin/env bash
# tools/deliver.sh vN : after ./finish.sh and the final renders (out/silent.mp4, out/silent_45.mp4), build deliver/vN/
set -euo pipefail
cd "$(dirname "$0")/.."
V=${1:-v1}; D=deliver/$V; mkdir -p "$D"
[ -e "$D/one-message-9x16.mp4" ] && { echo "$D already exists: never overwrite a version"; exit 1; }
ffmpeg -loglevel error -y -i out/silent.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -ar 48000 \
  -movflags +faststart -shortest "$D/one-message-9x16.mp4"
ffmpeg -loglevel error -y -i out/silent_45.mp4 -i audio/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -ar 48000 \
  -movflags +faststart -shortest "$D/one-message-4x5.mp4"
SZ=$(stat -c %s "$D/one-message-9x16.mp4")
if [ "$SZ" -gt 30000000 ]; then
  ffmpeg -loglevel error -y -i "$D/one-message-9x16.mp4" -c:v libx264 -crf 24 -preset slow -pix_fmt yuv420p -c:a aac -b:a 192k \
    -movflags +faststart "$D/one-message-9x16-view.mp4"
fi
# poster: the hook frame (headline in, ball launched; v2: no logo in the hook)
ffmpeg -loglevel error -y -ss 0.6 -i "$D/one-message-9x16.mp4" -frames:v 1 -q:v 2 "$D/poster.jpg"
# contact sheet: one frame per beat (treatment section 5), from the delivered master
T="0.6 1.65 3.62 5.2 7.6 8.8 11.0 12.6 14.6 18.8 22.2 24.5"
rm -rf out/cs && mkdir -p out/cs; i=0
for t in $T; do i=$((i+1)); ffmpeg -loglevel error -y -ss $t -i "$D/one-message-9x16.mp4" -frames:v 1 \
  -vf "scale=360:-1,drawtext=fontfile=assets/fonts/Montserrat/montserrat-latin-700-normal.woff2:text='${t}s':x=12:y=12:fontsize=22:fontcolor=white:box=1:boxcolor=0x1F1F1Fcc:boxborderw=6" \
  out/cs/$(printf %02d $i).png 2>/dev/null || ffmpeg -loglevel error -y -ss $t -i "$D/one-message-9x16.mp4" -frames:v 1 -vf scale=360:-1 out/cs/$(printf %02d $i).png; done
ffmpeg -loglevel error -y -i out/cs/%02d.png -vf "pad=iw+8:ih+8:4:4:white,tile=6x2" -frames:v 1 -q:v 3 "$D/contact-sheet.jpg"
node tools/readcheck.mjs --srt "$D/captions.srt" > /dev/null
cp CREDITS.md "$D/CREDITS.md"; cp CHANGELOG.md "$D/CHANGELOG.md"; [ -f post-caption.txt ] && cp post-caption.txt "$D/post-caption.txt"
ls -la "$D"
