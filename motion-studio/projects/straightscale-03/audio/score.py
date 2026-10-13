# Score and effects for StraightScale reel 03 "Qartësia", from real CC0 instrument samples (VSCO 2 CE, VCSL) via the
# Lemo-Opuscar sampler, plus procedural foley. Run with the sampler's venv:
#   ~/lemo/.venv/bin/python audio/score.py   ->  audio/music.wav, audio/sfx.wav (48 kHz stereo)
# Cues come from audio/events.json (exported from the film by tools/events.mjs) and audio/words.json, never retyped.
# Harmony follows the argument: A minor while attention leaks and the market gets noisy, a planned silence on
# "nuk janë më të zhurmshme", C major once clarity arrives, resolving on "strategji".
import json, os, sys
import numpy as np, soundfile as sf

sys.path.insert(0, os.path.expanduser('~/lemo/core/audio'))
import sampler as S, sfx as X

HERE = os.path.dirname(os.path.abspath(__file__))
EV = json.load(open(os.path.join(HERE, 'events.json')))
WD = json.load(open(os.path.join(HERE, 'words.json')))['words']
DUR = EV['duration']
SR = X.SR
N = int(DUR * SR)
times = lambda kind: [e['t'] for e in EV['events'] if e['kind'] == kind]
first = lambda kind: times(kind)[0]
ws = lambda i: WD[i]['s']
B = 0.5            # one beat at 120 BPM; sections restart their grid at spoken cues
music, fx = np.zeros((N, 2), np.float32), np.zeros((N, 2), np.float32)
ev = []            # sampler events (t, inst, pitch, dur, vel, pan)


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
      'G': ('G1', ['G3', 'B3', 'D4']), 'Dm': ('D2', ['F3', 'A3', 'D4']), 'E': ('E2', ['G#3', 'B3', 'E4'])}
MOTIF = {'Am': ['A4', 'C5', 'E5', 'C5'], 'F': ['A4', 'C5', 'F5', 'C5'], 'C': ['C5', 'E5', 'G5', 'E5'],
         'G': ['B4', 'D5', 'G5', 'D5'], 'Dm': ['A4', 'D5', 'F5', 'D5'], 'E': ['G#4', 'B4', 'E5', 'B4']}


def section(prog, motif_vel=0.3, bass_vel=0.55, pad_vel=0.22, motif=True, eighths=True):
    for t0, t1, c in prog:
        root, chord = CH[c]
        pulse('contrabass_pizz', [root], t0, t1, B, bass_vel)
        if eighths: pulse('cellos_pizz', [chord[0], chord[2]], t0, t1, B / 2, 0.26, 0.2)
        for j, p in enumerate(chord):
            ev.append((t0, 'vibraphone_bowed' if j else 'violas', p, t1 - t0 + 0.3, pad_vel, (-0.3, 0.3, 0.0)[j]))
        if motif:
            k = 0
            while t0 + k * B / 2 < t1 - 1e-6:
                ev.append((t0 + k * B / 2, 'marimba', MOTIF[c][k % 4], 0.45, motif_vel * (1 - 0.08 * (k % 4)), 0.3))
                k += 1


# ---- 1 hook: one bowed chord breathes in, a bell on the brackets, a low note on "kushton" ----
swell('vibraphone_bowed', 'A3', 0.0, 1.8, 0.05, 0.45, -0.2)
swell('vibraphone_bowed', 'E4', 0.0, 1.8, 0.05, 0.4, 0.2)
swell('vibraphone_bowed', 'B4', 0.1, 1.7, 0.05, 0.3, 0.0)
ev += [(times('bracket')[0], 'glockenspiel', 'E7', 0.8, 0.3, 0.3),
       (times('accent')[0], 'contrabass_pizz', 'A1', 1.0, 0.7, 0.0), (times('accent')[0], 'marimba', 'E5', 0.6, 0.5, 0.2)]

# ---- 2-6 the leak: an A minor pulse from the stopwatch on; low pops for the three losses ----
section([(ws(2), ws(5), 'Am'), (ws(5), ws(9), 'F'), (ws(9), ws(16), 'C'), (ws(16), ws(19), 'G'),
         (ws(19), ws(22), 'Am'), (ws(22), ws(25), 'F'), (ws(25), ws(27), 'G')], motif_vel=0.24)
for t in times('hex'):
    ev += [(t, 'timpani', 'A2', 1.0, 0.45, 0.0), (t, 'marimba', 'A3', 0.6, 0.5, -0.2)]
ev.append((first('ding'), 'glockenspiel', 'A6', 1.2, 0.4, 0.2))

# ---- 7 the noise: tension, sixteenths on the strings, the crowd thickens ----
t0, t1 = ws(27), first('hush')
section([(t0, ws(32), 'Dm'), (ws(32), t1, 'E')], motif_vel=0.3, bass_vel=0.6)
pulse('violins_spic', ['E5', 'E5', 'F5', 'E5'], ws(28), t1, B / 4, 0.3, 0.3)
pulse('violas_pizz', ['B3', 'G#3'], ws(32), t1, B / 4, 0.28, -0.3)
swell('violins_trem', 'G#4', ws(32), t1 - ws(32), 0.1, 0.55, -0.2)

# ---- 8 "nuk janë më të zhurmshme": the planned silence; one low note and air ----
hush = first('hush')
ev.append((hush + 0.05, 'upright', 'A2', 2.6, 0.35, 0.0))
swell('vibraphone_bowed', 'E4', ws(39), ws(44) - ws(39), 0.05, 0.25, 0.1)

# ---- 9-10 the pills: C major, bright and light; a harp note climbs with every pill ----
section([(ws(44), ws(47), 'C'), (ws(47), ws(51), 'G'), (ws(51), ws(53), 'Am'), (ws(53), ws(55), 'F'), (ws(55), ws(60), 'G')],
        motif_vel=0.34, bass_vel=0.58, pad_vel=0.2)
for t, p in zip(times('pill'), ['C5', 'E5', 'G5', 'C6', 'E6', 'G6']):
    ev.append((t, 'harp', p, 1.2, 0.55, 0.25))
for t in np.arange(ws(44) + B, ws(60), 2 * B):
    ev.append((float(t), 'tambourine', None, 0.4, 0.14, 0.35))

# ---- 11 the payoff: strings rise under the typing, the resolve lands on "strategji" ----
res = first('resolve')
section([(ws(60), res, 'F')], motif=False, bass_vel=0.45, pad_vel=0.18)
swell('violins', 'G4', ws(60), res - ws(60), 0.08, 0.5, 0.25)
swell('violas', 'D4', ws(60), res - ws(60), 0.08, 0.45, -0.25)
for p, inst, v in [('C2', 'contrabass', 0.6), ('C3', 'cellos', 0.55), ('G3', 'violas', 0.5), ('E4', 'violins', 0.45), ('C5', 'violins', 0.4)]:
    swell(inst, p, res, 3.2, v, 0.06, 0.0)
for i, p in enumerate(['C4', 'E4', 'G4', 'C5', 'E5', 'G5', 'C6']):
    ev.append((res + i * 0.04, 'harp', p, 2.0, 0.5, -0.3 + 0.1 * i))
ev += [(res, 'timpani', 'C3', 1.5, 0.5, 0.0), (res, 'glockenspiel', 'C7', 1.2, 0.35, 0.3)]

# ---- 12 the offer: light and quiet under the voice ----
section([(ws(67), ws(69), 'F'), (ws(69), ws(73), 'G'), (ws(73), first('sting'), 'C')], motif_vel=0.22, bass_vel=0.45, pad_vel=0.18)
ev.append((times('pop')[-1], 'glockenspiel', 'E6', 0.8, 0.3, 0.3))

# ---- 13 sting: three notes up, the final chord, a clean tail ----
st = first('sting')
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
for t in times('focus') + times('whoosh'):
    add(fx, X.lp(X.whoosh(0.35, 0.45), 7000), t - 0.12, 0.35, 0.2)
for t in times('bracket'):
    add(fx, X.lp(X.click(1.3, 0.5), 6000), t + 0.05, 0.35, 0.25)
for t in times('tick'):
    add(fx, X.lp(X.click(1.8, 0.6), 7000), t, 0.45, -0.2)
for t in times('pop') + times('pill'):
    add(fx, X.lp(X.pop(0.45), 6000), t, 0.3, 0.15)
for t in times('key'):
    add(fx, X.lp(X.click(1.1, 0.35), 5000), t, 0.22, 0.25)
add(fx, X.lp(X.whoosh(0.45, 0.6), 5000), first('marker'), 0.35, 0.1)
add(fx, X.thump(0.4, 60), first('sting') + 0.33, 0.4, 0.0)
fx[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)[:, None]

for name, x in (('music', music), ('sfx', fx)):
    peak = np.abs(x).max()
    sf.write(os.path.join(HERE, name + '.wav'), (x / max(peak, 1e-9) * 0.89).astype(np.float32), SR, subtype='PCM_24')
    print(name, f'{len(x) / SR:.2f} s, peak before normalise {20 * np.log10(peak + 1e-9):.1f} dBFS')
