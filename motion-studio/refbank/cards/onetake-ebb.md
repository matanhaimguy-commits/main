---
id: onetake-ebb
title: "Warm light floods a focus timer at zero and drains in rings that open onto the next screen"
url: references/onetake/cases/ebb-15s/
platform: web
creator: onetake
plays: 0
likes: 0
shares: 0
saves: 0
followers: 0
posted: null
captured: 2026-10-14
duration_s: 15
category: ui-saas
hook: [beautiful-first-frame]
devices: [mask-reveal, one-take-camera, pull-back-reveal, big-number, counter-ticker, whip-pan, grid-mosaic]
energy: medium
palette: [light, pastel]
palette_hex: ["#faf0e9", "#fcfbf6", "#f3c2a5", "#f7dbc7", "#ea9c6d"]
sound: [sfx-heavy, silence-moments]
voiceover: false
text_on_screen: headline
engine: [canvas, hyperframes]
difficulty: 3
fit: [saas, health, local-service, personal-brand]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 2.0
  mean_s_between_big_changes: 0.71
  change_rhythm_cv: 0.93
  quiet_share_2fps: 0.207
  hook_change_0_2s: 0.083
---

## The film in one line
Huge serif timer digits on warm paper pull back into a desktop focus-timer app, the session runs down as orange light rises through the glass, the light floods the frame at 00:00 and drains away in concentric rings that open onto a phone lock screen showing a break, then a whip drops onto rows of silky gradient cards that fly into a weekly grid and sink into the glow as the name rises.

Craft reference, not a social post: a 16:9 film for a fictional focus timer from the onetake repo. Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels or sound reused.

## Why it stops the scroll (first 2 s)
At 0.0-1.0 s "25:0" in an enormous high-contrast serif, cropped by the frame, warm glow at the bottom edge, dead still; at 1.5 s the camera pulls back and a sidebar appears; at 2.0 s the whole app window shows "25:00" and a start pill. Mechanism: an editorial type close-up recontextualised by a pull-back. Soft as a hook: still and silent for over a second (hook change 0.083); a reel must start the pull-back by 0.5 s.

## Beat map
| t (s) | on screen | what moves | sound (our loudness read) |
|---|---|---|---|
| 0.0-1.25 | 25:00 in macro | dead still | silent |
| 1.25-2.2 | the app window | pull back | quiet tones |
| 2.2-4.35 | the session | pill tapped; digits roll like an odometer; orange light rises behind them and turns them white where it passes; slow push, slight dutch | building |
| 4.35-5.25 | 00:00 | punch in on the colon; orange floods the frame; shake | loudest, about -15 LUFS |
| 5.25-7.55 | rings, the break | rings recede from the colon; a lock screen with a break timer sits in the smallest; push onto it | falling to near silence |
| 7.55-9.7 | whip, the day | fast tilt onto three rows of gradient cards at three depths; dolly along them | a hit, then quiet |
| 9.7-11.8 | the week | pull back; 21 cards fly into a 7 x 3 grid that sinks column by column into the glow | a gap near 10 s, rising |
| 11.8-15.0 | the name | serif name drops, a line rises, then 2.4 s dead still | last hit near 12 s, silent from 13.5 s |

Sound is undocumented and we cannot listen; -23 LUFS integrated with real silences suggests a sparse event score.

## Signature device
Light as the transition. One warm radial field lives under every scene and stands for time. It rises inside the digits as a masked fill, floods the frame at the climax, then recedes as concentric rings: alternating cream, peach and orange bands, each a circular mask expanding on an ease-out from the colon, with the next scene visible inside the innermost ring. Rings replace wipes.

## Pacing read
2 fps: 8.67 "cuts" per 10 s (punch, flood, whip and fly-in; no edits), big changes every 0.71 s, CV 0.93, 21 % quiet. Full rate: 27 % still, 33 % quiet, 10 beats, transitions at 5.0, 6.0, 7.83, 10.17 and 11.17 s, longest quiet run 3.33 s (the end), beat CV 0.61, spread 5.1x. Shape: frozen macro, slow build to the flood, a dense middle, a long true freeze on the name. Starts and ends on cream, so it could loop softly.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 3 cuts in 15.0 s sampled (2.0 per 10 s), at 5.0, 6.0, 8.0 s; 13 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
Warm paper (#faf0e9, #fcfbf6), peach (#f3c2a5, #f7dbc7), orange light (#ea9c6d). High-contrast Didone-style serif for numerals and name, small grotesk UI. Cards are marbled "silk" gradients in rose, ochre, plum and peach at three depths with focus falloff.

## Why it works
- The timer is a built-in countdown: the viewer waits for 00:00.
- The flood is the payoff; the rings deliver a second one (the phone) without a cut.
- Layered depth and soft focus signal a premium product; a long freeze lets the name land.

## Steal this (grammar) / Leave this (content)
- Steal: one material under every scene that carries every transition; macro type into a pull-back; flood at the climax, rings to reveal; depth layers with focus falloff; end on a true freeze.
- Leave: the fictional product, the numerals as set, the silk card art, the copy, the orange palette as a whole.

## Build it in our studio
Engine: canvas (gradients, circular masks, per-layer blur, shutter blur on the whip); stacked blur is slow in HyperFrames.
1. Macro digits with the light as a masked gradient inside the glyphs.
2. Pull back to the client's real app UI.
3. Flood the field to full frame on a punch.
4. Concentric masks with staggered expansion; the phone inside the inner ring.
5. Cards at three depths fly into a grid, sink into the glow, logo rises.
Hard part: silk gradients and blur without banding; seeded noise-warped gradients plus dither. No paid steps.

9:16: easier than most, since the lock screen is the natural vertical hero. Stack the digits on two lines to fill the height, centre the rings in the middle band, and turn card rows into columns drifting vertically.

## Business translations
- Yoga studio (health): a class timer in macro, light floods at zero and drains in rings onto the real booking screen.
- Meditation app (saas): session digits count down, flood at zero, rings open on the app's real "done" screen.
- Day spa (local-service): the appointment time in big serif type, light floods, rings open onto the confirmation and the spa's name.
