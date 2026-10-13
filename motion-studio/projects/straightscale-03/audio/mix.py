# Mix: voice on top, music ducked from the voice's own word timings (audio/words.json), effects.
# python3 audio/mix.py  (after audio/score.py and the EQ step in finish.sh) -> audio/mix_raw.wav
import json, os
import numpy as np, soundfile as sf

HERE = os.path.dirname(os.path.abspath(__file__))
SR, DUCK_DB, PAD_IN, PAD_OUT, BRIDGE, RAMP = 48000, -13.0, 0.12, 0.3, 0.7, 0.18
rd = lambda n: sf.read(os.path.join(HERE, n), dtype='float32', always_2d=True)[0]
vo, mu, fx = rd('vo_st.wav'), rd('music_eq.wav'), rd('sfx.wav')
N = max(len(vo), len(mu), len(fx))
pad = lambda x: np.pad(x, ((0, N - len(x)), (0, 0)))
vo, mu, fx = pad(vo), pad(mu), pad(fx)

# voice-active spans from the word timings; short gaps are bridged so the music doesn't pump between words
words = json.load(open(os.path.join(HERE, 'words.json')))['words']
spans = []
for w in words:
    s, e = w['s'] - PAD_IN, w['e'] + PAD_OUT
    if spans and s - spans[-1][1] < BRIDGE: spans[-1][1] = max(spans[-1][1], e)
    else: spans.append([s, e])
act = np.zeros(N, np.float32)
for s, e in spans: act[max(0, int(s * SR)):int(e * SR)] = 1
k = int(RAMP * SR); act = np.convolve(act, np.ones(k) / k, mode='same')        # smooth ramps
gain = 10 ** (DUCK_DB * act / 20)

# levels: the unducked music sits 1 dB under the voice, so it is ~14 dB under while ducked
rms = lambda x, m: np.sqrt(np.mean(x[m] ** 2) + 1e-12)
vmask = act > 0.99
m_gain = rms(vo, vmask) / rms(mu, slice(None)) * 10 ** (-1 / 20)
mix = vo + mu * m_gain * gain[:, None] + fx * 0.5
peak = np.abs(mix).max()
if peak > 0.95: mix *= 0.95 / peak
sf.write(os.path.join(HERE, 'mix_raw.wav'), mix, SR, subtype='PCM_24')
sf.write(os.path.join(HERE, 'music_ducked.wav'), mu * m_gain * gain[:, None], SR, subtype='PCM_24')
print(f'{len(spans)} voice spans, music gain {20 * np.log10(m_gain):.1f} dB, duck {DUCK_DB} dB')
