# Mix for film 04 (no voice): music and foley in one space, gentle EQ, peak guard. python3 audio/mix.py -> audio/mix_raw.wav
# Foley sits a little under the hits it doubles; the planned silence (4.0-6.5) stays digital zero except the far thump.
import os
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

HERE = os.path.dirname(os.path.abspath(__file__))
SR = 48000
mu, _ = sf.read(os.path.join(HERE, 'music.wav'), dtype='float32', always_2d=True)
fx, _ = sf.read(os.path.join(HERE, 'sfx.wav'), dtype='float32', always_2d=True)
N = max(len(mu), len(fx))
pad = lambda x: np.pad(x, ((0, N - len(x)), (0, 0)))
mu, fx = pad(mu), pad(fx)
hp = butter(2, 38, 'high', fs=SR, output='sos')
# a broad, gentle dip in the low mids (marimba and pizz bass pile up at 150-300 Hz on phone speakers)
def peq(x, f0, gain_db, q=0.9):
    A = 10 ** (gain_db / 40); w = 2 * np.pi * f0 / SR; al = np.sin(w) / (2 * q)
    b = np.array([1 + al * A, -2 * np.cos(w), 1 - al * A]); a = np.array([1 + al / A, -2 * np.cos(w), 1 - al / A])
    return sosfilt(np.hstack([b / a[0], a / a[0]])[None, :], x, axis=0)
mix = mu * 1.0 + fx * 0.85
mix = sosfilt(hp, mix, axis=0)
mix = peq(mix, 220, -2.5)
mix = peq(mix, 3800, +3.5, q=0.7)            # v2: presence (2.5-6 kHz held only 2.6 % of the energy in v1)
# master: loudness to -14 LUFS with a look-ahead limiter on 4x oversampled peaks (mallet transients are peaky, so a
# plain gain would clip); linked stereo gain; the final two-pass loudnorm in finish.sh then only trims.
import subprocess, re, tempfile
from scipy.signal import resample_poly
from scipy.ndimage import maximum_filter1d, uniform_filter1d

def lufs(x):
    with tempfile.NamedTemporaryFile(suffix='.wav') as f:
        sf.write(f.name, x.astype(np.float32), SR, subtype='FLOAT')
        err = subprocess.run(['ffmpeg', '-hide_banner', '-nostats', '-i', f.name, '-af', 'ebur128=peak=true', '-f', 'null', '-'],
                             capture_output=True, text=True).stderr
    tail = err[err.rfind('Summary:'):]
    return float(re.search(r'I:\s+(-?[\d.]+) LUFS', tail).group(1)), float(re.search(r'Peak:\s+(-?[\d.]+) dBFS', tail).group(1))

def limiter(x, ceil_db=-2.6, look=0.006, rel=0.06):
    ceil = 10 ** (ceil_db / 20)
    pk = np.abs(resample_poly(x, 4, 1, axis=0)).max(axis=1).reshape(-1, 4).max(axis=1)[:len(x)]
    n = int(look * SR)
    g = np.minimum(1.0, ceil / np.maximum(maximum_filter1d(pk, 2 * n + 1), 1e-9))
    g = np.minimum(g, uniform_filter1d(g, int(rel * SR)))      # slower recovery, never above the hold
    g = uniform_filter1d(g, n)
    limiter.stats = {k: float(np.mean(g < 10 ** (-k / 20))) for k in (1, 3, 6)}
    return x * g[:, None], 20 * np.log10(g.min())

raw = mix.copy()
I0, _ = lufs(raw)
gain_db = -14.0 - I0
for _ in range(3):
    out, gr = limiter(raw * 10 ** (gain_db / 20))
    I, tp = lufs(out)
    gain_db += (-14.0 - I)
out, gr = limiter(raw * 10 ** (gain_db / 20))
# v2: room tone in the planned silence (v1 was digital zero for 1.4 s): a dark, far air at about -50 dBFS, so the rest
# reads as the inside of the hole and not as a dropout. It is added after the limiter, under everything else.
import json
cu = json.load(open(os.path.join(HERE, 'events.json')))['cues']
rng = np.random.default_rng(5)
t0, t1 = cu['cut'] - 0.1, cu['light'] + 0.3
n = int((t1 - t0) * SR)
air = rng.standard_normal((n, 2)).cumsum(axis=0)
air = sosfilt(butter(2, [45, 900], 'band', fs=SR, output='sos'), air, axis=0)
env = np.minimum(1, np.minimum(np.arange(n) / (0.5 * SR), (n - np.arange(n)) / (0.4 * SR)))
air = air / np.sqrt(np.mean(air ** 2)) * 10 ** (-50 / 20) * env[:, None]
i0 = int(t0 * SR); out[i0:i0 + n] += air
I, tp = lufs(out)
sf.write(os.path.join(HERE, 'mix_raw.wav'), out.astype(np.float32), SR, subtype='PCM_24')
rms = lambda x: 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12)
print('limiter: share of samples reduced by more than 1/3/6 dB:', {k: f'{v * 100:.2f} %' for k, v in limiter.stats.items()})
print(f'mix_raw: in {I0:.1f} LUFS, gain {gain_db:+.1f} dB, max limiting {gr:.1f} dB -> {I:.2f} LUFS, true peak {tp:.2f} dBTP; music rms {rms(mu):.1f}, foley rms {rms(fx*0.85):.1f}')
