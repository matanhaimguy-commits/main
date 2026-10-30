"""The kit's vocabulary: every move, scene and cut, its template, its layer and its sound.

Layers from back to front (CSS z-index on the film root): set, B-roll and UI, grade (black-and-white grain acts on
everything below it), words behind the twin, the twin, words in front, captions, end card, flash.
"""

LAYERS = {
    "set": 10,
    "scene": 20,
    "grade": 25,
    "words-back": 30,
    "twin": 40,
    "words-front": 50,
    "captions": 60,
    "end": 65,
    "flash": 70,
}

# move id -> template file, layer, sound (Pixabay kit name), sound offset from the move's start, text variables
# (for the readability rule) and default duration of the hit.
MOVES = {
    "behind-word": {"template": "move-behind.html", "layer": "words-back", "sfx": "impact-bass-1", "sfx_at": 0.0,
                    "text": ["text"]},
    "two-tone": {"template": "move-twotone.html", "layer": "words-front", "sfx": "whoosh-short", "sfx_at": 0.0,
                 "text": ["lead", "key"]},
    "orbit": {"template": "move-orbit.html", "layer": "split", "sfx": "whoosh-cinematic", "sfx_at": 0.0,
              "text": ["words"]},
    "pop3d": {"template": "move-pop3d.html", "layer": "words-front", "sfx": "pop", "sfx_at": 0.12,
              "text": ["label"]},
    "bw-grain": {"template": "move-bwgrain.html", "layer": "grade", "sfx": "glitch-3", "sfx_at": 0.0, "text": []},
    "end-card": {"template": "end-card.html", "layer": "end", "sfx": "impact-bass-2", "sfx_at": 0.05,
                 "text": ["line"]},
}

# scenes fill the B-roll and UI layer; they are visual changes too, so they carry a sound
SCENES = {
    "ui-chat": {"template": "ui-chat.html", "layer": "scene", "sfx": "ping", "sfx_at": 0.35},
    "ui-notification": {"template": "ui-notification.html", "layer": "scene", "sfx": "notification", "sfx_at": 0.2},
    "ui-prompt": {"template": "ui-prompt.html", "layer": "scene", "sfx": "typing", "sfx_at": 0.15},
    "broll": {"template": None, "layer": "scene", "sfx": "whoosh-short", "sfx_at": 0.0},
}

# cuts are frame moves on the film root (whip) or a full-frame overlay (flash); the sound lands on the cut
CUTS = {
    "whip": {"sfx": "whoosh", "sfx_at": -0.18, "half": 0.16},
    "flash": {"sfx": "click", "sfx_at": 0.0, "half": 0.05},
}

# always-on parts that are not moves (no sound of their own)
FIXED = {
    "stage": {"template": "stage.html", "layer": "set"},
    "captions": {"template": "captions.html", "layer": "captions"},
    "flash": {"template": "move-flash.html", "layer": "flash"},
}


def template_for(kind):
    for table in (MOVES, SCENES, FIXED):
        if kind in table:
            return table[kind]["template"]
    raise KeyError(kind)
