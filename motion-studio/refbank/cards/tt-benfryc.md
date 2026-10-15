---
id: tt-benfryc
title: "Quiet macro feature tour of a keyboard, one tiny caption per feature, then a lights-out pre-order card"
url: https://www.tiktok.com/@benfryc/video/7354063442849910058
platform: tiktok
creator: benfryc
plays: 2100000
likes: 155400
shares: 19100
saves: 29519
followers: 5856
posted: 2024-04-04
captured: 2026-10-14
duration_s: 26
category: product-motion
hook: [beautiful-first-frame]
devices: [dolly-follow, list-of-n, countdown, before-after, cursor-demo]
energy: calm
palette: [light, mono]
palette_hex: ["#c3c4c0", "#e3e4e2", "#010101", "#2c2826", "#754e45"]
sound: [music-beat]
voiceover: false
text_on_screen: captions
engine: [footage, hyperframes, canvas, gen-3d]
difficulty: 3
fit: [ecommerce, saas, b2b, events]
wow: 3
relevance: 5
pacing:                               # frames_metrics.py on a 1 fps sample
  cuts_per_10s: 1.92
  mean_s_between_big_changes: 1.44
  change_rhythm_cv: 0.53
  quiet_share_2fps: 0.04
  hook_change_0_2s: 0.175
---

## The film in one line
A 3D-render launch for a light-grey keyboard with orange accent keys: the boxed product floats under
"Introducing", macro moves glide along the case for each feature (tilt risers, USB-C, Bluetooth switch, a slim
side display with volume and a timer), then a "Pre-Order Today" card goes dark so the keyboard glows, and the
maker's wordmark closes it.

## Why it stops the scroll (first 2 s)
- 0.0 s: soft grey seamless, a white box tilted to camera with the product name and an orange base; tiny
  "Introducing" at the top, tiny maker credit at the bottom.
- 1.0 s: the box drifts and rotates a few degrees.
- 2.0 s: cut to a macro side profile with a magnetic riser block, caption "Magnetic tilt risers".
- Mechanism: a calm premium frame in a loud feed, plus "Introducing" promising a reveal. Render quality is the
  hook, not motion (hook change 0.175).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-1 | box, "Introducing", maker credit | slow drift and rotation | rhythmic electronic beat |
| 2-4 | macro side profile, riser, USB-C port; "Magnetic tilt risers" | lateral track along the edge, riser snaps on | beat |
| 5-7 | orange cable plugs in ("USB-C Connectivity"); orange power slider ("Bluetooth Compatible") | cable slides in, slider flips | beat |
| 8-9 | top three-quarter view, knobs and a slim screen with a volume bar ("Control Computer Features"); macro of the fn key | bar moves, key press | beat |
| 10-15 | screen shows 9:00, a menu (5 to 120), then fills amber counting 9:58, 9:57; key-combo chips below light up; "Built-in Timer" | menu steps, timer fill, chips highlight | beat |
| 16-19 | end card: wordmark, serif "Pre-Order Today", orange price pill, keyboard, two URLs | keyboard racks from blur to sharp | beat |
| 20-22 | same card, lights out: keys and edges backlit orange, pill glows white | relight | beat |
| 23-25 | three white glyphs converge into the maker's wordmark on black | converge, hold | beat ends |

## Signature device
A quiet macro feature tour: each feature gets 1-3 s, one camera move and one tiny caption. A long lens sits very
close and tracks sideways along the case edge, so features arrive in order like a walk around the object. The
product performs one physical action per feature. Captions are deliberately small (about 22-26 px on a 1080
frame, light sans, top centre). The second half shows the product's own interface on its built-in screen, with
key-combo chips that light in sync. The ending is a before/after on one card: daylight, then lights out.

## Pacing read
At a 1 fps sample: 3.46 cuts per 10 s, a big change every 1.44 s, uneven (CV 0.53): quick feature cuts at 2-9 s,
a 6 s hold where only the screen changes, a 4 s end card that changes only through light. Quiet share 0.04. The
lights-out at 20 s is a late second hook that carries viewers through the call to action. Ends on a wordmark
hold; no loop.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 5 cuts in 26.0 s sampled (1.92 per 10 s), at 5.0, 6.0, 8.0, 16.0, 20.0 s; 9 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
Warm grey seamless (#c3c4c0, #e3e4e2), product white and grey, one orange accent (keys, cable, switch, pill);
black (#010101, #2c2826) only for lights-out and the logo. Light sans captions; condensed serif headline (about
70 px) with an accent pill on the end card. Soft top light, shallow focus, one rack focus.

## Why it works
It reads as a premium launch from a tiny account (2.1M plays, under 6k followers), so design fans share it. Each
feature is shown, not told, so it works muted. The timer demo is a story within the film (set, start, count) and
the chips teach the interaction. The relight adds a reveal exactly where ads usually lose people.

## Steal this (grammar) / Leave this (content)
- Steal: one small caption and one physical action per feature; a held framing where only the product's screen
  changes; chips lighting in sync; an end card that relights from day to dark.
- Leave: the keyboard and its renders, the maker's wordmark and glyphs, the price, URLs and orange accent.

## Build it in our studio
Engine: client renders or product photos (footage) assembled in HyperFrames; canvas for screen UI.
1. Get high-res renders or macro photos per feature, or the 3D file; `gen-3d` (paid, approval) is a risky
   fallback.
2. Each feature: 2-3 s slow push or lateral pan with slight parallax, one caption. House rule: text never under
   44 px, so keep the restraint through light weight and spacing, not tiny size.
3. Rebuild the client's real UI states masked into the product screen, chips below in sync.
4. End card with a real, dated price only if supplied; relight by crossfading to a dark render or a canvas glow
   pass on the edges.
- Hard part: physical actions need render sequences; with stills, use 2D moves on separated layers. Difficulty 3
  with client renders, 5 without.

## Business translations
- Homeware e-commerce: a lamp tour, one feature per macro still, ending on a relit "Available now" card.
- SaaS with an app: the phone stays still while only its screen moves through three flows, step chips below.
- B2B equipment maker: slow macro pans over real machine photos, one small spec caption each, dark contact card.
