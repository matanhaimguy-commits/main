"""Atlas USD per finished piece: a format's atlas_units at standards.json atlas_prices, plus the 25% retake buffer.

Units per piece (each [low, high], before retakes): images, video_s (H3 seconds asked for), omni_s (OmniHuman audio
seconds), voice_s (seconds of narration or dialogue, voiced in STANDARDS 4's takes at its pace) and songs (Suno calls).
STANDARDS.md 10 explains the counts; config/organic.json formats[].usd holds the result.
"""
from __future__ import annotations

from .config import CONFIG, STANDARDS

UNITS = ("images", "video_s", "omni_s", "voice_s", "songs")


def voice_usd(seconds: float, prices: dict = STANDARDS["atlas_prices"], audio: dict = STANDARDS["audio"]) -> float:
    """ElevenLabs on Atlas for every take of the words, plus xai/stt-v1 word timings on each take."""
    takes = audio["takes_per_beat"]
    chars = seconds * audio["pace_words_per_s_default"] * prices["chars_per_word"] * takes
    return chars / 1000 * prices["tts_1k_chars"] + seconds * takes / 60 * prices["stt_min"]


def piece_usd(units: dict, end: int, prices: dict = STANDARDS["atlas_prices"],
              buffer: float = STANDARDS["gate_policy"]["retake_buffer"]) -> float:
    """One end (0 low, 1 high) of a piece's USD range, retakes included, in cents."""
    bad = set(units) - set(UNITS)
    if bad:
        raise ValueError(f"unknown atlas_units {sorted(bad)} (known: {', '.join(UNITS)})")
    n = {k: (units.get(k) or [0, 0])[end] for k in UNITS}
    base = (n["images"] * prices["image"] + n["video_s"] * prices["video_s"] + n["omni_s"] * prices["omni_s"]
            + voice_usd(n["voice_s"], prices) + n["songs"] * prices["song"])
    return round(base * (1 + buffer), 2)


def format_usd(fmt: dict) -> list[float]:
    return [piece_usd(fmt.get("atlas_units") or {}, 0), piece_usd(fmt.get("atlas_units") or {}, 1)]


def all_formats() -> dict[str, list[float]]:
    return {fid: format_usd(f) for fid, f in CONFIG["formats"].items()}
