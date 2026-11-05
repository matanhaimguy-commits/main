#!/usr/bin/env bash
# tools/render_draft.sh FPS SUB [page] [out] : render the film in 3 parallel segments and join them
set -euo pipefail
cd "$(dirname "$0")/.."
FPS=${1:-30}; SUB=${2:-2}; PAGE=${3:-index.html}; OUT=${4:-out/draft.mp4}; H=1920
case "$PAGE" in *fmt=45*) H=1350;; esac
DUR=25; A=8.5; B=17
node ../../render.mjs --fps $FPS --sub $SUB --from 0 --dur $A --h $H --page "$PAGE" --out out/seg/a.mp4 > out/seg/a.log 2>&1 &
node ../../render.mjs --fps $FPS --sub $SUB --from $A --dur $(python3 -c "print($B-$A)") --h $H --page "$PAGE" --out out/seg/b.mp4 > out/seg/b.log 2>&1 &
node ../../render.mjs --fps $FPS --sub $SUB --from $B --dur $(python3 -c "print($DUR-$B)") --h $H --page "$PAGE" --out out/seg/c.mp4 > out/seg/c.log 2>&1 &
wait
printf "file 'a.mp4'\nfile 'b.mp4'\nfile 'c.mp4'\n" > out/seg/list.txt
ffmpeg -loglevel error -y -f concat -safe 0 -i out/seg/list.txt -c copy "$OUT"
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames,width,height,r_frame_rate -of csv=p=0 "$OUT"
