#!/usr/bin/env python3
"""Per-event sound report for this film (we cannot listen, so we measure).
  python3 tools/audio_report.py [audio/mix_raw.wav] [--png out/spectrogram.png]
Prints, for every cue in audio/events.json: effects-stem and music-stem RMS (dBFS) in the 150 ms after the cue and
the gap between them; a 0.25 s loudness strip of the whole mix; and silence runs. Writes a spectrogram with cue lines."""
import json, sys, os
import numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
av = sys.argv[1:]
if '--png' in av: i = av.index('--png'); av = av[:i] + av[i + 2:]
args = av
mixp = args[0] if args else os.path.join(HERE, 'audio/mix_raw.wav')
png = sys.argv[sys.argv.index('--png') + 1] if '--png' in sys.argv else None
ev = json.load(open(os.path.join(HERE, 'audio/events.json')))
rd = lambda p: sf.read(p, always_2d=True)[0].mean(axis=1)
mix = rd(mixp); SR = 48000
mu, fx = rd(os.path.join(HERE, 'audio/music.wav')), rd(os.path.join(HERE, 'audio/sfx.wav'))
db = lambda x: 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-9)
print('cue                  t      fx dB   music dB   fx-music')
seen = set()
for e in ev['events']:
    if e['kind'] == 'letter' and e.get('i', 0) % 3: continue
    a, b = int(e['t'] * SR), int((e['t'] + 0.15) * SR)
    f, m = db(fx[a:b]), db(mu[a:b])
    print(f"{e['kind']:<14} {e['t']:7.3f}  {f:7.1f}  {m:8.1f}  {f - m:8.1f}")
w = int(0.25 * SR)
strip = [db(mix[i:i + w]) for i in range(0, len(mix) - w + 1, w)]
print('mix RMS per 0.25 s:', ' '.join(f'{v:.0f}' for v in strip))
sil = [i * 0.25 for i, v in enumerate(strip) if v < -50]
print('windows under -50 dBFS at', sil)
if png:
    import subprocess
    from PIL import Image, ImageDraw
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', mixp, '-lavfi', 'showspectrumpic=s=1600x500:legend=0:mode=combined:scale=log:fscale=lin:stop=12000', png], check=True)
    im = Image.open(png).convert('RGB'); d = ImageDraw.Draw(im); Wd = im.width
    for e in ev['events']:
        if e['kind'] == 'letter': continue
        x = e['t'] / ev['duration'] * Wd
        d.line([(x, 0), (x, im.height)], fill=(0, 220, 255), width=1); d.text((x + 2, 2), e['kind'], fill=(0, 220, 255))
    im.save(png)
    print('spectrogram (0-12 kHz, cue lines in cyan):', png)
