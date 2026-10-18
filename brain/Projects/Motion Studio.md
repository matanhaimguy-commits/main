---
type: project
updated: 2026-10-18
tags: [project, motion-studio, video, motion-reel, hyperframes, refbank]
---

# Motion Studio

The code-rendered video studio in `motion-studio/`. Every video job (reels, launch videos, explainers, ads, motion
graphics, B-roll, any client video) runs through the `motion-reel` skill, from one prompt to delivered files. For
organic posts, motion reels are one format of the [[Growth Engine]] and pass the gates of the [[Production layer]].
Back to [[00 Index]].

Source: CLAUDE.md (repo root), motion-studio/CLAUDE.md, .claude/skills/motion-reel/SKILL.md

## Read order

1. `motion-studio/HANDOFF.md`: everything the studio built, proved, measured and learned (written 14 Oct 2026).
2. `.claude/skills/motion-reel/SKILL.md`: the A-to-Z workflow (stages 0 to 13).
3. `motion-studio/CLAUDE.md`: house rules for every engine.
4. `motion-studio/refbank/README.md`: the reference bank.
5. `motion-studio/knowledge/README.md`: index of the guides (our-pipeline, hyperframes, lemo-opuscar,
   onetake-principles, claude-animation-base, gbro-collage-broll).
6. `motion-studio/projects/straightscale-03/`: the best finished project, worth reading end to end.

Source: motion-studio/HANDOFF.md section 0, motion-studio/knowledge/README.md

## The motion-reel workflow

Modes: autopilot (default: one round of questions, then decide at each gate and log it in `PROJECT.md`) or guided
(pause after concepts, script and voice, styleframes, draft cut).

| Stage | What | Output or check |
|---|---|---|
| 0 Setup | `bash motion-studio/setup.sh` (add `lemo`, `voice`, `music` tiers); copy `templates/project` to `projects/<client>-<piece>`; read house rules | Containers are wiped, so every session |
| 1 Intake | One round of questions, then defaults | Brief in `PROJECT.md` |
| 2 Research and assets | Brand capture, facts table with sources | Every on-screen number has a source and a date |
| 3 References and art direction | `refbank.py pick` / `search` | At least 2 references, none already used by this client |
| 4 Three concepts | Different central visual ideas; one picked | `refbank.py check` passes |
| 5 Script and voice | Script, ElevenLabs voice, word timings | Transcript matches the script |
| 6 Treatment and beat sheet | Beats on the voice clock | Beat checks |
| 7 Styleframes | 3 to 4 key frames | Look proven before the film |
| 8 Build | Pick the engine by the look | `seekcheck` and `safezone` pass |
| 9 Sound | Music, effects from the film's own event times, mix | `audio_qa.py` |
| 10 Review | At least 3 logged rounds in `docs/review_log.md` | Every rubric axis 8+, all checks pass, or the blemish is logged and told |
| 11 Render and master | Draft, then final in parallel segments | Frame count, seams, loudness |
| 12 Deliver | `deliver/vN/` (never overwrite): 9:16 master, native re-layouts, poster, SRT, `CREDITS.md`, changelog | Then `refbank.py log` and commit |
| 13 Revisions | Changes in the source, next version to `deliver/vN+1/` | Re-run checks on what changed |

Source: .claude/skills/motion-reel/SKILL.md, motion-studio/HANDOFF.md section 2

## Engines

| Look or job | Engine |
|---|---|
| Kinetic type, UI and product demos, launch and brand reels, data, captions (most reels) | HyperFrames (HTML plus GSAP, one paused timeline, a registry of about 447 items). Default engine and master timeline |
| Custom drawing, generative or physical motion, macro worlds, true motion blur | motion-studio canvas engine (`window.seek(t)` plus `render.mjs`). All three early StraightScale reels used it |
| Painterly or illustrated looks | Lemo-Opuscar style engines, ported to a 9:16 page |
| A character who acts (mascot, host, reaction) | Claude Animation Base (p5.brush); the client's own character, never Anthropic's mascot |
| Abstract-line B-roll | Collage method (route C is code-only and free) |
| Photoreal imagery, product 3D, footage | Client footage first; paid generation only with approved spend |

Measured speeds here (4 CPUs, no GPU): HyperFrames about 3.3 s per second of video; canvas engine a 50 s film in
about 8 to 15 minutes; a full reel is about 1.5 to 2 hours of agent time.

Source: .claude/skills/motion-reel/SKILL.md stage 8, motion-studio/HANDOFF.md sections 2 and 9.1, motion-studio/knowledge/README.md (speeds)

## House rules (short)

- Render contract: every film is a pure function of time; no CSS transitions, timers, `requestAnimationFrame` in
  render mode or `Math.random`. `tools/seekcheck.mjs` must pass. Self-host every font and script.
- Banned looks include: centred title on a gradient, everything fading in, grey-bar placeholder cards, redrawn
  logos, fake UI or invented screens. One display font, one UI font, one accent colour, one signature device.
- Content: real brand material only; no invented numbers, reviews, clients or deadlines; always ask whether the film
  has a voiceover; client-language copy is flagged for a native speaker.
- Sound: master to -14 LUFS; we can't listen, so measure with `tools/audio_qa.py` and ask a human to listen.
- Loop before showing anything: contact sheet at phone size, 9-axis score, automatic checks, fix the 3 worst problems.
- API keys live in `motion-studio/.env` (gitignored). Never paste keys into prompts.

For organic Growth Engine posts, STANDARDS.md overrides some house numbers: the reels safe zone (STANDARDS 6, not the
house 250/400/140 px zone), music level under the voice, frame rate, the AI label, and the words come from Hook Lab
and Script Lab. See `growth-engine/adapters/motion-reel-organic.md` section 7 and [[Production layer]].

Source: motion-studio/CLAUDE.md, growth-engine/adapters/motion-reel-organic.md, growth-engine/production/STANDARDS.md section 12

## Motion reels inside the Growth Engine

- Format `reel_motion`: tier C, family `motion`, 0 to 30 Higgsfield credits, always voiced (owner rule, 15 Oct 2026),
  so the AI label is on.
- Project folder for an organic post: `motion-studio/projects/<slug>-<post_id>/`, plus a pipeline run
  (`pipeline.py init <slug> <post_id> --format reel_motion --card <card>`).
- Extra gates: G-MOTION-TEXT (a fresh prompt-reviewer checks the code's text constants before any render),
  G-HUMAN-HOOKBOARD on the hook styleframe, G-MOTION-FRAMES (fresh take-reviewer, M1 to M7), G-FINAL.
- `motion-video-director` is retired for our work; motion pieces use motion-reel.

Source: growth-engine/config/organic.json (formats.reel_motion), growth-engine/adapters/motion-reel-organic.md sections 1 and 8, growth-engine/production/STANDARDS.md section 9

## Reference bank

- `motion-studio/refbank/`: proven viral reels broken down into reusable grammar (hook, timed beat map, signature
  device, measured pacing, palette and type, how to build it here, business translations), plus a per-client usage
  ledger so a client's films never repeat.
- As of 14 Oct 2026: 92 cards (81 viral social reels, 75 TikTok and 6 Instagram, median 8.1M plays; 11 onetake craft
  films, study only), 17 categories.
- Third-party reels are for study only: take structure, timing, devices and sound logic, never their pixels, words,
  characters, music or marks.
- Commands (`python3 motion-studio/refbank/tools/refbank.py ...`): `pick --client X` (fresh references), `search`,
  `check` (before committing to a concept), `log` (after delivery, required), `history`, `stats`, `build`.
- Anti-repetition rule enforced by `pick` and `check`: no reference the client already used, not the previous film's
  category, no signature device from its last 3 films, at most one device shared with the last film.
- New references come through the Apify connector (Instagram, TikTok and Apify's own API host are blocked in the
  containers). Recipe: HANDOFF.md section 7.4 and `refbank/tools/CARD_BRIEF.md`.
- Ledger for StraightScale (from `refbank.py history`): 12 Oct `straightscale` (kinetic-type, shape-wipe), 13 Oct
  `straightscale-02` (spectacle-world, one-take camera), 14 Oct `straightscale-03` (kinetic-type, focus brackets),
  15 Oct `straightscale-2026-w43-3-reel-v2` (brand-ad, screen-in-frame).

Source: motion-studio/refbank/README.md, motion-studio/refbank/ledger.json via refbank.py history

## Where projects live

- One folder per client deliverable: `motion-studio/projects/<client>-<piece>/`, started from `templates/project/`.
  Never let two sessions build the same piece in parallel.
- Existing: `straightscale` (reel 01 "Marketing copë-copë"), `straightscale-02` ("Klientët që kthehen"),
  `straightscale-03` ("Qartësia", Albanian and an English cut; the one the user called perfect),
  `straightscale-2026-w43-3-reel` (24 s kinetic type, no voice: the user rejected it as boring, slow, too much text,
  no voiceover) and `straightscale-2026-w43-3-reel-v2` ("The 22:47 race", 60 s, made through ads-machine, Hook Lab
  and Script Lab, rendered in the Higgsfield sandbox). Content history: [[StraightScale content log]].
- The five reference repos (HyperFrames, onetake, gbro-collage-broll, claude-animation-base, lemo-opuscar) live in
  `references/`, gitignored, fetched with `bash references/fetch.sh`.

Source: .claude/skills/motion-reel/SKILL.md stage 0, motion-studio/HANDOFF.md section 1, motion-studio/projects/straightscale-2026-w43-3-reel-v2/PROJECT.md, CLAUDE.md (repo root)

## The automated reel machine (undecided)

`motion-studio/HANDOFF.md` is written for a session that builds a machine making reels on its own. Section 13 lists
three researched options (A: a Claude Code Routine fired by API, marked recommended; B: our own worker; C: GitHub
Actions) and says "pick one". No choice is recorded. Still to build: the job-brief parser and "never ask" rule,
auto-setup on session start, a delivery step, the human thumbs-up gate before posting, a weekly refbank refresh.

Source: motion-studio/HANDOFF.md section 13

## Open or unknown

- HANDOFF.md (14 Oct) names the default branch as `claude/discovery-engine-v16-ms5mxf`; the daily run (DAILY.md)
  commits to `claude/ig-fb-chatbot-automation-zk8w44`, which is the branch checked out today. Which branch is
  canonical for motion work is not stated.
- Whether `straightscale-2026-w43-3-reel-v2` was approved and posted is not in the project files I read; see
  [[StraightScale content log]].

Source: motion-studio/HANDOFF.md (intro), growth-engine/DAILY.md (intro), git branch --show-current

## Related

[[Growth Engine]] · [[Production layer]] · [[StraightScale]] · [[Standing rules]] · [[How Claude uses this brain]]
