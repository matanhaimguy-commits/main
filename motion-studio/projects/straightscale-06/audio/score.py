# Score and effects for StraightScale film 06 "The 108-hour week". No voice. Calm upright piano (felt-softened) and
# strings from real CC0 samples (VS Chamber Orchestra 2 CE through the Lemo-Opuscar sampler), effects synthesized here.
# Every cue time comes from audio/events.json, exported from the film itself (tools/events.mjs), never retyped.
#   ~/lemo/.venv/bin/python audio/score.py   ->  audio/music.wav, audio/sfx.wav, audio/mix_raw.wav (48 kHz stereo)
#
# The film's clock IS the bar line: 90 BPM, one day = one 2/4 bar, every closing (19:00) lands on a downbeat.
#   Week (0-9.9 s):   A minor ostinato, one chord per day: Am F C G Am F, then Dm under the weekend climb.
#                     A soft clock tick on every third hour (16th notes), a low pulse on every step up (each closing),
#                     a soft glockenspiel "message" ping for each bubble (unresolved 2nd/7th degrees: a question).
#                     Strings enter Wednesday and build to the landing. The last hours slow down: their ticks become
#                     a rising piano run (harmonic minor) that lands on E major with the 108.
#   Silence 1:        after the landing the music stops; the rest is a real rest.
#   Math (11.2 s):    three chords, one per line: Am, F, E (low pulse with "Closed 108.").
#   Silence 2:        a short breath, then the turn.
#   Answers (13.6 s): C major. Each answered bubble is a harp note rising in C pentatonic: the answer to the pings.
#   CTA (17.6 s):     F, G on the square's hop, C major with a low pulse when the logo opens. Strings release, end.
import json, os, sys
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

sys.path.insert(0, os.path.expanduser('~/lemo/core/audio'))
import sampler as S, sfx as X

HERE = os.path.dirname(os.path.abspath(__file__))
EV = json.load(open(os.path.join(HERE, 'events.json')))
CU, DUR, evs = EV['cues'], EV['duration'], EV['events']
SR = X.SR
N = int(round(DUR * SR))
of = lambda kind: [e for e in evs if e['kind'] == kind]
BEAT = 60 / 90
S.seed(6)
X._rng = np.random.default_rng(6)          # seeded foley noise: the same mix every build
rng = np.random.default_rng(16)
music, fx = np.zeros((N, 2), np.float32), np.zeros((N, 2), np.float32)
used = set()


def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x).astype(np.float32)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x).astype(np.float32)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'band', fs=SR, output='sos'), x).astype(np.float32)


def put(buf, x, t, gain=1.0, pan=0.0):
    X.add(buf, np.asarray(x, np.float32), t, gain, float(np.clip(pan, -1, 1)))


def piano(t, pitch, dur, vel, pan=0.0, gain=1.0):
    """upright piano softened toward a felt piano: low velocity, low-passed, a touch of attack rounding"""
    used.add('upright')
    x = S.note('upright', pitch, dur, vel)
    x = lp(x, 2600 + 1800 * vel)
    a = int(0.004 * SR); x[:a] *= np.linspace(0, 1, a)
    put(music, x, t, gain, pan)


def chord(t, pitches, dur, vel, spread=0.018, gain=1.0):
    for i, p in enumerate(pitches):
        piano(t + i * spread, p, dur, vel * (0.92 if i else 1.0), (-0.25 + 0.5 * i / max(1, len(pitches) - 1)), gain)


def strings(inst, t, pitch, dur, vel, pan=0.0, attack=0.35, release=0.8, gain=1.0):
    used.add(inst)
    x = S.note(inst, pitch, dur, vel, release=release, attack=attack)
    put(music, x, t, gain, pan)


def pulse(t, f, v=1.0, pan=0.0):
    """the low pulse when the line steps up: a sine with 2nd/3rd harmonics (audible on phones), soft saturation"""
    d = 0.9; tt = np.arange(int(d * SR)) / SR
    env = np.minimum(1, tt / 0.008) * np.exp(-tt / 0.2)
    x = np.tanh(1.6 * (np.sin(2 * np.pi * f * tt) + 0.35 * np.sin(2 * np.pi * 2 * f * tt) + 0.12 * np.sin(2 * np.pi * 3 * f * tt))) * env
    put(fx, x.astype(np.float32), t, 0.22 * v, pan)


def tick(t, v=0.5, pan=0.0):
    """a soft clock tick: a bright noise transient with a short wooden resonance"""
    d = 0.045; tt = np.arange(int(d * SR)) / SR
    p = 1.0 + 0.06 * rng.standard_normal()
    x = hp(rng.standard_normal(len(tt)).astype(np.float32), 2200) * np.exp(-tt / 0.0025)
    x = x + 0.5 * np.sin(2 * np.pi * 1850 * p * tt) * np.exp(-tt / 0.007) + 0.35 * np.sin(2 * np.pi * 620 * p * tt) * np.exp(-tt / 0.012)
    x = lp(x / (np.abs(x).max() + 1e-9), 7000)
    put(fx, x.astype(np.float32), t, 0.085 * v * (0.85 + 0.3 * rng.random()), pan)


def air(t, d, v=1.0, pan0=0.0, pan1=0.0):
    """a soft air whoosh (filtered noise sweep), panned with the motion"""
    x = X.whoosh(d, 1.0).astype(np.float32)
    x = lp(x, 5000)
    h = len(x) // 2
    put(fx, x[:h], t, 0.09 * v, pan0); put(fx, x[h:], t + h / SR, 0.09 * v, pan1)


def key(t, v=1.0):
    d = 0.04; tt = np.arange(int(d * SR)) / SR
    x = hp(rng.standard_normal(len(tt)).astype(np.float32), 1500) * np.exp(-tt / 0.003) + 0.6 * np.sin(2 * np.pi * 900 * tt) * np.exp(-tt / 0.006)
    x = lp(x / (np.abs(x).max() + 1e-9), 6000)
    put(fx, x.astype(np.float32), t, 0.07 * v * (0.8 + 0.4 * rng.random()), -0.1)


xpan = lambda e: (e.get('x', 0.5) - 0.5) * 1.2

# ---------------- the week: one chord per day bar ----------------
steps = sorted(of('step'), key=lambda e: e['t'])
DAYCH = [('A2', ['C4', 'E4', 'A4']), ('F2', ['C4', 'F4', 'A4']), ('C3', ['E4', 'G4', 'C5']),
         ('G2', ['D4', 'G4', 'B4']), ('A2', ['C4', 'E4', 'A4']), ('F2', ['C4', 'F4', 'A4'])]
FIG = [0, 2, 1, 2]                                   # broken-chord figure in eighths: low, top, middle, top
piano(0.0, 'E5', 1.2, 0.42, 0.2)                     # a single soft note on the very first frame
piano(0.0, 'A3', 1.0, 0.36, -0.2)
for k, e in enumerate(steps):
    t0 = e['t']
    bass, ch = DAYCH[k] if k < len(DAYCH) else ('D3', ['D4', 'F4', 'A4'])
    if k == 5:
        bass, ch = 'F2', ['C4', 'F4', 'A4']
    piano(t0, bass, 1.3, 0.34, -0.3)
    piano(t0, S.name(S.midi(bass) + 12), 1.3, 0.22, -0.3)
    for j, idx in enumerate(FIG):
        piano(t0 + j * BEAT / 2, ch[idx], 0.55, 0.29 + 0.05 * (j == 0), 0.15 * (idx - 1))
    if k < 3:   # Monday to Wednesday: a very soft held cello under the bar, growing day by day (the full strings come later)
        strings('cellos', t0, bass if S.midi(bass) >= 43 else S.name(S.midi(bass) + 12), 1.4, 0.16 + 0.06 * k, -0.25, attack=0.25, release=0.5)
    used.add('cellos_pizz'); put(music, S.note('cellos_pizz', bass, 0.6, 0.55), t0, 0.7, -0.1)
    pulse(t0, S.hz(bass) / (2 if S.hz(bass) > 80 else 1), 1.15 if e.get('weekend') else 0.85, xpan(e))
# Sunday bar (Sat 19:00 + one day = the first downbeat of the slowdown): D minor under the climb
t_sun = steps[-1]['t'] + 2 * BEAT
piano(t_sun, 'D3', 1.4, 0.36, -0.3); piano(t_sun, 'D2', 1.4, 0.26, -0.3)
for j, idx in enumerate(FIG[:2]):
    piano(t_sun + j * BEAT / 2, ['D4', 'F4', 'A4'][idx], 0.5, 0.25, 0.15 * (idx - 1))
# strings enter Wednesday and build through the weekend
w = steps[2]['t']
strings('violas', w, 'E4', steps[4]['t'] - w + 0.3, 0.32, 0.25, attack=0.6)
strings('violas', steps[4]['t'], 'E4', CU['land'] - steps[4]['t'] - 0.12, 0.34, 0.25, attack=0.2, release=0.12)
strings('cellos', steps[3]['t'], 'G2', steps[4]['t'] - steps[3]['t'] + 0.2, 0.36, -0.25, attack=0.5)
strings('cellos', steps[4]['t'], 'A2', steps[5]['t'] - steps[4]['t'] + 0.2, 0.40, -0.25, attack=0.2)
strings('cellos', steps[5]['t'], 'F2', t_sun - steps[5]['t'] + 0.2, 0.46, -0.25, attack=0.2)
strings('cellos', t_sun, 'D3', CU['land'] - t_sun - 0.12, 0.44, -0.25, attack=0.15, release=0.12)
strings('violins', steps[5]['t'], 'A4', t_sun - steps[5]['t'] + 0.2, 0.30, 0.35, attack=0.7)
strings('violins', t_sun, 'A4', CU['land'] - t_sun - 0.12, 0.34, 0.35, attack=0.3, release=0.12)   # a breath before the hit

# ---------------- the counter: ticks on the 16ths, then the slowdown ticks become a rising run ----------------
ticks = of('tick')
slow = [e for e in ticks if e['t'] >= t_sun - 1e-3 and e['t'] < CU['land'] - 1e-3]
RUN = ['A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G#5'][-len(slow):] if slow else []
for e in ticks:
    if e['t'] >= CU['land'] - 1e-3:
        continue
    tick(e['t'], 0.6 if e in slow else 0.45, xpan(e))
for e, p in zip(slow, RUN):
    piano(e['t'], p, 0.6, 0.30, 0.25)

# ---------------- the messages: a soft ping for each bubble, an answer for each one later ----------------
PING = ['B5', 'D6', 'B5', 'F6', 'D6', 'B5', 'D6', 'F6', 'B5']
for e in of('bubble'):
    used.add('glockenspiel')
    put(fx, S.note('glockenspiel', PING[e['i'] % len(PING)], 0.5, 0.22), e['t'], 0.32, xpan(e))
ANS = ['C5', 'D5', 'E5', 'G5', 'A5', 'C6', 'D6', 'E6', 'G6']
for e in of('answer'):
    used.add('harp')
    put(music, S.note('harp', ANS[e['i'] % len(ANS)], 1.4, 0.5), e['t'], 0.85, xpan(e))

# ---------------- landing: E major on the 108, then the first real silence ----------------
L = CU['land']
pulse(L, S.hz('E1') * 2, 1.7)
chord(L, ['E3', 'G#3', 'B3', 'E4', 'G#4'], 0.9, 0.52)
piano(L, 'E2', 1.0, 0.36, -0.3)
strings('cellos', L, 'E3', 0.35, 0.5, -0.25, attack=0.02, release=0.5)
strings('violas', L, 'B3', 0.35, 0.45, 0.25, attack=0.02, release=0.5)
strings('violins', L, 'G#4', 0.35, 0.40, 0.35, attack=0.02, release=0.5)
tick(L, 1.0)

# ---------------- the math: one chord per line ----------------
m1, m2, m3 = [e['t'] for e in sorted(of('math'), key=lambda e: e['t'])]
air(m1, 0.55, 0.7, -0.6, 0.6)                          # the sweep along the time axis
chord(m1, ['C4', 'E4', 'A4'], 0.7, 0.30); piano(m1, 'A2', 0.8, 0.30, -0.3)
chord(m2, ['C4', 'F4', 'A4'], 0.7, 0.30); piano(m2, 'F2', 0.8, 0.30, -0.3)
chord(m3, ['B3', 'E4', 'G#4'], 0.55, 0.36); piano(m3, 'E2', 0.6, 0.34, -0.3)
pulse(m3, S.hz('E2'), 1.1)
air(m3 + 0.05, 0.5, 0.5, 0.6, -0.3)                    # the 108 drops and slides into its sentence

# ---------------- the turn: C major, answers ----------------
s_in = CU['sysIn']
for t0, b, ch, d in [(s_in, 'C3', ['E4', 'G4', 'C5'], CU['list3'] - s_in),
                     (CU['list3'], 'F2', ['C4', 'F4', 'A4'], 1.333),
                     (CU['list3'] + 4 * BEAT / 2 * 1.0, 'A2', ['C4', 'E4', 'A4'], CU['cta'] - CU['list3'] - 4 * BEAT / 2)]:
    piano(t0, b, d + 0.3, 0.32, -0.3)
    for j in range(int(round(d / (BEAT / 2)))):
        piano(t0 + j * BEAT / 2, ch[FIG[j % 4]], 0.5, 0.22 + 0.04 * (j % 4 == 0), 0.15 * (FIG[j % 4] - 1))
chord(s_in, ['E4', 'G4', 'C5'], 1.2, 0.40)   # the turn arrives: C major
strings('cellos', s_in, 'C3', CU['list3'] - s_in + 0.2, 0.44, -0.25, attack=0.08)
strings('cellos', CU['list3'], 'F2', 1.4, 0.40, -0.25, attack=0.2)
strings('cellos', CU['list3'] + 1.333, 'A2', CU['cta'] - CU['list3'] - 1.333, 0.36, -0.25, attack=0.2)
strings('violas', s_in, 'G3', CU['sweep1'] - s_in + 0.2, 0.34, 0.25, attack=0.5, release=1.0)
strings('violins', CU['list1'], 'E5', CU['sweep1'] - CU['list1'] + 0.2, 0.30, 0.35, attack=0.8, release=1.0)
strings('violas', CU['sweep1'] + 0.2, 'A3', CU['cta'] - CU['sweep1'] - 0.2, 0.2, 0.25, attack=0.6)   # the rest: quieter

# ---------------- call to action and the logo ----------------
c = CU['cta']
air(c, 0.45, 0.6, 0.5, -0.2)                           # the chart folds, the square flies to the caret
piano(c, 'F2', 1.3, 0.38, -0.3); chord(c, ['C4', 'F4', 'A4'], 1.2, 0.38)
strings('cellos', c, 'F2', CU['hop'] - c + 0.1, 0.38, -0.25, attack=0.2)
strings('violas', c, 'A3', CU['hop'] - c + 0.1, 0.32, 0.25, attack=0.3)
for e in of('key'):
    if e['i'] % 2 == 0 or e['i'] == 7:
        key(e['t'], 1.0)
h = CU['hop']                                         # v2: the square goes the long way round (right, down, in under the copy)
air(h, CU['logo'] - h, 0.5, 0.45, -0.4)               # so the whoosh lasts the whole hop and pans with it
hg = CU['logo'] - BEAT / 2                            # the G chord stays on the eighth-note grid, mid-flight
piano(hg, 'G2', 0.4, 0.32, -0.3); chord(hg, ['B3', 'D4', 'G4'], 0.35, 0.28, spread=0.012)
lg = CU['logo']
pulse(lg, S.hz('C2'), 1.2)
piano(lg, 'C2', 3.5, 0.40, -0.3); piano(lg, 'C3', 3.5, 0.30, -0.3)
chord(lg, ['E4', 'G4', 'C5', 'E5'], 3.2, 0.34, spread=0.025)
piano(lg + 2 * BEAT, 'G5', 2.5, 0.20, 0.3)
# v2: the gold rule under ANALIZA gets a cue that reads over the held chord: the tonic C6 on piano, doubled by the
# glockenspiel that rang the unanswered message pings (B, D, F) earlier, now resolved
u_t = CU['under']
piano(u_t, 'C6', 2.8, 0.34, 0.35)
put(fx, S.note('glockenspiel', 'C6', 0.9, 0.34), u_t, 0.55, 0.25)
strings('cellos', lg, 'C3', 2.6, 0.42, -0.25, attack=0.05, release=1.6)
strings('violas', lg, 'G3', 2.6, 0.36, 0.25, attack=0.05, release=1.6)
strings('violins', lg, 'E4', 2.6, 0.32, 0.35, attack=0.05, release=1.6)

# ---------------- one shared room, mix, safety ----------------
music = S.room(music, size=0.42, mix=0.22)
fx = S.room(fx, size=0.42, mix=0.12)
fade = np.ones(N, np.float32); fl = int(0.6 * SR); fade[-fl:] = np.linspace(1, 0, fl) ** 2   # nothing rings past the cut
music *= fade[:, None]; fx *= fade[:, None]
mix = music * 0.9 + fx * 1.0
mix = np.stack([lp(mix[:, c], 16000, o=8) for c in range(2)], axis=1)    # v2: remove the 17.4 kHz sampler line
pk = np.abs(mix).max()
print(f'peak before scale {pk:.3f}')
sc = 0.89 / pk
sf.write(os.path.join(HERE, 'music.wav'), music * sc, SR, subtype='PCM_24')
sf.write(os.path.join(HERE, 'sfx.wav'), fx * sc, SR, subtype='PCM_24')
sf.write(os.path.join(HERE, 'mix_raw.wav'), mix * sc, SR, subtype='PCM_24')
open(os.path.join(HERE, 'instruments_used.txt'), 'w').write('\n'.join(sorted(used)) + '\n\n' + '\n'.join(S.credits(sorted(used))) + '\n')
print('instruments:', ', '.join(sorted(used)))
print('\n'.join(S.credits(sorted(used))))
