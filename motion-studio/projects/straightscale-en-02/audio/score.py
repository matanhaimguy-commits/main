# Score and effects for StraightScale EN reel 02, from real CC0 instrument samples (VSCO 2 CE, VCSL) via the
# Lemo-Opuscar sampler, plus procedural foley. Run with the sampler's venv:
#   ~/lemo/.venv/bin/python audio/score.py   ->  audio/music.wav, audio/sfx.wav (48 kHz stereo)
# Every accent comes from audio/events.json (exported from the film by tools/events.mjs), never retyped.
# Harmony follows the story: B minor under "praying someone books a call", a stop before the reveal, D major from
# "it sounds like you", a build under the 567 count that resolves when the number lands, and a cadence on the logo.
import json, os, sys
import numpy as np, soundfile as sf

sys.path.insert(0, os.path.expanduser('~/lemo/core/audio'))
import sampler as S, sfx as X

HERE = os.path.dirname(os.path.abspath(__file__))
EV = json.load(open(os.path.join(HERE, 'events.json')))
DUR, CUE = EV['duration'], EV['cues']
SR = X.SR
N = int(DUR * SR)
times = lambda kind, lo=-1.0, hi=1e9: [e['t'] for e in EV['events'] if e['kind'] == kind and lo <= e['t'] < hi]
first = lambda kind: times(kind)[0]
B = 60 / 104       # one beat at 104 BPM
music, fx = np.zeros((N, 2), np.float32), np.zeros((N, 2), np.float32)
ev = []            # sampler events (t, inst, pitch, dur, vel, pan)
S.seed(11)


def add(buf, x, t, gain=1.0, pan=0.0):
    x = np.asarray(x, np.float32)
    if x.ndim == 2:
        i = max(0, int(round(t * SR))); n = min(len(x), len(buf) - i); buf[i:i + n] += x[:n] * gain
    else:
        X.add(buf, x, max(0.0, t), gain, pan)


def swell(inst, pitch, t, dur, v0, v1, pan=0.0, gain=1.0):
    x = S.note(inst, pitch, dur, max(v0, v1))
    ramp = np.linspace(v0 / max(v0, v1), v1 / max(v0, v1), len(x), dtype=np.float32)
    add(music, x * ramp, t, gain, pan)


def grid(t0, t1, step):
    k = int(np.ceil(t0 / step - 1e-6))
    while k * step < t1 - 1e-6:
        yield k, k * step
        k += 1


CH = {'D': ('D2', ['D3', 'A3', 'F#4']), 'A': ('A1', ['A2', 'E3', 'C#4']), 'Bm': ('B1', ['B2', 'F#3', 'D4']),
      'G': ('G1', ['G2', 'D3', 'B3']), 'Em': ('E2', ['E3', 'B3', 'G4'])}
ARP = {'D': ['D5', 'A4', 'F#5', 'A4'], 'A': ['C#5', 'A4', 'E5', 'A4'], 'Bm': ['D5', 'B4', 'F#5', 'B4'],
       'G': ['D5', 'B4', 'G5', 'B4'], 'Em': ['E5', 'B4', 'G5', 'B4']}


def groove(prog, mar=0.3, bass=0.5, pad=0.18, pizz=0.0):
    """prog: [(t0, t1, chord)]. Pizzicato bass on the beat, a marimba ostinato in eighths, strings held under it."""
    for t0, t1, c in prog:
        assert t1 > t0, (t0, t1, c)
        root, chord = CH[c]
        for k, t in grid(t0, t1, B):
            ev.append((t, 'contrabass_pizz', root, B * 0.9, bass * (1.0 if k % 2 == 0 else 0.82), 0.0))
        if mar:
            for k, t in grid(t0, t1, B / 2):
                ev.append((t, 'marimba', ARP[c][k % 4], B * 0.9, mar * (1.0 if k % 2 == 0 else 0.78), 0.25))
        if pizz:
            for k, t in grid(t0, t1, B / 4):
                ev.append((t, 'violins_pizz', ARP[c][(k + 1) % 4], B * 0.3, pizz * (1.0 if k % 4 == 0 else 0.7), -0.3))
        if pad:
            for j, p in enumerate(chord):
                ev.append((t0, ('cellos', 'violas', 'violas')[j], p, t1 - t0 + 0.35, pad * (0.6 if j == 0 else 1.0), (-0.3, 0.3, 0.0)[j]))


l2, l3, l4, l5, l6, l7, l8, l9, l10 = (CUE[k] for k in ('l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8', 'l9', 'l10'))
stamp, brand = first('stamp'), first('brand')

# ---- hook (0 - 4.5): B minor, sparse; the slip lands on a low note ----
groove([(0.0, 2 * B * 2, 'Bm'), (4 * B, l2 - 0.45, 'G')], mar=0.24, bass=0.45, pad=0.16)
ev += [(0.0, 'timpani', 'B2', 1.2, 0.35, 0.0), (0.0, 'vibraphone', 'F#5', 1.6, 0.3, 0.2)]

# ---- the reveal (5.0 - 8.4): the pulse stops before "we didn't write that", then the stamp lands ----
swell('cellos', 'G2', l2 - 0.3, stamp - l2 + 0.6, 0.12, 0.4, -0.2)
swell('violas', 'D3', l2 - 0.1, stamp - l2 + 0.4, 0.1, 0.35, 0.2)
for p, inst, v in [('A2', 'contrabass_pizz', 0.7), ('A4', 'marimba', 0.5), ('C#5', 'marimba', 0.45), ('E5', 'marimba', 0.45),
                   ('A6', 'glockenspiel', 0.3)]:
    ev.append((stamp, inst, p, 1.2, v, 0.0))
groove([(stamp + B, l3, 'A')], mar=0.2, bass=0.4, pad=0.0)

# ---- "it sounds like you" (8.4 - 12.9): D major arrives; the loop I-V-vi-IV runs from here ----
loop = ['D', 'A', 'Bm', 'G']
def loop_prog(t0, t1, start=0, bars=2):
    out, i, t = [], start, t0
    while t < t1 - 1e-6:
        e = min(t1, t + bars * B)
        out.append((t, e, loop[i % 4])); i += 1; t = e
    return out
groove(loop_prog(l3, l4), mar=0.3, bass=0.5, pad=0.2)
nar = first('narrow')
ev += [(nar, 'vibraphone', 'D5', 1.4, 0.4, 0.2), (nar + 0.12, 'vibraphone', 'F#5', 1.4, 0.38, 0.25)]

# ---- the three places (12.9 - 27.3): the same loop, a lift each time a new source comes forward ----
groove(loop_prog(l4, l8), mar=0.32, bass=0.52, pad=0.2)
for t in times('num'):
    ev.append((t, 'glockenspiel', 'D6', 0.5, 0.25, 0.3))
for t, p in zip(times('slide', l5 - 0.5, l8 - 0.5), ['A5', 'B5', 'D6']):
    ev.append((t + 0.1, 'harp', p, 1.2, 0.4, -0.2))

# ---- don't polish it (27.75 - 32.5): the bass steps out; the strike lands on a low note ----
groove([(l8, l8 + 4 * B, 'G'), (l8 + 4 * B, l9, 'A')], mar=0.26, bass=0.0, pad=0.22)
ev.append((first('strike'), 'cellos_pizz', 'G2', 0.6, 0.55, 0.0))

# ---- 567 (32.5 - 37.4): a build on A that resolves to D when the number lands ----
c0, c1 = first('count0'), first('count1')
groove([(c0, c1, 'A')], mar=0.3, bass=0.45, pad=0.0, pizz=0.22)
swell('violins', 'E4', c0, c1 - c0 + 0.2, 0.08, 0.5, 0.25)
swell('violas', 'C#4', c0, c1 - c0 + 0.2, 0.08, 0.45, -0.25)
for i, p in enumerate(['A3', 'C#4', 'E4', 'A4', 'C#5', 'E5']):
    ev.append((c1 - 0.3 + i * 0.05, 'harp', p, 1.2, 0.45, -0.25 + 0.1 * i))
for p, inst, v in [('D2', 'contrabass_pizz', 0.75), ('D5', 'marimba', 0.55), ('F#5', 'marimba', 0.5), ('A5', 'marimba', 0.5),
                   ('D7', 'glockenspiel', 0.35)]:
    ev.append((c1, inst, p, 1.2, v, 0.0))
ev.append((c1, 'timpani', 'D3', 1.2, 0.45, 0.0))
groove(loop_prog(c1, l10), mar=0.3, bass=0.5, pad=0.2)

# ---- the CTA (37.4 - 40.1): the loop with a lift; WORDS on a glockenspiel ----
groove(loop_prog(l10, brand), mar=0.32, bass=0.52, pad=0.22, pizz=0.12)
c = first('cta')
ev += [(c, 'glockenspiel', 'A6', 1.0, 0.4, 0.3), (c + 0.1, 'glockenspiel', 'D7', 1.2, 0.35, 0.3)]
for k, t in grid(l10 + B, brand, 2 * B):
    ev.append((t, 'tambourine', None, 0.4, 0.12, 0.35))

# ---- the logo (40.1 - 42.1): the cadence on D, left to ring ----
for p, inst, v in [('D2', 'contrabass_pizz', 0.7), ('D5', 'marimba', 0.55), ('F#5', 'marimba', 0.45), ('A5', 'marimba', 0.45),
                   ('D7', 'glockenspiel', 0.32)]:
    ev.append((brand, inst, p, 1.6, v, 0.0))
for i, p in enumerate(['D3', 'A3', 'D4', 'F#4', 'A4', 'D5']):
    ev.append((brand - 0.22 + i * 0.045, 'harp', p, 1.6, 0.48, -0.25 + 0.1 * i))
for inst, p in [('cellos', 'D3'), ('violas', 'A3'), ('violins', 'F#4')]:
    swell(inst, p, brand, DUR - brand, 0.36, 0.02, 0.0)

add(music, S.render(ev, DUR, master=False), 0.0)
music = S.room(music, size=0.38, mix=0.18)
fade = int(0.4 * SR)
music[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)[:, None]


# ---- effects (procedural foley: paper, a marker, a stamp) ----
def marker(d=0.22):
    """A felt highlighter dragged across paper: band-passed noise with a slow wobble."""
    n = X.noise(d); tt = X.t_(d)
    y = X.bp(n, 2200, 5200) * (0.6 + 0.4 * np.sin(2 * np.pi * 9 * tt)) * np.minimum(1, tt / 0.02) * X.env_exp(d, d * 0.8)
    return X.norm(y, 0.8)


def paper(d=0.3):
    return X.norm(X.hp(X.whoosh(d, 1.0), 1200), 0.8)


add(fx, X.thump(0.5, 70), first('drop'), 0.45, 0.0)
add(fx, paper(0.25), first('drop') - 0.05, 0.3, 0.0)
for t in times('mark', 10):                       # the source highlights only; the hook's words stay quiet
    add(fx, marker(0.3), t, 0.28, 0.15)
add(fx, X.thump(0.7, 80), stamp, 0.55, 0.0)
add(fx, X.lp(X.clack(0.8, 0.8), 4000), stamp, 0.35, 0.1)
for t in times('paper') + times('slide') + times('swipe'):
    add(fx, paper(0.32), t - 0.05, 0.3, 0.2)
add(fx, X.pop(0.5), first('card'), 0.28, 0.1)
st = first('strike')
add(fx, X.bp(X.noise(0.24), 1800, 6000) * X.env_exp(0.24, 0.08), st, 0.24, 0.2)
add(fx, X.thump(0.55, 60), c1, 0.4, 0.0)
add(fx, X.thump(0.5, 60), brand, 0.4, 0.0)
fx[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)[:, None]

for name, x in (('music', music), ('sfx', fx)):
    peak = np.abs(x).max()
    sf.write(os.path.join(HERE, name + '.wav'), (x / max(peak, 1e-9) * 0.89).astype(np.float32), SR, subtype='PCM_24')
    print(name, f'{len(x) / SR:.2f} s, peak before normalise {20 * np.log10(peak + 1e-9):.1f} dBFS')
