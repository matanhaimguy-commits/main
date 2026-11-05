# Edit engine

The studio's in-house editing engine: the editing half of a reel, with no research or script writing. It takes either
**footage** of someone talking or a **voiceover** for a motion-graphics film, and returns a finished, captioned,
mixed reel with a report. It needs only `ffmpeg` and Python 3; it works the same on a Mac, on Ubuntu and in the cloud
sessions.

```bash
python3 motion-studio/edit-engine/edit.py styles          # list the looks
./motion-studio/edit-engine/selftest.sh                   # regression test (needs flite)
```

## Route A: footage (talking head, interview, to-camera)

```bash
E=motion-studio/edit-engine/edit.py
python3 $E transcribe clip.mp4 --out words.json            # local Whisper; in cloud sessions use ElevenLabs Scribe (below)
python3 $E plan clip.mp4 --words words.json --style punchy # see what would be cut; renders nothing
python3 $E run  clip.mp4 --words words.json --style punchy --music bed.mp3 --out deliver/v1 [--aspect 9x16] [--draft]
```

What `run` does, in order:
1. **Cuts** filler words (um, uh, erm...), pauses longer than the style's `max_pause`, and **retakes**: when a sentence
   is restarted with the same opening words, the earlier take is dropped and the later one is kept. Every drop is
   listed in `REPORT.md` so a person can confirm it. Without a words file it cuts on silence only.
2. **Jump-cut punch-ins**: the zoom changes only where time was removed, which hides the jump.
3. **Reframes** to 9:16, 4:5, 1:1 or 16:9: a centre crop with the face kept in the upper part of the frame, or
   `"frame": "blur"` to fit the whole shot over a blurred copy of itself.
4. **Captions** timed to the cut words (filler words never shown), placed inside the platform safe zones, with an
   active-word highlight and a pop or rise entrance. They are burned in, and `captions.srt` is also delivered.
5. **Sound**: the voice gets the studio EQ and compression; an optional music bed is levelled, EQ'd and
   **ducked under the voice** (sidechain); everything is mastered with two-pass loudnorm to -14 LUFS and -1.5 dBTP.
6. **Delivery** in `--out`: `<name>_<aspect>.mp4` master (H.264 CRF 21, AAC 320k, faststart), `_view.mp4` (under
   30 MB), `poster.png`, `captions.srt`, `words_cut.json` (word timings on the new timeline), `cutlist.json`
   (source in and out points), and `REPORT.md` / `report.json`.

## Route B: voiceover only (motion graphics, no footage)

```bash
python3 $E voice vo.mp3 --words words.json --out motion-studio/projects/<client>-<piece> --tighten
#   -> audio/vo.wav (pauses, fillers and retakes removed) + audio/words.json + audio/words.js = the master clock
#   build the picture against words.js (HyperFrames, or the canvas engine's cue table K), render it silent, then:
python3 $E finish out/silent.mp4 --voice <project>/audio/vo.wav --words <project>/audio/words.json \
        --captions bold --music bed.mp3 --out <project>/deliver/v1
```
`finish` adds captions (optional), the voice polish, the ducked music and the master, then delivers the same
package as route A. It also works on any finished silent render, including canvas-engine and HyperFrames films.

## Styles (`presets/*.json`)

| Style | Look |
|---|---|
| `punchy` (default) | tight cuts, alternating punch-ins, 3-word Montserrat Black captions, yellow active word |
| `bold` | one big word at a time, three zoom levels, the fastest cut |
| `clean` | only long pauses and fillers cut, no zooms, sentence captions on a dark box |
| `minimal` | slow push-in on every piece, lowercase captions on a soft box |
| `editorial` | Playfair Black Italic captions, red active word |
| `handwritten` | Caveat handwriting captions, green active word |

Brand overrides on any command: `--font "Montserrat Black" --size 90 --color "#F8F6EF" --highlight "#BE0F18"`.
A brand style is just another JSON file; pass its path to `--style`. The fonts in `fonts/` are the only ones the
captions can use; add a brand font as TTF with a clean family name (see `fonts/NOTICE.md`).

Style fields: `cut.max_pause` (longest pause kept, s), `pad_in` / `pad_out` (breath kept around words),
`punch` (zoom cycle), `push` (slow zoom per piece), `frame` (`crop` | `blur`), `focus_y` (0 top to 1 bottom),
`drop_fillers`, `drop_retakes`; `captions.font/size/case/words/max_chars/color/highlight/outline/shadow/box/y/anim`
(`pop` | `rise` | `none`); `music_db` (bed level before ducking).

## Transcription

- **Your own computer:** `edit.py transcribe` runs Whisper locally through the HyperFrames CLI.
- **Cloud sessions:** the Whisper model download is blocked. Use the ElevenLabs connector instead:
  `creative_transcribe_audio` on the clip's audio, and save the result as JSON. The engine reads Scribe, Whisper /
  HyperFrames and studio `{words:[{w,s,e}]}` files as they are.
- Always fix misheard names and numbers in the words file before `run`: the captions show exactly what it says.

## Going further on the same cut

The master is a normal video, so the heavier tools can run on top of it:
- `embedded-captions`: cinematic captions placed *behind* the speaker (35 looks). Run it on the master with
  `--no-captions` set here.
- `talking-head-recut`: designed graphic cards (titles, lower-thirds, data callouts) over the cut.
- `hyperframes` / the canvas engine: B-roll and motion-graphic inserts.

## What it does not do (by design)

No research, references, scripts or concept work; that is `motion-reel`. No colour grading. No multi-camera
switching. No automatic B-roll. It never posts: a person listens with sound and reads every caption first.

## Licences

All code here is the studio's own. Fonts are SIL Open Font License (`fonts/NOTICE.md`). Nothing from onetake
(non-commercial) is used, so the engine is safe for client work.
