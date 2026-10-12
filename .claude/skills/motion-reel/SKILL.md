---
name: motion-reel
description: The studio's entry point for every video job, from one prompt to delivered files - motion-graphics reels, launch and promo videos, product demos, explainers, ads, showreels, brand stories, mascot/character moments, collage B-roll, captioned clips - for clients or for us. Runs the A-to-Z workflow (intake, research, art direction from references, concepts, script and voice, treatment, styleframes, build, sound, gated review, render, multi-format delivery, revisions) and routes the build to HyperFrames, the motion-studio canvas engine, Lemo-Opuscar styles, Claude Animation Base or collage B-roll. Use it first whenever a video is asked for, even if another video skill also matches.
---

# Motion reel: the A-to-Z workflow

The goal is client work worth $10,000: a film with one clear idea, real brand material, art direction taken
from references, motion with weight, a sound mix that was measured, and nothing left that looks like an AI
default. Everything below exists to stop the cheap fallback (centred text on a flat background, grey-bar
placeholder cards, a redrawn logo, everything fading in, a slideshow of equal beats).

Read `motion-studio/knowledge/README.md` first: it says which reference covers what. Paths below are relative
to the repo root.

## Modes
- **Autopilot (default).** The user writes one prompt. Ask ONE round of questions only for essentials the
  prompt leaves open (stage 1), then run every stage, decide at each gate yourself, log every decision in
  `PROJECT.md`, and deliver. Stop again only to approve paid generation or when something is truly blocked.
- **Guided.** When the user or client asks for approvals: pause after concepts (stage 4), after script and
  voice (stage 5), after styleframes (stage 7) and after the draft cut (stage 10). One message per gate,
  with a recommendation and what you need from them.

## Stage 0 · Setup (every session; containers are wiped)
1. `bash motion-studio/setup.sh` (renderer deps, Python audio libs, `references/` repos, vendored GSAP,
   HyperFrames CLI). Add `lemo` for Lemo-Opuscar styles, `voice` for Kokoro scratch voice, `music` for the
   real-instrument sampler.
2. Create the project: `cp -r motion-studio/templates/project motion-studio/projects/<client>-<piece>`.
   One folder per client deliverable; if a folder for this client already exists, work in it. Never let two
   sessions build the same piece in parallel.
3. Read `motion-studio/CLAUDE.md` (house rules). They apply to every engine.

## Stage 1 · Intake (one round of questions, then defaults)
Fill the Brief in `PROJECT.md`. Ask only what the prompt doesn't answer, all in one message:
- What is it for and what should the viewer do (CTA)? Who is it for?
- Platform, length, language(s). Default: 9:16 master, 30-45 s, plus 4:5, 1:1 and 16:9 re-layouts.
- **Voiceover: yes or no** (always ask; never decide this silently). Which voice or what character?
- Brand material: website URL, logo file, fonts, colours, product screenshots, photos, past ads.
- References they love, and anything they must or must not say (claims, data with sources, legal lines).
- Paid generation allowed (AI images/video/voice credits)? Budget?
Write the answers and every default you chose into `PROJECT.md`.

## Stage 2 · Research and asset capture
- **Brand capture.** HyperFrames `capture <url>` (screenshots, `tokens.json` colours/fonts, visible text,
  full-page image, assets) or Firecrawl `firecrawl_scrape` with branding/screenshot formats. Official logo
  via the HyperFrames `logo` resolver or the client's file; never redraw a logo from a description.
  Self-host every font (no font CDN at render time). Log each asset with source and licence in `manifest.json`.
- **Market and audience.** Competitors' ads (Facebook Ads `ads_library_search`, Apify), customers' own words
  (reviews, comments), what everyone in the category says (so the film can say something else).
- **Facts.** Every number that will appear on screen gets a source and a date in `PROJECT.md`. No invented
  numbers, reviews, clients, testimonials or deadlines. Examples are labelled as examples.
- Write `brand.md` from what was captured (colour roles, type system for 1080x1920, safe zones, voice).

## Stage 3 · References and art direction
- Collect 3-6 references (client favourites, the best ads in the category, award-level motion). Measure each:
  `python3 motion-studio/tools/pacing.py ref.mp4` (rest share, quiet runs, transitions, beat rhythm, energy
  map) plus palette hexes and type sizes from frames. Write what to take (the grammar) and what to leave (the
  content). Method: `knowledge/onetake-principles.md` §3.
- Browse the style menu before choosing a look (table in stage 8): HyperFrames blueprints and 447 registry
  items (`knowledge/hyperframes.md` §4-5), Lemo-Opuscar's 43 styles and 98 style prompts
  (`knowledge/lemo-opuscar.md` §5), Claude Animation Base acting (`knowledge/claude-animation-base.md` §4),
  collage routes (`knowledge/gbro-collage-broll.md` §4), brand UI systems (`.claude/skills/awesome-design-md`).
- Fill section 3 of `docs/treatment.md`: design read, palette by role, type in motion, layout and focal
  points, ONE signature device, motion vocabulary and transition rule, texture, sound world, banned list.

## Stage 4 · Three concepts
Three concepts with different central visual ideas (one element that transforms through everything; a dive
through scale; a chain reaction; before/after split; a world built from the brand's material...), not three
versions of one layout. For each: the picture in one line, the first 2 s, what survives each transition, how
the message is physically in the image, style and engine, risk and render cost (`docs/treatment.md` §2;
doctrine in `knowledge/onetake-principles.md` P3 and `references/hyperframes/skills/product-launch-video`
pitch round). Pick the strongest (autopilot) or present them (guided). Never reuse the previous client's
concept, palette or camera language.

## Stage 5 · Script and voice
- Script in the client's language with an English check line under each line when the user can't read it.
  Hook in the first 2 s; teach or show one thing before the CTA; one idea per line; word budget ≈ 2.4 words
  per second; an alternative hook line. Rules from the brief (tone, banned words, no em dashes if asked).
- Voice: ElevenLabs (`creative_list_voices` → pick or design a voice → `creative_generate_speech`; several
  takes, pick the best). Kokoro (`setup.sh voice`) only for scratch timing. The approved voice is the master
  clock: get word timings (`creative_transcribe_audio`, or the TTS timestamps) into `audio/words.json`
  (`{source, duration, words:[{w,s,e}]}`). Pauses go into measured silences.
- Music plan: generated (ElevenLabs music), sampler score (Lemo `music` tier), our synth (`audio/score.py`
  pattern), or the client's licensed track. Measure the beat grid with `motion-studio/beats.py`.

## Stage 6 · Treatment and beat sheet
Finish `docs/treatment.md`: script table and the beat sheet on the voice or beat grid with columns
time | beat | voice | on screen | moving | still | link to next | audio. Self-check before building:
beat lengths vary (CV ≥ 0.25, longest ≥ 4x shortest), a real rest after the hook, every transition names
what survives it, every reaction has a visible cause, nothing important sits frozen > 4 s, the idea reads
with the sound off. For claims and timing math, run the account skill `anthropic-skills:storyboard-qa` if
available.

## Stage 7 · Styleframes (prove the look before the film)
Build 3-4 key frames in the real engine (hook, a middle beat, the proof or product moment, the end card).
Render them (`node motion-studio/stills.mjs --at ...` or HyperFrames `snapshot`), view them at phone size,
score them with the rubric in `docs/review_log.md`. Fix until every axis is 8+. In guided mode this is the
approval gate before the expensive part.

## Stage 8 · Build: pick the engine by the look

| The look or job | Engine | Notes |
|---|---|---|
| Kinetic type, UI and product demos, launch/brand reels, data, captions: most client reels | **HyperFrames** (HTML + GSAP, one paused timeline) | Master timeline and compositor for everything else. One sub-composition per scene, client copy as variables, `--batch` for variants. Search the registry before hand-building any named effect. Setup and gotchas: `knowledge/hyperframes.md` §6 (vendored GSAP, `font-family` not the `font:` shorthand, browser path) |
| Custom canvas drawing, generative or physical motion, ported 2D style engines, shots that need true motion blur | **motion-studio canvas engine** (`window.seek(t)` + `render.mjs`, 60 fps, 4 subframes) | `lib/motion.js` springs; `--from` segments in parallel. Text primitives and scene table: `projects/straightscale/index.html` |
| Painterly or illustrated worlds: watercolour, ink wash, impasto oil, whiteboard, iso-infographic, mid-century toon, dark keynote, swiss motion, art deco, silkscreen... | **Lemo-Opuscar engines**, ported into a 9:16 page (`setup.sh lemo`) | Demos are 16:9 references: author vertical pages, never crop. 2D styles 0.1-1.5 s/frame; impasto ≈ 20 min per 15 s; 3D stills only. Fonts: `tools/lemo_fonts.py`. Strip demo sign-offs and fan content |
| A character who acts: mascot, explainer host, reaction cutaway | **Claude Animation Base** (p5.brush, `--soft-gl`) | Redraw the client's own character in brand colours (never ship Clawd, Anthropic's mascot, in client work). ≈ 5 s/frame low-fill, 10x more with watercolour fills: keep inserts short, block in no-fill preview |
| Collage B-roll for an abstract line | **Collage method** (`knowledge/gbro-collage-broll.md` §4) | Route C (code-only halftone collage) is free and on-brand; Route B (generated pieces animated in code) needs approved spend |
| Photoreal imagery, product 3D, footage plates | Client footage first; else ElevenLabs/Higgs image, video or 3D generation **only with approved spend** | Composite inside HyperFrames or the canvas engine; log prompts and terms in CREDITS.md |

Specialty engines render their segment (MP4, or transparent WebM/PNG sequence) and it is placed on the
HyperFrames master timeline, or the whole film stays in one engine when the look is one style.
Building rules for every engine: deterministic pure function of time (no `Math.random`, timers or CSS
transitions; `node motion-studio/tools/seekcheck.mjs` passes), springs not easing curves, layouts from
`brand.md` with platform safe zones, every text at phone-readable size, a focal point in every frame, the
signature device present throughout, and the house banned list.

## Stage 9 · Sound
Voice (stage 5) + music + effects placed from the composition's own event times (never retyped), fewer
sounds than beats, one shared space, planned silences, a real ending (not a shimmer chord). Arrange the music
to the voice's structure, then duck it under the voice (sidechain or HyperFrames voiceover carve) so the
voice sits 10-20 dB above. Master: two-pass loudnorm to -14 LUFS, true peak -1.5 dBTP before encoding
(`projects/straightscale/finish.sh` pattern). We cannot listen, so measure: `tools/audio_qa.py` (loudness,
dropouts, mud, voice-over-music gap) and a spectrogram; ask the user to listen before final delivery.

## Stage 10 · Review (gated, at least 3 rounds, logged)
Each round in `docs/review_log.md`: phone-size contact sheet (one frame per beat), strips around every fast
moment and transition, the scored rubric (hook, readability, motion, continuity, pacing, composition, brand,
sound, message with sound off), automatic checks, then fix the three worst problems. Automatic checks:
`tools/seekcheck.mjs` · `tools/pacing.py` on the draft (compare with the references) · `tools/audio_qa.py` ·
HyperFrames `check --caption-zone` · Lemo `readcheck.mjs` for reading time. Gate list:
`knowledge/onetake-principles.md` §8. Ship only when every axis is 8+ and every automatic check passes, or the
remaining issue is written in the review log and told to the user.

## Stage 11 · Render and master
Drafts small and fast (HyperFrames `render --quality draft`, or `render.mjs --fps 15 --sub 1`). Final: HyperFrames
`render --quality delivery` (`--fps 60` for slick motion) or `render.mjs --fps 60 --sub 4` in 2-3 parallel
`--from` segments joined with ffmpeg concat (check the seams). Then mix, master and mux. Check frame count,
duration, loudness and seams on the final file.

## Stage 12 · Deliver
`deliver/vN/` (never overwrite a version): 9:16 master plus native re-layouts (4:5, 1:1, 16:9: separate
layouts sharing scenes, never a crop), cutdowns if asked, a viewing copy under 30 MB for chat, poster frame,
SRT captions, contact sheet, `CREDITS.md`, a short changelog. Send files with SendUserFile, commit and push,
and say plainly what was checked, what wasn't (e.g. nobody has listened yet, native-speaker check pending)
and what you would improve next. Offer the two unused concepts as alternatives.

## Stage 13 · Revisions
Feedback goes into `PROJECT.md` (decision table), changes are made in the source, and the next version
renders to `deliver/vN+1/` with its changelog. Re-run the review checks on what changed.

## Licences (check before using anything from `references/`)
- HyperFrames: Apache-2.0, fine. Avoid the 24 named text effects (from an unlicensed outside repo; use the
  registry equivalents), blocks that imitate other brands' UI, and the three 3D blocks with unconfirmed textures.
- Lemo-Opuscar, Claude Animation Base, collage B-roll: MIT; keep notices with copied code. Lemo: strip
  "LemoLab" sign-offs and fan-film content; credit Salamander piano (CC BY 3.0) and MuldjordKit drums
  (CC BY 4.0) when used; Microsoft edge voices are not for commercial use.
- onetake: PolyForm Noncommercial. Study its ideas through `knowledge/onetake-principles.md`; never run, copy
  or adapt its code or text in client work.
- Generated media follows the tool's terms (ElevenLabs, Higgsfield); record them in CREDITS.md.
