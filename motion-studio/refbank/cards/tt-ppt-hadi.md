---
id: tt-ppt-hadi
title: "A blank PowerPoint slide becomes a four-piece jigsaw SWOT infographic in one sped-up build"
url: https://www.tiktok.com/@ppt_hadi/video/7135980107868409089
platform: tiktok
creator: ppt_hadi
plays: 6900000
likes: 571300
shares: 4208
saves: 116793
followers: 323500
posted: 2022-08-26
captured: 2026-10-14
duration_s: 59
category: data-infographic
hook: [transformation-promise, sound-hook]
devices: [assembly-build, cursor-demo, icon-system, node-diagram]
energy: medium
palette: [saturated, light]
palette_hex: ["#e4e5e3", "#cdcfce", "#25304e", "#338cc2", "#db4332"]
sound: [trending-audio]
voiceover: false
text_on_screen: headline
engine: [hyperframes, canvas]
difficulty: 2
fit: [b2b, agency, education, finance, saas]
wow: 3
relevance: 4
pacing:
  cuts_per_10s: 0.67
  mean_s_between_big_changes: 3.75
  change_rhythm_cv: 1.19
  quiet_share_2fps: 0.026
  hook_change_0_2s: 0.162
---

## The film in one line
A sped-up PowerPoint screen recording draws one blue rounded square, carves it into a jigsaw piece, clones it
into a 2x2 puzzle, recolours it on navy, adds S-W-O-T letter discs, labels, icons and a title, and ends on the
finished slide in a red frame asking "YOUR IDEA IN THE COMMENT PLEASE".

## Why it stops the scroll (first 2 s)
- 0.0 s: an empty, light grey PowerPoint slide with faint centre guides and a cursor. Ribbon chrome at the top.
- 0.5-1.0 s: not sampled (1.5 s step); by 1.5 s a solid blue rounded square sits selected in the lower left,
  rotation handle showing.
- 2.0 s: the square is being worked on (handles, a circle being positioned on its right edge by 3.0 s).
- Mechanism: a blank canvas is a promise. Anyone who has made slides knows the empty slide, and the first shape
  appears within 1.5 s, so the viewer stays to see what it becomes. The music's vocal hook "Come check this"
  (the only words the transcript caught; it is the song, not a voiceover) does the calling.

## Beat map
Frames cover the whole 59 s (40 frames at 1.5 s).

| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-1.5 | blank slide, guides, cursor; then a blue rounded square | shape drawn and selected | song intro, "Come check this" |
| 3.0-7.5 | circle cut out of the right side (blank), circle added at the bottom (tab): one jigsaw piece | boolean shape ops, handles flicker | song |
| 9.0-13.5 | piece duplicated and rotated into a 2x2 square block | copies slide into place one by one | song |
| 15.0-18.0 | right-click menu, then the background turns navy and each piece gets its own colour: crimson, amber, green, cyan | colour pops piece by piece | song |
| 19.5-25.5 | navy circles with white S, W, O, T placed at the joints between pieces | discs dragged into place | song |
| 27.0-36.0 | text box "STRENGTH / Some texts goes here to explain briefly" typed, cloned to each piece and renamed WEAKNESSES, OPPORTUNITIES, THREATS | typing, copy-paste | song |
| 37.5-39.0 | Office icon library fills the screen | scroll through icon grid | song |
| 40.5-45.0 | white icons placed: weightlifter, standing figure, group with arrow, devil face | icons dropped then spread to their pieces | song |
| 46.5-55.5 | title typed above: "S.W.O.T ANALYSIS / FOR YOUR BUSINESS PRESENTATIONS", then all nudged to centre | text box resized, multi-select | song |
| 57.0-58.5 | finished slide inside a thick red border, white caps on red below: "YOUR IDEA IN THE COMMENT PLEASE" | hold | song ends |

## Signature device
Assembly build of a business framework from one primitive. A single rounded square (about 30 percent of frame
width) is turned into a jigsaw piece with two booleans: subtract a circle on one side (blank), union a circle on
another (tab), each circle roughly a third of the side. The piece is cloned four times and rotated 90 degrees
each time so tabs and blanks interlock into a perfect square. Only after the geometry is complete does colour
arrive: the ground flips from light grey to navy and the four pieces get four saturated hues at once, which is
the visual payoff. Then each layer of meaning is added in a fixed order: letter (S W O T in navy discs on the
seams), label, body line, icon, title. The cursor and selection handles stay visible, so the viewer sees it is
being made, not revealed.

## Pacing read
0.67 cuts per 10 s and a big change every 3.75 s: one sped-up take. CV 1.19: long stretches of small edits
broken by a few large jumps (navy flip at 16.5 s, icon library at 37.5 s, red end card at 57 s). Quiet share
0.026: always moving, in small steps. Hook change 0.162: the hook is the promise, not motion. Energy peaks at
the colour flip, then detail fills in and a static end card holds about 3 s. Not a loop.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 4 cuts in 60.0 s sampled (0.67 per 10 s), at 16.5, 37.5, 40.5, 57.0 s; 4 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette by role: light UI greys (#e4e5e3, #cdcfce) as frame and early ground; navy (#25304e) as the slide
  ground after the flip; crimson (#db4332), amber, green, cyan (#338cc2) as the four quadrant colours; white for
  letters, labels and icons; a bright red border and CTA band at the end.
- Type: a bold geometric sans in white caps for labels and title, small regular body text; letter discs are
  white caps in navy circles. At 1080 wide the labels are small (well under 44 px in the original).
- Texture: flat vector, no gradients, no shadows. Camera: static screen capture, no zoom.

## Why it works
- Clear before/after promise: blank slide to finished infographic, and the viewer can see each step.
- Save trigger: it is a recipe (116.8 K saves, one save per five likes). People keep it to copy later.
- Satisfying fit: interlocking tabs and the four-colour flip give a small "click" of completion.
- Comment trigger at the end: an explicit ask for ideas, on a high-contrast red card.
- The breakout is about 21 times the follower count, driven by usefulness rather than spectacle.

## Steal this (grammar) / Leave this (content)
- Steal: build a framework from one primitive shape, geometry first then colour as the payoff, meaning added in
  layers (letter, label, icon, title), visible cursor as the "making" signal, a held end card with one ask.
- Leave: the PowerPoint chrome, the SWOT layout and placeholder copy, Microsoft icons, the song, the red frame.

## Build it in our studio
- Engine: `hyperframes` (SVG shapes plus GSAP), or `canvas` for the boolean morphs. No fake software UI: we
  build on a clean brand canvas, or use a real screen recording of the client's own tool as `footage`.
- Scene plan: 1) empty brand-coloured canvas, a cursor draws one rounded square; 2) boolean notch and tab
  appear as SVG path morphs; 3) clone and rotate into the client's framework (2x2, 3-step, cycle); 4) ground
  flips to the brand dark, pieces take brand tints; 5) letters, labels and icons drop in on beats; 6) title and
  a held CTA card.
- Hard part: making it read as hand-made rather than a slick reveal. Keep a cursor, selection boxes drawn in
  brand line weight and slight "nudge" overshoots via `spring()`.
- Difficulty 2. A 30-45 s cut renders in about 8-12 min in HyperFrames (~16 s per second).

## Business translations
- Consultancy or agency: their own 4-step method assembled as interlocking pieces, ending "Which step do you
  skip? Comment below".
- Accounting firm: a quarterly tax checklist built as a puzzle from one square, each piece a deadline type.
- SaaS onboarding: the product's three core features built as linked shapes, each getting its real icon and
  label, ending on the sign-up URL.
