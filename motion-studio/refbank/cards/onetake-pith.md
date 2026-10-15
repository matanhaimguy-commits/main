---
id: onetake-pith
title: "Pulling out from one glowing terminal pixel until a whole desktop app has grown around it"
url: references/onetake/cases/pith-21s/
platform: web
creator: onetake
plays: 0
likes: 0
shares: 0
saves: 0
followers: 0
posted: null
captured: 2026-10-14
duration_s: 21.5
category: ui-saas
hook: [scale-shock, wait-for-it]
devices: [zoom-through-scale, pixel-art, typing-caret, one-take-camera, reaction-shot, icon-system]
energy: medium
palette: [dark, light]
palette_hex: ["#e1e2dc", "#18160b", "#fefefd", "#d3d4cf", "#f1f1ee"]
sound: [sfx-heavy, silence-moments]
voiceover: false
text_on_screen: heavy
engine: [canvas]
difficulty: 4
fit: [saas, b2b, education, ecommerce]
wow: 4
relevance: 3
pacing:
  cuts_per_10s: 1.4
  mean_s_between_big_changes: 0.67
  change_rhythm_cv: 0.82
  quiet_share_2fps: 0.167
  hook_change_0_2s: 0.393
---

## The film in one line
The frame opens inside one amber phosphor pixel and pulls back through a typed terminal prompt and streaming agent output, a window border draws itself around the text, the title bar lands and flips everything from amber dark mode to a light theme in one frame, the camera dives into two blinking pixel eyes in the title bar, follows their gaze to the input where a message is typed, then pulls out to a small window with seven tool names lined up beneath it and the product name.

Craft reference, not a social post: a 16:9 launch film for Pith, a real desktop app for a coding agent, from the onetake repo. Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels, font or sound reused.

## Why it stops the scroll (first 2 s)
At 0.0-1.0 s the frame is a few enormous amber cells with dark gaps, an abstract plaid, dead still, with one blink near 1.1 s; by 2.0 s the pull-back has begun and the cells resolve into giant pixel letters of a typed command. Mechanism: scale shock, an abstract frame that becomes legible inside two seconds. The strongest measured open in the onetake set (hook change 0.393).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-1.55 | one lit pixel at about 440x | dead still, one blink | phosphor hum, coil whine |
| 1.55-3.3 | the caret | pull back to about 9x; a prompt types in amber | dry key clicks |
| 3.3-7.55 | the wall, the frame | pull back to about 1.35x; output streams up; a 1 px border draws itself | hum, ticks |
| 7.55-7.77 | clamp and flip | title bar drops; amber on black becomes ink on light in one frame | hum cut; first note in the silence |
| 7.8-10.3 | the desk | held; detail lines fold, a sidebar slides out | notes, then silence |
| 10.3-12.1 | the eyes | push to about 44x into two pixel eyes; dead still; they blink, pupils snap aside | silence, lid ticks, a snap |
| 12.1-15.0 | the gaze | camera follows the gaze to the input; a message is typed and sent | keys |
| 15.0-21.5 | answer, tools, name | pull out to about 0.5x; seven row squares fly out and line up, each naming itself; the name drops in lavender | ticks, last notes |

Sound per the case notes: no music until the window exists; rests are scored.

## Signature device
Carry by scale, pulling out. Everything that appears was already inside the previous frame: pixel, caret, prompt, output, window, desktop. The interior is a page drawn in its own units under one transform, so type stays crisp at 440x, and unlit cells keep a faint residue so the deep camera has texture. The mid-film transition is the product's own theme switch, and the claim (seven tools) is built from seven objects already on screen, not from a caption.

## Pacing read
2 fps: 3.72 "cuts" per 10 s (the flip and the dives), big changes every 0.67 s, CV 0.82, 17 % quiet. Full rate: 15 % still, 29 % quiet, 15 beats, transitions at 1.17, 2.0, 7.83 and 12.58 s, longest quiet run 2.42 s, beat CV 0.63, spread 8.8x. The eye close-up is a second rest that doubles as the hand-off. No loop.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 3 cuts in 21.5 s sampled (1.4 per 10 s), at 1.0, 2.0, 8.0 s; 8 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
First third amber (#d1920b) on near-black (#18160b) with scanlines and pixel gaps; then a light grey desktop (#d3d4cf to #fefefd), a hard window shadow and a lavender name. The product's own bitmap pixel font throughout.

## Why it works
- Abstraction to recognition in two seconds; a long pull-out keeps adding context, so curiosity holds without cuts.
- The theme flip is a mid-film pattern interrupt.
- The blinking eyes add a character beat and a smile.

## Steal this (grammar) / Leave this (content)
- Steal: open inside the smallest unit of the product (a pixel, cell or stitch) and pull out; a real product behaviour (a theme or mode switch) as the transition; a mascot close-up as the rest; build the claim from objects already on screen.
- Leave: the terminal content, the eyes, the app UI, the pixel font, the name and colours.

## Build it in our studio
Engine: canvas (crisp text at 440x needs our own transforms).
1. Page model of the client's real UI in its own units.
2. A log-zoom spring anchored to a subject that travels (caret, mascot, input).
3. A single-frame mode flip with an impact; a close-up on a real logo or mascot detail as the rest.
4. Gather the real feature icons into a row, then the name.
Hard part: zoom steps of several log units in under a second without the target drifting off frame; use a travelling anchor and a longer settle. Difficulty 4.

9:16: the window becomes a phone screen, which is portrait anyway; end the pull-out with it at about 60 % of frame height; the feature row becomes a two-row grid; readable text at 36-40 px or more.
## Business translations
- App with a dark mode (saas): start inside one dark pixel, pull out, and make the flip to light mode the single hit.
- Online course platform (education): open inside one letter of a lesson, pull out to the course page, gather the real module icons.
- Print shop or textile brand (ecommerce): open inside one halftone dot or stitch, pull out to the finished product and the logo.
