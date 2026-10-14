---
id: tt-crannyjr-utd
title: "A five-second footballer fan edit that whips from the last shot back into the first and loops forever"
url: https://www.tiktok.com/@crannyjr_utd/video/7660930701184847125
platform: tiktok
creator: crannyjr_utd
plays: 23700000
likes: 2600000
shares: 136100
saves: 370889
followers: 296600
posted: 2026-07-11
captured: 2026-10-14
duration_s: 5
category: lyric-mograph
hook: [mid-action-start, familiar-ip]
devices: [seamless-loop, whip-pan, cut-on-beat, trending-audio]
energy: high
palette: [dark, mono]
palette_hex: ["#0f1417", "#1d242a", "#323940", "#565455", "#cac7b9"]
sound: [music-beat, trending-audio]
voiceover: false
text_on_screen: none
engine: [footage, hyperframes, canvas]
difficulty: 2
fit: [personal-brand, events, local-service, health]
wow: 3
relevance: 3
pacing:
  cuts_per_10s: 18.0
  mean_s_between_big_changes: 0.5
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.698
---

## The film in one line
A five-second After Effects edit of Barcelona's Lamine Yamal: a smiling finger-to-lips close-up, a laugh with a
teammate as the colour drains to grey, the back of his No. 10 shirt, a sharp head turn, a salute to camera, then
a motion-blur whip that lands back on the first shot so the clip loops without a seam.

## Why it stops the scroll (first 2 s)
- 0.0 s: pure motion blur, pale and blue-grey streaks with a curved light trail; the viewer is dropped into the
  middle of a camera whip.
- 0.5 s: the blur resolves into a close-up: the player grinning, finger by his mouth, Barcelona shirt, blurred
  stadium behind.
- 1.0 s: a shaken, cooler, half-desaturated frame mid-transition, a stadium board smeared across.
- 1.5-2.0 s: wider shot, he laughs with a teammate (back to camera at right), crowd and a stand banner behind.
- Mechanism: a famous face plus motion from frame one. The blur start is the tail of the loop, so on autoplay the
  first view already feels like a replay of something in progress. The caption says it plainly: "Loop at the end".

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0 | motion-blur streaks | whip resolving into shot 1 | energetic electronic track already running |
| 0.5 | close-up, finger near mouth, smiling | slight push-in | beat |
| 1.0 | chest-up, shaken, cool grade | camera shake, smear transition | beat |
| 1.5-2.5 | laughing with a teammate, crowd behind | slow push-in while the colour fades to near mono | music holds |
| 3.0 | back of the No. 10 shirt, sitting on grass | hard cut, saturated grass for one beat | beat |
| 3.5 | profile close-up, head turning | turn with motion blur | beat |
| 4.0 | medium close-up looking off right, floodlight bokeh | settle | beat |
| 4.5-5.0 | salute, hand flat on forehead, looking into lens | hold, then whip blur into 0.0 | track loops |

## Signature device
The whip loop: the last shot (a salute held for about half a second) ends in a fast directional motion blur, and
the first frame of the video is the same blur resolving into the first close-up. The streak direction, colour
and brightness match on both sides of the seam, so the platform's replay is invisible and watch time counts
double. Inside the loop, shots last 0.5-1 s and change on the beat, with one longer 1-1.5 s shot (the laugh) as the
only rest. Each shot gets a micro-move (push-in, shake or head turn) so no frame is static, and the grade swings
from natural colour to near monochrome and back, giving a second rhythm on top of the cuts.

## Pacing read
The 2 fps detector saturates: 18 cuts per 10 s, a big change every 0.5 s, CV 0.0 and no quiet samples mean every
sample differs from the last. Reading the frames, there are about seven shots in 5 s, with one held shot of about
1.5 s (1.5-2.5 s) where the colour drains instead of cutting. A hook change of 0.698 is very high: the whip into
the close-up is the biggest jump in the film. It never ends; the last beat is the transition back to the start.

## Look
- Palette by role: crushed teal-black shadows (#0f1417, #1d242a, #323940) dominate, skin and kit pulled toward
  grey (#565455), pale highlights and floodlights (#cac7b9); the club's red and blue survive only in some shots.
- Type: none.
- Texture: heavy contrast, soft glow on highlights, motion blur, camera shake, sharpened faces.
- Camera: broadcast and phone footage reframed to tight close-ups, digital push-ins.

## Why it works
- A star face in the first half second and constant motion.
- Short enough (5 s) that most people watch twice before deciding; the invisible loop turns that into many plays.
- The salute is a clean ending gesture that also feels like a sign-off, so the loop reads as intentional.
- Comment trigger: fans argue about the player and the trend; 17.7 K comments and 371 K saves (editors save it as
  a template). 23.7 M plays on 296.6 K followers is about 80x.

## Steal this (grammar) / Leave this (content)
- Steal: a 5 s loop of one hero person; whip blur as the seam with matched streak direction; shots of 0.5-1 s on
  the beat with one longer rest; a micro-move on every shot; colour-to-mono grade swing; end on a gesture to
  camera.
- Leave: the athlete, match footage and broadcast pixels, club crests and kit, the trend audio.

## Build it in our studio
- Engine: `footage` (the client's own clips) cut in `hyperframes` (registry transitions for whip blur, shake and
  grade); `canvas` if we want full control of the blur seam.
- Scene plan: 1) pick 6-7 short moments of one person from client footage, ending on a gesture into the lens;
  2) beat-grid the track with `beats.py` and place cuts on beats, one 1.5 s hold in the middle; 3) add a
  push-in or shake per shot (seek-safe keyframes); 4) build the seam: the last 0.15 s and the first 0.25 s use
  the same directional blur and grade so frame N-1 and frame 0 match; 5) grade swing with a saturation keyframe.
- Hard part: an invisible seam. Render the blur from a shared streak layer used on both ends, and check the
  last and first frame side by side.
- Cheap to render (5 s). Difficulty 2 with good footage; nothing to build without footage.

## Business translations
- Gym or personal trainer: a member's real lift, the bar locking out, a head turn, a nod to camera, then the whip
  back to the start.
- Barbershop: the client's own clip of a fresh cut: clipper pass, mirror turn, profile, a thumbs-up to camera,
  looping.
- Event or conference: the speaker walking on stage, the crowd reacting, a wave from the stage, looped as a
  story teaser.
