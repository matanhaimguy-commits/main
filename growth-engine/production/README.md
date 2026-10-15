# Production: how every post gets made, checked and let through

Organic Growth OS (`../ORGANIC-OS.md`) decides **what** to post and why. This folder decides **how** every image, carousel
and video is made, and makes the checks impossible to skip.

| File | What it is |
|---|---|
| `AI-VIDEO-PIPELINE.md` | The owner's spec: 16 steps (0 to 15) with gates, per-format table, house rules, the 18 inconsistencies (section 5). Verbatim. |
| `VISUAL-QA.md` | The owner's spec: Shot Specs, gate map, prompt cards, the three fresh reviewers, storyboards, the Failure Library, enforcement. Verbatim. |
| `STANDARDS.md` + `standards.json` | **The one numbers file.** Every model, duration, word budget, loudness, safe zone and pass rule, with the 18 issues resolved and the open re-tests. Prose in the .md, machine values in the .json (the gate reads it). |
| `STORY-FORMATS.md` | Story formats for organic posts: POV day in the buyer's life, two days, the problem as a villain, song, podcast, drama; animation styles; how they fit the weekly mix and the budget. |
| `schemas/shot-spec.schema.yaml` | The Shot Spec schema (VISUAL-QA section 2). |
| `failure-library.md` | FL-01 to FL-12 and how new patterns get added. `failure-log.csv` is the raw log every FAIL writes. |
| `install-gate.sh` | Installs the generation gate for a session rooted above the repo. |
| `queue/<date>.md` | The daily human approval queue (`pipeline.py queue --write`). |

Tools and agents:

| Where | What |
|---|---|
| `growth-engine/tools/pipeline.py` | Runs (one folder per post), the gate ledger, spec lint, reviewer records, budget gate, human checkpoints, the queue, and `check-call` (the gate logic). |
| `growth-engine/tools/vqa_crops.py` | Review packets: full image, 3x3 tiles at 2x, region crops, storyboard panels, 200 px thumbnail, frame contact sheets, H3 drift, loudness. |
| `.claude/hooks/generation_gate.py` + `.claude/settings.json` | The PreToolUse hook: blocks Higgsfield and ElevenLabs generation unless the gates pass. Fails closed. |
| `.claude/agents/visual-planner.md` | Writes the Shot Specs (step 6). |
| `.claude/agents/prompt-reviewer.md` | Fresh reviewer: Shot Specs (G-SPEC) and prompts (G-PROMPT-IMG, G-PROMPT-VID), P1 to P12. |
| `.claude/agents/visual-reviewer.md` | Fresh reviewer: stills, sheets, storyboards, slides (V1 to V26), continuity and carousel sets. |
| `.claude/agents/take-reviewer.md` | Fresh reviewer: video takes (T1 to T9), motion renders (M1 to M7), final cuts (F1 to F8). |
| `growth-engine/adapters/*-organic.md` | How each production skill runs for organic posts (CTA ladder, no offer, B2B hooks, AI label, organic LEARN). |

## One post, start to finish

```
Post Card (cards/<yyyy-mm>-W<n>/<post_id>.yaml)          organic.py card-check, route
  → pipeline.py init <slug> <post_id> --format F --card ...  runs/<post_id>/ledger.json
  → steps 0-3: brief, idea + THE PICTURE, hook (Hook Lab), script (Script Lab)    G-BRIEF G-IDEA G-HOOK G-SCRIPT(85+)
  → steps 4-5: audio master + timeline (video only)                                G-AUDIO-MASTER G-TIMELINE
  → step 6: visual-planner writes shots/*.spec.yaml → spec-check → prompt-reviewer   G-SPEC per shot
  → step 7: look bible (sheets, prop sheets) on the client's LIB run                 G-VIS-SHEET, G-HUMAN-LOOK once
  → step 8: storyboards → visual-reviewer per panel + continuity set                 G-VIS-BOARD, G-CONTINUITY, hook board → owner
  → step 9: pipeline.py budget                                                       G-BUDGET (cap, live balance, +25%)
  → step 10: generate (the hook checks every call)                                   G-PROMPT-* per prompt
  → step 11: vqa_crops.py → visual/take reviewer per asset                           G-VIS*, G-TAKE, G-MOTION-FRAMES
  → steps 12-13: edit → final review + Director                                      G-FINAL, G-DIRECTOR
  → step 14: hub draft → owner approves on the Content page                          G-HUMAN-FINAL
  → step 15: analyst at 72 h and 7 d → learnings, Hook Library, lessons             G-LEARN
```

Each family skips what it doesn't have (standards.json `families`): carousels and images skip audio, timeline,
storyboards and edit; the tier C quote reel skips the storyboard (one silent shot); real footage skips the look
bible, storyboards, credits and generation.

## What the gate checks before a generation call runs

For the exact prompt text (whitespace aside) it finds the registered asset version, then requires:
- every Shot Spec it serves is linted and has a G-SPEC PASS **for its current file**;
- a G-PROMPT PASS for **this exact prompt**; the references in the call are the reviewed ones, same order, same roles;
- every reference is a registered asset whose own review passed; sheets come from an owner-approved look bible;
- talking or multi-shot video: image 1 is a storyboard with G-VIS-BOARD and G-CONTINUITY PASS (hook boards also
  need the owner); audio references passed their transcript check;
- the model rules (standards.json): model per asset type, H3 at 2K, 9:16, `declined_preset_id`, 5 to 15 s; Kling only
  with G-FALLBACK; other video models only with an owner G-EXCEPTION; voices and music only on ElevenLabs;
- audio only after the script is released (G-SCRIPT 85+);
- a G-BUDGET PASS from the last 24 hours;
- a version is generated once (a retake is a new version, so attempts are counted), and after 3 attempts the owner
  or Director decides.
Cost preflights (`get_cost`, `estimate_only`) always pass. `GATE-SELFTEST` as a prompt is always blocked (proves the
gate is live). Other credit-spending generators (presets, Marketing Studio, influencer builder) need an owner-approved
test asset.

## Who decides what

- **Claude (orchestrator):** runs the steps, writes ledger records from reviewer JSON, never grades its own pictures.
- **Fresh reviewer agents:** every review, every retry; they get only the packet and must open every crop.
- **Organic Director:** the assembled piece (story, job, CTA), prompt-loop and Kling-fallback calls, the weekly memo
  that turns new failures into Failure Library entries.
- **Matan (batched once a day in `queue/`):** look bible per client or series, hook storyboards, voice casting once
  per voice, escalations, model exceptions, tests, and the final approval of every post on the hub.
