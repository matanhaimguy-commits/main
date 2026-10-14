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
A cream sheet slams onto a warm grey print bed, a pink cursor tagged "you" and a blue one tagged "them" roll ink in from opposite edges leaving two clouds of halftone dots that show nothing, "them" clicks a registration mark, the blue layer snaps into alignment and a violet ampersand appears in the overprint, a run of other word pairs prints the same way, and the product name prints last before the locked camera finally pushes in where its two halves overlap.

Craft reference, not a social post: a 16:9 film for a fictional two-person canvas app from the onetake repo. Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels or sound reused.

## Why it stops the scroll (first 2 s)
At 0.0 s an out-of-focus warm grey surface; at 0.5 s a cream sheet slams in, still soft; at 1.0 s focus racks sharp and a pink "you" cursor appears at the left edge; at 1.5-2.0 s a blue "them" cursor at the right, ink bands roll in and the two words print. Mechanism: a slam plus two named characters from opposite sides sets up a relationship; the dot cloud is a puzzle. A strong open for the set (hook change 0.288).

## Beat map
| t (s) | on screen | what moves | sound (our loudness read) |
|---|---|---|---|
| 0.2-1.5 | bed, sheet, cursors | sheet slams; rack focus; each cursor grabs a roller | a slam, then near silence |
| 1.5-3.6 | one pass from both sides | rollers pulled in and rolled out; two words and two dot circles; only noise | rolling, moderate |
| 3.6-4.2 | rest | nothing moves | silence |
| 4.2-5.8 | the loupe | a magnifier glides over dots that miss each other | quiet |
| 6.0-7.2 | in register | "them" clicks a crosshair; blue snaps; a violet ampersand appears; loupe lifts | loud hit |
| 7.2-8.5 | print run | six sheets slam in turn, each a different word pair with the same mark | rhythmic slams |
| 8.6-11.55 | the name | stack yanked away; the same pull prints the name in two halves | moderate |
| 11.7-15.0 | push in | the locked camera pushes into where two letters cross, tilts to the line, pulls back to the card | loudest near 12 s, then fades |

Sound undocumented; the column is our loudness read only.

## Signature device
The message exists only in register. Two plates share one random dot grid and one coin flip per cell: plate A inks the heads, plate B inks the tails except inside a hidden glyph, where it also inks heads. Each plate alone is the same noise; offset by a few cells they read as two clouds; only exactly aligned do the glyph's cells overlap and, with multiply blending, show a third colour. A dot circle about a third of sheet height, cells about 1 % of sheet width, the blue plate snapping home on a spring.

## Pacing read
2 fps: 4.67 "cuts" per 10 s (slams and the snap), big changes every 0.68 s, CV 0.72, 7 % quiet. Full rate: 17 % still, 27 % quiet, 12 beats, transitions at 0.5, 9.08 and 12.83 s, longest quiet run 0.83 s (a rest WARN: nothing reaches 1 s), beat CV 0.67, spread 7.6x. The one planned rest (3.6-4.2 s) is short; energy peaks at the snap (6 s) and the name (12 s). No loop.

## Look
Cream stock (#f1ebe0) on warm grey (#b1a99c, #bbbab0); fluorescent pink (#e9579f, sixth in the measured list) and riso blue (#3275a2) overprinting to violet. Heavy condensed grotesk for the big words, monospace small print, corner registration crosshairs, flat light.

## Why it works
- A puzzle (noise that must hide something) with a visible cause (the click) and an instant payoff.
- The print run lets the viewer start predicting each pair.
- Holding the camera still makes the final push feel like an event.
- Comment trigger: how does the hidden mark work.

## Steal this (grammar) / Leave this (content)
- Steal: a message that appears only when two parts align; two named cursors as characters; a locked camera until the payoff; a print-run montage of variations; one production process defining the whole look.
- Leave: the you and them pairs and all copy, the split name, the exact colours, the fictional product.

## Build it in our studio
Engine: canvas (seeded dot grid, multiply compositing, a spring snap, the loupe as a scaled clip).
1. Hidden glyph as a mask over the grid; a seeded coin per cell.
2. Render plate A and plate B with an offset.
3. Cursors pull rollers; loupe pass, snap, reveal.
4. A run of variants, the logo printed the same way, the camera's one move.
Hard part: the glyph must read on a phone: cells of 12 px or more on a 1080-wide frame and a simple shape. Zero assets.

9:16: a portrait sheet; cursors enter from top and bottom; the dot circle in the middle band; the two big words stacked.

## Business translations
- Co-branding or partnership launch (agency, b2b): two brand colours print noise until they align and the shared symbol appears.
- Wedding planner or venue (events): two first names in two inks; the ampersand appears only when the layers align.
- Team collaboration software (saas): "you" and "your team" cursors print halves of a plan that reads only when both are in.
