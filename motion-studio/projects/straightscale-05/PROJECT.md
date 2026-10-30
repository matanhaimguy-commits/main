# StraightScale · reel 05 "Three things, one system"

One file that says what this job is, where it stands, and what was decided.

## Brief
- Client / product: StraightScale (our own agency, Instagram @straightscale_, Tirana). The StraightScale Client Engine,
  shown as one idea: the things an owner runs separately become one system built around the business.
- Goal of this piece and the single action: a loopable logo-reveal motion graphic that makes an owner feel the
  "three separate things" problem and lands the brand as the answer. CTA: follow ("Follow for the build, step by step.";
  v1 said "one step a week.", see decisions).
- Audience: owners of established service businesses (clinics, salons, studios, gyms, consultants, trades), 35-60,
  scrolling Reels between jobs. They already post, answer messages and chase follow-ups by hand, each on its own.
- Platform and formats: Instagram Reels. 9:16 master 1080x1920 at 60 fps, plus a native 4:5 1080x1350 re-layout
  (same timeline, own layout, not a crop). No 1:1 or 16:9 (not asked in this batch).
- Length: 14.0 s (v1 14.75 s), built to loop: frame 0 shows "Still running / your business" set, and the film's last
  0.44 s lift the end card out while those words rise back into that same frame.
- Language: English on screen. No English check lines needed.
- Voiceover: no (fixed by the owner's batch brief: on-screen text carries the message, readable with the sound off).
- Music: our own score from the VSCO 2 CE / VCSL sampler (CC0) through the Lemo-Opuscar sampler, plus effects
  synthesized in numpy. No paid generation of any kind (no Higgsfield, ElevenLabs or Atlas calls).
- Brand assets: `clients/straightscale/brand-kit.md` (only source of facts); real logo files copied from
  `projects/straightscale-03/assets/brand/` (logo-full.png, wordmark-white.png, symbol.png); Playfair Display and
  Montserrat self-hosted from `projects/straightscale-03/assets/fonts/` (OFL).
- References: refbank card `tt-rafaellfreitaas` (1.2M plays; three white dots spin, merge into a glowing ball that
  squashes, flies out, lands as the brand icon, slides left, wordmark revealed letter by letter).
- Proof and data shown: none. No numbers appear on screen.
- Rules: no prices, discounts, invented numbers, results, client names, reviews, testimonials, guarantees, deadlines,
  "answer within 1 hour", "we chase your leads", hype words, em dashes, real platform names or logos. Calm, direct,
  practical voice. The logo is never redrawn, recoloured or traced: reveals only mask, scale or fade the real files.
- Paid generation budget: zero.
- Deadline: this batch (20 Oct 2026).

## Status
Stage: delivered (v2, revision after the independent review of v1 failed it)
Current version: v2 (`deliver/v2/`); v1 kept in `deliver/v1/`
Next step: an independent review round on v2; a human listen on a phone speaker and on headphones; owner approval in
the hub.
Blockers / open questions: (1) G-MOTION-TEXT is a self-check in `docs/review_log.md`; a fresh reviewer and the
`pipeline.py record` entry (ledger under `clients/straightscale/runs/`, outside this job's write scope) are still
needed before the hub. (2) The CTA no longer promises a weekly series, but "the build" still points at build content
(The Build and One Step series in the content map are not live yet): the owner decides between this follow line and
the brand's one path (comment ANALIZA). (3) Nobody has listened yet.

## Defaults chosen (autopilot, no questions asked)
| Item | Default | Why |
|---|---|---|
| Engine | motion-studio canvas engine (`window.seek(t)`, `render.mjs`) | springs, squash and stretch and in-page subframe motion blur are native; the card recommends it; seekcheck and safezone tools are built for it |
| Frame rate | 60 fps, 8 subframes per frame (in-page average), plus speed-driven in-page samples (1 to 24 per subframe) for the dots and labels | the ball travels up to about 95 px per frame at 60 fps; 8 subframes keep its copies under 12 px apart; the small dots and 50 px words need more (v2) |
| Length | 14.0 s (v1 14.75 s) | brief asked 12-16 s; set by the reading-time rule for the CTA (3.43 s) |
| Hook | v2: "Still running / your business" set on frame 0, "on three / separate things?" in by 0.94 s, dots pop on notes at 0.06 / 0.20 / 0.34 s, labels 0.90-1.14 s | STANDARDS M5 (hook text on screen by 0.3 s) overrules motion-reel's 2 s; v1's slow build relied on brand recognition StraightScale does not have |
| Palette | charcoal ground, ivory type and dots, gold for one word and one rule, crimson for the ball, the real mark's own red and gold | brand kit; no gold text on ivory, no red text on charcoal |
| Type | Playfair Display 900 (question 98 px in v2, "One system."), Playfair 900 italic gold ("three"), Playfair 700 italic gold ("Built around your business."), Montserrat 600 (labels, CTA) | brand kit |
| Safe zones (9:16) | v2: text inside x 96-853, y 269-1248 | STANDARDS section 6 (top 269, bottom 672, right 227, sides 65) overrules the house zone (250/400/140) that v1 used |
| 4:5 margins | x 92-988, y 104-1270 | feed post, no overlay UI; same grid idea |
| Loudness | -14 LUFS integrated, true peak <= -1.5 dBTP measured on the encoded AAC | house rule |

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 2026-10-20 | v2: CTA line 2 "step by step." (was "one step a week.") | keep the brief's line and block posting until a weekly series exists; switch to "comment ANALIZA" | the independent review flagged the weekly promise; the series is not live (content map). Keeps the follow CTA and the stepped rule (one word per beat), drops the cadence. v1 keeps the original line if the owner prefers it later | autopilot (owner can revert) |
| 2026-10-20 | v2: hook text set on frame 0; the end card lifts out while the question rises back into frame 0 | words rising 0.0-0.3 s; accept a non-empty frame 0 without the loop rise | M5 needs the text by 0.3 s; this gives it at 0.0 s, a readable first frame, and a seamless loop | autopilot |
| 2026-10-20 | v2: STANDARDS section 6 safe zone; headline fitted to 757 px (98 px), spinner smaller (R0 170) and centred at (500, 980), lockup and end card up 70 px | keep 104 px and log the tool's upper-half flag as a false positive | the strict tool run passes with no exceptions; 98 px still reads large | autopilot |
| 2026-10-20 | v2: labels hang 10 px under their own dot and turn with it | v1's elliptical ring; a flattened ring | on the ring a label crossed its own dot mid-step (a dot sat on a word in the slow tail of each step) and needed vertical room the section 6 zone does not have | autopilot |
| 2026-10-20 | v2: speed-driven in-page motion blur for dots and labels ('lighter' average of 1 to 24 samples per subframe; `?sh=` = 1/(fps x sub)) | dip the label alpha in the fastest 70 ms | an exact smear keeps the word continuous and the reading-time rule unbroken | autopilot |
| 2026-10-20 | v2: the ball lands on the floor it took off from (y 980) with its bottom held there; the mark is revealed at centre, rises into the lockup row (6.8 s) and slides left (7.0 s) | reveal at the lockup row (v1) | v1 left the lower two-thirds empty for 2 s and its landing sank through a floor that was not there | autopilot |
| 2026-10-20 | v2: end card tightened (CTA 9.3 s, three steps from 10.65 s, exit 13.45 s, film 14.0 s); bed +3 dB under the question (enters mid-bow), end pad held | reviewer's 10.75 / 13.5 s | CTA reading time needs 3.43 s fully visible; the bowed sample's 0.5 s attack kept the bed quiet under the question | autopilot |
| 2026-10-20 | End card CTA moved to 9.7 s and enlarged to 56 px; the gold rule under "one step a week." grows one word per beat (11.25-12.75 s), each word hops as the rule reaches it, each step a harp note | a continuous rule; a longer static hold | pacing.py failed a 3.3 s frozen stretch at the end; the stepped rule is the line's own idea ("one step") and keeps something moving every 0.5 s | autopilot |
| 2026-10-20 | Exit at 14.25 s, film 14.75 s | 15.25 s | shorter loop, every block still passes the reading-time rule | autopilot |
| 2026-10-20 | Labels ride an elliptical ring (262 x 318 px) around the dots, triangle centre moved to y 1165 | circular ring; labels below each dot | a circular ring pushed "Follow-ups" past the right safe edge mid-step and the bottom label under the 1520 px line | autopilot |
| 2026-10-20 | Hero mark taken from the symbol region of `logo-full.png` (367 px native), not from `symbol.png` | `symbol.png` as the brief named | `symbol.png` is only 200 x 195 px of artwork and 2.6% wider than tall, so a 272 px hero would be upscaled 1.4x and would jump when it hands over to the lockup's mark; the same mark inside `logo-full.png` is 367 x 367 and matches `wordmark-white.png`'s mark proportions. Still the real file, only masked (source rectangle) and scaled | autopilot |
| 2026-10-20 | Lockup = `wordmark-white.png` letters (mask and fade, letter by letter) with the hi-res mark registered exactly over the file's own mark position | showing `wordmark-white.png` whole at the end | the file's own mark at 1.27x is visibly softer; the registered hi-res mark is the same artwork at the same place | autopilot |
| 2026-10-20 | The question leaves where the ball passes through it on the way up (each line lifts and parts around the ball) | a plain fade-out | every reaction has a visible cause (onetake P5) | autopilot |
| 2026-10-20 | Concept A "Three things, one system" (the batch brief's concept), canvas engine | B: three separate phone screens fold into one; C: three threads braid into the S channel | see `docs/treatment.md` §2 | autopilot |

## Approvals
| Date | What | By | Notes |
|---|---|---|---|
| | v1 cut | failed independent review (2 major) | superseded by v2 |
| | v2 cut | pending (independent review, then the owner in the hub) | nothing is posted without approval |

## Log
- 2026-10-20 · setup, read skill, house rules, knowledge guides, reference card, brand kit · project scaffolded, assets copied
- 2026-10-20 · `refbank.py check --client straightscale --category logo-reveal --devices morph,mask-reveal,word-by-word` · ok, no repeats
- 2026-10-20 · styleframes round (out/sf1.png, sf2.png, sf4x5_1.png) · crowding under the question fixed, ring made elliptical, step spring tightened
- 2026-10-20 · score and effects (audio/score.py) · first pass, ticks raised 10 dB after the per-event report
- 2026-10-20 · draft 1 (30 fps) · review round 1 logged; fixes: end-card hold, CTA size, ring and safe zones
- 2026-10-20 · draft 2 (30 fps) · review round 2 logged
- 2026-10-20 · final render 60 fps / 8 subframes, 9:16 and 4:5, master and mux · deliver/v1
- 2026-10-20 · independent review of v1: FAIL (M5 hook timing, STANDARDS section 6 safe zone; 5 minors)
- 2026-10-20 · v2 source changes (hook on frame 0 and loop rise, section 6 layout, labels under dots, in-page motion blur, landing floor and rise, end card, CTA, bed and pad levels) · styleframes, draft 1 (round 4), draft 2 and final (round 5)
- 2026-10-20 · final render 60 fps / 8 subframes in 3 parallel segments per format, joined, mastered, muxed · deliver/v2
