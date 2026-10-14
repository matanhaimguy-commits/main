---
id: tt-cgsick
title: "Jakarta's Monas monument is gone, then spotted being airlifted away by a fleet of helicopters"
url: https://www.tiktok.com/@cgsick_/video/7351633687462546690
platform: tiktok
creator: cgsick_
plays: 76600000
likes: 2600000
shares: 84000
saves: 155532
followers: 55300
posted: 2024-03-30
captured: 2026-10-14
duration_s: 24
category: cgi-fooh
hook: [question, impossible-object]
devices: [fooh-composite, pov-camera, scribble-annotation, reaction-shot]
energy: medium
palette: [natural, mono]
palette_hex: ["#d3d7dd", "#e8e9ec", "#c2c7cd", "#a5a29c", "#8a8782"]
sound: [diegetic-audio]
voiceover: false
text_on_screen: headline
engine: [gen-video, footage, hyperframes]
difficulty: 4
fit: [local-service, real-estate, events, restaurant]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 0.42
  mean_s_between_big_changes: 0.52
  change_rhythm_cv: 0.2
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.727
---

## The film in one line
A bystander on the Monas plaza in Jakarta finds the national monument missing (a dashed outline marks where it
stood), searches the sky, and spots about ten heavy-lift helicopters carrying it away on cables while people
photograph it and wave goodbye.

## Why it stops the scroll (first 2 s)
- 0.0 s: cover card over the overcast skyline: a red dashed outline of the obelisk and the headline "OTW IBUKOTA
  BARU? JADI NIH PINDAH!!" ("On the way to the new capital? So it really moved!!"), key words in red.
- 0.5-1.0 s: cut to phone footage: cobbled plaza, two women walking toward a skyline with no monument.
- 2.0 s: a black dashed outline of the obelisk is drawn exactly where it used to stand.
- Mechanism: a landmark the whole country knows is missing. The outline turns absence into a picture and the
  headline ties it to real news (the capital moving to IKN). The camera person sounds confused (AI segment).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | cover card: red outline, headline | static | not described |
| 0.5-1.0 | plaza, two women walking | handheld walk | confused speech in Indonesian |
| 1.5-2.5 | dashed outline of the missing monument over the skyline | outline holds, camera drifts | speech |
| 3.0-8.0 | camera tilts into grey sky, sweeps left and right | searching tilt and pan | someone shouts |
| 8.5-9.0 | camera swings down, a woman points, something big enters top left | whip back | excited shouting |
| 9.5-12.0 | the monument tipped on its side under a helicopter formation | slow drift, cables sway | speech |
| 13.0-17.0 | two women photograph it | object drifts, camera follows | chatter |
| 18.0-20.0 | a man walks in and waves goodbye | wave | speech |
| 21.0-23.5 | wide hold on the fleet over the skyline | slow drift; ends on the hold | speech |

## Signature device
Absence first, spectacle second. The landmark is never shown in place: its absence is drawn as a dashed outline
over the real empty skyline at the exact spot and scale. Only after six seconds of searching sky does the payoff
arrive: the monument, tipped horizontal (square base with its carved relief toward camera, shaft trailing left),
slung under a formation of about ten twin-rotor helicopters on long cables, far enough away (a few hundred
metres) to read small and believable, drifting right to left with debris hanging below. Real people in the
foreground react as if it were a normal news day. Flat overcast light makes the composite easy to match.

## Pacing read
5.83 cuts per 10 s and a big change every 0.52 s are mostly handheld motion: after the cover card it is one phone
take, and the "cuts" are fast tilts into the sky. CV 0.2 means steady change. The 0.727 hook change is the card
cutting to footage plus the outline. Structure: 9 s of absence and searching, then a 15 s payoff that mostly holds,
refreshed by a new person entering the foreground every 3 to 4 s. It ends on the hold, so the loop returns to the
headline card.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 1 cuts in 24.0 s sampled (0.42 per 10 s), at 0.5 s; 14 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette: overcast whites and greys (#e8e9ec, #d3d7dd, #c2c7cd) fill most of the frame, warm grey cobbles
  (#a5a29c, #8a8782), a strip of green lawn, the monument in off-white.
- Type: cover only, heavy rounded sans in white with a dark outline, key words red, comic burst marks; the
  outline is a hand-drawn style stroke about 4 px wide.
- Camera: handheld phone at eye level, walking and tilting, no zooms, no grade.

## Why it works
- Curiosity gap built on a national landmark plus a topical story.
- The absence is held for nine seconds, so the reveal feels earned and absurd.
- Deadpan bystanders (phones up, waving goodbye) make it funny and believable.
- National pride and a topical joke drive tags and "is it real" arguments.

## Steal this (grammar) / Leave this (content)
- Steal: show the absence of something famous first; make the viewer search with the camera; reveal it moving
  away at a believable distance; deadpan bystanders; tie it to real news.
- Leave: Monas, Jakarta, the helicopter design, the Indonesian headline, the creator's footage and voices.

## Build it in our studio
- Engine: client footage plus `gen-video` (paid, approval) for the airlift; HyperFrames for the cover card and the
  dashed outline.
- Plan: 1) handheld plate of the client's real location with the thing absent, people in the foreground; 2) an
  SVG dashed path drawn on with stroke-dashoffset at 1.5 s, locked to the plate; 3) generate the airlift
  image-to-video from a sky still of the plate; 4) cut the generated sky in at a whip tilt so the seam hides in
  motion blur; 5) crowd chatter and distant rotor thump.
- Hard part: tracking into handheld footage. Hide it in the whip tilt, keep the object far away, use flat light.
- Difficulty 4: the overlay is easy, the photoreal airlift needs paid generation and retries.

## Business translations
- Removals company: the client's office is gone from its street, then seen hanging under drones heading for its
  new address.
- Restaurant moving location: a dashed outline marks the old shopfront, then the whole kitchen floats across town.
- Real estate developer: a dashed outline of the new tower on today's empty plot; the camera tilts up to find the
  building arriving by air.
