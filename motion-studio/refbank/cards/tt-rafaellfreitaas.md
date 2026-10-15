---
id: tt-rafaellfreitaas
title: "Three white dots spin, merge into a green blob that bounces and becomes a music app's icon and wordmark"
url: https://www.tiktok.com/@rafaellfreitaas/video/7157543761185180933
platform: tiktok
creator: rafaellfreitaas
plays: 1200000
likes: 23200
shares: 38500
saves: 11558
followers: 368
posted: 2022-10-23
captured: 2026-10-14
duration_s: 8
category: logo-reveal
hook: [wait-for-it, familiar-ip]
devices: [morph, mask-reveal, word-by-word]
energy: medium
palette: [dark, brand-colour]
palette_hex: ["#000000", "#000100", "#38ea68"]
sound: [sfx-heavy]
voiceover: false
text_on_screen: none
engine: [canvas, hyperframes]
difficulty: 2
fit: [saas, agency, ecommerce, restaurant, any]
wow: 3
relevance: 5
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 8.0
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.2
  hook_change_0_2s: 0.024
---

## The film in one line
On pure black, three small white dots appear in a triangle and rotate, collapse into one glowing green ball,
which squashes, flies off and lands back as the brand's circular icon, slides left, and the wordmark is written
out letter by letter beside it.

## Why it stops the scroll (first 2 s)
- 0.0 s: pure black frame (landscape 16:9 inside the 9:16 feed).
- 0.5 s: three small white dots in a triangle, centred, about 2% of frame width each.
- 1.0-1.5 s: the triangle rotates and widens a little, like a loading spinner.
- 2.0 s: the dots have merged into one green circle with a soft glow, about one fifth of frame height.
- Mechanism: almost nothing on screen, so the eye locks onto the few moving dots; viewers who know the brand
  colour start guessing the logo as soon as the green appears. A sound effect marks the merge (per the AI
  description). The hook is the slow build, not a picture.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0 | black | nothing | not described |
| 0.5-1.5 | three white dots in a triangle | triangle rotates about its centre, spacing grows | soft SFX |
| 2.0 | single green ball with a glow, centre | dots converge and pop into the ball | merge SFX |
| 2.5 | ball squashed into an egg, tilted | squash and stretch | playful SFX |
| 3.0 | ball stretched, flying to the upper left | it leaves frame centre fast | whoosh-like SFX (not certain) |
| 3.5 | ball returns, a wedge bites out of it, a curved green arc trails below | ball reforms, arcs are cut | playful SFX |
| 4.0-4.5 | full circular icon with three curved bars | small scale overshoot and settle | SFX |
| 5.0-6.0 | icon slides left, letters appear one after another to its right | wordmark reveals left to right | SFX |
| 6.5-7.5 | full lockup centred, settles a little smaller | gentle scale down, hold | ends |

## Signature device
One shape, many states. The film never cuts: three dots become one ball, the ball becomes a soft body with
squash and stretch (about 30% deformation along the motion axis), it leaves the centre and comes back, and its
final landing carves out the three curved bars of the icon as if they were bitten out of the ball. Every state
is driven by springs with clear overshoot, so it feels like a living object rather than a logo fading in. Once
the icon is set, it moves left by about one icon width and the wordmark is revealed letter by letter from behind
it (a mask that opens to the right), then the lockup scales down about 10% to rest. Total: 2 s of dots, 2 s of
blob, 3 s of lockup.

## Pacing read
The metrics read 0 cuts and a quiet share of 0.2 because the elements are tiny on a black frame: frame
difference never crosses the cut threshold (hook change 0.024). In reality the motion never stops for the first
5 s; the rhythm is a steady chain of state changes about every 0.5 s, then a 2 s hold on the lockup. It is a
classic sting structure: tension (spinner), release (merge), play (bounce), resolution (logo). It ends on the
hold, so the loop restarts from black, which reads as a natural reset.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 0 cuts in 8.0 s sampled (0.0 per 10 s); 0 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette by role: black background (#000000), white for the starting dots, one brand green (#38ea68 measured
  on the icon) for every shape after the merge.
- Type: the brand's own rounded geometric wordmark, about one third of frame width in the final lockup. No other
  text.
- Texture and light: flat vector shapes; a soft outer glow only on the ball at the merge moment.
- Camera: none; flat 2D, centred, landscape 16:9.

## Why it works
- Familiar IP: guessing the brand from colour and shape is the game, and the payoff is a logo everyone knows.
- Craft share: motion designers share it as a reference (38.5k shares, more than its 23.2k likes). Breakout of
  about 3,000 times its 368 followers.
- Character in a logo: squash and stretch gives the mark a personality in 8 s.
- Short and clean: 8 s, then a hold, then the loop.

## Steal this (grammar) / Leave this (content)
- Steal: start from primitive dots, merge into one brand-colour shape, give it one playful soft-body move, carve
  the mark out of it, then reveal the wordmark from behind the mark. Springs with overshoot at every step.
- Leave: the third-party logo and wordmark, their exact sound design.

## Build it in our studio
- Engine: canvas engine (springs and squash and stretch are native there); HyperFrames also works with GSAP.
- Scene plan: 1) three dots on a rotating triangle with a spring on radius; 2) converge to a circle in the brand
  colour, one glow pulse; 3) squash and stretch along velocity, a hop out and back; 4) morph the circle into the
  client's real mark (official SVG, or traced with `tools/vectorize_mark.py`), using a mask that carves the
  inner shapes; 5) slide the mark, reveal the real wordmark with a rectangular mask, settle with a spring.
- Hard part: the carve from ball to mark must use the official logo geometry (no redrawn logos). Build the carve
  as an animated mask over the real SVG so the final frame is the exact file.
- Difficulty 2: about 8 s at 60 fps, fast to render. Add placed SFX from event times.

## Business translations
- SaaS: three dots of a loading spinner merge into the product's app icon, then the name types out beside it.
- Restaurant: three drops of sauce merge into a blob that bounces and becomes the restaurant's round logo.
- E-commerce brand: three product-colour dots merge, bounce and become the shop's monogram for the end card of
  every ad.
