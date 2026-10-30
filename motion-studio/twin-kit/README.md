# Twin edit kit (T3)

Turns a host clip (the HeyGen twin, or any talking head) into a 1080x1920 reel: the person cut out and placed on a
set, six moves as HyperFrames templates with variables, UI scenes, captions from word timings, a sound on every
move, a music bed ducked under the voice, and a two-pass loudnorm to -14 LUFS. Plan: `Agency OS/Projects/Twin reel
machine plan 2026-10-29.md` in the vault, section "T3 Edit kit". Everything here runs at $0 on the cloud box.

## Commands

Run `bash motion-studio/setup.sh` first (vendored GSAP, HyperFrames CLI 0.8.150).

```bash
cd motion-studio/twin-kit
python3 twinkit.py cutout clip.mp4 --out twin.webm          # person cut-out, VP9 with alpha (u2net_human_seg on CPU)
python3 twinkit.py face twin.webm --out face.json           # head and face boxes from the matte
python3 twinkit.py align voice.mp3 script.txt --out words.json   # $0 word timings (see "Word timings")
python3 twinkit.py check edl.json                           # the edit rules, no render
python3 twinkit.py compose edl.json --out out/              # final.mp4, picture.mp4, stems, report.json
python3 twinkit.py compose edl.json --out out/ --keep-picture   # redo the sound only (seconds)
python3 -m unittest discover -s tests                       # 83 tests, one file per module
```

Checks on a render (STANDARDS 9, G-MOTION-FRAMES), from `out/build/`:

```bash
node ../../../../../tools/seekcheck.mjs --hf --dur 10.6                      # same pixels after any seek
node ../../../../../tools/safezone.mjs --hf --top 269 --bottom 672 --right 227 --left 65   # no text in the UI zones
npx -y hyperframes@0.8.150 check . --caption-zone "x0=0.06;y0=0.55;x1=0.79;y1=0.62;severity=error" --at-transitions
python3 ../../../../../tools/pacing.py ../final.mp4
python3 ../../../../../tools/audio_qa.py ../final.mp4 --music ../stem-music.wav --vo ../stem-voice.wav
```

safezone `--hf` asks HyperFrames itself (one `check --caption-zone` per forbidden band), so it sees the compiled page.
Captions carry `data-layout-allow-caption-zone`, so HyperFrames skips them there; `kit/rules.py` places them.

## The EDL

One JSON file per film (example: `examples/test-clip/edl.json`). Beats tile the film; each beat has a twin mode
(`stage`, `full`, `off`), at most one `hero` move, optionally a `scene` (UI or B-roll), a `grade` (the grain beat)
and a `cut_in` (`whip` or `flash`). Move variables go in `vars`; `at` delays a move inside its beat. Paths are
relative to the EDL; any image or video variable is copied into the build.

## Layers (back to front, `kit/moves.py`)

Twin modes: `stage` (scale 0.5, face 724-1050 px, the clip's box edges faded into the set) and `full` (full
width, face 367-1019 px). Both keep the face 15-55% from the top.

set (10) · B-roll and UI (20) · grade (25) · words behind the twin (30) · twin (40) · words in front (50) ·
captions (60) · end card (65) · flash (70). The whip moves the whole frame (`#frame`) on the root timeline.

## The moves (`templates/`)

| # | Move | Template | Layer | Sound | Built from |
|---|---|---|---|---|---|
| 1 | Words orbiting the head, passing behind it | `move-orbit.html` (mounted twice: back and front) | 30 + 50 | whoosh-cinematic | registry `locked-nucleus-orbit` idea; a halo at forehead height, the far side behind the crown (the matte occludes it), the near side above the brows |
| 2 | One big word behind the subject | `move-behind.html` | 30 | impact-bass-1 | the embedded-captions matte idea: the word sits under the cut-out |
| 3 | Two-tone type, key word heavy | `move-twotone.html` | 50 | whoosh-short | masked word rise |
| 4 | 3D object pop with motion blur | `move-pop3d.html` | 50 | pop | registry `motion-blur` (vendored in `third_party/`), CSS 3D extrusion |
| 5 | Black-and-white grain beat, graphics only | `move-bwgrain.html` | 25 | glitch-3 | backdrop filter under the twin and words, seeded grain |
| 6 | Whip and flash cuts, logo end card | root timeline (`kit/layers.py`), `move-flash.html`, `end-card.html` | frame, 70, 65 | whoosh, click, impact-bass-2 | registry `whip-pan-cut` profile; the real logo file |

Plus `stage.html` (the set: wall, light pool, drift, grain, or a set plate image), `ui-notification.html`,
`ui-chat.html`, `ui-prompt.html` (neutral system looks, no product's brand) and `captions.html`.

Sounds are the Pixabay kit bundled with media-use (`.claude/skills/media-use/audio/assets/sfx`, Pixabay Content
License), placed from the EDL's own times (`kit/sfx.py`).

## Edit rules (`kit/rules.py`, checked before every render)

One hero move per beat · every move, scene, grade and cut has a kit sound · hero text 4 words or fewer and on screen
1 s or more (orbit items 2 words or fewer) · a visual change at least every 3 s · the twin on screen 50% or less ·
no front word, object or caption on the face (brows to chin, from the matte) · the face 15 to 55% from the top ·
every text layer (behind-twin words, UI scenes and captions too) inside the STANDARDS 6 zone (top 269, bottom 672,
sides 65, right 227 in the lower half; `kit/zones.py`) · captions 80 to 100 px in the 55-62% band · text 44 px or
more. Then on the render: `node ../tools/safezone.mjs --hf` and HyperFrames `check --caption-zone` (below).

## Word timings

`xai/stt-v1` returns text only, no word times (checked on the 28 Oct runs in `SSEN-LIB-ATLAS-TESTS/qa/stt-*.json`),
so it cannot give captions their timing. `kit/align.py` lays the known script over the voice's voiced stretches
(phrases never straddle a pause). On the test voice it lands on the four documented pauses. It is an estimate,
accurate to about a syllable, and says so in `words.json`. A word-timed transcript (ElevenLabs timestamps, or a
STT model that returns words) drops straight in with the same format.

## Measured here (30 Oct 2026, 4 CPUs)

- Cut-out: 10.1 s of 1080x1890 in 4 min 5 s (about 0.04x real time); clean matte on hair and shoulders. Plan
  for about 25 min of CPU per minute of twin, or cut out only the beats where the twin is on screen.
- Render: the 10.6 s test film in 110 s end to end (HyperFrames `looks` quality, 30 fps), sound remix 3 s.
- Snapshots of 8 frames: 27 s.

## Licences

HyperFrames and its registry: Apache-2.0 (`third_party/LICENSE-hyperframes`). Fonts: the brand's Playfair Display
and Montserrat (OFL), loaded from the EDL. Sounds: Pixabay Content License.
