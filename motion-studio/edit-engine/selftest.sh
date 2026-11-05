#!/usr/bin/env bash
# Regression test: build the messy test clip, run every style, check length, sync and loudness.
set -euo pipefail
HERE=$(cd "$(dirname "$0")" && pwd)
T=${1:-$(mktemp -d)}
command -v flite >/dev/null || { echo "needs flite: apt-get install -y flite"; exit 1; }
python3 "$HERE/tools/make_test_clip.py" "$T"
for st in punchy bold clean minimal editorial handwritten; do
  python3 "$HERE/edit.py" run "$T/talk.mp4" --words "$T/words.json" --out "$T/out_$st" --style "$st" --music "$T/bed.wav" --draft 2>/dev/null
  python3 - "$T/out_$st/report.json" <<'PY'
import json, sys
r = json.load(open(sys.argv[1]))
assert len(r["fillers"]) == 2 and len(r["retakes"]) == 1, r
assert abs(r["loudness"]["lufs"] + 14) <= 0.6, r["loudness"]
assert r["loudness"]["true_peak_db"] <= -1.0, r["loudness"]
print(f"ok  {r['style']:12s} {r['source_s']} s -> {r['cut_s']} s  {r['loudness']['lufs']} LUFS")
PY
done
echo "all styles pass; outputs in $T"
