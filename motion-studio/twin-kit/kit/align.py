"""A $0 fallback aligner: word timings from a known script and the voice's pauses.

Used when no word-timed transcript exists (the speech-to-text model we have returns text only, no word times). It
finds the voiced stretches by energy, then lays the script's words over them weighted by length. When the script has
as many phrases as the audio has voiced stretches, each phrase gets its own stretch. Accurate to about a syllable:
good for cutting on words and for captions, not for lip-level work. The output says it is estimated.
"""
import re
import subprocess

import numpy as np

SR = 16000
HOP = 0.01          # 10 ms analysis frames
FLOOR_DB = -32      # below the loudest frame by this much = silence
MIN_GAP = 0.16      # pauses shorter than this are inside a phrase
MIN_SPEECH = 0.08


def decode(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


def voiced(signal, sr=SR):
    """[(start, end)] of voiced stretches, pauses under MIN_GAP merged."""
    hop = int(sr * HOP)
    n = len(signal) // hop
    if n == 0:
        return []
    frames = signal[: n * hop].reshape(n, hop)
    rms = 20 * np.log10(np.sqrt(np.mean(frames ** 2, axis=1)) + 1e-9)
    on = rms > rms.max() + FLOOR_DB
    segs, start = [], None
    for i, v in enumerate(on):
        if v and start is None:
            start = i
        if not v and start is not None:
            segs.append([start * HOP, i * HOP])
            start = None
    if start is not None:
        segs.append([start * HOP, n * HOP])
    merged = []
    for s in segs:
        if merged and s[0] - merged[-1][1] < MIN_GAP:
            merged[-1][1] = s[1]
        else:
            merged.append(s)
    return [(round(a, 3), round(b, 3)) for a, b in merged if b - a >= MIN_SPEECH]


def script_phrases(text):
    """Words grouped into phrases at , . ! ? ; :"""
    out, cur = [], []
    for w in text.split():
        cur.append(w)
        if re.search(r"[,.!?;:]$", w):
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


def spread(words, start, end):
    """Words laid over [start, end] in proportion to their length."""
    weights = np.array([len(re.sub(r"\W", "", w)) + 1.5 for w in words], float)
    edges = start + (end - start) * np.concatenate([[0], np.cumsum(weights)]) / weights.sum()
    return [{"w": w, "s": round(float(edges[i]), 3), "e": round(float(edges[i + 1]), 3)} for i, w in enumerate(words)]


def align(text, segments):
    groups = script_phrases(text)
    if not segments:
        raise ValueError("no voiced audio found")
    if len(groups) == len(segments):
        out = []
        for g, (a, b) in zip(groups, segments):
            out += spread(g, a, b)
        return out
    # otherwise lay the phrases over the voiced time as one stream, give each phrase to the stretch holding its
    # middle (a phrase never straddles a pause), then spread each stretch's phrases over it
    total = sum(b - a for a, b in segments)
    stream = spread([" ".join(g) for g in groups], 0.0, total)
    owner = [segment_at(segments, (p["s"] + p["e"]) / 2) for p in stream]
    out = []
    for k, (a, b) in enumerate(segments):
        mine = [w for g, o in zip(groups, owner) if o == k for w in g]
        if mine:
            out += spread(mine, a, b)
    return out


def segment_at(segments, t):
    """Index of the stretch that stream time t (voiced time only, pauses removed) falls in."""
    for k, (a, b) in enumerate(segments):
        if t <= (b - a) + 1e-9:
            return k
        t -= b - a
    return len(segments) - 1


def run(audio, text):
    sig = decode(audio)
    segs = voiced(sig)
    return {"source": f"estimated by kit/align.py from {audio} and its script (no word-timed transcript)",
            "duration": round(len(sig) / SR, 3), "segments": segs, "words": align(text, segs)}
