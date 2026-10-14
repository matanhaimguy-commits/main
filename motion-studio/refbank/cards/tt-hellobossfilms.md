---
id: tt-hellobossfilms
title: "A TV remote channel-surfs a cafe menu: every click swaps the item on the table"
url: https://www.tiktok.com/@hellobossfilms/video/7431929201692806433
platform: tiktok
creator: hellobossfilms
plays: 2700000
likes: 47100
shares: 38400
saves: 62112
followers: 2245
posted: 2024-10-31
captured: 2026-10-14
duration_s: 7
category: brand-ad
hook: [mid-action-start, pattern-interrupt]
devices: [match-cut, cut-on-beat, list-of-n, trending-audio, seamless-loop]
energy: high
palette: [dark, brand-colour]
palette_hex: ["#3b2720", "#101a27", "#ccb3a1", "#07070b", "#413e62"]
sound: [trending-audio, music-beat]
voiceover: false
text_on_screen: none
engine: [footage, hyperframes]
difficulty: 2
fit: [restaurant, ecommerce, local-service, health]
wow: 3
relevance: 5
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 1.17
  change_rhythm_cv: 0.47
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.098
---

## The film in one line
A locked-off shot of a round cafe table under the BÄR BAR sign: a hand points a TV remote at it and with every
click the item on the table jumps to the next menu item (smoothie, granola cup, bowl, juice, shot, sandwich) on
the beat, cycling round and round.

## Why it stops the scroll (first 2 s)
- 0.0 s: dark navy wall, purple "BÄR BAR" sign top centre, a light wooden round table, a red smoothie in a branded
  cup at left, a hand with a TV remote from the right, already aimed at the cup.
- 0.5 s: same frame; the remote is the question.
- 1.0 s: click, the smoothie becomes a granola cup in exactly the same spot.
- 1.5-2.0 s: a pink branded bowl, then an orange smoothie.
- Mechanism: an everyday gesture (zapping channels) applied to a real object, clear in one second, then repeated
  at speed. The track is a well-known synth-pop song ("Smalltown Boy"), which carries recognition on its own.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | red smoothie, remote aimed | hand still | synth-pop track starts |
| 1.0 | granola cup | swap on click | beat |
| 1.5 | pink bowl with toppings | swap | beat |
| 2.0 | orange smoothie | swap | beat |
| 2.5 | green bowl with fruit | swap | beat |
| 3.0 | small juice shot | swap; smallest item, a size joke | beat |
| 3.5 | wrapped baguette sandwich lying flat | swap | beat |
| 4.0-6.0 | the cycle restarts: red smoothie, granola, bowl, orange, green | swaps continue | AI says clicks speed up near the end |
| 6.0-7.0 | green bowl | hold to end, loops to the red smoothie | music continues |

## Signature device
Remote-control swap cut. Camera locked on a tripod at table height, the product on one marked spot in the left
third, a hand with a remote in the right third, the brand sign top centre. One clean plate per product with
nothing else moved, cut on every beat (about every 0.5 s), so only the product changes. The hand stays in frame
the whole time (held still in every take, or shot once as a constant layer), which makes the remote read as the
cause. Seven products, cycled twice; the ending lands mid-cycle so the loop is invisible.

## Pacing read
The metric reads 0 cuts and a hook change of only 0.098 because about 90% of the frame never changes and the
product area falls under the hard-cut threshold. In reality there is a swap roughly every 0.5 s, with big changes
every 1.17 s on average when a tall cup becomes a low bowl; CV 0.47 reflects similar versus different shapes. No
rests: the rhythm is constant from 1 s to the end, and with no outro it loops straight back.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 0 cuts in 7.0 s sampled (0.0 per 10 s); 0 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette: dark navy wall (#101a27), near-black shadow (#07070b), warm wood table (#ccb3a1), brown curtain
  (#3b2720), brand violet (#413e62) on the sign; the products give the colour pops.
- Type: none as overlay; the brand is on the sign and every cup.
- Light and camera: one soft key from the left, hard shadow to the right, low-key cafe mood; locked off at the
  table edge.

## Why it works
- One-second concept; the viewer stays to see the whole menu.
- Swaps on the beat feel satisfying and leave no dead time; a full menu tour in 7 s invites rewatch.
- 62 K saves and 38 K shares from a 2.2 K follower account: creators and small businesses saved it as a template
  ("creative ways to make commercials").
- No end card, so views stack on the loop.

## Steal this (grammar) / Leave this (content)
- Steal: a locked-off product stage, one marked spot, a cause-object held in frame (remote, finger tap, bell, pen
  click), a swap on every beat, the full range cycled, ending mid-cycle.
- Leave: BÄR BAR, their cups, menu and sign, the remote gag framed exactly like this, and "Smalltown Boy" (use
  licensed or generated music with a clear 4/4 beat).

## Build it in our studio
- Engine: client footage (7 to 10 locked-off phone plates, one per product) edited in HyperFrames, or HyperFrames
  with real product cut-out photos over one plate.
- Plan: 1) music first, `beats.py` for the beat grid; 2) one product layer per beat; 3) hand-and-remote layer
  constant on top; 4) optional 2-frame scale pop (1.00 to 1.03) per swap; 5) a soft click under the music.
- Hard part: consistency between plates. Tape the spot, lock exposure and white balance, shoot all items in one
  session; for cut-outs, draw a matching contact shadow.
- Difficulty 2: simple to build; the quality lives in the shoot.

## Business translations
- Restaurant or cafe: the full menu zapped on a table with a remote, ending on the new seasonal item.
- Skincare e-commerce: a finger tap on a bathroom shelf swaps through the whole range.
- Hair salon: a pen click at a mirror jumps the reflection through each style on offer, one per beat, with real
  clients who agreed to it.
