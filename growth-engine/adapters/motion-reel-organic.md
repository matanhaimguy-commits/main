# motion-reel, organic adapter

Pass this file, the Post Card and `growth-engine/production/STANDARDS.md` with every `motion-reel` run for an organic
`reel_motion` post (organic.json: tier C, production family `motion`, 0 to 30 credits, jobs trust, reach, convert,
beliefs B2 to B5, "always voiced"). The skill's method stays: setup, the reference bank, art direction, concepts, the
treatment and beat sheet, styleframes, the engines, the render contract, the sound method, the review loop and the
delivery folder (`.claude/skills/motion-reel/SKILL.md`, house rules in `motion-studio/CLAUDE.md`). What changes: its
words come from Hook Lab and Script Lab (organic adapters), its voice and numbers from STANDARDS.md, a fresh reviewer
checks its text in code before any render (G-MOTION-TEXT), and fresh reviewers run G-MOTION-FRAMES (M1 to M7) and
G-FINAL. Where this file or STANDARDS.md disagrees with the skill or the house rules, they win for organic posts
(section 7). Built from motion-reel (180 lines), `motion-studio/CLAUDE.md` (74 lines) and
`production/audit/motion-reel-growth-engine.json`. "Line" means a SKILL.md line; "house line" a
`motion-studio/CLAUDE.md` line. motion-video-director is retired for our work (section 8).

## 1. The skill's stages on the 16-step pipeline
Every step applies to the `motion` family (standards.json): step 7 has no gate (the brand look is the brand kit),
step 8 is the build with G-MOTION-TEXT on the code's text constants and the owner's look at the hook styleframe, step
10 the preview render, step 11 G-MOTION-FRAMES.

| Skill stage (lines) | Step | Gate in the ledger | Who |
|---|---|---|---|
| 0 Setup (24 to 31) | before 0 | none | `bash motion-studio/setup.sh`; project `motion-studio/projects/<slug>-<post_id>/`; `pipeline.py init <slug> <post_id> --format reel_motion --card <card>`. A session rooted above the repo installs the generation gate and proves it (DAILY.md 0) |
| 1 Intake, 2 Research and assets (33 to 52) | 0 | G-BRIEF | Claude, from brain.json, brand-kit.md and the card. No question round (section 2); real logo files and fonts from the brand kit; `brand.md` carries the STANDARDS zone |
| 3 References, 4 Three concepts (54 to 83) | 1 | G-IDEA | Claude: THE PICTURE passes the one-second read; `refbank.py pick` and `check`; the Organic Director checks Content Map fit |
| (stage 5's hook line) | 2 | G-HOOK | hook-agent with `hook-lab-organic.md`, a code-made concept frame per finalist, a fresh grader (section 2) |
| 5 Script (86 to 88) | 3 | G-SCRIPT 85+, G-HUMAN-SPINE | script-agent with `script-lab-organic.md` (section 2); spine pick delegated with the reason |
| 5 Voice, music plan (89 to 94) | 4 | G-AUDIO-MASTER, G-HUMAN-VOICE (once per voice) | `pipeline.py budget` first (the voice is the run's first generation, STANDARDS 10), then ElevenLabs per STANDARDS 4; G-AUDIO on each voice asset (section 3) |
| 5 Word timings, beat grid (90 to 94) | 5 | G-TIMELINE | `audio/words.json` from the approved master; every scripted word found |
| 6 Treatment and beat sheet (96 to 102) | 6 | G-PLAN, G-SPEC per scene | beat sheet checks; visual-planner writes `SCnn` Shot Specs; fresh prompt-reviewer (section 4) |
| (brand kit, fonts, logo files) | 7 | none | close with a note: the look is the brand kit |
| 7 Styleframes (104 to 108), 8 Build (110 to 131) | 8 | G-MOTION-TEXT, G-HUMAN-HOOKBOARD | Claude builds the composition and the styleframes and registers the `MR` version; a fresh prompt-reviewer checks the code's text constants (G-MOTION-TEXT); the hook styleframe, hook text on it, goes to the owner (section 5) |
| (budget) | 9 | G-BUDGET | `pipeline.py budget` again once steps 0 to 8 are closed: it re-prices the whole piece (music, SFX, any generated image, 25% retakes); step 9 closes only on a G-BUDGET recorded after them (STANDARDS 10) |
| 8 Build: the preview render (110 to 131) | 10 | none of its own; G-PROMPT-IMG and G-VIS for any generated image | Claude renders the `MR` version that passed G-MOTION-TEXT (section 5) |
| 10 Review (141 to 149) | 11 | G-ASSETS: G-MOTION-FRAMES on the latest `MR` version, G-AUDIO on every audio asset, G-VIS on any generated image | fresh take-reviewer, motion mode (M1 to M7) |
| 9 Sound, 11 Render and master (133 to 155) | 12 | none | Claude: the frame rate of section 6, the mix and loudness of section 3 |
| (final review) | 13 | G-FINAL, G-DIRECTOR | fresh take-reviewer, final mode (F1 to F8 plus the STANDARDS 9 extra checks); the Organic Director |
| 12 Deliver (157 to 166) | 14 | G-HUMAN-FINAL | hub draft; Matan approves on the Content page; then `refbank.py log` |
| 13 Revisions (168 to 170) | back to the changed step | the gates of that step | section 6 |
| (none in the skill) | 15 | G-LEARN | the analyst at 72 h and 7 d |

Human stops are only the pipeline's: G-HUMAN-SPINE (delegated, shown as FYI), G-HUMAN-VOICE (once per voice),
G-HUMAN-HOOKBOARD, G-HUMAN-ESCALATE (an asset after 3 failed attempts; a prompt after 2 failed review loops goes to
the Organic Director first) and G-HUMAN-FINAL. Guided mode's pauses (lines 20 to 22) and the autopilot stop "to
approve paid generation" (line 19) are replaced by them and by G-BUDGET.

## 2. Words: Hook Lab and Script Lab, not stage 5's own rules
- **Intake is the card.** CTA, length, language, voice and spend come from the Post Card and the brain. The skill's
  voiceover question (line 37, house line 35) is answered: `reel_motion` is always voiced (owner rule, 15 Oct 2026).
- **Hook (step 2), `hook-lab-organic.md`:** 10 hooks, a 3-channel stack (visual, text, spoken), every channel A or A+
  from Hook Lab and from a fresh grader. Frame 1 shows the problem where it lives in the business (the phone with an
  unanswered "Sa kushton?" message, a quiet inbox after paid ads). Screens show states, never counts, and no real
  platform logos or names: "the inbox", "the phone" (STANDARDS 6). Text hook and hook timing per STANDARDS 5 and 6
  (4 to 10 words in the top third, on screen by 0.3 s and held to about 3 s, never over the frame-1 subject; an
  optional label of 6 words or fewer). Spoken: first word at 0.0 s (within 0.1 s of the first frame), the problem in
  the first 6 words, sentence 1 of 8 to 14 words. Motion in the first second. No product, brand name, price or offer
  in the first 3 s; no logo intro. The skill's "hook in the first 2 s" and its single alternative hook line (lines 87
  to 88) are replaced. Hook Lab's 2 variants can be rendered cheaply as trial reels, each through G-FINAL.
- **Concept frames** (AI-VIDEO-PIPELINE step 2): one per finalist stack (the master and 2 variants), made in code from
  the brand kit as a still of frame 1 with its text hook on it (no generation, 0 credits), saved in
  `runs/<post_id>/qa/hook-concepts/` and shown to the fresh grader at phone size with the text hook and spoken line 1.
  A frame 1 that needs a generated image follows `hook-lab-organic.md` (a gated hero `still`).
- **Script (step 3), `script-lab-organic.md`** (this is how motion-reel calls Script Lab: issue 17): the narrator line
  format of Script Lab's 18a (one line = one breath = one picture, 4 to 17 words; commas join running thoughts;
  numbers as words; brand names spelled for the TTS), not its brand-name count: the agency is named lightly or not at
  all. On-screen words are read as 18e cards in the sound-off read. Name one structure: myth vs truth ST6, mistakes
  list ST7, hidden cause (compact) ST3, problem-solution ST2, breakdown ST3 or ST9, demo ST14, two futures ST5. For a
  B4 method post, one step of the Only Choice System per episode (Find, Own, Attract, Convert, Close). organic.json
  lists no `story_templates` for `reel_motion`, so a story shape (`pov_day`, `two_days`, `hidden_villain`,
  `object_speaks`) on a motion reel waits until it is added there.
- **Length is the card's tier** (STANDARDS 8 is the single source: O15, O30, O60, and O90 only with a stated reason;
  no full discovery story under 45 s; nothing over 90 s until the owner confirms a longer limit). The skill's 30 to
  45 s default (line 36) is not used.
- **Word budget** at the locked narrator's measured pace, per beat, then the total checked; until it is measured, 2.5
  words a second (STANDARDS 4; the skill's 2.4, line 87, is replaced).
- **Gate:** Script Lab's 100 points, release at 85 or more with no critical fail, after a fresh cold read (two from
  O60 up: listen-only and sound-off, the sound-off reader getting the planned on-screen text only). 3 FIX loops, new
  readers every loop, then the owner (G-HUMAN-ESCALATE). Record `pipeline.py gate <slug> <post_id> G-SCRIPT --status
  PASS --by "script-lab gate" --score <n>`, report in `runs/<post_id>/qa/script-gate.md`.
- **Close:** one organic ask for the card's job (organic.json `cta_types` and `jobs`; ORGANIC-OS 6.2), spoken as the
  last line and shown on the end card (STANDARDS 5): follow, save, send, comment (an answer to a question the reel
  asks), keyword (only a keyword live in brain.json; StraightScale today: only ANALIZA), DM, or book. "Book" only on a
  convert card, said as the keyword path ("comment ANALIZA; the booking button comes in the DM", brand-kit "One
  path"), never as a link. Examples (ti): "Ruaje këtë postim." / "Dërgoja një pronari biznesi." / "Shkruaj ANALIZA në
  komente." No price, discount, guarantee or urgency.
- **Offer reels:** only a hard offer card (`hard_offer: true`: a convert card, about 3% of output, capped by
  organic.json `stage_mix`) is about the one free offer, the free analysis, with only the facts brain.json holds and
  the same limits. No B8 "what happens in the analysis" reel until decision D3. The offer beat of the first
  StraightScale motion reel (`knowledge/our-pipeline.md` section 3) is not repeated on any other card.
- **Facts:** only from brain.json and brand-kit.md. StraightScale's proof bank has no public entry, so no result,
  revenue or client number on screen. No number on a screen or in a line unless it is in brain.json (STANDARDS 6); a
  count of the post's own items ("5 hapa" for the five steps in brain.json) is structure and must match what the reel
  shows. The skill's rule "every number on screen has a source and a date in PROJECT.md" (line 50) stays, and that
  source must be the brain. An anecdote in the brand's voice is a clearly framed POV ("POV: ..."), never stated as
  something that happened (STANDARDS 7). The brand kit's Never list holds (no answer-time promise, no claim that we
  work the client's leads: we build them a system); no hype words; no em dashes.

## 3. Voice and sound (STANDARDS 1 and 4)
- **Narrator:** ElevenLabs `eleven_v4` (audition `eleven_v3` beside it); StraightScale's locked narrator is voice
  `8oGKUMljR779HzpZBiE4`. No G-HUMAN-VOICE record exists for it yet (`runs/SS-LIB-STYLE` holds only G-HUMAN-LOOK), so
  the first voiced run asks the owner once (audition and a 15 s pilot: `pipeline.py ask ... G-HUMAN-VOICE`) and the
  answer is recorded on a LIB run, so later runs pass on the measured take checks. The G-HUMAN-VOICE note records the
  narrator's pace band measured on the approved audition (STANDARDS 4: 4.3 to 5.5 syllables/s is the English band;
  Albanian takes are scored against the measured one). Kokoro (`setup.sh voice`) is for scratch timing only, never
  the master clock or the delivery. Designing a new voice is a casting: G-HUMAN-VOICE.
- **The gate:** every ElevenLabs call is checked by the hook. The voice is the run's first generation, so at step 4,
  before the first call: `pipeline.py budget <slug> <post_id> --planned <Higgsfield credits, 0 if none> --balance
  <live balance> --el <ElevenLabs credits>` (the gate wants a G-BUDGET PASS from the last 24 hours; about 177
  ElevenLabs credits per 4-take narrator beat, STANDARDS 10). A later batch (the bed, SFX, a generated image) needs a
  G-BUDGET from the last 24 hours too, and step 9 re-prices the whole piece (section 1). Each beat is a `voice` asset
  (`pipeline.py asset ... VO-B1 --type voice`, `prompt ... --file` with the exact text); audio only after G-SCRIPT.
- **Takes:** beats of 2 to 7 lines, 4 takes each; the take score (word errors, the pace band from the G-HUMAN-VOICE
  note, pitch range 7 semitones or more, flat lines flagged); lowest score wins. Every take transcribed word for word:
  ElevenLabs Scribe (`creative_transcribe_audio`) or a multilingual faster-whisper model (`small` or `medium`,
  `language="sq"`, in the Higgsfield sandbox when this container can't download it), never an `.en` model; spelling
  read against the script. Record the check on each kept take as its audio gate (STANDARDS 9 G-AUDIO): `pipeline.py
  gate <slug> <post_id> G-AUDIO --status PASS --by <who> --asset VO-B1@v<n> --note "<what was checked>"`, then
  G-AUDIO-MASTER on the run. Step 11 (G-ASSETS) can't close while an audio asset lacks it. The skill's "several takes,
  pick the best" (line 89) is replaced.
- **Pauses:** never capped or compressed; pause spread (SD) 0.1 s or more and at least one pause of 0.45 s or more per
  3 sentence ends (STANDARDS 4, proposed). Pauses go into measured silences (line 92 stays). Never speed the voice past
  1.05x.
- **Timeline (step 5):** `audio/words.json` (`{source, duration, words:[{w,s,e}]}`) from the approved master; every
  scripted word found; `beats.py` for the music grid. The voice is the master clock; event times come from the
  composition, never retyped (line 134 stays).
- **Music and SFX:** the bed is `eleven_music_v2_5`, instrumental, 2 takes, the VO length plus 3 to 5 s, a `music`
  asset with its own G-AUDIO. Levels per STANDARDS 4: 14 to 18 dB under the voice; under the hook only a tension bed
  with no melody, further down; ducking on the lines; dropped further under the turn, the reveal and the payoff (the
  skill's 10 to 20 dB, line 137 and house line 41, is replaced). SFX `eleven_text_to_sound_v2`, 4 takes, always with
  `duration_seconds` set, levels per STANDARDS 4, never under the hook words; each an `sfx` asset with its own
  G-AUDIO. Fewer sounds than beats, planned silences, a real ending (lines 134 to 136 stay).
- **Master:** loudness per STANDARDS 4 (-14 LUFS integrated plus or minus 1, true peak -1 dBTP or lower, plus its
  loudness range and short-term limits). The skill's two-pass loudnorm to -14 LUFS and -1.5 dBTP
  (`motion-studio/projects/straightscale/finish.sh`) complies; keep it. Measure with `python3
  growth-engine/tools/vqa_crops.py loudness <file>` (it reports all four values and a pass flag) and still run
  `tools/audio_qa.py` and a spectrogram.
- **AI label:** an ElevenLabs narrator speaking as a person is "an AI voice speaking as a person": the label is on and
  the hub notes say "AI label: on", per STANDARDS 7 (D1 decides whether to extend it). An AI person in any generated
  image is labelled too, never a client and never shown with a result (section 5 for how people may appear).

## 4. Shot Specs per scene (step 6)
- **The plan (G-PLAN):** the beat sheet in `docs/treatment.md` (time, beat, voice, on screen, moving, still, link to
  next, audio) passes the skill's checks (lines 99 to 101: beat lengths vary, CV 0.25 or more, the longest 4x the
  shortest or more; every transition names what survives it; every reaction has a visible cause; nothing important
  frozen over 4 s; the idea reads with the sound off) and STANDARDS 5: a picture change every 2 to 4.5 s, every 1 to
  1.5 s in the first 5 s, motion in the first second. A planned rest after the hook stays at 1.5 s or less while it
  is inside the first 5 s. Record `pipeline.py gate <slug> <post_id> G-PLAN --status PASS --by claude --note
  "docs/treatment.md"`.
- **One Shot Spec per scene** (`shots/SC01.spec.yaml` to `SCnn`, VISUAL-QA 7.2), written by the visual-planner:
  `format: motion`, `aspect: "9:16"`, `hero: true` on SC01 (frame 1); `script_lines` and `line_text` from the line
  table; `must_read_in_1s`; `text_in_image` with every on-screen string, its surface, position and occlusion (each
  line its own surface of 6 words or fewer: check P6); `timing` with `start_s`, `end_s`, `words` and `mode: CODE`;
  the `motion` block: `elements` (id, text, position, `enter_on_word`, `exit_s`), `brand_colours` (brand kit hexes),
  `fonts` (Playfair Display, Montserrat); `action_physics` as positions and times ("line 2 rises from 34% to 30% of
  the height between 0.2 and 0.5 s and stops"), unless the scene is `static`; `setting.background_rule` (no fake UI,
  no invented screens: house line 20); `camera.safe_zones` with the STANDARDS zone; `regions` for every text surface;
  targeted `must_not` ("no drawn or rebuilt logo", "no text in the bottom 35%", "no em dashes").
- `pipeline.py spec-check <slug> <post_id>` until clean; a fresh prompt-reviewer in spec mode records G-SPEC per scene.

## 5. Build, the code-level text review, G-MOTION-FRAMES (steps 8 to 11)
- **Engines** as the skill's table (lines 112 to 119): HyperFrames by default (client copy as variables, one
  sub-composition per scene, the registry searched before any named effect); the canvas engine, Lemo-Opuscar, Claude
  Animation Base (the client's own character, never Clawd) or collage Route C when the look needs it. The render
  contract (house lines 8 to 15) stays.
- **Generated images** (collage Route B, a photoreal plate) are optional and gated: each is a `still` asset with its
  Shot Spec, G-PROMPT-IMG and its own G-VIS PASS (M7), on the STANDARDS 1 model (a still with no person in the
  client's style: GPT Image 2.5; a realistic person: GPT Image 2 with a reference photo), made when the build needs it
  with a G-BUDGET from the last 24 hours. People follow STANDARDS 7 until D1 is decided: an AI business owner only from
  behind, as hands, at a distance or as stylized animation; the StraightScale strategist faces the camera only as the
  presenter in his clearly staged studio set (the whiteboard), AI label on, never as a client, owner or customer. The
  skill's "approved spend" (line 119) is G-BUDGET.
- **Brand:** fonts self-hosted (`font-family`, never the `font:` shorthand); colours from the brand kit, one accent;
  no gold text on ivory, no red text on charcoal; body text 44 px or more on a 1080-wide frame, checked at 360 px wide
  (house line 28 stays). Captions per STANDARDS 6 (1 to 4 words per card, bold sans, contrast 4.5:1 or more, timed to
  the word, its size and band); supers 2 to 6 words, never the transcript.
- **Safe zone (STANDARDS 6):** top 14% (269 px) and bottom 35% (672 px) clear of key content, the right 21% of the
  width (227 px) in the lower half, and 6% side margins (65 px). House line 27 (250, 400, 140 px) is replaced; write
  the zone into `brand.md`. Canvas engine: `node motion-studio/tools/safezone.mjs <project> --top 269 --bottom 672
  --right 227 --left 65 --min 44` (it applies the right margin to the full height, stricter than STANDARDS above the
  middle). Check HyperFrames pages against the same zone (`check --caption-zone` uses its own zone; M3 decides).
- **Logo: the real files only.** `clients/<slug>/brand/wordmark-white.png` on dark, `logo-full.png` on light,
  `symbol.png` for the mark, placed as PNGs on the end card. Never redrawn, traced, generated or rebuilt in canvas or
  CSS: the first StraightScale motion reel drew a `logoMark` from a description (our-pipeline.md section 3), and that
  is not allowed now. No logo before the end card.
- **Styleframes (step 8):** 3 or 4 key frames in the real engine (hook, a middle beat, the method moment, the end
  card), scored by the producer on the skill's rubric (8 or more on every axis) as a pre-check, never as a gate. The
  hook styleframe with the hook text on it, at phone size, goes to the owner: `pipeline.py ask <slug> <post_id>
  G-HUMAN-HOOKBOARD --note "hook styleframe" --files <png>`; the answer is recorded with `pipeline.py approve`.
- **G-MOTION-TEXT, the text-constant review before any render** (step 8; VISUAL-QA 7.2, the Prompt Reviewer's
  equivalent; STANDARDS 9): register the build as a version of the render asset (`pipeline.py asset <slug> <post_id> MR
  --type motion_render --shots SC01,SC02,...`). Export every on-screen string from the code (HyperFrames variables or
  the canvas scene table) with its scene, position, font, size, colour and enter and exit times to
  `runs/<post_id>/edit/text-constants.v<n>.json`. A fresh prompt-reviewer gets only that file, the `SCnn` specs, the
  released script and `words.json`, and checks M1 (every string letter by letter against the spec and the script: ë,
  ç, punctuation, no em dashes; nothing in the code that the spec lacks; the word counts of STANDARDS 6), M3 (positions
  inside the zone), M4 (each element enters on or just before its word) and M6 (colours and fonts from the brand kit).
  Its report (`"gate": "G-MOTION-TEXT"`, `"asset_id": "MR"`, `"version": <n>`, `"independent": true`, the four checks
  and `files_opened`) is saved as `runs/<post_id>/qa/text-constants.v<n>.review.json` and goes in with `pipeline.py
  record <slug> <post_id> <that file>`. Step 8 closes on G-MOTION-TEXT and G-HUMAN-HOOKBOARD. No render without the
  PASS: G-MOTION-FRAMES fails on a version that lacks it.
- **G-MOTION-FRAMES (step 11):** render a draft of the `MR` version that passed G-MOTION-TEXT, at the delivery frame
  rate (section 6), add it with `pipeline.py media ... MR@v<n> --file <draft>`, then `python3
  growth-engine/tools/vqa_crops.py motion <video> --run <slug>/<post_id> --asset MR@v<n>` (frames every 0.5 s plus
  each cut's start, middle and end). Run the skill's automatic checks on the same render first (`seekcheck.mjs`,
  `pacing.py`, `audio_qa.py`, `safezone.mjs` with the zone above, HyperFrames `check`, Lemo `readcheck.mjs`): they
  record no gate, but G-MOTION-FRAMES passes only when they pass too (STANDARDS 9). A fresh take-reviewer in motion
  mode opens every file in `must_open` and runs M1 to M7: M1 every word spelled exactly; M2 no unplanned overlap,
  nothing clipped; M3 the STANDARDS zone and contrast 4.5:1; M4 each text on or just before its spoken word (from
  `words.json`); M5 motion in the first second, hook text by 0.3 s; M6 brand colours and fonts only; M7 every
  generated image passed G-VIS on its own; and nothing important frozen more than 4 s. Pass: zero critical, zero
  major. `pipeline.py record` the JSON. Fix in code as a new `MR` version: it needs its own G-MOTION-TEXT (the gate
  reads each version), then its render and a review by a new reviewer. The final render starts only after a PASS. The
  skill's self-scored rounds (lines 141 to 149) are the builder's pre-check, never the gate.

## 6. Render, G-FINAL, delivery (steps 12 to 15)
- **Render** (frame rate per STANDARDS 5, one rate per file): HyperFrames and the canvas engine deliver 30 or 60 fps
  (HyperFrames `render --quality delivery`, with `--fps 60` for 60; the canvas engine's `render.mjs --fps 30` or
  `--fps 60` with `--sub 4`, in parallel segments with the seams checked), so the skill's 60 fps finals (lines 115,
  153) may stay. A whole Lemo-Opuscar or Claude Animation Base piece renders and delivers at 24 fps; a 24 fps segment
  inside a 30 or 60 fps master is conformed by repeating frames, never by interpolation. Export H.264 High, 1080x1920,
  AAC 48 kHz; the master audio is the only audio.
- **G-FINAL:** the final is a `final` asset (`pipeline.py asset ... FINAL --type final`). `vqa_crops.py final <video>
  --run <slug>/<post_id> --asset FINAL@v<n>` (frames every 1.5 s plus every cut), `vqa_crops.py loudness`, and a
  transcript of the final mix. A fresh take-reviewer in final mode runs F1 to F8: clean frames; the sound-off watch
  (hook and story read without audio); captions exact, timed and inside the zone; the transcript matches the script;
  loudness per STANDARDS 4 (the `vqa_crops.py loudness` pass flag); first word at 0.0 s; policy and the AI label;
  credits within the preflight. STANDARDS 9 adds the sound-on watch, the voice-alone listen (a robotic voice sends the
  piece back to step 4) and the banned-model check (the run's `calls.jsonl` shows only standard models, or a recorded
  G-EXCEPTION or G-FALLBACK). Then the Organic Director: `pipeline.py gate <slug> <post_id> G-DIRECTOR --status PASS
  --by organic-director --note ...`.
- **Delivery:** `deliver/vN/` as the skill says (never overwritten), plus `reel.mp4` (the STANDARDS 3 reel file: 9:16
  MP4, under 100 MB; its length is the card's tier, STANDARDS 8, never over 90 s until the owner confirms a longer
  limit) and `cover.jpg` (the poster frame) in `clients/<slug>/content/<key>/` with the caption, alt text,
  `script.md` and `qa.md`. The 4:5, 1:1 and 16:9 re-layouts (line 158) only when the card asks. Hub draft (DAILY.md
  section 4), status `draft`, notes "Native Albanian read needed (on-screen text, captions, caption)" and "AI label:
  on". Nothing posts before G-HUMAN-FINAL. The owner's listen happens there (line 139: "ask the user to listen";
  STANDARDS 14 H1). After delivery, `refbank.py log` and commit `refbank/ledger.json` (line 164 stays).
- **Concepts and series:** the three-concept round (stage 4) runs for a one-off or a new series. A series episode
  fills the series' locked template. `refbank.py check` fails a film that repeats a used category or a device from the
  client's last 3 films; when a series device repeats by design, the Organic Director decides and it is written in
  `PROJECT.md`.
- **Revisions (stage 13):** changed spoken words go back through G-SCRIPT and the voice; any change in the code is a
  new `MR` version through G-MOTION-TEXT and G-MOTION-FRAMES; any change after G-FINAL repeats G-FINAL.
- **G-LEARN (step 15):** the analyst at 72 h and 7 d: skip rate, average watch time, sends, saves, follows and ANALIZA
  comments per reach; drop-offs mapped to line numbers where insights allow; 1 or 2 lessons to
  `clients/<slug>/analytics/learnings.md`; the hook's result to the client's Hook Library. motion-reel has no learning
  loop of its own (the refbank ledger logs use, not results).

## 7. What this adapter overrides in the skill and the house rules, and why
| Skill or house rule (line) | Organic rule | Why |
|---|---|---|
| Own hook and script rules, 1 alternative hook (87 to 88) | Hook Lab (10 hooks, fresh grader) and Script Lab 85+ with a cold read | STANDARDS 12; issues 13, 17 |
| Hook in the first 2 s (87) | First word at 0.0 s, hook text by 0.3 s, motion in the first second | AI-VIDEO-PIPELINE 2; VISUAL-QA M5 |
| About 2.4 words a second (87) | The narrator's measured pace; 2.5 before measuring | STANDARDS 4 |
| Default 30 to 45 s (36) | The card's tier: O15, O30, O60, O90 only with a stated reason | STANDARDS 8 |
| Ask whether there is a voiceover (37; house 35) | Always voiced | organic.json `reel_motion` (owner rule) |
| "Several takes, pick the best" (89) | 4 takes per beat, take score, transcript of every take | STANDARDS 4 |
| Music 10 to 20 dB under the voice (137; house 41) | 14 to 18 dB; only a tension bed with no melody under the hook; lower under turn, reveal, payoff | STANDARDS 4 |
| -14 LUFS, -1.5 dBTP (137; house 41) | Kept: it meets -14 (plus or minus 1), -1 dBTP or lower; loudness range and short-term limits added | STANDARDS 4 |
| 60 fps finals and canvas engine (115, 153) | Kept: 30 or 60 fps, one rate per file; a Lemo or Claude Animation Base piece 24 fps | STANDARDS 5 (issue 10) |
| Safe zone top 250, bottom 400, right 140 px (house 27) | Top 269, bottom 672, right 227 px in the lower half, sides 65 px | STANDARDS 6 (issue 11) |
| No em dashes "if asked" (88) | No em dashes anywhere | STANDARDS 6 |
| Self-scored review rounds (141 to 149) | Fresh reviewers: G-MOTION-TEXT before any render, G-MOTION-FRAMES, then G-FINAL | VISUAL-QA 1, 7.2; STANDARDS 9 |
| Paid generation "with approved spend" (19, 119) | Registered prompts, G-PROMPT-IMG, G-VIS, G-BUDGET; the gate checks every call | VISUAL-QA 9 |
| Guided pauses (20 to 22) | The pipeline's human checkpoints, batched in the daily queue | README "Who decides what" |
| 4 aspect ratios on every delivery (158) | 9:16 only unless the card asks | Organic posts are Reels |
| No AI disclosure rule | The label for an AI voice speaking as a person, per STANDARDS 7 (D1 decides whether to extend it) | Issue 12 |
| Number sources in PROJECT.md (50) | Kept, and the source must be brain.json | Brain rule: facts only from the brain |

## 8. motion-video-director is retired for our work (issue 13)
Do not load `motion-video-director` for any of our videos, organic or paid; route every video to motion-reel (the
root `CLAUDE.md`, STANDARDS 12 and 13). Its description still matches any video request, so a session that loads it
stops and switches. The reasons, from `production/audit/motion-video-director-claymation.json`:
- **It writes its own hooks and scripts.** Its hook devices include "result-first" (its line 267), against Hook Lab's
  gate 7 (no product or result in the first 3 s); it never calls Hook Lab or Script Lab.
- **Em dashes as pause marks** (its lines 333 and 353, and its example script), against "no em dashes anywhere".
- **The user makes the MP3 by hand** on elevenlabs.io (its lines 241 and 384): no `eleven_v4` route, no 4-take score,
  no gated generation, and "Eleven v4 (or v3)" in one place, "Eleven v3 (or v4)" in another.
- **Freesound-only SFX** (its lines 35, 91, 154, 328) and no named music source; Freesound and Hugging Face are blocked
  in this environment, and STANDARDS 1 names the ElevenLabs sound models.
- **Missing helper scripts:** `preflight.sh`, `create_env.sh`, `normalize_env.py`, `analyze_ref.sh` and the fetch
  scripts exist nowhere; `preview.mjs` exists only as a copy built for `straightscale-reel/`, with flags outside the
  skill's own contract. An unattended agent fails at its preflight.
- **Its own numbers:** a per-video word table whose 15 s top (38 words) breaks its own formula (about 35), a third
  safe-zone set (top 220, bottom 420, right 140 px), captions at 60 to 70% of the height.
- **No budget, AI label, compliance or learning step;** its human gates are chat approvals (approve script, plan,
  preview) an automated run can't wait for; it suggests unverified community MCPs and Pinterest scraping with a
  logged-in browser.
- **Contradictions:** "run preflight first" against "send the kickoff before anything else", and a full 508-line read
  before the first reply.

What it did well already lives elsewhere: resume files (motion-reel's `PROJECT.md` and the run ledger), the transcript
diff against the script (STANDARDS 4 and F4), timestamped preview sheets (`vqa_crops.py motion`), the reading-time
check (Lemo `readcheck.mjs`), caption contrast 4.5:1 (M3), no logo intro (section 2). The `claymation` style skill in
the same audit is not used by motion-reel; animated stories take only its style block, through
`animation-organic.md`, never its Seedance 1.5 Pro transitions.
