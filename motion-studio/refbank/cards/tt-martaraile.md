---
id: tt-martaraile
title: "A green-screen phone slid over a closed shoebox becomes an X-ray window onto the shoes inside"
url: https://www.tiktok.com/@martaraile/video/7643918901503347990
platform: tiktok
creator: martaraile
plays: 3800000
likes: 179300
shares: 22800
saves: 118250
followers: 70000
posted: 2026-05-25
captured: 2026-10-14
duration_s: 19
category: vfx-edit
hook: [wait-for-it, text-headline]
devices: [x-ray-cutaway, mask-reveal, before-after, screen-in-frame]
energy: medium
palette: [natural, light]
palette_hex: ["#aea79e", "#121211", "#2a2622", "#c4c5c4", "#918277"]
sound: [trending-audio]
voiceover: false
text_on_screen: headline
engine: [footage, canvas, hyperframes]
difficulty: 2
fit: [ecommerce, restaurant, real-estate, local-service]
wow: 3
relevance: 5
pacing:
  cuts_per_10s: 1.58
  mean_s_between_big_changes: 0.83
  change_rhythm_cv: 0.94
  quiet_share_2fps: 0.108
  hook_change_0_2s: 0.246
---

## The film in one line
A creator shows how she makes a product shot: she films a closed shoebox while sliding a phone with a solid green
screen across its lid, films the opened box from the same locked tripod, chroma-keys the green in a phone editor,
and the result is a phone that works like an X-ray window, showing the shoes inside the closed box as it slides.

## Why it stops the scroll (first 2 s)
- 0.0 s: wide shot of a bright room: white wardrobe doors, a boucle armchair with a white shoebox on it, a phone on
  a tripod in the foreground, a woman kneeling right, reaching out with a phone whose screen is solid green. Bold
  white uppercase "WHAT I DO" with "STEP 1" small beneath, upper third.
- 0.5-1.5 s: she slides the green phone left to right across the lid. Nothing else moves.
- 2.0 s: cut closer, behind the tripod, the green rectangle now big in frame.
- Mechanism: an odd action (why wave a green phone over a box?) plus a numbered process that promises a payoff
  labelled "what you see". The caption says "Another product video idea you can steal".

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-1.5 | wide BTS: tripod phone, shoebox on chair, green phone; "WHAT I DO / STEP 1" | hand slides green phone across lid | trending synth-pop track |
| 2.0-3.5 | closer behind the tripod, tripod phone screen shows the take | green phone slides back and forth | music |
| 4.0 | wide again, she pulls her arm back | settle | music |
| 4.5-6.5 | "STEP 2": tight on the box, hands lift the lid, brown leather loafers revealed | lid lifts and leaves frame, then a still hold | music |
| 7.0-9.5 | "STEP 3": screen recording of a phone editor, open-box clip on the main track, green-phone clip added as overlay | timeline scrolls, overlay track appears | music |
| 10.0 | effects menu: auto removal, custom removal, chroma key | tap | music |
| 10.5-13.5 | chroma key panel: colour picker on the green, sliders for intensity, shadow, feather edge, clean up edge | sliders drag, green turns see-through | music |
| 14.0-19.0 | "WHAT YOU SEE": the closed box, a hand slides a phone across the lid and its screen shows the shoes inside | phone slides left, right and back; the inside view moves with it | music to the end |

## Signature device
The see-through phone. Two takes from one locked camera: take A, the closed box with a hand sliding a phone that
shows a full-screen pure green image across the lid (about 0.5 to 1 s per pass, slight tilt); take B, the box open
with the product arranged inside, nothing moving. Take B goes on the base track and take A on top, then the green
is keyed out, so the phone's screen becomes a hole through the lid into take B. Because both plates share the
same camera position, the product sits exactly where it would be under the lid, and the phone bezel, the hand and
the reflections make the window feel physical. The phone covers about one third of the lid width, so the viewer
only sees part of the product at a time, which makes them follow it.

## Pacing read
5.26 cuts per 10 s with a big change every 0.83 s and CV 0.94 shows an uneven rhythm: quick step cards and cuts in
the first 7 s, then slow screen-recording time in the editor (quiet share 0.108, longest quiet 2 s while the
chroma panel is adjusted), then a 5 s continuous result shot. The hook change is low (0.246) because the opening
is a held wide with one moving hand. Energy peaks at the reveal of the result, which is the longest single shot,
and it ends mid-slide with no outro, so it loops back to step 1.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 3 cuts in 19.0 s sampled (1.58 per 10 s), at 6.5, 8.5, 14.0 s; 10 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette by role: warm off-white room and chair (#aea79e, #c4c5c4), dark editor UI (#121211, #2a2622), brown
  leather product (#918277), the key green only in the BTS steps.
- Type: heavy geometric sans, all caps, white with a soft shadow, about 70 px cap height on a 1080 frame for
  "WHAT I DO", step number about 35 px under it; same position in every step.
- Light: soft warm practical light (a bulb lamp and flowers behind), no hard shadows, which helps the key.
- Camera: locked tripod for the plates; a slightly closer BTS angle for step 1.

## Why it works
- Save trigger: a technique people can copy for their own or client videos (118k saves, 3% of plays).
- Process then payoff: the steps build an open loop that only closes in the last 5 s.
- Real, cheap tools make it feel doable, which drives shares to other creators.
- The reveal itself is satisfying: the hidden product appears exactly where it should be.

## Steal this (grammar) / Leave this (content)
- Steal: the keyed "window" that lets the viewer see inside packaging, a room, a device or a wall; locked camera
  for two plates; the "What I do / What you see" BTS format with numbered steps.
- Leave: the shoe brand and box, her room and styling, her caption and the track.

## Build it in our studio
- Engine: client footage plus our compositing (ffmpeg chromakey or HyperFrames layering), or a 2D canvas version
  where an illustrated phone shape is a mask over a cutaway layer.
- Scene plan: 1) the client films two locked-off plates of their product (closed and open), plus the green phone
  pass on the closed plate; 2) we key the green with ffmpeg (chromakey, similarity about 0.15, blend 0.05) over
  the open plate; 3) optional BTS: the client films the steps on a phone and we add the step cards in HyperFrames;
  4) end on the clean result loop.
- Hard part: exposure and position must match between plates; any tripod bump breaks it. Fix by shooting both in
  one session, locking exposure, and using a 2D offset in the composite if needed.
- Difficulty 2: easy if the client follows a one-page shoot sheet; the 2D version is difficulty 1.

## Business translations
- E-commerce skincare: a phone slides over a sealed gift box and shows the products packed inside.
- Real estate: a phone held up to a closed front door shows the renovated living room behind it.
- Bakery: a phone slid over a closed cake box reveals the decorated cake, then the box opens for real.
