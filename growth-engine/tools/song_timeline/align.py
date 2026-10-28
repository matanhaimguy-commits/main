"""Forced alignment of the known lyric words to the master (pocketsphinx, its bundled en-us model; it installs from
PyPI, so it runs where model hosts such as huggingface.co are blocked). Free recognition is not used: the lyric match
itself is measured by STT at step 4/5; this only places the known words in time."""
from __future__ import annotations

import re

SAMPLE_RATE = 16000
# Wide beams: the default ones lose the path under the guitar and the alignment fails to reach the grammar's end.
BEAMS = {"beam": 1e-100, "wbeam": 1e-80, "pbeam": 1e-100, "lw": 6.5}


def load_pcm(path: str) -> bytes:
    import librosa
    import numpy as np
    y, _ = librosa.load(path, sr=SAMPLE_RATE, mono=True)
    return (np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes()


def align(pcm: bytes, tokens: list[str]) -> list[dict]:
    """[{word, start, end}] in seconds, silences dropped; raises if a token has no pronunciation."""
    from pocketsphinx import Decoder
    d = Decoder(samprate=SAMPLE_RATE, **BEAMS)
    missing = sorted({t for t in tokens if d.lookup_word(t) is None})
    if missing:
        raise ValueError(f"no pronunciation for {missing}: add them with Decoder.add_word")
    d.set_align_text(" ".join(tokens))
    d.start_utt()
    d.process_raw(pcm, full_utt=True)
    d.end_utt()
    words = []
    for s in d.seg():
        name = re.sub(r"\(\d+\)$", "", s.word)
        if name.startswith("<") or name.startswith("["):
            continue
        words.append({"word": name, "start": round(s.start_frame / 100, 2), "end": round((s.end_frame + 1) / 100, 2)})
    if [w["word"] for w in words] != tokens:
        raise RuntimeError("alignment did not cover every lyric word in order")
    return words
