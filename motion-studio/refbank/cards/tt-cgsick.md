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
  cuts_per_10s: 5.83
  mean_s_between_big_changes: 0.52
  change_rhythm_cv: 0.2
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.727
---

## The film in one line
A bystander on the empty Monas plaza in Jakarta finds the national monument missing (a dashed outline marks
where it stood), searches the sky, and spots ten heavy-lift helicopters carrying it away on cables toward the
new capital while people photograph it and wave goodbye.

## Why it stops the scroll (first 2 s)
- 0.0 s: cover card. Overcast skyline, a red dashed outline of the Monas obelisk where the real one should be,
  with bold white-outlined text "OTW IBUKOTA BARU? JADI NIH PINDAH!!" ("On the way to the new capital? So it
  really moved!!"), the key words in red, with comic "burst" tick marks either side.
- 0.5 s: hard cut to real phone footage: low angle over cobblestones, two women walking toward a skyline with
  no monument in it.
- 1.0 s: same walk, camera rising.
- 2.0 s: a black dashed outline of the obelisk and its base is drawn over the empty skyline, exactly where the
  monument stood.
- Mechanism: a landmark everyone in the country knows is missing. The outline turns absence into a picture and
  the headline ties it to a news story (the capital moving to IKN). The viewer has to stay to find out where it
  went. Speech in Indonesian from the camera person sounds confused about where they are.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | cover card: dashed red Monas outline, headline text | static | not described |
| 0.5-1.0 | cobbled plaza, two women walking toward the skyline | handheld walk | camera person speaks, confused (AI segment) |
| 1.5-2.5 | black dashed outline of the missing monument over the skyline | outline holds, camera drifts; a hand enters right | speech |
| 3.0-8.0 | camera tilts up into grey sky, sweeps left and right, blurred pans | searching tilt and pan | speech, someone shouts |
| 8.5-9.0 | camera swings back down; a woman points, an edge of something big enters top left | whip back | shouting, excitement |
| 9.5-12.0 | wide: the monument tipped on its side, square base with carved relief facing camera, shaft trailing left, slung under about ten twin-rotor helicopters | slow drift right to left, cables sway | speech |
| 13.0-17.0 | two women in the foreground photograph it with phones | object drifts, camera follows | Indonesian chatter |
| 18.0-20.0 | a man in black walks into frame and waves goodbye | he waves, fleet keeps drifting | speech |
| 21.0-23.5 | wide hold on the fleet over the skyline | slow drift; ends on the hold | speech |

## Signature device
Absence first, spectacle second. The film never shows the landmark in place. It opens on its absence, drawn as
a dashed outline over the real empty skyline at the exact spot and scale (base about one fifth of frame width,
tip in the upper third). Only after six seconds of searching sky does the payoff arrive: the monument, tipped
horizontal, hanging under a formation of about ten heavy-lift helicopters on long cables, about 300 to 500 m
away so it reads small enough to be believable, drifting slowly right to left with cables swaying and debris
hanging below. All of it is filmed on a handheld phone at eye level with real people in the foreground who react
as if it were a normal news day (photographing, waving goodbye). Flat overcast light makes the composite easy to
match and hides render shading.

## Pacing read
5.83 cuts per 10 s and a big change every 0.52 s are mostly the handheld camera: after the cover card there is
essentially one continuous phone take, and the "cuts" are fast tilts into the sky at 3 to 8 s. CV 0.2 means the
change is steady, not punchy. The hook change of 0.727 in the first 2 s is high because the card cuts to footage
and the outline appears. The structure is a long setup (9 s of absence and searching) and a 15 s payoff that
mostly holds still, with new people entering the foreground every 3 to 4 s to refresh the frame. It ends on the
same wide hold with no outro, so the loop goes back to the headline card.

## Look
- Palette by role: overcast sky whites and greys (#e8e9ec, #d3d7dd, #c2c7cd) fill 70% of the frame, warm grey
  cobbles (#a5a29c, #8a8782), small green strip of lawn, the monument in off-white.
- Type: cover only. Heavy rounded sans in white with a dark outline, two lines, key words in red, about 70 px
  cap height on a 1080 frame, comic burst marks. The dashed outline is a hand-drawn style stroke, about 4 px.
- Texture and light: phone footage, flat diffuse light, slight softness, no grade.
- Camera: handheld phone, eye level, walking and tilting; no zooms.

## Why it works
- Curiosity gap built on a national landmark plus a real news story: the move of Indonesia's capital.
- Delayed payoff: the absence is held for nine seconds, so the reveal feels earned and a little absurd.
- Realism cues: deadpan bystanders, phones up, waving goodbye. The comedy is in how normal they act.
- Share trigger: national pride and a topical joke; viewers tag friends and argue whether it is real.
- Loop: ends on the same hold, and the cover card restarts the question.

## Steal this (grammar) / Leave this (content)
- Steal: show the absence of something famous first (dashed outline over the empty spot); make the viewer search
  with the camera; reveal it moving away at a believable distance; deadpan bystanders photograph and wave; tie it
  to a real piece of news.
- Leave: Monas, Jakarta, the helicopters design, the Indonesian headline, the creator's footage and voices.

## Build it in our studio
- Engine: client footage (or a shot we film) plus `gen-video` (paid, approval) for the airlift; HyperFrames for
  the cover card and the dashed outline over the plate.
- Scene plan: 1) film a handheld plate of the client's real location with the thing missing (or empty space
  where it will "go"), 3 people in foreground; 2) HyperFrames overlay: an SVG dashed path drawn on with
  stroke-dashoffset at 1.5 s, locked to the plate; 3) generate the airlift as image-to-video from a still of the
  sky section of the plate; 4) cut the generated sky into the plate at a whip tilt so the seam hides in motion
  blur; 5) diegetic crowd chatter and distant rotor thump.
- Hard part: tracking the object into handheld footage. Hide it with the whip tilt, keep it far away and small,
  and use flat overcast light.
- Difficulty 4: the overlay is easy, the photoreal airlift needs paid generation and retries.

## Business translations
- Removals company: the client's own office building is gone from its street, then seen dangling under a
  fleet of drones heading for its new address.
- Restaurant moving location: a dashed outline marks the old shopfront, then the whole kitchen floats across
  town to the new street.
- Real estate developer: a dashed outline of the new tower appears on today's empty plot, and the camera pans up
  to find the building arriving by air.
