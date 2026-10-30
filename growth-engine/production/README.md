# Production: how every post gets made, checked and let through

Organic Growth OS (`../ORGANIC-OS.md`) decides **what** to post and why. This folder decides **how** every image, carousel
and video is made, and makes the checks impossible to skip.

| File | What it is |
|---|---|
| `AI-VIDEO-PIPELINE.md` | The owner's spec: 16 steps (0 to 15) with gates, per-format table, house rules, the 18 inconsistencies (section 5). Verbatim. |
| `VISUAL-QA.md` | The owner's spec: Shot Specs, gate map, prompt cards, the three fresh reviewers, storyboards, the Failure Library, enforcement. Verbatim. |
| `STANDARDS.md` + `standards.json` | **The one numbers file.** Every model, duration, word budget, loudness, safe zone and pass rule, with the 18 issues resolved and the open re-tests. Prose in the .md, machine values in the .json (the gate reads it). |
| `FORMATS.md` | **The format library.** Every format we can make (UGC, whiteboard presenter, podcast, drama, song, animation styles, talking object, carousel, static, motion as one option among many): the beat and funnel stage it carries, its L19 properties, the skill and gates, the Atlas route, the price, StraightScale's past pieces, and the model gaps as owner decisions. The router ranks by it. |
| `STORY-FORMATS.md` | Story formats for organic posts: POV day in the buyer's life, two days, the problem as a villain, song, podcast, drama; animation styles; how they fit the weekly mix and the budget. |
| `schemas/shot-spec.schema.yaml` | The Shot Spec schema (VISUAL-QA section 2). |
| `failure-library.md` | FL-01 to FL-13 and how new patterns get added. `failure-log.csv` is the raw log every FAIL writes. |
| `install-gate.sh` | Installs the generation gate for a session rooted above the repo. |
| `queue/<date>.md` | The daily human approval queue (`pipeline.py queue --write`). |

Tools and agents:

| Where | What |
|---|---|
| `growth-engine/tools/pipeline.py` | Runs (one folder per post), the gate ledger, spec lint, reviewer records, budget gate, human checkpoints, the queue, and `check-call` (the gate logic). |
| `growth-engine/tools/vqa_crops.py` | Review packets: full image, 3x3 tiles at 2x, region crops, storyboard panels, 200 px thumbnail, frame contact sheets, H3 drift, loudness. |
| `.claude/hooks/generation_gate.py` + `.claude/settings.json` | The PreToolUse hook: refuses Higgsfield outright (switched off, owner 28 Oct 2026; generation runs on Atlas) and blocks ElevenLabs generation unless the gates pass. Fails closed. |
| `growth-engine/tools/atlas/` | Atlas Cloud behind the same gate: `setup.sh` installs the pinned CLI and the `atlas` wrapper, which sends every billable `atlas generate` call through `pipeline.py check-call atlas_generate` and blocks `atlas chat`. Models only from `standards.json` `models.atlas.allowed`, each entry with its parameters and text fields (empty today: every Atlas generation is blocked). Fails closed. |
| `.claude/agents/visual-planner.md` | Writes the Shot Specs (step 6). |
| `.claude/agents/prompt-reviewer.md` | Fresh reviewer: Shot Specs (G-SPEC), prompts (G-PROMPT-IMG, G-PROMPT-VID), P1 to P12, and a motion piece's code text before any render (G-MOTION-TEXT). |
| `.claude/agents/visual-reviewer.md` | Fresh reviewer: stills, sheets, storyboards, slides (V1 to V26), continuity and carousel sets. |
| `.claude/agents/take-reviewer.md` | Fresh reviewer: video takes (T1 to T9), motion renders (M1 to M7), final cuts (F1 to F8). |
| `growth-engine/adapters/*-organic.md` | How each production skill runs for organic posts (the organic CTA ladder instead of the paid offer close, B2B hooks, AI label, organic LEARN). |

## One post, start to finish

```
Post Card (cards/<yyyy-mm>-W<n>/<post_id>.yaml)          organic.py card-check, route
  → pipeline.py init <slug> <post_id> --format F --card ...  runs/<post_id>/ledger.json
  → steps 0-3: brief, idea + THE PICTURE, hook (Hook Lab), script (Script Lab)    G-BRIEF G-IDEA G-HOOK G-SCRIPT(85+) G-HUMAN-SPINE
  → pipeline.py budget before the run's FIRST generation (see below)                 G-BUDGET (cap, live balance, +25%)
  → step 4: voice, song, music, SFX (video only)                                    G-AUDIO per audio asset, G-AUDIO-MASTER,
                                                                                     G-HUMAN-VOICE once per voice, G-HUMAN-SONG every song
  → step 5: slices + timeline (video only)                                           G-AUDIO per slice, G-TIMELINE
  → step 6: visual-planner writes shots/*.spec.yaml → spec-check → prompt-reviewer   G-PLAN, G-SPEC per shot
  → step 7: look bible (sheets, prop sheets) on the client's LIB run                 G-PROMPT-IMG, G-VIS-SHEET, G-HUMAN-LOOK once
  → step 8: storyboards → visual-reviewer per panel + continuity set                 G-PROMPT-IMG, G-VIS-BOARD, G-CONTINUITY,
            (motion: G-MOTION-TEXT on the code, then the hook styleframe)            G-HUMAN-HOOKBOARD (hook board → owner)
  → step 9: pipeline.py budget again: the whole piece re-priced                      G-BUDGET recorded after steps 0-8 closed
  → step 10: generate (the hook checks every call; no video call before step 9)     G-PROMPT-IMG / G-PROMPT-VID per prompt
  → step 11: vqa_crops.py → visual/take reviewer per asset                           G-ASSETS: every asset's own gate
                                                                                     (G-VIS*, G-TAKE, G-MOTION-FRAMES, G-AUDIO)
  → steps 12-13: edit → final review + Director                                      G-FINAL, G-DIRECTOR
  → step 14: hub draft → owner approves on the Content page                          G-HUMAN-FINAL
  → step 15: analyst at 72 h and 7 d → learnings, Hook Library, lessons             G-LEARN
```

**Budget timing (STANDARDS 10).** `pipeline.py budget` runs before the run's first generation: at step 4 for voiced
pieces (the ElevenLabs voice is a generation), before step 7 on a LIB run, before the first slide on a carousel. It
runs again within 24 h of each later batch. Step 9 then re-prices the whole video: it closes only on a G-BUDGET
recorded after steps 0 to 8 closed, and the gate refuses every video call until step 9 is closed.

**Gates that sit on the ledger, not on a call (STANDARDS 9).** G-AUDIO: each audio asset (voice, slice, song, music,
SFX) passes its take check, recorded with `pipeline.py gate <slug> <post_id> G-AUDIO --status PASS --by <who> --asset
<ID>@v<n> --note "..."`; an audio file without it can't be a reference in an H3 call. G-ASSETS: step 11 closes when every
asset's latest version passed its own gate (`pipeline.py status` lists what is open). G-MOTION-TEXT: a fresh
prompt-reviewer checks a motion piece's code text constants before any render, recorded with `pipeline.py record` on
the `motion_render` version; G-MOTION-FRAMES fails on a version without it.

Each family skips what it doesn't have (standards.json `families`): carousels and images skip audio, timeline,
storyboards and edit; the tier C quote reel (`keyframe_reel`) skips the storyboard (one silent shot) and its step 4
needs G-HUMAN-VOICE until the narrator's record exists; song pieces (`reel_song`, family `song`) run every step and
step 4 adds G-HUMAN-SONG; motion reels put G-MOTION-TEXT before any render at step 8; real footage skips the look
bible, storyboards, credits and generation.

## What the gate checks before a generation call runs

For the exact prompt text (whitespace aside) it finds the registered asset version, then requires:
- every Shot Spec it serves is linted and has a G-SPEC PASS **for its current file**;
- a G-PROMPT PASS (G-PROMPT-IMG for images, G-PROMPT-VID for clips) for **this exact prompt**; the references in the
  call are the reviewed ones, same order, same roles;
- every reference is a registered asset whose own review passed; sheets come from an owner-approved look bible. The
  one exception is the **edit pass** (VISUAL-QA 5.5 route 1, STANDARDS 1): an image asset's own previous version (same
  asset id, same run, any gate status) as the **single** image reference, registered with role `edit_source`
  (`pipeline.py prompt ... --media <previous version's job id>:edit_source`) and passed in the call as
  `image_references` (`image` on `gpt_image_2`). The edit is a new version, counts as one attempt and gets its own full
  review;
- talking or multi-shot video: image 1 is a storyboard with G-VIS-BOARD and G-CONTINUITY PASS (hook boards also
  need the owner). Silent keyframe clips are one shot each (start image, optional end image), so they need no
  storyboard; a chain of silent shots is several one-shot clips (STANDARDS 2). Every audio reference has its own
  G-AUDIO PASS;
- the model rules (STANDARDS 1 and 2, standards.json): Atlas only, on the owner's named models with their settings
  (H3 at 768P, 4 to 15 s; `openai/gpt-image-2` at medium; voices on `elevenlabs/v3/text-to-speech`; songs on
  `suno/chirp-v6`) and the reference rule of STANDARDS 1. Higgsfield and the ElevenLabs connector are off
  (`disabled_services`): every one of their generating or credit-spending tools is refused;
- audio only after the script is released (G-SCRIPT 85+);
- a G-BUDGET PASS from the last 24 hours; a video call also needs step 9 closed (STANDARDS 10);
- a song run: no image or video call before the owner's G-HUMAN-SONG;
- a version is generated once (a retake is a new version, so attempts are counted). After 3 attempts the asset goes
  to the owner (G-HUMAN-ESCALATE); a prompt that fails 2 review loops goes to the Organic Director first (STANDARDS 9).

**The twin route (HeyGen, D-T4; STANDARDS 10).** Only `create_speech` and `create_video_from_avatar` generate; every
other HeyGen tool is refused (generation tools by the service, writes and account changes by the HeyGen tools hook);
reads (`list_*`, `get_*`, `lookup_*`, `bulk_*_statuses`) pass. Both calls need a card marked `twin_host` and a G-BUDGET
from the last 24 h with `--heygen CREDITS`. The flow:
1. voice asset: `pipeline.py asset <slug> <post> VO --type voice --tool mcp__HeyGen__create_speech`, then `pipeline.py
   prompt ... VO --file <the spoken script>` (it prints the sha256);
2. G-SCRIPT PASS with `--data '{"script_sha256": "<that sha256>"}'` (the text, whitespace-normalised);
3. `create_speech`: a `host.voices` id and exactly that text; no `engine`, `settings` or `forceRegenerate`;
4. `pipeline.py media ... VO@v<n> --id <the returned audio URL or asset id>`, then G-AUDIO PASS on `VO@v<n>`;
5. clip asset: `pipeline.py asset ... AROLL --type video_clip --shots S.. --tool mcp__HeyGen__create_video_from_avatar`,
   `pipeline.py prompt ... AROLL --file <note> --media <the same id>:audio`; step 9 closed;
6. `create_video_from_avatar`: a `host.looks` id, `aspectRatio` 9:16, `fit` cover for the landscape look, that audio
   only; no script, voice, motion prompt, burned captions, background, background removal, webm or 4k.
The gate trusts the registered audio id or URL (it can't see the bytes behind it): register only what `create_speech`
returned. `pipeline.py check-call --explain <tool> <input.json>` shows the answer without logging a call.

Cost preflights (`get_cost`, `estimate_only`) always pass. `GATE-SELFTEST` as a prompt is always blocked (proves the
gate is live). The Higgsfield credit-spending tools (presets, Marketing Studio, influencer builder, upscale, 3D,
sandbox and the rest) are refused with the service, whatever the test asset.

## Who decides what

- **Claude (orchestrator):** runs the steps, writes ledger records from reviewer JSON, never grades its own pictures.
- **Fresh reviewer agents:** every review, every retry; they get only the packet and must open every crop.
- **Organic Director:** the assembled piece (story, job, CTA), prompt-loop and Kling-fallback calls, the weekly memo
  that turns new failures into Failure Library entries.
- **Matan (batched once a day in `queue/`):** look bible per client or series, hook storyboards, voice casting once
  per voice, every song master (G-HUMAN-SONG), escalations, model exceptions, tests, and the final approval of every
  post on the hub.
- **Failing shots** (AI-VIDEO-PIPELINE step 11): retakes don't wait for Matan. Claude lists each failed asset version
  to him as an FYI in the run's summary (the version, the failed checks, the one change in the retake), and every
  failed check is written to `failure-log.csv`.
