#!/usr/bin/env python3
"""Retime the film from real word timings: a data change only, no film code changes.

    python3 tools/retime.py audio/words.json [--offset 0.3]

words.json is {source, duration, words: [{w, s, e}]} (stage 5 of the motion-reel skill). The voice words are matched
to the script words in order (punctuation ignored); a script word the voice file lacks gets a time interpolated from
its neighbours. Every cue in film/timing.json is anchored to a line or a word, so the whole film follows the voice.
--offset shifts the voice (seconds of silence before it starts in the film).
"""
import argparse
import difflib
import json

from timing_lib import letters, load, save


def match(script_words, voice):
    """Index of the voice word for each script word (None when unmatched)."""
    a = [letters(w) for w in script_words]
    b = [letters(v["w"]) for v in voice]
    found = [None] * len(a)
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag in ("equal", "replace") and i2 - i1 == j2 - j1:
            for k in range(i2 - i1):
                found[i1 + k] = j1 + k
    return found


def fill(times):
    """Interpolate None entries in a list of (s, e) from the nearest known neighbours."""
    known = [i for i, t in enumerate(times) if t]
    for i, t in enumerate(times):
        if t:
            continue
        lo = max((k for k in known if k < i), default=None)
        hi = min((k for k in known if k > i), default=None)
        s = times[lo][1] if lo is not None else times[hi][0] - 0.3
        e = times[hi][0] if hi is not None else s + 0.3
        times[i] = (s, (s + e) / 2)
    return times


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("words")
    ap.add_argument("--offset", type=float, default=0.0)
    args = ap.parse_args()
    voice = json.load(open(args.words, encoding="utf-8"))
    data = load()
    flat = [(li, w) for li, line in enumerate(data["lines"]) for w in line["words"]]
    idx = match([w["w"] for _, w in flat], voice["words"])
    times = fill([(voice["words"][j]["s"] + args.offset, voice["words"][j]["e"] + args.offset) if j is not None
                  else None for j in idx])
    for (li, w), (s, e) in zip(flat, times):
        w["s"], w["e"] = round(s, 3), round(e, 3)
    for k, line in enumerate(data["lines"]):
        line["start"] = line["words"][0]["s"]
        nxt = data["lines"][k + 1]["words"][0]["s"] if k + 1 < len(data["lines"]) else line["words"][-1]["e"] + 0.3
        line["end"] = round(max(line["words"][-1]["e"] + 0.1, min(nxt, line["words"][-1]["e"] + 0.6)), 3)
    data["source"] = f"voice: {voice.get('source', args.words)} (offset {args.offset} s)"
    save(data)
    missing = sum(1 for j in idx if j is None)
    print(f"retimed {len(flat)} words from {args.words}; {missing} interpolated")


if __name__ == "__main__":
    main()
