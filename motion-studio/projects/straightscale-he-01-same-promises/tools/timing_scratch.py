#!/usr/bin/env python3
"""Scratch timing (no voice yet): per-line seconds from docs/script.md, word starts spread by word length.

    python3 tools/timing_scratch.py          # rewrites "lines" and "source" in film/timing.json, keeps cues and tail

Model: inside each line, a word takes time in proportion to its letters + 1.6; a comma adds 0.22 s and a mid-line
"?" or "." adds 0.32 s of pause; the line leaves 0.12 s of air at its end. Real timings replace this with retime.py.
"""
from timing_lib import letters, load, save, script_lines

PAUSE = {",": 0.22, "?": 0.32, ".": 0.32}


def weight(word):
    """Spoken length proxy: letters + 1.6; a figure is said as a word ("8" = shmone), so it counts 3 letters a digit."""
    digits = sum(c.isdigit() for c in word)
    return (3 * digits + 1 if digits else len(letters(word))) + 1.6


def spread(text, start, end):
    words = text.split()
    pauses = [PAUSE.get(w[-1], 0) if i < len(words) - 1 else 0 for i, w in enumerate(words)]
    weights = [weight(w) for w in words]
    speak = (end - start - 0.12) - sum(pauses)
    unit = speak / sum(weights)
    out, t = [], start
    for w, wt, p in zip(words, weights, pauses):
        d = wt * unit
        out.append({"w": w, "s": round(t, 3), "e": round(t + d * 0.92, 3)})
        t += d + p
    return out


def main():
    data = load()
    data["source"] = "scratch: per-line seconds from docs/script.md section 2, words spread by length (no voice yet)"
    data["lines"] = [{"id": i, "text": text, "start": s, "end": e, "words": spread(text, s, e)}
                     for i, text, s, e in script_lines()]
    save(data)
    print(f"{len(data['lines'])} lines, {sum(len(l['words']) for l in data['lines'])} words -> film/timing.json")


if __name__ == "__main__":
    main()
