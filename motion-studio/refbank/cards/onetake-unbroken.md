---
id: onetake-unbroken
title: "The same hour drawn twice as a brush circle: broken by notifications on one side, whole on the other"
url: references/onetake/cases/unbroken-15s/
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
category: explainer-2d
hook: [contrast-split]
devices: [split-screen, before-after, versus-compare, counter-ticker, pull-back-reveal]
energy: calm
palette: [dark, mono]
palette_hex: ["#131419", "#101115", "#191920", "#0e0f13", "#9c9891"]
sound: [sfx-heavy, silence-moments]
voiceover: false
text_on_screen: headline
engine: [canvas]
difficulty: 3
fit: [saas, health, finance, personal-brand, any]
wow: 3
relevance: 5
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 5.0
  change_rhythm_cv: 0.67
  quiet_share_2fps: 0.241
  hook_change_0_2s: 0.01
---

## The film in one line
On black, a thin rule splits the frame and an ivory brush starts the same circle on both sides, but on the left small notification chips keep popping up and each one lifts the brush, leaving a ring of 17 broken fragments, while the right side finishes one unbroken circle; the left half falls away, the camera pulls back, and the circle becomes the o in the product name, followed by a short tagline and a small red seal.

Craft reference, not a social post: a 16:9 film for a fictional notification-holding Mac app from the onetake repo. Study only (PolyForm Noncommercial): ideas in our words, no code, text, pixels or sound reused.

## Why it stops the scroll (first 2 s)
At 0.0-0.5 s black with faint vertical brush texture as a rule begins to draw down the middle; at 1.0 s tiny labels top each half; at 1.5-2.0 s two brush tips touch down in step. Mechanism: a contrast split, the same action under two conditions, so the viewer waits to see which side wins. Very quiet open (hook change 0.01); the premise is clear only by about 3 s, when the first ping breaks the left stroke.

## Beat map
| t (s) | on screen | what moves | sound (our loudness read) |
|---|---|---|---|
| 0.5-1.4 | the split | rule draws; labels appear | near silence |
| 1.4-2.25 | brushes down | two strokes start in step | brush texture rising |
| 2.25-7.1 | the pings | 17 chips appear on the left, coming faster; each lifts the brush, which restarts a little behind; an "interrupted" counter climbs; the right keeps going | steady level with pings |
| 7.4 | the hour ends | right closes its circle with a "finished" label | a hit |
| 7.4-8.45 | held breath | nothing moves | drops |
| 8.45-9.7 | left falls away | fragments drop, the rule retracts, the camera finds the circle | low |
| 9.7-11.2 | the name | pull back about 6.7x; the circle is the o; letters rise around it | rise, then near silence |
| 11.6-15.0 | tagline | a short imperative line; a red seal stamps | loud hit near 12 s, fade |

Sound undocumented; the column is our loudness read only.

## Signature device
Before and after on a split screen with one shared clock. Both halves run the same timeline; only the left receives interruptions. Each interruption is a chip popping beside the stroke, a small shake on the left half only, and the brush lifting and resuming slightly behind, so strokes get shorter as pings quicken. The brush is procedural: dozens of fine bristle lines along the path with seeded dry-brush gaps, ivory on black. The finished circle is the o of the logo; a pull-back from 1x to about 0.15x turns the hero object into a letter.

## Pacing read
2 fps: 0 cuts, big changes every 5.0 s, CV 0.67, 24 % quiet. Full rate: 24 % still, 61 % quiet (the highest in the set), 3 beats, no transitions, longest quiet run 2.17 s, beat CV 0.87, spread 17.3x (the widest). The case notes warn that stillness metrics over-read on dark grounds. Shape: one long build (the hour), one held breath, one reveal. Restraint looks premium but is slow for a feed. No loop.

## Look
Ink-black ground (#0e0f13 to #191920) with faint vertical streaks, bone-white brush (#9c9891 in its shadows), small dark chips with a cold blue dot, one vermilion seal. Thin monospace labels (too small for a phone), a light rounded grotesk wordmark.

## Why it works
- Almost everyone knows the interrupted-work feeling: high relatability, a "this is me" share.
- The split turns the product's benefit into a picture rather than a claim; the counter makes it a score.
- The circle becoming a letter is a satisfying reveal; the tagline is an instruction that matches the image.

## Steal this (grammar) / Leave this (content)
- Steal: the same task drawn twice, with and without the product, on one clock; interruption as a physical event that breaks a stroke; the finished object becomes a letter of the name; a held breath before the reveal.
- Leave: the ensō, the brush look as designed, the copy, the fictional app, the seal.

## Build it in our studio
Engine: canvas (seeded bristle strokes, path-length reveal, per-half shake).
1. Split, labels, one shared path for both halves.
2. An interruption schedule that quickens, each event breaking the left stroke; counter.
3. Hold, drop the left half.
4. Pull back into the logo word and tagline.
Hard part: brushwork that looks hand-made at 60 fps (thin bristles with pressure and dry gaps along the path, all seeded). Zero assets.

9:16: split top and bottom instead of left and right; each half a band of about 1080 x 650 inside the safe zone; circles at about 45 % of width; labels at 44 px or more; logo lands in the middle band. Relevance 5: before and after transfers to almost any business.

## Business translations
- Bookkeeping firm (finance): the same month drawn as a line twice; the top keeps stopping for missing receipts, the bottom runs clean and becomes a letter of the firm's name.
- Physiotherapy clinic (health): the same walk drawn as a line, one broken by pain markers, one smooth; the smooth line resolves into the clinic's mark.
- Focus coach (personal-brand): interrupted versus uninterrupted work blocks, ending on the coach's own logo and a real offer.
