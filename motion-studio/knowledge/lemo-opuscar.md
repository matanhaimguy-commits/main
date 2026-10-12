# Lemo-Opuscar: reference guide for our client-reel pipeline

Repo: `lemomo-ai/lemo-opuscar` (MIT), full clone at `references/lemo-opuscar/` (commit `227e00a`).
Launcher skill: `.claude/skills/lemo-opuscar/` (`SKILL.md` + `scripts/setup.sh`).
Researched and tested in this cloud container on 12 Oct 2026 (4 CPUs, no GPU, Node 22, ffmpeg 6.1.1,
Python 3.12/3.13, Chromium 1194 at `/opt/pw-browsers`). All paths below are relative to
`references/lemo-opuscar/` unless they start with `/` or `motion-studio/`.

---

## 0. In one screen

- **What it is:** a library of 43 film *styles* (watercolour, impasto oil, ink wash, dark tech keynote,
  isometric infographic, glass product, ...). Each style = a `STYLE.md` "style prompt" (invariants of the
  look, sound and camera) + one demo short film whose full source is in `styles/<slug>/demo/`. On top sit
  three directing/building guides (`AGENTS.md`, `DIRECTOR.md`, `TECHNIQUE.md`) and a shared toolkit
  (`core/`: frame-by-frame Chromium renderer, Kokoro TTS + Whisper check, a 97-instrument sampler of mostly CC0 recordings,
  procedural foley, loudness mux, reading-time checker). No AI video, no stock: every frame and note is code.
- **Does it run here?** Yes, with workarounds. Canvas-2D styles render at **0.1-1.5 s per 1080p frame**
  (an 8 s 1080x1920 test reel rendered in 14 s with 3 workers). WebGL styles fall back to SwiftShader
  software GL: impasto takes **4.5 s/frame (no supersampling) to 15-26 s/frame (2x supersampling)**; a 3 s
  1080x1920 impasto clip rendered in 244 s with 3 workers. Any frame over 30 s fails on Playwright's
  screenshot timeout. three.js styles need a GPU (glass-product: 68-120 s per frame here, stills only).
  Kokoro TTS (offline) and the sampler (sample packs from GitHub Releases) work. Whisper speech check and
  edge-tts are **blocked** by the egress proxy (huggingface.co, speech.platform.bing.com).
  `core/render/mux.sh` **falsely rejects every mix shorter than ~58 s on ffmpeg 6.1** (one-line patch in §6).
- **Demos are 16:9 only and hard-coded to 1920x1080.** `--size 1080x1920` just crops them. A vertical reel
  must be authored for `innerWidth x innerHeight`; the engines themselves are resolution-independent
  (proven here with the watercolour and impasto engines at 1080x1920).
- **Most valuable for client work:** the directing method (`DIRECTOR.md`), the style prompts as a
  style-selection menu, the 2D engines (watercolour, impasto, one-line, whiteboard, iso-infographic,
  dataviz, dark-keynote, midcentury-toon, hologram-hud, silkscreen, swiss), the sampler (CC0 packs + CC BY piano) for real
  instrument scores, and the QA tools (`readcheck.mjs`, `mux.sh` loudness, cue checks).
- **Role we recommend:** a *style and technique library* that feeds our own `motion-studio` pipeline, not a
  replacement for it. Lift engines + audio toolchain + QA; keep our render contract, 60 fps motion blur,
  9:16-first layout and client process. Details in §7.

---

## 1. What it is, licence, commercial use

**Author:** Lemomo / LemoLab ("Made by LemoLab x Claude Opus 5.5"). The README says the styles were tuned
for Opus 5.5 and every demo was directed, drawn, scored and mixed by an agent writing code. A film takes an
agent "about 30-60 minutes and a fair amount of tokens".

**Licence: MIT** (`LICENSE`, (c) 2026 LemoLab). We may use, copy, modify, and use commercially, including
for client films. If we copy engine source files into our repo or a delivered source package, keep the MIT
notice (copy `LICENSE` next to the copied files). The rendered films are ours / the client's.

Third-party material has its own licence (the repo says "you are responsible for the materials you use"):

| Material | Licence | Commercial client use |
|---|---|---|
| Code in `core/`, `styles/*/demo/`, `tools/` | MIT | Yes, keep notice when redistributing source |
| Sample packs VSCO 2 CE, VCSL, FreePats, Karoryfer (`core/audio/instruments/`) | CC0 | Yes, no credit required (credit appreciated) |
| Salamander Grand Piano V3 (`piano`) | **CC BY 3.0** | Yes, **credit required** (exact line: `core/audio/INSTRUMENTS.md` §4, or `sampler.credits([...])`) |
| MuldjordKit drums (`drum_kit`) | **CC BY 4.0** | Yes, **credit required** |
| Kokoro-82M voice model + kokoro-onnx | Apache-2.0 (per demo CREDITS) | Yes |
| faster-whisper (speech check only) | MIT | Yes (not in the film) |
| edge-tts (Microsoft neural voices, online) | Microsoft service terms | Repo itself warns: check Microsoft's terms before commercial use. Treat as **not cleared** for clients |
| Fonts: `core/fonts/` and every font the styles name (Google Fonts) | SIL OFL 1.1 | Yes; self-host, keep OFL text |
| Poly Haven models/HDRIs (`core/assets/polyhaven/`) | CC0 | Yes |
| Demo stories / characters | MIT code, but some demos are **unofficial fan films** of real events or IP (pictogram-motion = 2026 Asian Games; living-screencast = Claude Code UI + Clawd mascot; OPUSCAR 98 = real Best Picture films) | Never carry those names, marks or characters into a client film (`DIRECTOR.md` §12) |

Credit rule: a user's film carries **no LemoLab credit and no watermark** (`AGENTS.md`). The
"LemoLab x Claude Opus 5.5" sign-off is hard-coded in 55+ places in demo code (e.g. `styles/impasto/demo/film.js`
credits div); if we lift a demo file, strip it. Their own pre-delivery check:
`grep -rniE "lemo ?lab|opus 5\.5" <project>` must find nothing outside LICENSE/CREDITS, and watch the
last seconds (text drawn into images cannot be grepped).

`STYLE.md` files name real artists, films and brands as **grammar references only** ("never copy their
characters, layouts, typefaces or music, and never name them in the film"). Glass-product, brick-toy,
riso, etc. explicitly forbid real product silhouettes, trademarks (LEGO, RISO) and logos.

---

## 2. Map of the repo

| Path | What it is for |
|---|---|
| `README.md` / `README.zh-CN.md` | Gallery, install, how to ask for a film. Gallery: https://lemomo-ai.github.io/lemo-opuscar/ |
| `AGENTS.md` (`CLAUDE.md` just imports it) | Agent entry: style vs story rules, how to find a style, the 6-step workflow, where files go |
| `DIRECTOR.md` | **The directing method** (brief, benchmark, story, treatment, look, sound, rhythm, camera, performance, common failures, pre-delivery checks, deliverables, copyright). Read first; it is the most transferable file |
| `TECHNIQUE.md` | **The build method**: page contract, determinism, one timeline, voice, music, sfx/mix, subtitles, review loop, 3D notes, character rigs, assets/fonts, where to look in demos |
| `MAINTAINING.md` | Owner-only: adding/registering/publishing a style (gates: ASR, -14 LUFS, readcheck, `release.py check --strict`) |
| `core/README.md` | Command reference for every tool, env vars, exit codes |
| `core/render/` | `page.mjs` (static server + Playwright page, waits for `window.READY`, dies on page errors), `serve.mjs` (serves library root; external project mounted at `/@film/`), `browser.mjs` (Chrome args, `PLAYWRIGHT_CHROME`, `LEMO_ANGLE`), `still.mjs` (review stills), `video.mjs` (parallel workers, JPEG screenshots piped to ffmpeg, lossless concat), `events.mjs` (`DUR`+`EV` to JSON), `readcheck.mjs` (reading-time QA), `mux.sh` (two-pass loudnorm -14 LUFS, grain in ffmpeg, damaged-audio checks), `sheet.py` (contact sheet), `srt.py`, `slot.mjs` (machine-wide render slots) |
| `core/lib.js` | Seeded RNG `mulberry`, `hash`, `vnoise`, `seg/clamp/lerp`, easings `ss eio eo ei back spring`, `monotone`/`track` keyframes, `env` |
| `core/tts/` | `tts.py` (Kokoro offline, EN default `af_bella` speed 0.92), `tts_zh.py` (edge-tts online), `asr_check.py` (faster-whisper word-for-word check + `words.json` timestamps) |
| `core/audio/` | `sampler.py` (97 sampled instruments, round-robins, velocity layers, seamless long-note extension, `render(events)`, `room()` reverb, `credits()`), `pluck.py` (Karplus-Strong + modal: guqin, pipa, shamisen, koto, banjo, guitars, harp, kalimba, music box), `sfx.py` (procedural foley + `compress`, `limit`, `add(buf, x, t, gain, pan)`), `INSTRUMENTS.md` (instrument list, licences, per-mood recipes; in Chinese) |
| `core/three/post.js` | three.js post: GTAO, physical DOF (CoC from depth), bloom, grade, 2x SSAA |
| `core/post/crt.js` | WebGL2 CRT/VHS pass over any 2D canvas (bloom, chroma bleed, scanlines, grille, power-on, tracking noise) |
| `core/fonts/` | Fredoka, Lilita One, IM Fell English, ZCOOL KuaiLe (CJK subset, ~200 glyphs only) |
| `core/assets/polyhaven/` | CC0 desk lamp, tea set, walnut textures (HDRIs via `tools/fetch.sh hdri`) |
| `styles/README.md` | Generated index: EN/CN name, folder, demo title |
| `styles/<slug>/STYLE.md` | The style prompt, 11 fixed sections: 1 essence / not-this, 2 materials & rendering, 3 colour logic, 4 type & subtitles, 5 motion, 6 camera grammar table, 7 sound palette, 8 native moves ("fits content like..."), 9 pitfalls, 10 engine (files + API), 11 variation space (3 structures / openings / endings far from the demo; scene styles add a use-case table) |
| `styles/<slug>/DEMO.md` | How the demo was made: story, shot table with *why*, score structure, sound-design table, palette, build notes, **engine reference** (API table + minimal example). Read only after your own treatment |
| `styles/<slug>/demo/` | Demo source + `build.sh` + `CREDITS`. Fonts, audio, voices are **gitignored** (not in the clone) |
| `styles/<slug>/poster.jpg`, `style.json` | Poster frame; metadata incl. `uses` (suggested use cases) and `dur` |
| `styles/_template/` | Template for STYLE.md / DEMO.md / style.json: use it as our own "style bible" format |
| `styleboard/` | Gallery generator (`build.py`), `catalog.json`, `opuscar98.html`, and **`opuscar98_styles.json`: 98 more style prompts** (one per Best Picture film; 77 2D / 4 2.5D / 17 3D; fields `style_en`, `blend_en`, `render`, `prompt_en`, `desc_en`, `shots`) |
| `docs/` | README images: `cover.jpg`, `frames/<slug>.jpg` (one frame per style), OPUSCAR 98 and thank-you posters |
| `tools/fetch.sh` + `tools/assets.json` | Downloads big packs from the GitHub `assets` release (voice, hdri, instruments) with sha256 check and resume |
| `tools/release.py`, `publish.sh`, `web_cuts.sh` | Maintainer publishing (repo hygiene checks: big files, local paths, secrets) |
| `plugin/`, `.claude-plugin/` | Claude Code plugin `lemo-opuscar@lemolab` = the same skill as `.claude/skills/lemo-opuscar/` |

Finished demo films are not in git: full 1080p on the `films` release, 720p cuts on the `web` release
(`https://github.com/lemomo-ai/lemo-opuscar/releases/download/films/<slug>.mp4`); GitHub Releases are
reachable from this container.

---

## 3. The director's process (what to copy into our workflow)

Source: `AGENTS.md` (workflow) + `DIRECTOR.md` (method). Order of judgement: **sound, rhythm, camera,
directing**; "good-looking frames are only the starting point".

### 3.1 Brief: one round of questions, then no more (`DIRECTOR.md` §1, `AGENTS.md` Workflow 1)
Ask once, in one message: facts/names/logos/products that must appear; the client's own material (voice
recording, music, photos, logos, fonts); language; whether they want a storyboard first (default no);
missing tools. Skip what the request already answers, fill every other gap with defaults, summarise the
brief in a few lines and start. Defaults: 30-60 s, 1920x1080 @ 24 fps (vertical via `--size 1080x1920`),
voice + burned-in subtitles + `.srt` in the client's language, -14 LUFS.

### 3.2 Benchmark first (§2)
Pick 1-2 reference works that set the bar **for this style and this topic** (not the demo's). Write
"what to learn" (composition, pacing, camera grammar, colour logic, score structure) and "what not to take"
(characters, designs, melodies, shots, logos, fonts). "The benchmark lifts quality more than any rule."

### 3.3 Story rules (§3)
One subject, one goal, one turn; **hook in the first 3 s** (no slow logo reveal); an ending that echoes
(bookend, scale reveal, or doing it right the second time); **one native move** of the medium at the
emotional peak (each `STYLE.md` §8 lists them); cut extras: one gag readable at thumbnail size beats three.

### 3.4 Treatment before anything (§4) - `TREATMENT.md`, written before opening the demo
1. **Three candidate structures** (journey, before/after, countdown, list that turns...) and the choice + why;
   the first idea for a style is usually its cliché.
2. Logline and arc (setup, turn, ending).
3. Benchmark learn / don't learn.
4. **Shot list**: framing, angle, camera move, duration, and **why**.
5. Beat sheet, second by second.
6. **Cue map**: tempo, bar grid, instrumentation per section, which beat every cut / action / subtitle lands on.
7. **Sound design table**: per section, ambience bed, main foley, music state.
8. Subtitle and title design (type is part of the style).

### 3.5 Prove the look (§5)
Model sheet (turnaround, 3-4 expressions, 2-3 key poses, palette) + 2 style frames, or 3 style frames
without characters, **rendered with the real drawing code**. Optional storyboard: 6-9 key shots tiled with
`core/render/sheet.py`, shot number / framing / duration / line under each; send with the logline and
"what I'm least sure about"; wait for approval only if the client asked for it.

### 3.6 Production order (`AGENTS.md` step 5, `TECHNIQUE.md`)
Voice -> ASR check -> score (parallel) -> animation -> mix -> render. Picture locks to the music grid,
not the other way round.

### 3.7 Delivery (§11)
Review loop; "**not the demo again**" (compare structure, opening, signature shot, camera path, score shape,
ending with the demo: at least 4 of 6 must differ); ASR passes; ~-14 LUFS; no black/NaN frames; subtitles
in sync and off key action; every sound-design row actually in the mix; no LemoLab sign-off.
Deliverables: `<name>.mp4`, `poster.jpg`, `<name>.srt`, `TREATMENT.md`, `CREDITS` (every third-party asset +
licence), source with a one-command `build.sh`.

### 3.8 The failures they saw most (§10) - put these in our review checklist
Subject too small / too far / pushed to the edge; too dark, or colour on the same colour; subtitles covering
the subject; a gag too fast to read; blank frames in transitions; a tracked effect (iris, zoom, spotlight)
that drifts off the subject after the camera moves (fix: one world-to-screen function).

---

## 4. Techniques worth stealing (concrete, with file pointers)

### 4.1 The page contract and determinism (`TECHNIQUE.md` §2, `core/README.md`)
```js
window.DUR = 54.2;                       // seconds
window.render = t => { ... };            // draw frame at t, pure function
window.READY = true;                     // after fonts/images/precompute
window.EV = [{t, type, ...}];            // sound/cue events -> events.mjs -> mix.py
window.TEXTS = t => [{id, text, x0, y0, x1, y1}];   // every on-screen text at t -> readcheck.mjs
```
Same idea as our `window.seek(t)`; a one-line shim (`window.seek = window.render`) lets our
`motion-studio/render.mjs` (60 fps, subframe blur) render a Lemo-style page, and vice versa.
Rules: no `Date.now()`, no unseeded `Math.random`, no state from the previous frame; any stroke generated
inside `render(t)` must be built under a fixed seed (`withSeed` in `styles/watercolor/demo/engine.js`) or
parallel workers disagree and paint "boils". Cache finished objects as sprites; draw stroke-by-stroke only
what is being painted. **Grain goes in ffmpeg (`mux.sh` grain arg), never in the page** (it makes frames
incompressible and slow). "Animate on twos where the style wants it, but keep camera and light smooth every
frame; a stepped camera reads as lag."

### 4.2 Painterly rendering
- **Impasto / palette knife** (`styles/impasto/demo/engine/impasto.js` + `plate.js`, WebGL2):
  design each set as a **flat, value-planned reference illustration** in Canvas2D (`Ref.fill/line/text/tint`,
  every shape tagged `{dir, maxR, detail, group, type}`), then `paintRef()` lays knife strokes **coarse to fine**
  (radii e.g. `[40,20,10,5]`) only where the painting still differs from the reference (Hertzmann-style),
  **never crossing shape groups** so silhouettes stay crisp. A blurred **underpainting** (`E.texture` + `E.under`)
  stops canvas showing between strokes. Strokes write colour + height; `E.finish(post)` rakes light across the
  height field (`light, norm, amb, dif, spec, ao`) and grades. Every stroke stores a grey and a colour version:
  `draw(batch, {grey:1, reveal:T})` + per-stroke `rev` delay = **colour re-laid by the knife** as a wave;
  per-stroke `app` + `appear:T` = **paint-over transition**. Moving figures are rebuilt each frame with fixed
  seeds (`drawNow`). Reflections are stacks of short horizontal dabs. **No film grain** (eats knife edges);
  supersample 2x. Check: "if the reference doesn't read at 480 px wide, no brushwork will save it".
  Our test (`/tmp/.../lemo-test/films/imp-reel/index.html`, ~70 lines) built a 1080x1920 café-cup plate with
  a knife paint-in and a grey-to-colour wave from the cup in one sitting: this is the single most
  "$10k-looking" technique in the repo for warm brand stories.
- **Watercolour** (`styles/watercolor/demo/engine.js`, Canvas 2D, classic scripts): stroke = variable-width
  ribbon (`prof: brush|leaf|even|tip|trunk`, +-22 % noise) at partial opacity + 3-9 **bristle tracks** with random
  dash patterns = flying white; `drawS(ctx, stroke, p)` paints up to fraction `p` (moving brush tip);
  `drawList(ctx, list, p)` paints a list in order (structure before detail); washes = same polygon 3 passes
  with jittered vertices (pooled edges); paper is a pre-generated image (`demo/paper.py`: warm base, 3 octaves
  noise, 2600 fibres, vignette); `sprite()` caches finished objects. Paper is the white; ink only for lines/text.
  Hand-written notes (Caveat) with pen leader lines. Native moves: painting-in reveal, burst, palette-as-data,
  specimen + note, **mist erase** to paper, map in time.
- **Ink wash** (`styles/ink-wash/demo/ink.js`, `comp.js` WebGL rice-paper compositor): five ink tones with
  opacities (.96/.82/.60/.34/.16), bristle model with ink load dropping along the stroke, "loaded stroke" whose
  dark side is its own contour, wet layer bleeds with edge pigment accumulation; **ink-bloom transition**
  (next scene grows inside a spreading drop with a tide line). Calligraphy from an OFL font used as a skeleton.
- **Urban sketch, pen & wash** (`styles/urban-sketch/demo/engine.js`): fineliner with wobble, 3-8 px overshoot,
  mid-stroke gaps; **stroke draw-time baked per pixel** so a shader plays back stroke order; wash misregistered
  1-3 px with dried darker edges and granulation; a **colour arrival field** (every pixel has a time colour
  reaches it, ragged wet front). Tip for big canvases in headless Chrome: pack ink + time into RGBA textures,
  upload the arrival field as `R16F`.
- **Crayon** (`styles/crayon-book/demo/gl.js`): wax sticks only where `tooth > 1 - k*pressure`; watercolour wash
  is resisted by wax (density x (1 - 0.9 x wax)) = "wax resist" hidden-message reveal.
- **One-line** (`styles/one-line/demo/ink.js`, `geom.js`): ink is a filled polygon, width = base x pressure,
  pressure from speed `0.66 + 0.8*exp(-v/300)`; ink pooling where speed drops; a stop leaves a teardrop blot;
  clamp minimum screen width on pull-backs; plan the path like an Euler circuit (stray connectors ruin a reveal);
  the pen is only a soft shadow. Excellent for minimal brand stories ("company milestones forming its logo").
- **Engraving** (`styles/engraving/demo/engine/index.js` `engraveShape(svgPath, {...})`): any SVG shape becomes an
  engraved figure (contour hatching, cross-hatch only in half-tones, swelling burin lines), then hand washes.

### 4.3 Texture
Paper everywhere is procedural and **anchored to the world** (moves with the camera; octaves cross-fade on
zoom so grain stays ~1 px). Light vignette. Misregistration of 1-3 px for print styles (risograph,
silkscreen, midcentury-toon re-rolls fill offsets on twos so the picture "shimmers"). Grain only via ffmpeg,
less on light backgrounds, **none** for pixel/vector/knife. Generated paper: `styles/watercolor/demo/paper.py`
(we parameterised it for 1080x1920 in 1.6 s).

### 4.4 Camera
- "Every shot needs a reason"; at least **4 different moves** and real changes of framing; one **signature shot**;
  at key moments the subject fills >= 1/3 of the frame height.
- **One world-to-screen function** for every effect that follows a subject.
- Each `STYLE.md` §6 is a camera grammar table (move / what it expresses / can serve): steal these tables for
  shot-list writing.
- 2.5D camera for UI: scale `s = 1/(1/zoom - z)`, near cards blur with magnification (`styles/dark-keynote/demo/engine.js`).
- **Log-space zoom keyed per bar** with monotone interpolation for long pull-backs (dark-keynote DEMO "Shots").
- Keep the camera inside the painted plate (`half = W/2/zoom`) for painted worlds.
- **Transitions inside the medium**, one consistent grammar per film: UI expand/collapse (keynote), knife
  paint-over + scrape (impasto), mist / brush-edge wipe / page turn (watercolour), ink bloom (ink wash),
  medallion iris and colour-block wipes (midcentury), doors split on the axis (art deco), dot wipe (halftone).
  Avoid default fades and dissolves (dissolving two knife layers "turns to mud").

### 4.5 Timing and rhythm
- **One timeline file drives everything** (`timeline.js` -> JSON): sections, BPM, hit points as `[section, beat]`;
  score, mixer, subtitles and checks read the same numbers. `tools/cuecheck.py` in 12 demos
  (e.g. `styles/dark-keynote/demo/tools/cuecheck.py`) compares every visual hit with its music cue; aim 0 ms;
  "every spawned element lands on a note" (<= 6 ms).
- **Reading time** (`DIRECTOR.md` §7, enforced by `core/render/readcheck.mjs`): subtitle >= max(1.8 s, line + 0.6 s);
  text hold after it finishes animating >= letters/15 + 1.5 s (EN) or chars/4.5 + 1.5 s (CJK); title card >= 4 s;
  "make it fast with fewer words per screen, not by cutting before people finish reading".
- Vary pace: one clear acceleration or deceleration, one breath (long take or held pause); "a film at one even
  speed has failed". One action, one sound, one cut, but don't cut on every beat.
- Concrete motion numbers from `styles/dark-keynote/DEMO.md`: typed spawns 0.2-0.3 s (drop 34 px + 6 px bounce),
  ease-out with one overshoot (`back`, s ~ 1.3), wind-up >= 8 frames, 2-frame contact, spring follow-through 0.6 s,
  light-reveal sweep 1.3 s with a 20 % glint, digits lock right-to-left one per sixteenth note, nothing just fades
  (CRT-off squash, retract one part per beat). Glass product: exploded view = long ease-out apart, short hover,
  very short ease-in snap on a downbeat.
- Scene styles give **information-order grammar with hold times**, directly usable for ad scripts:
  hologram-hud (spec walkthrough: title >= 5 s, each value >= 2.5 s, final sheet >= 3 s, 30-40 s for 2-5 parts),
  midcentury-toon (set-up guide: step detail >= chars/12 + 1 s; safety card 3-4 s per rule; store notice >= 3 s
  per card, 15-25 s), silkscreen-poster (event poster: headline 2.5 s, date + venue 3 s, final 3 s, 15-20 s;
  product drop 1.8 s per colourway, 12-18 s), engraving (museum label, "one minute on...", craft heritage).

### 4.6 Sound
- "Sound is half the film": every visible action has a sound matched to its material; three layers
  (ambience, foley, music); duck music under dialogue; **at least two real silences** before the turn/peak,
  and the first sound after the silence is one of the most important; use sound as a transition (J-cut / L-cut)
  at least twice; no generic "piano and strings": score in the style's sound palette (`STYLE.md` §7).
- **Sampler** (`core/audio/sampler.py`): `S.render([(t, inst, pitch, dur, vel, pan), ...], dur)` with real CC0
  instruments; long notes extended seamlessly by pitch-synchronous grain splicing; round-robins; `S.room()`
  reverb; `S.credits(names)` writes the CREDITS lines. Recipes per mood in `core/audio/INSTRUMENTS.md` §6
  (orchestral/epic, gentle/handmade, Chinese, Japanese, jazz/café, retro, baroque, sacred, pop, world, cold/sci-fi).
  This directly fixes our "synthesised score nobody listened to" gap with real-sounding instruments.
- **Pluck** (`core/audio/pluck.py`, numba): guqin/pipa/shamisen/koto/banjo/guitars/harp/kalimba/music box with
  bends, vibrato, tremolo, harmonics.
- **Foley** (`core/audio/sfx.py`): procedural click/clack/whoosh/thump/ding/pop/rumble/heartbeat + filters,
  `compress`, `limit`, `add()`; drive it from `window.EV` so each sound sits on its frame.
- Mix rules (`TECHNIQUE.md` §4-6): compress TTS first (Kokoro peaks ~17 dB over RMS), then balance by RMS with
  voice ~10 dB above music; duck music ~8 dB (keynote) to ~12 dB (glass) under voice; low end 20-120 Hz ~ -3 dB
  relative to the rest, no pad notes below MIDI 48, give bass 2nd/3rd harmonics for phone speakers; silence =
  digital zero on every track. Two sound families as story (disorder = detuned, random pans; product = one
  family, one mode, centred: `styles/dark-keynote/STYLE.md` §7). Spell numbers out in TTS text, digits on screen.
- **Master** (`core/render/mux.sh`): two-pass loudnorm to -14 LUFS / TP -1.2 dB, prints measured I/LRA/peak,
  warns if off target, pads short audio, refuses damaged audio. Our test: -14.1 LUFS, peak -1.2 dB.

### 4.7 QA tools
`still.mjs --range a:b:step` + `sheet.py` contact sheets (two full passes); 0.2 s strips of key actions;
`readcheck.mjs` (exit 0/1/2; caught both too-short holds in our test); `asr_check.py` (every voice line must
transcribe back); `ffmpeg -af ebur128` + `blackdetect`; cuecheck; "not the demo" comparison; sign-off grep.
Render tools exit 1 on any page error or missing script, and print `optional file missing` for fonts/fetches.
Debug pages in demos: `?test=sheet|model|frame`, `?all=1`, `?scene=engineDemo` render model sheets from the real engine.

---

## 5. Style catalog (all 43)

Legend. **Tech:** 2D = Canvas2D/SVG/DOM only (fast here); GL2D = 2D drawing + a WebGL2 compositor or shader
pass (works here via SwiftShader, slow); 3D = three.js (GPU strongly preferred). **Here:** measured or
expected CPU behaviour in this container. Speeds are per 1920x1080 frame unless noted.

### Hand-drawn & painting
| Style (slug) | Looks like | Key techniques | Tech / here | Client fit |
|---|---|---|---|---|
| Crayon Picture Book (`crayon-book`) | Picture-book page drawn live in wax crayon on toothy paper + watercolour wash | wax adhesion to paper tooth, boil, wash resisted by wax, child-logic perspective | GL2D / slow (expected) | Kids brands, family products, thank-you/year-in-review cards, "hidden message" reveals |
| Watercolor Brush (`watercolor`) | Self-painting journal page, translucent strokes with dry-brush flying white, hand notes | ribbon + bristle strokes, paint-in progress, sprite cache, mist erase, palette-as-data | 2D / **0.12-0.4 s at 1080x1920, tested end to end** | Premium nature/food/farm/travel stories, recipes, process explainers, wellness, real-estate neighbourhood journals |
| Chinese Ink Wash (`ink-wash`) | Xieyi ink on rice paper, five ink tones, one red seal, mostly empty paper | bristle brush engine, loaded strokes, bleed compositor, ink-bloom transitions, handscroll pan | GL2D / slow (expected) | Luxury/cultural brands (tea, spirits, calligraphy-adjacent), calm premium, Asian markets |
| Impasto Oil Painting (`impasto`) | Moving palette-knife oil painting, raking light on paint ridges | reference -> coarse-to-fine knife strokes, height-field lighting, grey-to-colour reveal, paint-over | GL2D / **15-26 s at 1080p ss2; 1080x1920: 4.5 s ss1, 14 s ss2** | Emotional brand stories, hospitality/café/wine, art & culture, "one coloured thing" product hero, launches with a warm tone |
| One-line Drawing (`one-line`) | One continuous ink line on warm paper, never lifts; scenes morph | pressure-from-speed ink, blots, Euler-path planning, nib-follow camera | 2D / **0.4-0.55 s** | Minimal premium ads, brand stories, founder story, milestones -> logo, consulting |
| Whiteboard Explainer (`whiteboard`) | Glossy whiteboard, single-line handwriting written in stroke order, floating markers, magnets | single-line fonts, pen speed solved to deadlines, multiply ink, window sheen, eraser rewind | 2D / **0.3-0.36 s** | Explainers 60-120 s, clinic "how the treatment works", courses, SaaS how-it-works |
| Urban Sketch, Pen & Wash (`urban-sketch`) | Sketchbook page: sepia fineliner + loose misregistered watercolour, frayed edges | stroke-time playback shader, colour arrival field, sketched figures | GL2D / slow-ish (expected) | **Real estate & architecture**, city/travel, lifestyle brands, restaurants (chef plating), hotels |

### East Asian traditions
| Style | Looks like | Key techniques | Tech / here | Client fit |
|---|---|---|---|---|
| Shadow Puppetry (`shadow-puppet`) | Dyed-hide lace puppets on a backlit cotton screen | carved pieces, lamp field x transmission compositor, jointed IK rigs | GL2D / slow (expected) | Heritage, festivals, myth-style brand origin stories |
| Ukiyo-e (`ukiyoe`) | Woodblock prints: flat blocks, carved lines, bokashi skies; handscroll camera | block-by-block printing reveal, cartouche & seals, banded waves | 2D / fast expected | Travel/tourism, Japanese food & culture, series-of-views product films |
| Red Paper-cut (`papercut-red`) | Red window-flower cut-outs, holes are light | fold-cut-unfold, rosettes, backlit projected patterns | 2D / fast expected | Lunar New Year campaigns, festive greetings, franchises ("one cut becomes many") |
| Paper-cut Lightbox (`paper-lantern`) | Layered paper-cut shadow box lit from behind | stacked lit sheets, DoF, windows lighting one by one | 3D / GPU | Mid-Autumn/gift brands, anniversaries, product unboxing keepsake |

### Print & printmaking
| Style | Looks like | Key techniques | Tech / here | Client fit |
|---|---|---|---|---|
| Risograph Print (`risograph`) | 2-3 translucent spot inks, halftone, misregistration on warm paper | plate shader, overprint mixing, registration kicks on accents | GL2D / slow (expected) | Indie brands, cafés, zines, lifestyle, merch drops |
| Halftone Dossier (`halftone-dossier`) | Retro case file: cream paper, Ben-Day dots, slammed stamps, huge headlines | dot density fields, stamps, exhibits, redaction, telop captions | 2D (SVG) / fast expected | Humorous social ads ("the case of X"), myth-busting, B2B "problem on trial", pet brands |
| Woodcut Print (`woodcut`) | Black block, light only where cut; one colour plate | carve any path, form-following hatching, mirrored block -> print | GL2D / slow (expected) | Craft brands (breweries, bakeries, furniture), book trailers, heritage |
| Copperplate Engraving (`engraving`) | Natural-history plate engraving itself, then hand-coloured | `engraveShape(svg)`, burin swelling lines, magnification roundels, washes | 2D / fast expected | Museum labels, science explainers, **clinic anatomy**, craft heritage, premium spirits/watches |
| Silkscreen Travel Poster (`silkscreen-poster`) | WPA-style opaque flat inks, stepped bands, printed on camera | `ink()` any Path2D, squeegee pulls, re-ink palettes, series wall | 2D / fast expected | Tourism, trails, **event posters**, product drops (colourways), seasonal notices; scene style with content.json |

### Graphic & type
| Style | Looks like | Key techniques | Tech / here | Client fit |
|---|---|---|---|---|
| Swiss Motion Graphics (`swiss-motion`) | Grid, one typeface, one signal colour, exact snaps | grid-as-meaning, snap = beat, knife cut, re-flow, scale contrast | 2D / fast expected | Brand identity reveals, consulting/agency, events, design-led B2B |
| 60s Spy Title Sequence (`spy-titles`) | Cut-paper four-ink Saul-Bass-like titles, silhouettes, brass stabs | type as set, diagonal grid, silhouette rigs, stabs = cuts | 2D / fast expected | Event openers, conference titles, trailers, launch teasers |
| Art Deco (`art-deco`) | Gold keylines on black lacquer, airbrushed volumes, bulb marquees | counted bulb lights, threshold doors, dials, sheen sweep | 2D / fast expected | **Luxury hospitality, galas, invitations, real-estate premium**, countdowns |
| Blueprint (`blueprint`) | White line work on Prussian-blue cyanotype, drafting order | draw-on polylines, live dimensions, exploded oblique, title block | GL2D / slow (expected) | Engineering, hardware, **floor plan -> building** (real estate/construction), renovation |
| Stained Glass (`stained-glass`) | Lead-came glass lit by moving sun, projected on stone | light-as-clock compositor, piece-by-piece rigs | GL2D / slow (expected) | Heritage, legends, holiday stories |
| Pictogram Motion (`pictogram-motion`) | Beat-locked flash cards: geometric pictograms, core-graphic pattern, bold bilingual type | `G.drawFigure` poses, mask text, edit list in beats | 2D / **0.1-0.14 s** | Event openers, sports, gyms/fitness classes, "all N services" lists |
| ASCII / CRT Terminal (`ascii-crt`) | Monospace glyph grid on phosphor CRT | image -> glyph density, CRT post | GL2D / slow (expected) | Dev tools, cybersecurity, tech brands |

### Information & keynote
| Style | Looks like | Key techniques | Tech / here | Client fit |
|---|---|---|---|---|
| Data Storytelling (`dataviz`) | Real data drawn by a red-blue pencil on cream paper with pinned notes | chart picked by data type, marks pop + ripple, sonification | 2D / fast expected | Results/annual reports, consulting case results, impact stats |
| Isometric Infographic (`iso-infographic`) | Flat three-tone isometric diorama with ink labels and Isotype numbers | `Iso` depth-sorted queue, cutaways, insets, iconGrid, `shape()` any outline | 2D / **0.2-0.27 s** | **Process/supply-chain explainers, clinic/facility tours, real-estate cutaways (floors), logistics** |
| Dark Tech Keynote (`dark-keynote`) | Near-black stage, hairline grid, one accent, snap-grid UI | generated accumulation, snap grid, light reveal, number scramble, UI expand/collapse | 2D / **0.25-1.5 s, tested, premium look** | **SaaS / app launches, feature films, keynotes**, fintech |
| Living Screencast (`living-screencast`) | Redrawn hi-res product UI + low-res pixel mascot acting out the software | DOM UI, word-anchored timeline `W(id, word)`, cursor + mascot | DOM / fast expected | Product tutorials, onboarding, feature launches (needs client UI screenshots to redraw) |
| Sci-fi Hologram HUD (`hologram-hud`) | Wireframe scanned into light, target boxes, rolling digits | wireframe engine, scan growth, local explode, `modelFromPath` | 2D / fast expected | **Product spec walkthroughs**, e-bikes/devices/equipment, trade-show loops; scene style (content.json) |

### Cartoon & anime
| Style | Looks like | Key techniques | Tech / here | Client fit |
|---|---|---|---|---|
| 1930s Rubber Hose (`rubber-hose`) | B&W hot-jazz cartoon, everything dances | constant-width ink + boil, film damage, big-band sampler score | 2D / fast expected | **Food & drink**, retro ads, jingles (bouncing-ball singalong) |
| 80s Cel Anime (`cel-anime-80s`) | Flat cels over airbrushed neon backgrounds, VHS on CRT | cel paths, painted plates, `core/post/crt.js` | GL2D / slow (expected) | Music videos, nightlife, gaming, nostalgia campaigns |
| Sci-Fi Sitcom Toon (`scifi-toon`) | Adult-swim style boiling outlines, portal worlds | toon vector engine, lip-sync envelopes | 2D / fast expected | Comedic social ads, tech brands with humour |
| Mid-century Cartoon (`midcentury-toon`) | 1950s UPA flat colour off-register, classroom narrator, cool jazz | off-register cels on twos, limited animation (only hands move), call-outs, numbered medallions | 2D / fast expected | **How-to / set-up guides, clinic patient instructions, safety cards, recipe cards, store notices**; scene style |

### Games
| Style | Looks like | Key techniques | Tech / here | Client fit |
|---|---|---|---|---|
| 16-bit Pixel RPG (`pixel-rpg`) | 320x180 indexed-palette RPG, dialog boxes, chip music | indexed framebuffer, palette collapse/flood, save files | 2D / fast expected | Gaming, nostalgia, "level up" growth stories, recruiting |
| HD-2D (`hd-2d`) | Pixel sprites in a lit fogged 3D diorama, tilt-shift | billboards, point lights, DOF + tilt-shift | 3D / GPU | Game trailers, fantasy, chapter-based stories |
| Microgame Frenzy (`microgame`) | WarioWare-style rapid games, each in a different art style | per-medium shaders, speed-up structure | GL2D / slow (expected) | Social shorts, onboarding, energetic promos |
| Game Show Flat (`game-show`) | Candy-coloured rhythm-game variety show, judgement words | SVG mascots, tempo grid, call-and-response | 2D (SVG) / fast expected | Year in review, product line-ups, playful brands |

### Cinema & eras
| Style | Looks like | Key techniques | Tech / here | Client fit |
|---|---|---|---|---|
| 1920s Silent Film (`silent-film`) | Ink-and-silver engraved world, flickering 4:3 print, intertitles, piano | `Redraw` (real footage -> ink drawing), `FilmPost` damage pass | GL2D / slow (expected) | Retro brands, bakeries/heritage, comedy; **turning client footage into period drawings** |
| Liminal Found Footage (`backrooms`) | 90s camcorder in endless fluorescent rooms | three.js world, VHS shader, OSD | 3D / GPU | Horror/ARG/game teasers (rarely client-safe) |

### Materials & 3D
| Style | Looks like | Key techniques | Tech / here | Client fit |
|---|---|---|---|---|
| Brick Toy (`brick-toy`) | Stop-motion toy bricks on a real desk, macro lens | brick geometry + clearcoat plastic, held poses on twos, HDRI | 3D / GPU | Toys/kids, "building the company", product assembly |
| Paper Pop-up Book (`paper-popup`) | Cut-paper actors in a pop-up book on a real desk | cut meshes, book open/page curl, hand DOF | 3D / GPU | Children's brands, story films, tutorials |
| Tilt-Shift Miniature (`tilt-shift`) | Photoreal town as a tabletop model, time-lapse stutter | procedural city, traffic sim, tilt-shift DOF band | 3D / GPU | **City promos, real estate, transport**, events |
| Low-poly Island (`lowpoly-island`) | Faceted iso world, every piece lands with a note | hex growth schedule -> notes, ortho post | 3D / GPU | Calm brand worlds, growth stories, game trailers |
| Glass Product Render (`glass-product`) | Fictional glass/metal product in black studio, strip-light sweeps, caustics | strip-light PMREM per frame, transmission + dispersion, exploded snap, comet pulses | 3D / **68-120 s per frame here (tested; stills only)** | **Premium product launches**, consumer tech, beauty/skincare bottles |

**CPU-friendly shortlist for client reels here:** dark-keynote, watercolor, one-line, whiteboard,
iso-infographic, dataviz, swiss-motion, midcentury-toon, hologram-hud, engraving, silkscreen-poster,
art-deco, halftone-dossier, pictogram-motion, rubber-hose, ukiyoe, spy-titles, living-screencast.
**Painterly hero styles that work but slowly:** impasto (budget ~4.5 s/frame at 1080x1920 without
supersampling), urban-sketch, ink-wash, crayon-book, risograph, woodcut, blueprint (all WebGL compositors
on SwiftShader). **Need a GPU machine:** glass-product, tilt-shift, brick-toy, paper-popup, lowpoly-island,
hd-2d, paper-lantern, backrooms.

**Quick picker by client type**
| Client job | First picks | Alternates |
|---|---|---|
| Premium brand story / founder story | impasto, one-line, watercolor | ink-wash, urban-sketch, engraving |
| SaaS / app launch, feature reel | dark-keynote | living-screencast, swiss-motion, hologram-hud |
| Physical product launch | hologram-hud (CPU), glass-product (GPU) | dark-keynote light reveal, silkscreen product drop |
| Explainer / how it works | whiteboard, iso-infographic | midcentury-toon, dataviz, blueprint |
| Real estate / architecture | urban-sketch, iso-infographic (cutaway floors) | blueprint (plan -> building), art-deco (luxury), tilt-shift (GPU), watercolor neighbourhood journal |
| Food / restaurant / café | watercolor (recipe), impasto (warm café) | rubber-hose (retro fun), risograph (indie), midcentury recipe card, urban-sketch (chef) |
| Clinic / health | midcentury-toon (patient instructions), whiteboard (treatment explained) | iso-infographic cutaway, engraving anatomy plate, one-line (calm) |
| Consulting / B2B | swiss-motion, dataviz (results) | iso-infographic (process), halftone-dossier ("the case of"), one-line |
| Events / hospitality / galas | art-deco, spy-titles | silkscreen-poster, pictogram-motion |
| Festive campaigns | papercut-red (Lunar NY), paper-lantern (Mid-Autumn) | crayon-book (holiday card), stained-glass |
| Playful social ads | halftone-dossier, scifi-toon | game-show, microgame, rubber-hose |

**98 extra style prompts:** `styleboard/opuscar98_styles.json` holds a reusable `prompt_en` for each of the
98 OPUSCAR shots (e.g. #12 Technicolor impasto, #24 Dufy watercolour ballet, #42 Warhol silkscreen,
#53 transparent watercolour, #59 pen & wash field sketch, #61 80s airbrush + callouts, #79 street stencil,
#91 linen postcard, #93 soft pastel, #94 scrimshaw). Each prompt is a precise recipe (palette hex values,
coverage percentages, grain, signature shot, cut rhythm, "avoid"). They name real artists/films as references:
use as grammar, never name them in client films. 77 of the 98 are 2D.

---

## 6. How to run it here (tested 12 Oct 2026)

### 6.1 Setup that works (do NOT run `setup.sh deps` unmodified)
`setup.sh deps` runs `node node_modules/playwright-core/cli.js install chromium-headless-shell`, which for
playwright-core 1.63 wants revision 1243 and would download a second browser. Do the steps by hand:

```sh
LIB=/path/to/lemo-test/lib            # a copy of references/lemo-opuscar (short path; see espeak note)
cp -r /home/user/main/references/lemo-opuscar "$LIB"          # 14 s, 177 MB
cd "$LIB"
npm install --no-audit --no-fund --loglevel=error              # 2.3 s (playwright-core 1.63, three 0.170)
export PLAYWRIGHT_CHROME=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell   # works with pw-core 1.63
uv venv --quiet --python /usr/bin/python3.12 .venv && uv pip install --quiet --python .venv/bin/python -r requirements.txt   # core tier, 9 s
uv pip install --python .venv/bin/python -r requirements-voice.txt    # kokoro-onnx, edge-tts, faster-whisper: 19 s
sh tools/fetch.sh voice                                                # Kokoro model 354 MB from GitHub Releases: 19 s
uv pip install --python .venv/bin/python -r requirements-music.txt    # numba: 14 s
sh tools/fetch.sh instruments vsco2ce   # 414 MB, ~5 s; also karoryfer (78 MB), salamander (229 MB), vcsl (285 MB), freepats (416 MB, 15 s); all = 1.4 GB
```
Kokoro needs Python 3.11-3.13 (system 3.12/3.13 fine). The skill's normal home is `~/lemo-opuscar`
(`LEMO_OPUSCAR_HOME` overrides; `sh .claude/skills/lemo-opuscar/scripts/setup.sh` does a sparse clone from
GitHub without demo sources, posters or styleboard, and `setup.sh demo <slug>` adds one demo; we did not run
it, we copied the local clone). The clone `references/lemo-opuscar` must stay untouched; work in a copy.
Don't change existing `core/` files in the copy; add patched copies beside them or next to the project (`mux_fixed.sh` can live anywhere; a no-timeout `still.mjs` copy must sit in `core/render/` because it imports `./page.mjs`).

### 6.2 Results
| Test | Command | Result |
|---|---|---|
| Impasto demo stills 1080p | `node core/render/still.mjs styles/impasto/demo 5 20 28.58` (after fetching fonts) | 15.3 s, 26.3 s, then **`page.screenshot: Timeout 30000ms exceeded`** on the third frame. SwiftShader WebGL |
| one-line / whiteboard / iso-infographic / pictogram-motion demo stills | `still.mjs styles/<slug>/demo 3 <frame_sec>` | 0.40-0.55 / 0.30-0.36 / 0.20-0.27 / 0.10-0.14 s per frame, correct output |
| dark-keynote demo stills | `still.mjs styles/dark-keynote/demo 2 12 8.4 36` | 0.25-1.5 s per frame, correct, looks premium |
| Demos at `--size 1080x1920` | `still.mjs ... --size 1080x1920` | **Cropped**: left 1080 px of the 16:9 frame in the top 1080 rows, rest blank/background |
| Vertical watercolour reel (own page, demo engine) | `films/wc-reel/` (see 6.4) | Stills 0.12-0.4 s; 8 s video 192 frames **in 14 s** with 3 workers (an earlier 6 s run took 24 s) |
| Vertical impasto plate (own page, demo engine) | `still.mjs <proj> ... --size 1080x1920 --q ss=1` | **4.5 s/frame at ss=1, 14 s/frame at ss=2** (single worker). See 6.3 for a full clip |
| Kokoro TTS | `.venv/bin/python core/tts/tts.py lines.json voices/` | Works offline: 2 English lines (`bf_emma`) in 30 s incl. model load |
| Whisper ASR check | `core/tts/asr_check.py lines.json voices/` | **Fails, exit 2**: `ProxyError 403` (huggingface.co blocked; hf-mirror.com also blocked) |
| edge-tts | `core/tts/tts_zh.py` | **Fails, exit 2**: speech.platform.bing.com blocked |
| Sampler + foley mix | own `mix.py` using `S.render`, `S.room`, `sfx` | Works; piano/harp/cellos/violas/glockenspiel rendered in seconds |
| Mux + loudness | `sh core/render/mux.sh video.mp4 mix.wav out.mp4 24 1` | **Fails on ffmpeg 6.1** ("only 5.1 s of 8.0 s could be decoded"); patched copy: -14.1 LUFS, LRA 3.5, peak -1.2 dB, 12 s |
| readcheck | `node core/render/readcheck.mjs <proj> --size 1080x1920` | Works (1.3 s); flagged both too-short holds, passed after extending |
| events | `node core/render/events.mjs <proj> --size 1080x1920` | Works |

### 6.3 Impasto video at 1080x1920 (3 s, 72 frames, ss=1, 3 workers)
`node core/render/video.mjs <proj> --fps 24 --workers 3 --size 1080x1920 --q ss=1 --out <proj>/out/video_ss1.mp4`
finished in **244 s for 72 frames (3.4 s per frame effective, ~0.3 fps)**, exit 0, 1080x1920, no black
frames, knife paint-in and grey-to-colour wave intact (some other test renders shared the CPUs part of the
time). Extrapolated: 15 s reel at 24 fps (360 frames) ~ 20 min, 30 s ~ 40 min; with ss=2 roughly 3x that.
The page (`films/imp-reel/index.html` in scratch) reads `?ss=` so previews can run at ss=1 and finals at ss=2
on a GPU machine.

**three.js check (glass-product demo, 1080p):** one frame takes **68-120 s** on SwiftShader, so the stock
`still.mjs` fails at the 30 s screenshot timeout; a copy with `page.screenshot({..., timeout: 0})` rendered
correct frames (dispersion, caustic rings, frosted glass). Usable here for posters/thumbnails, not video
(a 15 s reel would be 7-12 h on one worker).

### 6.4 The tested vertical project layout (skill mode: project outside the library)
Files in `/tmp/claude-0/-home-user-main/e4f36c47-85ff-5efa-82ed-895fc9328db0/scratchpad/lemo-test/films/wc-reel/`
(scratch, may be gone): `index.html` (page contract, layout from `innerWidth/innerHeight`, `TEXTS`, `EV`),
copied `engine.js` + `plants.js` from `styles/watercolor/demo/`, `paper.jpg` (paper.py with W,H = 1080,1920),
`fonts/` (Cormorant Garamond Italic woff2 from Google Fonts CSS2, Caveat from google/fonts GitHub),
`lines.json` (Kokoro), `mix.py` (sampler + sfx + voice + ducking), `build.sh`:
```sh
cd "$LIB"
node core/render/events.mjs "$HERE" --size 1080x1920
node core/render/video.mjs "$HERE" --fps 24 --workers 3 --size 1080x1920 --out "$HERE/out/video.mp4"
"$LIB/.venv/bin/python" "$HERE/mix.py"
sh mux_fixed.sh "$HERE/out/video.mp4" "$HERE/out/mix.wav" "$HERE/wc-reel.mp4" 24 1
```
The tested 9:16 impasto page, condensed (copy `styles/impasto/demo/engine/{impasto,plate}.js` into
`<proj>/engine/`; title is a DOM div faded in by `render`):
```js
import { Impasto, Strokes, KNIFE, hex } from './engine/impasto.js';
import { Ref, paintRef } from './engine/plate.js';
const VW = innerWidth, VH = innerHeight, SS = +(new URLSearchParams(location.search).get('ss') || 2);
window.DUR = 3;
const E = new Impasto(document.getElementById('c'), { W: VW, H: VH, ss: SS });
const CUP = [VW * .5, VH * .63], R = new Ref(VW, VH, 1);           // flat value-planned reference
R.fill(c => c.rect(0, 0, VW, VH * .7), '#a86a40', { dir: 90, maxR: 40, group: 1 });          // wall: big planes
R.fill(c => c.rect(0, VH * .68, VW, VH * .32), '#5a3420', { dir: 0, maxR: 36, group: 3 });   // table
R.fill(c => c.rect(CUP[0] - 160, CUP[1] - 60, 320, 46), '#c8342a', { dir: 0, maxR: 8, detail: .4, group: 5 }); // accent band
// ... more shapes (gradients allowed as fills; small maxR + detail<1 = fine strokes at the focus)
const S = paintRef(R, { R: [40, 20, 10, 5], seed: 3,
  rev: (x, y) => Math.hypot(x - CUP[0], y - CUP[1]) / 900,         // colour arrives as a wave from the cup
  app: (x, y, level) => y / VH * .6 + level * .18 });              // paint-in top->bottom, coarse first
const B = E.batch(S.data()), TEX = E.texture(R.ctx.canvas), dyn = new Strokes(64);
window.render = t => {
  E.begin();
  const o = { t, cam: { x: VW / 2, y: VH / 2, zoom: 1 }, grey: 1, reveal: 1.2, revDur: .25, appear: 0, appDur: .3 };
  E.under(TEX, VW, VH, { ...o, alpha: Math.min(1, Math.max(0, (t - .5) / .7)), revC: [CUP[0], CUP[1], 900] });
  E.draw(B, o);
  dyn.clear(); /* push moving strokes (steam) with fixed seeds */ E.drawNow(dyn.data(), { t, cam: o.cam, grey: 0, run: .2 });
  E.finish({ vig: .3, expo: 1.03 });
};
window.render(0); window.READY = true;
```

Library files are served at `/core/...`, `/node_modules/...`; the project at `/@film/`. Classic-script
engines (watercolour) declare globals `W=1920,H=1080` in `engine.js`: don't reuse those names, use your own
`VW/VH` from `innerWidth/innerHeight`.

### 6.5 Gotchas and fixes
1. **Demo fonts are not in git.** Every demo dies at load with `[pageerror] A network error occurred.`
   (a `FontFace`/`document.fonts.load` of a missing file) after an `optional file missing: .../fonts/X.ttf` line.
   Fix: read the demo's `index.html` / `fonts.css` / `CREDITS`, download the files from
   `https://raw.githubusercontent.com/google/fonts/main/ofl/<family>/<File>[wght].ttf` (works; 9 fonts in 3 s)
   or the Google Fonts CSS2 API (works; returns woff2 per subset). A TTF saved under a `.woff2` name loaded fine.
   Demos also lack voices/music/audio (gitignored), so their `build.sh` cannot rebuild the soundtrack.
2. **16:9 only.** Demos hard-code `width=1920 height=1080`; vertical must be authored. Engines that take
   `{W,H}` (impasto `new Impasto(canvas,{W,H,ss})`) or draw in local coordinates (watercolour, iso, toon engines)
   port easily; full demo films do not.
3. **WebGL = SwiftShader** (the tools print `[note] WebGL runs on software rendering`). Budget: impasto
   1080x1920 at ss=1 measured 3.4 s/frame effective with 3 workers, so 15 s @ 24 fps = 360 frames is ~20 min
   (workers contend: SwiftShader is itself multi-threaded; load average hit ~20 on 4 CPUs). Use `ss=1` + mux grain 0,
   or render at 12 fps for previews. Frames over 30 s fail: `still.mjs`/`video.mjs` call `page.screenshot`
   with Playwright's default 30 s timeout; lower supersampling or use a copy with `timeout: 0`:
   `sed "s/type: 'jpeg', quality: 92 }/type: 'jpeg', quality: 92, timeout: 0 }/" core/render/still.mjs > core/render/still_nt.mjs`
   (same edit for `quality: 95` in `video.mjs`).
4. **`mux.sh` false "damaged audio" on ffmpeg 6.1.** It measures decoded length from the last `out_time` of the
   loudnorm pass; ffmpeg 6.1 reports ~2.9 s less (loudnorm lookahead), and the tolerance is max(5 %, 0.15 s), so
   every mix shorter than ~58 s is rejected. Fix (copy, don't edit the library):
   ```sh
   sed 's/^DEC=\$(echo "\$M" | grep/DEC=$(ffmpeg -hide_banner -nostats -progress pipe:2 -i "$A" -f null - 2>\&1 | grep/' \
     "$LIB/core/render/mux.sh" > mux_fixed.sh
   ```
5. **No ASR check here** (Whisper model download blocked). Options: skip and listen/inspect waveform; bring a
   faster-whisper model folder from elsewhere and pass `--model /path`; or use a paid transcription API only with
   the user's OK. Kokoro output is deterministic, so a line that was checked once stays checked.
6. **No edge-tts here.** English: Kokoro (voices `af_*`/`am_*` American, `bf_*`/`bm_*` British; unknown name prints
   the list). Chinese offline Kokoro "sounds plain". For premium client VO we will usually want ElevenLabs
   (our existing pipeline) and use Kokoro only as scratch VO.
7. **espeak-ng path limit**: Kokoro's espeak data path must be < 160 bytes (realpath); `tts.py` checks. Our
   scratchpad path passed, but keep the library at a short path.
8. **`video.mjs` renders the whole `DUR`**, no `--from/--dur` (our `motion-studio/render.mjs` has it). For partial
   renders let the page read `?dur=` / `?t0=` from `location.search` (`--q`). Each parallel render needs its own
   `--out` (lock file). No motion blur, 24 fps default (pass `--fps 30/60` if the page is smooth).
9. **Render tools exit on any page error** (`[pageerror]`) or a 404 on a script/module: good for CI, but one bad
   frame kills a long render; run `still.mjs --range` over the whole film first.
10. **Fonts in render**: never link Google Fonts at render time; self-host in `fonts/` (CJK: subset with the CSS2
    API `&text=`). `core/fonts/` ZCOOL KuaiLe has only ~200 glyphs.
11. Background processes: the tools clean up their own segment dirs/locks; `RENDER_SLOTS` limits concurrent renders.

---

## 7. Where it plugs into our A-to-Z reel pipeline

Our current engine (`motion-studio/`, see `knowledge/our-pipeline.md`) already has: `window.seek(t)` pages,
60 fps renders with subframe motion blur, springs, beat grid, contact-sheet critique loop, ElevenLabs VO,
two-pass loudness. Its gaps (from that note): reference-driven art direction, typography/layout system,
imagery, real music, captions/SRT, multi-format, review loop. Lemo-Opuscar fills several of those.

| Stage | What to take from Lemo-Opuscar | Files |
|---|---|---|
| **Intake** | One-round question list + default table; "client's own material" question; storyboard yes/no | `DIRECTOR.md` §1, `AGENTS.md` Workflow 1 |
| **Concept** | Benchmark (learn / don't learn); story rules (hook in 3 s, one turn, echo ending, one native move); 3 candidate structures then choose | `DIRECTOR.md` §2-4 |
| **Style choice** | 43 `STYLE.md` + 98 OPUSCAR prompts as a menu; `style.json` `uses`; our picker table (§5). Write our own house styles in the `styles/_template` format (11 sections) | `styles/*/STYLE.md`, `styleboard/opuscar98_styles.json` |
| **Script** | VO rules: one idea per line, numbers spelled for TTS / digits on screen, voice character from `STYLE.md` §7; scene-style information order + hold times for ads | `TECHNIQUE.md` §4, scene-style §11 tables |
| **Storyboard** | 6-9 key shots rendered with the real engine, tiled with `sheet.py`, plus logline and biggest doubt | `DIRECTOR.md` §5, `core/render/sheet.py` |
| **Build** | Page contract (`render/DUR/READY/EV/TEXTS`), determinism rules, `core/lib.js` helpers, lift a style engine into the project (keep MIT notice, strip sign-off), camera grammar tables, in-medium transitions | `TECHNIQUE.md` §2, `styles/<slug>/demo/engine*` |
| **Sound** | Cue map first; sampler score in the style's palette; procedural foley from `EV`; mix rules; silences; J/L cuts | `core/audio/*`, `DIRECTOR.md` §6, `STYLE.md` §7 |
| **Review** | `readcheck.mjs` (add `window.TEXTS` to our pages), cuecheck pattern (0 ms target), 0.2 s strips, "failures we saw most", not-the-demo check | `core/render/readcheck.mjs`, `DIRECTOR.md` §10-11 |
| **Render** | Either their `video.mjs` (24 fps, fast JPEG pipeline, parallel workers) or our `render.mjs` via `window.seek = window.render` shim (60 fps + blur). Painterly WebGL styles: 24 fps, ss=1 here, or a GPU box | `core/render/video.mjs` |
| **Delivery** | mp4 + poster + srt + TREATMENT + CREDITS (with sampler credit lines) + one-command build.sh; -14 LUFS via (patched) `mux.sh` | `DIRECTOR.md` §11, `core/render/mux.sh`, `srt.py` |

**Recommendation.** Treat Lemo-Opuscar as the **style bible and technique library**, not as the pipeline:
1. Adopt `DIRECTOR.md`'s treatment format and checks as our concept/treatment stage (it is better than what we have).
2. Build 9:16 house templates by porting the CPU-friendly engines (start with dark-keynote, watercolour,
   iso-infographic, one-line, midcentury-toon, hologram-hud) into `motion-studio` pages with the
   `render`/`seek` shim; impasto as the premium painterly option, budgeted for software GL or a GPU render box.
3. Use `core/audio/sampler.py` + the CC0 packs for real-instrument scores and `sfx.py` for foley; keep
   ElevenLabs for final VO, Kokoro for scratch VO.
4. Add `window.TEXTS` + `readcheck.mjs` and a cuecheck step to our critique loop.
5. Don't use the skill's "make me a film" flow directly for clients: it is 16:9, 24 fps, film-like (30-60 s
   stories) and needs edits to delete demo sign-offs; it also lacks client-specific stages (brand assets,
   CTA, safe zones, multi-format, versioning).

---

## 8. Pitfalls

- **Rebuilding the demo instead of directing.** Their rule: write the treatment before opening `DEMO.md`/demo
  code; use the demo only for techniques; 4 of 6 structural choices must differ. Swapping a scene style's
  `content.json` is "a technical check, never the way to deliver".
- **Demo sign-offs** ("LemoLab x Claude Opus 5.5", "Lemo-Opuscar") are baked into demo code and end cards. Grep
  and watch the last seconds before delivery.
- **Fan-film content** (Asian Games pictograms, Claude Code UI/Clawd, Best Picture films) and named references
  must never reach a client film. No real logos/brands unless the client owns them.
- **Credits**: using `piano` (Salamander) or `drum_kit` requires the CC BY credit line in CREDITS; edge-tts voices
  are not cleared for commercial use.
- **16:9 assumptions everywhere** (canvas sizes, `const W = 1920, H = 1080` globals, layouts, subtitle positions).
  For reels also respect platform UI safe zones (keep text out of roughly the top 250 px and bottom 400 px of
  1080x1920 and the right-hand action rail); Lemo has no notion of these.
- **24 fps and no motion blur** by default; fine for painterly/print styles (many step on twos anyway), weaker
  for slick keynote motion where our 60 fps + blur looks better.
- **Software WebGL**: painterly WebGL styles are 15-80x slower than the 2D styles here, and several hundred times
  slower than the author's GPU (the impasto demo's 952 frames took ~30 s there per its DEMO.md; 15-26 s per frame
  here). 3D styles need a GPU; screenshot timeout at 30 s per frame.
- **mux.sh on ffmpeg 6.1** rejects short films (patch above). **Whisper and edge-tts blocked** in this container.
- **Missing fonts** crash pages with a misleading "network error"; always self-host every font the page loads.
- **Determinism traps** called out per style: strokes built inside `render(t)` without a fixed seed boil and
  disagree across workers; touching a `const` before declaration in async init leaves `READY` false (render times
  out after 180 s); WebGL VAO left bound rewires attributes (impasto DEMO build notes); `half` is a reserved word
  in GLSL ES 3.00.
- **Readability**: the reading-time rules are strict and right; short reels tempt us to cut text early. Fewer
  words per screen instead.
- **Low end**: synthetic/sampled scores get bass-heavy on phones; measure band energy, no pads below MIDI 48.
- **Loudness**: hot bass peaks push loudnorm into dynamic mode and miss -14 LUFS; limit peaks ~3 dB first.
- **Expect cost**: their estimate is 30-60 agent minutes and many tokens per 30-60 s film on a Mac GPU; here,
  painterly WebGL renders add tens of minutes.
