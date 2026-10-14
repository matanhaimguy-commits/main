---
id: tt-babyinside7
title: "Inside the body, day by day: eight 8-second 3D shots step through a menstrual cycle under a day counter"
url: https://www.tiktok.com/@babyinside7/video/7565499340504960286
platform: tiktok
creator: babyinside7
plays: 62100000
likes: 3900000
shares: 1900000
saves: 486336
followers: 307200
posted: 2025-10-26
captured: 2026-10-14
duration_s: 64
category: explainer-3d
hook: [number-ladder, text-headline]
devices: [timeline-progression, x-ray-cutaway, voiceover-explainer, asmr-foley]
energy: calm
palette: [dark, pastel]
palette_hex: ["#000000", "#ae7787", "#86505d", "#632c33", "#d4a6bc"]
sound: [voiceover, asmr-foley]
voiceover: true
text_on_screen: headline
engine: [gen-video, canvas, hyperframes]
difficulty: 4
fit: [health, education, local-service]
wow: 4
relevance: 4
pacing:                               # 1.5 s sampling, 43 frames cover the full 64 s
  cuts_per_10s: 0.0
  mean_s_between_big_changes: 1.61
  change_rhythm_cv: 0.32
  quiet_share_2fps: 0.0
  hook_change_0_2s: 0.255
---

## The film in one line
A letterboxed 3D animation travels inside the uterus and ovary for eight days, one 8-second chapter per day:
the lining sheds and bleeds, the walls contract, the bleeding stops, a fresh pink layer grows, follicles swell
until one dominates, nerves spark, and on Day 8 a glossy mature follicle sits ready.

## Why it stops the scroll (first 2 s)
- 0.0 s: black screen with a wide picture band in the middle. Above it, white serif "Period Cycle Day 1"; below it,
  "Period cycle 3D Process Day 1 & Day 8". In the band, a soft pink dome of tissue inside a cavity.
- 0.5-1.0 s: slow push; the dome surface is cracked like dry clay.
- 1.5-2.0 s: the dome breaks open and dark red blood and white tissue spill down the cavity.
- Mechanism: a taboo, rarely seen process shown "for real" in glossy 3D, plus a day counter that promises a
  journey to Day 8. No voice in Day 1, only wet squelching sound (AI segment), so the image does the work.
  The first spoken line arrives at about 8 s: "The myometrium undergoes strong, wave-like contractions to expel
  the thickened uterine lining."

## Beat map
| t (s) | on screen | what moves | sound |
|---|---|---|---|
| 0-8 Day 1 | close inside the uterus: cracked pink dome gives way to blood and tissue | slow push, tissue crumbles and pours down | wet squelching foley, no VO |
| 8-16 Day 2 | wider cross-section, ribbed muscle walls left and right | walls contract in waves, lining and blood burst out of the cavity | VO: the contraction line above |
| 16-24 Day 3 | frontal cutaway of the uterus, ovary on the right with small bubble follicles | blood traces thin out, slight drift | VO: "The bleeding begins to decrease. Tiny follicles start forming in the ovaries." |
| 24-32 Day 4 | macro of the lining: beads of pink cells with red flecks, then a clean empty uterus | push in, then pull back | ambient (no VO in transcript) |
| 32-40 Day 5 | frontal uterus, then into the ovary: a cluster of follicles, then one smooth sphere fills the band | push into the ovary | VO: "The inside of the uterus appears clear, smooth, and covered with a new pink layer of endometrium." |
| 40-48 Day 6 | translucent dominant follicle in its nest; the lining swelling with pores, then fringed folds | slow orbit, surfaces thicken | VO: "One follicle becomes larger and more dominant than the others. The uterine lining thickens in preparation for the next stage of the cycle." |
| 48-56 Day 7 | close on the lining and vessels with glowing yellow electric filaments | sparks sweep across the tissue | buzzing electrical SFX |
| 56-64 Day 8 | glossy mature follicle, then pull back to the full uterus with both ovaries | pull-back reveal | ambient musical tones |

Script structure: six sentences in total, purely descriptive. Day 1 has no words (image and foley carry it);
Days 2, 3, 5 and 6 get one or two sentences each, always "subject + process verb + result" in clinical present
tense; Days 7 and 8 drop the voice for sound effects and an ambient tone. No setup line and no conclusion: the
open loop is the "Day 1 & Day 8" promise in the bottom title, and the payoff is simply reaching Day 8.

## Signature device
A numbered day ladder over one continuous inside-the-body journey. The frame is fixed: black letterbox, a
landscape picture band across the middle third, a changing serif chapter title above ("Period Cycle Day N",
about 60 px on 1080) and a static series title below. Each day is exactly 8 s, one camera idea per day (push,
pull back, orbit), soft dissolves between them, and one plain present-tense sentence of narration describing
what is visible. The counter is the open loop: the viewer stays to reach the day promised in the bottom title.

## Pacing read
0.0 cuts per 10 s: the cut detector finds no hard cuts because chapters dissolve and 62% of each frame is black
letterbox, which damps the change score. Big changes every 1.61 s with CV 0.32 show steady, slow camera motion.
The hook change of 0.255 is low: this is a calm open that relies on content, not motion. Rhythm is a strict
8 s grid; energy peaks at Day 2 (contractions) and Day 7 (sparks). It ends on a wide reveal, no loop.

## Look
- Palette: black frame (#000000), flesh pinks from deep (#632c33, #86505d) to mid (#ae7787) and pale lilac
  pink (#d4a6bc) highlights; blood red and electric yellow as accents.
- Type: white serif with a soft shadow, two fixed lines, no animation beyond the number swap.
- Render: soft subsurface tissue, glossy wet highlights, shallow depth of field, slow cinematic camera.

## Why it works
- Curiosity about a hidden, universal body process; many viewers have never seen it.
- Share trigger: "send this to someone who should understand this" (1.9 M shares, half the like count).
- Saves (486 K) as a reference; the counter makes it feel complete and learnable.
- Low cognitive load: one day, one image, one sentence.

## Steal this (grammar) / Leave this (content)
- Steal: the fixed letterbox with chapter title above and series title below; a fixed time slot per step;
  one camera move and one sentence per step; foley carrying the wordless first step.
- Leave: the medical renders, the creator's titles, the narration text, the subject itself.

## Build it in our studio
- Engine: photoreal tissue needs `gen-video` (paid, needs approval) per chapter; `hyperframes` for the frame,
  titles and timing. Stylised option: `canvas` illustrated cutaways with soft gradients and spring-driven
  swelling shapes.
- Scene plan: 1) list 6-8 steps of a real process from the client with a source; 2) one 8 s shot per step;
  3) one sentence per step, recorded VO; 4) frame template with the counter; 5) foley per step.
- Hard part: consistent look across generated shots; lock one style prompt and seed, keep cameras simple.
- Difficulty 4 photoreal, 3 stylised.

## Business translations
- Dental clinic: "Implant healing, Week 1 to Week 12", one stylised cutaway of the jaw per stage.
- Physiotherapy practice: "Torn ligament, Day 1 to Day 60", the repair seen inside the knee.
- Bakery: "Sourdough, Hour 1 to Hour 8", macro of the dough rising and bubbling under a counter.
