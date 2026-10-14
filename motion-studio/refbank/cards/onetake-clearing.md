---
id: onetake-clearing
title: "One unbroken zoom from a full year down to the one free half hour, and back"
url: references/onetake/cases/clearing-15s/
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
hook: [beautiful-first-frame, text-headline]
devices: [zoom-through-scale, one-take-camera, whip-pan, grid-mosaic, silence-before-hit]
energy: medium
palette: [saturated]
palette_hex: ["#616cdc", "#2a3ad0", "#3646db", "#2231c1", "#8d94e0"]
sound: [sfx-heavy, silence-moments]
voiceover: false
text_on_screen: headline
engine: [canvas, hyperframes]
difficulty: 3
fit: [saas, health, local-service, finance, real-estate]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 4.0
  mean_s_between_big_changes: 0.83
  change_rhythm_cv: 1.11
  quiet_share_2fps: 0.172
  hook_change_0_2s: 0.096
---

## The film in one line
A year of tiny calendar squares fills an electric blue field, the camera dives into one fully booked day, finds its only free half hour, lands a yellow "Clear." block in it, then whips back out so the kept days spell the product name across the year.

Craft reference, not a social post: a 16:9 film for a fictional calendar app from the onetake repo. Study only (PolyForm Noncommercial): ideas in our words, never its code, text, sound or pixels.

## Why it stops the scroll (first 2 s)
At 0.0 s an empty blue field; at 0.5 s rows of small squares wipe in; at 1.0 s the full year is there and a header types the year, an event count and "0 hours free"; at 2.0 s the frame falls into one cell. Mechanism: a pain statement written as data, then a scale shock. The first second is calm (hook change 0.096).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-1.8 | year grid, header | cells pop in as a wave; header types | rising ticks, one marimba note |
| 1.8-3.6 | dive into one day | zoom 1x to 40x; meetings resolve | air as loud as the zoom speed |
| 3.6-4.8 | the schedule | a yellow scan line slows onto a dashed empty slot | sinking tone, ticks |
| 4.8-5.6 | the gap | held breath | a bell, then silence |
| 5.6-7.6 | into the half hour | 50x to 300x; a minute ruler draws | deeper air, sparse ticks |
| 7.6-9.0 | "Clear." lands | yellow block drops in, then dead still | soft heavy hit, held chord |
| 9.0-10.4 | whip out | 300x to 1x in about 0.6 s, full smear | widest air, whoosh |
| 10.4-11.7 | the name | yellow cells ripple out and spell the name | a climbing note per cell |
| 11.9-15.0 | end card | tagline; one cell pulses | keys, a bell |

Sound per the case notes (no music).

## Signature device
Nested zoom with no cuts. Three levels drawn in their own units: a 52 x 7 year grid, one day as a full page scaled into its cell, one half hour as a page inside the day. One zoom value spans 1x to 300x, eased in log space, and the camera tracks the target's screen position rather than its world position, so it settles the same at every depth. Detail fades in by on-screen size (hours first, titles later, the ruler only at extreme depth). The found slot sits inside a letter of the name laid over the grid, so the find becomes the logo.

## Pacing read
2 fps: 4.0 "cuts" per 10 s, but these are the dives and the whip, not edits; big changes every 0.83 s, uneven (CV 1.11), 17 % quiet. Full rate: 21 % still, 30 % quiet, 6 beats, transitions at 2.75 and 9.08 s, longest quiet run 1.92 s, beat CV 0.61, spread 8.7x. Shape: fill, plunge, scan, held breath, deeper plunge, dead-still landing (the loudest moment), whip, ripple, 3 s still end. Holds are truly frozen (slow pushes failed their first render). No loop.

## Look
Electric blue ground (#2a3ad0 to #616cdc), white cells at partial opacity, one warm yellow accent (not in the measured top five) only for the slot, block and name. Grotesk labels, monospace times. Flat.

## Why it works
- Open loop: "0 hours free" plus a dive asks what it is looking for; the slot answers at 4.8 s.
- Escalation by depth: the second dive goes further.
- The payoff is a still, quiet frame after fast moves: relief, the product promise.
- The yellow you followed becomes the logo, which invites a rewatch.

## Steal this (grammar) / Leave this (content)
- Steal: problem as dense data; a dive through nested scales to the one thing that matters; freeze on the find; whip back and let it become the logo; silence around the single landing.
- Leave: the blue and yellow pairing, the calendar layout, the pixel-font name, the copy, the score, all code.

## Build it in our studio
Engine: canvas (subframe blur sells the whip; crisp type at 300x needs our own transforms).
1. Each level a page in its own coordinates under one composed transform.
2. Log-zoom spring with a screen-space anchor; seek every 0.1 s to prove the target stays in frame.
3. Detail fades keyed to on-screen size.
4. Landing, a frozen 1 s hold, the whip as a step in the zoom target.
5. Ripple the name's cells from the found cell; place sound from exported zoom speed.
Hard part: sharp text at depth; draw every level in its own units, never scale bitmaps. No paid steps.

9:16: turn the year to 7 columns x 52 rows (or one month); a day page is already portrait. Keep slot and name in the middle band, clear of the top 250 px and bottom 400 px.

## Business translations
- Clinic or salon (health, local-service): a month of booked cells, dive to the one open slot, "Book it" lands, back out to the brand mark.
- Bookkeeping firm (finance): a year of transaction rows, dive into one flagged line, back out to the logo built from cleared rows.
- Real estate agency: a city grid of lots, dive into one listing, back out so the agency's pins outline its logo.
