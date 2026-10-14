---
id: tt-bymike0404
title: "Day 3 of making commercials for brands: the Uber wordmark becomes a city, the car becomes the map dot"
url: https://www.tiktok.com/@bymike0404/video/7626041677869763870
platform: tiktok
creator: bymike0404
plays: 4900000
likes: 792000
shares: 6016
saves: 49847
followers: 12500
posted: 2026-04-07
captured: 2026-10-14
duration_s: 17
category: ui-saas
hook: [series-hook, text-headline]
devices: [zoom-through-scale, match-cut, map-zoom, ui-card-stack, screen-in-frame, series-episode]
energy: high
palette: [mono, dark]
palette_hex: ["#070705", "#a2a1a7", "#3f3c37", "#797c84", "#bfbfc6"]
sound: [music-beat]
voiceover: false
text_on_screen: headline
engine: [hyperframes, canvas]
difficulty: 3
fit: [saas, local-service, ecommerce, agency]
wow: 4
relevance: 5
pacing:
  cuts_per_10s: 10.0
  mean_s_between_big_changes: 0.5
  change_rhythm_cv: 0.0
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.396
---

## The film in one line
A phone films an editing app playing a self-made Uber spot: squares form the creator's winking avatar, the Uber
wordmark builds, the camera dives into its letters which become a black and white city, a white car drives
through, turns into the blue location dot on a map, the map becomes the phone app (Where to?, destinations, UberX,
Confirm and request), and it ends on the car in profile with the avatar on its window.

## Why it stops the scroll (first 2 s)
- 0.0-0.5 s: a monitor filmed at an angle, editing app and timeline visible, squares assembling on a white comp;
  caption "Day 3 of making commercials for brands" in the lower third.
- 1.0-1.5 s: the creator's line-drawn avatar winks on black.
- 2.0 s: "Ube" in the Uber wordmark, the last letter still forming.
- Mechanism: the "Day N" caption promises a new brand daily and visible craft; a known brand lands at 2 s.

## Beat map
| t (s) | on screen (inside the monitor) | what moves | sound |
|---|---|---|---|
| 0.0-1.5 | squares assemble into the creator's winking avatar | pop in, wink | energetic music |
| 2.0-2.5 | Uber wordmark builds on white | letters complete | music hit |
| 3.0-4.0 | dive into the extruded "b"; letters become white buildings from above, a car between them | push in to top-down | music |
| 4.5-8.5 | car drives between black boxes, then crosses frame side-on | chase, lateral pan | music |
| 9.0-10.5 | the car becomes a blue dot; pull back to a map crossroads | match cut, zoom out | music |
| 11.0-13.0 | the map is a tilted phone: "Where to?", destinations, "UberX ... USD 3.99" | cards slide and stack | music |
| 13.5-14.5 | button grows into "Confirm and request (0:02)" and counts down | morph | music |
| 15.0-16.5 | car stops in profile on a blue glow; avatar on its window | settle, sign-off | music ends |

## Signature device
Logo-into-world zoom: the camera pushes into the brand's own wordmark until the letterforms, extruded in white
with hard black shadows, become city blocks seen from above, with the product (a car) already driving between
them. Match cuts keep the viewer inside the brand's world: car to blue map dot (same position and scale), map to
phone screen, phone to floating UI cards in real flow order, and back to the car as hero. Strict black, white and
greys; the brand's one accent (the blue dot) appears only when the product becomes the app.

## Pacing read
10 cuts per 10 s and a change every 0.5 s (CV 0.0) mix real scene changes (every 1 to 1.5 s) with the handheld
phone. Longest steady stretch 3.5 s (the chase). No rests until the car settles in the last 1.5 s; the busiest part
is 9 to 14.5 s, a new card every half second. It ends on a near-still hero frame, a sign-off rather than a loop.

## Look
- Palette: near-black surround and app chrome (#070705, #3f3c37), white and light greys for city and UI
  (#bfbfc6, #a2a1a7, #797c84), one saturated accent: the app's blue dot and the blue glow under the car.
- Type: the brand's wordmark and real app type; the caption is the platform's white text, about 40 px on 1080.
- Light and camera: studio white, hard top light on the letters; phone filming the monitor close, at an angle.

## Why it works
- The "Day 3" caption builds a habit; the avatar makes it personal.
- The logo-to-city dive is a real surprise at 3 s; match cuts make brand, ride, app and car one thought.
- The familiar UI drives recognition and "do my brand next" comments; 792 K likes on 4.9 M plays.

## Steal this (grammar) / Leave this (content)
- Steal: dive into the client's logo until it becomes their world; the product lives there; match cut the product
  into its UI symbol (dot, icon, cursor); pull back into the device; walk the real flow as floating cards; end on
  the product hero with a small signature.
- Leave: Uber's wordmark, screens, prices and addresses; the creator's avatar; their music.

## Build it in our studio
- Engine: HyperFrames for the wordmark build, map and UI cards (real screenshots of the client's app, never
  invented screens); canvas for the dive (extruded letterforms with projection math, top-down camera, product
  sprite with a soft shadow).
- Plan: 1) vectorise and extrude the real logo, push to top-down in 1 s; 2) product drives with `spring()` easing;
  3) match cut to the UI symbol at the same position; 4) pull back to a phone with the real app, CSS 3D tilt;
  5) cards every 0.5 s; 6) hero shot.
- Hard part: the dive must hand over from letters to city without a pop. Keep one extrusion and shading in both
  states and move the camera along one continuous curve.
- Difficulty 3: all 2D or fake-3D in our stack; it needs careful matching at each cut.

## Business translations
- SaaS scheduling tool: the logo letters become a week grid, a meeting block slides in and becomes the
  notification dot, then the real app flow.
- Local taxi firm: the wordmark becomes the town's streets, the car becomes the tracking dot, then real booking
  screens.
- E-commerce shop: the logo becomes shelves, a parcel becomes the cart badge, then the real checkout.
