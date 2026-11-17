# Mix for the MaxDigital explainer: voice (ElevenLabs take 1) + music bed (ElevenLabs music) ducked under the voice from the
# word timings + Kenney CC0 UI effects placed from the film's own event times (audio/events.json, exported by
# tools/events.mjs). Writes audio/mix_raw.wav; finish.sh masters it to -14 LUFS / -1.5 dBTP.
import json, os, subprocess
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
SR = 48000
EV = json.load(open(os.path.join(HERE, 'events.json')))
WORDS = json.load(open(os.path.join(HERE, 'words.json')))['words']
DUR = EV['duration']
N = int(DUR * SR)
LIB = '/home/user/organic-engine/code/edit-engine/sfx_lib/kenney_interface'


def load(path, af=None):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, *(['-af', af] if af else []), '-ac', '2', '-ar', str(SR), '-f', 'f32le', '-'],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()


def db(x): return 10 ** (x / 20)


def place(buf, x, t, gain_db):
    i = int(t * SR)
    if i >= len(buf): return
    x = x[: len(buf) - i] * db(gain_db)
    buf[i:i + len(x)] += x


voice = load(os.path.join(HERE, 'takes/take1.mp3'), 'highpass=f=80,equalizer=f=220:width_type=o:w=1.2:g=-4,equalizer=f=3500:width_type=o:w=1.4:g=2')
music = load(os.path.join(HERE, 'music.mp3'), 'highpass=f=45,equalizer=f=220:width_type=o:w=1.3:g=-6')
vo = np.zeros((N, 2), np.float32); vo[:min(N, len(voice))] = voice[:N]
mu = np.zeros((N, 2), np.float32); mu[:min(N, len(music))] = music[:N]

# ducking: -16 dB under speech, opened in the gaps; gain curve from the word timings, smoothed (60 ms attack, 300 ms release)
g = np.ones(N, np.float32)
for w in WORDS:
    a, b = int(max(0, w['s'] - 0.06) * SR), int(min(DUR, w['e'] + 0.12) * SR)
    g[a:b] = db(-16)
k = int(0.3 * SR)
kern = np.ones(k, np.float32) / k
g = np.convolve(g, kern, mode='same')
music_gain = db(-8)  # the bed itself sits low even in gaps
mu *= (g * music_gain)[:, None]
# fade the bed in over the first 0.6 s and out under the end card's last 1.8 s
fi, fo = int(0.6 * SR), int(1.8 * SR)
mu[:fi] *= np.linspace(0, 1, fi)[:, None]
mu[-fo:] *= np.linspace(1, 0, fo)[:, None]

# effects: one sound per event kind, quiet; fewer sounds than beats ('rise' stays silent)
MAP = {
    'chip': ('select_002', -20), 'stamp': ('drop_003', -14), 'card': ('pluck_001', -18), 'pop': ('pluck_002', -19),
    'slump': ('minimize_004', -16), 'brand': ('bong_001', -15), 'suck': ('minimize_002', -17), 'step': ('switch_002', -16),
    'draw': ('scroll_001', -22), 'build': ('maximize_002', -18), 'accent': ('select_005', -19), 'strike': ('scratch_002', -18),
    'whoosh': ('maximize_004', -18), 'button': ('confirmation_001', -14),
}
fx = np.zeros((N, 2), np.float32)
cache = {}
for e in EV['events']:
    kind = e['kind']
    if kind == 'ticks':   # a month of days ticking off: 30 tiny ticks over one second
        x = cache.setdefault('tick_001', load(f'{LIB}/tick_001.wav'))
        for i in range(30): place(fx, x, e['t'] - 0.1 + 0.05 + i * 0.033 + 0.12, -27)
        continue
    if kind not in MAP: continue
    name, gain = MAP[kind]
    x = cache.setdefault(name, load(f'{LIB}/{name}.wav'))
    place(fx, x, e['t'], gain)

mix = vo + mu + fx
peak = np.abs(mix).max()
if peak > 0.98: mix *= 0.98 / peak
sf.write(os.path.join(HERE, 'mix_raw.wav'), mix, SR, subtype='PCM_24')
print(f'mix_raw.wav: {DUR:.2f} s, peak before trim {peak:.2f}, {len(EV["events"])} events')
