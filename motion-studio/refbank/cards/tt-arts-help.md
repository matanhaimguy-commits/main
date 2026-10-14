---
id: tt-arts-help
title: "A green marker whose strokes grow into real grass, drawing a smiley on a yellow street box"
url: https://www.tiktok.com/@arts_help/video/7308406020374613254
platform: tiktok
creator: arts_help
plays: 76100000
likes: 3100000
shares: 42800
saves: 270871
followers: 8000000
posted: 2023-12-03
captured: 2026-10-14
duration_s: 7
category: vfx-edit
hook: [mid-action-start, impossible-object]
devices: [transformation-sequence, assembly-build, pull-back-reveal, fooh-composite]
energy: medium
palette: [saturated]
palette_hex: ["#bca706", "#dfce32", "#57571a", "#a49f81", "#6c824b"]
sound: [diegetic-audio]
voiceover: false
text_on_screen: none
engine: [canvas, footage, gen-video]
difficulty: 3
fit: [local-service, ecommerce, real-estate, health]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 17.14
  mean_s_between_big_changes: 0.5
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.558
---

## The film in one line
A hand draws three strokes with a fat green marker on a yellow street box; each glossy stroke sprouts into dense
real-looking grass half a second after it is drawn, and the camera pulls back on a grass smiley face.

## Why it stops the scroll (first 2 s)
- 0.0 s: macro close-up of a hand pressing a chunky green marker onto glossy yellow painted metal. Already
  mid-action.
- 0.5 s: a short stroke of flat, wet-looking green paint beside the nib.
- 1.0 s: the same stroke is now a raised strip of grass, like a fuzzy caterpillar.
- 2.0 s: a second flat stroke goes down to the right; the viewer now watches for the growth.
- Mechanism: an everyday tool doing something impossible in the first second, in close-up, in real footage. No
  text. The caption adds a comment trigger: "Name this marker".

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | nib on yellow metal, hand on the right | short vertical stroke | street ambience (AI segment) |
| 0.5-1.0 | stroke flat green, then grass | stroke sprouts | ambience |
| 1.5-2.0 | marker moves right, second stroke | second flat stroke | ambience |
| 2.5 | two grass strips, the eyes | second stroke grown, camera eases back | ambience |
| 3.0-3.5 | marker swings lower left | long curved stroke starts | ambience |
| 4.0 | smile: left half grass, right half still flat paint | growth chases the nib | ambience |
| 4.5 | smile complete, hand exits | last section grows | ambience |
| 5.0-6.5 | pull back: grass smiley on a yellow street box, cobbles below, white graffiti tag | slow settle, hold | ambience |

## Signature device
Draw-then-grow: each stroke first appears as flat glossy paint, then converts into a 3D material (grass) a beat
later, so the viewer sees both states and reads the change as caused by the tool. The stroke is about nib width
(roughly 1.5 cm); the grass pile is about 1 cm tall with blades leaning randomly and pale tips, lit to match flat
daylight with a soft contact shadow. Growth lags the nib by about 0.5 s, so on the long smile stroke the grass
visibly chases the nib. Three strokes only, each a facial feature, so the shape is guessable after stroke two and
confirmed on the pull-back. Handheld phone at macro distance, widening only at the end.

## Pacing read
17.14 cuts per 10 s and a change every 0.5 s (CV 0.0) come from macro handheld motion and the hand filling the
frame; there are no edits, it is one 7 s take. The real rhythm is three draw-grow cycles of about 1.5, 1.5 and 2 s,
then a 2 s pull-back and hold on the finished face, the only rest. The 0.558 hook change is the hand and marker
dominating the frame. It ends on the still smiley; a loop restarts on the nib touching down.

## Look
- Palette: signal yellow paint (#bca706, #dfce32) fills half the frame, grass greens (#57571a, #6c824b) as hero,
  grey cobbles and sticker residue (#a49f81) as texture.
- Type: none.
- Texture and light: a real street surface with peeled stickers and graffiti, overcast daylight, fine grass
  fibres with bright tips. Camera: handheld phone, macro then medium.

## Why it works
- Impossible action in the first second, in a real place.
- Each stroke is a mini open loop closed half a second later: three loops in 5 s.
- The guessable smile pays off on the pull-back.
- "Name this marker" invites comments, and many viewers think it is real; 270 K saves.

## Steal this (grammar) / Leave this (content)
- Steal: a real hand using a normal tool that turns marks into a material; flat state first, then the material;
  growth lags the tool; few strokes forming a guessable symbol; pull back to reveal the whole.
- Leave: the smiley, the yellow box, the green marker design, the location, their footage.

## Build it in our studio
- Engine: `canvas` over a locked or lightly moving plate (client footage); `gen-video` (paid, approval) for full
  photoreal handheld.
- Plan: 1) film the client's surface with a hand drawing (or miming), phone on a tripod; 2) define each stroke as
  a spline with a start time; 3) along each spline spawn 40 to 80 blades per centimetre with seeded length, lean
  and tint; blade height follows `spring()` from 0 to full, triggered 0.5 s after the nib passes; 4) a flat
  glossy paint pass under the blades that fades as they grow; 5) pull-back as a 2D scale of plate plus overlay.
- Hard part: matching handheld motion. Use a tripod plate and add the same seeded drift to both layers, or track
  two points by hand.
- Difficulty 3: blades are simple to draw; realism lives in lighting and edge softness.

## Business translations
- Landscaping company: someone draws their phone number on a bare fence and it grows into turf.
- Eco cleaning e-commerce: a drawn leaf on a dirty tile grows into moss, then wipes away clean.
- Real estate agent: a hand draws a house outline on a plain wall and the lines sprout ivy around the new
  listing's address.
