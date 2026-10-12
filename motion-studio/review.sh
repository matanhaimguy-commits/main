#!/usr/bin/env bash
# ./review.sh [video] [strip_time] — frame sheets for the critique loop (Step 9)
set -euo pipefail
V=${1:-out/final.mp4}; T=${2:-4.1}
mkdir -p out
# Contact sheet: 2 frames per second, 6 across, as many rows as the video needs
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V")
ROWS=$(python3 -c "import math; print(math.ceil(float('$DUR') * 2 / 6))")
ffmpeg -loglevel error -y -i "$V" -vf "fps=2,scale=270:-1,tile=6x$ROWS" -frames:v 1 out/contact.png
# Strip: 12 frames around a fast moment, to catch glitches
ffmpeg -loglevel error -y -ss "$T" -i "$V" -vf "scale=320:-1,tile=12x1" -frames:v 1 out/strip.png
# Phone test: how it reads at 360px wide
ffmpeg -loglevel error -y -i "$V" -vf "fps=1,scale=360:-1,tile=5x3" -frames:v 1 out/phone.png
# Loop check: play it twice and watch the seam
ffmpeg -loglevel error -y -stream_loop 1 -i "$V" -c copy out/loop_check.mp4
echo "wrote out/contact.png out/strip.png out/phone.png out/loop_check.mp4"
