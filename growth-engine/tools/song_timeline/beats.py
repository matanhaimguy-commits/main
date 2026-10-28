"""The beat grid (same method as motion-studio/beats.py): BPM, beats, downbeats (every 4th beat), onset hits."""
from __future__ import annotations


def beat_grid(path: str) -> dict:
    import librosa
    import numpy as np
    y, sr = librosa.load(path, sr=None, mono=True)
    tempo, frames = librosa.beat.beat_track(y=y, sr=sr, units="frames")
    beats = librosa.frames_to_time(frames, sr=sr).round(3).tolist()
    onset = librosa.onset.onset_strength(y=y, sr=sr)
    peaks = librosa.util.peak_pick(onset, pre_max=3, post_max=3, pre_avg=3, post_avg=5, delta=0.5, wait=10)
    return {"bpm": round(float(np.atleast_1d(tempo)[0]), 1), "duration": round(len(y) / sr, 2), "beats": beats,
            "downbeats": beats[::4], "hits": librosa.frames_to_time(peaks, sr=sr).round(3).tolist()}
