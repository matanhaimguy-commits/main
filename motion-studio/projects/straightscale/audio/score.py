# Original score + SFX for the StraightScale reel, synthesized from scratch.
# python3 audio/score.py  ->  audio/music.wav, audio/sfx.wav
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

SR = 44100
BPM = 120
BEAT = 60 / BPM
DUR = 50.0
N = int(DUR * SR)
rng = np.random.default_rng(7)  # seeded: identical render every time


def lp(x, hz, order=2):
    return sosfilt(butter(order, hz, 'low', fs=SR, output='sos'), x)


def hp(x, hz, order=2):
    return sosfilt(butter(order, hz, 'high', fs=SR, output='sos'), x)


def bp(x, lo, hi, order=2):
    return sosfilt(butter(order, [lo, hi], 'band', fs=SR, output='sos'), x)


def mtof(m):
    return 440 * 2 ** ((m - 69) / 12)


def saw(f, n, phase=0.0):
    t = np.arange(n) / SR
    return 2 * ((t * f + phase) % 1) - 1


def env(n, a=0.005, d=0.2, s=0.0, r=0.05, hold=None):
    """Attack / exponential decay toward s / release over n samples."""
    t = np.arange(n) / SR
    e = np.where(t < a, t / max(a, 1e-6), s + (1 - s) * np.exp(-(t - a) / max(d, 1e-6)))
    rel = int(r * SR)
    if rel and n > rel:
        e[-rel:] *= np.linspace(1, 0, rel)
    return e


def place(buf, x, t, gain=1.0):
    i = int(round(t * SR))
    if i >= len(buf):
        return
    x = x[: len(buf) - i]
    buf[i:i + len(x)] += gain * x


# ---------- instruments ----------
def kick(n=int(0.45 * SR)):
    t = np.arange(n) / SR
    f = 45 + 95 * np.exp(-t * 28)
    ph = 2 * np.pi * np.cumsum(f) / SR
    body = np.sin(ph) * np.exp(-t * 7)
    click = hp(rng.standard_normal(n), 2000) * np.exp(-t * 300) * 0.25
    return np.tanh(1.6 * (body + click))


def hat(open_=False):
    n = int((0.22 if open_ else 0.06) * SR)
    t = np.arange(n) / SR
    return hp(rng.standard_normal(n), 7000, 4) * np.exp(-t * (18 if open_ else 70))


def clap():
    n = int(0.3 * SR)
    t = np.arange(n) / SR
    noise = bp(rng.standard_normal(n), 900, 5000)
    e = np.exp(-t * 22)
    for off in (0.008, 0.017):  # the three-hand smear of a real clap
        k = int(off * SR)
        e[k:] += np.exp(-(t[: n - k]) * 22) * 0.8
    return noise * e * 0.55


def bass_note(m, n):
    f = mtof(m)
    x = 0.8 * np.sin(2 * np.pi * f * np.arange(n) / SR) + 0.35 * lp(saw(f, n), 400)
    return x * env(n, 0.004, 0.18, 0.55, 0.03)


def pad_chord(notes, n, cutoff):
    x = np.zeros(n)
    for m in notes:
        for det in (-0.08, 0.0, 0.07):
            x += saw(mtof(m + det), n, phase=(m * 0.137 + det) % 1)
    x = lp(x, cutoff, 2) / (len(notes) * 3)
    t = np.arange(n) / SR
    a = np.minimum(1, t / 0.25)
    rel = np.minimum(1, (n / SR - t) / 0.2)
    return x * a * rel


def pluck(m, n=int(0.35 * SR)):
    f = mtof(m)
    x = saw(f, n) * 0.6 + np.sin(2 * np.pi * f * 2 * np.arange(n) / SR) * 0.3
    return lp(x, 3200) * env(n, 0.002, 0.09, 0.0, 0.02)


def riser(n):
    t = np.arange(n) / SR
    x = rng.standard_normal(n)
    segs = 16  # stepped band-pass sweeping upward
    out = np.zeros(n)
    for s in range(segs):
        a, b = s * n // segs, (s + 1) * n // segs
        c = 400 * (12 ** (s / segs))
        out[a:b] = bp(x[a:b], c, min(c * 2.2, 18000))
    return out * (t / t[-1]) ** 2


def impact(n=int(1.6 * SR)):
    t = np.arange(n) / SR
    f = 38 + 60 * np.exp(-t * 10)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.2)
    air = lp(rng.standard_normal(n), 3000) * np.exp(-t * 6) * 0.4
    return np.tanh(1.4 * (sub + air))


# ---------- arrangement ----------
music = np.zeros(N)
DM, BB, F, C = ([62, 65, 69], 38), ([58, 62, 65], 34), ([60, 65, 69], 41), ([60, 64, 67], 36)
problem = [DM, BB, F, C]   # minor colour for the problem (0-20 s)
fix = [F, C, DM, BB]       # same notes, but centred on F major for the fix (20-50 s)
bar = 4 * BEAT  # 4/4: one bar = 2 s

for b in range(25):
    t0 = b * bar
    prog = problem if t0 < 20 else fix
    notes, root = prog[b % 4]
    cutoff = 700 if t0 < 4 else 1300 if t0 < 20 else 2600
    place(music, pad_chord(notes, int(bar * SR) + int(0.2 * SR), cutoff), t0, 0.32 if t0 < 20 else 0.36)

    for s in range(4):  # beats
        tb = t0 + s * BEAT
        drums_on = 4 <= tb < 19.0 or 20 <= tb < 34 or 36 <= tb < 48
        if drums_on:
            place(music, kick(), tb, 0.9)
            place(music, hat(open_=True), tb + BEAT / 2, 0.12)
            if s in (1, 3) and tb >= 6:
                place(music, clap(), tb, 0.5)
        if tb < 4 or 19 <= tb < 20:  # hook and pre-turn: ticking 16ths, no kick
            for q in range(4):
                place(music, hat(), tb + q * BEAT / 4, 0.10 if q % 2 else 0.16)
        elif drums_on:
            for q in (1, 3):
                place(music, hat(), tb + q * BEAT / 4, 0.07)
        # bass: eighth notes on the root, octave jump on the "and" of 4
        if tb < 48 and not (34 <= tb < 36):
            for e in range(2):
                m = root + (12 if (s == 3 and e == 1) else 0)
                place(music, bass_note(m, int(BEAT / 2 * SR * 0.9)), tb + e * BEAT / 2, 0.42)

    if t0 >= 20 and t0 < 48:  # arpeggio once the fix starts
        arp = [notes[0] + 12, notes[1] + 12, notes[2] + 12, notes[1] + 12]
        for e in range(8):
            place(music, pluck(arp[e % 4]), t0 + e * BEAT / 2, 0.16 if e % 2 == 0 else 0.10)

place(music, impact(), 0.0, 0.55)
place(music, riser(int(1.9 * SR)), 18.1, 0.35)
place(music, impact(), 20.0, 0.7)
place(music, impact(), 36.0, 0.55)
# final bar: one sustained F chord and a last hit under the logo
place(music, pad_chord([53, 60, 65, 69], int(2.2 * SR), 2200), 48.0, 0.45)
place(music, impact(), 48.0, 0.5)
place(music, bass_note(29, int(1.9 * SR)), 48.0, 0.5)


# ---------- sound effects (cue list mirrors docs/shotlist.md) ----------
def pop(pitch=900):
    n = int(0.09 * SR)
    t = np.arange(n) / SR
    f = pitch * (1 + 1.5 * np.exp(-t * 60))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 45)


def tick():
    n = int(0.03 * SR)
    t = np.arange(n) / SR
    return bp(rng.standard_normal(n), 2500, 7000) * np.exp(-t * 200)


def click():
    n = int(0.05 * SR)
    t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1800 * t) * 0.6 + hp(rng.standard_normal(n), 3000) * 0.5) * np.exp(-t * 140)


def key():
    n = int(0.04 * SR)
    t = np.arange(n) / SR
    return bp(rng.standard_normal(n), 1200, 6000) * np.exp(-t * 160) + np.sin(2 * np.pi * 300 * t) * np.exp(-t * 120) * 0.4


def whoosh(dur=0.45, lo=300, hi=4000):
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = rng.standard_normal(n)
    out = np.zeros(n)
    segs = 10
    for s in range(segs):
        a, b = s * n // segs, (s + 1) * n // segs
        c = lo * ((hi / lo) ** np.sin(np.pi * s / segs))
        out[a:b] = bp(x[a:b], c, min(c * 1.8, 18000))
    return out * np.sin(np.pi * t / t[-1]) ** 2


def thump():
    n = int(0.25 * SR)
    t = np.arange(n) / SR
    f = 70 + 80 * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 16)


def stamp():
    return thump() * 0.8 + np.pad(tick(), (0, int(0.25 * SR) - int(0.03 * SR))) * 0.6


def swish():
    return whoosh(0.22, 1500, 9000)


def ping():
    n = int(0.6 * SR)
    t = np.arange(n) / SR
    return (np.sin(2 * np.pi * 1318.5 * t) + 0.5 * np.sin(2 * np.pi * 1975.5 * t)) * np.exp(-t * 7)


sfx = np.zeros(N)
cues = [
    (0.0, pop(820), .5), (0.5, pop(980), .5), (1.0, pop(1150), .5),
    (1.5, tick(), .5), (1.55, tick(), .4), (1.6, tick(), .4),
    (1.85, whoosh(0.5, 2000, 300), .5), (2.3, thump(), .5),
    (3.5, thump(), .8), (4.5, swish(), .45),
    (6.0, whoosh(), .4),
    (6.5, stamp(), .6), (7.0, stamp(), .6), (7.5, stamp(), .6), (8.0, stamp(), .7),
    (10.0, thump(), .6),
    (11.5, whoosh(), .4), (13.5, click(), .7),
    (15.0, thump(), .7), (16.0, stamp(), .6), (16.5, stamp(), .6), (17.0, stamp(), .6), (17.5, stamp(), .6),
    (18.5, whoosh(0.6, 200, 1500), .45),
    (20.0, whoosh(0.7, 300, 6000), .5),
    (21.5, swish(), .35), (22.5, swish(), .35),
    (24.0, whoosh(), .35), (26.0, swish(), .5), (27.0, pop(700), .5),
    (30.0, whoosh(), .35), (31.0, tick(), .6), (31.5, tick(), .6), (32.0, tick(), .6), (32.5, tick(), .6),
    (34.0, whoosh(0.5, 4000, 400), .35),
    (38.0, pop(600), .6), (39.0, swish(), .3), (39.5, swish(), .3), (40.0, swish(), .3),
    (42.5, whoosh(), .4),
    (46.0, whoosh(), .35),
]
for i in range(7):  # A-N-A-L-I-Z-A typed on 16ths from 46.5
    cues.append((46.5 + i * BEAT / 4, key(), .55))
cues += [(47.5, pop(1100), .6), (48.0, ping(), .35)]
for t, x, g in cues:
    place(sfx, x, t, g)

for name, x in (('music', music), ('sfx', sfx)):
    fade = int(0.4 * SR)
    x[-fade:] *= np.linspace(1, 0, fade)
    x = x / (np.max(np.abs(x)) + 1e-9) * 0.89
    sf.write(f'audio/{name}.wav', np.stack([x, x], 1).astype(np.float32), SR, subtype='PCM_24')
print('wrote audio/music.wav audio/sfx.wav')
