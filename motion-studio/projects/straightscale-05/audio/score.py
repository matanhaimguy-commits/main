# Score and sound design for StraightScale reel 05 "Three things, one system". No paid generation: real CC0 instrument
# samples (VSCO 2 CE, VCSL) through the Lemo-Opuscar sampler, plus effects synthesized here in numpy.
#   ~/lemo/.venv/bin/python audio/score.py   ->  audio/music.wav, audio/sfx.wav, audio/mix_raw.wav (+ stems report)
# Every cue comes from audio/events.json (exported from the film by tools/events.mjs), never retyped.
# Harmony follows the idea: three loose notes (A, E, B: an open A sus2 with no third) while the business runs on three
# separate things; the riser pulls them together; the ball's flight hangs on the dominant (A); the lockup resolves to
# D major add9. One shared room for music and effects; effects lead, the bed sits under them.
import json, os, sys
import numpy as np, soundfile as sf
from scipy.signal import butter, sosfilt

sys.path.insert(0, os.path.expanduser('~/lemo/core/audio'))
import sampler as S

HERE = os.path.dirname(os.path.abspath(__file__))
EV = json.load(open(os.path.join(HERE, 'events.json')))
CU, DUR, SR = EV['cues'], EV['duration'], 48000
N = int(round(DUR * SR))
times = lambda kind: [e['t'] for e in EV['events'] if e['kind'] == kind]
first = lambda kind: times(kind)[0]
S.seed(5)
R = np.random.default_rng(505)

music, fx = np.zeros((N, 2), np.float32), np.zeros((N, 2), np.float32)
ev = []   # sampler events (t, inst, pitch, dur, vel, pan)


# ---------- helpers ----------
def t_(d): return np.arange(int(round(d * SR))) / SR
def lp(x, f, o=2): return sosfilt(butter(o, f, 'low', fs=SR, output='sos'), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, 'high', fs=SR, output='sos'), x)
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], 'band', fs=SR, output='sos'), x)
def norm(x, p=1.0): m = np.abs(x).max(); return x * (p / m) if m > 0 else x


def add(buf, x, at, gain=1.0, pan=0.0):
    x = np.asarray(x, np.float32)
    s = int(round(at * SR))
    if s >= len(buf): return
    if s < 0: x = x[-s:]; s = 0
    e = min(len(buf), s + len(x))
    if x.ndim == 2:
        buf[s:e] += x[:e - s] * gain; return
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    buf[s:e, 0] += x[:e - s] * gain * l * 1.414
    buf[s:e, 1] += x[:e - s] * gain * r * 1.414


def svf_sweep(x, f0, f1, q=2.0, curve='exp'):
    """state-variable band-pass whose centre moves from f0 to f1 over the length of x (air, whooshes)"""
    n = len(x); u = np.linspace(0, 1, n)
    f = f0 * (f1 / f0) ** u if curve == 'exp' else f0 + (f1 - f0) * u
    g = 2 * np.sin(np.pi * np.minimum(f, SR / 6) / SR); damp = 1 / q
    low = band = 0.0; out = np.zeros(n)
    for i in range(n):
        high = x[i] - low - damp * band
        band += g[i] * high
        low += g[i] * band
        out[i] = band
    return out


def env_ar(n, a, r):
    e = np.ones(n); na, nr = int(a * SR), int(r * SR)
    if na: e[:na] = np.sin(np.linspace(0, np.pi / 2, na)) ** 2
    if nr: e[-nr:] *= np.cos(np.linspace(0, np.pi / 2, nr)) ** 2
    return e


def shaped(inst, pitch, t0, t1, curve, pan=0.0, gain=1.0, vel=0.6, attack=0.0, skip=0.0):
    """a sustained sampler note whose loudness follows curve(u), u = 0..1 over [t0, t1]; skip drops the sample's
    first seconds (v2: the bowed vibraphone takes about 0.5 s to speak, too slow under a question set on frame 0)"""
    x = S.note(inst, pitch, t1 - t0 + skip, vel, attack=attack)[int(skip * SR):][:int((t1 - t0) * SR)]
    u = np.linspace(0, 1, len(x))
    add(music, x * curve(u), t0, gain, pan)


# ---------- synthesized effects ----------
def bubble(f0=420, v=1.0):
    """a resonant pop: a short sine that glides up, with a soft noise onset"""
    d = 0.16; tt = t_(d)
    f = f0 * (1 + 1.4 * (1 - np.exp(-tt / 0.012)))
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.035)
    x += lp(R.standard_normal(len(tt)), 3000) * np.exp(-tt / 0.004) * 0.25
    return norm(x) * v


def sub_thump(f0=62, f1=40, d=0.6, v=1.0):
    """an impact: a low sine that drops in pitch, driven into saturation so phones hear its harmonics"""
    tt = t_(d)
    f = f1 + (f0 - f1) * np.exp(-tt / 0.06)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.14)
    x = np.tanh(2.2 * x) / np.tanh(2.2)
    x += lp(R.standard_normal(len(tt)), 900) * np.exp(-tt / 0.012) * 0.35
    return norm(lp(x, 2500)) * v


def wobble(d=0.62, v=1.0, hz=6.2, decay=5.2):
    """the jelly wobble after the merge: a soft low tone whose pitch and level follow the picture's squash"""
    tt = t_(d)
    q = np.exp(-tt * decay) * np.sin(2 * np.pi * hz * tt)
    f = 132 * (1 + 0.1 * q)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = (np.sin(ph) + 0.35 * np.sin(2 * ph) + 0.12 * np.sin(3 * ph)) * np.exp(-tt * decay * 0.8) * (0.7 + 0.3 * np.abs(q) / (np.abs(q).max() + 1e-9))
    x *= env_ar(len(tt), 0.006, 0.08)
    return norm(lp(x, 1400)) * v


def air(d, f0, f1, v=1.0, q=1.6, shape=(0.4, 0.6)):
    """a whoosh: noise through a moving band-pass, with a rise-fall envelope"""
    tt = t_(d); n = R.standard_normal(len(tt))
    x = svf_sweep(n, f0, f1, q)
    a, b = shape
    e = np.where(tt < a * d, np.sin(np.pi / 2 * tt / (a * d)) ** 2, np.cos(np.pi / 2 * (tt - a * d) / (b * d)) ** 2)
    return norm(x * e) * v


def riser(d, v=1.0):
    """into the merge: air that climbs and brightens, with a soft rising tone under it; it stops on the merge"""
    tt = t_(d); u = tt / d
    n = svf_sweep(R.standard_normal(len(tt)), 300, 6500, 2.4)
    f = 196 * (2 ** (2 * u ** 1.6))      # two octaves up, faster at the end
    ph = 2 * np.pi * np.cumsum(f) / SR
    tone = (np.sin(ph) + 0.5 * np.sin(2.003 * ph) + 0.25 * np.sin(3.01 * ph)) * 0.18
    x = (norm(n) * 0.8 + tone) * (u ** 2.2)
    x *= env_ar(len(tt), 0.0, 0.012)
    return norm(x) * v


# ---------- MUSIC ----------
merge, land, lock, rev, ex = CU['merge'], CU['land'], CU['lock'], CU['rev'], CU['exit']
spin = CU['spin']

# 1. three loose notes: a bowed bed on A3 / E4 / B4 that breathes in, crescendos with the riser, and stops on the merge
# v2: the question is on screen from frame 0, so the bed arrives faster (0.2 s, entering mid-bow) and sits 3 dB higher
# under it (0.78 vs 0.55)
# plus a further lift under the question (about +3 dB to 1.0 s, back to the base by 2.0 s, before the ticks need room)
qlift = lambda tt: 1 + 0.42 * (1 - np.clip((tt - 1.0) / 1.0, 0, 1) ** 2)
bed = lambda u, t0=0.0, t1=merge: np.minimum(1, (u * (t1 - t0)) / 0.2) ** 1.5 * qlift(u * (t1 - t0) + t0) * (0.78 + 0.22 * np.clip(((u * (t1 - t0) + t0) - spin) / (merge - spin), 0, 1) ** 2)
for p, pan in (('A3', -0.25), ('E4', 0.25), ('B4', 0.0)):
    shaped('vibraphone_bowed', p, 0.0, merge + 0.03, lambda u: bed(u) * env_ar(len(u), 0, 0.03), pan, 0.75, 0.5, skip=0.45)
shaped('cellos', 'A2', 0.2, merge + 0.03, lambda u: bed(u, 0.2) * env_ar(len(u), 0.6, 0.03), 0.0, 0.4, 0.45, attack=0.4)
# the dots appear as three notes
for t, p, pan in zip(times('pop'), ['A4', 'E5', 'B5'], [0.0, 0.35, -0.35]):
    ev.append((t, 'vibraphone', p, 1.4, 0.42, pan))
# v2: each label lands with its dot's note an octave down on the harp, softly
for t, p, e in zip(times('label'), ['A3', 'E4', 'B4'], [x for x in EV['events'] if x['kind'] == 'label']):
    ev.append((t, 'harp', p, 1.2, 0.3, max(-0.5, min(0.5, e.get('x', 0) * 0.6))))
# the spinner: each tick turns the three-note cycle one step
for t, p in zip(times('tick'), ['E5', 'B4', 'A4', 'E5']):
    ev.append((t, 'marimba', p, 0.4, 0.28, 0.15))
# the riser: strings tremolo pull the three notes together
shaped('violins_trem', 'E5', spin, merge + 0.02, lambda u: (0.05 + 0.95 * u ** 2) * env_ar(len(u), 0.05, 0.02), 0.3, 0.42, 0.55)
shaped('violins_trem', 'A4', spin, merge + 0.02, lambda u: (0.05 + 0.95 * u ** 2) * env_ar(len(u), 0.05, 0.02), -0.3, 0.38, 0.55)
# merge: one bright note, still suspended (E is the ninth of D, resolved later)
ev.append((merge, 'glockenspiel', 'E6', 1.4, 0.4, 0.0))
ev.append((merge, 'contrabass_pizz', 'A1', 1.2, 0.6, 0.0))
# landing: the dominant in the bass; the reveal brings the bed back, suspended (A D E)
ev.append((land, 'timpani', 'A2', 1.6, 0.55, 0.0))
for p, pan in (('A3', -0.2), ('D4', 0.2), ('E4', 0.0)):
    shaped('vibraphone_bowed', p, rev, lock + 0.05, lambda u: np.minimum(1, u * 6) * (0.6 + 0.4 * u) * env_ar(len(u), 0.05, 0.05), pan, 0.42, 0.45)
ev.append((CU['goldT'], 'glockenspiel', 'A6', 0.8, 0.22, 0.4))
# letters: a harp line climbs under the wordmark (every third letter)
for t, p, pan in zip(times('letter')[::3], ['D4', 'F#4', 'A4', 'D5', 'E5'], [-0.3, -0.15, 0.0, 0.15, 0.3]):
    ev.append((t, 'harp', p, 1.6, 0.42, pan))
# 2. the lockup: D major add9, strings, harp roll, vibraphone, glockenspiel
ev.append((lock, 'contrabass_pizz', 'D2', 2.0, 0.7, 0.0))
ev.append((lock, 'timpani', 'D3', 2.0, 0.42, 0.0))
for i, p in enumerate(['D3', 'A3', 'D4', 'F#4', 'A4', 'D5', 'E5', 'F#5']):
    ev.append((lock + i * 0.035, 'harp', p, 2.4, 0.5 - 0.02 * i, -0.35 + 0.1 * i))
ev += [(lock, 'vibraphone', 'F#5', 2.5, 0.38, 0.25), (lock, 'vibraphone', 'D5', 2.5, 0.36, -0.25), (lock, 'glockenspiel', 'D6', 1.6, 0.3, 0.3)]
hold_end = ex + 0.35
# v2: the pad barely decays (floor 0.85, was 0.45) so the end card does not sag to -26 dBFS
hold = lambda u, t0=lock, peak=0.6: (np.minimum(1, (u * (hold_end - t0)) / 0.25) * (0.85 + 0.15 * np.exp(-(u * (hold_end - t0)) / 3.0))) * env_ar(len(u), 0, 0.5)
for inst, p, pan, g in (('cellos', 'D3', -0.2, 0.24), ('violas', 'A3', 0.2, 0.3), ('violins', 'F#4', 0.0, 0.28), ('contrabass', 'D2', 0.0, 0.18), ('vibraphone_bowed', 'E5', 0.3, 0.22)):
    shaped(inst, p, lock, hold_end, hold, pan, g * 1.6, 0.5, attack=0.15)
# 3. the end card: one low note under "One system.", then the step motif under the call to action (a step every beat)
ev.append((CU['one'], 'harp', 'D3', 2.0, 0.42, 0.0))
ev.append((CU['cta'], 'vibraphone', 'D5', 1.6, 0.3, -0.15))
# the rule under "step by step." grows one step per beat: a harp note climbs the D major triad with each step
for t, p, k in zip(times('step'), ['A4', 'D5', 'F#5'], range(3)):
    ev.append((t, 'harp', p, 1.2, 0.42 + 0.03 * k, -0.2 + 0.13 * k))
ev.append((times('step')[-1], 'vibraphone', 'A5', 1.6, 0.22, 0.3))

add(music, S.render(ev, DUR, master=False), 0.0)

# ---------- EFFECTS (from the picture's event times) ----------
for e in EV['events']:
    t, k = e['t'], e['kind']
    if k == 'pop':
        add(fx, bubble(380 + 90 * e['i'], 1.0), t, 0.32, e.get('x', 0) * 0.6)
    elif k == 'tick':
        wb = S.hit('woodblock', 'c', 0.22)
        add(fx, lp(hp(wb, 400), 5000), t, 2.6, 0.1)   # v2: +5.4 dB, to stay over the lifted bed
    elif k == 'riser':
        add(fx, riser(e['dur'], 1.0), t, 0.42, 0.0)
        cy = S.hit('sus_cymbal', 'cresc', 0.55)               # a real cymbal swell, its loudest point on the merge
        env = np.abs(cy); w = int(0.05 * SR)
        sm = np.convolve(env, np.ones(w) / w, mode='same'); pk = int(np.argmax(sm))
        seg = cy[max(0, pk - int(e['dur'] * SR)):pk].copy()
        seg *= np.linspace(0, 1, len(seg)) ** 2; seg[-240:] *= np.linspace(1, 0, 240)
        add(fx, hp(seg, 2000), t + e['dur'] - len(seg) / SR, 0.5, 0.2)
    elif k == 'merge':
        add(fx, bubble(300, 1.0), t, 0.55, 0.0)
        add(fx, sub_thump(70, 44, 0.5), t, 0.5, 0.0)
    elif k == 'wobble':
        add(fx, wobble(), t, 0.3, 0.0)
    elif k == 'crouch':
        add(fx, air(e['dur'] + 0.05, 900, 400, 1.0, 1.2, (0.8, 0.2)), t, 0.1, 0.0)
    elif k == 'whoosh':
        if e['dir'] == 'up':
            add(fx, air(0.42, 500, 3600, 1.0, 1.8, (0.18, 0.82)), t - 0.03, 0.5, -0.25)
        else:
            add(fx, air(0.2, 3000, 700, 1.0, 1.8, (0.75, 0.25)), t - 0.02, 0.36, 0.0)
    elif k == 'thud':
        gc = S.hit('gran_cassa', 'hit', 0.5)[:int(1.4 * SR)]
        gc *= env_ar(len(gc), 0, 0.6)
        add(fx, gc, t, 0.55, 0.0)
        add(fx, sub_thump(64, 41, 0.6), t, 0.62, 0.0)
        felt = lp(R.standard_normal(int(0.03 * SR)), 2200) * np.exp(-t_(0.03) / 0.005)
        add(fx, norm(felt), t, 0.18, 0.0)
    elif k == 'reveal':
        add(fx, air(0.34, 1800, 7500, 1.0, 1.4, (0.35, 0.65)), t, 0.2, 0.0)
    elif k == 'rise':   # v2: the mark rises from where it landed into the lockup row
        add(fx, air(0.3, 700, 2600, 1.0, 1.5, (0.4, 0.6)), t, 0.16, 0.0)
    elif k == 'slide':
        add(fx, air(0.36, 2400, 900, 1.0, 1.5, (0.3, 0.7)), t, 0.2, -0.35)
    elif k == 'cta':
        wb = S.hit('woodblock', 'a', 0.16)
        add(fx, lp(hp(wb, 500), 4000), t, 3.0, -0.1)
    elif k == 'step':
        add(fx, air(0.16, 3000, 6000, 1.0, 1.2, (0.2, 0.8)), t - 0.02, 0.08, -0.2 + 0.1 * e['i'])
    elif k == 'exit':
        add(fx, air(0.45, 4500, 600, 1.0, 1.3, (0.25, 0.75)), t, 0.22, 0.0)

# ---------- one room, levels, ending ----------
def peq(x, f0, gdb, q=1.0):
    A = 10 ** (gdb / 40); w = 2 * np.pi * f0 / SR; al = np.sin(w) / (2 * q)
    b = [1 + al * A, -2 * np.cos(w), 1 - al * A]; a = [1 + al / A, -2 * np.cos(w), 1 - al / A]
    from scipy.signal import lfilter
    return lfilter(np.array(b) / a[0], np.array(a) / a[0], x, axis=0)
music = hp(music.T, 60).T if False else sosfilt(butter(2, 60, 'high', fs=SR, output='sos'), music, axis=0)
music = peq(music, 230, -4.0, 0.9).astype(np.float32)
MUSIC_G, FX_G = 0.6, 1.0
send = music * 0.22 * MUSIC_G + fx * 0.14 * FX_G
wet = S.room(send, size=0.42, mix=1.0, predelay=0.014, damp=0.55)
music_bus = music * MUSIC_G
fx_bus = fx * FX_G
mix = music_bus + fx_bus + wet
# the loop seam: fade the very end to digital silence, and keep the first 50 ms clean
fade = int(0.3 * SR)
mix[-fade:] *= np.linspace(1, 0, fade)[:, None] ** 2
peak = np.abs(mix).max()
mix *= 0.89 / peak
for name, x in (('music', music_bus / peak * 0.89), ('sfx', fx_bus / peak * 0.89), ('mix_raw', mix)):
    sf.write(os.path.join(HERE, name + '.wav'), x.astype(np.float32), SR, subtype='PCM_24')
print(f'{DUR:.2f} s, raw peak {20 * np.log10(peak):.1f} dBFS (normalised to -1 dBFS before mastering)')
print('instruments:', sorted({e[1] for e in ev} | {'woodblock', 'sus_cymbal', 'gran_cassa', 'vibraphone_bowed', 'cellos', 'violins_trem', 'violas', 'violins', 'contrabass'}))
