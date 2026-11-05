"""Voiceover with Kokoro (offline). One take per line, joined with planned silences.
Writes audio/vo.wav and audio/lines.json ({source, duration, lines:[{i,text,s,e}]})."""
import json, sys, os
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro

HERE = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = sys.argv[1]
VOICE = sys.argv[2] if len(sys.argv) > 2 else "af_heart"
SPEED = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0

# (text, pause after in seconds)
LINES = [
    ("Two years of posting content, running ads, and praying someone books a call.", 0.55),
    ("We didn't write that. A business owner did, in a review.", 0.40),
    ("It stopped you because it sounds like you. Your buyers stop for their own words.", 0.40),
    ("Here are three places to find them.", 0.35),
    ("One. Your competitors' worst reviews: what people paid for and never got.", 0.45),
    ("Two. Reddit threads in your niche: the problem, before they know you exist.", 0.45),
    ("Three. Newsletters where owners write about their worst month.", 0.45),
    ("Copy the sentence. Don't polish it. Once it's polished, it sounds like an ad.", 0.45),
    ("We collected five hundred sixty-seven of these before we posted a single video.", 0.40),
    ("Comment words for the exact searches we use.", 0.80),
]

k = Kokoro(os.path.join(MODEL_DIR, "kokoro-v1.0.onnx"), os.path.join(MODEL_DIR, "voices-v1.0.bin"))
out, meta, t, sr0 = [], [], 0.0, None
lead = 0.12
for i, item in enumerate(LINES):
    text, pause = item[0], item[1]
    speed = item[2] if len(item) > 2 else SPEED
    samples, sr = k.create(text, voice=VOICE, speed=speed, lang="en-us")
    sr0 = sr0 or sr
    samples = np.asarray(samples, dtype=np.float32)
    # trim the model's own leading and trailing silence so our pauses are the only pauses
    env = np.abs(samples) > 0.01
    idx = np.where(env)[0]
    a, b = (max(idx[0] - int(0.02 * sr), 0), min(idx[-1] + int(0.06 * sr), len(samples))) if len(idx) else (0, len(samples))
    seg = samples[a:b].copy()
    nf = int(0.03 * sr); seg[-nf:] *= np.linspace(1, 0, nf)  # 30 ms fade on every line ending
    sf.write(os.path.join(HERE, "lines", f"line{i+1:02d}.wav"), seg, sr)
    if i == 0:
        out.append(np.zeros(int(lead * sr), dtype=np.float32)); t = lead
    s = t; out.append(seg); t += len(seg) / sr; e = t
    meta.append({"i": i + 1, "text": text, "s": round(s, 3), "e": round(e, 3)})
    out.append(np.zeros(int(pause * sr), dtype=np.float32)); t += pause
audio = np.concatenate(out)
sf.write(os.path.join(HERE, "vo.wav"), audio, sr0)
json.dump({"source": f"kokoro-onnx v1.0, voice {VOICE}, speed {SPEED}", "duration": round(len(audio) / sr0, 3), "lines": meta},
          open(os.path.join(HERE, "lines.json"), "w"), indent=1)
print(json.dumps({"duration": round(len(audio) / sr0, 2), "lines": [(m["i"], m["s"], m["e"]) for m in meta]}))
