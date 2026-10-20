# StraightScale · Film 04 "One message, all the way" (beat-sync marble run)

One file that says what this job is, where it stands, and what was decided. Update it at every stage.

## Brief
- Request (owner, 20 Oct 2026, relayed by the batch workflow): "generate for me 3 viral motion graphics for
  straightscale in english based on winning formats pacing animations sounds etc". This is film 1 of the batch of
  three (films 2 and 3 are other sessions in `straightscale-05`, `straightscale-06`). Autopilot: no questions asked;
  the workflow fixed the decisions below.
- Client / product: StraightScale (our own agency, Instagram @straightscale_, Tirana). Facts only from
  `clients/straightscale/brand-kit.md`.
- Goal of this piece and the single action (CTA): make an owner feel, in 25 seconds, what one unanswered message
  costs, and that a system answers every step. Action: share it ("Send this to an owner who loses clients after the
  first message."). The post caption carries the one path (comment ANALIZA, the booking button comes in the DM):
  `deliver/v2/post-caption.txt`; it is not on screen because the brief for this film names the share ask as the end
  line (the independent review asked for it in the caption, or for the owner to confirm a share-only post).
- Audience: owners of established Albanian service businesses (clinics, salons, studios, gyms, consultants, trades),
  35-60, scrolling Instagram/Facebook Reels; they get clients from referrals and Instagram but not predictably, and
  messages go unanswered while they work (brand-kit avatar).
- Platform and formats: 9:16 master 1080x1920 (Reels) and a 4:5 1080x1350 native re-layout (feed). No 1:1 / 16:9
  (not asked). 60 fps (fast ball motion), 4 subframes of motion blur.
- Length: 25.0 s, a seamless loop (frame 25.0 is frame 0). v1 was 27.0 s; v2 cut 2 s of quiet end (review r1).
- Language: English on screen. No English check lines needed.
- Voiceover: NO (fixed by the workflow): the on-screen text carries the message, sound-off readable; music and
  effects only.
- Music: our own score from the VSCO 2 CE / VCSL sampler (CC0), built from the film's impact times
  (`audio/score.py`); foley synthesized (`~/lemo/core/audio/sfx.py`). No paid generation of any kind.
- Brand assets: real logo files copied from `projects/straightscale-03/assets/brand/` (logo-full.png used; v2 shows it
  only in the end frame, behind a marble hatch that opens when the ball is home);
  Playfair Display + Montserrat (OFL) self-hosted from `projects/straightscale-03/assets/fonts/`. Colours from the
  brand kit: mark-red #BE0F18, mark-gold #DD9A10, crimson #B31217, ivory #F8F6EF, marble #EDE4D6, charcoal #1F1F1F.
- References: `refbank/cards/ig-satisfy3dverse.md` (109M plays; a glossy ball bounces down a pale wall of sound
  objects, follow-cam, every hit a note, seamless loop). Take the grammar, leave the content (see treatment §1).
- Proof and data shown: none. No numbers, results, clients, reviews, prices, deadlines or guarantees on screen. The
  station names are the steps of a client's path; the sub-labels are Build items from the brand kit (instant-answer
  and follow-up automations, rebooking).
- Rules: no em dashes, no hype words, no "1 hour", no lead chasing, no platform names or logos, no gold text on ivory,
  no red text on charcoal, real logo only (never redrawn or recoloured; it is only scaled and composited).
- Paid generation budget: none used (0 credits, 0 minutes). Nothing to approve.
- Deadline: same session.

## Defaults chosen (autopilot)
| Item | Default | Why |
|---|---|---|
| Engine | motion-studio canvas engine (`index.html`, `window.seek(t)`, `render.mjs`) | deterministic precomputed physics path, springs, true subframe motion blur; the look is drawn shapes, not DOM layout |
| Frame rate | 60 fps, 4 subframes per frame | the ball reaches ~2,000 px/s; 30 fps would strobe |
| Gravity / ball | g = 6000 px/s², radius 34 px | bounces of 100-170 px between beats read lively at 1.18x |
| Tempo | 120 BPM, beat grid A from 0.0 s, grid B from the rebuilt plate's lock at 7.0 s | every contact sits on a beat or an eighth/sixteenth of it |
| Working zoom | 1.18x | objects fill the frame like the reference's close follow-cam |
| Loudness | -14 LUFS integrated, -2.0 dBTP before AAC, <= -1.5 dBTP after | house standard with margin for the encoder; v2 adds a linear trim after loudnorm so ebur128 reads -14.0 |
| Reading time | 0.25 s per word + 0.5 s, fully in to the start of the exit | the rule the independent review applies; the Lemo-Opuscar rule (letters/15 + 1.5 s) is printed as advice |
| Caption band | opaque behind the glyph rows (9:16 to y 549, 4:5 to y 329), fading below the type only | review r1 finding 1: nothing may ghost through a caption |
| 4:5 | same world and timeline, own camera anchor, caption band, map zoom and rebuild framing | native re-layout, not a crop |

## Status
Stage: delivered (v2, revision after the independent review r1 FAILED v1)
Current version: v2 (`deliver/v2/`); v1 kept untouched in `deliver/v1/`
Next step: independent re-review of v2; a human listens on a phone (nobody has listened: we measure only); the owner
approves in the hub.
Blockers / open questions: none blocking. The post caption must carry the ANALIZA path (`deliver/v2/post-caption.txt`)
unless the owner confirms a share-only post. `captions.srt` is a reference of the burned-in lines: do not upload it as
closed captions (every line would appear twice).

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 2026-10-20 | v2: the logo lives behind a marble hatch above the cradle: it opens when the ball lands home (21.06 s) and closes as the flipper arms (24.15 s), so it never travels under a caption and the hook frame has no logo | (a) move the logo on the wall; (b) only an opaque band; a screen-space lockup | any logo on the wall above the cradle must cross the top band when the follow cam descends; (b) alone would still fog it in the fade; a lockup would sit on top of the world. The hatch is a cause-and-effect mechanism that fits the machine and makes the brand the payoff | Claude (review r1, finding 1) |
| 2026-10-20 | v2: the caption band is fully opaque behind the glyph rows, its colour follows the light, and its windows open 0.4 s before a caption and close after the last line has gone | v1's 90-94 % haze | a 6-10 % ghost of whatever passes under the type; checked by `tools/ghostcheck.mjs` (0 levels in both formats) | Claude (review r1, finding 1) |
| 2026-10-20 | v2: loop 25 s; the ask rises in the flight home and holds 3.6 s once fully in; the path stays lit through the ask with light pulses on the taps; slow push into the hook's close-up | keep 27 s and add motion | 12 words need 3.5 s under the house rule; a shorter loop replays sooner; longest quiet run 4.42 s -> 1.67 s | Claude (review r1, finding 2) |
| 2026-10-20 | v2: pass 2 shot closer (z 1.42) with a swinging follow leaning toward Reply; frame 0 a close shot on the ball and flipper (z 1.32) | start the replay at Comment | the replay's phrase has to repeat musically; the picture does not | Claude (review r1, findings 3 and 4) |
| 2026-10-20 | v2: the dark is inside the shaft (perspective edges, drifting rings, warm falloff, last glint, camera still sinking) | a vignette only | the review read v1's dark as a title card | Claude (review r1, finding 5) |
| 2026-10-20 | v2 sound: room tone about -50 dBFS in the silence; stations +2 dB and pegs -1 dB; presence +3.5 dB at 3.8 kHz; hatch, flight-home and arming foley | digital zero | the review (finding 6); audio_qa still flags 5-6 s as a dropout because the rest is 30+ dB under the median, by design | Claude |
| 2026-10-20 | v2: marble veins as stretched contour lines with a slow warp, a touch deeper | v1's warped sine (loops) | review finding 9 | Claude |
| 2026-10-20 | The two fast zooms (16.9-18.0, 20.2-21.2 s) re-rendered at 16 subframes and spliced in frame-exactly | slower zooms; 16 subframes for the whole film (4x render time) | 4 subframes left stepped label copies only in those two moves (review round 3) | Claude |
| 2026-10-20 | Master through an oversampled look-ahead limiter, then a linear two-pass loudnorm | dynamic loudnorm | mallet transients made the peak-to-loudness ratio 18 dB; dynamic loudnorm would pump the music | Claude |
| 2026-10-20 | Music rendered 3 s past the end and wrapped onto the start | hard stop at 27.0 | the reel loops: note tails cross the seam the same way they cross any bar line | Claude |
| 2026-10-20 | Captions, SRT and the reading-time check come from one table (`LINES` in `index.html`) | separate lists | one source of truth; a retime can't desync the SRT | Claude |
| 2026-10-20 | Camera aims at where the ball will be 0.22 s ahead | velocity look-ahead | the follow spring lags ~0.2 s; the deep drop to Booking left its label under the safe line | Claude (safe-zone check) |
| 2026-10-20 | Sub-labels written on the plate face (a second line revealed when the plate opens) | under the plate | under Reply they sat on the dark hole (red on charcoal, banned) | Claude (review round 1) |
| 2026-10-20 | An engraved route groove links the stations and lights crimson as the ball completes it; it flows on the map | stations alone | the wall looked sparse, and "That is a system." needs a picture of one connected path | Claude (review round 1) |
| 2026-10-20 | End line structure: zoom out to the whole lit map ("Every step answered. That is a system."), then back to the logo and the ask | a separate end card | the device rules say an end card breaks the loop; the logo lives on the wall inside the cycle | Claude |
| 2026-10-20 | Return tube on the left carries the ball back to the cradle (Referral kicks it in) | one big ballistic flight | the loop is literally drawn on the wall: down the stations, back up the tube | Claude |
| 2026-10-20 | Reply missing = a dashed outline over a real opening in the wall; the ball falls into it and shrinks into the dark | ball falls off the bottom | the gap is physical (P7: message inside the image) and the dark rest is the planned silence | Claude |
| 2026-10-20 | Concept A (marble run, as briefed) | B: a speech bubble that ages unanswered; C: a split screen of two businesses | the workflow fixed concept A; B and C kept as alternatives (treatment §2) | workflow brief |
| 2026-10-20 | Engine: canvas, not HyperFrames | HyperFrames | physics path + subframe blur + per-frame procedural drawing; HyperFrames would add DOM cost for no gain | Claude |

## Approvals
| Date | What | By | Notes |
|---|---|---|---|
| | v1 cut | FAILED independent review r1 (`docs/review_independent_r1.md`) | not for posting |
| | v2 cut | pending (independent re-review, then the owner in the hub) | nothing is published by this session |

## Spend
Paid generation: none (0 Higgsfield credits, 0 ElevenLabs characters, 0 Atlas calls). Render: local CPU only.

## Log
- 2026-10-20 · read skill, house rules, knowledge (hyperframes, onetake principles, our-pipeline §3, lemo §4.6), card ig-satisfy3dverse, brand kit · ok
- 2026-10-20 · `refbank.py check --client straightscale --category beat-sync --devices beat-sync-hits,marble-run,dolly-follow,seamless-loop` · "ok: no repeats against the last films"
- 2026-10-20 · path solved backwards from the beat (contacts first, targets placed from in/out velocities), debug overview · ok
- 2026-10-20 · styleframes and strips (hook, dive, rebuild, run, map, end) · round 1 fixes (docs/review_log.md)
- 2026-10-20 · score + foley from `audio/events.json`; master -14 LUFS · ok
- 2026-10-20 · checks: seekcheck PASS, safezone 9:16 ok, safezone 4:5 ok, readcheck PASS, loopcheck PASS (both formats)
- 2026-10-20 · draft 2 (30 fps) review round 2 · fixes; final render 60 fps x 4 subframes, both formats (3 parallel segments each, about 8 min per format)
- 2026-10-20 · review round 3 on the final: stepped copies in the two fast zooms → re-rendered at 16 subframes, spliced (`tools/patch_fast.sh`) · seams PASS
- 2026-10-20 · delivered `deliver/v1/`: 9:16 21.2 MB and 4:5 16.4 MB, both 27.000 s / 1620 frames / 60 fps, -13.8 LUFS, -2.3 dBTP after AAC, LRA 10.1 LU; poster, contact sheet, SRT, credits, changelog
- 2026-10-20 · not done by this session (workflow rule): the reference-bank ledger entry. To log it: `python3 motion-studio/refbank/tools/refbank.py log --client straightscale --project straightscale-04 --refs ig-satisfy3dverse --category beat-sync --devices beat-sync-hits,marble-run,dolly-follow,seamless-loop,pull-back-reveal --hook guess-challenge --palette light --camera "follow-cam on the ball, dive into the hole, whip up, one pull-back to the whole map" --engine canvas --concept "One message, all the way: a crimson ball runs a marble wall of client steps; Reply is missing, it falls into the dark; rebuilt, it runs the full lit path and loops" --language en`
- 2026-10-20 · v2 · independent review r1 (`docs/review_independent_r1.md`): FAIL on one major finding (headline over a ghosted logo) and three axes under 8; every finding addressed in the source (treatment §6)
- 2026-10-20 · v2 · new checks: `tools/ghostcheck.mjs`, `tools/hookchange.mjs`, `audio/measure.py`, `tools/strip.sh`, `tools/splice.py`; `tools/readcheck.mjs` gates on 0.25 s per word + 0.5 s (Lemo printed as advice)
- 2026-10-20 · v2 · review round 4 on page stills and 30 fps drafts: fixed the band-times-light ghost (6.9 s), a safe-zone overshoot (12.2 s), the rebuild framing, the vein grid, the faint shaft
- 2026-10-20 · v2 · score re-cut for 25 s, stations +2 dB / pegs -1 dB, presence EQ, room tone, hatch / flight-home / arming foley; ebur128 trim after loudnorm
- 2026-10-20 · v2 · final 60 fps x 4 subframes both formats; round 5 fixes (rise in the dark, 16 subframes on the whip, even light fade on the reset) re-rendered as windows and spliced in one encode (`tools/splice.py`); all seams PASS
- 2026-10-20 · delivered `deliver/v2/`: 9:16 21.6 MB and 4:5 16.8 MB, both 25.000 s / 1500 frames / 60 fps, -14.0 LUFS, -2.4 dBTP after AAC, LRA 11.4 LU; ghostcheck 0 levels both formats; pacing longest quiet 1.5 s; poster, contact sheet, SRT (reference only), post caption, credits, changelog
- 2026-10-20 · v2 · not done by this session (workflow rule): the reference-bank ledger entry (command above, add `--devices ...,pull-back-reveal` as before); commit and push; a human listen
