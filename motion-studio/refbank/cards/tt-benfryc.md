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
  cuts_per_10s: 3.46
  mean_s_between_big_changes: 1.44
  change_rhythm_cv: 0.53
  quiet_share_2fps: 0.04
  hook_change_0_2s: 0.175
---

## The film in one line
A 3D render launch for a light-grey keyboard with orange accent keys: the boxed product floats under the word
"Introducing", macro camera moves glide along the case for each feature (tilt risers, USB-C, Bluetooth switch,
a slim side display with volume and a timer), then a "Pre-Order Today" card with the price pill goes dark so
the keyboard glows, and the maker's wordmark closes it.

## Why it stops the scroll (first 2 s)
- 0.0 s: soft grey seamless background, a white product box tilted towards camera with the product name on the
  lid and an orange base, tiny "Introducing" caption at the top, tiny maker credit at the bottom.
- 0.5-1.0 s: the box drifts and rotates a few degrees; nothing else moves.
- 2.0 s: cut to a macro side profile of the case with a magnetic riser block under it, caption "Magnetic tilt
  risers".
- Mechanism: a calm, premium first frame in a feed of loud videos (contrast through restraint), plus the word
  "Introducing", which promises a product reveal. The hook is the render quality, not motion (hook change
  0.175).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-1 | product box, "Introducing", maker credit | slow drift and rotation | rhythmic electronic beat |
| 2-4 | macro side profile, riser block under the case, USB-C port; "Magnetic tilt risers" | camera tracks sideways along the edge, riser snaps on | beat |
| 5 | low angle; orange cable plugs into the port; "USB-C Connectivity" | cable slides in from lower left | beat |
| 6-7 | other side of the case, orange power slider; "Bluetooth Compatible" | slider flips | beat |
| 8 | top three-quarter view of the right end with knobs and a slim screen showing a volume bar; "Control Computer Features" | volume bar moves | beat |
| 9 | extreme macro on the fn key, shallow focus | key press | beat |
| 10-15 | same view; screen shows 9:00, then a menu (5, 10, 15, 30, 60, 120), then fills amber and counts 9:58, 9:57; key-combo chips below light up ("fn + knob", "fn x fn"); "Built-in Timer" | menu selection steps, timer fill, chips highlight | beat |
| 16-19 | end card: wordmark, serif "Pre-Order Today", orange price pill, keyboard at three-quarter view, two URLs | keyboard racks from blur to sharp and slides in | beat |
| 20-22 | same card, lights out: background dark, keyboard edges and keys backlit orange, pill glows white | light switch, glow | beat |
| 23 | black, three small white glyphs (cross, half disc, square) | glyphs converge | beat |
| 24-25 | maker wordmark in white on black, URLs | hold | beat ends |

## Signature device
A quiet macro feature tour: each feature gets 1-3 s, one camera move and one tiny caption. The camera sits very
close to the product with a long lens, moving laterally along the case edge (dolly-follow) so features
appear in order like a guided walk around the object. The product does one physical action per feature (riser
snaps on, cable plugs in, switch flips, screen state changes). Captions are deliberately small (about 22-26 px
on a 1080 frame, light sans, centred near the top), which signals confidence and keeps the product as the
picture. The second half answers "what does it do" with the product's real interface on the built-in screen,
with key-combo chips under the product that light up in sync. The ending is a before/after on one card: the
same pre-order layout in daylight, then with the lights off so the product glows.

## Pacing read
At a 1 fps sample, 3.46 cuts per 10 s and a big change every 1.44 s, with an uneven rhythm (CV 0.53): quick
feature cuts in 2-9 s, then a 6 s hold on one framing (10-15 s) where only the screen changes, then a 4 s end card
that changes only through light. Quiet share is low (0.04) because something always moves, but the moves are
small. The strongest change is the lights-out at 20 s, a late second hook that holds viewers through the call to
action. It ends on a 2 s wordmark hold; no loop.

## Look
- Palette: warm light grey seamless (#c3c4c0, #e3e4e2), product white and grey, one orange accent for keys,
  cable, switch and price pill; black (#010101, #2c2826) only for the lights-out and the logo end.
- Type: captions in a small light sans; the end card pairs a condensed serif headline (about 70 px) with a pill
  in the accent colour; URLs tiny.
- Light: soft top light, gentle shadows, shallow depth of field on macros; final scene lit by the product.
- Camera: long-lens macros, slow lateral tracks, one rack focus on the end card.

## Why it works
It reads like an Apple-grade launch from a small creator account (2.1M plays on fewer than 6k followers), which
makes design and keyboard fans share it. The feature list is short and each item is shown, not told, so it
works with the sound off. The timer demo is a small story inside the film (set, start, count) and the key-combo
chips teach the interaction. The lights-out end card adds a final reveal right where most ads lose people.
Saves come from people keeping it as launch-film reference.

## Steal this (grammar) / Leave this (content)
- Steal: one caption per feature in a deliberately small size; one physical action per feature; a held framing
  where only the product's own screen changes; key-combo or step chips that light in sync; end card with a
  daylight-to-dark relight.
- Leave: the keyboard, its renders, the maker's wordmark and glyphs, the price and URLs, the orange accent.

## Build it in our studio
Engine: client renders or product photography (footage) assembled in HyperFrames, with canvas for any
product-screen UI.
1. Ask the client for high-resolution renders or macro photos of each feature (or the product's 3D file). We
   cannot render photoreal products ourselves; `gen-3d` (paid, approval) is a fallback that risks inaccuracy.
2. Each feature shot: 2-3 s slow push or lateral pan across a high-res still with slight parallax (product layer
   over background), one caption top centre in the safe zone. Note house rule: body text is never under 44 px,
   so our captions go at 44-48 px in a light weight; keep the restraint through weight and spacing, not size.
3. Screen demo: rebuild the client's real UI states in HyperFrames, masked into the product's screen area, with
   chips below that highlight in sync.
4. End card: the call to action and real price only if the client supplies it with a date; relight by
   crossfading to a dark render of the same angle, or a canvas glow pass on the product edges.
- Hard part: the physical actions (cable plugs in, switch flips) need render sequences or video; with stills
  only, use simple 2D moves on separated layers.
- Difficulty 3 with client renders, 5 without them.

## Business translations
- E-commerce hardware or homeware: a lamp or kettle tour, one feature per macro still, ending on a relit
  "Available now" card.
- SaaS with a device or app: the phone sits still while only its screen changes through the three main flows,
  with step chips lighting below.
- B2B equipment maker: slow macro pans over a machine's real photos, one small caption per spec, ending on a
  dark card with the contact line.
