"""Transcript check of the voiceover against the script with Whisper base.en (sherpa-onnx, offline).
Usage: python asr_check.py <whisper_model_dir> [lines_dir]"""
import json, os, re, sys, difflib
import numpy as np, soundfile as sf, sherpa_onnx
HERE = os.path.dirname(os.path.abspath(__file__)); M = sys.argv[1]
LD = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "lines")
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=f"{M}/base.en-encoder.onnx", decoder=f"{M}/base.en-decoder.onnx",
                                                tokens=f"{M}/base.en-tokens.txt", language="en", task="transcribe")
meta = json.load(open(os.path.join(HERE, "lines.json")))
norm = lambda s: re.findall(r"[a-z0-9']+", s.lower().replace("-", " ").replace("linkedin", "linkedin"))
tot = []
for ln in meta["lines"]:
    x, sr = sf.read(os.path.join(LD, f"line{ln['i']:02d}.wav"), dtype="float32")
    st = rec.create_stream(); st.accept_waveform(sr, x); rec.decode_stream(st); hyp = st.result.text.strip()
    r = difflib.SequenceMatcher(None, norm(ln["text"]), norm(hyp)).ratio(); tot.append(r)
    print(f"{ln['i']:2d} {r:.2f} | {hyp}")
print("mean word match", round(sum(tot) / len(tot), 3))
