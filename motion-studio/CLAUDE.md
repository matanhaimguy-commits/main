# Motion studio rules

Every video job runs through the motion-reel skill (`.claude/skills/motion-reel/SKILL.md`): setup, intake,
research, art direction, concepts, script and voice, treatment, styleframes, build, sound, review, render,
delivery. Start a session with `bash motion-studio/setup.sh`; the knowledge base is `knowledge/README.md`.
These rules apply to every engine (HyperFrames, the canvas engine, Lemo-Opuscar, Claude Animation Base).

## Render contract
- Every film is a pure function of time: `window.seek(t)` (canvas engine) or a paused GSAP timeline
  (HyperFrames) paints frame t. `node tools/seekcheck.mjs` must pass.
- No CSS transitions, no setTimeout, no requestAnimationFrame in render mode, no state carried between
  frames. Seeded noise only, never Math.random.
- Self-host every font and script (CDNs are blocked here). Write `font-family`, never the `font:` shorthand,
  in HyperFrames pages (the shorthand silently skips font embedding).
- Canvas engine: `node render.mjs` (H.264 yuv420p, CRF 16). HyperFrames: `render --quality delivery`.

## Look
- Banned: centred title on a gradient, everything fading in, corner labels and frame borders, glow on UI,
  generic particle bursts, grey-bar placeholder cards, generic avatar circles, redrawn logos, fake UI or
  invented screens, a frame whose lower half is empty for no reason, "cards on a flat background" as the
  whole idea.
- One display font, one UI font, from the client's brand. One accent colour unless the brief says otherwise.
- One signature device per film, present throughout.
- Every 2 to 4 seconds at the latest something new must happen on screen, and real rests (≥ 1 s) are planned, not
  accidental. For hook-driven social reels aim faster: the 81 viral reels in `refbank/` change something big every
  0.5-1.5 s (median), mostly inside continuous shots, with rests as short freezes on a payoff.
- Keep text and logos out of the platform UI on 9:16: top 250 px, bottom 400 px, right 140 px.
- Text sizes for phones: body never under 44 px on a 1080-wide frame; check every beat at 360 px wide.
- Search the HyperFrames registry and the Lemo-Opuscar styles before hand-building any named effect or look.

## Content
- Real brand material only: official logo file, captured colours and fonts, real product UI.
- No invented numbers, reviews, clients, testimonials or deadlines. Every number on screen has a source and
  a date in PROJECT.md. Examples are labelled as examples.
- Always ask whether the film has a voiceover; never decide it silently.
- Client-language copy gets an English check line when the user can't read it; flag it for a native speaker.

## Sound
- Music is generated, sampled, synthesized or supplied (licensed); effects are placed from the composition's
  own event times.
- Arrange music to the voice, then duck it 10-20 dB under the voice. Master to -14 LUFS, true peak -1.5 dBTP
  before encoding.
- We can't listen: run `tools/audio_qa.py` and look at a spectrogram, and ask a human to listen before the
  final delivery.

## Loop before you show me anything
1. Render one frame per beat as a contact sheet and LOOK at it at phone size.
2. Score it 1-10 on: hook in first 2s, readability at phone size, motion quality, continuity, pacing,
   composition, brand accuracy, sound sync, message with the sound off. Log it in `docs/review_log.md`.
3. Run the automatic checks (`tools/seekcheck.mjs`, `tools/pacing.py`, `tools/audio_qa.py`, HyperFrames
   `check --caption-zone`). Fix the 3 worst problems. Repeat until every score is 8+.
4. Only then do the full render. Never ship a known blemish without logging it and saying so.

## Studio tools
- setup.sh: session setup (`lemo`, `voice`, `music` tiers).
- lib/motion.js: closed-form spring() and track(). Use these instead of easing curves.
- render.mjs: canvas renderer, 60 fps with in-page subframe motion blur; `--from 12 --dur 3` renders one
  segment; run 2-3 segments in parallel for long films and concat them (check the seams).
- stills.mjs: `node stills.mjs --from 0.25 --step 0.5 --dur 20` contact sheet straight from index.html.
- review.sh: `./review.sh [out/final.mp4] [4.1]` writes contact, strip and phone sheets to out/.
- beats.py: `python3 beats.py audio/track.wav > beats.json`.
- tools/pacing.py, tools/audio_qa.py, tools/seekcheck.mjs: automatic review checks.
- tools/seekcheck.mjs --hf: the same determinism check for a HyperFrames project (via `hyperframes snapshot`).
- twin-kit/: the twin edit kit (cut-out host on a set, 6 moves as HyperFrames templates, UI scenes, one composer
  command with SFX on every move, ducked bed, two-pass loudnorm). Read `twin-kit/README.md`.
- tools/lemo_fonts.py: fetch the fonts a Lemo-Opuscar demo expects.
- tools/vectorize_mark.py: trace a flat-colour logo PNG into SVG paths (reports IoU per colour) so the real mark
  stays sharp in macro shots; hand over to the PNG at native size.
- tools/safezone.mjs: seeks a canvas-engine page every 0.1 s and flags text outside the safe zones or under 44 px
  (the page's text helper pushes boxes into `window.__boxes`, see projects/straightscale-02/index.html).
- tools/events.mjs: dumps the page's `window.EVENTS` (sound cue times) to JSON for the score and foley.
- templates/project/: the folder every new job starts from.
- refbank/: the reference bank (viral reels as breakdown cards + per-client usage ledger). `refbank/tools/refbank.py
  pick --client X` for fresh references, `check` before a concept, `log` after delivery. Never repeat a client's
  previous category, a signature device from its last 3 films, or a reference it already used.
- HANDOFF.md: everything this studio knows, written for the session building the automated reel machine.
- API keys live in .env (e.g. ELEVENLABS_API_KEY). Never paste keys into prompts.
