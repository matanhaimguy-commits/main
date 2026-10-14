---
id: tt-kotsarevm
title: "Hand-animating the Netflix logo in Procreate, then hitting play: letters turn to popcorn"
url: https://www.tiktok.com/@kotsarevm/video/7546673576217414934
platform: tiktok
creator: kotsarevm
plays: 23000000
likes: 1800000
shares: 32400
saves: 156210
followers: 70200
posted: 2025-09-05
captured: 2026-10-14
duration_s: 20
category: logo-reveal
hook: [brand-name-drop, mid-action-start]
devices: [screen-in-frame, type-morph, deconstruction, morph, seamless-loop]
energy: medium
palette: [dark, brand-colour]
palette_hex: ["#101012", "#17171a", "#cdcbc6", "#070709", "#673030"]
sound: [music-beat]
voiceover: false
text_on_screen: none
engine: [canvas, hyperframes, footage]
difficulty: 3
fit: [agency, personal-brand, restaurant, ecommerce]
wow: 4
relevance: 4
pacing:
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 1.33
  change_rhythm_cv: 0.97
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.084
---

## The film in one line
On an iPad lying on a black desk, an animator takes the red Netflix N apart frame by frame in Procreate, hits
play to show it fold out of a single ribbon, then animates the NETFLIX wordmark so its letters pop into popcorn,
fall into a striped popcorn box, bounce back as a cartoon N, splat into an ink blob and return to the ribbon.

## Why it stops the scroll (first 2 s)
- 0.0 s: top-down-ish view of an iPad held in a left hand on a black surface; cream Procreate canvas with the
  red Netflix N in the centre; an Apple Pencil in the right hand; the animation toolbar along the bottom.
- 0.5 s: same; the pencil approaches.
- 1.0-1.5 s: the right stem of the N folds and slides (onion-skin frames visible): the logo is being taken
  apart.
- 2.0 s: only the diagonal and a stub remain.
- Mechanism: one of the most recognisable logos in the world, plus the promise of seeing how its animation is
  made by hand. The viewer stays for the playback. Upbeat pop music from the start (AI segment).

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0.0-0.5 | iPad, cream canvas, red N, pencil | still, pencil approaches | upbeat pop music |
| 1.0-3.5 | the N loses its stems frame by frame until only the diagonal ribbon is left | strokes fold and shrink, onion skin | music |
| 4.0-5.5 | a red sliver with transform handles, then an empty canvas with the frame strip | pencil works, then lowers | music |
| 6.0-7.5 | playback: a diagonal ribbon unfolds into the full N, then collapses to a tick | frame-by-frame animation plays | music |
| 8.0-8.5 | pencil swipes a black page in; NETFLIX wordmark in red on black | page swap | music |
| 9.0-11.5 | animator edits the X; a popcorn kernel is drawn at its tip | editing | music |
| 12.0-14.5 | playback on black: N, then NET, then the full wordmark draws on | letters pop on | music |
| 15.0-16.0 | the T drops out, letters burst into popcorn kernels that fall into a red and white striped box; background washes from black to cream | morph and fall | music |
| 16.5-17.5 | striped box on cream, kernels pop up out of it with a black streak | bounce | music |
| 18.0-18.5 | a bold cartoon N with a black outline and impact lines lands and squashes | hit and squash | music |
| 19.0-19.5 | a black ink blob splats over the whole canvas, then a red diagonal ribbon on black, the first frame of the logo | splat, reset | music; video fades out (AI segment) |

## Signature device
Make-then-play on a real screen. The camera films a physical tablet on a black desk, so the viewer sees the
maker's hands, the pencil and the app UI, and then the same screen plays the finished animation full-frame on
the tablet. It is done twice, each time with a short editing section (3 to 5 s) followed by a longer playback
(2 to 7 s), so the rhythm is "how" then "wow". Inside the playback, the logo goes through a chain of type morphs,
each a single idea tied to the brand's world: wordmark letters burst into popcorn (cinema), kernels fall into a
striped popcorn box, the box spits out a cartoon N with impact lines, an ink splat wipes the frame, and the
splat resolves into the ribbon that starts the official logo animation, so the end connects to the beginning.
Style is hand-drawn, about 12 fps, flat fills with the brand red, black outlines only on the cartoon N.

## Pacing read
0 cuts and a hook change of only 0.084: the camera never cuts and the change is confined to the tablet screen,
so the frame-wide metric reads it as calm. Big changes every 1.33 s with CV 0.97 mean the rhythm is very uneven:
slow editing sections (1 to 5.5 s, 9 to 11.5 s) alternate with dense playback bursts (6 to 7.5 s, 12 to 19.5 s)
where something new happens every 0.5 s. The real peak is 15 to 19 s, a morph every half second. It ends on the
first frame of the logo animation, so the loop is seamless.

## Look
- Palette by role: black desk and dark tablet (#101012, #17171a, #070709) as the surround, the cream canvas
  (#cdcbc6) in the first half, the brand red (seen darkened as #673030 in the average) as the only accent;
  popcorn yellow and white stripes appear only in the morph chain.
- Type: the brand's own wordmark only; no captions.
- Texture and light: soft top light on the desk, slight reflection on the screen, flat digital drawing on screen.
- Camera: locked or near-locked phone above the desk at about 30 degrees, the tablet filling the width.

## Why it works
- Famous logo, so the first frame is already recognised.
- "How is it made" curiosity, paid off by watching it play.
- The morph chain is a list of small surprises tied to the brand's world (cinema popcorn), each 0.5 to 1 s, so
  there is no dead time in the second half.
- Seamless loop back to the ribbon invites rewatch; tags of the brand drive comments and shares.
- Shows craft: designers save it (156 K saves) as reference.

## Steal this (grammar) / Leave this (content)
- Steal: filming the piece playing on a real device with the maker's hands in frame; editing then playback,
  twice; a chain of morphs where each step is an object from the client's world; ending on the frame the loop
  begins with.
- Leave: the Netflix logo, wordmark, red and the popcorn idea; the creator's drawings; their music.

## Build it in our studio
- Engine: `canvas` for the frame-by-frame logo animation (stepped at 12 fps, hand-drawn look with slightly
  wobbling outlines from seeded noise), then `footage`: play our render on a real tablet or monitor and film it
  with a hand in frame. HyperFrames can do the morph chain too if the client's mark is clean SVG.
- Scene plan: 1) get the real logo file (vectorize with `tools/vectorize_mark.py` if needed); 2) storyboard a
  morph chain of 4 to 5 steps using objects from the client's trade; 3) animate in canvas with `spring()` for
  pops and squash; 4) export a "process" pass (app-like UI is not ours to fake: film a real drawing app or our own
  editor instead) and the playback pass; 5) film both on a tablet on a dark desk; 6) music with a clear beat.
- Hard part: the hand-drawn charm. Use stepped timing (hold each drawing 2 frames at 24 fps), boil the outlines
  slightly every drawing, and keep fills flat.
- Difficulty 3: the animation is 2D and fully in our stack; the effort is in drawing the morph steps.

## Business translations
- Cinema or restaurant: their logo letters turn into the signature dish's ingredients and fall into a takeaway
  box, filmed playing on a tablet at the counter.
- Design agency: a short "watch me animate a client logo" series on a desk tablet, one client per episode,
  with permission.
- Coffee roaster e-commerce: the wordmark bursts into beans, beans fall into the bag, the bag bounces back as the
  logo.
