# Mix measurements for the review (v2): hit levels by kind, presence and band shares, the silence floor.
# python3 audio/measure.py [file.wav|mp4] [--events audio/events.json]   (default audio/mix.wav)
import json, os, subprocess, sys
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt
HERE = os.path.dirname(os.path.abspath(__file__))
args = [a for a in sys.argv[1:] if not a.startswith('--')]
src = args[0] if args else os.path.join(HERE, 'mix.wav')
EVP = sys.argv[sys.argv.index('--events') + 1] if '--events' in sys.argv else os.path.join(HERE, 'events.json')
if src.endswith('.wav'):
    x, SR = sf.read(src, dtype='float32', always_2d=True)
else:
    SR = 48000
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-f', 'f32le', '-ac', '2', '-ar', str(SR), '-'], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).reshape(-1, 2)
m = x.mean(1)
ev = json.load(open(EVP))
db = lambda v: 20 * np.log10(max(v, 1e-9))
lev, rl = {}, {}
mh = sosfilt(butter(2, 400, 'high', fs=SR, output='sos'), m)      # the hit's own band (no bass, cajon or pad body)
for e in ev['events']:
    if e['kind'] in ('peg', 'station', 'hop'):
        i = int(e['t'] * SR); w = m[max(0, i - int(0.005 * SR)): i + int(0.06 * SR)]
        lev.setdefault(e['kind'], []).append(db(np.abs(w).max()))
        r = mh[i: i + int(0.15 * SR)]; rl.setdefault(e['kind'], []).append(db(np.sqrt(np.mean(r ** 2))))
for k, v in lev.items():
    print(f'{k:8s} n={len(v):2d}  onset peak median {np.median(v):6.1f} dBFS (max {max(v):.1f});  150 ms RMS above 400 Hz median {np.median(rl[k]):6.1f} dBFS')
if 'station' in lev and 'peg' in lev:
    print(f'station over peg: {np.median(lev["station"]) - np.median(lev["peg"]):+.1f} dB onset peak, {np.median(rl["station"]) - np.median(rl["peg"]):+.1f} dB 150 ms RMS')
P = np.abs(np.fft.rfft(m)) ** 2; f = np.fft.rfftfreq(len(m), 1 / SR); tot = P.sum()
for lo, hi in ((60, 120), (120, 300), (300, 2500), (2500, 6000), (6000, 16000)):
    print(f'band {lo:5d}-{hi:5d} Hz: {100 * P[(f >= lo) & (f < hi)].sum() / tot:5.1f} % of the energy')
cu = ev['cues']
s0, s1 = int((cu['cut'] + 1.1) * SR), int((cu['light'] - 0.1) * SR)
seg = m[s0:s1]
print(f'silence {cu["cut"] + 1.1:.2f}-{cu["light"] - 0.1:.2f} s: rms {db(np.sqrt(np.mean(seg ** 2))):.1f} dBFS, digital zero samples {np.mean(seg == 0) * 100:.1f} %')
TMP = os.path.join(HERE, '..', 'out', '_hp150.wav')
hp = sosfilt(butter(4, 150, 'high', fs=SR, output='sos'), x, axis=0).astype(np.float32)
sf.write(TMP, hp, SR)
err = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', TMP, '-af', 'ebur128', '-f', 'null', '-'], capture_output=True, text=True).stderr
import re
print('through a 150 Hz high-pass (phone speaker):', re.findall(r'I:\s+(-?[\d.]+) LUFS', err)[-1], 'LUFS')
