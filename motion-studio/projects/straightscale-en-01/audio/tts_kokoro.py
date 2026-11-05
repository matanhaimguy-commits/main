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
    ("Your March: three clients. Your April: zero. Same LinkedIn.", 0.45),
    ("Fifty-nine owners in our research describe this exact cycle.", 0.35),
    ("The usual advice? Post more. Prospect more.", 0.30),
    ("But your channel still works. The replies still come.", 0.30, 0.95),  # 0.95: Whisper heard "reply" at 1.0
    ("The months go missing after the reply.", 0.55),
    ("Here's the three-step check.", 0.35),
    ("One. Write down replies and new clients, for each of the last six months.", 0.40),
    ("Two. Circle the months where replies held, but clients dropped. That gap is your leak.", 0.40),
    ("Three. Today, answer every open reply with two real call times. Not, let me know.", 0.50),
    ("Comment the word path, and we'll send you five ready-to-send messages for that step.", 0.40),
    ("Fix the step, not the channel.", 0.80),
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
