#!/usr/bin/env python3
"""Audio QA for a finished mix or a final video (our own tool). We can't listen, so we measure.

    python3 tools/audio_qa.py deliver/film.mp4 [--music audio/music.wav] [--vo audio/vo.wav] [--png out/spectrum.png]

Reports and checks:
  - integrated loudness and true peak (house target -14 LUFS, true peak <= -1.5 dBTP after encoding)
  - dropouts: any 1 s window far quieter than the film's median (catches a score that goes silent)
  - low-mid mud: 0.5 s windows where 100-300 Hz carries most of the energy (a male voice trips this
    naturally; run the tool on the music stem alone to judge the score)
  - with --music (the music as it enters the mix: after gain and ducking) and --vo: the gap between them while the voice speaks
  - optional spectrogram image to eyeball sections
"""
import argparse, json, re, subprocess, sys
import numpy as np

SR = 22050


def decode(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


def loudness(path):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-vn", "-af", "ebur128=peak=true",
                          "-f", "null", "-"], capture_output=True, text=True).stderr
    tail = err[err.rfind("Summary:"):]
    i = re.search(r"I:\s+(-?[\d.]+) LUFS", tail)
    tp = re.search(r"Peak:\s+(-?[\d.]+) dBFS", tail)
    return float(i.group(1)) if i else None, float(tp.group(1)) if tp else None


def db(x):
    return 20 * np.log10(np.sqrt(np.mean(np.square(x))) + 1e-9)


def windows(x, size):
    n = int(size * SR)
    return [x[i:i + n] for i in range(0, len(x) - n + 1, n)]


def band_share(x, lo, hi):
    spec = np.abs(np.fft.rfft(x * np.hanning(len(x)))) ** 2
    freqs = np.fft.rfftfreq(len(x), 1 / SR)
    total = spec[(freqs > 40) & (freqs < 10000)].sum() + 1e-12
    return spec[(freqs >= lo) & (freqs < hi)].sum() / total


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("mix")
    ap.add_argument("--music")
    ap.add_argument("--vo")
    ap.add_argument("--png")
    ap.add_argument("--target", type=float, default=-14.0)
    a = ap.parse_args()

    checks = []
    def check(level, ok, msg):
        checks.append(("PASS" if ok else level, msg))

    lufs, tp = loudness(a.mix)
    check("FAIL", lufs is not None and abs(lufs - a.target) <= 1.0, f"integrated loudness {lufs} LUFS (target {a.target})")
    check("WARN", tp is not None and tp <= -1.0, f"true peak {tp} dBTP (keep <= -1.5 before encoding, <= -1.0 after)")

    x = decode(a.mix)
    sec = [db(w) for w in windows(x, 1.0)]
    med = float(np.median(sec))
    drops = [i for i, v in enumerate(sec) if v < med - 20]
    tail_ok = [i for i in drops if i < len(sec) - 2]  # the last seconds may fade out on purpose
    check("FAIL", not tail_ok, f"dropouts (1 s windows 20 dB under the median {med:.1f} dB): "
          f"{[f'{i}-{i + 1}s' for i in tail_ok] or 'none'}")

    muddy = [round(i * 0.5, 1) for i, w in enumerate(windows(x, 0.5)) if db(w) > med - 10 and band_share(w, 100, 300) > 0.6]
    check("WARN", len(muddy) <= 2, f"low-mid mud (100-300 Hz over 60% of the energy) at: {muddy[:12] or 'none'}")

    if a.music and a.vo:
        m, v = decode(a.music), decode(a.vo)
        n = min(len(m), len(v), len(x))
        under = []
        for wm, wv in zip(windows(m[:n], 0.5), windows(v[:n], 0.5)):
            if db(wv) > -40:  # the voice is speaking here
                under.append(db(wv) - db(wm))
        if under:
            gap = float(np.median(under))
            check("WARN", 10 <= gap <= 20, f"music sits {gap:.1f} dB under the voice while it speaks (want 10-20 dB)")

    if a.png:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", a.mix, "-lavfi", "showspectrumpic=s=1600x400:legend=1:scale=log",
                        a.png], check=True)
        print(f"spectrogram: {a.png}")

    print(f"== {a.mix}  per-second level: " + " ".join(f"{v:.0f}" for v in sec))
    fail = False
    for level, msg in checks:
        print(f"  {level:4}  {msg}")
        fail |= level == "FAIL"
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
