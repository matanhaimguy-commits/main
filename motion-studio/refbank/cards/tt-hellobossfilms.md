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
- 0.0 s: dark navy wall, purple "BÄR BAR" sign top centre, a light wooden round table, a red smoothie in a
  branded cup at left, a hand with a TV remote entering from the right, already aimed at the cup.
- 0.5 s: same frame, the smoothie still there; the remote is the question: what will it do?
- 1.0 s: click, the smoothie is replaced by a granola yogurt cup in exactly the same spot.
- 1.5 s: click, a pink branded bowl. 2.0 s: an orange smoothie.
- Mechanism: an everyday gesture (zapping channels) applied to a real object, so the product "changes channel".
  The idea is clear in one second and then repeats at speed. The music is a well-known synth-pop track
  ("Smalltown Boy"), which carries recognition on its own.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | red smoothie in branded cup, remote aimed | hand holds still | trending synth-pop track starts |
| 1.0 | granola cup | swap on click | beat |
| 1.5 | pink bowl with toppings | swap | beat |
| 2.0 | orange smoothie | swap | beat |
| 2.5 | green bowl with fruit on top | swap | beat |
| 3.0 | small juice shot | swap; smallest item, a size joke | beat |
| 3.5 | wrapped baguette sandwich lying flat | swap | beat |
| 4.0-6.0 | red smoothie, granola, bowl, orange smoothie, green bowl again | the cycle restarts | music continues; AI says the clicks speed up near the end |
| 6.0-7.0 | green bowl | hold to end, loops back to the red smoothie | music continues |

## Signature device
Remote-control swap cut. Camera locked on a tripod at table height, 50 mm-ish framing, the product placed on one
marked spot at the left third of the table, a hand with a remote in the right third, the brand sign top centre.
Shoot one clean plate per product without moving anything else, then cut between them on every beat of the
music (about every 0.5 s), so the only thing that changes is the product. The hand stays in frame the whole
time (shot once and kept as a constant layer, or held still in every take), which makes the remote read as the
cause. Seven products, cycled twice; the ending lands mid-cycle so the loop is invisible.

## Pacing read
The metric reads 0 cuts and a hook change of only 0.098 because the frame is about 90% identical and only the
product area changes, which falls under the hard-cut threshold. In reality there is a swap roughly every 0.5 s
(one per beat at our sampling rate), with big changes every 1.17 s on average when a tall cup becomes a low bowl.
CV 0.47 reflects that some swaps are similar in shape (cup to cup) and some are not. There are no rests: the
rhythm is constant from 1 s to the end, and the ending has no outro, so it loops straight back to the start.

## Look
- Palette by role: dark navy wall (#101a27) and near-black shadows (#07070b), warm wood table (#ccb3a1) with a
  brown-wood curtain behind (#3b2720), brand violet (#413e62) on the sign; the products give the colour pops
  (red, orange, green, pink).
- Type: none as overlay. The brand appears on the sign and on every cup.
- Texture and light: one soft key from the left, hard shadow on the table to the right, moody low-key cafe look.
- Camera: locked off, eye level with the table edge, no movement at all.

## Why it works
- One-second concept: the viewer gets the joke instantly and stays to see the whole menu.
- Fast swaps on the beat feel satisfying and leave no dead time.
- It works as a complete menu tour in 7 s; viewers rewatch to see each item.
- High saves (62 K) and shares (38 K) from a 2.2 K follower account: other creators and small businesses saved it
  as a template idea ("creative ways to make commercials").
- The loop has no end card, so the views stack.

## Steal this (grammar) / Leave this (content)
- Steal: locked-off product stage, one marked spot, a cause-object (remote, tap of a finger, a bell, a click of a
  pen) held in frame, a swap on every beat, the full range cycled, ending mid-cycle for the loop.
- Leave: BÄR BAR, their cups, menu and sign, the remote gag exactly as framed, and the "Smalltown Boy" track
  (use licensed or generated music with a clear 4/4 beat).

## Build it in our studio
- Engine: `footage` (the client shoots 7 to 10 locked-off plates on a phone tripod, one per product) edited in
  HyperFrames; or HyperFrames with real product cut-out photos over one plate.
- Scene plan: 1) get the music first and run `beats.py` for the beat grid; 2) build a HyperFrames timeline
  where each beat shows the next product layer; 3) keep the hand-and-remote layer constant on top; 4) optional
  tiny 2-frame scale pop (1.00 to 1.03) on each product to sell the click; 5) a soft click SFX on each swap
  under the music.
- Hard part: consistency between plates (lighting, position, shadow). Mark the spot with tape, lock exposure and
  white balance, and shoot all items in one session; for cut-outs, draw a matching contact shadow.
- Difficulty 2: simple to build; the quality lives in the shoot.

## Business translations
- Restaurant or cafe: the full menu zapped on a table with a remote, ending on the new seasonal item.
- E-commerce skincare brand: a finger tap on a bathroom shelf swaps through the whole product range.
- Local hair salon: a hand clicks a pen at a mirror and the client's reflection jumps through each style on
  offer, one per beat (with real clients who agreed to it).
