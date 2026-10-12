# Our pipeline so far: inventory, lessons, gaps

Written 12 Oct 2026 from the repo on branch `claude/discovery-engine-v16-ms5mxf`, the git history, the
session transcript and the rendered outputs. Purpose: everything a new A-to-Z "one prompt to a premium
client reel" workflow should know about what we have already built, what broke and why, and what is
still missing. The five downloaded reference repos (`references/`) and the 25 third-party video skills
are covered in separate notes and only listed here.

---

## 0. Summary

- **We have one working end-to-end engine** (`motion-studio/`): HTML canvas page with `window.seek(t)`,
  headless Chromium renderer with real 4-subframe motion blur, closed-form springs, beat grid, contact
  sheets, synthesized score + SFX, VO splice, sidechain ducking, two-pass loudness mastering. It shipped a
  finished 50 s Albanian reel with voiceover (`projects/straightscale/deliver/straightscale_reel_9x16_vo.mp4`,
  1080x1920, 60 fps, -14.0 LUFS, -1.0 dBTP) in about an hour of wall time.
- **A second, parallel engine** (`straightscale-reel/`, built by another session with the account skill
  `motion-video-director`) has the better process (approval gates, PROGRESS/LOG/manifest, word-level
  captions, low-res preview loop, HTTP-served modular scenes) and the better art direction (collage vs
  one gold line), but stopped at a voice-only rough cut. Same client, two timelines, two looks.
- **OpenMontage** (`openmontage-work/`) produced a clean 46.5 s 16:9 science explainer through a staged,
  checkpointed agent pipeline on Remotion, with ElevenLabs voice and music and a YouTube export package.
- **Quality reached:** technically clean, deterministic, on-beat, correct loudness. Visually it is a
  well-made kinetic-typography reel, not yet a $10k agency piece: no real brand assets (logo redrawn from
  a text description), placeholder grey-bar UI cards, top-heavy compositions with empty lower halves, no
  imagery, no 3D, one format only, synthesized music nobody listened to before delivery.
- **Biggest gaps:** real brand/asset capture, a reference-driven art-direction stage, a typography and
  layout system, imagery/3D, real music, captions/SRT, native multi-format, a client review loop with
  versions, and one project folder per client instead of parallel sessions.

---

## 1. Repo map

| Path | What it is | Status |
|---|---|---|
| `motion-studio/` | Our code-rendered motion studio, built from the guide "How to Build a Motion Design Studio With Opus 5.5" | Working, used once |
| `motion-studio/projects/straightscale/` | Finished 50 s StraightScale reel (Albanian VO) | Delivered |
| `straightscale-reel/` | Parallel StraightScale project (motion-video-director process) | Rough cut v2, awaiting approval, abandoned |
| `openmontage-work/` | Saved OpenMontage setup fixes + "Why Is the Sky Blue?" explainer | Rendered + YouTube package, not uploaded |
| `Mark AI/` | Discovery Engine v16: e-commerce product research runs | Not video; research discipline is reusable |
| `.claude/skills/motion-reel/` | Our skill wrapping motion-studio | Works, thin |
| `.claude/skills/{taste-skill,image-to-code,web-design-guidelines,awesome-design-md}` | Design skills (web-focused) | Installed, unused for video so far |
| `.claude/skills/<25 third-party video skills>` | HyperFrames (21), onetake, gbro-collage-broll, claude-animation-base, lemo-opuscar | Installed, untested (covered elsewhere) |
| `references/` | `fetch.sh` + full clones of the five reference repos (gitignored, ~800 MB) | Downloaded |

Git history (oldest first): Mark AI runs (Aug) -> OpenMontage sky explainer (4fba9cb..b9539f3) ->
straightscale-reel setup (7c478f8) -> motion-studio (845deb9) -> design skills (3d96c37) ->
straightscale-reel VO + engine (48349b1) -> motion-studio StraightScale project + faster renderer
(fac7889) -> text-only final (1507093) -> straightscale-reel storyboard v2 (d0f062c) -> VO version
(cc58488) -> VO final (22665b8) -> five video skills (ab79968). A local commit 6c5b909 (reference
repos + fetch.sh) is not on the branch yet; `references/` and the `.gitignore` change are uncommitted.

---

## 2. motion-studio: the engine

### Files
| File | Role |
|---|---|
| `CLAUDE.md` | House rules (render contract, banned looks, sound, critique loop, tool list). Only loaded when a session works inside `motion-studio/`; there is no root CLAUDE.md pointing at it. |
| `render.mjs` | `node render.mjs --fps 60 --dur 15 --sub 4 [--from 0] [--w 1080 --h 1920] [--out out/silent.mp4]`. Launches Chromium with `--allow-file-access-from-files`, opens `index.html` over `file://`, waits for `window.seek` and `document.fonts.ready`. If the page has `<canvas id="c">` it injects `window.__frame(times)` that calls `seek` for each subframe, sums `getImageData` into a Float32 buffer, averages, returns one PNG per output frame. Otherwise falls back to the guide's screenshot-per-subframe + ffmpeg `tmix`. Pipes into libx264 CRF 16 yuv420p. |
| `stills.mjs` | Contact sheet straight from `index.html` without rendering: `--from/--step/--dur` or `--at 1.2,3.4`. 50 frames in about 20 s. |
| `review.sh` | From a finished MP4: contact sheet (2 fps, all rows), 12-frame strip around a fast moment, 360 px phone test, loop check. |
| `beats.py` | librosa beat track -> `{bpm, beats, downbeats (every 4th beat), hits (onset peaks)}`. |
| `lib/motion.js` | `spring(t,k,d)` closed-form damped spring 0->1; `track(t, [[time,value],...])` stacks one spring per change; `clamp`. |
| `package.json` | Playwright 1.56.1 only (uses preinstalled Chromium at `/opt/pw-browsers`). |

### Contract (from the guide, kept)
Every frame is a pure function of time; no CSS transitions, timers, rAF or carried state; seeded noise
only; H.264 yuv420p CRF 16; one display font + one UI font; one accent; something new every 2-4 s;
banned: centered title on gradient, everything fading in, corner labels, frame borders, glow on UI,
generic particle bursts; music/SFX synthesized unless supplied; hits on the measured beat grid; -14 LUFS;
critique loop (contact sheet, score 1-10 on hook / phone readability / motion / variety / brand / sound
sync, fix the 3 worst, repeat to 8+) before any full render.

### Measured performance (4 CPUs, no GPU)
| Operation | Cost |
|---|---|
| `seek(t)` on the StraightScale page | ~13 ms |
| Playwright element screenshot (guide's method) | ~238 ms per subframe |
| In-page `toDataURL` PNG / `getImageData` | ~48 ms / ~13 ms |
| Guide renderer, 15 fps preview, 1 subframe | ~2.3 frames/s (a 60 fps x 4 sub render would have taken over an hour) |
| In-page blend, 60 fps x 4 sub | ~0.37 s per finished frame (3.6x faster); 3 s test = 70 s |
| Full 50 s, 60 fps, 4 sub, 3 parallel `--from` segments + concat | ~7.5-8 min wall clock, load avg ~5.5 |
| Master size | 34 MB (CRF 16, 60 fps, 50 s); chat upload limit is 30 MB, so a CRF 21 viewing copy (~14 MB) was sent |

Known limits: `--w/--h` only changes the viewport; the canvas and every layout constant in `index.html`
are hard-coded to 1080x1920, so 1:1 / 16:9 are not actually produced. Subframes are averaged in
gamma-encoded sRGB, which slightly darkens bright-on-dark blur trails (linear-light averaging would be
more correct). No `--scale` low-res mode, no timestamp overlay, no per-frame error logging, and
`file://` pages cannot `fetch()` JSON, so timings must be inlined in the page.

---

## 3. The finished StraightScale reel (`motion-studio/projects/straightscale/`)

### Brief (from the client message)
Business growth partner in Tirana; IG/FB organic reel; Albanian, informal "ti", English check line under
each line; teach one thing then CTA "Shkruaj ANALIZA në komente"; hook in 2 s; no founder, no invented
numbers/reviews/clients/deadlines, no prices, no em dashes, no hype words, no "1 hour", no lead chasing;
palette Gold/Crimson/Ivory/Charcoal/Marble with "no gold on ivory, no crimson on charcoal"; Playfair
Display + Montserrat; logo described in words only. Real data: ~1,800 active "cilësi" ads (Meta Ad
Library, 11 Oct 2026) and three revenue results.

### How it is built
- **`index.html` (581 lines, one canvas).** Spring presets as named pairs: `TYPE [190,27]`, `UI [260,24]`,
  `POP [320,23]`, `HEAVY [70,16]`, `sp(t, t0, preset)`. Seeded mulberry32 `rng`; procedural grain tile
  (overlay, re-seeded at 24 fps) and a value-noise marble background generated once at load.
  Text primitives: `wrap`, `measure`, `riseLine` (segments of mixed fonts/colours rising out of a clip
  mask, with in and out times; returns x-ranges so strikes/arrows can attach), `riseBlock` (staggered
  lines). Shapes: `rrect`, `withXf`, `star`, `person` (generic avatar), `arrow`, `cursor`, `strike`,
  `chip`, `logoMark` (logo redrawn from the description).
- **Scenes** are functions of absolute time (`s1 ... s11b`) listed in `SCENES = [[start, end, fn]]`;
  `run()` draws any scene within +-0.3 s of its window so exits and entrances overlap.
- **Transitions** live in `seek()`: a rotated gold-thread clip wipe from charcoal to marble on "Ja çfarë
  bën" (17.3 s), charcoal rising from the bottom for the offer (39.22 s), ivory dropping for the CTA
  (44.92 s), each with a 10 px gold edge.
- **Timeline = the voiceover.** Every `tin/tout` was set by hand from the other session's Scribe word
  timings (`straightscale-reel/plan/beats.json`) plus the 2.5 s pause cut in at 36.75 s.
- **`audio/score.py` (272 lines).** Numpy/scipy instruments: kick (pitch-swept sine + click), open/closed
  hats, clap (three-hand smear), bass, detuned-saw pad, pluck, stepped band-pass riser, impact; SFX: pop,
  tick, click, key, whoosh, thump, stamp, swish, ping. `place(buf, x, t, gain)` (handles negative start
  times). Arrangement at 120 BPM with bar lines at 1.5 + 2k s so the turn lands on a downbeat; minor
  colour for the problem, same chords centred on F major for the fix; drums drop under the brand line;
  arpeggio after the turn; riser + impact into the turn. SFX cue list mirrors `docs/shotlist.md`
  (stamps on "cilësi", click on "çmimin", keys typing ANALIZA on 16ths). Output normalised to -1 dBFS peak.
- **`finish.sh`.** (1) Builds `vo.wav`: splits the approved ElevenLabs take at 36.75 s, inserts 2.5 s of
  silence, pads to 50 s, mono to stereo. (2) Mix: music x0.3 sidechain-compressed by the voice
  (threshold 0.02, ratio 6, attack 15 ms, release 350 ms), SFX x0.4, voice, `amix normalize=0`,
  `alimiter 0.95`. (3) Two-pass `loudnorm` I=-14 TP=-1 LRA=11 (measured JSON fed back, linear mode),
  48 kHz. (4) Mux AAC 320k + faststart. (5) `review.sh`, contact sheet and poster frame into `deliver/`.
  Measured result: voice ~-20 dBFS RMS vs ducked music ~-33/-34 (12-14 dB gap), music back to -26 in the
  pause; final -14.0 LUFS, LRA 2.4, true peak -1.0 dB.
- **`docs/shotlist.md`.** Time | Albanian VO | English check | On screen, plus a rules-check paragraph.
- **Deliverables.** `straightscale_reel_9x16_vo.mp4` (final), `straightscale_reel_9x16.mp4` (text-only
  v1, kept), `contact.png`, `poster.png`.

### Build timeline (from the transcript)
19:38 brief -> 19:42 shot list -> 19:43 score -> 19:46 `stills.mjs` written -> 19:49 first contact
sheets -> 19:50 round 1 fixes -> 19:51 low-res preview (too slow) -> 19:55 benchmark -> 19:57 in-page
blending -> 19:58 round 3 fixes + parallel final render -> 19:59 score bug found from the spectrogram ->
20:06 render done -> 20:09 text-only reel delivered. 20:23 user: "Why don't you hear anybody?" ->
20:28 retimed to VO -> 20:30 render -> 20:40 VO version delivered.

### Lessons from the history (what broke, why, the rule it implies)
1. **`file://` module imports.** The guide's renderer opens `index.html` over `file://`; Chromium blocks
   the `import` of `../../lib/motion.js`, so `window.seek` is never defined and the guide's render loop
   fails. Fix: launch with `--allow-file-access-from-files` and `waitForFunction(() => typeof
   window.seek === 'function')`. Rule: wait for an explicit ready signal; better, serve the project over
   a local HTTP server (as `straightscale-reel/src/render.js` does), which also allows `fetch()` of JSON.
2. **Bar-length bug in the score.** `bar = 2 * BEAT` (1 s) instead of `4 * BEAT` (2 s): drums doubled,
   chords changed twice as fast, and a `range(25)` bar loop ran out at ~26 s, leaving 22 s of silence
   except two impacts. The agent cannot listen; it found the bug because a spectrogram and per-2 s RMS
   windows showed -180 dB from 26 s. Rule: always run objective audio checks (RMS per window, spectrogram,
   `ebur128`, re-run `beats.py` on the result and compare bar lines to the plan), derive loop counts from
   duration, and ask a human to listen before delivery.
3. **Render speed.** The guide's screenshot-per-subframe path ran at ~2-3 frames/s. Benchmarking showed
   the screenshot (~238 ms) dominated, not drawing (~13 ms). In-page subframe averaging + one PNG per
   frame gave 3.6x; `--from` segments in parallel (3 on 4 CPUs) brought a 50 s 60 fps master to ~8 min.
   Rule: measure before optimising; check segment seams (strips at 16.92 s and 33.92 s were checked).
4. **Voiceover omitted by assumption.** The brief never said "no VO"; the agent chose a text-only reel
   and the user expected a voice. Rule: an explicit intake question for VO (and every other format
   decision) before building; never decide a deliverable's modality silently.
5. **Voiceover retiming.** Retiming every scene to the approved take: on-screen text follows the voice
   phrase by phrase (still works muted), key visual events land on spoken words (counter on "tetëqind",
   click on "çmimin", rows on "reklama/faqe/telefon"). A 2.5 s pause was cut into a measured silence
   (36.6-36.97 s) so the proof figures could be read; two lines the approved script does not say were
   cut. Rule: the approved VO is the master clock; visuals never carry claims the voice script did not
   approve; insert pauses only at measured silences.
6. **Sidechain ducking + score re-arrangement.** After the VO, the score was re-arranged so the downbeat
   hits "Ja çfarë bën" (17.5 s), drums drop under the brand line, and music is ducked under the voice.
   Rule: arrange music to the VO's structure, then duck; check the VO-to-music gap numerically (10-15 dB).
7. **Critique loop findings** (rounds 1-3): text clipping off the right edge, a misread italic word, an
   overlapping exit, weak hook (bubbles enlarged), falling bubbles passing through the next line (fall
   started earlier and harder, whoosh moved), "Thuaje kudo" orientation, marble too loud, proof digits
   moved from Playfair (old-style figures) to Montserrat, counter exit, arrows appearing before their
   text row, last figure still counting when the scene leaves. Scores were "around 8" but never logged
   (no `review_log.md`), and one blemish (proof exit at ~42.3 s) shipped in v1.
8. **Loudness.** The first raw mix measured -17.4 LUFS, TP -0.2, LRA 15.8; two-pass loudnorm fixed it.
   AAC encoding moved the peak up (-0.9 -> -0.5 dB on v1). Rule: master to -1.5 dBTP before AAC.
9. **Delivery.** 34 MB master > 30 MB chat limit; send a CRF 21 copy, keep the master in the repo.
10. **Things that were right first time:** glyph coverage checked with fontTools (ë ç Ë € present, arrows
    and ticks drawn as shapes), only brief data used and sourced on screen ("Burimi: Meta Ad Library,
    11.10.2026"), the 10-day promise labelled SHEMBULL (example), generated audio kept out of git and
    rebuilt from `score.py`.

---

## 4. straightscale-reel (parallel StraightScale project, other session)

### Process (account skill `motion-video-director`)
- Preflight table (Node 22, Python 3.13, ffmpeg 6.1, Chromium-1194, Playwright 1.56.1; demucs,
  faster-whisper, rembg missing because Hugging Face and fbaipublicfiles are blocked; Freesound,
  Unsplash, Pixabay, LottieFiles blocked; Google Fonts and npm reachable).
- Project files: `PROJECT.md` (brief, approvals with timestamps, open questions), `PROGRESS.md`
  (phase/next step for resuming), `LOG.md` (append-only), `manifest.json` (fonts with OFL licence
  files, VO with ElevenLabs flow/generation IDs and voice ID).
- `plan/script.md`: ElevenLabs-ready VO block with audio tags (`[curious]`, `[thoughtful]`, `[warmly]`,
  `[confidently]`), word budget (119 words ~ 49 s at 2.4 w/s), AV table, on-screen keywords,
  pronunciation note (StraightScale said in English, alias "Strejt Skejl"), alt hook, rules check.
  Approved 19:14.
- VO: workspace voice "StraightScale - Strategist (male, 45)", eleven_v4, 4 takes (~3.1k credits,
  ~$0.56), take 4 (45.92 s) chosen; Scribe forced alignment -> `plan/beats.json` word timings
  (119/119 words match the script).
- `plan/fonts.md`, `plan/styleboard.png` (palette with 60/30/10 roles + type + code stills),
  `plan/storyboard.md` with real rendered frames (`storyboard_v2.html` -> `storyboard_v2.jpg`) and a
  table of every on-screen Albanian string with English for a native-speaker check.
- **Storyboard v1 rejected by the user: "boring, same design structures".** Self-diagnosis: every shot
  was a centred UI card on a flat background with pop-ins, plus fades, glow, particles and centred titles
  (all banned by our studio rules).
- **v2 redesign:** World 1 = ransom-note collage (torn paper, tape, label-maker strips, ransom letters cut
  from six styles of the two brand fonts, marker strikes, rubber stamps, camera shakes and zooms); World 2
  = marble and **one gold line at y = 894 in every shot** that words rise out of or drop from; Droste
  pull-back to 1,800 identical boards; frame-in-frame (the promise was a phone ad, pull back to site and
  call); logo built on the line. Critique fixes logged: S2 overflow, caption fade -> spring snap, stamp
  over labels, odometer overshoot, tape size, empty beat in S8, ads covering "falas", label behind clock,
  stray tape on pull-back, **placeholder domain removed** (no invented URLs).
- Stopped at `renders/previews/roughcut_v2.mp4` (540x960, 15 fps, voice only, 47.6 s). Music/SFX
  (planned via ElevenLabs), polish, final render and QA never happened.

### Engine
- `src/index.html` + `main.js` (captions, frame entry, font loading, `window.__ready`), `lib.js`
  (palette, `SAFE` zone `{top 220, bottom 1500, left 60, right 940}`, easing set `E.*`, `text/measure`
  with letter spacing, `logo()`, cached marble, charcoal vignette, stitch line), `fx.js` (collage
  toolkit: `paperTex`, `tornPath`, `scrap`, `halftone`, `tape`, `dymo`, `RANSOM` styles,
  `ransomLetter/Word/Width`, `marker` polyline reveal, `rubberStamp` with ink gaps, `captionStrip`,
  `goldLine`, `fromLine` mask), 13 scene modules `{id, start, end, draw(ctx,t), init?}` (1,425 lines).
- `src/render.js`: local HTTP server, `?scale=` low-res frames, `?stamp=1` time + scene-id overlay,
  `--from --to --fps --scale --out --jpg --frames-only --name --audio` (mux trimmed audio), page error
  and console error logging, sRGB colour profile flag. No motion blur, 30 fps.
- `scripts/preview.mjs`: every frame of a range at 8 fps / 0.25 scale tiled with timestamps, or a
  15 fps half-res MP4 with the mix.
- Captions: words grouped at punctuation or 4 words, strip snaps open with a spring, active word gold,
  `NO_CAPTION` windows where the same words are already big on screen.

### How it differs from motion-studio
| | motion-studio | straightscale-reel |
|---|---|---|
| Structure | One HTML file, scenes as functions | index/main/lib/fx + one module per scene |
| Serving | `file://` + flag | Local HTTP server |
| Entry | `window.seek(t)` | `window.drawFrame(t)` + `__ready` |
| Frame rate / blur | 60 fps, 4-subframe blur | 30 fps, none |
| Timing source | Literals typed from VO timings | `plan/beats.json` loaded at runtime (captions); scene times hand-set |
| Motion | Springs only | Springs + easing curves (outBack captions) |
| Captions | On-screen copy follows VO; no caption track | Word-level karaoke captions |
| Preview | `stills.mjs` sheets, full-res stills | Every-frame sheets at 0.25 scale with timestamps, low-res MP4 with audio |
| Process | Shot list then build, no approval gates | Script, storyboard, style board gates; PROGRESS/LOG/manifest |
| Audio | Synthesized score + SFX, ducking, mastering | VO only so far |
| Look | Editorial kinetic type, cards, marble/charcoal | Collage vs gold-line concept, denser frames |
| State | Delivered | Rough cut, unapproved |

Lesson: the best StraightScale reel would have been v2's art direction on motion-studio's finishing
(blur, score, ducking, mastering). Two sessions on one client produced duplicate work and divergent
timelines (47.6 s vs 50 s). One project folder and one source of truth per client.

---

## 5. openmontage-work (OpenMontage)

**What OpenMontage is** (from the saved artifacts; the clone itself is gitignored): an open-source agentic
video production framework (github.com/calesthio/OpenMontage) with pipeline types (here
`animated-explainer`), stage checkpoints (`research -> proposal -> script -> scene_plan -> assets ->
edit -> compose -> publish`, each a `checkpoint_*.json` with history), a `decision_log.json` (options
considered with scores and rejection reasons, user_visible / user_approved flags), Python tools
(`tools.video.video_compose`), and render runtimes Remotion (React/SVG), HyperFrames (HTML/GSAP) or
FFmpeg. "Atelier" mode = a bespoke hand-authored composition that must declare `art-direction.md` and may
not import the stock components; the final review checks this.

**What was done ("Why Is the Sky Blue?", 46.5 s, 1920x1080, 30 fps):**
- Research brief with 13 sources, landscape of existing explainers, underserved angle ("why not
  violet?"); proposal with 3 concepts (c2 "Sunlight, Sorted by Color" chosen), runtime choice (Remotion
  over HyperFrames because caption burn parity was Remotion-only), voice/music choices.
- `art-direction.md`: design read, taste dials (variance 5, motion 5, density 3), palette taken from the
  subject, two fonts, motion character, **one signature device** used once and echoed once, scene
  inventory (each scene has its own primary subject and framing), anti-patterns avoided.
- Scene plan with shot language, narrative role, information role, transitions per scene; storyboard
  sheet; per-scene snapshots; 731-line `Composition.tsx`.
- Audio: started on Piper (user said no paid keys), switched to ElevenLabs on user instruction: voice
  "Abby" eleven_v4, 4 takes, take 1, `atempo 1.08` to land 45.3 s ($0.55); music eleven_music_v2_5,
  4 takes, take 2 for steady level, offset 2.5 s, Scribe used to confirm no vocals ($1.20).
- `final_review.json` (technical probe, visual spot check, audio check, promise preservation, subtitle
  check, atelier stock-reuse check) and `render_report.json`; publish stage: title, description with
  sources, chapters, tags, SRT, thumbnail. Nothing uploaded.

**Lessons:**
- Proxy/sandbox fixes are real work: Remotion cannot download its Chrome from remotion.media, so
  `remotion.config.ts` reuses the HyperFrames or Playwright headless shell; Remotion forces
  `--no-proxy-server`, so `.local/chrome-via-proxy.sh` strips it and routes through `$HTTPS_PROXY`;
  Hugging Face blocked -> Piper voice from GitHub releases.
- The structured artifacts (decision log, proposal with options, art direction, final review JSON,
  publish package) are the most reusable part.
- Output quality: clean, coherent vector explainer, but captions are small, loudness -16.1 LUFS (not
  -14), 30 fps without blur, no brand work. Competent YouTube explainer, not premium.
- Remotion's licence requires a paid company licence above a small team size; check before agency use.
  HyperFrames is Apache-2.0.

---

## 6. Mark AI

"Discovery Engine v16": an e-commerce product-opportunity research engine (UK geo mode). A seeded draw of
lenses, product families and geos; candidates anchored to brands with live Meta ad counts; kill rules;
UK VAT profit math with a hard gate (GP >= GBP 20, margin >= 60 %, 3x multiple); fixed /100 rubric; HTML
dossiers; a traffic gate added after **fabricated ad counts and brand IDs were found and removed**
(f276153). Not video production. Reusable for reels: the evidence discipline (every number has a
retrieved source, `SOURCE-CONDITIONAL` labels, a correction log) and Meta Ad Library research, which is
exactly where the StraightScale "1,800 cilësi ads" data point came from.

---

## 7. Skills

### Ours
- **`motion-reel`**: collects inputs (product + URL, duration, formats, brand colours + fonts, reference,
  music), then: gather assets with Playwright -> style guide from reference -> beats -> shot list on the
  beat grid (wait for OK) -> build `index.html` -> contact sheet critique x3 -> render, sound, -14 LUFS,
  all formats -> deliver final, contact, poster + "what I'd improve". Hard rules: real product UI only,
  no randomness/timers/transitions, banned looks. In practice steps 1, 2, 4's wait and multi-format were
  skipped for StraightScale.

### Design skills and how they help reels
| Skill | What it is | Use in reels |
|---|---|---|
| `awesome-design-md` | 84 brand `DESIGN.md` files (YAML front matter tokens: colours, type scale with sizes/weights/line-height/tracking, radii, spacing; then prose: overview, components, do's and don'ts) | Template for a per-client `brand.md`; on-screen UI for "make it feel like Linear/Stripe/Apple"; realistic UI mock components (buttons, cards, inputs) instead of grey bars; type-scale discipline |
| `taste-skill` | Anti-slop frontend rules: design read in one line, three dials (variance / motion / density), AI-tell bans | Port its design read + dials into art direction; its bans map to video tells: no div-style fake UI, no three equal cards, no filled progress tracks, no fake-perfect numbers, no em dashes, no startup-slop names, no section-number eyebrows |
| `image-to-code` | Image-first: generate design images, analyse them deeply (type, spacing, colour, components), then implement to match | Styleframe-first workflow: generate or capture 3-4 styleframes per reel, extract tokens from them, then code scenes to match |
| `web-design-guidelines` | Fetches Vercel's Web Interface Guidelines and audits UI code | Minor: audit any on-screen web UI recreations; mostly web-only |

### Third-party video skills (not covered here)
claude-animation-base, embedded-captions, faceless-explainer, figma, gbro-collage-broll, general-video,
hyperframes, hyperframes-animation, hyperframes-audio, hyperframes-cli, hyperframes-core,
hyperframes-creative, hyperframes-keyframes, hyperframes-registry, hyperframes-studio, lemo-opuscar,
media-use, motion-graphics, music-to-video, onetake (noncommercial licence: not for client work),
pr-to-video, product-launch-video, remotion-to-hyperframes, slideshow, talking-head-recut (25 folders).
Routing conflict to resolve: `hyperframes` calls itself the mandatory entry point for any video request.

### Account skills read for this note
- **`anthropic-skills:motion-video-director`** (the process behind `straightscale-reel`). Golden rules:
  preflight, plan before build, explicit approval before any render, log everything, keep
  `PROGRESS.md` current, preview loop after every change, hunt assets yourself (Playwright MCP),
  read the whole skill first, kickoff message first, **never build scenes before the final VO MP3
  exists**, never print keys. Kickoff: plain-language "what I'll make / how we'll work / what you do
  now / 3-6 questions" (topic, platform, length, vibe, VO, audience/CTA, brand, personal vs commercial,
  deadline). Structure: PROJECT/PROGRESS/LOG/manifest, `plan/`, `assets/`, `src/`, `renders/previews|
  final|logs`. Workflow gates: references + story -> brief -> VO script (ElevenLabs paste block, word
  budget table 15 s = 30-38 words ... 60 s = 135-150) -> user sends MP3 -> storyboard -> style board with
  font research (Fontshare, Open Foundry, etc., licence checked) -> assets (VO intake: probe, loudness,
  transcribe, diff vs script, lock timings) -> preview approval -> final + QA. Render CLI contract
  `--from --to --fps --scale --out [--jpg]`. Director knowledge: hook -> problem -> solution -> proof ->
  CTA; on-screen text <= 6-8 words; intensity scale 1-5 by video type; motion catalogue; 9:16 safe zones
  (top ~220 px, bottom ~420 px, right ~140 px); sound trio riser/impact/whoosh; VO 10-15 dB over music;
  -14 LUFS / -1.5 dBTP; "go 3D when it matters" (2D->3D pop, Three.js, swiftshader); kinetic type
  vocabulary; four reverse-engineered reference recipes (talking-head caption reel, documentary
  storyteller edit, Slack-style SaaS launch, Frontify-style kinetic promo); 15-point QA checklist;
  native re-layout for other aspect ratios, never crop.
- **`anthropic-skills:storyboard-qa`** (hard gate before generation in the AI-video ad stack). Five audits:
  (1) timing math: VO words per shot at 2.4 w/s (2.8 UGC) + 0.5 s per boundary vs clip length per tool
  (Kling 3-5 s, Sora 12 s, Seedance up to 15 s), per shot within 0.5 s, total within 10 % and the
  platform target, silent beats budgeted explicitly; (2) continuity: every shot states what it inherits,
  its causal link (cause/effect, question/answer, claim/proof, before/after, escalation; "related topic"
  fails), motion/gaze vectors, and the whole video must be retellable in 3 sentences; (3) reference
  completeness: every element in every shot maps to a canonical reference image; (4) format fidelity
  (e.g. motion graphics: every stat traced to a source ID); (5) generation-method fidelity (multi-shot
  groups with start and end frame anchors, reference stacks, hook/payoff contract). Verdict PASS or a
  tagged fix list, max 2 iterations, never soften a FAIL. Directly reusable as our storyboard gate,
  especially timing math, causal links, claim tracing and hook/payoff.
- Not read in this pass: storyboard-ai-ad, ad-video-factory, daily-video-factory, claymation,
  scroll-craft, seedance-*, readymerce-*, strategy-*, ugc-video-script-and-storyboard-designer,
  viral-format-scout, ig-competitor-research.

---

## 8. The original guide vs what we built

| Guide element | Status |
|---|---|
| Render contract, `seek(t)`, CLAUDE.md banned list | Built (CLAUDE.md is per-folder) |
| Renderer with subframe blur | Built and made 3.6x faster; `file://` bug fixed |
| Effort xhigh/max for new videos | Session setting; xhigh used |
| Step 4: real product URL, Playwright screenshots, real logo/colours/fonts into `./assets`, never redraw UI | **Not done.** StraightScale had no URL; logo and UI were drawn from imagination (grey-bar ad and review cards) |
| Step 5: reference frame/video -> `style_guide.md` | **Not done** for either StraightScale reel |
| Step 6: state-list spec, one container that never cuts, loopable last frame | Not used |
| Step 7: springs + stacked `track()` | Built and used everywhere |
| Step 8: beats.py, synthesized score, SFX cue list, -14 LUFS | Built; score bug caught |
| Step 9: contact / strip / phone / loop + harsh critique 3 rounds to 8+ | Built; 3 rounds done, scores not logged |
| Step 10: director's brief with gates (plan, stills, rough cut, animation, polish, sound, render), `review_log.md`, `ANIMATION_GUIDE.md` + subagents for long films | Gates done only in straightscale-reel; no review log |
| Step 11: skill packaging | `motion-reel` |
| Step 12: service offer (20-45 s, original music, optional VO, real UI, all formats, 3 rounds of edits) | Not productised: no formats, no edit-round tracking |
| 1:1 and 16:9 from the same timeline | Not done (layout hard-coded) |

---

## 9. Tools in this environment, mapped to stages (noted, not called)

| Stage | Tools |
|---|---|
| Brand + asset capture | Firecrawl `firecrawl_scrape` (formats `branding`, `screenshot`, `images`, `links`), ElevenLabs `creative_create_brand_kit_from_website` / brand kits, browserbase cloud browser, Playwright (local Chromium), Google Drive (client files), Mobbin (real app UI references), Figma (often disconnected), Canva (disconnected) |
| Research / references | Facebook Ads `ads_library_search`, Apify scrapers (Instagram, TikTok, ads), TranscriptAPI (YouTube transcripts), Higgs `video_analysis_create` (reference video analysis), Firecrawl search |
| Voice | ElevenLabs `creative_list_voices`, `creative_design_voice` + `creative_save_designed_voice`, `creative_generate_speech`; `creative_transcribe_audio` (Scribe word timings, used for alignment); Higgs `create_voice`, `voice_change`, `dubbing` (localised versions) |
| Music / SFX | ElevenLabs music via flows (`eleven_music_v2_5` was used by OpenMontage), Higgs `generate_audio`, `tiktok_music_trending` (licensing caution), our `score.py` |
| Imagery / plates / 3D | ElevenLabs `creative_generate_image/video`, `creative_edit_image`; Higgs `generate_image`, `generate_video`, `generate_3d` (image -> GLB), `scene_builder_3d_*`, `upscale_image/video`, `remove_background`, `outpaint_image` |
| Multi-format | Higgs `reframe` (footage), but code scenes need native re-layout |
| Testing / publishing | Higgs `virality_predictor`, `tiktok_prepare_publish`; Google Drive for client delivery |

Container: Node 22, ffmpeg 6.1, Python 3 (numpy, librosa, scipy, soundfile; fontTools installed on demand),
Chromium at `/opt/pw-browsers`, 4 CPUs, no GPU, ephemeral (no SessionStart hook exists yet:
`npm install`, `pip install`, `references/fetch.sh` must be re-run each session). Blocked hosts seen:
Hugging Face, fbaipublicfiles, Freesound, Unsplash, Pixabay, LottieFiles, remotion.media.

---

## 10. Quality bar reached (assessment from the rendered frames)

| Output | Strengths | Weaknesses |
|---|---|---|
| motion-studio StraightScale VO reel | Deterministic 60 fps with real motion blur; springs feel weighted; text tracks the voice; clean brand palette and contrast rules respected; thread wipe transition; on-beat SFX; correct loudness and ducking; sourced data; rules check | Mostly type on flat charcoal/marble; ad and review "cards" are grey-bar placeholders (the AI tell taste-skill bans); many frames top-heavy with the lower half empty; similar to the "cards on flat background" look the user rejected in the other session's v1; logo redrawn; generic avatar circles; filled progress tracks for proof; synthesized 4-chord score unheard by a human; no captions track; one format |
| straightscale-reel v2 rough cut | Real concept and signature device (gold line), collage texture world, Droste pull-back, frame-in-frame, word-level captions, approval trail | Unfinished: 15 fps preview, no music/SFX, no blur; some label/stamp collisions in S3; caption strip repeats on-screen words in places |
| OpenMontage sky explainer | Coherent art direction from the subject, one signature device, clear mechanism diagrams, research-backed script, publish package | Small captions, -16 LUFS, 30 fps, generic friendly-explainer look |

Net: we can reliably produce a clean, on-brand, beat-synced kinetic-type reel in about an hour. The
craft ceiling is limited by the lack of real assets, imagery, a layout/type system and art direction from
references, not by the render engine.

---

## 11. Gaps to $10k-level output

1. **Real brand asset capture.** Logo (SVG), exact fonts, product UI screenshots, photography, past
   campaigns, captured and logged into `assets/` + `manifest.json` before design. Both StraightScale
   reels redrew the logo from a sentence.
2. **Art direction from references.** A reference board (client's best competitors' ads from the Ad
   Library, Dribbble/Behance motion, past winners), a written `style_guide.md`, a design read + dials,
   one signature device, and 3-4 approved styleframes before any scene code.
3. **Typography system.** Per-client type tokens (display / headline / body / label / figure sizes,
   weights, tracking, line height), figure style (lining vs old-style), max words per line, kinetic-type
   vocabulary, glyph checks per language, variable fonts for weight animation.
4. **Layout system for 9:16 (and others).** Safe zones, a grid, focal point per beat, no dead halves;
   phone-size readability checked per beat, not only at the end.
5. **Imagery and depth.** Photography/footage plates, generated plates (Higgs/ElevenLabs), cutouts,
   textures, and **3D** for hero moments (Three.js or Higgs `generate_3d`); currently zero.
6. **Real UI and proof.** Recreated client UI from real screenshots or design-system components
   (`awesome-design-md` tokens) instead of grey bars; real reviews only when the client supplies them.
7. **Music.** A licensed or generated track (ElevenLabs music) or a much richer synthesized score, beat
   grid re-measured on the final mix, and a human listen gate. The agent cannot hear.
8. **Captions.** Burned-in word-level captions as a style choice plus an SRT for every deliverable;
   caption design per brand.
9. **Multi-format and cutdowns.** Parameterised `W/H` and layouts so 9:16, 4:5, 1:1, 16:9 are native
   re-layouts, plus 15 s / 30 s cutdowns and a hook A/B.
10. **Client review loop.** Approval gates (brief, script, VO, styleframes, animatic, final), a review
    page (Artifact) with the preview, frame-accurate timestamped comments, and a cap on edit rounds.
11. **Versioning.** `v1, v2...` deliverables never overwritten, a changelog per version, approvals logged
    with dates (straightscale-reel's PROJECT/PROGRESS/LOG pattern), render logs kept.
12. **One project per client.** A single folder and timeline; parallel sessions caused duplicate work.
13. **Native-language and claims QA.** Native-speaker check of VO and on-screen text (still pending for
    Albanian), pronunciation dictionary, claims traced to sources (storyboard-qa style), rules check.
14. **Scored critique log.** `review_log.md` with per-beat scores and the 3 fixes per round; never ship
    with a known blemish without saying so.
15. **Session robustness.** SessionStart hook (npm, pip, fonts, `references/fetch.sh`), a root
    CLAUDE.md that points at `motion-studio/CLAUDE.md`, and one renderer that merges both engines'
    features.
16. **Performance feedback.** Hook strength / virality prediction (Higgs `virality_predictor`), and
    post-launch numbers feeding the next brief.
17. **Skill routing.** Decide which skill owns "make a video" (HyperFrames vs motion-reel vs onetake);
    keep onetake out of client work.

---

## 12. Reusable pieces the A-to-Z workflow should keep

**Engine**
- `motion-studio/render.mjs` in-page subframe blending + `--from` parallel segments + concat, merged with
  `straightscale-reel/src/render.js` features: local HTTP server, `__ready` flag, `--scale`, `--stamp`,
  `--frames-only`, `--jpg`, `--audio` mux, page-error logging, sRGB flag. Add `--w/--h` that the page
  reads, and linear-light blending.
- `lib/motion.js` (`spring`, `track`) + named spring presets (`TYPE/UI/POP/HEAVY` in the StraightScale
  page).
- Text primitives from `projects/straightscale/index.html`: `wrap`, `measure`, `riseLine` (mask reveal
  with in/out and returned x-ranges), `riseBlock`, `strike`, `chip`; scene table `[[start, end, fn]]`
  with +-0.3 s overlap; mask transitions (thread wipe, rise/drop with a gold edge); seeded `rng`, grain
  tile, procedural marble.
- `straightscale-reel/src/fx.js` collage toolkit (paper, torn scrap, tape, label-maker, ransom letters,
  marker, rubber stamp, halftone, gold line, `fromLine`), `lib.js` SAFE zone and `text()` helper,
  `main.js` caption engine (groups, spring strip, active word, `NO_CAPTION`), per-scene module format.

**Audio**
- `audio/score.py` instrument + SFX library and `place()`; cue list mirrored from the shot list.
- `finish.sh`: VO splice at measured silence, sidechain ducking, two-pass loudnorm, mux, review, poster
  (change TP to -1.5 dBTP).
- `beats.py`; ElevenLabs Scribe word timings as the master clock (`plan/beats.json` format:
  `{source, duration, words: [{w, s, e}]}`); objective audio checks (RMS per 2 s window, spectrogram,
  `ebur128`).

**Review**
- `stills.mjs` (pre-render sheets at chosen times), `scripts/preview.mjs` (every-frame sheets with
  timestamps), `review.sh` (contact / strip / phone / loop), seam strips for segment joins, the
  guide's harsh-critique prompt with a logged score table.

**Process and documents**
- motion-video-director scaffolding: kickoff questions (always ask VO yes/no), PROJECT / PROGRESS / LOG /
  manifest, approval gates, ElevenLabs paste-ready script format with word budget and alt hook.
- Shot list format: time | VO (client language) | English check | on screen | SFX, plus a rules check.
- storyboard-qa audits as the storyboard gate (timing math, causal links, claim tracing, hook/payoff).
- OpenMontage artifacts: `decision_log.json` (options with scores and rejection reasons),
  proposal with 3 concepts, `art-direction.md` (design read, dials, palette from the subject, one
  signature device, scene inventory, anti-patterns), `final_review.json`, publish package (title,
  description with sources, chapters, tags, SRT, thumbnail); Remotion proxy fixes if Remotion is used.
- Design-skill pieces: DESIGN.md token format for a per-client `brand.md`; taste-skill design read,
  dials and AI-tell list adapted to video; image-to-code's styleframe-first analysis.
- Mark AI evidence discipline: every number on screen has a retrieved source and date; fabricated data is
  a stop-ship.
- Brief rules that worked: client-language copy with English check lines, no invented numbers/reviews/
  deadlines, examples labelled as examples, sources on screen, no em dashes or hype words.
