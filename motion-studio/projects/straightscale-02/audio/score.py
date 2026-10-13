# Score and effects for StraightScale reel 02, from real CC0 instrument samples (VSCO 2 CE, VCSL) via the
# Lemo-Opuscar sampler, plus procedural foley. Run with the sampler's venv:
#   ~/lemo/.venv/bin/python audio/score.py   ->  audio/music.wav, audio/sfx.wav (48 kHz stereo)
# Effects are placed from audio/events.json (exported from the film by tools/events.mjs), never retyped.
# Harmony follows the story: D minor while clients leak away, D major from the moment the cold client lights up.
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
B = 0.6            # one beat at 100 BPM; sections restart their grid at story events
music, fx = np.zeros((N, 2), np.float32), np.zeros((N, 2), np.float32)
ev = []            # sampler events (t, inst, pitch, dur, vel, pan)


def add(buf, x, t, gain=1.0, pan=0.0):
    x = np.asarray(x, np.float32)
    if x.ndim == 2:  # already stereo: place as is
        i = int(round(t * SR)); n = min(len(x), len(buf) - i); buf[i:i + n] += x[:n] * gain
    else:
        X.add(buf, x, t, gain, pan)


def swell(inst, pitch, t, dur, v0, v1, pan=0.0, gain=1.0, buf=None):
    """A long note with a gain ramp (crescendo or fade), placed directly into the music bus."""
    x = S.note(inst, pitch, dur, max(v0, v1))
    ramp = np.linspace(v0 / max(v0, v1), v1 / max(v0, v1), len(x), dtype=np.float32)
    add(music if buf is None else buf, x * ramp, t, gain, pan)


def pulse(inst, notes, t0, t1, step, vel, pan=0.0):
    """Repeated notes on a grid from t0 to t1, cycling through notes."""
    i, t = 0, t0
    while t < t1 - 1e-6:
        ev.append((t, inst, notes[i % len(notes)], step * 0.9, vel * (1.0 if i % 2 == 0 else 0.82), pan))
        i, t = i + 1, t + step


def pad(chords, vel=0.3):
    """chords: [(t0, t1, [pitches])], strings (violas + cellos) held under the voice."""
    for t0, t1, ps in chords:
        for j, p in enumerate(ps):
            ev.append((t0, 'violas' if j else 'cellos', p, t1 - t0 + 0.4, vel, (-0.3, 0.3)[j % 2]))


# ---- 1 hook (0 - 4.2): D minor pulse, a falling marimba note for every client that passes ----
pulse('contrabass_pizz', ['D2'], 0.0, 1.95, B, 0.6)
pulse('contrabass_pizz', ['A#1'], 1.95, 4.2, B, 0.6)
pulse('cellos_pizz', ['D3', 'A3'], 0.0, 1.95, B / 2, 0.38, 0.2)
pulse('cellos_pizz', ['A#2', 'F3'], 1.95, 4.2, B / 2, 0.38, 0.2)
pad([(0.0, 1.95, ['D3', 'A3']), (1.95, 4.2, ['A#2', 'F3'])], 0.26)
for t, p in zip(times('whoosh'), ['A5', 'F5', 'D5', 'C5']):
    ev.append((t, 'marimba', p, 0.6, 0.55, 0.25))
for t, p in zip(times('enter'), ['F4', 'A4', 'D5']):
    ev.append((t, 'marimba', p, 0.5, 0.5, 0.35))

# ---- 2 the ride (4.2 - 6.5): sixteenths build to the exit, then everything stops ----
ride, out = first('ride'), first('exit')
pulse('cellos_spic', ['A#2', 'A#2', 'F3', 'A#2'], ride, ride + 1.2, B / 4, 0.42)
pulse('cellos_spic', ['C3', 'C3', 'G3', 'C3'], ride + 1.2, out, B / 4, 0.5)
pulse('contrabass_pizz', ['A#1'], ride, ride + 1.2, B / 2, 0.6)
pulse('contrabass_pizz', ['C2'], ride + 1.2, out, B / 2, 0.66)
swell('violins_trem', 'A4', ride, out - ride, 0.12, 0.7, 0.2)
swell('violas', 'E4', ride + 0.6, out - ride - 0.6, 0.1, 0.5, -0.25)
ev += [(out + 0.04, 'marimba', 'A4', 0.8, 0.5, -0.3), (out + 0.36, 'marimba', 'F4', 0.8, 0.4, -0.35),
       (out + 0.68, 'marimba', 'D4', 1.0, 0.32, -0.4)]
swell('cellos', 'D2', out, 3.6, 0.35, 0.05, 0.0, 0.8)

# ---- 3 the rest (7.08 - 10.3): one bowed chord, nothing moves ----
swell('vibraphone_bowed', 'A#3', 7.1, 3.3, 0.45, 0.25, -0.2)
swell('vibraphone_bowed', 'D4', 7.1, 3.3, 0.4, 0.22, 0.2)
swell('vibraphone_bowed', 'F4', 7.25, 3.15, 0.35, 0.2, 0.0)
ev.append((7.12, 'harp', 'D5', 2.0, 0.42, 0.1))

# ---- 4 return time (10.3 - 17.1): a soft pulse; each sweep climbs on the vibraphone ----
pulse('cellos_pizz', ['F2', 'C3'], 10.3, 13.9, B / 2, 0.3)
pulse('cellos_pizz', ['C2', 'G2'], 13.9, 15.1, B / 2, 0.3)
pulse('cellos_pizz', ['F2', 'C3'], 15.1, 16.0, B / 2, 0.3)
pulse('cellos_pizz', ['C2', 'G2'], 16.0, 17.1, B / 2, 0.3)
pad([(10.3, 13.9, ['F2', 'C3', 'A3']), (13.9, 15.1, ['C3', 'G3', 'E4']), (15.1, 16.0, ['F2', 'C3', 'A3']), (16.0, 17.1, ['C3', 'G3', 'E4'])], 0.22)
ev.append((first('ring'), 'glockenspiel', 'C7', 0.8, 0.3, 0.3))
for t0, step in zip(times('sweep'), (0.24, 0.15)):
    for i, p in enumerate(['F4', 'A4', 'C5', 'E5']):
        ev.append((t0 + i * step, 'vibraphone', p, 0.9, 0.42, -0.2 + 0.15 * i))

# ---- 5 the recall (17.1 - 19.6): the thread climbs on the harp; D major arrives when the client lights up ----
msg, live = first('message'), first('live')
ev.append((msg, 'harp', 'A4', 1.2, 0.5, 0.2))
for i, p in enumerate(['D4', 'F#4', 'A4', 'D5']):
    ev.append((msg + 0.45 + i * (live - msg - 0.45) / 4, 'harp', p, 1.4, 0.48, -0.1 + 0.08 * i))
for p in ['D4', 'F#4', 'A4']:
    ev.append((live, 'vibraphone', p, 2.4, 0.55, 0.0))
ev.append((live, 'glockenspiel', 'D7', 1.2, 0.35, 0.3))
pulse('cellos_pizz', ['F2', 'C3'], 17.1, live, B / 2, 0.28)
pad([(17.1, live, ['F2', 'C3', 'A3']), (live, 19.6, ['D3', 'A3', 'F#4'])], 0.26)

# ---- 6 review and referral (19.6 - 24.4): a light groove in D major ----
prog = [(19.6, 21.2, 'D'), (21.2, 22.4, 'G'), (22.4, 23.6, 'D'), (23.6, 24.4, 'A')]
ROOT = {'D': ('D2', ['D3', 'A3', 'F#4']), 'G': ('G1', ['G2', 'D3', 'B3']), 'A': ('A1', ['A2', 'E3', 'C#4']),
        'Bm': ('B1', ['B2', 'F#3', 'D4']), 'Em': ('E2', ['E3', 'B3', 'G4'])}
MOTIF = {'D': ['D5', 'F#5', 'A5', 'F#5'], 'G': ['D5', 'G5', 'B5', 'G5'], 'A': ['C#5', 'E5', 'A5', 'E5'],
         'Bm': ['D5', 'F#5', 'B5', 'F#5'], 'Em': ['E5', 'G5', 'B5', 'G5']}


def groove(prog, motif=True, motif_vel=0.32, bass_vel=0.55, pad_vel=0.24):
    for t0, t1, c in prog:
        root, chord = ROOT[c]
        pulse('contrabass_pizz', [root], t0, t1, B, bass_vel)
        pulse('cellos_pizz', [chord[0], chord[1]], t0, t1, B / 2, 0.3, 0.2)
        pad([(t0, t1, chord)], pad_vel)
        if motif:
            for i, p in enumerate(MOTIF[c]):
                if t0 + i * B / 2 < t1: ev.append((t0 + i * B / 2, 'marimba', p, 0.5, motif_vel * (1 - 0.1 * i), 0.3))


groove(prog)
ev += [(first('star'), 'glockenspiel', 'A6', 1.0, 0.45, 0.25), (first('star') + 0.08, 'glockenspiel', 'D7', 1.0, 0.35, 0.3)]
ev += [(first('friend'), 'marimba', 'F#5', 0.7, 0.45, -0.3), (first('friend'), 'marimba', 'A5', 0.7, 0.4, 0.3)]

# ---- 7 the loop (24.4 - 26.4): strings rise while the pair draws the way back; the warm chord when it closes ----
home = first('home')
swell('violins', 'A4', 24.4, home - 24.4, 0.1, 0.55, 0.25)
swell('violas', 'F#4', 24.4, home - 24.4, 0.1, 0.5, -0.25)
pulse('cellos_spic', ['D3', 'D3', 'A3', 'D3'], 24.4, home, B / 4, 0.4)
pulse('contrabass_pizz', ['D2', 'A1'], 24.4, home, B / 2, 0.6)
for i in range(int((home - 24.9) / 0.1)):
    ev.append((24.9 + i * 0.1, 'timpani', 'A2', 0.3, 0.15 + 0.35 * i / ((home - 24.9) / 0.1), 0.0))
for p, inst, v in [('D2', 'contrabass', 0.6), ('D3', 'cellos', 0.6), ('A3', 'violas', 0.55), ('F#4', 'violins', 0.5),
                   ('D5', 'violins', 0.45), ('D4', 'horn', 0.4)]:
    swell(inst, p, home, 3.4, v, 0.08, 0.0)
for i, p in enumerate(['D4', 'F#4', 'A4', 'D5', 'F#5', 'A5', 'D6']):
    ev.append((home + i * 0.045, 'harp', p, 2.0, 0.5, -0.3 + 0.1 * i))
ev += [(home, 'timpani', 'D3', 1.5, 0.55, 0.0), (home, 'marimba', 'D6', 1.0, 0.5, 0.3)]

# ---- 8 the reveal (26.4 - 29.76): the chord rings, a soft pulse, the brand sting ----
pulse('contrabass_pizz', ['D2'], home + 1.2, 28.8, B, 0.45)
pulse('cellos_pizz', ['D3', 'A3'], home + 1.2, 28.8, B / 2, 0.24)
pad([(28.8, first('brand'), ['G2', 'D3', 'B3'])], 0.22)
brand = first('brand')
ev += [(brand, 'marimba', 'A5', 0.8, 0.55, 0.2), (brand + 0.12, 'marimba', 'D6', 0.8, 0.55, 0.25),
       (brand + 0.24, 'glockenspiel', 'F#6', 1.4, 0.4, 0.3), (brand, 'contrabass_pizz', 'D2', 1.0, 0.7, 0.0)]
swell('violas', 'A3', brand, 1.2, 0.35, 0.1, -0.2)

# ---- 9 proof (music only), 10 offer (ducked), 11 CTA and the ending ----
groove([(30.9, 31.95, 'D'), (31.95, 33.0, 'G'), (33.0, 33.95, 'A')], motif_vel=0.4, bass_vel=0.62, pad_vel=0.28)
for t, p in zip(times('row'), ['D5', 'F#5', 'A5']):
    ev.append((t, 'harp', p, 1.4, 0.6, 0.2))
for t in np.arange(30.9 + B, 33.95, 2 * B):
    ev.append((float(t), 'tambourine', None, 0.4, 0.18, 0.35))
groove([(33.95, 35.15, 'Bm'), (35.15, 36.35, 'G'), (36.35, 37.5, 'D')], motif=False, bass_vel=0.5, pad_vel=0.22)
groove([(37.5, 38.7, 'G'), (38.7, 39.9, 'A')], motif=False, bass_vel=0.5, pad_vel=0.22)
land = first('land')
for t in times('key'):
    ev.append((t, 'claves', None, 0.2, 0.12, 0.3))
for p, inst, v in [('D2', 'contrabass_pizz', 0.7), ('D5', 'marimba', 0.55), ('F#5', 'marimba', 0.45), ('A5', 'marimba', 0.45),
                   ('D6', 'glockenspiel', 0.35)]:
    ev.append((land, inst, p, 1.0, v, 0.0))
for i, p in enumerate(['D3', 'A3', 'D4', 'F#4', 'A4', 'D5']):
    ev.append((land - 0.25 + i * 0.05, 'harp', p, 1.2, 0.5, -0.25 + 0.1 * i))
for p, inst in [('D3', 'cellos'), ('A3', 'violas'), ('F#4', 'violins')]:
    swell(inst, p, land - 0.25, DUR - land + 0.25, 0.4, 0.02, 0.0)

# render the sampler events, room, fade the very end
add(music, S.render(ev, DUR, master=False), 0.0)
music = S.room(music, size=0.42, mix=0.2)
fade = int(0.35 * SR)
music[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)[:, None]

# ---- effects (procedural foley) ----
for t in times('whoosh'):
    add(fx, X.whoosh(0.32, 0.5), t - 0.16, 0.5, 0.3)
for t in times('enter'):
    add(fx, X.lp(X.click(0.8, 0.5), 5000), t, 0.4, 0.4)
add(fx, X.whoosh(out - ride + 0.2, 0.8), ride, 0.45, 0.0)
add(fx, X.thump(0.6, 60), out, 0.5, -0.2)
for t in (first('ring'), msg):
    add(fx, X.lp(X.click(1.4, 0.4), 6000), t, 0.3, 0.2)
add(fx, X.pop(0.5), live, 0.3, 0.0)
add(fx, X.thump(0.5, 55), brand, 0.4, 0.0)
add(fx, X.thump(0.45, 65), land, 0.45, 0.1)
fx[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)[:, None]

for name, x in (('music', music), ('sfx', fx)):
    peak = np.abs(x).max()
    sf.write(os.path.join(HERE, name + '.wav'), (x / max(peak, 1e-9) * 0.89).astype(np.float32), SR, subtype='PCM_24')
    print(name, f'{len(x) / SR:.2f} s, peak before normalise {20 * np.log10(peak + 1e-9):.1f} dBFS')
