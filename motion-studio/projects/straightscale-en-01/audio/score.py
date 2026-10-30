# Score and effects for StraightScale EN reel 01, from real CC0 instrument samples (VSCO 2 CE, VCSL) via the
# Lemo-Opuscar sampler, plus procedural foley. Run with the sampler's venv:
#   ~/lemo/.venv/bin/python audio/score.py   ->  audio/music.wav, audio/sfx.wav (48 kHz stereo)
# Every accent is placed from audio/events.json (exported from the film by tools/events.mjs), never retyped.
# Harmony follows the story: C major for the good March, A minor once the replies leak, C major again when the
# third plank closes the gap, and a full cadence on the logo. The pulse keeps one beat grid (96 BPM) for the whole
# film and stops only while the months go missing.
import json, os, sys
import numpy as np, soundfile as sf

sys.path.insert(0, os.path.expanduser('~/lemo/core/audio'))
import sampler as S, sfx as X

HERE = os.path.dirname(os.path.abspath(__file__))
EV = json.load(open(os.path.join(HERE, 'events.json')))
DUR, CUE = EV['duration'], EV['cues']
SR = X.SR
N = int(DUR * SR)
times = lambda kind, lo=0.0, hi=1e9: [e['t'] for e in EV['events'] if e['kind'] == kind and lo <= e['t'] < hi]
first = lambda kind: times(kind)[0]
B = 0.625          # one beat at 96 BPM
music, fx = np.zeros((N, 2), np.float32), np.zeros((N, 2), np.float32)
ev = []            # sampler events (t, inst, pitch, dur, vel, pan)
S.seed(7)


def add(buf, x, t, gain=1.0, pan=0.0):
    x = np.asarray(x, np.float32)
    if x.ndim == 2:
        i = int(round(t * SR)); n = min(len(x), len(buf) - i); buf[i:i + n] += x[:n] * gain
    else:
        X.add(buf, x, t, gain, pan)


def swell(inst, pitch, t, dur, v0, v1, pan=0.0, gain=1.0):
    """A long note with a gain ramp, placed straight into the music bus."""
    x = S.note(inst, pitch, dur, max(v0, v1))
    ramp = np.linspace(v0 / max(v0, v1), v1 / max(v0, v1), len(x), dtype=np.float32)
    add(music, x * ramp, t, gain, pan)


def grid(t0, t1, step):
    """Points of the film's one beat grid inside [t0, t1)."""
    k = int(np.ceil(t0 / step - 1e-6))
    while k * step < t1 - 1e-6:
        yield k, k * step
        k += 1


CH = {'C': ('C2', ['C3', 'G3', 'E4']), 'Am': ('A1', ['A2', 'E3', 'C4']), 'F': ('F1', ['F2', 'C3', 'A3']),
      'G': ('G1', ['G2', 'D3', 'B3'])}
ARP = {'C': ['C4', 'G4', 'E5', 'G4'], 'Am': ['A3', 'E4', 'C5', 'E4'], 'F': ['F3', 'C4', 'A4', 'C4'], 'G': ['G3', 'D4', 'B4', 'D4']}
MOTIF = {'C': ['E5', 'G5', 'C6', 'G5'], 'G': ['D5', 'G5', 'B5', 'G5'], 'Am': ['E5', 'A5', 'C6', 'A5'], 'F': ['F5', 'A5', 'C6', 'A5']}


def groove(prog, piano=0.3, bass=0.5, pad=0.2, motif=0.0, pizz=0.0):
    """prog: [(t0, t1, chord)]. Bass on the beat, a broken chord on the upright in eighths, strings held under it."""
    for t0, t1, c in prog:
        assert t1 > t0, (t0, t1, c)
        root, chord = CH[c]
        for k, t in grid(t0, t1, B):
            ev.append((t, 'contrabass_pizz', root, B * 0.9, bass * (1.0 if k % 2 == 0 else 0.85), 0.0))
        if piano:
            for k, t in grid(t0, t1, B / 2):
                ev.append((t, 'upright', ARP[c][k % 4], B * 0.8, piano * (1.0 if k % 2 == 0 else 0.8), 0.15))
        if pizz:
            for k, t in grid(t0, t1, B / 2):
                ev.append((t, 'violins_pizz', chord[1 + k % 2].replace('3', '5').replace('4', '5'), B * 0.4, pizz, -0.3))
        if motif:
            for k, t in grid(t0, t1, B / 2):
                if k % 8 < 4: ev.append((t, 'marimba', MOTIF[c][k % 4], B, motif * (1 - 0.08 * (k % 4)), 0.3))
        if pad:
            for j, p in enumerate(chord):
                ev.append((t0, ('cellos', 'violas', 'violas')[j], p, t1 - t0 + 0.35, pad, (-0.3, 0.3, 0.0)[j]))


# ---- A1 March (0 - 1.79): C major, light; each signed client a rising marimba note ----
april = CUE['april']
groove([(0.0, april, 'C')], piano=0.32, bass=0.5, pad=0.18)
for t, p in zip(times('signed'), ['E5', 'G5', 'C6']):
    ev.append((t, 'marimba', p, 0.6, 0.55, 0.3))

# ---- A2 April (1.79 - 4.33): the floor drops to A minor; the path cracks; three replies fall ----
groove([(april, CUE['l2'], 'Am')], piano=0.26, bass=0.55, pad=0.0)
swell('cellos', 'A2', april, CUE['l2'] - april + 0.4, 0.45, 0.2, -0.2)
swell('contrabass', 'A1', april, CUE['l2'] - april + 0.4, 0.5, 0.2, 0.0)
crack = first('crack')
ev.append((crack, 'timpani', 'A2', 1.2, 0.5, 0.0))
for t, p in zip(times('fall', 0, 5), ['E4', 'C4', 'A3']):
    ev.append((t, 'marimba', p, 0.8, 0.42, -0.25))

# ---- B proof (4.33 - 8.2): Am and F trade like good and empty months; the grid arrives on a harp ----
l2, l3 = CUE['l2'], CUE['l3']
groove([(l2, l2 + 2 * B, 'Am'), (l2 + 2 * B, l2 + 4 * B, 'F'), (l2 + 4 * B, l3, 'Am')], piano=0.28, bass=0.48, pad=0.2)
g = first('grid')
for i, p in enumerate(['A3', 'C4', 'E4', 'A4', 'C5']):
    ev.append((g + i * 0.04, 'harp', p, 1.2, 0.42, -0.2 + 0.1 * i))
for k, t in grid(CUE['exact'], l3, B / 2):
    ev.append((t, 'vibraphone', ['E5', 'C5'][k % 2], B, 0.22, 0.25))

# ---- C advice (8.2 - 11.26) and D still works (11.26 - 14.44): the pulse walks on; each reply a soft high note ----
l4, l5 = CUE['l4'], CUE['l5']
groove([(l3, CUE['post'], 'Am'), (CUE['post'], CUE['prospect'], 'G'), (CUE['prospect'], l4, 'F'),
        (l4, l4 + 2 * B, 'F'), (l4 + 2 * B, l4 + 4 * B, 'C'), (l4 + 4 * B, l5, 'G')], piano=0.28, bass=0.5, pad=0.2)
for t, p in zip(times('reply'), ['A5', 'C6', 'E6', 'D6', 'C6', 'E6', 'G6', 'E6', 'A6']):
    ev.append((t, 'glockenspiel', p, 0.5, 0.2, 0.35))
tk = first('tick')
ev += [(tk, 'vibraphone', 'G5', 0.9, 0.4, 0.2), (tk + 0.1, 'vibraphone', 'C6', 1.2, 0.4, 0.25)]

# ---- E the leak (14.44 - 16.96): the pulse stops; a low drone; each lost reply a falling harp note ----
l6 = CUE['l6']
swell('cellos', 'A2', l5, l6 - l5 + 0.6, 0.15, 0.55, -0.2)
swell('contrabass', 'A1', l5, l6 - l5 + 0.6, 0.2, 0.5, 0.0)
swell('vibraphone_bowed', 'E4', l5 + 0.3, l6 - l5, 0.35, 0.2, 0.2)
for t, p in zip(times('fall', 10), ['A4', 'G4', 'E4', 'D4', 'C4', 'B3', 'A3', 'G3', 'E3']):
    ev.append((t, 'harp', p, 1.6, 0.48, -0.1))

# ---- F the check (16.96 - 18.65): the planks appear on a harp; the numerals land on wood ----
l7 = CUE['l7']
groove([(l6, l7, 'Am')], piano=0.0, bass=0.4, pad=0.2)
o = first('outline')
for i, p in enumerate(['A3', 'C4', 'E4', 'A4', 'C5', 'E5']):
    ev.append((o + i * 0.05, 'harp', p, 1.4, 0.45, -0.25 + 0.1 * i))

# ---- G, H, I the three steps (18.65 - 34.27): one progression; each plank lands on its chord ----
p1, p2, p3 = times('plank')
l8, l9 = CUE['l8'], CUE['l9']
groove([(l7, l7 + 4 * B, 'Am'), (l7 + 4 * B, p1, 'F'), (p1, l8, 'C')], piano=0.3, bass=0.5, pad=0.2)
groove([(l8, l8 + 4 * B, 'F'), (l8 + 4 * B, CUE['gap'], 'C'), (CUE['gap'], p2, 'Am'), (p2, l9, 'C')], piano=0.3, bass=0.5, pad=0.2)
groove([(l9, l9 + 4 * B, 'F'), (l9 + 4 * B, l9 + 6 * B, 'G'), (l9 + 6 * B, l9 + 8 * B, 'Am'), (l9 + 8 * B, p3, 'G')],
       piano=0.32, bass=0.52, pad=0.22)
groove([(l9 + 4 * B, p3, 'G')], piano=0.0, bass=0.0, pad=0.0, pizz=0.16)     # a lift as the last step is spoken
for t, p in zip(times('col'), ['C5', 'D5', 'E5', 'G5', 'A5', 'C6']):
    ev.append((t, 'marimba', p, 0.6, 0.32, 0.3))
for t, p in zip((p1, p2), ('C5', 'E5')):
    ev += [(t, 'marimba', p, 0.9, 0.5, 0.2), (t, 'contrabass_pizz', 'C2', 0.9, 0.6, 0.0)]
lk = first('leak')
swell('cellos', 'A2', lk, 1.2, 0.45, 0.1, -0.2)
# the bridge closes: C major arrives in full
for i, p in enumerate(['C4', 'E4', 'G4', 'C5', 'E5', 'G5', 'C6']):
    ev.append((p3 + i * 0.04, 'harp', p, 2.0, 0.5, -0.3 + 0.1 * i))
ev += [(p3, 'timpani', 'C3', 1.4, 0.5, 0.0), (p3 + 0.3, 'glockenspiel', 'C7', 1.2, 0.3, 0.3)]
for inst, p, v in [('cellos', 'C3', 0.4), ('violas', 'G3', 0.38), ('violins', 'E4', 0.34), ('violins', 'C5', 0.28)]:
    swell(inst, p, p3, 2.2, v, 0.12, 0.0)

# ---- J the CTA (34.27 - 39.53): a C major groove with a marimba motif; PATH on a glockenspiel ----
l11, brand = CUE['l11'], first('brand')
groove([(p3, p3 + 2 * B, 'C'), (p3 + 2 * B, p3 + 4 * B, 'G'), (p3 + 4 * B, p3 + 6 * B, 'Am'), (p3 + 6 * B, l11, 'F')],
       piano=0.3, bass=0.52, pad=0.2, motif=0.3)
c = first('cta')
ev += [(c, 'glockenspiel', 'G6', 1.0, 0.4, 0.3), (c + 0.1, 'glockenspiel', 'C7', 1.2, 0.35, 0.3)]
for k, t in grid(p3 + B, l11, 2 * B):
    ev.append((t, 'tambourine', None, 0.4, 0.13, 0.35))

# ---- K the close (39.53 - 41.3): F to G, held open; L the brand (41.3 - 43.25): the cadence on C ----
groove([(l11, l11 + 1.5 * B, 'F'), (l11 + 1.5 * B, brand, 'G')], piano=0.24, bass=0.45, pad=0.22)
for p, inst, v in [('C2', 'contrabass_pizz', 0.7), ('C5', 'marimba', 0.55), ('E5', 'marimba', 0.45), ('G5', 'marimba', 0.45),
                   ('C7', 'glockenspiel', 0.32), ('C3', 'upright', 0.45), ('G3', 'upright', 0.4), ('E4', 'upright', 0.4)]:
    ev.append((brand, inst, p, 1.6, v, 0.0))
for i, p in enumerate(['C3', 'G3', 'C4', 'E4', 'G4', 'C5']):
    ev.append((brand - 0.22 + i * 0.045, 'harp', p, 1.6, 0.48, -0.25 + 0.1 * i))
for inst, p in [('cellos', 'C3'), ('violas', 'G3'), ('violins', 'E4')]:
    swell(inst, p, brand, DUR - brand, 0.36, 0.02, 0.0)

# render the sampler events, one room, fade the very end
add(music, S.render(ev, DUR, master=False), 0.0)
music = S.room(music, size=0.38, mix=0.18)
fade = int(0.4 * SR)
music[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)[:, None]

# ---- effects (procedural foley, small and dry) ----
add(fx, X.lp(X.clack(0.55, 0.9), 3500), crack, 0.55, -0.1)
add(fx, X.thump(0.55, 60), crack, 0.5, 0.0)
for t in times('fall', 0, 5):
    add(fx, X.hp(X.whoosh(0.3, 0.45), 900), t - 0.05, 0.3, -0.2)
for t in times('stamp'):
    add(fx, X.thump(0.7, 85), t, 0.55, 0.0)
    add(fx, X.lp(X.click(0.7, 0.7), 4000), t, 0.35, 0.1)
for t in times('land') + times('plank'):
    add(fx, X.lp(X.clack(0.9, 0.6), 5000), t, 0.38, -0.15)
for t in times('circle'):
    add(fx, X.hp(X.whoosh(0.4, 0.35), 2500), t, 0.28, 0.25)
for t in times('bubble'):
    add(fx, X.pop(0.5), t, 0.3, 0.15)
st = first('strike')
scratch = X.bp(X.noise(0.22), 1800, 6000) * X.env_exp(0.22, 0.07)
add(fx, scratch, st, 0.22, 0.2)
add(fx, X.thump(0.6, 55), p3, 0.45, 0.0)
add(fx, X.thump(0.5, 60), brand, 0.4, 0.0)
fx[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)[:, None]

for name, x in (('music', music), ('sfx', fx)):
    peak = np.abs(x).max()
    sf.write(os.path.join(HERE, name + '.wav'), (x / max(peak, 1e-9) * 0.89).astype(np.float32), SR, subtype='PCM_24')
    print(name, f'{len(x) / SR:.2f} s, peak before normalise {20 * np.log10(peak + 1e-9):.1f} dBFS')
