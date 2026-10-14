---
id: tt-vaporama-vision
title: "A swimmer's-eye float through an endless tiled poolroom, past a black drop-off and eye graffiti, toward a playground it never reaches"
url: https://www.tiktok.com/@vaporama_vision/video/7433431479041985825
platform: tiktok
creator: vaporama_vision
plays: 95400000
likes: 6800000
shares: 826600
saves: 566378
followers: 985600
posted: 2024-11-04
captured: 2026-10-14
duration_s: 60
category: spectacle-world
hook: [beautiful-first-frame, scale-shock]
devices: [pov-camera, liquid-sim, escalation-ladder]
energy: calm
palette: [mono, pastel]
palette_hex: ["#627f90", "#8499a9", "#4b6575", "#2f4451", "#b8c5cf"]
sound: [diegetic-audio]
voiceover: false
text_on_screen: none
engine: [hyperframes, gen-video, canvas]
difficulty: 4
fit: [local-service, real-estate, events, agency]
wow: 5
relevance: 2
pacing:                               # 1.5 s sampling, 40 frames cover the full 60 s
  cuts_per_10s: 1.0
  mean_s_between_big_changes: 1.5
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.692
---

## The film in one line
A camera floats at water level through a vast white-tiled pool hall lit by thousands of tiny lights, along the line
where a bright shallow shelf drops into black water. It passes floating balls and walls filling with ink eyes, then
dips into the dark water, always facing a colourful water playground it never reaches.

## Why it stops the scroll (first 2 s)
- 0.0 s: a wide fisheye view at water level. A turquoise shallow shelf fills the lower third and ends in a curved
  edge. Beyond it lie black deep water, a wall of white light points and a tiny playground at dead centre, with a
  blue ball floating.
- 1.5-2.0 s: the camera has drifted closer to the edge, and the black water fills the middle of the frame.
- No on-screen text. The post caption reads "Don't go too near the edge", and the edge is in the first frame.
- Mechanism: a familiar place (a public pool) shown empty, too big and too clean. The drop to black water triggers
  a fear of deep water before anything happens.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-3 | the shelf, the black water, the light wall, the playground, a blue ball | slow drift toward the edge | pool ambience; the caption credits a track |
| 3-7.5 | the light wall curves overhead into a huge cylindrical shaft of dots | turn and tilt up: the scale reveal | echoing water |
| 9-13.5 | cut: a long tiled channel with ceiling lamps and square openings at water level | glide along the wall | sloshing echoes |
| 15-16.5 | cut: a green ball on the line between shallow and deep | glide past at water level | lapping |
| 18-30 | the channel wall fills with ink eyes, then faces, then "ALL EYES ON ME", until a corner is covered | close drift; the lens bends the grid | watery echoes |
| 31.5-43.5 | back down the channel (a yellow ball); a purple ball before a black doorway under a green exit sign | slow push to the doorway | ambient |
| 45-54 | out into the hall: a tall, stretched pool ladder rising from black water; a tilt up to a dome of lights | drift, tilt | ambient |
| 54-60 | the camera dips to the surface; a dark swell rises at the lens, with the playground beyond | the dip, waves at the lens | ripples and splashes |

There is no VO. The AI hears only water ambience, and the credited track cannot be checked from frames.

## Signature device
The swimmer's-eye float. A camera rides a few centimetres above the water on a wide lens with heavy barrel
distortion, gliding slowly with few cuts through one building of three materials: white tiles with dark grout,
clear water over a tiled shelf, and black deep water. "The edge" between shelf and black water stays in frame most
of the time. A light wall receding into a curved shaft gives scale, and a small saturated playground is a goal never
reached. A ball in a new colour marks each section. One detail escalates (the eyes), and the end crosses the
boundary, down into the dark water.

## Pacing read
The film runs 1.0 cuts per 10 s, with a mean shot of 8.57 s and a longest of 22.5 s (31.5-54 s, corridor to hall
in one move). Every 1.5 s sample is still a big change (quiet share 0.0), because the wide lens turns small moves
into whole-frame changes. A CV of 0.0 only reflects the sampling step. The 0.692 hook change is the drift to the
edge. Energy stays between about 0.5 and 0.88, lowest during the slow glides at 36-39 s and rising for the final
dip. Nothing jumps out. It may loop, since the end faces the playground as the start does, but frames cannot
confirm that.

Re-measured with colour-gated cut detection (a cut needs the colour distribution to jump, so camera moves, morphs and full-frame patterns no longer count): 6 cuts in 60.0 s sampled (1.0 per 10 s), at 9.0, 15.0, 18.0, 31.5, 54.0, 58.5 s; 39 samples where most of the picture changed. Where an earlier figure in this section differs, this one is current.

## Look
- Palette: cool blue-greys from tile and water (#627f90, #8499a9, #4b6575), deep water (#2f4451) and pale tile
  (#b8c5cf). The only saturated colour is small: the playground, one ball at a time and a green exit sign.
- Light: soft and shadowless, from round lamps and the point grid.
- Render: Blender (per the hashtags), with a displaced water surface refracting the floor tiles, slight depth of
  field, motion blur and fisheye.

## Why it works
- Liminal familiarity: a known place emptied until it feels wrong. It taps the #backrooms and #poolrooms crowd.
- One rule in the caption turns a calm drift into suspense, and the film obeys it until the end.
- Tension without a scare: viewers rewatch to find the eyes, the scrawl and the doorway.
- A far goal gives the eye somewhere to go.
- Shares come from "this is my nightmare" and fear of deep water: 826.6K shares, 566.4K saves.

## Steal this (grammar) / Leave this (content)
- Steal: a slow POV riding a material boundary; one caption rule that creates suspense; a bright far goal; one
  coloured marker per section; one escalating detail; an end that crosses the boundary.
- Leave: the poolroom and its layout, the eye drawings and the scrawl, the music and the props.

## Build it in our studio
- Engine: `hyperframes` with the Three.js adapter on software WebGL: tiled boxes, an instanced dot grid for the
  light wall, water as a plane with scrolling normal maps and refracted floor tiles, and a barrel-distortion pass.
  `gen-video` (paid, needs approval) gives convincing poolrooms with weak camera control. The stylised fallback is
  `canvas`, with projected tile grids and sine-displaced water in a low-res PS1 look.
- Plan: 1) one space, one boundary, one far goal; 2) a camera spline at water height with a seeded bob; 3) one
  marker per section plus the escalating detail; 4) a dip under the surface at the end; 5) water ambience under a
  supplied ambient track.
- Hard part: believable water without a GPU. Keep the scene sparse, bake the textures, and render 3 segments in
  parallel.
- Difficulty 4, or 2 with client footage (a gimbal at water level in a real pool).

## Business translations
- Hotel or spa: a dawn float at water level through their real, empty pool, with one caption line, ending under
  the surface.
- Events venue or immersive exhibition: a slow float toward one bright object at the far end, with a single rule in
  the caption.
- Real-estate developer: a wide-lens drift through an amenity floor that keeps the window line in frame and crosses
  it at the end (from their renders or footage).
