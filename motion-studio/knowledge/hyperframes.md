# HyperFrames: reference guide for the motion studio

Written 12 Oct 2026 from a full clone of `heygen-com/hyperframes` at commit `4120042`
(`references/hyperframes/`, CLI `0.8.150` = npm `latest` that day) plus hands-on tests in this cloud
container (4 CPUs, no GPU, Node 22, ffmpeg 6.1, egress proxy). All paths below are relative to
`references/hyperframes/` unless they start with `~`, `/` or `motion-studio/`. The 21 skills are also
installed at `.claude/skills/` (identical to the clone except an added `hyperframes/LICENSE`).

---

## 0. TL;DR

- **What:** an Apache-2.0 framework (by HeyGen) that renders an HTML page into a deterministic MP4.
  A composition is HTML whose elements carry `data-start` / `data-duration`; animation lives on one
  paused GSAP timeline registered at `window.__timelines["<id>"]`; the renderer seeks every frame in
  headless Chrome and pipes it to FFmpeg. Plus a CLI (lint, check, snapshot, preview, render, batch),
  a Studio editor, ~447 registry blocks/components, and 21 agent skills full of motion-design doctrine.
- **Local rendering works here.** Verified: `init`, `lint`, `check`, `snapshot`, `render` (MP4, WebM
  with alpha, batch variants), sub-compositions, registry components, audio mix with automation,
  Kokoro TTS, background removal, beat analysis, website capture, voiceover carve. DOM-only 1080x1920
  at 30 fps renders at about **3.3 s per second of video** (6 s reel in 19.5 s) when the box is idle.
- **Must-do in this container:** vendor GSAP locally (jsDelivr/unpkg/cdnjs are blocked by egress
  policy; every template and registry item points at jsDelivr), run `npx hyperframes browser ensure`
  once (or set `HYPERFRAMES_BROWSER_PATH`), and set `HYPERFRAMES_NO_TELEMETRY=1`.
- **Does not work here:** transcription (models come from huggingface.co, blocked), WebGPU blocks
  (no adapter), `publish` / cloud / HeyGen catalog (HeyGen hosts blocked and need an account).
  WebGL works but is slow (software SwiftShader, about 16 s per second at 1080p).
- **Needs a HeyGen account (none used):** `cloud render`, `auth`, HeyGen TTS with word timings,
  `media-use resolve` for bgm / image / icon / voice / avatar video, `publish` hosting. Lambda and Cloud
  Run need your own AWS / GCP account.
- **Recommendation:** adopt HyperFrames as the **build-and-render layer** of the A-to-Z pipeline
  (replacing our hand-rolled `render.mjs` for DOM/GSAP reels), and steal its doctrine (motion language,
  cut catalog, blueprints, review loop, safe zones, carve) wholesale. Keep our own pieces where it is
  weak here: transcription (use ElevenLabs Scribe or a supplied transcript and import it), music,
  loudness mastering to -14 LUFS, and real subframe motion blur. Details in section 7.

---

## 1. What it is, license, commercial use

**What it is.** "Write HTML. Render video. Built for agents." Inspired by Remotion but plain HTML (no
React, no build step). Same input gives the same frames. Used in production at HeyGen. Pieces:

| Piece | What it does |
|---|---|
| `hyperframes` CLI (`packages/cli`) | scaffold, lint/check, snapshot, preview Studio, render (mp4/webm/mov/gif/png-sequence/hls), batch, capture websites, TTS, transcribe, remove-background, catalog/add, cloud/lambda/cloudrun |
| Core / Engine / Producer | parse + compile compositions, drive headless Chrome frame-by-frame, encode with FFmpeg, mix audio |
| Registry (`registry/`) | 210 blocks + 237 components + 8 starter examples, installed with `npx hyperframes add` |
| Skills (`skills/`) | 21 agent skills: a router, 10 creation workflows, 9 domain skills (core, animation, keyframes, creative, audio, registry, cli, studio, media-use) + figma |
| Studio | browser timeline editor (`preview`), plus a separate desktop app ("Framey" chat) they upsell |

**License.** `LICENSE` is Apache-2.0 for the whole repo. README: "no per-render fees or commercial-use
thresholds". For us that means:

- We may use it commercially, modify it, vendor parts of it, and sell the videos we render. Apache
  places no restriction on rendered output. If we redistribute their code (e.g. ship a copy of a block
  inside a deliverable project folder), keep the license text; Apache grants no trademark rights, so do
  not present work as "by HeyGen/HyperFrames" or use their marks to imply endorsement.
- **GSAP** (the animation runtime every composition uses) is under the GSAP Standard "no charge"
  license, not OSI (`CREDITS.md`). Since 3.13 all plugins (SplitText, MorphSVG, DrawSVG, ...) ship free
  in the npm package (verified in `gsap@3.14.2`). Making client videos is fine; read
  gsap.com/standard-license before building a product that resells GSAP-based authoring tools.
- **Registry items** are Apache-2.0 unless the item says otherwise: 36 WebGPU shader blocks are
  "Apache-2.0 AND MIT" (shaders.com library, license text in `compositions/lib/shaders.THIRD-PARTY-LICENSES.txt`
  after install); `weight-wave` OFL-1.1; `caret-swap` MIT+OFL; `kinetic-center-build` MIT. The seven
  3D-motion pieces list some assets whose **origin is still "to be confirmed"** (`CREDITS.md`):
  `canopy-part-title` leaf textures, `glass-shard-title` matcap, `frost-sequence-camera-orbit` shard and
  ice textures. Do not ship those three in client work until cleared, or swap the textures.
- **Bundled SFX** (`skills/media-use/audio/assets/sfx/`, 19 files) are Pixabay Content License:
  commercial use, no attribution needed.
- **The "24 text effects"** are NOT in this repo: they come from `pixel-point/animate-text`, which
  declares no license (`skills/hyperframes-animation/adapters/animate-text.md`). Use the effect names as
  vocabulary only; most have Apache-2.0 equivalents in the registry (section 4.4).
- **Models:** Kokoro-82M (local TTS) Apache-2.0; Parakeet (transcription) CC-BY-4.0; u2net_human_seg
  (background removal) from rembg. HeyGen catalog media (music, images, voices) follow HeyGen's terms.
- **Platform look-alikes:** `chatgpt-exchange`, `claude-exchange`, `slack-notification-ad`,
  `heygen-avatar-promo-card`, `apple-money-count`, `ios26-liquid-glass`, `macos-tahoe-liquid-glass`,
  `instagram-follow`, `tiktok-follow`, `spotify-card`, `x-post`, `reddit-post`, `yt-lower-third` imitate
  third-party UI. Fine for a client's own real handle or a truthful product demo; never to fake an
  endorsement, review, metric or partnership.

**Telemetry.** On by default: anonymous PostHog events (`us.i.posthog.com`), a CLI id in
`~/.hyperframes/config.json`, render/lint stats, a first-run notice, and in Studio the CLI id is
injected into page loads. Off switches (`packages/cli/src/telemetry/policy.ts`): env
`HYPERFRAMES_NO_TELEMETRY=1` or `DO_NOT_TRACK=1` (checked first), or persist with
`npx hyperframes telemetry disable`. `telemetry status` shows the source. PostHog is blocked here
anyway. Skills also ask agents to send `hyperframes feedback` reports after renders: don't, for client
work (it posts to a public channel).

---

## 2. Map of the repo

| Path | What it is for |
|---|---|
| `README.md`, `CLAUDE.md`, `AGENTS.md` | overview, skill list, conventions (bun, oxlint), composition rules summary |
| `DESIGN.md` | the HyperFrames docs site brand guide (colors/type for their website). Not video doctrine |
| `CREDITS.md`, `LICENSE` | third-party licenses (see section 1) |
| `skills/hyperframes/` | **router**: project-state table, routing table, `references/` with the process contracts: `intent-interview.md`, `pitch-round.md`, `brief-contract.md`, `brief-format.md`, `storyboard-format.md`, `script-format.md`, `review-loop.md`, `production-loop.md`, `capability-menu.md`, `frame-worker-core.md`, `subagent-dispatch.md`, `routes/<workflow>.md` |
| `skills/hyperframes-core/` | **composition contract**: `references/minimal-composition.md`, `data-attributes.md`, `sub-compositions.md`, `composition-patterns.md`, `tracks-and-clips.md`, `variables-and-media.md`, `determinism-rules.md`, `creator-editing-recipes.md` (cuts, crossfades, fades, ducking, speed ramps) |
| `skills/hyperframes-animation/` | **all motion knowledge**: `rules-index.md` + `rules/` (48 atomic GSAP recipes), `blueprints-index.md` + `blueprints/` (22 shot templates), `transitions/` (overview, catalog, 13 `css-*.md`, `TRANSITION-REGISTRY.md`), `techniques.md`, `references/motion-blur.md`, `adapters/` (GSAP, Lottie, Three, Anime, CSS, WAAPI, TypeGPU, html-in-canvas, animate-text), `examples/` (13 runnable scene HTMLs), `scripts/animation-map.mjs` (choreography audit) |
| `skills/hyperframes-creative/` | non-motion direction: `references/house-style.md`, `video-composition.md`, `motion-principles.md`, `typography.md`, `beat-direction.md`, `story-spine.md`, `narration.md`, `data-in-motion.md`, `audio-reactive.md`, `design-spec.md`, `storyboard-recipe.md`; `palettes/` (9); `frame-presets/` (13 design systems with caption skins); `scripts/extract-audio-data.py`, `contrast-report.mjs` |
| `skills/hyperframes-keyframes/` | seek-safe keyframes, camera moves, punch-ins, FLIP, masks, 3D; `hyperframes keyframes` diagnostics |
| `skills/hyperframes-audio/` | mixing: fx chains, automation lanes, voiceover carve (`scripts/carve.mjs`), submix buses, `references/presets.md` symptom table |
| `skills/hyperframes-registry/` | search/install/wire blocks and components; authoring new ones (`references/component-quality-bar.md`, `placeholder-material.md`) |
| `skills/hyperframes-cli/` | every CLI command; `references/preview-render.md`, `cloud.md`, `lambda.md`, `cloudrun.md`, `compare-and-batch.md`, `lint-validate-inspect.md` |
| `skills/hyperframes-studio/` | Studio timeline layout conventions and **safe zones** |
| `skills/media-use/` | media OS: `resolve` (bgm/sfx/image/icon/logo/voice/grade/lut), audio engine (`audio/`), media treatments (grading, retro, privacy), memory + recipes (`scripts/prefs.mjs`, `recipe.mjs`) |
| `skills/motion-graphics/` | short unnarrated pieces: categories (kinetic-type, stat, charts, logo-reveal, lower-thirds, maps, webpage, news, tweet, asset-fusion), `catalog-map.md`, shot-plan IR |
| `skills/product-launch-video/` | the most complete A-to-Z pipeline: capture, `frame.md`, storyboard, audio, parallel frame workers, assembly, transitions, captions; `references/story-design.md`, `visual-design.md`, `motion-language.md`, `cut-catalog.md`; `scripts/` (build-frame, audio, captions, transitions, assemble-index, frame-packets) |
| `skills/faceless-explainer/`, `pr-to-video/`, `music-to-video/`, `talking-head-recut/`, `embedded-captions/`, `general-video/`, `slideshow/`, `figma/`, `remotion-to-hyperframes/` | the other workflows; `music-to-video/scripts/analyze-beatgrid.py` is the beat analyzer; `embedded-captions/` has 35 caption identities |
| `registry/blocks/`, `registry/components/`, `registry/examples/` | the catalog source; each item has `registry-item.json` + HTML. `registry/components/CATALOG.md` = the "hero primitive shelf of 21" with use_when / avoid_when |
| `registry/catalog-artifact/` | precomputed vectors for the on-device semantic search |
| `docs/` | Mintlify docs: `concepts/` (compositions, data attributes, determinism, frame adapters, variables), `guides/rendering.mdx`, `4k-rendering.mdx`, `hdr.mdx`, `performance.mdx`, `captions-and-recuts.mdx`, `color-grading.mdx`, `deploy/` |
| `examples/` | deployment examples only: `aws-lambda/`, `gcp-cloud-run/`, `k8s-jobs/` (Dockerfile pattern with `PRODUCER_HEADLESS_SHELL_PATH`) |
| `packages/` | `cli`, `core` (types, parser, linter, runtime, adapters), `engine` (Chrome capture: `services/frameCapture.ts`, `browserManager.ts`, `audioMixer.ts`), `producer` (pipeline), `player` (`<hyperframes-player>`), `shader-transitions` (`HyperShader`), `studio`, `studio-server`, `sdk`, `aws-lambda`, `gcp-cloud-run`, `lint`, `parsers` |
| `themes/`, `plans/`, `releases/`, `updates/` | internal planning, release notes |

**How rendering works** (from `packages/engine`, `packages/producer` and our render logs): compile
(assemble sub-compositions, inline fonts as `@font-face` data URIs, fetch Google Fonts at build time
and cache them in `~/.cache/hyperframes/fonts/`) → browser probe → pre-extract video frames with FFmpeg
(so `<video>` is frame-exact) → N parallel workers each launch chrome-headless-shell → for each frame the
runtime seeks every registered timeline/adapter to time t → capture via `HeadlessExperimental.beginFrame`
(fast deterministic path on Linux) or `Page.captureScreenshot` (used for alpha output) → frames stream
into FFmpeg while capturing → audio: effect chains run in an OfflineAudioContext in the browser, then the
engine's `audioMixer` bakes volume lanes and mixes to AAC → mux. The summary's second line tells you the
path: `beginframe capture · software gpu · ... capture 13.9s · encode (during capture)`.

---

## 3. The composition model

### 3.1 Rules in brief

- **Root:** one element with `data-composition-id`, `data-width`, `data-height`, and (recommended)
  `data-duration`. The root `data-duration` is read once at compile time and is the render length; a
  timeline that runs longer is cut, one that ends early holds its last frame. Style the root
  `width/height: 100%`; the runtime stamps the pixel size.
- **Clips:** any element with `data-start` is a clip (timed visibility). Window is half-open
  `[start, start+duration)`, so land final states slightly before the end. `class="clip"` is a
  convention (the runtime ignores it) but your CSS should give it `position:absolute; inset:0`.
  `data-track-index` is only a Studio display lane; layering is CSS `z-index`.
- **Relative timing:** `data-start="intro + 2"` / `"intro - 0.5"` (spaces required; a typo silently
  resolves to 0).
- **One paused timeline per composition:** `const tl = gsap.timeline({ paused: true }); ...;
  window.__timelines["<composition-id>"] = tl;` Register after the build completes (async builds inside
  `document.fonts.ready` are fine). Never `tl.play()`. The runtime creates `window.__timelines`.
- **Seek-safety / determinism:** every frame must be a pure function of time. No `Date.now`,
  `performance.now`, unseeded `Math.random`, timers, hover/scroll state, render-time network fetches, CSS
  `transition`s on animated elements, or standalone `gsap.to()` outside the timeline (it will not render).
  Use `fromTo` (explicit start state) rather than `from`. `repeat: -1` only under a finite root duration.
  Never tween `display`/`visibility`/`autoAlpha` on a `.clip`; animate a child. Never tween
  `width/height/top/left`; use transforms, masks, `clip-path`, scale proxies.
- **Sub-compositions:** a scene in its own file, mounted with
  `<div data-composition-id="stat" data-composition-src="compositions/stat.html" data-start data-duration>`.
  The file wraps everything (styles, markup, scripts) inside `<template>`; `<head>` is discarded. Host id
  = inner `data-composition-id` = timeline key. The runtime seeks child timelines itself; never nest them
  into the host timeline. A sub-comp timeline cannot animate host elements. The host clip's
  `data-duration` is the visible window (a short internal timeline holds its last frame).
- **Variables:** declare on `<html data-composition-variables='[{"id","type","label","default"}]'>`
  (types string/number/color/boolean/enum). Bind with `data-var-text="id"`, `data-var-src="id"`, or CSS
  `var(--id)` (every scalar variable becomes a CSS custom property on the root). Override per instance
  with `data-variable-values='{...}'` on a host, per render with `--variables` / `--variables-file`, or
  one output per row with `render --batch rows.json`.
- **Media:** `<video>` / `<audio>` work at any depth; the framework owns playback (never call `play()`).
  Every `<audio>` needs an `id` or it is silently not mixed. Video with sound: `data-has-audio="true"`;
  silent: `muted`. `data-media-start` trims the source, `data-volume` (0..3.98) is static gain,
  `data-playback-rate` constant speed, `data-automation` lanes do fades, ducking and speed ramps:
  `data-automation='{"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":0},{"t":0.4,"v":1}]}]}'`
  (`t` is clip-local seconds). Never `crossorigin` on media. Never give a `<video data-start>` an
  ancestor that also has `data-start` (sub-composition hosts are exempt).
- **Runtimes:** GSAP is the default; Lottie, Three.js, Anime.js, CSS keyframes, WAAPI and TypeGPU have
  seek adapters (`skills/hyperframes-animation/adapters/`). Several can coexist.
- **Fonts:** write a real Google font name in a `font-family` declaration and the compiler embeds it
  (18 families are pre-bundled offline, others are fetched at build time). See pitfall on the `font:`
  shorthand.
- **Layout helpers at runtime:** `window.__hyperframes.fitTextFontSize(text, {maxWidth, fontFamily, fontWeight})`,
  `window.__hyperframes.pretext` (canvas text measurement), `window.__hyperframes.getVariables()`.

### 3.2 Verified minimal example (single file, 4 s, 1080x1920)

Rendered here in 18.3 s, `check` clean (2 benign warnings suggesting sub-compositions). Requires
`assets/vendor/gsap.min.js` (copy from `npm pack gsap@3.14.2`).

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="assets/vendor/gsap.min.js"></script>
    <style>
      html, body { margin: 0; width: 1080px; height: 1920px; overflow: hidden; background: #0b0b10; }
      #root { position: relative; width: 100%; height: 100%; overflow: hidden; }
      #bg { position: absolute; inset: 0; background: radial-gradient(120% 80% at 50% 30%, #2a1b5e 0%, #0b0b10 70%); }
      .clip { position: absolute; inset: 0; }            /* without this, flex scenes collapse to the top */
      .scene { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 36px; }
      .kicker { color: #ff5c39; font-family: "IBM Plex Mono", monospace; font-weight: 700; font-size: 40px; letter-spacing: 0.24em; text-transform: uppercase; }
      .headline { display: block; width: 900px; margin: 0; color: #f6f5f1; font-family: "League Gothic", sans-serif; font-size: 210px; line-height: 0.9; text-align: center; text-transform: uppercase; }
      .word { display: inline-block; }                    /* transforms are no-ops on inline spans */
      .stat { display: block; color: #f6f5f1; font-family: "League Gothic", sans-serif; font-size: 420px; line-height: 0.9; font-variant-numeric: tabular-nums; }
      .bar { display: block; width: 600px; height: 12px; border-radius: 6px; background: #ff5c39; transform-origin: left center; }
      .label { color: #cfc9ee; font-family: "IBM Plex Mono", monospace; font-size: 46px; text-transform: uppercase; }
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="4" data-width="1080" data-height="1920">
      <div id="bg" class="clip" data-start="0" data-duration="4" data-track-index="0"></div>
      <section id="s1" class="clip scene" data-start="0" data-duration="2" data-track-index="1">
        <div id="s1-kicker" class="kicker">New drop</div>
        <h1 id="s1-headline" class="headline"><span class="word">Motion</span> <span class="word">that</span> <span class="word">sells.</span></h1>
      </section>
      <section id="s2" class="clip scene" data-start="2" data-duration="2" data-track-index="1">
        <div id="s2-stat" class="stat">0%</div>
        <div id="s2-bar" class="bar"></div>
        <div id="s2-label" class="label">more watch time</div>
      </section>
    </div>
    <script>
      const tl = gsap.timeline({ paused: true });
      tl.fromTo("#s1-kicker", { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 0.15);
      tl.fromTo("#s1-headline .word", { opacity: 0, y: 120 }, { opacity: 1, y: 0, duration: 0.7, ease: "expo.out", stagger: 0.12 }, 0.25);
      const n = { v: 0 }, statEl = document.getElementById("s2-stat");
      tl.fromTo(n, { v: 0 }, { v: 87, duration: 1.1, ease: "power3.out",
        onUpdate: () => { statEl.textContent = Math.round(n.v) + "%"; } }, 2.1);
      tl.fromTo("#s2-stat", { opacity: 0, scale: 0.9 }, { opacity: 1, scale: 1, duration: 0.6, ease: "power3.out" }, 2.05);
      tl.fromTo("#s2-bar", { scaleX: 0 }, { scaleX: 1, duration: 0.9, ease: "power3.inOut" }, 2.25);
      tl.fromTo("#s2-label", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, 2.5);
      window.__timelines["main"] = tl;
    </script>
  </body>
</html>
```

### 3.3 Verified modular example (sub-compositions + registry components + audio)

6 s, 1080x1920, `check` fully clean, rendered with audio in 19.3 s (-15.1 LUFS integrated, measured).
`index.html` is a thin orchestrator: theme tokens on `#root`, scene hosts, audio at the root.

```html
<div id="root" data-composition-id="main" data-start="0" data-duration="6" data-width="1080" data-height="1920"
     style="--bg:#0b0b10; --fg:#f6f5f1; --brand:#ff5c39; --accent:#7c6cff; --accent-2:#ffd166; --font-display:'Montserrat', sans-serif;">
  <div id="bg" class="clip" data-start="0" data-duration="6" data-track-index="0"></div>
  <!-- registry component mounted as a scene, configured by variables -->
  <div id="el-hook" class="clip" data-composition-id="per-word-rise"
       data-composition-src="compositions/components/per-word-rise.html"
       data-variable-values='{"text":"Motion that sells.","accent":"green"}'
       data-start="0" data-duration="2.2" data-track-index="1"></div>
  <!-- our own sub-composition (file wraps <style>, markup and <script> in <template>) -->
  <div id="el-stat" class="clip" data-composition-id="stat" data-composition-src="compositions/stat.html"
       data-start="2.2" data-duration="2.2" data-track-index="1"></div>
  <div id="el-logo" class="clip" data-composition-id="logo-sting"
       data-composition-src="compositions/components/logo-sting.html"
       data-variable-values='{"wordmark":"ACME","accent":"green"}'
       data-start="4.4" data-duration="1.6" data-track-index="1"></div>
  <audio id="vo" src="assets/vo.wav" data-audio-group="voiceover" data-start="0.3" data-track-index="8"></audio>
  <audio id="music" src="assets/bed.wav" data-audio-group="music" data-start="0" data-duration="6" data-track-index="9"
         data-volume="0.5"
         data-automation='{"version":1,"lanes":[{"target":"volume","points":[{"t":0,"v":0},{"t":0.4,"v":1},{"t":5.2,"v":1},{"t":6,"v":0}]}]}'></audio>
</div>
<script>window.__timelines["main"] = gsap.timeline({ paused: true });</script>
```

with `#root > div[data-composition-src] { position:absolute; inset:0; }` in the host CSS. Observations:
the components read the theme tokens (`accent: "green"` rides `--brand`, so it rendered in our orange);
components paint their own opaque `--bg` and cover anything under them; `per-word-rise`'s default type
size is too small for a 9:16 feed and must be edited in the installed copy.

---

## 4. Ideas worth stealing for premium motion

### 4.1 Motion doctrine (the most valuable text in the repo)

From `skills/product-launch-video/references/motion-language.md` Part 2 ("the difference between a
launch video and an agent-made PowerPoint"):

1. **Smooth beats bouncy; `power3` is the default.** No `back.out` / `bounce` / `elastic` as house
   style; overshoot only for an explicitly playful beat. A critically damped `springEase` (ζ=1) exists in
   `skills/hyperframes-animation/adapters/gsap-easing-and-stagger.md`.
2. **Sequential reveal in the back ~50%, timed to the voiceover.** Do not dump content in the first
   25%; reveal each line/card when the VO names it. Write VO as discrete cues so the shot can pace to it.
3. **No lazy breathing, no slow pan/push in the back half.** "I'd rather have no motion than bad
   motion." The only sanctioned hold aliveness is low-amplitude jitter or live SVG internals.
4. **Internal seams are velocity-matched cuts** (cut at peak velocity, same direction and speed on both
   sides): `references/cut-catalog.md` gives four: zoom-through (state change), inverse zoom-through
   (arrival/payoff), cut-the-curve (continuing idea on x/y), waterfall (word-level). Blur at the cut:
   **10 px peak for text, 18-20 px for full-frame surfaces**, same value both sides, on the wrapper.
   Exit phase example: scale 1.0→1.2, blur 0→10 px with `power3.in`, opacity 1→0.15 linear, 0.2 s.

From `skills/hyperframes-creative/references/motion-principles.md`: vary eases (max 2 tweens share
one per scene), slowest scene 3x slower than fastest, vary entry directions, offset first animation
0.1-0.3 s, `.out` for entrances / `.in` for exits / `.inOut` for moves, build/breathe/resolve, exits
faster than entrances, stagger in order of importance with total stagger under 500 ms, plus the
"load-bearing GSAP rules" (no iframes, never two concurrent transform tweens on one element, split
parent/child, `fromTo` over `from`, ambient tweens must live on the timeline, hard-kill inner elements
with `tl.set` at boundaries).

Note the tension: `house-style.md` says decoratives should breathe/drift; the launch doctrine bans
lazy breathing. For premium client work follow the launch doctrine.

### 4.2 Composition and design rules

- `skills/hyperframes-creative/references/video-composition.md`: video scale table (headlines 64-120 px,
  body 28-42, labels 18-24, decorative opacity 12-25%, borders 2-4 px, padding 60-140); 6-10 visual
  roles per produced frame (background treatment / midground message / foreground accents); brand
  accent visible at 15-25% atmospheric or full saturation focal; **no full-screen linear gradients on dark
  backgrounds (they band under H.264)**; two focal points; hero text 60-80% of frame width; anchor to
  edges, split frames, structural rules that animate (`scaleX 0→1`).
- `typography.md`: the 18 pre-bundled families and aliases (Helvetica→Inter, Bebas Neue→League Gothic,
  Futura→Montserrat); a **banned list** of AI-default fonts (Inter, Roboto, Poppins, Playfair, Syne...);
  distinctive embedded picks: Montserrat, Oswald, League Gothic, Archivo Black, Space Mono, IBM Plex
  Mono, JetBrains Mono; never two sans; weight contrast 300 vs 900; **in-feed (IG/TikTok) sizes: body
  ≥32 px, headlines ≥90 px, labels ≥24 px**; tracking -0.03 to -0.05 em on display; 3 s on screen must
  read in 2.
- `house-style.md` "lazy defaults to question": gradient text, left accent stripes, cyan/purple neon,
  pure #000/#fff, identical card grids, everything centered.
- `frame-presets/` (13 design systems: biennale-yellow, blockframe, blue-professional, bold-poster,
  broadside, capsule, cartesian, cobalt-grid, code-editorial, coral, creative-mode, daisy-days,
  editorial-forest), each a `FRAME.md` (YAML tokens: colors, a type ramp in `cqw` units, components) +
  `caption-skin.html` + `frame-showcase.html`. `product-launch-video/scripts/build-frame.mjs --preset <name>`
  remixes a preset onto captured brand tokens. The "frame.md" idea (design.md inverted for the camera:
  atoms sacred, composition free) is the right shape for our per-client design system.
- `palettes/` (9 moods) and `references/data-in-motion.md` (stats/infographics).
- Safe zones (`skills/hyperframes-studio/SKILL.md` §4): action-safe 90%, title-safe 80%, captions and
  key content inside title-safe. For Reels/TikTok UI, enforce a keep-out band with
  `npx hyperframes check --caption-zone "x0=0;y0=.82;x1=1;y1=1;severity=error;seek=.25,1"`.
  Embedded-captions puts the portrait rail ~600-700 px from the bottom.

### 4.3 Shot blueprints and rules

- `skills/hyperframes-animation/blueprints-index.md`: **22 time-coded shot templates** reverse-engineered
  from 178 product-launch clips, each with a signature move and a role menu (Hook, Problem,
  Product_Intro, Key_Feature, Benefits, Social_Proof, CTA, Brand_Outro): kinetic-type-beats (workhorse),
  typewriter-reveal, spatial-pan-stations, camera-journey, zoom-out-workspace-reveal, constellation-hub,
  grid-card-assemble, logo-assemble-lockup, cursor-ui-demo, device-surface-showcase,
  prompt-type-submit-generate, agent-progress-theater, panel-edit-live-sync,
  transcript-scroll-artifact-reveal, dataviz-countup, titlecard-reveal, comparison-split,
  overwhelm-surround, ticker-takeover, fixed-anchor-cycle, video-text-pivot, cta-morph-press.
  Method: pick a role → blueprint, then Reproduce / Adapt (keep the signature move) / Compose.
- `rules-index.md`: **48 atomic recipes** (compose 2-4 per scene): text (hacker-flip-3d,
  vertical-spring-ticker, counting-dynamic-scale, discrete-text-sequence, asr-keyword-glow,
  3d-text-depth-layers, kinetic-beat-slam, gradient-text-sweep, chromatic-glitch), data
  (stat-bars-and-fills, chart-scrub-readout), sequencing (dynamic-content-sequencing: script-driven
  phrase windows; context-sensitive-cursor: typing caret colour/blink), camera (coordinate-target-zoom, camera-cursor-tracking,
  multi-phase-camera, viewport-change, 3d-camera-flight, depth-of-field-blur), layout
  (center-outward-expansion, split-tilt-cards, orbit-3d-entry, depth-scatter-assemble,
  anchored-layout-expand, avatar-cloud-network, 3d-page-scroll, ai-tracking-box), SVG (svg-path-draw,
  svg-icon-enrichment), transitions/physics (reactive-displacement, press-release-spring,
  physics-press-reaction, cursor-click-ripple, cursor-drag, multi-cursor-choreography,
  control-target-sync, scale-swap-transition, card-morph-anchor, theme-crossfade-morph,
  spring-pop-entrance, motion-blur-streak, waterfall-entry, particle-burst, nudge-curve), ambient
  (sine-wave-loop, ambient-glow-bloom), recipes (gsap-effects, css-marker-patterns).
- `examples/` has 13 runnable reference scenes (brand-reveal-assemble-zoom, hook-counter-burst,
  metric-video-text-pivot, cta-morph-press, proof-logo-chain, ...).
- `techniques.md`: SVG path drawing, Canvas 2D, CSS 3D, per-word kinetic type, Lottie, video
  compositing, typing, variable-font axes, MotionPath, velocity-matched transitions, audio-reactive,
  clip-path masks (give glyphs 0.2 em padding so descenders are not clipped), WebGL shader art.

### 4.4 Transition vocabulary and the 24 text effects

`skills/hyperframes-animation/transitions/overview.md` is a ready-made decision table:

- Energy → primary: calm (blur crossfade, focus pull; shader cross-warp; 0.5-0.8 s, `sine.inOut`),
  medium (push slide, staggered blocks; shader whip pan / cinematic zoom; 0.3-0.5 s, `power2/3`), high
  (zoom through, overexposure; shader ridged burn / glitch / chromatic split; 0.15-0.3 s, `power4/expo`).
  One primary for 60-70% of cuts + 1-2 accents.
- Mood table (warm, clinical, editorial, tech, tense, playful, dramatic, premium/luxury = focus pull,
  blur crossfade, dip to black, cross-warp; retro = film burn, light leak, VHS).
- Narrative position (opening = most distinctive; between related points = primary 0.3 s; topic change
  = different; climax = boldest; outro = slowest), blur by energy (calm 20-30 px, high 3-6 px), presets
  (snappy 0.2 `power4.inOut`, smooth, gentle, dramatic, instant, luxe 0.7 `power1.inOut`).
- Hard rules: transitions are the exit (no exit animations except the final scene); outgoing and
  incoming animate at the same time T; don't use star iris, tilt-shift, lens flare, hinge.
- `catalog.md` + `css-push|radial|3d|scale|dissolve|cover|light|distortion|mechanical|grid|other|blur|destruction.md`
  hold ~40 CSS implementations; WebGL shaders come from `@hyperframes/shader-transitions`
  (`HyperShader.init({scenes, transitions:[{time, shader, duration}]})`) with shader-safe CSS rules
  (no `transparent` in gradients, explicit scene `background-color`, `data-no-capture`).
- `TRANSITION-REGISTRY.md`: the curated, injectable subset (crossfade, blur-crossfade, push-slide,
  zoom-through, squeeze) with GSAP templates on scene wrappers `#el-<sid>`.

**The 24 named text effects** (vocabulary only, see license note): per-character soft-blur-in,
per-character-rise, typewriter, bottom-up-letters, top-down-letters, stagger-from-center,
stagger-from-edges; per-word per-word-crossfade, spring-scale-in, shared-axis-y, blur-out-up,
kinetic-center-build, short-slide-right, short-slide-down, depth-parallax-words; per-line
mask-reveal-up, line-by-line-slide; whole-element micro-scale-fade, shimmer-sweep, fade-through,
shared-axis-z, scale-down-fade, focus-blur-resolve, shared-axis-x. Apache-2.0 registry equivalents:
`soft-blur-in`, `per-word-rise`, `typewriter`, `bottom-up-letters`, `top-down-letters`,
`per-word-crossfade`, `shared-axis-y`, `blur-out-up`, `kinetic-center-build` (MIT), `line-by-line-slide`,
`shimmer-sweep`, `fade-through`, `shared-axis-z`, `focus-blur-resolve`, `staggered-fade-up`,
`tracking-in`. Name one effect per text role in the storyboard so the piece reads as one system.

### 4.5 Camera and keyframes

`skills/hyperframes-keyframes/SKILL.md`: punch-in/out = scale + translate on a non-timed wrapper inside
the clip; multi-state zoom = one wrapper with a pose ladder; Ken Burns = wrapper translate + scale;
match cut / whip pan = velocity-preserving handoff; crop/reframe = `clip-path`/mask on an inner
wrapper; speed ramps = a `rate` lane in `data-automation`; arbitrary mid-source freeze is not supported
(pre-render a still). Mechanism table (FLIP for box changes, path travel, stroke draw, shape morph,
masks, stagger, glyph subdivision, counter-transforms, state machines, real 3D). "Scale alone is fake
depth": use perspective + `preserve-3d` + z travel + occlusion. Proof tools:
`npx hyperframes keyframes . [--selector --shot --layout strip --ghost --angle]` (static analysis plus
onion-skin shots; verified it runs). Camera rules worth copying: `viewport-change` (`.world` wrapper,
`T = -offset x S`), `coordinate-target-zoom`, `3d-camera-flight`, `depth-of-field-blur`.
`references/motion-blur.md`: blur only motion that crosses enough frame to smear; registry
`motion-blur` / `shutter-slam` integrate GSAP sub-frame samples (shutter angle, samples) seek-safely.

### 4.6 Audio mixing

`skills/hyperframes-audio/`: effect chains as `data-fx-chain` (highpass/lowpass/peaking/shelves,
compressor, limiter, truepeak, gate, saturate, delay, reverb, chorus, phaser, bitcrush), envelopes on
any parameter, submix buses `<hf-audio-group>` (one chain/fader for all VO clips), preview and render
run the same Web Audio graph. **Voiceover carve**: instead of ducking the whole bed, dip only the bands
the voice occupies (`data-fx-carve` on the bed, sources = the voice group). Verified:
`node .claude/skills/hyperframes-audio/scripts/carve.mjs --comp index.html --core <dir-with-@hyperframes/core> --dry-run`
found bed + voice and proposed 6 peaking dips (160 Hz-2.5 kHz, -7 to -15 dB) + a 67-point level
envelope. Symptom → fix table in `references/presets.md` (rumble-cut, Tame Boominess 200 Hz, Reduce Mud
250 Hz, Add Clarity 3 kHz, Soften Harshness 3.2 kHz, room-gate, voice-clean). Ordering: subtract before
add, level after filter, relationships after level, character and ceiling last. For delivery ceilings use
`truepeak` set 2 dB under the limit. There is no automatic -14 LUFS master; `normalize-audio` only
matches one clip to another, so keep our two-pass ffmpeg `loudnorm` master.

### 4.7 Captions

- `skills/embedded-captions/`: 35 caption identities (`CATALOG.md`: anchor default quiet rail, cream,
  ink, editorial, keynote, documentary, loud, neon, glitch, chrome, velocity, ordnance, terminal,
  neonsign, stardust, stomp, lastpage, scoreboard, transit, vhs, arcade, dossier, laser, thunder,
  hologram, biolume, aurora, spectrum, papercut, popup, chalkboard, graffiti, brush, inkwater, ransom).
  Model: **drop** (filler) / **rail** (verbatim lower-third, carries most text) / **embed** (one peak
  word composited behind the subject using a matte; scarce, ≤1 per block, ≥0.6 s air). Pipeline:
  `scripts/prepare.sh` (matte ∥ transcribe ∥ audio envelope → safe-zones) → small JSON of choices →
  `make-theme.cjs` / `make-cinematic.cjs` → `preview-frames.cjs` (~2 s/frame QA) → render + gates
  (timing, occlusion, overflow). `references/aesthetic-principles.md` has 18 rules worth adopting (cap
  height 3.5-5% of frame height, min 0.4 s per word, segment on breath, one hue + neutrals, break
  rhythm once per 30 s, safe zones per platform).
- Registry `caption-*` components (17 styles, section 5.2) for captions on motion pieces;
  `product-launch-video/scripts/captions.mjs` builds caption groups from word timings using the
  preset's `caption-skin.html`.
- Word timings come from HeyGen TTS (returned with audio) or from transcription; `hyperframes
  transcribe` also **imports** `.json/.srt/.vtt` and exports SRT/VTT (`--to srt|vtt`), verified here;
  that is how we feed it ElevenLabs Scribe word timings (convert to `[{text,start,end}]` JSON first,
  because an imported SRT stays one entry per cue).

### 4.8 Process: brief, pitch, storyboard, review, QA

- **Pitch round** (`skills/hyperframes/references/pitch-round.md`): for an unformed request, four
  private questions (what the subject looks like, what the emotion looks like as a frame, what the
  playback surface demands, what every other video on this subject looks like), then **five concepts**
  from five paths (subject's world, emotion, audience, inverted anti-pattern, unusual format), with an
  internal probability estimate where **at least two must be below 0.10** and no two may share a
  silhouette. Present all five, then recommend one. This is the best anti-median device in the repo.
- **Brief contract**: one field per question, recommended option first, `destination` → `aspect`
  (feed 1080x1080, Reels/TikTok 1080x1920, YouTube 1920x1080), separate stated vs inferred fields with
  receipts, `BRIEF.md` as the resumable source of truth, remembered preferences (`media-use/scripts/prefs.mjs`).
- **Story** (`product-launch-video/references/story-design.md`): extract audience / pain / promise /
  product role / proof / CTA; pick one arc (PAS, Future Pacing, Demo Loop, BAB, Feature-Benefit
  Cascade); one job per beat; hook in the first 3-5 s in outcome language; script bank of VO shapes per
  role → blueprint; `story-spine.md` for value-before-evidence and source-traceable visuals.
- **Review loop** (`review-loop.md`): plan in chat ("This video tells [audience] that [message]" +
  frame table) → optional static sketch sheet `storyboard.html` with real fonts/colors/copy → build on
  confirmed layouts → final Studio preview with one question "render now, or what changes?" → render →
  offer to **freeze a recipe** (`media-use/scripts/recipe.mjs freeze`) so the next video for that client
  starts from the approved design spec and storyboard skeleton. Autonomous mode still posts every
  checkpoint and delivers a contact sheet + frame ids.
- **QA gates**: `lint` (static), `check` (lint + runtime errors + failed requests + layout overflow at
  sampled times + motion assertions in `*.motion.json` + WCAG contrast), `snapshot --at` (contact sheet),
  cut checks at `cut-0.1 s` and `cut+0.2 s` for handoff continuity, `animation-map.mjs` (dead zones,
  stagger consistency), `keyframes` shots, `compare` / `grade-compare` sheets for variants and grades.
  Handoff contract between parallel frame workers: `handoff_out` / `handoff_in` with exact x/y, scale,
  opacity, direction at the cut.
- **Production loop** (`production-loop.md`): install registry blocks once before parallel work, run
  audio generation in the background, sync scene durations to real VO length (real duration wins),
  carve the bed, batch visual checks into one contact sheet (each image re-prices the context).

---

## 5. Catalog: registry blocks and components

Blocks = standalone sub-compositions with their own size/duration (mount via `data-composition-src`).
Components = elastic snippets/primitives (most fill the host box via container queries, expose
variables, `accent` enum green/blue/violet riding `--brand`/`--accent`/`--accent-2`, `exit` default
`none`, `cues` to lock beats to narration). Nearly all blocks are 1920x1080: for 9:16 either use a
native vertical block, an elastic component, or adapt the installed copy. Search before hand-building:
`npx hyperframes catalog --query "<the move in plain English>" --json`. Previews live at
hyperframes.heygen.com/catalog (blocked here; `static.heygen.ai` poster/video URLs are in each
`registry-item.json`). Legend: **[V]** native 1080x1920, **[GL]** WebGL (renders here, slow),
**[GPU]** WebGPU (does NOT render here), **[!]** brand look-alike or unconfirmed asset.

### 5.1 Blocks (210)

**Native vertical / social ad templates (best direct fit for Reels/TikTok):**
- `ai-chat-reveal` [V] 19.3 s: question typed on a rising keyboard, AI streams the answer, cuts to a
  branded close. Fit: AI/SaaS product ad.
- `chatgpt-exchange` [V][!] 14.9 s, `claude-exchange` [V][!] 21.4 s: AI chat UIs streaming answers,
  tables, citations. Fit: "watch it answer" demos; avoid implying the vendor endorses the client.
- `message-thread-reveal` [V] 25.8 s: full iMessage-style conversation with typing dots, link card,
  receipts, closing card. Fit: relatable-story ads, UGC-feel hooks.
- `notes-reveal` [V] 24.9 s: notes-app confession typed with a caret, then hand-lettered paper card
  with checklist. Fit: founder-voice / "honest note" ads.
- `notification-cascade` [V] 14 s, `slack-notification-ad` [V][!] 12 s: notifications pile up then
  payoff. Fit: problem/overwhelm hook for B2B tools.
- `share-sheet-carousel` [V] 7.2 s: share sheet springs up and cycles previews. Fit: app/content sharing.
- `heygen-avatar-promo-card` [V][!] 10 s: avatar mosaic offer card (HeyGen-branded, use as a layout only).
- `instagram-follow` [V] 4.5 s, `tiktok-follow` [V] 4.5 s, `spotify-card` [V] 5 s: follow / now-playing
  cards. Fit: end-card CTA with the client's real handle.
- `ai-answer-rank` (1080x1080) 9 s: brand slides into the #1 slot of an AI answer list. Fit: AEO/SEO agencies.
- `week-in-merges` (1080x1350): leaderboard rows. `flowchart-vertical` (1440x2560): portrait decision tree.

**Titles, logos, brand stings:**
- `logo-outro` 6 s: piece-by-piece logo assembly, glow bloom, tagline, URL pill. Fit: default end card.
- `extruded-logo` [GL] 5 s: beveled 3D letters flip up, light across bevels (chrome/gold/matte). Fit: premium brand sting.
- `glass-hero` [GL] 5 s: glass object refracts a giant headline. Fit: luxury/tech hero.
- `canopy-part-title` [GL][!] 12 s (leaves part to reveal headline), `glass-shard-title` [GL][!] 12 s
  (shards tile into the headline), `code-slice-hero` [GL] 8 s (tiles flip to a rear headline),
  `wireframe-portal-title` [GL] 8 s (portal burst, phrase swap), `frost-sequence-camera-orbit` [GPU][!]
  22.5 s (ice logo breaks and reforms). Fit: hero openers; heavy to render.
- `weight-wave` 6 s: a weight/slant wave travels through a variable-font headline. `split-flap-board`
  3.5 s: Solari board resolves text. `vfx-text-cursor` [GL] 8 s: cursor-glow text reveal with chromatic
  rays. `gooey-split` 4.7 s: metaball dot-to-menu logo morph with motion blur.
- Creator-style: `yt-logo-intro`, `yt-prism-title` (chromatic fringe title, transparent root),
  `hw-title`, `hw-write-title` (true stroke-order handwriting write-on), `hw-path-text` (handwriting
  along an SVG path), `hw-text-cloud` (hand-drawn speech bubble), `mk-callout-highlight` (word-sweep
  karaoke emphasis driven by one scalar, syncs to VO), `blue-sweater-intro-video` [!].

**Product, device and 3D showcase:**
- `product-turntable` [GL] 6 s: GLB/glTF product (or built-in can with your label) turning on a plinth,
  seamless loop. Fit: e-commerce product reels.
- `app-showcase` 5.5 s: three floating phone screens. `ui-3d-reveal` 13 s: perspective UI reveal.
- `vfx-iphone-device` [GL] 15 s: real GLTF iPhone 15 Pro Max + MacBook with live HTML screens, review
  camera choreography. `ios26-liquid-glass` [GPU][!], `macos-tahoe-liquid-glass` [GL][!] 15 s: 3D
  device home screen / desktop with liquid glass (html-in-canvas; untested here).
- `liquid-glass-notification` [GPU], `liquid-glass-widgets` [GPU] 8 s: frosted cards over aurora.
- `exploded-stack` [GL] 5 s: isometric layers explode with labels (architecture). `cuboid-carousel`
  [GL] 6.7 s, `orbit-card` 10 s: 3D card carousels. `gallery-tunnel` [GL] 12 s: infinite corridor of
  image panels. `code-3d-extrude` [GL], `code-particle-assemble` [GL] 8 s.
- `vfx-liquid-background`, `vfx-liquid-glass`, `vfx-magnetic`, `vfx-portal`, `vfx-shatter` [GL]
  (html-in-canvas VFX scenes).

**Image carousels (25 variants, 6 s, 12-24 image slots):** `carousel-circle-1..5` (cards on a circle,
fast-slow-fast swings), `carousel-orbit-1..5` (3D Fibonacci sphere), `carousel-path-1..5` (bezier
arc/V/wave/S paths), `carousel-vision-1..5` (tilted ring under 3D camera), `carousel-text-circle-1..5`
(headline mask-reveal threaded by a circle carousel, then a 1.4x hard-cut second line). Fit: product
ranges, portfolios, real-estate listings, event recaps; adapt to 9:16.

**Data, charts, maps, diagrams:**
- `data-chart` 15 s (bar + line, NYT typography), `bar-chart-race` 12 s, `mk-line-graph` 7 s,
  `mk-progress-stat` 7 s (big numeral + progress track), `mk-specs-list` 8 s (spec checklist),
  `apple-money-count` [!] 5 s ($0→$10,000 counter + money burst + SFX).
- Maps: `us-map`, `us-map-bubble`, `us-map-flow`, `us-map-hex`, `world-map`, `spain-map` (D3/SVG
  choropleths), `nyc-paris-flight` (Apple-style flight with SFX), `north-korea-locked-down` (map zoom +
  scribble circle + label; the annotation kit for "asset fusion"). Real basemaps: motion-graphics
  `categories/maps/bake-basemap.mjs` (needs map tile access).
- Diagrams: `flowchart`, `flowchart-vertical`, `hw-pipeline` (hand-drawn), `exploded-stack`,
  `oscilloscope-trace` (CRT waveform).

**Code / developer:** `code-typing`, `code-diff`, `code-highlight`, `code-morph` (Shiki magic move),
`code-scroll`, `code-shader-dissolve` [GL], `code-snippet-dark-2026`, `code-snippet-dark-modern`
(full VS Code chrome), `code-snippet-apple-terminal-pro`. Fit: dev-tool and SaaS feature reels.

**Lower thirds, overlays, social proof cards:** `lt-accent-underline`, `lt-bold-block`, `lt-clean-bar`,
`lt-color-block`, `lt-dark-card`, `lt-kicker-name`, `lt-mask-reveal`, `lt-neon-border`, `lt-side-rule`,
`lt-soft-pill`, `lt-stack-bars` (all 4.8 s name+role lower thirds for talking heads), `lower-third-bild`
(tabloid news), `news-ticker`, `macos-notification`, `x-post` [!], `reddit-post` [!], `yt-comment-card`,
`yt-lower-third` [!], `thread-message-stack`.

**Shader transitions (single, 4 s demo pages with a WebGL canvas) [GL]:** `flash-through-white`,
`whip-pan`, `cinematic-zoom`, `cross-warp-morph`, `domain-warp-dissolve`, `light-leak`, `sdf-iris`,
`glitch`, `chromatic-radial-split`, `gravitational-lens`, `ridged-burn`, `ripple-waves`,
`swirl-vortex`, `thermal-distortion`. These are demos: in a real piece call
`HyperShader.init({... shader: "<name>" ...})` from `@hyperframes/shader-transitions`. Verified
`flash-through-white` renders here (64 s for 4 s at 1080p).

**CSS transition showcases (reference code, 11-24 s each):** `transitions-push`, `-scale`, `-blur`,
`-dissolve`, `-cover`, `-radial`, `-light`, `-distortion`, `-mechanical`, `-grid`, `-3d`,
`-destruction`, `-other`. Overlay transitions: `hw-scribble-transition` 2.2 s, `mk-clone-wall-transition`
2.4 s (tiled word wall with difference blend), `beat-freeze-cut` 6 s (speed ramp + freeze + hard cuts
on the beat), `editorial-flash-overlay`, `organic-light-leak-overlay`.

**Media-treatment overlays and footage dressing:** `camcorder-hud` (REC/battery/date), `freeze-frame-dressing`
(paper, tape, flash around a cutout subject), `snow`, `starfield`, `cinemagraph` (one living region in a
still), `yt-vertical-fill` (portrait media in a wide frame), `hw-frame` (hand-drawn border),
`mk-placeholder-grid` (rounded N-up media grid), `rack-focus` [GL] (real bokeh focus pull),
`camera-dolly-zoom` (vertigo shot on layered depth).

**Backgrounds:** WebGPU shader loops [GPU] 2 s each (shaders.com, MIT): `aurora`, `blob`, `chrome-orb`,
`color-wheel`, `falling-lines`, `flowing-gradient`, `fractal-noise`, `frost`, `gabor-noise`, `godrays`,
`goo`, `heatmap`, `hologram`, `holographic`, `lens-flare`, `light-edge`, `liquid-metal`, `marble`,
`mesh-gradient`, `nebula`, `obsidian`, `plasma`, `plastic`, `prism`, `ripples`, `sine-wave`, `spiral`,
`strands`, `stripes`, `sun-burst`, `swirl`, `thin-film`, `voronoi`, `water`, `waveform`,
`worley-noise`. WebGL [GL] alternatives that work here: `cosmic-orb`, `halftone-field`,
`spiral-galaxy`, `vfx-anamorphic-flare`. DOM: `mk-background` (soft blob gradient, frosted mode),
`yt-lcd-background` (scanline paper board). Fit: hero backdrops; prefer DOM/WebGL here.

**Character:** `lottie-character-walk` 7.5 s (jointed Lottie character walks in and points at a card).

**Showcase pieces (study, don't ship):** `vpn-youtube-spot`, `blue-sweater-intro-video`,
`apple-money-count`, `nyc-paris-flight`.

**Starter examples (`init --example <name>`):** decision-tree, kinetic-type, nyt-graph, play-mode,
product-promo, swiss-grid, vignelli (1080x1920, bold type with red accents), warm-grain.

### 5.2 Components (237)

**Text effects and kinetic type:** `per-word-rise`, `soft-blur-in`, `blur-in`, `blur-out-up`,
`focus-blur-resolve`, `bottom-up-letters`, `top-down-letters`, `staggered-fade-up`,
`per-word-crossfade`, `line-by-line-slide`, `line-swap` (masked beat replacement), `shared-axis-y`,
`shared-axis-z`, `tracking-in`, `kinetic-center-build`, `kinetic-type-swap` (one rolling word slot),
`caret-swap`, `typewriter`, `typed-prompt`, `streaming-text` (AI token rhythm), `scramble-reveal`,
`matrix-decode`, `rgb-glitch-text`, `scan-band`, `char-slam-explode`, `headline-slam`, `shutter-slam`,
`text-shimmer`, `shimmer-sweep`, `colorama-wipe` (AE "shiny wipe"), `inline-highlight`,
`marker-highlight`, `vox-annotate` (Vox-style marker + callout), `strikethrough-replace`,
`ticker-takeover`, `slot-machine-roll`, `number-wheel`, `number-pop-in`, `text-match-cut`,
`type-match-cut`, `morph-text` (gooey), `particle-text-dissolve`, `stitched-text-draw`,
`texture-mask-text` (66 ambientCG texture masks), `variable-axis-type`, `variable-font-flex`,
`wordmark-tiles`, `mk-emphasis-type` (huge ghost word behind subject), `perspective-marquee`,
`titlecard-calm`, `titlecard-lockup`, `text-stagger`, `text-state-swap`. Fit: hooks, taglines,
statement beats; pick one family per video.

**Caption styles (17):** `caption-highlight` (TikTok red word sweep), `caption-pill-karaoke`,
`caption-kinetic-slam` (one full-screen word at a time), `caption-editorial-emphasis` (dual font size
contrast), `caption-weight-shift`, `caption-clip-wipe`, `caption-gradient-fill`, `caption-emoji-pop`,
`caption-neon-glow`, `caption-neon-accent`, `caption-glitch-rgb`, `caption-matrix-decode`,
`caption-particle-burst`, `caption-parallax-layers` (behind-subject depth), `caption-texture`,
`caption-blend-difference` (auto-inverting), `caption-camera-follow` (camera pulls back as words grow).
Fit: on-screen VO captions for reels; `highlight`/`pill-karaoke` for social defaults,
`editorial-emphasis`/`weight-shift` for premium.

**Product demo, UI and cursors:** `browser-device-stage` (default way to show a product: browser,
window or phone chrome with a screen slot), `device-frame-stage`, `multi-device-splay`,
`parallax-device-dive` (camera pushes through a phone screen), `screen-flow-carousel`,
`sticky-mock-swap`, `ui-focus-zoom`, `scroll-camera-story`, `filmed-screen` [GL] (scene filmed off a
monitor with DoF and LED subpixels), `oversized-cursor` (3.5x macOS arrow click), `press-ripple`,
`agent-cursor`, `dart-cursor`, `magnetic-cursor`, `multiplayer-cursors`, `cursor-annotate`,
`cursor-context-menu`, `cursor-drag-drop`, `cursor-glyph-trail`, `cursor-marquee-select`,
`cursor-text-select`, `cursor-zoom-follow` (screen-recording auto-zoom), `gesture-tap`,
`touch-indicator`, `swipe-rail`, `pull-to-refresh`, `sheet-spring-up`, `native-notification-pop`,
`notification-stack`, `notification-pileup`, `chat-message`, `chat-thread`, `typing-indicator`,
`notes-typing`, `code-terminal-run`, `terminal-simulator`, `vector-editor-rig`, `signup-flow`,
`onboarding-stepper-flow`, `settings-toggle-flow`, `toggle-flip`, `state-chip-rail`, `telemetry-hud`,
`segmentation-flood` (machine-vision overlay), `camera-scan-gate` (QR/viewfinder scan + verify), `tracing-beam`, `icon-morph-beat`, `soft-blob-touch`,
plus transitions.dev micro-interactions: `badge-pop`, `card-resize`, `icon-swap`, `input-feedback`,
`menu-morph`, `micro-transitions`, `modal-morph`, `page-slide`, `panel-reveal`, `skeleton-reveal`,
`success-check`, `tabs-slide-indicator`, `tilt-card`, `avatar-group-hover`, `spotlight-card`. Fit:
SaaS/app launch reels built from real screenshots.

**Proof, stats, CTA, end cards:** `count-up`, `chart-story` (bars/line/donut/progress landing exact
values), `animated-bar-chart`, `conic-progress-ring`, `mk-usage-arc`, `decline-chart` (problem
framing), `star-rating-fill`, `testimonial-card`, `testimonial-proof-card`, `social-proof-card`
(app-store close), `logo-wall`, `trust-strip`, `avatar-cloud`, `store-badge-lockup`, `cta-close`,
`cta-lockup`, `logo-brand-close`, `logo-sting`, `x-follow-card`. Fit: every reel's last 3 s; only real
numbers and real testimonials.

**Transitions and reveals:** `cut-the-curve`, `whip-pan-cut`, `match-cut`, `text-match-cut`,
`type-match-cut`, `zoom-through-transition`, `directional-wipe`, `fade-through`, `iris-reveal`,
`morph-swap`, `before-after-wipe`, `comparison-split`, `grade-split-reveal`, `parallax-zoom`,
`parallax-unzoom`, `rubber-band-bumper`, `chromatic-aberration-wipe`, `grid-pixelate-wipe`,
`halftone-dissolve`, `ink-bleed-reveal`, `ordered-dither-pass`, `paper-collage-reveal`,
`torn-paper-rip`, `curtain-reveal`, `particle-image-reveal`, `slit-scan-reveal`, `svg-mask-reveal`
(media through a wordmark), `ascii-trail-reveal`.

**Camera, depth, time:** `push-in`, `pull-back-reveal`, `pan-stations`, `focus-rack`, `focus-swap`,
`drift-hold`, `camera-shake` (9 measured handheld/telephoto/rig profiles), `camera-rig-depth-stack`,
`yt-camera-move` (punch-in/slide/tilt helpers), `extended-keyframe` (AE "never fully lands" arrival
with motion blur), `motion-blur` (shutter-integrated blur), `echo-trail`, `keyframe-scrub-stack`,
`light-sweep-pass` (traveling key light re-shades a scene), `stop-motion-cadence`.

**Layout and assembly:** `grid-card-assemble`, `stagger-cascade`, `stagger-lattice`,
`split-tilt-cards`, `radial-surround`, `constellation-hub`, `locked-nucleus-orbit`,
`overwhelm-surround`, `spring-stack-shuffle`, `velocity-throw-snap`, `physical-exit`, `pendulum-swing`,
`spring-pop`, `gloss-sweep`, `outline-draw`, `separator`, `svg-stroke-trace`, `svg-line-draw-loader`,
`whiteboard-ink`, `facet-morph`, `offset-path-traveler`, `arc-motion-path`, `three-orbiting-cards`
[GL], `confetti` (seeded), `scroll-feed`, `beat-timeline`.

**Backgrounds, texture, finishing:** `grain-overlay` (CSS film grain), `grain-field`, `vignette`,
`aurora-drift`, `mesh-gradient-bg`, `dynamic-grid`, `beat-pulse-background`, `beat-accent` (one music
hit sting), `yt-screen-warp` (footage on a physical display), `yt-feather-highlight` (spotlight hole),
`ascii-render-pass`. Prefer `hyperframes media-treatment` finishing grain/vignette on real footage.

**Hand-drawn annotation:** `hw-arrow`, `hw-boil`, `hw-box-label`, `hw-callout-circle`, `hw-underline`,
`marker-checklist-card`, `yt-circle-pointer`.

**The "hero shelf of 21"** (`registry/components/CATALOG.md`, with use_when/avoid_when/pairs_with):
per-word-rise, scramble-reveal, kinetic-type-swap, oversized-cursor, press-ripple,
browser-device-stage, count-up, chart-story, and others. Read its avoid_when lines; they are real QA
failures (e.g. scramble-reveal reads noisy in calm premium brands).

---

## 6. How to run it here (tested 12 Oct 2026)

### 6.1 Setup

```bash
export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1 HYPERFRAMES_SKIP_SKILLS=1   # last one: no skills check on init
HF="npx -y hyperframes@0.8.150"          # pin; first call installs in ~14 s
$HF --version && $HF doctor              # doctor: 4 s; flags whisper/Kokoro/MusicGen/Chrome/Docker
$HF browser ensure                       # 5 s: downloads pinned chrome-headless-shell 152 from storage.googleapis.com
# alternative: export HYPERFRAMES_BROWSER_PATH=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell  (Chrome 141, worked)
$HF init my-reel --non-interactive --resolution portrait     # 2 s; writes index.html, hyperframes.json, package.json (pins the version), CLAUDE.md
DL=$(mktemp -d) && (cd "$DL" && npm pack gsap@3.14.2 && tar xzf gsap-3.14.2.tgz) \
  && mkdir -p my-reel/assets/vendor && cp "$DL/package/dist/gsap.min.js" my-reel/assets/vendor/
sed -i 's#https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js#assets/vendor/gsap.min.js#' my-reel/index.html
```

GSAP must be local: `cdn.jsdelivr.net`, `unpkg.com`, `cdnjs.cloudflare.com` all return 403 from the
egress proxy, and the scaffold, every registry block/component and the docs load GSAP from jsDelivr.
After every `hyperframes add`, run
`sed -i 's#https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js#assets/vendor/gsap.min.js#' compositions/*.html compositions/components/*.html`
and grep for other CDN URLs (some 3D blocks load three.js / d3 from jsDelivr: vendor those from npm too).

### 6.2 Results table

| Command | Result here | Time |
|---|---|---|
| `--version`, `--help`, `doctor` | works | 14 s first npx, then ~1 s; doctor 4 s |
| `init --non-interactive --resolution portrait` | works | 2 s |
| `lint` | works | 2 s |
| `check` | works after GSAP is vendored (with CDN GSAP: `request_failed ... ERR_TUNNEL_CONNECTION_FAILED` + `page_error`) | 9-17 s |
| `snapshot --at 0.4,1.6,...` | works; writes PNGs + `snapshots/contact-sheet.jpg` (`--describe` needs GEMINI_API_KEY) | 8 s for 6 frames |
| `render` 4 s 1080x1920 DOM | works, beginframe capture, software GPU, 2 auto workers | 16.6-21.2 s |
| `render --quality delivery` 6 s, 3 sub-comps, VO + bed | works, AAC 48 kHz stereo, -15.1 LUFS | 19.3-19.5 s |
| same under CPU contention from other sessions | works | 40-46 s (`--workers 4` did not help) |
| `render` WebGL shader block 4 s 1920x1080 | works via SwiftShader (probe prints "WebGL unavailable" but it renders) | 64 s |
| `render` WebGPU block (`mesh-gradient`) | **fails**: `shaders: WebGPU unavailable (no-adapter)` | - |
| `render --format webm` (transparent root) | works, VP9 `ALPHA_MODE=1`, uses screenshot capture | 16.3 s for 2 s |
| `render --batch rows.json --output "renders/{name}.mp4"` | works, `renders/manifest.json` per row | 15 s for 2 x 2 s |
| `preview --background` / `--status` / `--stop` | works, Studio on `http://127.0.0.1:3002` (200). **Stamps `data-hf-id` into your HTML files** | ~5 s |
| `catalog --query "..." --json` | works, `tier: words` (local word match); `--on-device` needs a 33 MB model | 11 s |
| `add <item>` | works (registry at raw.githubusercontent.com is reachable) | ~2 s each |
| `capture <url> --json` | works for reachable sites (GitHub page: 21 screenshots, 48 assets, tokens.json, 55 s); `example.com` blocked → `BLOCKED.md`, `ok:false` | 55 s |
| `tts "<text>" -v am_michael -o vo.wav` | works with a venv: `python3 -m venv v && v/bin/pip install kokoro-onnx soundfile` (26 s) and `HYPERFRAMES_PYTHON=$PWD/v/bin/python`; downloads model + 27 MB voices from GitHub on first run | 34 s first run for 3.7 s of speech |
| `transcribe` | **fails**: builds whisper.cpp from GitHub fine (132 s, cmake present) then `getaddrinfo ENOTFOUND huggingface.co` for the model. Parakeet also downloads from Hugging Face. Import works instead (verified): `transcribe vo.srt --json` → `transcript.json` (an SRT stays cue-level: 2 cues = 2 entries; feed a word-timed JSON `[{text,start,end}]` for word captions), then `transcribe transcript.json --to vtt -o vo.vtt` | 1 s |
| `remove-background img.png -o out.png` | works on CPU: installs onnxruntime-node once, downloads u2net_human_seg (168 MB) from GitHub | 23 s first run; 0.3 fps |
| `keyframes .` | works (static; component timelines built at runtime show 0 s) | 1 s |
| `timeline --json`, `media-treatment --capabilities` | work | ~1 s |
| `carve.mjs` (hyperframes-audio) | works once `@hyperframes/core@0.8.150` is installed somewhere and passed with `--core` | 5 s install |
| `analyze-beatgrid.py` (music-to-video) | works with system librosa: 129.2 BPM on a 130 BPM test track | 10 s for 16 s |
| `auth status` | exit 1 "Not signed in" (normal offline state) | - |
| `usage --json` | `{"status":"unknown","reason":"unsupported_auth"}`; reports the **agent harness's** (Claude Code/Codex/Grok) plan windows, not HeyGen credits | - |
| `publish`, `cloud render`, `media-use resolve` (bgm/image/icon/voice), HeyGen TTS | not run: need a HeyGen account; `api.heygen.com`, `static.heygen.ai`, `hyperframes.dev` are blocked here | - |

Speed rule of thumb (4 CPUs, idle): DOM/GSAP 1080x1920 at 30 fps ≈ 3.3 s per output second (a 30 s
reel ≈ 100 s); WebGL scenes ≈ 16 s per second at 1080p; transparent output is slower (screenshot path).
`--resolution portrait-4k` renders at a higher device scale factor (more time). Docker mode
(`--docker`) needs the Docker daemon (installed but not running here).

### 6.3 What needs an account or money

| Feature | Needs | Local alternative |
|---|---|---|
| `cloud render` | HeyGen sign-in (`auth login` OAuth or API key), paid per credit, 200 MB upload limit | local `render` |
| `lambda ...` / `cloudrun ...` | your own AWS / GCP account | local render; batch locally |
| `publish` (stable hosted link) | hyperframes.dev hosting (private by default) | our own Artifact/drive delivery |
| `media-use resolve --type bgm/sfx/image/icon/voice/video` | `heygen` CLI ≥0.3.0 signed in (OAuth = free allowance; API key bills credits) or a host `HEYGEN_API_BASE` | bundled 19 SFX; `logo` resolver (theSVG/GitHub/favicon, free); local Kokoro voice; MusicGen/mflux/LTX if installed |
| HeyGen TTS with word timestamps | HeyGen | Kokoro + transcription, or ElevenLabs (TTS with timestamps / Scribe) then `transcribe --import` |
| Avatar video, photo avatar, dubbing | HeyGen (paid/metered) | none |
| `capture` image captions, `snapshot --describe` | `GEMINI_API_KEY` / `GOOGLE_API_KEY` / OpenRouter (optional, ~$0.001/image) | DOM context; our own vision review of contact sheets |
| `figma` import | `FIGMA_TOKEN` | export assets manually |
| On-device catalog search | 33 MB model download (consent) | default word search |
| Everything else (render, check, snapshot, Studio, registry, capture, TTS, bg removal, beats, carve) | nothing | - |

---

## 7. Where it plugs into our A-to-Z reel pipeline

| Stage | Use from HyperFrames | Keep / add from our side |
|---|---|---|
| **Intake** | `brief-contract.md` question protocol; `BRIEF.md` format; destination → aspect rule; stated-vs-inferred receipts; remembered prefs | our client intake skills; claims rules (no invented numbers) |
| **Research** | `capture <url>` → screenshots, `tokens.json` (colors, fonts, CSS vars), `visible-text.txt`, assets, `full-page.png` for scroll shots; `logo` resolver (official marks, never redrawn) | Ad Library / competitor reels; ElevenLabs/Higgs for imagery; blocked sites need user-supplied assets |
| **Concept** | `pitch-round.md` five-concept gate (2 below 0.10, silhouette check); `capability-menu.md` to name the machinery per concept | our scoring and client selection |
| **Script** | `story-design.md` arcs + script bank; VO written as discrete cues; `narration.md`; `SCRIPT.md` format | native-language QA; ElevenLabs voices |
| **Design system** | `frame.md` presets + `build-frame.mjs` remix; `typography.md` (bundled fonts, banned list, in-feed sizes); `video-composition.md`; palettes | per-client token file; `awesome-design-md` brand references |
| **Storyboard** | `STORYBOARD.md` format (status outline→built→animated, `transition_in`, `handoff_out/in`); blueprint per beat (`blueprints-index.md`); sketch sheet `storyboard.html` for approval | our Artifact review page |
| **Build** | compositions (one sub-comp per scene), registry search before hand-authoring, rules/blueprints, `motion-language.md` doctrine, `cut-catalog.md` seams, variables for every client-specific string/color, parallel frame workers with packets (`frame-packets.mjs`) | real subframe motion blur from our `render.mjs` if needed (or registry `motion-blur`) |
| **Sound** | `<audio>` placement, `data-automation` fades/ducks, `data-fx-chain`, voiceover carve, bundled SFX, `analyze-beatgrid.py` / `beats` for cut grids, `audio-reactive.md` | music source (ElevenLabs music / licensed / supplied), human listen gate, **two-pass loudnorm to -14 LUFS / -1 dBTP after render** |
| **Captions** | caption components / embedded-captions identities / `captions.mjs`; `transcribe` import + `--to srt` export | word timings from ElevenLabs Scribe here (HF transcription blocked) |
| **Review** | `check` (+ `--caption-zone` for platform UI), `snapshot` contact sheets at midpoints and cut±, `keyframes` shots, `animation-map.mjs`, `compare`, Studio preview for the client | our scored critique loop (hook, phone readability, motion, variety, brand, sound) |
| **Render** | `render --quality delivery`, `--fps 60` when wanted, `--format mov` (ProRes 4444) / `webm` for overlays, `--resolution portrait-4k` | loudness master, file-size viewing copies |
| **Delivery** | output naming, `renders/manifest.json` | our versioned `deliver/vN/` folders, changelog, Artifact/Drive links (not `publish`) |
| **Versions / formats** | `render --batch rows.json` for copy/colour/CTA variants and A/B hooks; `--variables`; sub-comp `data-variable-values`; recipes (`recipe.mjs freeze`) for repeat clients | native re-layouts per aspect: author a separate root per aspect (9:16, 4:5, 1:1, 16:9) sharing scene sub-comps, because root `data-width/height/duration` are fixed at compile time |

Suggested shape: one project per client deliverable (`motion-studio/projects/<client>/<piece>/`),
`hyperframes init` inside it, `BRIEF.md` → `STORYBOARD.md` → `frame.md` → `compositions/`, every scene a
sub-composition, all client data as variables, gates `lint` → `check --caption-zone` → `snapshot` →
our critique → render → master → deliver. Read `skills/product-launch-video/SKILL.md` as the reference
implementation of this whole loop.

---

## 8. Pitfalls (each one hit or verified here unless marked)

1. **CDN scripts fail silently in render.** jsDelivr is blocked; `check` reports `request_failed` +
   `Cannot read properties of undefined (reading 'timeline')`. Vendor GSAP and any three.js/d3, and
   re-patch after every `hyperframes add`.
2. **The CSS `font:` shorthand bypasses font embedding.** `font: 700 40px "IBM Plex Mono"` rendered a
   generic sans and `check` still passed; `font-family: "IBM Plex Mono"` was fetched and embedded. Always
   write `font-family` explicitly and look for `[Compiler] Fetched ... font face(s)` in the log.
3. **Flex scene clips collapse to the top** unless `.clip { position:absolute; inset:0 }` (the runtime
   only sizes root-level clips that have no computed size). Our first render had all content at the top.
4. **Only one root HTML per project.** A second top-level `.html` with `data-composition-id` is a lint
   error (`multiple_root_compositions`) and disables layout/contrast audits. Keep alternates outside the
   project folder.
5. **A lint error makes `check` lie:** layout/contrast then report `0 samples` / `0/0` which looks clean.
6. **Studio preview rewrites your files** (adds `data-hf-id` to every element in `index.html` and
   sub-comps, writes `.hyperframes/hf-ids-stamped.json`). Commit or diff before opening it; never run it
   on files you don't want touched.
7. **Sub-composition traps:** `<style>`/`<script>` in `<head>` are dropped (put them inside
   `<template>`); host id ≠ inner id ≠ timeline key → 45 s timeout per scene and a frozen render; style the
   sub-comp root with `#root`, not a class; sub-comp timelines cannot reach host elements.
8. **Registry components bring their own opaque `--bg`**, small default type for 9:16, and accent enums
   tied to `--brand/--accent/--accent-2`. Set theme tokens on `#root` and edit the installed copy.
9. **Root `data-duration` is compile-time.** Variables cannot change render length; make per-length
   cutdowns separate roots.
10. **`<audio>` without `id` renders silent;** two overlapping `<audio>` on the same track index warn;
    a volume tween is ignored when a lane exists. No automatic loudness target: master yourself.
11. **Dark gradients band.** Visible rings in our radial gradient at CRF 16. Add grain
    (`grain-overlay` or media-treatment finishing grain), avoid full-screen linear gradients on dark.
12. **WebGPU blocks do not render here** (~40 items incl. all shaders.com backgrounds,
    `ios26-liquid-glass`, `liquid-glass-*`, `frost-sequence-camera-orbit`); WebGL renders but ~5x slower
    than DOM. Check the tag before planning a hero shot around a block.
13. **Transcription is blocked here** (Hugging Face). Captions need ElevenLabs/HeyGen timings or a
    supplied transcript imported with `transcribe <file.json|srt|vtt>`.
14. **Spinner output floods logs.** Pipe through `| tr '\r' '\n' | tail` or use `--json`; tts/remove-background
    print hundreds of spinner frames.
15. **Shared container contention.** Other sessions' Chrome renders doubled our render times; measure on
    an idle box, and never kill processes you didn't start.
16. **`usage --json` is not a HeyGen meter** (it reads the agent harness login); `auth status` exits 1
    when signed out by design (don't `set -e` on it).
17. **The skills push upsells and telemetry:** `skills update` on init (set `HYPERFRAMES_SKIP_SKILLS=1`),
    desktop-app "Framey" lines after renders, `feedback` reports to a public channel, `publish`. Skip all
    for client work.
18. **Motion-doctrine conflicts:** `house-style.md` (ambient breathing on decoratives) vs
    `motion-language.md` (no lazy breathing). Use the latter for premium.
19. **Brand look-alike blocks and unconfirmed textures** (section 1): legal review before client use.
20. **Registry `add` always needs the network** and only accepts `https://` registries; offline, copy
    files by hand from `references/hyperframes/registry/<blocks|components>/<name>/` (pinned to the clone's
    commit, which matches CLI 0.8.150).
21. **`transform` on inline spans is a no-op** and scaling a 0-width element shows nothing: make animated
    words `display:inline-block` and bars `display:block` with a real width.
22. **Never pair a CSS `transform` with a GSAP tween on the same property** (`gsap_css_transform_conflict`);
    center with flex/inset, not `translate(-50%,-50%)`.
23. **`data-start="intro-0.5"` without spaces** silently resolves to 0; snapshot reference-timed clips.
24. **Do not run `npx skills add ... --all` inside a HyperFrames checkout** (it deletes `skills/` dirs),
    and never modify `references/`.

---

## 9. Test artifacts

Everything from these tests is in the scratchpad (session-only):
`/tmp/claude-0/-home-user-main/e4f36c47-85ff-5efa-82ed-895fc9328db0/scratchpad/hf-test/` — `reel-test/`
(modular reel with sub-comps, components, VO, bed; renders and contact sheet), `mono-test/` (the minimal
example above), `var-test/` (batch variables + transparent WebM), `gl-test/` (WebGL shader transition),
`gpu-test/` (failed WebGPU), `capture-test2/` (GitHub capture), logs `render*.log`, `check*.log`.
Caches written to `~/.cache/hyperframes/` (1.4 GB: Chrome 152, fonts, Kokoro, whisper.cpp build, u2net)
and `~/.hyperframes/` (config with telemetry disabled).
