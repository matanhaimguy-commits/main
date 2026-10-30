#!/usr/bin/env bash
# tools/strip.sh VIDEO FROM TO FPS OUT [cols] [width]: a strip of frames from FROM to TO at FPS, each stamped with its time
set -euo pipefail
V=$1; A=$2; B=$3; F=$4; O=$5; C=${6:-8}; WD=${7:-270}
D=$(mktemp -d -p "$(dirname "$O")"); i=0
for t in $(python3 -c "import numpy as n; print(' '.join(f'{x:.3f}' for x in n.arange($A, $B + 1e-6, 1 / $F)))"); do
  i=$((i+1)); ffmpeg -loglevel error -y -ss $t -i "$V" -frames:v 1 -vf "scale=$WD:-1,drawtext=fontfile=assets/fonts/Montserrat/montserrat-latin-700-normal.woff2:text='${t}':x=6:y=6:fontsize=18:fontcolor=white:box=1:boxcolor=0x1F1F1Fcc:boxborderw=4" "$D/$(printf %03d $i).png" 2>/dev/null \
    || ffmpeg -loglevel error -y -ss $t -i "$V" -frames:v 1 -vf "scale=$WD:-1" "$D/$(printf %03d $i).png"
done
R=$(( (i + C - 1) / C ))
ffmpeg -loglevel error -y -i "$D/%03d.png" -vf "pad=iw+4:ih+4:2:2:white,tile=${C}x${R}" -frames:v 1 "$O"
rm -rf "$D"; echo "$O ($i frames)"
