#!/usr/bin/env python3
"""Build a deliberately messy test clip for the edit engine: filler words, long pauses and one restarted
sentence, with exact word timings. Needs `flite` (apt-get install flite) and ffmpeg.

  python3 tools/make_test_clip.py OUT_DIR   -> talk.mp4 (1920x1080 test pattern), speech.wav, words.json, bed.wav
Expected plan: 2 fillers and 1 retake removed, about 24.4 s -> 16.9 s.
"""
import json, os, struct, subprocess, sys, wave

out = sys.argv[1] if len(sys.argv) > 1 else "edit-test"
os.makedirs(out, exist_ok=True)
os.chdir(out)
SCRIPT = [("Most businesses lose clients after the first sale.", 0.9), ("um", 0.4), ("So here is the fix.", 1.0),
          ("You need to", 0.7), ("You need to follow up within one day.", 1.1), ("uh", 0.5),
          ("Clients who hear back fast buy again.", 0.8), ("Comment ANALYSIS and I will send you the plan.", 0.6)]
RATE = 16000
pcm, words, t = b"\0\0" * int(RATE * 0.4), [], 0.4
for phrase, pause in SCRIPT:
    for w in phrase.split():
        subprocess.run(["flite", "-voice", "slt", "-t", w.strip(".,").lower(), "-o", "w.wav"], check=True)
        r = wave.open("w.wav"); fr = r.readframes(r.getnframes()); r.close()
        smp = struct.unpack("<%dh" % (len(fr) // 2), fr)
        idx = [i for i, v in enumerate(smp) if abs(v) > 400]
        fr = fr[idx[0] * 2:(idx[-1] + 1) * 2]
        d = len(fr) / 2 / RATE
        words.append({"text": w, "start": round(t, 3), "end": round(t + d, 3)})
        pcm += fr + b"\0\0" * int(RATE * 0.07); t += d + 0.07
    pcm += b"\0\0" * int(RATE * pause); t += pause
os.remove("w.wav")
o = wave.open("speech.wav", "wb"); o.setnchannels(1); o.setsampwidth(2); o.setframerate(RATE); o.writeframes(pcm); o.close()
json.dump(words, open("words.json", "w"), indent=0)
dur = len(pcm) / 2 / RATE
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"testsrc2=s=1920x1080:r=30:d={dur}", "-i", "speech.wav",
                "-vf", "drawtext=text='SRC %{pts\\:hms}':x=(w-tw)/2:y=h*0.45:fontsize=90:fontcolor=white:box=1:boxcolor=black@0.6",
                "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-c:a", "aac", "-shortest", "talk.mp4"], check=True)
subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", "sine=f=220:d=20", "-f", "lavfi", "-i", "sine=f=277.2:d=20",
                "-f", "lavfi", "-i", "sine=f=329.6:d=20", "-filter_complex", "amix=inputs=3,volume=0.5,tremolo=f=2:d=0.3",
                "bed.wav"], check=True)
print(f"{out}: talk.mp4 {dur:.2f} s, {len(words)} words")
