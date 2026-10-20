# Score and effects for StraightScale film 04 "One message, all the way". No voice. Every ball contact is a note:
# the melody IS the hits, read from audio/events.json (exported from the film by tools/events.mjs), never retyped.
# Real CC0 instrument samples (VSCO 2 CE, VCSL) through the Lemo-Opuscar sampler, plus procedural foley.
#   ~/lemo/.venv/bin/python audio/score.py   ->  audio/music.wav, audio/sfx.wav (48 kHz stereo, unmastered)
# Harmony: D minor -> C on the first run, which asks for F on the downbeat at 4.0; instead the ball falls and the music
# stops (planned silence 4.0-6.5). The rebuilt plate is the first sound after the silence. The replay repeats the first
# phrase; at Reply the missing note finally plays and F major lands on the downbeat with the full beat. The tube ride
# climbs with the ball (pitch follows height), a plagal Bb -> F cadence lands with the ball in the cradle, and the end
# card's C bar leads straight back into the opening D minor bar, so the loop has no seam.
# v2 (independent review r1): 25 s loop (F, C after the landing instead of F, Dm, C); station notes +2.5 dB over the
# pegs (they are the hits that matter); hatch, flipper-arming and flight-home foley; room tone in the silence (mix.py).
import json, os, sys
import numpy as np, soundfile as sf

sys.path.insert(0, os.path.expanduser('~/lemo/core/audio'))
import sampler as S, sfx as X

HERE = os.path.dirname(os.path.abspath(__file__))
EV = json.load(open(os.path.join(HERE, 'events.json')))
CU, DUR = EV['cues'], EV['duration']
SR = X.SR
N = int(round(DUR * SR))
TAIL = 3 * SR                             # rendered past the end, then wrapped onto the start: the loop has no seam
NE = N + TAIL
evs = EV['events']
of = lambda kind: [e for e in evs if e['kind'] == kind]
first = lambda kind: of(kind)[0]['t']
B = 0.5                                   # one beat at 120 BPM (grid A from 0.0, grid B from the snap at 7.0)
S.seed(4)
ev = []                                   # sampler events (t, inst, pitch, dur, vel, pan[, gain])
music, fx = np.zeros((NE, 2), np.float32), np.zeros((NE, 2), np.float32)


def add(buf, x, t, gain=1.0, pan=0.0):
    x = np.asarray(x, np.float32)
    if t < 0:
        x = x[int(round(-t * SR)):]; t = 0.0
    if x.ndim == 2:
        i = int(round(t * SR)); n = max(0, min(len(x), len(buf) - i)); buf[i:i + n] += x[:n] * gain
    else:
        X.add(buf, x, t, gain, pan)


def swell(inst, pitch, t, dur, v0, v1, pan=0.0, gain=1.0):
    x = S.note(inst, pitch, dur, max(v0, v1))
    ramp = np.linspace(v0 / max(v0, v1), v1 / max(v0, v1), len(x), dtype=np.float32)
    add(music, x * ramp, t, gain, pan)


# ---------------- harmony and beat, bar by bar ----------------
CH = {'Dm': ('D2', ['F4', 'A4', 'D5']), 'C': ('C2', ['E4', 'G4', 'C5']), 'F': ('F1', ['F4', 'A4', 'C5']),
      'Bb': ('A#1', ['F4', 'A#4', 'D5']), 'Am': ('A1', ['E4', 'A4', 'C5'])}


def bar(t0, chord, beat='light', pad=0.16, bass=0.5):
    root, notes = CH[chord]
    # bass: root on 1, fifth-ish pickup on the 'and' of 3
    ev.append((t0, 'contrabass_pizz', root, 0.7, bass, 0.0))
    ev.append((t0 + 1.0, 'contrabass_pizz', root, 0.45, bass * 0.75, 0.0))
    ev.append((t0 + 1.5, 'contrabass_pizz', S.name(S.midi(root) + 7), 0.35, bass * 0.55, 0.0))
    if pad:
        for j, p in enumerate(notes):
            ev.append((t0, 'vibraphone_bowed', p, 2.05, pad, (-0.35, 0.35, 0.0)[j]))
    if beat == 'none':
        return
    for k in range(8):                                      # hats on the eighths
        t = t0 + k * B / 2
        ev.append((t, 'hihat', 'closed', 0.12, (0.30 if k % 2 == 0 else 0.20) * (1.0 if beat == 'full' else 0.75), 0.25))
    ev.append((t0, 'cajon', 'bass', None, 0.68 if beat != 'half' else 0.55, 0.0))
    if beat in ('light', 'full'):
        ev.append((t0 + 1.0, 'cajon', 'bass', None, 0.55, 0.0))
        ev.append((t0 + 0.5, 'cajon', 'slap', None, 0.35, -0.1))
        ev.append((t0 + 1.5, 'cajon', 'slap', None, 0.38, -0.1))
    if beat == 'full':
        ev.append((t0 + 0.75, 'cajon', 'bass', None, 0.42, 0.0))
        ev.append((t0 + 1.75, 'cajon', 'bass', None, 0.38, 0.0))
        for b_ in (0.5, 1.5):
            ev.append((t0 + b_, 'claps', 'group', None, 0.42, 0.0))
        for k in range(16):
            ev.append((t0 + k * B / 4, 'shaker', 'down' if k % 2 == 0 else 'up', None, 0.16 + 0.06 * (k % 4 == 2), 0.4))


# pass 1 (0-4): D minor, C ... the F never comes
bar(0.0, 'Dm', 'light'); bar(2.0, 'C', 'light')
# rebuild (7-9): light returns on a bowed F swell, then a quiet F bar with no drums
for p, pan in [('F3', -0.3), ('A3', 0.3), ('C4', 0.0)]:
    swell('vibraphone_bowed', p, CU['light'], CU['snap'] - CU['light'] + 0.1, 0.02, 0.22, pan)
bar(7.0, 'F', 'none', pad=0.14, bass=0.55)
# replay (9-13): the same first phrase, a touch fuller
bar(9.0, 'Dm', 'light', pad=0.17); bar(11.0, 'C', 'light', pad=0.18)
# Reply lands: F on the downbeat with the full beat, through the run
bar(13.0, 'F', 'full', pad=0.18, bass=0.6); bar(15.0, 'Bb', 'full', pad=0.18, bass=0.6)
# the tube ride over the map: half-time, strings carry it up
bar(17.0, 'C', 'half', pad=0.15, bass=0.5); bar(19.0, 'Bb', 'half', pad=0.15, bass=0.5)
swell('violins', 'G4', 17.0, 2.1, 0.1, 0.42, 0.25); swell('violas', 'E4', 17.0, 2.1, 0.1, 0.38, -0.25)
swell('violins', 'F4', 19.0, 2.1, 0.12, 0.45, 0.25); swell('violas', 'D4', 19.0, 2.1, 0.12, 0.4, -0.25)
swell('cellos', 'A#2', 19.0, 2.1, 0.1, 0.35, 0.0)
# home: F, then C -> straight back into the opening D minor bar (loop)
bar(21.0, 'F', 'light', pad=0.16); bar(23.0, 'C', 'light', pad=0.15)

# ---------------- the melody: one note per contact ----------------
PEG_G, ST_G = 0.89, 1.26             # v2: pegs -1 dB, stations +2 dB: station hits sit ~3 dB over the pegs
MEL = {  # pass: [notes in contact order]
    1: ['A4', 'D5', 'F5', 'E5', 'C5', 'E5'],
    2: ['A4', 'D5', 'F5', 'E5', 'C5', 'E5', 'G5', 'A5', 'C6', 'A5', 'G5', 'F5', 'D5', 'F5', 'A#5', 'D6', 'C6'],
}
hits = {1: [e for e in evs if e['kind'] in ('peg', 'station', 'hop') and e.get('pass') == 1],
        2: [e for e in evs if e['kind'] in ('peg', 'station', 'hop') and e.get('pass') == 2]}
for ps, hs in hits.items():
    assert len(hs) == len(MEL[ps]), (ps, len(hs))
    for e, p in zip(hs, MEL[ps]):
        t, pan, v = e['t'], e.get('x', 0.0) * 0.6, min(1.0, e.get('v', 1500) / 1900)
        if e['kind'] == 'peg':
            ev.append((t, 'marimba', p, 0.5, 0.46 + 0.16 * v, pan, PEG_G))
            ev.append((t, 'xylophone', S.name(S.midi(p) + 12), 0.25, 0.12 * v, pan, PEG_G))
        elif e['kind'] == 'hop':
            ev.append((t, 'marimba', p, 0.4, 0.45, pan, PEG_G))
        else:  # a station lights: glockenspiel + vibraphone, the plate's own voice (v2: the loudest hits)
            ev.append((t, 'glockenspiel', S.name(S.midi(p) + 12), 1.0, 0.42 + 0.15 * v, pan, ST_G))
            ev.append((t, 'vibraphone', p, 1.1, 0.5, pan, ST_G))
            if e['id'] == 'reminder':      # the reminder is a bell
                ev.append((t, 'tubular_bells', 'F4', 1.6, 0.45, pan))
            if e['id'] == 'reply' and ps == 2:   # the note that was missing: bigger
                ev.append((t, 'harp', 'G4', 1.5, 0.5, -0.2)); ev.append((t, 'harp', 'D5', 1.5, 0.42, 0.2))
                ev.append((t, 'timpani', 'C3', 1.0, 0.36, 0.0))
# the downbeat after Reply (13.0): F lands
ev += [(13.0, 'timpani', 'F2', 1.4, 0.45, 0.0), (13.0, 'harp', 'F3', 1.6, 0.5, -0.3), (13.0, 'harp', 'C4', 1.6, 0.45, 0.3)]
# flipper launches
for e in of('kick'):
    ev.append((e['t'], 'marimba', 'D4', 0.4, 0.42, e['x'] * 0.6))
# the tube ride: a harp line that climbs with the ball (pitch follows height), one note per eighth
SCALE = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'A#4', 'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'A#5']
enter, land = CU['enter'], CU['land']
k = 0
t = 17.5
while t < land - 0.2:
    ev.append((t, 'harp', SCALE[min(len(SCALE) - 1, k // 1)], 0.8, 0.32 + 0.02 * min(k, 10), -0.4 + 0.05 * k))
    k += 1; t += B
# landing in the cradle on the downbeat: a plain cadence, no shimmer
ev += [(land, 'marimba', 'F4', 0.8, 0.6, -0.2), (land, 'marimba', 'A4', 0.8, 0.5, -0.2), (land, 'marimba', 'C5', 0.8, 0.5, -0.2),
       (land, 'harp', 'F2', 2.0, 0.55, 0.0), (land, 'vibraphone', 'F5', 1.4, 0.38, 0.0)]
# end: small taps (the ball waiting, each sends a pulse down the lit path) and a quiet two-note motif per bar
TAPN = {22.0: ('A4', 'C5'), 23.0: ('G4', 'C5'), 23.5: ('C5', 'E5')}
for e in of('tap'):
    a_, b_ = TAPN.get(round(e['t'], 2), ('A4', 'D5'))
    ev.append((e['t'], 'marimba', a_, 0.4, 0.45, -0.3)); ev.append((e['t'] + 0.13, 'marimba', b_, 0.4, 0.35, -0.3))
for t0, a_, b_ in [(22.0, 'C5', 'A4'), (24.0, 'E5', 'G4')]:
    ev.append((t0, 'vibraphone', a_, 0.9, 0.3, 0.3)); ev.append((t0 + 0.5, 'vibraphone', b_, 0.9, 0.25, 0.3))

music += S.render(ev, DUR + TAIL / SR, master=False)[:NE]
music = S.room(music, size=0.38, mix=0.16)


def wrap(x):
    y = x[:N].copy(); y[:TAIL] += x[N:N + TAIL]; return y


music = wrap(music)

# ---------------- the planned silence: everything stops on the downbeat where F should have been ----------------
cut, light = CU['cut'], CU['light']
g = np.ones(N, np.float32)
i0, i1 = int(cut * SR), int((cut + 0.025) * SR)
g[i0:i1] = np.linspace(1, 0, i1 - i0); g[i1:int(light * SR)] = 0.0
music *= g[:, None]

# ---------------- foley: one shared space, sparser than the picture ----------------
for e in evs:
    t, pan = e['t'], e.get('x', 0.0) * 0.7
    if e['kind'] == 'peg':
        add(fx, X.lp(X.click(2.2, 0.55), 6500), t, 0.14, pan)          # brass peg: a bright tink
    elif e['kind'] in ('station', 'hop'):
        add(fx, X.lp(X.clack(0.9, 0.6), 5000), t, 0.2 if e['kind'] == 'station' else 0.12, pan)  # stone plate
    elif e['kind'] == 'kick':
        add(fx, X.lp(X.clack(1.3, 0.7), 7000), t - 0.01, 0.36, pan)
add(fx, X.lp(X.whoosh(0.5, 0.7), 4200), first('miss') + 0.02, 0.32, 0.1)        # the fall
add(fx, X.lp(X.thump(0.5, 52), 900), first('gone'), 0.22, 0.0)                  # far away, in the dark
add(fx, X.lp(X.whoosh(0.2, 0.5), 6000), first('slide') - 0.02, 0.28, 0.4)       # the plate slides in
add(fx, X.lp(X.clack(1.1, 0.9), 7000), first('snap'), 0.5, 0.15)                # it locks: first sound after the silence
add(fx, X.lp(X.click(1.6, 0.7), 8000), first('snap') + 0.035, 0.32, 0.25)
add(fx, X.lp(X.click(1.5, 0.6), 8000), first('lock'), 0.32, -0.15)
add(fx, X.lp(X.whoosh(0.6, 0.6), 5000), first('whip') - 0.05, 0.36, -0.1)       # whip back to the top
# the tube: a soft roll that follows the ball's speed (fast entry, slows to the cradle)
tt = np.arange(int((land - enter) * SR)) / SR
spd = np.clip(1.0 - tt / (land - enter), 0, 1) ** 1.6
roll = X.bp(X.noise(len(tt) / SR), 300, 2600) * (0.25 + 0.75 * spd) * np.minimum(1, tt / 0.05)
add(fx, roll.astype(np.float32), enter, 0.07, -0.5)
add(fx, X.lp(X.click(1.2, 0.6), 6000), land, 0.34, -0.3)
for e in of('tap'):
    add(fx, X.lp(X.click(1.4, 0.4), 6000), e['t'], 0.18, -0.3); add(fx, X.lp(X.click(1.4, 0.35), 6000), e['t'] + 0.26, 0.14, -0.3)
# v2: the camera flies home; the hatch opens on the landing and closes as the flipper arms (stone leaves, brass stops)
add(fx, X.lp(X.whoosh(0.7, 0.45), 3500), first('home') + 0.05, 0.22, -0.2)
for kind, pan_ in (('hatch_open', 0.15), ('hatch_close', 0.15)):
    t0 = first(kind)
    add(fx, X.lp(X.bp(X.noise(0.32), 250, 2200) * np.hanning(int(round(0.32 * SR))), 2600), t0, 0.06, pan_)   # marble sliding
    add(fx, X.lp(X.clack(1.25 if kind == 'hatch_open' else 1.1, 0.6), 6500), t0 + (0.28 if kind == 'hatch_open' else 0.24), 0.2, pan_)
add(fx, X.lp(X.click(1.8, 0.5), 7000), first('cock'), 0.18, -0.35); add(fx, X.lp(X.click(2.1, 0.4), 7000), first('cock') + 0.06, 0.12, -0.35)
fx = wrap(S.room(fx, size=0.38, mix=0.1))
# keep the silence clean (effects in the dark: only the fall's tail and the far thump)
gf = np.ones(N, np.float32)
j0 = int((first('gone') + 0.9) * SR); gf[j0:int(light * SR)] = 0.0
k0 = int((first('gone') + 0.6) * SR); gf[k0:j0] = np.linspace(1, 0, j0 - k0)
fx *= gf[:, None]

for name, x in (('music', music), ('sfx', fx)):
    peak = float(np.abs(x).max())
    if peak > 0.98:
        x = x * (0.98 / peak)
    sf.write(os.path.join(HERE, f'{name}.wav'), x.astype(np.float32), SR, subtype='FLOAT')
    print(name, 'peak', round(peak, 3), 'len', round(len(x) / SR, 3))

used = sorted({e[1] for e in ev} | {'violins', 'violas', 'cellos'})
open(os.path.join(HERE, 'instruments_used.txt'), 'w').write('\n'.join(used) + '\n\n' + '\n'.join(S.credits(used)) + '\n')
print('instruments:', ', '.join(used))
