---
id: tt-hati-hati-mas
title: "A tagged box on a subway platform comes alive, lolls out a giant tongue and pops its eyeballs onto the floor"
url: https://www.tiktok.com/@hati.hati.mas/video/7148302966120877318
platform: tiktok
creator: hati.hati.mas
plays: 62700000
likes: 4300000
shares: 95200
saves: 316367
followers: 363100
posted: 2022-09-28
captured: 2026-10-14
duration_s: 11
category: cgi-fooh
hook: [pattern-interrupt, impossible-object]
devices: [creature-reveal, softbody, fooh-composite, pov-camera]
energy: high
palette: [natural, saturated]
palette_hex: ["#88796e", "#a6978b", "#2c2220", "#575245", "#802745"]
sound: [diegetic-audio]
voiceover: false
text_on_screen: none
engine: [canvas, footage, gen-video]
difficulty: 3
fit: [restaurant, ecommerce, events, agency]
wow: 5
relevance: 3
pacing:
  cuts_per_10s: 19.09
  mean_s_between_big_changes: 0.5
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.641
---

## The film in one line
On a subway platform (the hashtags point to Hamburg) a grey utility box covered in graffiti, with two googly
eyes on top, drops its front panel like a jaw, flops a giant glossy pink tongue onto the tiles and keeps popping
its eyeballs out as pink balls that bounce across the platform while a train pulls away behind it.

## Why it stops the scroll (first 2 s)
- 0.0 s: handheld view of a platform: green pillar, departure board, a red and white train, and a tagged grey
  box with two cartoon googly eyes. A face on an object is already a small hook.
- 0.5 s: same; nothing happens yet.
- 1.0-1.5 s: the front panel is gone, a dark mouth opens and a fat pink tongue bulges out; the eyes bulge.
- 2.0 s: the tongue slaps down to the bottom left corner and both eyeballs burst out as glossy pink balls.
- Mechanism: pattern interrupt in a mundane real place. The face was there from frame one, so when it moves it
  feels "always alive"; the gross-cute tongue and popping eyes add physical comedy.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | platform, train, tagged box with googly eyes | handheld drift | sound not described in AI segments |
| 1.0-2.0 | panel becomes a mouth; tongue bulges, then slaps the floor; both eyes pop out | stretch, two balls launch | not described |
| 2.5-4.0 | new eyes appear; camera pushes in, tongue whips toward the lens | wobble, motion blur | not described |
| 5.0-7.0 | more eyeballs spill onto the tiles; train gone, a burger billboard revealed | camera swings, settles | not described |
| 8.0-9.0 | tongue pulls back and slaps out again; another pair pops | repeat | not described |
| 10.0-10.5 | tongue curls up, balls roll away | ends mid-wiggle | not described |

## Signature device
A real street object becomes a creature using a face that was already on it. The box is about 1.6 m tall; the
googly eyes (each about a fifth of its width) read as street art for the first second. At 1.0 s the front panel
becomes a mouth and a tongue about 3 m long unrolls as a soft body: glossy magenta with darker veins and a wet
highlight, heavy at the tip so it slaps and drags on the tiles. The eyes bulge, then pop out as bouncy pink
eyeballs with irises that bounce three or four times and stay on the floor while new eyes appear. The cycle
repeats every 3 to 4 s and the eyeball pile grows. Handheld phone walking in and around the box.

## Pacing read
19.09 cuts per 10 s and a change every 0.5 s (CV 0.0) are a moving handheld camera plus a big deforming object;
there are no edits, it is one 11 s take. No rests after the 1 s setup, with peaks at 2.0 s (first slap and pop),
3.5 to 4.0 s (tongue toward the lens) and 8.5 s (second pop). The growing eyeball pile is the escalation. It ends
mid-wiggle, so a loop back to the calm opening feels like a reset.

## Look
- Palette: beige and grey tiles (#88796e, #a6978b), dark box (#2c2220, #575245), the creature's magenta (#802745
  in shade) as the only saturated colour.
- Type: none. Light: cold fluorescent; glossy speculars separate the creature from the matte real world.

## Why it works
- Pareidolia primes the viewer from frame one; payoff at 1 s; slapstick needs no language.
- Constant escalation as eyeballs pile up; real train, ad and platform keep it believable.
- An ongoing art character builds a following; 316 K saves; the mid-wiggle ending invites rewatch.

## Steal this (grammar) / Leave this (content)
- Steal: give a real object in the client's space a face that is visible before anything moves; let one part
  become an overgrown soft body that interacts with the floor; repeat with growing debris; keep the real world
  alive around it.
- Leave: the artist's Hati-Hati character and googly-eye mark, the tongue-and-eyeballs gag, the subway, the ad.

## Build it in our studio
- Engine: `canvas` over a locked or slowly moving plate; `gen-video` (paid, approval) for photoreal handheld.
- Plan: 1) film the client's object (vending machine, letterbox, shop door) locked off for 11 s with life around
  it; 2) the soft part as a verlet chain of 20 to 30 points with gravity, floor collision and stiffness, drawn as
  a thick shaded ribbon with a specular stripe; 3) balls with a damped `spring()` bounce, shaded sphere and iris;
  4) repeat every 3.5 s with seeded variation; 5) slap and boing SFX from the event times.
- Hard part: a 2D soft body reading as glossy 3D on footage. Two-tone gradient across the ribbon, a moving
  highlight, a soft floor shadow and renderer motion blur.
- Difficulty 3 for a locked plate; 4 or more for handheld photoreal.

## Business translations
- Snack or drinks brand: their vending machine in a station blinks, opens its flap and spits bouncing cans
  across the floor.
- Restaurant: the letterbox gets eyes, flops out a giant menu like a tongue, and cartoon meatballs bounce onto
  the pavement.
- Events agency: a photo booth opens its curtain like a mouth and confetti eyeballs bounce across the dance floor.
