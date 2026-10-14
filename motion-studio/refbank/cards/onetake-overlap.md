---
id: onetake-overlap
title: "Two cursors ink two misaligned print layers until they snap into register and a hidden symbol appears"
url: references/onetake/cases/overlap-15s/
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
category: kinetic-type
hook: [mid-action-start, wait-for-it]
devices: [mask-reveal, halftone-collage, cursor-demo, rack-focus, list-of-n]
energy: medium
palette: [light, saturated]
palette_hex: ["#f1ebe0", "#b1a99c", "#bbbab0", "#e5b5c5", "#3275a2"]
sound: [sfx-heavy, silence-moments]
voiceover: false
text_on_screen: headline
engine: [canvas]
difficulty: 3
fit: [agency, b2b, saas, events]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 4.67
  mean_s_between_big_changes: 0.68
  change_rhythm_cv: 0.72
  quiet_share_2fps: 0.069
  hook_change_0_2s: 0.288
---

## The film in one line
A cream sheet slams onto a warm grey print bed, a pink cursor tagged "you" and a blue one tagged "them" roll ink in from opposite edges leaving two clouds of halftone dots that show nothing, a loupe finds the dots missing each other, "them" clicks a registration mark, the blue layer snaps into alignment and a violet ampersand appears in the overprint, a run of other word pairs prints the same way, and the product name prints last before the locked camera finally pushes in where its two halves overlap.

Craft reference, not a social post: a 16:9 film for a fictional two-person canvas app, from the onetake repo. Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels or sound reused.

## Why it stops the scroll (first 2 s)
- 0.0 s: an out-of-focus warm grey surface, empty.
- 0.5 s: a cream sheet slams in, still soft.
- 1.0 s: focus racks sharp; a pink "you" cursor appears at the left edge.
- 1.5-2.0 s: a blue "them" cursor at the right; pink and blue ink bands roll in and the two words print.
Mechanism: a physical slam plus two named characters entering from opposite sides sets up a relationship; the dot cloud that follows is a puzzle. The strongest physical open in the onetake set after pith (hook change 0.288).

## Beat map
| t (s) | on screen | what moves | sound (our loudness read) |
|---|---|---|---|
| 0.2-1.25 | bed and sheet | sheet slams in; rack focus to sharp | a slam, then near silence |
| 0.95-1.5 | two cursors | "you" and "them" grab a roller each | quiet |
| 1.5-3.6 | one pass from both sides | rollers pulled in and rolled out; each prints its word and a circle of dots; only noise | rolling, moderate |
| 3.6-4.2 | rest | nothing moves | silence |
| 4.2-5.8 | the loupe | a magnifier glides over dots that miss each other and a doubled mark | quiet |
| 6.0 | in register | "them" clicks a crosshair; blue snaps; a violet ampersand appears | loud hit |
| 6.35-7.2 | loupe lifts | the pair reads whole with the ampersand | loud |
| 7.2-8.5 | print run | six sheets slam one after another, each a different word pair with the same mark | rhythmic slams |
| 8.6-9.7 | new sheet | "them" yanks the stack away; a blank sheet slams in | moderate |
| 9.7-11.55 | the name | the same pull prints the name in two halves and colours; the blue snaps | moderate |
| 11.7-15.0 | push in | the locked camera pushes into the crossing of two letters, tilts down to the line, pulls back to the card | loudest near 12 s, then fades |

The case notes do not describe the sound; the column is our loudness read only (integrated -16 LUFS, silences at about 1 and 4 s).

## Signature device
The message exists only in register. Two plates share one random dot grid and one coin flip per cell: plate A inks the heads, plate B inks the tails except inside a hidden glyph, where it also inks heads. Each plate alone is the same noise; offset by a few cells they read as two clouds; only exactly aligned do the glyph's cells overlap and, with multiply blending, show a third colour. Geometry: a dot circle about a third of sheet height, cells about 1 % of sheet width, the blue plate offset by a few cells until a spring snaps it home. Camera: locked off like a copy stand until the payoff, then one operator move.

## Pacing read
2 fps proxy: 4.67 "cuts" per 10 s (the slams and the snap), big changes every 0.68 s, CV 0.72, 7 % quiet. Full-rate checker: 17 % still, 27 % quiet, 12 beats, transitions at 0.5, 9.08 and 12.83 s, longest quiet run 0.83 s (a rest WARN: no rest reaches 1 s), beat CV 0.67, spread 7.6x. The one planned rest (3.6-4.2 s) is short; energy peaks twice, at the snap (6 s) and the name (12 s). The camera's first move at 11.7 s lifts the ending. No loop.

## Look
Cream stock (#f1ebe0) on a warm grey bed (#b1a99c, #bbbab0); fluorescent pink (#e9579f, sixth in the measured list) and riso blue (#3275a2) overprinting to violet; pale pink tint (#e5b5c5). A heavy condensed grotesk for the big words (about a sixth of frame height), monospace for small print lines. Halftone dots, registration crosshairs in the corners, slight plate shift. Flat light.

## Why it works
- A puzzle (noise that must hide something) with a visible cause (the click) and an instant payoff.
- The print run lets the viewer start predicting each pair, which is satisfying.
- Holding the camera still makes the final push feel like an event.
- Comment trigger: how does the hidden mark work.

## Steal this (grammar) / Leave this (content)
- Steal: a message that appears only when two parts align; two named cursors as characters; a locked camera until the payoff; a print-run montage of variations; one production process defining the whole look.
- Leave: the you and them pairs and all copy, the split name, the exact colours, the fictional product.

## Build it in our studio
Engine: canvas (seeded dot grid, two layers with multiply compositing, a spring snap, the loupe as a scaled clip).
1. Define the hidden glyph as a mask over the grid; seed a coin per cell.
2. Render plate A and plate B with an offset.
3. Cursors pull rollers in (accelerating) and roll out (easing).
4. Snap and reveal; loupe pass before it.
5. A run of variants, then the logo printed the same way.
6. The camera's first and only move.
Hard part: the hidden glyph must read on a phone: cells of 12 px or more on a 1080-wide frame and a simple glyph. Difficulty 3, zero assets.

9:16: use a portrait sheet; cursors enter from top and bottom; the dot circle sits in the middle band; the two big words stack one above the other.

## Business translations
- Co-branding or partnership launch (agency, b2b): two brand colours print noise until they align and the shared symbol appears.
- Wedding planner or venue (events): two first names in two inks; the ampersand appears only when the layers align.
- Team collaboration software (saas): "you" and "your team" cursors print halves of a plan; it reads only when both are in.
