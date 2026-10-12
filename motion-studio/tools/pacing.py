#!/usr/bin/env python3
"""Pacing check for a rendered film or a reference clip (our own tool).

    python3 tools/pacing.py out/final.mp4 [more.mp4 ...] [--json]

Decodes small greyscale frames, measures frame-to-frame change, and reports:
  - stillness: share of frames that are dead still / quiet, and the longest quiet run
  - dead stretches: quiet runs longer than 4 s (a reel that sits still that long loses people)
  - transitions: hard changes grouped into events (a fast wipe is one event, not five cuts)
  - beat rhythm: intervals between energy peaks; equal intervals read as a slideshow
  - an energy map, one row per 4 s, to compare a render against a reference

Run it on a reference clip to get target numbers, then on our render to compare.
Thresholds follow knowledge/onetake-principles.md (gates 3 and 5), adapted for 9:16 reels.
"""
import json, subprocess, sys
import numpy as np

FPS, W = 12, 320            # analysis rate and width
NOISE = 10                  # per-pixel change (0-255) below this is grain or encoding noise, not motion
STILL, QUIET = 0.0005, 0.01 # share of the picture changing: below STILL nothing moves, below QUIET only a detail moves
HARD = 0.4                  # share of the picture changing at once: a cut, wipe or whip
PEAK = 0.05                 # an energy peak (a beat landing)
LEVELS = [0.0005, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4]  # map glyph thresholds
GLYPHS = " .:-=+*#%@"


def frames(path):
    info = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                      "stream=width,height", "-of", "json", path],
                                     capture_output=True, text=True, check=True).stdout)["streams"][0]
    h = int(round(info["height"] * W / info["width"] / 2) * 2)
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={FPS},scale={W}:{h}",
                          "-f", "rawvideo", "-pix_fmt", "gray", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.uint8).reshape(-1, h, W).astype(np.float32)


def runs(mask):
    """(start_index, length) of every run of True."""
    out, start = [], None
    for i, m in enumerate(list(mask) + [False]):
        if m and start is None:
            start = i
        elif not m and start is not None:
            out.append((start, i - start))
            start = None
    return out


def group(idx, gap):
    """Group sorted frame indices closer than `gap` frames; return each group's (first, peak-ish middle)."""
    groups = []
    for i in idx:
        if groups and i - groups[-1][-1] <= gap:
            groups[-1].append(i)
        else:
            groups.append([i])
    return groups


def analyse(path):
    f = frames(path)
    # d = share of the picture that changed since the previous frame
    d = np.concatenate([[0.0], (np.abs(np.diff(f, axis=0)) > NOISE).mean(axis=(1, 2))])
    dur = len(d) / FPS
    quiet_runs = runs(d < QUIET)
    longest_quiet = max((n for _, n in quiet_runs), default=0) / FPS
    dead = [(round(s / FPS, 2), round(n / FPS, 2)) for s, n in runs(d < STILL) if n / FPS > 3.0]

    transitions = [round(float(g[0]) / FPS, 2) for g in group(np.where(d > HARD)[0], int(0.5 * FPS))]
    # energy peaks: local maxima above PEAK, at least 0.4 s apart
    peaks = [i for i in range(1, len(d) - 1) if d[i] > PEAK and d[i] >= d[i - 1] and d[i] >= d[i + 1]]
    beats = [g[int(np.argmax([d[i] for i in g]))] for g in group(peaks, int(0.4 * FPS))]
    intervals = np.diff([0] + beats + [len(d)]) / FPS
    intervals = intervals[intervals > 0.25]
    cv = float(intervals.std() / intervals.mean()) if len(intervals) > 1 else 0.0
    spread = float(intervals.max() / intervals.min()) if len(intervals) > 1 else 1.0

    rows = [d[k:k + 4 * FPS] for k in range(0, len(d), 4 * FPS)]
    emap = "\n".join(f"{k * 4:5.1f}s |" + "".join(GLYPHS[int(np.searchsorted(LEVELS, v))] for v in r) + "|"
                     for k, r in enumerate(rows))
    r = {
        "clip": path, "dur_s": round(dur, 2),
        "still_share": round(float((d < STILL).mean()), 3), "quiet_share": round(float((d < QUIET).mean()), 3),
        "longest_quiet_s": round(longest_quiet, 2), "dead_stretches": dead,
        "transitions": transitions, "beats": len(beats),
        "beat_interval_cv": round(cv, 2), "beat_interval_spread": round(spread, 1),
        "map": emap,
    }
    checks = []
    def check(level, ok, msg):
        checks.append(("PASS" if ok else level, msg))
    check("WARN", r["still_share"] >= 0.25 or r["longest_quiet_s"] >= 1.0,
          f"rests: {r['still_share']:.0%} still, longest quiet run {r['longest_quiet_s']} s (want >= 25% or a >= 1 s rest)")
    check("WARN", r["longest_quiet_s"] <= 5.0, f"longest quiet run {r['longest_quiet_s']} s (only a detail moving; over 5 s risks the scroll)")
    check("FAIL", not dead, f"frozen stretches over 3 s (nothing moves at all): {dead or 'none'}")
    check("WARN", cv >= 0.25, f"beat rhythm variety: CV {cv:.2f} (want >= 0.25; equal spacing reads as a slideshow)")
    check("WARN", spread >= 4 or len(intervals) < 3, f"beat lengths spread {spread:.1f}x (want >= 4x between shortest and longest)")
    r["checks"] = checks
    return r


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit(__doc__)
    results = [analyse(p) for p in args]
    if "--json" in sys.argv:
        print(json.dumps(results, indent=1))
        sys.exit(0)
    fail = False
    for r in results:
        print(f"== {r['clip']}  {r['dur_s']} s  still {r['still_share']:.0%}  quiet {r['quiet_share']:.0%}  "
              f"beats {r['beats']}  transitions {len(r['transitions'])} at {r['transitions'][:10]}")
        for level, msg in r["checks"]:
            print(f"  {level:4}  {msg}")
            fail |= level == "FAIL"
        print(r["map"])
    sys.exit(1 if fail else 0)
