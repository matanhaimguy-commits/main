# Motion studio knowledge base

Read this first on any video job, then follow `.claude/skills/motion-reel/SKILL.md` (the A-to-Z workflow).
The guides below were written from full reads of the five reference repos and from tests in this container
(12 Oct 2026). The repos themselves live complete and unmodified in `references/` (`bash references/fetch.sh`
in a new session); every path inside a guide points into them.

## The guides

| Guide | Covers | Read it when |
|---|---|---|
| [`our-pipeline.md`](our-pipeline.md) | Everything we built before (motion-studio engine, the StraightScale reels, OpenMontage, account skills), what worked, what broke and why, the honest quality bar, the 17 gaps to $10k work, reusable pieces | Starting any job; deciding what to reuse |
| [`hyperframes.md`](hyperframes.md) | HyperFrames: composition model, motion doctrine, transitions, captions, audio mixing, the 447-item registry catalogue, tested CLI commands and speeds, what needs a HeyGen account | Building most reels (it is the default engine and master timeline) |
| [`lemo-opuscar.md`](lemo-opuscar.md) | 43 film styles + 98 style prompts, the director's process (treatment, story rules, failures), painterly rendering, sampler music, tested setup and speeds | Choosing a look; painterly/illustrated films; treatment; real-instrument scores |
| [`onetake-principles.md`](onetake-principles.md) | Craft principles for product motion (rhythm vs carry, concepts before beats, operated camera, cause, meaning in the artwork, shutter blur, sound as one room), measuring references, the acceptance-check spec, UI rebuilt from screenshots, the 8 review gates | Concepts, beat sheets, product demos, review. Study only: never use onetake's code or text |
| [`claude-animation-base.md`](claude-animation-base.md) | Hand-painted character animation: the 7 rules, the full engine API, the catalogue (5 views, 31 emotions, 18 emotes, hats, dances, transitions, camera, light, paper), client mascot adaptation, tested 9:16 renders and speeds | Any character, mascot, host or reaction moment |
| [`gbro-collage-broll.md`](gbro-collage-broll.md) | Editorial halftone paper-collage B-roll: finding the visual metaphor, art direction, prompts, QA, and four ways to make it here without Codex or Gemini | Abstract lines that need a visual metaphor; collage inserts |

## Where to find it

| I need... | Look at |
|---|---|
| The order of work and the gates | `.claude/skills/motion-reel/SKILL.md` |
| House rules (render contract, banned looks, sound, review loop) | `motion-studio/CLAUDE.md` |
| A look to choose from | Lemo styles: `lemo-opuscar.md` §5 and `references/lemo-opuscar/styles/*/STYLE.md` (posters in each style folder) · `references/lemo-opuscar/styleboard/opuscar98_styles.json` · HyperFrames blueprints and design presets: `hyperframes.md` §4.2-4.3 · brand UI systems: `.claude/skills/awesome-design-md/design-md/` |
| A named effect (glitch, film grain, chart, code window, map, shimmer...) | HyperFrames registry: `hyperframes.md` §5, `references/hyperframes/registry/` (search with `catalog --query` before building anything by hand) |
| Transitions and cut rules | `hyperframes.md` §4.4 and `references/hyperframes/skills/product-launch-video/references/cut-catalog.md` · carry vs swap: `onetake-principles.md` P1, P6, P8 |
| Motion feel (easing, springs, camera) | `references/hyperframes/skills/product-launch-video/references/motion-language.md` · `onetake-principles.md` P4, P9, P10 · `motion-studio/lib/motion.js` |
| Typography in motion and sizes for phones | `hyperframes.md` §4.2 (typography, in-feed sizes) · `templates/project/brand.md` |
| Concepts and story structure | `onetake-principles.md` P3 · `lemo-opuscar.md` §3.3-3.4 · HyperFrames pitch round (`hyperframes.md` §4.8) |
| Character acting (emotions, takes, timing for the viewer) | `claude-animation-base.md` §2 and §4 · `references/claude-animation-base/docs/emotions.jpg`, `views.jpg` |
| Painterly rendering techniques | `lemo-opuscar.md` §4.2-4.4 (impasto knife strokes, watercolour, texture, camera) |
| Product UI demos without screen recording | `onetake-principles.md` §5 |
| Captions | `hyperframes.md` §4.7 (35 caption styles, word-timed JSON import) |
| Music, SFX and mixing | `hyperframes.md` §4.6 (automation, carve) · `lemo-opuscar.md` §4.6 (sampler, foley, silences) · `projects/straightscale/audio/score.py` and `finish.sh` |
| Measuring a reference or our draft | `motion-studio/tools/pacing.py` · method: `onetake-principles.md` §3 |
| Review checks | `onetake-principles.md` §8 · `motion-studio/tools/` (`seekcheck.mjs`, `pacing.py`, `audio_qa.py`) · `templates/project/docs/review_log.md` |
| What broke before (so it doesn't again) | `our-pipeline.md` §3 "Lessons from the history" |
| Which tools in this session do what (voice, music, images, research) | `our-pipeline.md` §9 |

## Speeds measured here (4 CPUs, no GPU)

| Engine | Speed |
|---|---|
| HyperFrames DOM/GSAP, 1080x1920, 30 fps | ≈ 3.3 s per second of video (WebGL scenes ≈ 16 s per second) |
| motion-studio canvas, 60 fps, 4 subframes, 3 parallel segments | 50 s film ≈ 8-15 min |
| Lemo-Opuscar 2D styles | 0.1-1.5 s per frame |
| Lemo-Opuscar impasto (WebGL oil paint), 24 fps | ≈ 20 min per 15 s |
| Lemo-Opuscar 3D | 68-120 s per frame: stills only |
| Claude Animation Base, 24 fps | ≈ 5 s per frame low-fill; ≈ 50 s per frame with full watercolour fills |
