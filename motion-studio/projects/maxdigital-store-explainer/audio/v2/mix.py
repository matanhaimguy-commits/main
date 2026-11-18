# v2 mix: energetic voice (Dorian take B, tightened, 1.14x) + ElevenLabs music bed ducked from the word timings +
# denser effects from the film's own event times (audio/v2/events.json, tools/events.mjs). Effects come from the
# Earshot code-made bank (organic-engine/sfx/earshot) and Kenney CC0. Writes audio/v2/mix_raw.wav.
import json, os, subprocess
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
SR = 48000
EV = json.load(open(os.path.join(HERE, 'events.json')))
WORDS = json.load(open(os.path.join(HERE, '..', 'words.json')))['words']
DUR = EV['duration']
N = int(DUR * SR)
ES = '/home/user/organic-engine/sfx/earshot'
KN = '/home/user/organic-engine/code/edit-engine/sfx_lib/kenney_interface'


def load(path, af=None):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, *(['-af', af] if af else []), '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def db(x): return 10 ** (x / 20)


def put(buf, x, t, gain_db, pan=0.0):
    i = int(max(0, t) * SR)
    if i >= len(buf): return
    x = x[: len(buf) - i] * db(gain_db)
    if pan: x = x * np.array([1 - max(0, pan), 1 + min(0, pan)], np.float32)
    buf[i:i + len(x)] += x


vo = np.zeros((N, 2), np.float32)
voice = load(os.path.join(HERE, 'tight.wav'), 'highpass=f=80,equalizer=f=230:width_type=o:w=1.2:g=-3,equalizer=f=3500:width_type=o:w=1.4:g=2.5')
vo[:min(N, len(voice))] = voice[:N]
mu = np.zeros((N, 2), np.float32)
music = load(os.path.join(HERE, 'music.mp3'), 'highpass=f=40,equalizer=f=230:width_type=o:w=1.3:g=-6')
mu[:min(N, len(music))] = music[:N]

# ducking from the word timings: -14 dB under speech, bed lifts in the gaps and on the end card
g = np.ones(N, np.float32)
for w in WORDS:
    a, b = int(max(0, w['s'] - 0.05) * SR), int(min(DUR, w['e'] + 0.1) * SR)
    g[a:b] = db(-14)
k = int(0.25 * SR); g = np.convolve(g, np.ones(k, np.float32) / k, mode='same')
mu *= (g * db(-7))[:, None]
fo = int(0.8 * SR); mu[-fo:] *= np.linspace(1, 0, fo)[:, None]

# effects: (file, gain dB). Fewer, louder hits on structure; quiet ticks on UI.
MAP = {
    'whip': (f'{ES}/whoosh/whoosh_fast__whip.wav', -13), 'cut': (f'{ES}/whoosh/swish__soft.wav', -18),
    'hook': (f'{ES}/impact/cut_hit__sub.wav', -9), 'chip': (f'{ES}/chime/notify__m2.wav', -19),
    'stamp': (f'{ES}/impact/impact__punch.wav', -11), 'card': (f'{ES}/pop/pro_pop_in__round.wav', -15),
    'drain': (f'{ES}/riser/downlifter__sub_sink.wav', -15), 'riser': (f'{ES}/riser/riser__rush.wav', -17),
    'brand': (f'{ES}/impact/pro_logo_sting__sweep_hit.wav', -10), 'step': (f'{ES}/click/toggle__on.wav', -14),
    'draw': (f'{ES}/whoosh/pro_zip__up.wav', -19), 'swoosh': (f'{ES}/whoosh/whoosh_big__thump_airy.wav', -14),
    'pop': (f'{ES}/pop/ui_pop__wide.wav', -16), 'trust': (f'{ES}/chime/pro_notify__ding_2045.wav', -16),
    'accent': (f'{ES}/click/pro_click__glass.wav', -17), 'popup': (f'{ES}/impact/logo_sting__soft_bloom.wav', -10),
    'msg': (f'{ES}/pop/ui_pop__blip.wav', -15), 'msgme': (f'{ES}/pop/pro_pop__chirp.wav', -16),
    'sale': (f'{ES}/chime/pro_notify__ding_1930.wav', -17), 'strike': (f'{KN}/scratch_002.wav', -15),
    'brand2': (f'{ES}/impact/logo_sting__spark.wav', -13), 'button': (f'{ES}/click/pro_tap__glass.wav', -12),
}
fx = np.zeros((N, 2), np.float32); cache = {}
for e in EV['events']:
    kind, t = e['kind'], e['t']
    if kind == 'ticks':
        x = cache.setdefault('tick', load(f'{ES}/click/hover_tick__high.wav'))
        for i in range(30): put(fx, x, t - 0.05 + i * 0.022 + 0.08, -25, pan=0.3 * np.sin(i))
        continue
    if kind not in MAP: continue
    f, gain = MAP[kind]
    x = cache.setdefault(f, load(f))
    put(fx, x, t, gain)

mix = vo + mu + fx
peak = float(np.abs(mix).max())
if peak > 0.98: mix *= 0.98 / peak
sf.write(os.path.join(HERE, 'mix_raw.wav'), mix, SR, subtype='PCM_24')
print(f'mix_raw.wav: {DUR:.2f} s, peak {peak:.2f}, {len(EV["events"])} events')
