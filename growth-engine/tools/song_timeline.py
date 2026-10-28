"""Step 5 for a song run: word timings, beat grid, line times and the slice plan for each master.

  python3 growth-engine/tools/song_timeline.py <run_dir> O60=<master.mp3> [O30=<master.mp3> ...]

Reads the line table from <run_dir>/audio/timeline.md (rows `| O60-L01 | Section | Words |`), writes
<run_dir>/audio/words.json (aligned words per master) and <run_dir>/audio/timeline.json (BPM, beats, lines, slices).
Package: song_timeline/. Tests: test_song_timeline.py."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from song_timeline import align, beats, lines, lyrics


def build(md_text: str, prefix: str, master: str) -> tuple[list[dict], dict]:
    table = lyrics.read_lines(md_text, prefix)
    tokens = [t for line in table for t in line["tokens"]]
    words = align.align(align.load_pcm(master), tokens)
    grid = beats.beat_grid(master)
    timed = lines.line_times(table, words)
    plan = lines.slices(timed, grid["beats"], grid["duration"], prefix)
    summary = {"master": master, "bpm": grid["bpm"], "duration": grid["duration"], "voice_in": words[0]["start"],
               "method": "pocketsphinx forced alignment to the line table (en-us model); librosa beat_track",
               "lines": [{k: v for k, v in t.items() if k != "words"} for t in timed], "slices": plan,
               "beats": grid["beats"], "downbeats": grid["downbeats"], "hits": grid["hits"]}
    return words, summary


def main(argv: list[str]) -> int:
    run = Path(argv[0])
    md_text = (run / "audio/timeline.md").read_text()
    all_words, all_tl = {}, {}
    for arg in argv[1:]:
        prefix, master = arg.split("=", 1)
        all_words[prefix], all_tl[prefix] = build(md_text, prefix, master)
        tl = all_tl[prefix]
        print(f"{prefix}: {tl['bpm']} BPM, {tl['duration']} s, voice in {tl['voice_in']} s, "
              f"{len(tl['lines'])} lines, {len(tl['slices'])} slices")
    (run / "audio/words.json").write_text(json.dumps(all_words, indent=1) + "\n")
    (run / "audio/timeline.json").write_text(json.dumps(all_tl, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
