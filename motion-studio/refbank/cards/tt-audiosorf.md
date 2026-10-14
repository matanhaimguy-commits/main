---
id: tt-audiosorf
title: "A lyric edit where one small ball bounces, rolls and rises through a new primitive 3D set on every word, always on the centre line"
url: https://www.tiktok.com/@audiosorf/video/7666541874097786134
platform: tiktok
creator: audiosorf
plays: 3600000
likes: 751700
shares: 38300
saves: 161738
followers: 37200
posted: 2026-07-25
captured: 2026-10-14
duration_s: 10
category: lyric-mograph
hook: [text-headline, sound-hook]
devices: [lyric-sync-type, match-cut, cut-on-beat, word-by-word, rigid-body-drop]
energy: high
palette: [dark, saturated]
palette_hex: ["#221f1e", "#c3ded9", "#1d13d8", "#d60d14", "#9e886b"]
sound: [music-beat]
voiceover: false
text_on_screen: heavy
engine: [canvas, hyperframes]
difficulty: 2
fit: [agency, saas, events, personal-brand, education]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 12.0
  mean_s_between_big_changes: 0.56
  change_rhythm_cv: 0.28
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.909
---

## The film in one line
Cut to a sung line, a small sphere travels through a string of minimal 3D sets that change on almost every word:
it bounces on a lone pillar behind a giant red "TIME", rolls along beams through door frames under "TO RUN" and
"AWAY", rises through tilted neon square frames under "AWAY", "IS", "EASY", and ends balanced among rising and
falling pillars under "RUNNING AWAY" and "IS", with clock-dial tick marks as the recurring time motif.

## Why it stops the scroll (first 2 s)
- 0.0 s: black frame, one grey square pillar rising from the bottom centre. Nothing else.
- 0.5 s: hard flip to light grey with an enormous condensed red "TIME" filling the width; a white ball bounces
  on top of the pillar in front of the word.
- 1.0 s: background flips to near-black on the beat; same word, same ball.
- 1.5 s: camera pulls back; "TIME" now sits inside a ring of clock tick marks, the pillar and ball centred.
- 2.0 s: hard cut to saturated blue: a yellow ball above an olive beam that leads into a dark door frame.
- Mechanism: an empty first frame, then a huge word on the first sung beat (hook change 0.91, the highest
  possible kind of jolt), with the light-dark flip on the next beat. The sound carries the hook: the words are
  the lyric.

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0 | black, single pillar | pillar | song starts |
| 0.5-1.5 | red "TIME" behind a ball on the pillar; bg flips light, dark, light; clock ticks appear | ball bounces, camera pulls back | sung "time" |
| 2.0-2.5 | blue world: yellow ball over a beam heading into a door frame | ball arcs down toward the door, camera pushes in | beat |
| 3.0 | cyan world, blue "TO RUN", red ball rolling on a pink beam | ball rolls to the door | lyric |
| 3.5 | red world, yellow "AWAY", ball on a teal beam at the door | ball rolls | lyric |
| 4.0 | black, "E[AS]Y" with red E and Y and white bracketed "AS", blue door frame | type snaps in | lyric |
| 4.5 | light grey with pink floor, dark red pillar, white ball above | ball drops toward the pillar | beat |
| 5.0-5.5 | dark: three tilted square frames in blue, magenta and pink, red ball rising through them; clock ticks arc | frames rotate and change colour | build |
| 6.0-7.0 | white "AWAY", "IS", then glitching "EASY" over the frames | words swap per beat, frames recolour orange, green, cyan | lyric |
| 7.5 | light grey, the letters T I M E fanned around the ball in an arc | letters fan out | "time" |
| 8.0-9.5 | dark: pillars of different heights rise and fall, ball balanced on the centre one; "RUNNING AWAY" (red and white), then "IS"; clock arc above | pillars pump | lyric, ends |

## Signature device
One ball, one centre line, a new world per word. Every scene is a minimal set of flat-shaded primitives (square
pillars, beams, door frames, square rings) on a single flat background colour, and the ball always sits on the
frame's vertical centre line, so each hard cut is a match cut on the ball: the eye never has to search. The
ball's motion (bounce, roll, rise) changes with the meaning of the word ("time" bounces in place, "run away"
rolls toward an exit, "easy" floats up through frames). Words are huge condensed or heavy grotesque caps that
sit behind or above the ball and swap on the syllable. A clock dial of tick marks recurs as the motif for
"time".

## Pacing read
12 cuts per 10 s, a big change every 0.56 s and a CV of 0.28: a steady, beat-locked cut rhythm with no quiet
frames at all. The fastest stretch is 2.0 to 4.5 s (a new colour world every half second). The square-frame
section (5 to 7 s) holds the set for about 2 s and lets the words change over it, which works as the breath. It
ends mid-phrase on "IS" over the pillars, so the loop feels like the song continuing.

## Look
- Palette by role: near-black (#221f1e) and pale grey (#c3ded9 as measured) as the two neutral grounds;
  scene floods of electric blue (#1d13d8), signal red (#d60d14), cyan, yellow; olive and tan beams
  (#9e886b); spheres in white, yellow or red.
- Type: one condensed heavy sans for the red "TIME" (fills about 90% of the width), one heavy geometric sans for
  the other words (about 120 to 180 px cap height on a 1080 frame), all caps, colour swapped per scene; one
  glitch treatment on "EASY".
- Material and light: flat or lightly shaded primitives, soft gradient shading on pillar faces, a red glow on the
  floor in the pillar scenes.
- Camera: centred, slow push-ins and pull-backs; square (1:1) framing.

## Why it works
- Lyric plus image: each word gets a visual that acts it out, which people save to learn the edit
  (162 k saves) and to reuse the sound.
- The centre-line ball keeps a chaotic cut rate readable.
- Colour floods change on the beat, so it feels faster than it is.
- High like rate (about one like per five views) shows it is enjoyed, not just watched.

## Steal this (grammar) / Leave this (content)
- Steal: one hero object locked to the centre line across hard cuts; a new single-colour primitive set per
  word; the object's motion acting out the word; giant type behind the object; a recurring motif (clock ticks)
  for the theme word.
- Leave: the song and its lyrics, their sets and colour order, the glitch "EASY" treatment.

## Build it in our studio
- Honest difficulty: despite the "physics" caption, nothing here needs simulation. Bounces and rolls are
  closed-form arcs and eases; the sets are boxes, cylinders and spheres. Difficulty 2.
- Stylised 2.5D route (our main route): canvas engine with simple perspective projection for boxes and frames,
  spheres as radial-gradient circles with a contact shadow, background colour fills per scene; type drawn with
  the client's display font. Or HyperFrames with the Three.js adapter for true 3D primitives (software WebGL is
  fine at this polygon count).
- Paid route: not needed. Only if a client wants glossy realistic materials would we use `gen-video` (with
  approval) per scene from styleframes, but beat-locked cutting and the centre-line match are better kept in
  code.
- Scene plan: 1) take the client's slogan or a licensed track's hook, mark word onsets (beats.py plus a manual
  word map); 2) one set and one colour per word, the object's motion chosen to act out the word; 3) object locked
  to x = 540 in every scene; 4) type behind the object, swap on onsets; 5) one recurring motif from the
  client's world.

## Business translations
- Delivery app: a parcel-shaped block travels the centre line through a new set per word of the slogan, rolling
  to a door on "delivered".
- Fitness studio: a ball bounces through sets acting out "Show up. Sweat. Repeat." on a generated track, the
  studio colour per word.
- Event organiser: the festival's mascot object rises through square frames on each word of the date and venue,
  ending on the ticket line.
