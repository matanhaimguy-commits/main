---
id: onetake-one-dot
title: "One dot plays every part: cursor, menu, ring, curve, ball, sun, and finally the dot on the i"
url: references/onetake/cases/one-dot-15s/
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
hook: [wait-for-it]
devices: [morph, one-take-camera, typing-caret, progress-ring, chart-grow, rigid-body-drop]
energy: medium
palette: [dark]
palette_hex: ["#0d0c12", "#09080d", "#14131b", "#07060b", "#f0e9da"]
sound: [sfx-heavy, music-beat, silence-moments]
voiceover: false
text_on_screen: headline
engine: [canvas, hyperframes]
difficulty: 3
fit: [saas, finance, health, personal-brand, any]
wow: 3
relevance: 5
pacing:
  cuts_per_10s: 1.33
  mean_s_between_big_changes: 3.0
  change_rhythm_cv: 1.21
  quiet_share_2fps: 0.241
  hook_change_0_2s: 0.012
---

## The film in one line
On near-black, a single violet dot pops in, stretches into a text cursor, splits into a four-item menu, types a request, swallows the sentence, hollows into a loading ring, unrolls into a spring curve, rolls off it as a bouncing ball, bounces open a cream card where it becomes the sun, folds back into a dot and lands as the dot on the i of the product name.

Craft reference, not a social post: a 16:9 launch film for the onetake skill (shown under its earlier name). Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels or sound reused.

## Why it stops the scroll (first 2 s)
At 0.0 s a dark ground with a faint lighter centre, nothing else; at 0.5 s a violet dot pops in on a spring; at 1.0 s it glides left and stretches into a caret; at 1.5-2.0 s it types a slash, then splits into four bullet dots with labels. Mechanism: a minimal pattern interrupt; with one object on screen the eye locks onto it and asks what it will become. Weak in a feed: the first half second is empty (hook change 0.012).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.5-1.5 | dot, caret | spring pop; glides and stretches; types a slash | pop, key tick |
| 1.75-3.35 | menu | dot splits into four bullets; one pulses, three fall away | ticks |
| 3.5-5.0 | request | caret types a sentence; a still beat | key clicks |
| 5.0-6.0 | send | the dot swallows the sentence; camera whips home with it | whoosh; music enters on the 6.0 downbeat |
| 6.0-8.0 | ring, curve | dot hollows into a ring that fills, then unrolls into a spring curve | rising tones |
| 8.0-10.0 | ball | a bead runs the curve, drops, bounces twice | gated silent on the hang, then bounce hits |
| 10.0-11.25 | result | the second bounce opens a cream card where the dot is the sun | loudest hit |
| 11.25-15.0 | name | card folds into the sun, sun into the dot; letters rise; it lands on the i and winks | landing hit, held chord, quiet end |

Sound per the case notes; landings on a 120 BPM grid.

## Signature device
Identity morph. One object never leaves; every new interface state is that object changing shape: circle to caret (width shrinks, height grows), caret to four circles, back to caret, back to circle (swallow), circle to ring (fill becomes stroke), ring to curve (cut at one point and unroll its length into a path), curve to ball, ball to sun, sun to the dot of a letter. The camera leads the subject by 0.1-0.2 s with springs on position and log zoom, over a dim far dot lattice that gives it something to slide past (a fixed-camera version was rejected for lacking tracking).

## Pacing read
2 fps: 1.33 cuts per 10 s, big changes every 3.0 s, CV 1.21, 24 % quiet. Full rate: 9 % still, 43 % quiet, only 2 beats detected, one transition at 11.42 s, longest quiet run 2.0 s, beat CV 0.74, spread 7.6x. The meters underread a small dot on black; the felt rhythm is a morph every 1-2 s on 120 BPM landings. Ends on a slow push and a wink. No loop.

## Look
Near-black ground (#07060b to #14131b), one violet accent (not in the measured top five), a cream card (#f0e9da) with a yellow sun at the result. White grotesk text, bold wordmark, faint dot grid, shutter smear on the streak.

## Why it works
- One subject means zero orientation cost.
- Each morph is a small surprise, so "what will it become" renews every 1-2 s.
- The ending ties the object you followed to the logo.
- Rewatch trigger: spotting how each shape came from the dot.

## Steal this (grammar) / Leave this (content)
- Steal: one element of the client's mark (a dot, bar, tick or circle) plays every role; a camera that leads it; a far lattice on a plain ground; landings on the beat; it snaps into the logo at the end.
- Leave: violet on black, the command menu, the sun card, the wordmark.

## Build it in our studio
Engine: canvas (closed-form shape morphs, springs from lib/motion.js, subframe blur for the streak).
1. List six to eight states the element passes through, each a real product moment.
2. Define each as a parametric shape (radius; rect size and corner; ring stroke; path).
3. Camera rig that leads the element; far lattice.
4. Sound on the landings; logo landing.
Hard part: topology changes (circle to path) without a pop; cut the ring at one point and map its arc length onto the curve. Zero assets.

9:16: one object suits a tall frame; the menu is already vertical; land the logo in the middle band. Relevance 5: any brand with a simple mark can use it.

## Business translations
- Payments app (finance): the dot in the logo becomes the cursor of a transfer field, a progress ring, a balance curve, then returns to the logo.
- Dental or physio clinic (health): the dot of the clinic's mark becomes a booking cursor, a check mark, and lands back in the mark.
- Coach or consultant (personal-brand): the dot of their initial types their headline, fills a programme progress ring, and ends as the full stop of their tagline.
