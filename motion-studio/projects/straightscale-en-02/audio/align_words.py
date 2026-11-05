"""Word timings for the voiceover: pocketsphinx forced alignment per line (offline).
Reads audio/lines.json + audio/lines/lineNN.wav, writes audio/words.json ({source, duration, words:[{w,s,e,line}]}).
Words missing from the CMU dictionary are spelled as dictionary words for alignment and mapped back."""
import json, os, re
import numpy as np, soundfile as sf
from pocketsphinx import Decoder

HERE = os.path.dirname(os.path.abspath(__file__))
meta = json.load(open(os.path.join(HERE, "lines.json")))
SPELL = {"linkedin": ["linked", "in"], "fifty-nine": ["fifty", "nine"], "three-step": ["three", "step"], "sixty-seven": ["sixty", "seven"],
         "ready-to-send": ["ready", "to", "send"], "we'll": ["we'll"], "here's": ["here's"], "it's": ["it's"]}

def resample16k(x, sr):
    if sr == 16000: return x
    n = int(round(len(x) * 16000 / sr))
    return np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x).astype(np.float32)

words_out, fails = [], []
for ln in meta["lines"]:
    x, sr = sf.read(os.path.join(HERE, "lines", f"line{ln['i']:02d}.wav"), dtype="float32")
    x = resample16k(x, sr)
    pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16).tobytes()
    shown = re.findall(r"[A-Za-z0-9'\-]+", ln["text"])
    groups, flat = [], []
    for w in shown:
        parts = SPELL.get(w.lower(), [w.lower().strip("-")])
        groups.append((w, len(parts))); flat += parts
    timed = None
    try:
        d = Decoder(samprate=16000, bestpath=False, loglevel="FATAL")
        d.set_align_text(" ".join(flat))
        d.start_utt(); d.process_raw(pcm, full_utt=True); d.end_utt()
        d.set_alignment()  # second pass: phone-level alignment gives word times
        d.start_utt(); d.process_raw(pcm, full_utt=True); d.end_utt()
        al = [(seg.name, seg.start / 100.0, (seg.start + seg.duration) / 100.0) for seg in d.get_alignment()]
        al = [a for a in al if a[0] not in ("<sil>", "<s>", "</s>", "[NOISE]") and not a[0].startswith("+")]
        if len(al) == len(flat): timed = al
    except Exception as e:
        fails.append((ln["i"], str(e)[:80]))
    if timed is None:  # proportional fallback by letters
        fails.append((ln["i"], "fallback"))
        dur = ln["e"] - ln["s"]; tot = sum(len(f) for f in flat); acc = 0.0; timed = []
        for f in flat:
            a = acc / tot * dur; acc += len(f); timed.append((f, a, acc / tot * dur))
    k = 0
    for w, n in groups:
        a, b = timed[k][1], timed[k + n - 1][2]; k += n
        words_out.append({"w": w, "s": round(ln["s"] + a, 3), "e": round(ln["s"] + b, 3), "line": ln["i"]})
json.dump({"source": meta["source"] + "; pocketsphinx forced alignment per line", "duration": meta["duration"], "words": words_out},
          open(os.path.join(HERE, "words.json"), "w"), indent=1)
print("words", len(words_out), "fails", fails)
for w in words_out[:14]: print(w)
