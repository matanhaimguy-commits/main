# Score and effects for StraightScale week 43 post 3 "Fat apo sistem", from CC0 VSCO 2 CE samples via the
# Lemo-Opuscar sampler, plus procedural foley. Run with the sampler's venv from the project folder:
#   ~/lemo/.venv/bin/python audio/score.py   ->  audio/music.wav, audio/sfx.wav
# Cues come from audio/events.json (exported from the film by tools/events.mjs), never retyped.
# No voice, so the music carries the argument: a riser and a hit on the viral spike, a planned silence on the flat
# line, a steady C major pulse once the system starts with a harp note one step higher on every stair, the resolve
# on the real mark, and a short sting to end.
import json, os, sys
import numpy as np, soundfile as sf

sys.path.insert(0, os.path.expanduser('~/lemo/core/audio'))
import sampler as S, sfx as X

HERE = os.path.dirname(os.path.abspath(__file__))
EV = json.load(open(os.path.join(HERE, 'events.json')))
DUR = EV['duration']
SR = X.SR
N = int(DUR * SR)
times = lambda kind: [e['t'] for e in EV['events'] if e['kind'] == kind]
first = lambda kind: times(kind)[0]
music, fx = np.zeros((N, 2), np.float32), np.zeros((N, 2), np.float32)
ev = []            # sampler events (t, inst, pitch, dur, vel, pan)
B = 0.4            # one beat at 150 BPM: a stair (1.6 s) is one bar


def add(buf, x, t, gain=1.0, pan=0.0):
    x = np.asarray(x, np.float32)
    if x.ndim == 2:
        i = int(round(t * SR)); n = min(len(x), len(buf) - i); buf[i:i + n] += x[:n] * gain
    else:
        X.add(buf, x, t, gain, pan)


def swell(inst, pitch, t, dur, v0, v1, pan=0.0, gain=1.0):
    x = S.note(inst, pitch, dur, max(v0, v1))
    ramp = np.linspace(v0 / max(v0, v1), v1 / max(v0, v1), len(x), dtype=np.float32)
    add(music, x * ramp, t, gain, pan)


def pulse(inst, notes, t0, t1, step, vel, pan=0.0):
    i, t = 0, t0
    while t < t1 - 1e-6:
        ev.append((t, inst, notes[i % len(notes)], step * 0.9, vel * (1.0 if i % 2 == 0 else 0.8), pan))
        i, t = i + 1, t + step


CH = {'Am': ('A1', ['A3', 'C4', 'E4']), 'F': ('F1', ['F3', 'A3', 'C4']), 'C': ('C2', ['G3', 'C4', 'E4']),
      'G': ('G1', ['G3', 'B3', 'D4'])}
MOTIF = {'Am': ['A4', 'C5', 'E5', 'C5'], 'F': ['A4', 'C5', 'F5', 'C5'], 'C': ['C5', 'E5', 'G5', 'E5'], 'G': ['B4', 'D5', 'G5', 'D5']}


def bar(t0, t1, c, motif_vel=0.26, bass_vel=0.55, pad_vel=0.2):
    root, chord = CH[c]
    pulse('contrabass_pizz', [root], t0, t1, B, bass_vel)
    pulse('cellos_pizz', [chord[0], chord[2]], t0, t1, B / 2, 0.24, 0.2)
    for j, p in enumerate(chord):
        ev.append((t0, 'vibraphone_bowed' if j else 'violas', p, t1 - t0 + 0.3, pad_vel, (-0.3, 0.3, 0.0)[j]))
    k = 0
    while t0 + k * B / 2 < t1 - 1e-6 and motif_vel > 0:
        ev.append((t0 + k * B / 2, 'marimba', MOTIF[c][k % 4], 0.4, motif_vel * (1 - 0.08 * (k % 4)), 0.3))
        k += 1


rise, peak, drop = first('rise'), first('peak'), first('drop')
steps = times('step') + times('stepfast')
parts = times('part')
pull, travel, brand = first('pull'), first('travel'), first('brand')
keys = times('key')
stair0 = steps[0] - 0.62 * 1.6          # the first stair's bar starts here (the page puts the ramp at 62 % of it)

# ---- 1 hook: a low breath, a riser into the peak, a hit, and the drop ----
swell('vibraphone_bowed', 'A3', 0.0, rise + 0.2, 0.08, 0.35, -0.2)
swell('vibraphone_bowed', 'E4', 0.0, rise + 0.2, 0.08, 0.3, 0.2)
ev += [(0.0, 'contrabass_pizz', 'A1', 0.6, 0.5, 0.0), (0.27, 'contrabass_pizz', 'A1', 0.5, 0.35, 0.0)]
swell('violins_trem', 'A4', rise, peak - rise + 0.15, 0.05, 0.6, -0.15)
swell('violins_trem', 'E5', rise, peak - rise + 0.15, 0.05, 0.5, 0.15)
ev += [(peak, 'timpani', 'A2', 1.2, 0.6, 0.0), (peak, 'glockenspiel', 'E7', 1.0, 0.45, 0.3), (peak, 'sus_cymbal', None, 1.4, 0.35, 0.0)]
ev += [(drop, 'timpani', 'E2', 1.6, 0.55, 0.0), (drop, 'contrabass_pizz', 'E1', 1.2, 0.6, 0.0)]

# ---- 2 the silence: nothing but a slow tick and one low note on "Nesër, heshtje" ----
ev.append((3.75, 'upright', 'A1', 2.2, 0.32, 0.0))

# ---- 3-4 the system: C major, one bar per stair, a harp note one step higher on every ramp ----
prog = ['C', 'G', 'Am', 'F', 'C', 'G']
for i, c in enumerate(prog):
    t0 = stair0 + i * 1.6
    bar(t0, t0 + 1.6, c, motif_vel=0.0 if i == 0 else 0.24)
for t, p in zip(steps, ['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6']):
    ev.append((t, 'harp', p, 1.0, 0.55, 0.25))
for t in parts:
    ev.append((t, 'vibraphone', 'G5', 1.0, 0.3, -0.25))
for t in np.arange(stair0 + 2 * B + 1.6, stair0 + 6 * 1.6, 2 * B):
    ev.append((float(t), 'tambourine', None, 0.4, 0.12, 0.35))

# ---- 5 the pull-back: fast stairs, the strings rise and hold on the open chord ----
t0 = stair0 + 6 * 1.6
pulse('contrabass_pizz', ['C2'], t0, travel, B / 2, 0.5)
swell('violins', 'G4', pull, travel - pull + 0.4, 0.1, 0.5, 0.25)
swell('violas', 'E4', pull, travel - pull + 0.4, 0.1, 0.45, -0.25)
swell('cellos', 'C3', pull, travel - pull + 0.4, 0.1, 0.5, 0.0)

# ---- 6 the brand: the dot flies, the mark assembles on the resolve ----
for p, inst, v in [('C2', 'contrabass', 0.6), ('C3', 'cellos', 0.55), ('G3', 'violas', 0.5), ('E4', 'violins', 0.45), ('C5', 'violins', 0.4)]:
    swell(inst, p, brand, 3.0, v, 0.05, 0.0)
for i, p in enumerate(['C4', 'E4', 'G4', 'C5', 'E5', 'G5', 'C6']):
    ev.append((brand + i * 0.04, 'harp', p, 2.0, 0.5, -0.3 + 0.1 * i))
ev += [(brand, 'timpani', 'C3', 1.5, 0.5, 0.0), (brand, 'glockenspiel', 'C7', 1.2, 0.35, 0.3)]

# ---- 7 the CTA: light pulse under the typing, then a three-note sting and a clean end ----
cta = keys[0] - 0.6
for t0, t1, c in [(cta, cta + 1.6, 'F'), (cta + 1.6, cta + 3.2, 'G')]:
    bar(t0, t1, c, motif_vel=0.2, bass_vel=0.45, pad_vel=0.16)
st = cta + 3.2
for i, p in enumerate(['C5', 'E5', 'G5']):
    ev.append((st + i * 0.11, 'marimba', p, 0.8, 0.55, 0.1 * i))
fin = st + 0.33
for p, inst, v in [('C2', 'contrabass_pizz', 0.75), ('C5', 'marimba', 0.5), ('E5', 'vibraphone', 0.45), ('G5', 'vibraphone', 0.4), ('C6', 'glockenspiel', 0.35)]:
    ev.append((fin, inst, p, 1.6, v, 0.0))
ev.append((fin, 'timpani', 'C3', 1.6, 0.5, 0.0))
for p, inst in [('C3', 'cellos'), ('G3', 'violas'), ('E4', 'violins')]:
    swell(inst, p, fin, DUR - fin, 0.35, 0.02, 0.0)

add(music, S.render(ev, DUR, master=False), 0.0)
music = S.room(music, size=0.4, mix=0.18)
fade = int(0.35 * SR)
music[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)[:, None]

# ---- effects (procedural foley, low-passed so nothing is a digital click) ----
add(fx, X.lp(X.whoosh(0.35, 0.6), 7000), rise - 0.1, 0.4, 0.2)
add(fx, X.thump(0.6, 55), drop, 0.5, 0.0)
add(fx, X.lp(X.whoosh(0.5, 0.45), 5000), drop + 0.4, 0.3, -0.2)   # the slide
for t in np.arange(2.75, stair0 - 0.05, 0.5):
    add(fx, X.lp(X.click(1.6, 0.4), 6000), float(t), 0.3, -0.15)  # the clock while nothing happens
for t in steps:
    add(fx, X.lp(X.click(1.2, 0.4), 6000), t, 0.22, 0.2)
add(fx, X.lp(X.whoosh(0.6, 0.5), 5000), travel, 0.35, 0.1)
add(fx, X.lp(X.pop(0.5), 6000), brand, 0.35, 0.0)
for t in keys:
    add(fx, X.lp(X.click(1.1, 0.35), 5000), t, 0.22, 0.25)
add(fx, X.thump(0.4, 60), fin, 0.4, 0.0)
fx[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)[:, None]

for name, x in (('music', music), ('sfx', fx)):
    pk = np.abs(x).max()
    sf.write(os.path.join(HERE, name + '.wav'), (x / max(pk, 1e-9) * 0.89).astype(np.float32), SR, subtype='PCM_24')
    print(name, f'{len(x) / SR:.2f} s, peak before normalise {20 * np.log10(pk + 1e-9):.1f} dBFS')
