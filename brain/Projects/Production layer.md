---
type: project
updated: 2026-10-18
tags: [project, production, pipeline, gates, qa, higgsfield, elevenlabs]
---

# Production layer

How every image, carousel and video for a [[Growth Engine]] post is made, checked and let through. The Growth Engine
decides **what** to post; this layer decides **how**, and makes the checks impossible to skip: a hook blocks any
Higgsfield or ElevenLabs generation whose gates have not passed. Motion reels are built in [[Motion Studio]] and then
pass the same gates. Back to [[00 Index]].

Start with `growth-engine/production/README.md`.

Source: growth-engine/production/README.md

## Files

| File | What it is |
|---|---|
| `AI-VIDEO-PIPELINE.md` | Owner's spec, verbatim: the 16 steps (0 to 15) with gates, per-format table, house rules, the 18 inconsistencies |
| `VISUAL-QA.md` | Owner's spec, verbatim: Shot Specs, gate map, prompt cards, the three fresh reviewers, storyboards, enforcement |
| `STANDARDS.md` + `standards.json` | The one numbers file (prose in .md, machine values in .json that the gate reads) |
| `STORY-FORMATS.md` | Story reels: templates, animation styles, how they fit the week and the budget |
| `failure-library.md` + `failure-log.csv` | Known failure patterns FL-01 to FL-13; the raw log every FAIL writes |
| `schemas/shot-spec.schema.yaml` | The Shot Spec schema |
| `install-gate.sh` | Installs the generation gate for a session rooted above the repo |
| `queue/<date>.md` | The daily human approval queue (`pipeline.py queue --write`) |
| `audit/` | The 15 Oct 2026 skill audit and Kallaway research behind STANDARDS |

Source: growth-engine/production/README.md, ls growth-engine/production

## The 16-step gated pipeline

Rule behind the order: words before sound, sound before pictures, plan before assets, look before you cut. Every post
is one run: `pipeline.py init <slug> <post_id> --format F --card <path>`.

| # | Step | What it locks | Gates |
|---|---|---|---|
| 0 | Foundation and brief | Avatar, buyer words, beliefs, proof, offer, the Post Card | G-BRIEF |
| 1 | Idea, angle and THE PICTURE | One angle, one visual metaphor, the length tier | G-IDEA |
| 2 | Hook (visual, text, spoken) | A or A+ hook stack, before any script line | G-HOOK |
| 3 | Script | Script Lab release at 85/100 after a fresh cold read; spine pick | G-SCRIPT, G-HUMAN-SPINE (delegable) |
| 4 | Audio (voice, conversation, song, music, SFX) | The timing master; budget runs before the first generation | G-BUDGET, G-AUDIO per audio asset, G-AUDIO-MASTER, G-HUMAN-VOICE (once per voice), G-HUMAN-SONG (every song) |
| 5 | Audio analysis and timeline | Word timestamps, pause map, slices of 5 to 15 s | G-AUDIO per slice, G-TIMELINE |
| 6 | Visual plan | One Shot Spec per shot or slide (visual-planner), linted, fresh review | G-PLAN, G-SPEC |
| 7 | Look bible | Style, character, set and prop sheets on the client's LIB run, once per series | G-PROMPT-IMG, G-VIS-SHEET, G-HUMAN-LOOK |
| 8 | Storyboards (motion: code text check, hook styleframe) | One board per sequence, hook board first | G-PROMPT-IMG, G-VIS-BOARD, G-CONTINUITY, G-HUMAN-HOOKBOARD; motion: G-MOTION-TEXT |
| 9 | Budget preflight | The whole piece re-priced (+25%) against the cap and live balance | G-BUDGET recorded after steps 0 to 8 closed |
| 10 | Generate | Only registered prompts and references; no video call before step 9 | G-PROMPT-IMG or G-PROMPT-VID per prompt |
| 11 | Per-asset QA | Review packet per asset, fresh reviewer | G-VIS*, G-TAKE, G-MOTION-FRAMES, G-AUDIO; closes as G-ASSETS |
| 12 | Edit | Audio master is the timeline; captions in the safe zone; loudness | (checked at 13) |
| 13 | Final QA and Director | Sound-off, sound-on, voice-alone, transcript, banned-model check | G-FINAL, G-DIRECTOR |
| 14 | Package and approval | Hub draft; owner approves on the Content page | G-HUMAN-FINAL |
| 15 | Learn | Analyst at 72 h and 7 d; lessons and hook library | G-LEARN |

**Families skip steps they don't have** (`standards.json` families): `still` (images, carousels) skips 4, 5, 8, 12
(step 11 is G-VIS-SLIDE, step 13 is G-SET); `keyframe_reel` (tier C quote reel) skips 8; `real` (owner footage) skips
7 to 10; `motion`, `ai_video` and `song` run every step (song adds G-HUMAN-SONG at step 4).

Source: growth-engine/production/AI-VIDEO-PIPELINE.md sections 1 and 2, growth-engine/production/README.md ("One post, start to finish"), growth-engine/production/standards.json (families)

## The gate ledger

- One folder per post: `clients/<slug>/runs/<post_id>/` with `ledger.json`, `shots/`, `prompts/`, `qa/`, `assets/`,
  `audio/`, `edit/`, `final/` and `calls.jsonl`.
- Each asset version has an entry: type, what it depends on, the prompt's hash, and its gates with status and report.
- A gate passes only when its report exists with PASS for that exact asset version.
- Only `pipeline.py` changes gate status. Reviewers return JSON; the orchestrator records it (`pipeline.py record`).
- A version is generated once; a retake is a new version, so attempts are counted.
- Client-wide assets (style reference, cast sheets, voice approval) live on a LIB run. StraightScale's is
  `runs/SS-LIB-STYLE`.
- `pipeline.py status <slug> <post_id>` shows steps, gates, open items and the next action.

Source: growth-engine/production/VISUAL-QA.md section 9.1, growth-engine/tools/pipeline.py --help, growth-engine/production/README.md

## The generation hook (and GATE-SELFTEST)

- `.claude/hooks/generation_gate.py` is a PreToolUse hook registered in `.claude/settings.json`. It matches the
  Higgsfield generation tools (images, video, audio, batches, presets, outpaint, motion control, Ads Studio, Shorts
  Studio, AI influencer) and the ElevenLabs creative generation tools (speech, image, edit, video, flows).
- It calls `pipeline.check_call` (same logic as `pipeline.py check-call <tool> <input.json>`). It **fails closed**: if
  the check errors, the call is blocked.
- Before a generation it requires: every Shot Spec served is linted with a G-SPEC PASS for its current file; a
  G-PROMPT PASS for this exact prompt, with the reviewed references in the same order and roles; every reference is a
  registered asset whose own review passed; the model rules of STANDARDS 1 and 2; audio only after G-SCRIPT 85+; a
  G-BUDGET PASS from the last 24 hours, and step 9 closed for any video call; for talking or multi-shot video, a
  storyboard with G-VIS-BOARD and G-CONTINUITY as image 1; for a song run, G-HUMAN-SONG before any picture.
- One exception: the **edit pass**, an image asset's own previous version as the single reference (role
  `edit_source`). It is a new version, one attempt, with its own full review.
- Cost preflights (`get_cost`, `estimate_only`) always pass.
- **GATE-SELFTEST:** the prompt `GATE-SELFTEST` is always blocked. A session rooted above the repo first runs
  `bash growth-engine/production/install-gate.sh`, then calls `generate_image` with that prompt; it must come back
  blocked ("the production gate is live"). If it generates instead, stop and say so: never produce without the gate.

Source: .claude/hooks/generation_gate.py, .claude/settings.json, growth-engine/production/install-gate.sh, growth-engine/production/README.md ("What the gate checks"), growth-engine/DAILY.md section 0, growth-engine/tools/pipeline.py (GATE-SELFTEST check)

## Fresh reviewers

Generators never grade their own work. The producer writes the prompt and generates; a separate fresh agent judges the
output against the Shot Spec, not against the prompt.

| Agent | Checks | Gates |
|---|---|---|
| visual-planner | Writes one Shot Spec per shot, slide or scene (regions for every hand, prop, text surface, face); runs `spec-check` | G-PLAN, feeds G-SPEC |
| prompt-reviewer | Shot Specs (spec mode), prompts before any credits, motion code text before any render; checks P1 to P12 | G-SPEC, G-PROMPT-IMG, G-PROMPT-VID, G-MOTION-TEXT |
| visual-reviewer | Stills, sheets, storyboards, slides, statics: V1 to V26; set mode for continuity and carousel sets | G-VIS, G-VIS-SHEET, G-VIS-BOARD, G-VIS-SLIDE, G-CONTINUITY, G-SET |
| take-reviewer | Video takes T1 to T9, motion renders M1 to M7, final cuts F1 to F8 | G-TAKE, G-MOTION-FRAMES, G-FINAL |

Rules: a new agent for every review and every retry; it gets only the packet, never the producer's reasoning; it must
open every file in the packet's `must_open` list (`pipeline.py record` checks `files_opened`). If a reviewer type is
not registered in the session, run a general-purpose agent told to read and follow that agent file. Above them, the
Organic Director judges the assembled piece.

Source: growth-engine/production/VISUAL-QA.md sections 1 and 9.3, .claude/agents/visual-planner.md, prompt-reviewer.md, visual-reviewer.md, take-reviewer.md, growth-engine/DAILY.md section 3, growth-engine/tools/vqa_crops.py (docstring)

## Pass rules

- Hook: all 9 Hook Lab gates; every channel A or A+; a fresh grader agrees on the master stack.
- Script: 85/100 or more, no critical fail, after a fresh cold read (two from O60 up). 3 FIX loops, then the owner.
- Spec: lint clean and a fresh prompt-reviewer PASS for the current file.
- Prompt: P1 to P12 all PASS; after 2 failed loops it goes to the Organic Director.
- Visual: hero assets (frame 1, hook concept frame, storyboards, sheets, covers, start frames, the style reference):
  zero defects. Others: zero critical, zero major, at most 2 minor. 3 attempts per asset, then the owner.
- Take: zero critical, zero major, drift fixable in the edit, every scripted word present.
- Audio: each audio asset passes its take check, recorded as G-AUDIO; without it the file can't be a reference.
- Assets (step 11): every asset's latest version passed its own gate.
- Final: F1 to F8, sound-on watch, voice-alone listen, banned-model check, then the Director, then the owner.

Fix routes on a FAIL, in order: edit pass (local defects), regenerate with a corrected prompt (structural defects),
simplify the shot (after 2 fails), escalate to the owner (after 3 attempts). Retakes don't wait for Matan; failed
versions are listed to him as an FYI in the run summary.

Source: growth-engine/production/STANDARDS.md section 9, growth-engine/production/VISUAL-QA.md section 5.5, growth-engine/production/README.md ("Who decides what")

## Human checkpoints (owner, batched daily)

Matan answers once a day from `growth-engine/production/queue/<date>.md`: look bible once per client or series
(G-HUMAN-LOOK), every hook storyboard (G-HUMAN-HOOKBOARD), each new voice once (G-HUMAN-VOICE), every song master
(G-HUMAN-SONG), escalations after 3 failed attempts (G-HUMAN-ESCALATE), model re-tests (G-HUMAN-TEST), model
exceptions (G-EXCEPTION), and the final approval of every post on the hub (G-HUMAN-FINAL). The Organic Director
decides Kling fallbacks (G-FALLBACK). The spine pick (G-HUMAN-SPINE) is delegated: Claude picks and says why.

The last queue file in the repo is `queue/2026-10-16.md` with 6 pending items: R1 and R2 model re-tests, D9 drama
model routing, the narrator voice listen (G-HUMAN-VOICE), the carousel weekly budget line, and what to do with the
live 15 Oct carousel that shows a model-drawn logo. Whether any were answered since is not recorded in what I read.

Source: growth-engine/production/standards.json (human_checkpoints), growth-engine/production/STANDARDS.md section 9, growth-engine/production/queue/2026-10-16.md

## Failure Library

Each pattern has prevention (what the prompt must say), detection (what the reviewer looks at) and a fix route. The
prompt-reviewer fails a prompt that matches a pattern without its prevention (check P12).

| Id | Pattern |
|---|---|
| FL-01 | Text over hands |
| FL-02 | Object structure wrong |
| FL-03 | Action not happening |
| FL-04 | Empty story props |
| FL-05 | Empty background frames and screens |
| FL-06 | Faceless or blob anatomy in close-ups |
| FL-07 | Video without a storyboard; prompt ignores the attached images |
| FL-08 | Phone vanishes mid-gesture |
| FL-09 | Frozen background in video |
| FL-10 | Gibberish banners and signs in H3 |
| FL-11 | Cloned character in one panel; floating person |
| FL-12 | "Same pose, different man" across models |
| FL-13 | Model-drawn logo (models never draw the logo; the real file goes on afterwards) |

Every FAIL is logged to `failure-log.csv` by `pipeline.py record`. In the Monday memo the Organic Director turns a new
failure into the next FL entry the same week; a pattern seen 3 times despite its prevention gets a stronger prevention
or a simpler default shot.

Source: growth-engine/production/failure-library.md

## Where the numbers live

All production numbers live in `growth-engine/production/STANDARDS.md` (v1.1, 16 Oct 2026) and `standards.json`. On a
number, STANDARDS wins over every skill and doc; on method, the skill wins. Other notes should cite the section, not
copy the number.

| Section | Holds |
|---|---|
| 1 | Models per use (H3 for video, GPT Image 2 for realistic people, GPT Image 2.5 for carousels and statics, Nano Banana 2 for stylized sheets until R1, claymation route) |
| 2 | H3 clips (slice lengths, words and shots per take) |
| 3 | Stills, sheets, storyboards |
| 4 | Audio (voice, pace, music bed, loudness) |
| 5 | Picture and edit (frame rates, cut rules) |
| 6 | Text, captions and the reels safe zone |
| 7 | AI disclosure and how AI people are shown |
| 7b | Drama exceptions X1 to X10 |
| 8 | Lengths (tiers O15, O30, O60, O90, podcast C45): the single source |
| 9 | Pass rules and human checkpoints |
| 10 | Budget (prices, when G-BUDGET runs) |
| 11 | QA methods |
| 12 | What each skill keeps and what STANDARDS overrides |
| 13 | The 18 issues, checked and resolved |
| 14 | Open re-tests and owner decisions |

Source: growth-engine/production/STANDARDS.md (headings and precedence)

## Tools

| Tool | What it does |
|---|---|
| `growth-engine/tools/pipeline.py` | Runs, ledger, `status`, `step`, `spec-check`, `asset`, `prompt`, `media`, `record`, `gate`, `budget`, `ask`, `approve`, `queue`, `check-call` |
| `growth-engine/tools/vqa_crops.py` | Review packets: `image` (full, 3x3 tiles at 2x, region crops, 200 px thumbnail), `frames`, `motion`, `final`, `drift` (H3 lip-sync), `loudness` |
| `growth-engine/tools/brand_overlay.py` | Pastes the client's real logo file (from `clients/<slug>/brand/`) onto a reviewed image; refuses a busy or bright corner |
| `growth-engine/tools/fix_drawn_logo.py` | Repairs older images where the model drew a logo: inpaints it and pastes the real file; the output gets its own review |
| `growth-engine/production/install-gate.sh` | Installs the hook for sessions rooted above the repo |

Run from the repo root: `python3 growth-engine/tools/pipeline.py ...`.

Source: growth-engine/tools/pipeline.py --help, vqa_crops.py, brand_overlay.py, fix_drawn_logo.py (docstrings), growth-engine/production/README.md

## Story formats and how they fit the week

- A story post is three choices on one Post Card: `story_template` (the narrative), `format` (who is on screen, which
  skill, tier), `animation_style` (animated formats only). Templates and styles are listed in [[Growth Engine]].
- Weekly rhythm (STORY-FORMATS 5.1): Monday a story reel (reach, B1 or B2) opens the week's question; Tuesday a One
  Step carousel teaches the fix; Wednesday a second reel angle; Thursday an owner self-check carousel (ANALIZA);
  Friday a convert reel (ANALIZA); Saturday the owner-question image; Sunday a carousel retelling the tier A piece or a
  One Step episode.
- The chain: the story reel names the cause, the next carousel teaches the step, keyword posts send people to the
  hub funnel.
- Lab, then factory: test a new angle cheap (carousel, quote reel, animation short); an angle that beats the median
  gets `angle_proven` and may go tier A; one wildcard a month.
- A tier A piece makes 6 derived assets: main cut, short cut, 3 hook variants as trial reels, a retelling carousel,
  2 or 3 Story frames, an ad version.
- A worked StraightScale month (cap 1,300) is priced in STORY-FORMATS 5.6 at about 990 to 1,492 credits, with two
  written controls that cut the top under the cap.
- Story pieces are made in a normal session, not in the daily run.
- AI people (until decision D1): shown only from behind, hands only, at a distance, or stylized; never presented as a
  real client. A confession POV needs real footage. See [[Standing rules]] and [[StraightScale decisions]].

Source: growth-engine/production/STORY-FORMATS.md sections 1, 5 and 6, growth-engine/production/STANDARDS.md section 7, growth-engine/DAILY.md section 3

## Open re-tests and decisions

R1 (stylized model side-by-side, about 10 credits), R2 (H3 duration re-test, about 80 credits), D1 (AI label and AI
people), D9 (drama model routing), H1 (whether the owner restores four human listens). Status as of STANDARDS v1.1,
16 Oct 2026; later answers unknown.

Source: growth-engine/production/STANDARDS.md section 14

## Related

[[Growth Engine]] · [[Motion Studio]] · [[StraightScale]] · [[Standing rules]] · [[How Claude uses this brain]]
