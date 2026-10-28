"""Line times from the aligned words, and the slice plan: consecutive whole lines grouped into 5 to 15 s slices
(STANDARDS: one per lip-sync sequence or clip), each cut snapped to the nearest beat inside the gap between lines."""
from __future__ import annotations

SLICE_MIN, SLICE_MAX = 5.0, 15.0


def line_times(lines: list[dict], words: list[dict]) -> list[dict]:
    """Adds start, end and words (with times) to each line; words are consumed in order."""
    out, i = [], 0
    for line in lines:
        n = len(line["tokens"])
        ws = words[i:i + n]
        i += n
        out.append({"id": line["id"], "section": line["section"], "text": line["text"],
                    "start": ws[0]["start"], "end": ws[-1]["end"], "words": ws})
    return out


def snap(lo: float, hi: float, beats: list[float]) -> float:
    """A cut point in the gap [lo, hi]: the beat in it closest to the gap's middle, else the middle."""
    mid = (lo + hi) / 2
    inside = [b for b in beats if lo <= b <= hi]
    return round(min(inside, key=lambda b: abs(b - mid)) if inside else mid, 2)


def slices(timed: list[dict], beats: list[float], duration: float, prefix: str) -> list[dict]:
    """Greedy: close a slice at 8 s or more, or before the next line would take it past SLICE_MAX (never under
    SLICE_MIN); a short last slice joins the one before it when that stays within SLICE_MAX."""
    cuts = [0.0] + [snap(a["end"], b["start"], beats) for a, b in zip(timed, timed[1:])] + [round(duration, 2)]
    out, first = [], 0
    for k in range(len(timed)):
        start, end = cuts[first], cuts[k + 1]
        nxt = cuts[k + 2] if k + 2 < len(cuts) else None
        last = k == len(timed) - 1
        if last or (end - start >= SLICE_MIN and (nxt - start > SLICE_MAX or end - start >= 8.0)):
            out.append({"id": f"{prefix}-S{len(out) + 1:02d}", "start": start, "end": end,
                        "length": round(end - start, 2), "lines": [t["id"] for t in timed[first:k + 1]]})
            first = k + 1
    if len(out) > 1 and out[-1]["length"] < SLICE_MIN and out[-1]["end"] - out[-2]["start"] <= SLICE_MAX:
        tail = out.pop()
        out[-1].update(end=tail["end"], length=round(tail["end"] - out[-1]["start"], 2),
                       lines=out[-1]["lines"] + tail["lines"])
    return out
