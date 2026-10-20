# StraightScale · 06 "The 108-hour week"

Film 3 of a batch of three viral motion-graphics reels for StraightScale's own Instagram (@straightscale_, Tirana),
made in autopilot mode. One file that says what this job is, where it stands, and what was decided.

## Brief
- Client / product: StraightScale (our own agency). Offer facts only from `clients/straightscale/brand-kit.md`.
- Goal of this piece and the single action (CTA): show an owner how many hours a week their business is closed
  while clients still write, then send them to the one path: comment ANALIZA, the booking button for the free
  45-minute analysis comes in the DM.
- Audience: owners of established Albanian service businesses, 35-60 (clinics, salons, studios, gyms, consultants,
  agencies, trades), who work in the business all day and lose messages that arrive after hours.
- Platform and formats: Instagram Reels 9:16 master 1080x1920, plus a native 4:5 1080x1350 re-layout (same code,
  its own layout table; not a crop). 60 fps.
- Length: 24.0 s (brief: 18-24 s).
- Language: English on screen. No English check lines needed.
- Voiceover: no (fixed decision in the brief). On-screen text carries the message; it reads with the sound off.
- Music: our own score from real CC0 instrument samples (VSCO 2 CE + VCSL through the Lemo-Opuscar sampler):
  felt-softened upright piano, cello/viola/violin sections, harp, glockenspiel. Effects synthesized in code.
- Brand assets: logo files `assets/brand/` copied from `projects/straightscale-03/assets/brand/` (wordmark-white.png
  used on charcoal; never redrawn), fonts Playfair Display + Montserrat (OFL) from `projects/straightscale-03/assets/fonts/`.
- Reference: `refbank/cards/tt-foil-finance.md` (1.5M plays, data-infographic; step chart + date clock).
- Proof and data shown on screen: see "Numbers on screen" below. No results, clients, reviews or prices.
- Rules: no prices, discounts, invented numbers, results, client names, reviews, testimonials, guarantees, deadlines,
  "we answer within 1 hour", "we chase your leads", hype words, em dashes, real platform names or logos.
- Paid generation: none (no Higgsfield, ElevenLabs or Atlas calls). Spend: 0 credits.
- Deadline: same session.

## Numbers on screen (source and date for each)
| On screen | Where it comes from | Checked |
|---|---|---|
| "Example: open 09:00 to 19:00, Monday to Saturday." | A stated example schedule, labelled "Example" on screen (brief, 20 Oct 2026) | 2026-10-20 |
| 168 (hours in a week) | 7 x 24 | arithmetic |
| 60 (open) | 10 h x 6 days, from the stated example | arithmetic |
| 108 (closed) | 168 - 60; the chart's closed periods sum to 5 x 14 h (Mon-Fri 19:00 to 09:00) + 38 h (Sat 19:00 to Mon 09:00) = 108 | arithmetic, and the page computes it from the open-hours table |
| The day-and-time counter (Mon 09:00 to Mon 09:00) and the riding "N h" value | the same example week, computed per frame by `cum(h)` in `film/index.html` | seekcheck |
| Axis labels 0, 40, 80, 120 (v2; v1 labelled every 20 up to 140) | chart scale only (not a claim) | |
| "free 45-minute analysis", "Comment ANALIZA", "booking button ... in the DM" | `clients/straightscale/brand-kit.md` (one offer, one path) | 2026-10-20 |
| "64%" | not shown (allowed only with its arithmetic; left out to keep the film to one number) | |

## Status
Stage: delivered (v2, after the independent review `docs/review_independent_r1.md`: PASS with 11 minor findings)
Current version: deliver/v2 (v1 kept unchanged)
Next step: a person listens to the mix on a phone and approves the cut in the hub; then the ledger entry (below).
Blockers / open questions: none for the film. Not done here by instruction: refbank ledger entry, commit/push,
hub upload (a person approves).

## Defaults chosen (autopilot)
| Question | Default | Why |
|---|---|---|
| Engine | HyperFrames 0.8.150, one composition per format, one paused GSAP timeline whose single clock tween calls a pure `frame(t)` | the brief prefers HyperFrames for charts and type; one clock function keeps chart, type and sound cues in sync and seek-safe |
| Tempo / clock | 90 BPM, one day = one 2/4 bar (1.333 s), 18 hours per second; every closing (19:00) lands on a downbeat | the music grid is the film's clock, so pulses, steps and ticks never drift |
| Ending of the crawl | the last 14 hours (Sun 19:00 to Mon 09:00) decelerate onto a downbeat (power ease-out, p = 1.714, matching the 18 h/s entry speed) | the counter slows into the 108 like a ritardando |
| Palette | charcoal ground, ivory type, one accent: mark-gold #DD9A10 (the closed hours, the line's climbs, CLOSED, the answers, ANALIZA); red only in the real logo; secondary text grey #9B958D = brand marble at 60 % over charcoal (derived in code, not a new colour) | brand kit; gold on charcoal passes contrast; no red text on charcoal |
| Type | Playfair Display 700 (headlines, "closed" in 700 italic gold), Montserrat 500-800 (note, labels, figures, clock) | brand kit; sizes: headline 80 px, body >= 44 px, clock 116 px |
| Safe zones | 9:16: no text or logo in the top 14 %, bottom 20 %, right 140 px; 4:5: 60 px margin | brief and house rules; checked every 0.05 s (`tools/textcheck.mjs`) |
| Length | 24.0 s | the reading-time rule (chars / 15 + 1.5 s) for the CTA body needs 5.23 s after it is fully visible |
| Music | sampler score, no paid music | brief |

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 2026-10-20 | v2: fixed all eleven minor review findings that were cheap and safe (see `deliver/v2/CHANGELOG.md`); kept the brief's headline wording "clients still write." | "while clients still message you" (reviewer's optional suggestion) | the headline is fixed copy in the batch brief; flagged for the owner instead of changed | agent |
| 2026-10-20 | Answered bubbles turn gold and their dots become a check | 1.5-2x larger badges (would collide between the two rows) | the answer reads at 360 px wide; no new element | agent |
| 2026-10-20 | The square's hop to the logo goes round the right of the body copy and in under it, starting a quarter beat earlier (18.72 s), smoothstep on a cubic Bezier | an arc to the left (would cross ANALIZA) | never covers a letter; peak speed stays under the 80 px/frame limit | agent |
| 2026-10-20 | Grey kept, documented as marble 60 % over charcoal and computed from the two kit colours in code | a new kit entry (not editable from a film project) | identical pixels; no new colour | agent |
| 2026-10-20 | Gold rule draws under ANALIZA at 21.2 s | static end hold; a blinking caret | pacing.py found a 4.25 s frozen end; the rule is a last cue to the one action and leaves only 2.3 s still | agent |
| 2026-10-20 | Strings breathe out 0.12 s before the landing; landing chord and pulse raised; the rest before the CTA quieter | louder landing only | momentary loudness showed the landing (-10.3) quieter than its approach (-9.1); now -9.2 vs -14.2 | agent |
| 2026-10-20 | CTA moved half a beat later, film 24.0 s | shorter copy (not allowed: copy fixed) | reading time of the system line and the CTA body | agent |
| 2026-10-20 | "108" flies from the tip of the line into the sentence "Closed 108." (drops down the right side, then slides left) | a straight diagonal (crossed the other lines) | continuity: the number the viewer watched climb is the number in the sentence | agent |
| 2026-10-20 | The gold tip square becomes the typing caret for ANALIZA, then lands exactly on the gold square of the real logo file, which is revealed by a clip growing out of it | logo fade-in | one survivor from the first frame to the last; the logo itself is only masked, never redrawn or recoloured | agent |
| 2026-10-20 | Message bubbles live in a lane above the plot, in the dark columns; answered with a gold check square during "A system answers..." while the open-hour light sweeps over the closed hours | bubbles attached to the line (collided with the label and each other) | readable at phone size, no counts, no names | agent |
| 2026-10-20 | Y axis rescales twice (40 -> 80 on Wednesday's closing, 80 -> 140 on Friday's), so the weekend climb reads as a cliff in the final chart | fixed 0-120 axis (first steps tiny); rescale every night (weekend looked small) | keeps the reference's auto-scaling grammar without hiding the story's shape | agent |
| 2026-10-20 | Concept "The 108-hour week" (step chart + day-and-time counter) | see docs/treatment.md section 2 | given by the batch brief; passes `refbank.py check` | brief |

## Approvals
| Date | What | By | Notes |
|---|---|---|---|
| | cut v1 | superseded by v2 | |
| | cut v2 | pending (hub) | nobody has listened yet; a person approves in the hub |

## Log
- 2026-10-20 08:38 · project set up, HyperFrames init, GSAP vendored, fonts and real logo files copied · ok
- 2026-10-20 08:46 · charcoal ground textures generated (`tools/make_bg.py`) · ok
- 2026-10-20 08:55 · composition built; first styleframes (out/sf1_sheet.jpg) · day roll unreadable, mask leaks, CTA collision, crowded bubbles
- 2026-10-20 09:02 · fixes; HyperFrames check passes (caption band bottom 20 %), textcheck and seekcheck pass · ok
- 2026-10-20 09:07 · draft 1 (HyperFrames, 30 fps), review round 1 · see docs/review_log.md
- 2026-10-20 09:12 · score v1-v3 (sampler), master -14.0 LUFS, TP -3.2 dBTP · ok
- 2026-10-20 09:16 · draft 2 of both formats with audio, review round 2 · ok
- 2026-10-20 09:18 · delivery renders 60 fps, mux, deliver/v1 · see CHANGELOG
- 2026-10-20 09:42 · independent review round 1: PASS, 11 minor findings (`docs/review_independent_r1.md`)
- 2026-10-20 09:50 · v2 fixes in `film/index.html` and `audio/score.py` (v1 sources kept in `versions/v1/`); checks pass
- 2026-10-20 10:00 · v2 delivery renders 60 fps, mix rebuilt, deliver/v2 · see deliver/v2/CHANGELOG.md
- Not done by instruction: `refbank.py log` (ledger), commit and push, hub upload. Suggested ledger line:
  `python3 motion-studio/refbank/tools/refbank.py log --client straightscale --project straightscale-06 --refs tt-foil-finance --category data-infographic --devices chart-grow,counter-ticker,timeline-progression,big-number --hook text-headline --palette dark --camera "locked, no camera; chart folds onto its baseline" --engine hyperframes --concept "The 108-hour week: a step chart climbs through the closed hours of one example week while a day-and-time counter ticks to 108" --language en`
