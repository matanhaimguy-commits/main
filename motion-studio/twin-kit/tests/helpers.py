"""Shared test fixtures: a small valid EDL and the test clip's face data."""
import copy
import json
import sys
from pathlib import Path

KIT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KIT))
EXAMPLE = KIT / "examples" / "test-clip"

FACE = {"src_w": 1080, "src_h": 1890, "head": [240, 184, 844, 996], "face": [240, 407, 844, 1059], "samples": 20}


def example_edl():
    """The test clip's EDL, loaded the way the composer loads it."""
    from kit import edl
    return edl.load(EXAMPLE / "edl.json")


def small_edl(**over):
    base = {
        "width": 1080, "height": 1920, "fps": 30, "duration": 8.0, "_dir": str(EXAMPLE),
        "brand": {"bg": "#111111", "fg": "#ffffff", "accent": "#ff9900", "display_font": "Serif", "ui_font": "Sans"},
        "twin": {"src": "media/twin-cut.webm"},
        "voice": {"src": "media/vo.mp3", "start": 0.3, "words": "words.json"},
        "beats": [
            {"id": "a", "start": 0.0, "end": 2.0, "twin": "full",
             "hero": {"move": "behind-word", "vars": {"text": "HELLO", "y": 560}}},
            {"id": "b", "start": 2.0, "end": 4.0, "twin": "off", "cut_in": "whip",
             "scene": {"move": "ui-prompt", "vars": {"text": "hi"}}},
            {"id": "c", "start": 4.0, "end": 6.0, "twin": "stage",
             "hero": {"move": "two-tone", "vars": {"lead": "A", "key": "WORD", "y": 560, "size": 180}}},
            {"id": "d", "start": 6.0, "end": 8.0, "twin": "off", "cut_in": "flash",
             "hero": {"move": "end-card", "vars": {"line": "Comment PLAN"}}},
        ],
    }
    out = copy.deepcopy(base)
    out.update(over)
    return out


def dump(obj):
    return json.dumps(obj)
