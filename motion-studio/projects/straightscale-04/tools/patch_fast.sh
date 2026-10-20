#!/usr/bin/env bash
# tools/patch_fast.sh IN OUT [page] [windows]: re-render fast camera moves with 16 subframes and splice them in
# frame-exactly (one re-encode at CRF 16). 4 subframes leave stepped copies of the labels in fast moves (v1 review
# round 3). Default v2 windows: the rise out of the hole and the whip up (5.95-8.6 s), the pull-back to the map
# (16.9-18.0 s) and the flight home (19.95-21.05 s). windows = "a0:a1 b0:b1 ..." in seconds, ascending.
set -euo pipefail
cd "$(dirname "$0")/.."
IN=$1; OUT=$2; PAGE=${3:-index.html}; WIN=${4:-"5.95:8.6 16.9:18.0 19.95:21.05"}; H=1920; FPS=60
case "$PAGE" in *fmt=45*) H=1350;; esac
mkdir -p out/patch
f() { python3 -c "print(round($1 * $FPS))"; }
k=0; INPUTS="-i $IN"; FILTER=""; LABELS=""; prev=0; n=${#WIN}
WS=($WIN); NW=${#WS[@]}
FILTER="[0:v]split=$((NW + 1))$(for i in $(seq 0 $NW); do printf '[s%d]' $i; done);"
for w in "${WS[@]}"; do
  a=${w%:*}; b=${w#*:}; fa=$(f $a); fb=$(f $b); k=$((k + 1))
  node ../../render.mjs --fps $FPS --sub ${SUB:-16} --from $a --dur $(python3 -c "print(round($b - $a, 4))") --h $H --page "$PAGE" --out out/patch/w${k}_$H.mp4 > out/patch/w${k}_$H.log 2>&1 &
  INPUTS="$INPUTS -i out/patch/w${k}_$H.mp4"
  FILTER="$FILTER[s$((k - 1))]trim=start_frame=$prev:end_frame=$fa,setpts=PTS-STARTPTS[k$k];[$k:v]trim=start_frame=0:end_frame=$((fb - fa)),setpts=PTS-STARTPTS[p$k];"
  LABELS="$LABELS[k$k][p$k]"; prev=$fb
done
wait
FILTER="$FILTER[s$NW]trim=start_frame=$prev,setpts=PTS-STARTPTS[tail];${LABELS}[tail]concat=n=$((2 * NW + 1)):v=1:a=0,format=yuv420p[v]"
ffmpeg -loglevel error -y $INPUTS -filter_complex "$FILTER" -map "[v]" -r $FPS -c:v libx264 -crf 16 -preset medium "$OUT"
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames,width,height,r_frame_rate -of csv=p=0 "$OUT"
