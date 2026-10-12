# Claude Animation Base: catalog, rules, and how to use it in client reels

Written 12 Oct 2026 from a full read of `references/claude-animation-base` (README, ANIMATION_GUIDE.md,
all of `src/`, `render.mjs`, `studio.html`, `gpu_probe.mjs`, the model sheets) and from a render test in
this cloud container (section 8). It's also installed as a skill at
`.claude/skills/claude-animation-base/`: the same files plus a SKILL.md that says to copy the kit into
a project, then `npm install`, then read the guide, then render with
`--chrome=/opt/pw-browsers/chromium-1194/chrome-linux/chrome --soft-gl`.

---

## 1. What it is

- **Repo:** github.com/JohnHeibel/ClaudeAnimationBase. **License: MIT**, (c) 2026 John Heibel. It's
  free for commercial client work; keep the copyright and permission notice with any copied code.
- **What it is:** a small starter kit for **hand-painted 2D character animation** in **p5.js 2.x +
  p5.brush 2.2** (watercolour, ink and hatching brushes on WebGL). It stars **Clawd**, the terracotta
  Claude Code mascot.
- **Origin:** it's distilled from the music video "I'm Upping My P(doom)" plus the author's analysis of
  what Opus did and didn't do well. The guide is written *for the model*: rules, workflow and the full
  API.
- **The look:**
  - Flat 2D watercolour wash with ink outlines that **boil** at 12 fps.
  - Paper texture under everything and grain multiplied on top.
  - No text, no 3D.
  - Characters act with cartoon principles (anticipation, takes, squash and stretch, overlap) locked to
    a BPM.
- **What it isn't:** it's not for UI, kinetic typography or product motion graphics. The skill
  description says so. It's for the **character moment**: a mascot, an explainer host, a reaction.
- **Rendering:** a headless-Chrome renderer (`render.mjs`, puppeteer-core) produces contact sheets,
  frame strips, crops that follow a point, stills, PNG loops, parallel resumable JPEG frames and MP4
  (ffmpeg, x264), with optional audio mux.
- **Canvas and frame rate:** 1920x1080, 24 fps. `onTwos()` gives 12-drawings-a-second acting, and the
  boil is always 12/s.

### File map

| path | what it is |
|---|---|
| `ANIMATION_GUIDE.md` | The rules (3 goals, 7 rules), the animation principles, the workflow (storyboard, build, review loop, render), the full engine and Clawd API, music, common failures, and a worked timing example. **Read it fully before drawing.** |
| `README.md` | Quick start, render flags (`--soft-gl`, `--gpu-angle`, `--chrome`), file table |
| `src/config.js` | `PROJECT = { duration: 11, bpm: 120, offset: 0, audio? }`: length, tempo, first downbeat |
| `src/core.js` | Canvas (1920x1080 WEBGL), `PAL` palette, easing/timing/motion helpers, `boilSeed`, camera, full-frame effects (`flash`, `iris`, `irisShape`), `glow`, geometry (`rectPts`...`ribbon`), `paint()`/`inkLine()`, lettering, paper and grain, custom brushes, `setup`/`draw`, `renderAt`/`renderSheet` hooks, dev scrubber |
| `src/clawd.js` | Clawd: `VIEWS`, `spinView`, `turn`, tints, `clawd()`, lunchbox lid, smear, gloom, blush, 24 eyes, 16 mouths, 15 hats + 3 face pieces, 18 emotes, `EMO` (31 emotions), `feel`, `emotions`, `move` (12 dances), `dancer` |
| `src/timeline.js` | `shots()`, `LOOPS`, `drawWorld`, placeholder, `brushWipe()` |
| `src/sheets.js` | Model sheets as loops: `LOOPS.emotions`, `LOOPS.views` (the only place labels are allowed) |
| `src/scenes/demo.js` | "The fallen star", 11 s, 2 shots: one example, explicitly **not a template** |
| `studio.html` | Loads p5, p5.brush and the src scripts; a scrubber UI (`?t=2.5`, `?loop=emotions`). **Pulls the Permanent Marker font from Google Fonts** (see pitfalls) |
| `render.mjs` | Headless renderer, all modes (section 8) |
| `gpu_probe.mjs` | Prints which WebGL renderer each Chrome flag set gets |
| `docs/emotions.jpg/.webp`, `docs/views.jpg` | Model sheets: 31 emotions; 5 views + motion + hats |

---

## 2. The rules, in usable form

**Three goals:**

- **Handmade:** brush strokes, boiling ink, flat 2D, no lettering.
- **Alive:** something always moves and always happens; faces act, they don't snap; characters are
  big.
- **One piece:** one short film, planned first, every scene linked.
- Under all three, **the viewer must be able to follow it.** Timing is the rule models break most.

### Rule 1: the medium is solid

- **Paint everything with p5.brush** through `paint()` / `inkLine()`.
  - Characters: a flat `wash` plus an ink outline.
  - Backgrounds: soft watercolour `fill` shapes with no or a thin outline.
  - **Never plain p5 `rect`/`ellipse`/`fill()`.** They read as 2000s Flash.
- **The linework boils.** `jit()` and `random()` are reseeded 12 times a second.
  - Things that must not move (star positions, tuft heights) use `hash(i)`.
  - **Call `boilSeed(key)` before every separate element**, or one moving thing makes everything drawn
    after it re-boil every frame (jitter).
- **Flat 2D only.** No `rotateY`, no WEBGL 3D, no perspective math.
  - Turns go through **drawn key views** (front, 3/4, side, back 3/4, back).
  - Depth comes from overlap, scale and colour: farther is smaller, bluer, paler.
- **Light is the one exception:** `glow()` adds real (additive) light, because pigment mixing turns
  yellow over blue into green.
- **Soft palette:** no pure black or white. Use `PAL.ink`, `PAL.cream`, `PAL.paper`.

### Rule 2: no text

- No captions, titles, labels, signs, speech bubbles with words, or words on screens.
- Reactions are **painted marks** (emotes).
- "A sign that repeats the story is the classic failure."
- If a word truly is the joke, use `letter()` once, for 1 or 2 words. For client reels, our own type
  layer handles copy (section 7).

### Rule 3: something happens in every scene

- Every shot has an **event**: something changes from its first frame to its last.
- **One focal action at a time**, with a clear silhouette.
- **Cause, then reaction.** Give the reaction time; it's often the funniest part.
- **Pay off** every setup.

### Rule 4: timing, modelled on the viewer (the most important rule)

- **Write the reads:** for each shot, the ordered list of things the viewer must understand, each with
  a start and an end.
- **One read at a time.** Two things at once means one gets missed. Put the cause and the reaction in
  sequence.
- **Fast actions, slow meanings.** Anticipation lets a move be quick; the hold after it lets it land.
  Rhythm is the contrast between quick and held.
- **Lead the eye** before each important read: a look, a camera move, a light or movement.
- **The reads set the shot length,** including the last shot: its final read must land before the end.
- **Count frames:** 24 = 1 s. A read that gets a handful of frames is lost.
- **Worked example (the demo ending):**
  - throw (7.0 s, fast) -> star flies home (0.8 s) -> arrival flare (0.45 s, Clawd only watches) ->
    Clawd falls in love (0.6 s) -> wave goodbye (0.45 s) -> the star twinkles back (0.4 s) -> iris
    holds and shuts (1.2 s).
  - The first version crammed all of this into 1.3 s and nobody could follow it.

### Rule 5: alive

- **Nothing is ever still.**
  - Every emotion has its own idle motion.
  - Cameras drift or push.
  - Grass sways, stars twinkle, lines boil.
- **Faces act through `emotions()`**, never by swapping eyes or mouth between frames.
- **Clawd is big:** u = 20–28 in a medium shot, 40–70 in a close-up. Below 12 only in establishing
  wides.
- **Everything moves on a beat** (`PROJECT.bpm`), even with no music.

### Rule 6: transitions always

- A transition into the first shot, at every seam, and out of the last shot. Never start on a hard
  frame or just stop.
- Choose one that belongs to the story; don't repeat one blindly. The menu:
  - brush wipe
  - iris or shaped iris
  - whip pan with a smear
  - match cut
  - cut on action
  - a camera move that carries through the cut
  - fade or push from paper or black
- A plain cut only on action or as a deliberate smash cut.
- **Changes inside a shot are transitions too:** emotions go through `emotions()`, turns through
  `turn()`, and props arrive on arcs, never popping in.

### Rule 7: one piece, a vision before code

- **Write `STORYBOARD.md` first:**
  - logline: "wants ___, but ___, so ___";
  - world (setting, a small palette, light, a colour arc);
  - motif;
  - the emotion keys across the whole film;
  - shots with a transition in, the event, the reaction, the camera, and **timed reads**;
  - a transition out.
- **One world** with a colour arc (e.g. cold night -> warm dawn).
- **One emotional thread** across the whole video.
- **Rhyme the ending with the opening.**
- **Keep screen direction and carry motion across cuts.**

**Animation principles as the kit implements them:**

| principle | how |
|---|---|
| anticipation | built into `jump()` and `emotions()` (squint and squash before the change) |
| squash and stretch | `sq` (keeps volume) |
| slow in / slow out | `ease`, `easeIn`, `easeOut`, `backOut` (never a raw linear `lerp`) |
| weight | heavy = slow start/stop, little bounce; light = snappy, bouncy |
| arcs | `arcPt` |
| overlap / follow-through | `spring`, `ring`, `backOut`; the eyes lead, the body follows, props drag |
| no twinning | offset arms, phases and seeds; one arm acts, the other does something smaller |
| exaggeration | push poses and takes further than feels natural |
| strong key poses | block the keys as stills first |
| show the thought | notice, think, act; the eyes move first |
| secondary action | hat bob, emote pop, grass stirring, but never competing with the main action |

**Review loop** (the guide budgets it as mandatory):

- One contact sheet per shot, a strip for every key motion and transition, and a crop for every face
  that carries the story.
- Check: the read, timing (a sheet every 0.1–0.15 s, counting frames per read), motion (anticipation,
  follow-through, pops, constant speed, mirroring), boil, contacts (feet, hands on props), transitions
  at every seam, the rules (text, 3D, dead stretches), and colour (muddy glows, pure black or white).

**Common failures** (from the guide; check every storyboard against them):

- signs or captions
- Clawd standing still and smiling
- one brisk speed with no holds
- moments over before they're understood
- a tiny Clawd for the whole video
- snapping faces
- mechanical, mirrored motion
- timid poses
- jittery boil
- hard cuts
- 3D
- plain p5 shapes or digital glows
- muddy yellow-over-blue
- props floating near hands
- unrelated worlds per shot

---

## 3. Engine API (what a scene can call)

**Contract:**

- A shot is `fn(t, lt, dur)` (video time, time in the shot, shot length).
- It paints the **whole frame**, and is a **pure function of t**: frames render in parallel and out of
  order.
- Register shots with `shots([[t0, fn], ...])`.
- `LOOPS.name = t => {...}; LOOPS.name.len = 4` makes a standalone loop (`--loop=name`).
- Canvas 1920x1080, origin top-left, y down.

**Painting:**

- `paint(pts, o)` options:
  - `wash`/`washOp`: flat colour (255 = exact).
  - `fill`/`fillOp`/`bleed`/`tex`/`border`: watercolour, the slow part (section 8).
  - `hatch: {d, a, o, b, c, w}`.
  - `ink`/`sw`/`br`: outline; `ink: null` means none.
  - `curv`: 0–1 smoothing.
- `inkLine(pts, sw, col, brush, curv)`.
- **Brushes:**
  - kit: `ink`, `inkfine`, `dry`;
  - p5.brush built-ins: `2B`, `HB`, `charcoal`, `marker`, `pen`, `cpencil`, `rotring`, `spray`.
- **Geometry:**
  - `rectPts(x,y,w,h,jitter)`
  - `ellPts(cx,cy,rx,ry,n,jitter,rot)`
  - `rrPts(x,y,w,h,r,jitter)`
  - `starPts(cx,cy,r,inner,n,rot)`
  - `heartPts(cx,cy,r)`
  - `through(P)`: a Catmull-Rom curve through points
  - `ribbon(P,w0,w1)`: one tapered outline for tails, vines, trails, noodle arms
- **"One shape, one outline":** build creatures and props from as few outlines as possible.
- **Light:** `glow(x, y, r, col, a)`, additive. Draw it before whatever sits in front of the light.
- **Palette `PAL`:**

  | name | hex | name | hex |
  |---|---|---|---|
  | paper | `#F3EBDC` | ochre | `#E8AA38` |
  | ink | `#2B2233` | sap | `#6E9F58` |
  | clay | `#D97757` | teal | `#3A9C98` |
  | clayDk | `#A84D33` | violet | `#7B5CA8` |
  | clayLt | `#F2A283` | cream | `#FFF5E2` |
  | night | `#1F2550` | sky | `#8EC3E6` |
  | indigo | `#2F3C7A` | | |
  | rose | `#E27A92` | | |

  `mixCol(a, b, k)` mixes two hex colours.

**Time and motion** (all pure functions of t):

| helper | what it does |
|---|---|
| `seg(t,a,b)` | 0..1 progress through [a, b] |
| `kf(t, [[t0,v0],...], ease)` | keyframes; values may be arrays (camera paths) |
| `lerp`, `clamp`, `frac`, `wob(t,f,ph)`, `TAU` | basics |
| `ease`, `easeIn`, `easeOut`, `backOut`, `elasticOut` | easing; `backOut` overshoots |
| `BEAT`, `bpOf(t)`, `beatN(t)`, `pulse(t,k)`, `pulse2(t,k)` | beat grid: `pulse` is 1 on each beat (pulse2 on eighths) and then decays |
| `jump(t,t0,t1,h)` | crouch, stretch, arc, squash-land, recover -> `{dy, sq}` |
| `take(t,t0,amt)` | surprise take: a quick squash, then a big stretch that springs back -> `{sq, dy}` |
| `stroll(t,t0,t1,x0,x1,u)` | an eased walk in 3/4 view, facing front when it stops -> `{x, walk, view, flip, dy}` (override `view:'side'` for a trot) |
| `spring(t,t0,k,w)`, `ring(t,[...])` | a damped wobble after an event (settles, hats, tails); `ring` gives one kick per event |
| `arcPt(p0,p1,h,k)` | a point on a thrown arc |
| `onTwos(t)` | holds each drawing two frames (12/s) |
| `hash(i)`, `jit(a)`, `boilSeed(key)` | stable random, boil random, per-element boil seeds |
| `shakeXY(t, amt)` | deterministic camera shake at 24 fps |

**Camera:**

- `camBegin(cx, cy, zoom, rot)` ... `camEnd()`: one level only, always paired.
- `toScreen(x, y)` maps world to screen, e.g. to aim an iris at a character.
- Keep the camera alive with a slow drift and push: `camBegin(960 + 20*sin(lt*.6), 540, 1 + .02*lt)`.

**Full-frame effects** (screen space, after `camEnd()`):

- `brushWipe(p, [c1, c2])`: five fat ragged paint strokes cover the frame (p 0 -> .5), then drag off
  (.5 -> 1).
  - Cut under full cover.
  - End of shot A: `if (lt > dur-.3) brushWipe((lt-(dur-.3))/.6)`.
  - Start of shot B: `if (lt < .3) brushWipe(.5 + lt/.6)`.
  - It uses wash + watercolour fill + charcoal hatch, so it's expensive.
- `iris(cx, cy, r, col)`: a circular iris.
- `irisShape(pts, col)`: everything outside any star-shaped hole (a heart, star, keyhole or logo
  silhouette).
- `flash(k, col)`: a full-frame flash.

**Lettering** (avoid):

- `letter(txt, x, y, size, col, {pop, rot, alpha, screen, font, stroke})`.
- `sfx(txt, x, y, size, col, age)`: a comic sound effect that pops, wobbles and fades.
- The font is Permanent Marker. Letters are composited at `flushLetters()`.

**Paper:**

- `makePaper()`: the paper colour plus 70 soft stains and 1,400 fibre strokes from a seeded LCG.
- `makeGrain()`: static grain plus a warm vignette, **multiplied** over the final frame. The reason
  everything sits "in" the paper.
- Both are worth porting to our canvas engine for any paper or collage look.

---

## 4. Catalog: Clawd and everything that ships

`clawd(x, y, u, options)`: (x, y) is the ground point between the feet; Clawd is 10u wide and 8u tall.

**Sizes:** wide u = 10–16, medium 20–28, close-up 40–70, extreme close-up 90+.

**Options:**

| group | options |
|---|---|
| pose | `dx`, `dy` (in u, negative = up), `sq` (squash; negative stretches), `rot` (pivots at the feet), `flip`, `sx`, `sy`, `aL`/`aR` (arm angle: 0 = out, + = up, ±1.5 = vertical), `walk` (leg phase), `noLegs`, `noShadow` |
| view | `view`, `smear` 0..1 + `smearDir` ±1 (0 = both sides) |
| face | `eyes` (or a `[left, right]` pair), `mouth`, `lookX`/`lookY`, `squint`, `blush`, `gloom`, `lid`, `seed` (blink phase) |
| colour | `tint` (+ `tintK`), or `col`/`dk`/`lt` directly |
| extras | `hat`, `emote` + `emoteK` + `emoteAge`, `draw(u, sw)` (paint in body space), `armL`/`armR(u, sw)` (paint at the arm tip; held props follow the arm) |
| boil | `boilKey` (a stable id when characters come and go mid-shot) |

- **Options compose by spreading:**
  `clawd(x, y, u, { ...feel('happy', t), ...turn(t, 1, 1.15, 0, .25), hat: 'party' })`.
  Later spreads win; **add** fields that both set (`dy`, `sq`).
- **Body-local coordinates** (front view): body x -5u..5u, y -8u..-2u; eyes at (±2.5u, -6u); mouth
  near (0, -4.3u); arms pivot at (±4.9u, -4.5u) and are 2.2u long.

### 4.1 Views (5 drawn key views, all facing screen-right; `flip: true` faces left)

| view | what you see | use in a reel |
|---|---|---|
| `front` | face, both arms, four legs | address the viewer, react, present a product |
| `q` (3/4) | the face shifted toward the heading, a darker side strip, the seam line | walking toward something, looking at a product beside it |
| `side` | profile: one eye at the leading edge, one arm | trots and runs across frame, pushing or pulling props |
| `qback` | 3/4 from behind, no face | discovering something: Clawd turns to look at the reveal |
| `back` | from behind, no face | facing a big screen, a skyline or a product reveal with the viewer |

- **`spinView(a)`:** a heading in turns (0 front, .25 right, .5 back, -.25 left), snapped to the
  nearest of 8 drawings (front, q, side, qback, back, then the mirrored qback, side and q).
- **`turn(t, t0, t1, a0, a1)`:** steps through the key views over 0.12–0.25 s with smears, like a
  drawn turn.

### 4.2 Emotions (31): `feel(name, t, over)` and `emotions(t, keys, {take})`

Each emotion is a face, a colour and an idle motion locked to the beat. `emotions()` acts the change:

- a squint and squash just before it (anticipation);
- the face swaps under the squint;
- a take sized to the new emotion;
- an overshoot settle;
- the colour, blush, gloom and lid cross-fade over 0.3 s;
- the new emote pops in (one-off emotes such as `!` fade after 1.4–1.8 s).

`take` below is the reaction size on entering the emotion.

| family | emotion | face | colour / emote | idle motion | take | client-reel use |
|---|---|---|---|---|---|---|
| joy | **happy** | ^ ^ eyes, smile, light blush | none | bounces 1.2u on every beat, arms swing alternately | .6 | default "delighted customer" loop; the end-card mascot |
| joy | **excited** | wide eyes, open mouth | spark | hops 2.4u twice a beat, arms pumping | 1 | launch-day hype, "it's here!", a sale reveal |
| joy | **laugh** | > < squeeze, laughing mouth with tongue, blush | none | fast 5 Hz chuckle-shake, slightly tilted, arms down | .8 | punchline beats, humour ads |
| joy | **love** | heart eyes, cat mouth, strong blush | rosy tint, floating hearts | slow sway over 4 beats, gentle bob | .7 | "customers love it", a product-crush moment, Valentine's |
| joy | **proud** | closed eyes, smile | gold tint, spark | stretched tall (chest out), arms down at the sides, bob on hits | .5 | the "we did it" milestone, award, 5-star review |
| joy | **starstruck** | star eyes, open mouth | gold tint | bouncing twice a beat, both arms up | 1 | big reveal, celebrity or partner announcement, unboxing |
| joy | **playful** | wink, tongue out | none | side-to-side hop each beat with a lean | .6 | casual social content, a teaser |
| joy | **hopeful** | shiny eyes, cat mouth, blush | none | stretched up, looking up, arms open | .5 | "imagine if...", the before-the-solution beat |
| joy | **relieved** | closed eyes, smile | sweat drop | slow breathing squash, arms down | .4 | the "problem solved" exhale after the product saves the day |
| sly | **smug** | narrow eyes, smirk | none | leans back, looks right, one arm up | .4 | comparison ads ("we already knew"), insider tips |
| sly | **cool** | sunglasses, smirk | music notes | head-nod on the beat, one arm up | .4 | lifestyle brand, music sync, "too easy" |
| sly | **mischief** | narrow eyes, grin, gloom brow | none | hand-rubbing tremble, low crouch | .5 | a sneak-peek or "secret deal" teaser |
| sly | **suspicious** | narrow eyes, flat mouth | none | slow side-eye scan, leaning with the look | .4 | "too good to be true?" objection handling |
| low | **sad** | worried eyes, frown, gloom | blue tint, personal rain cloud | slumped, slow sway, arms hanging, looking down | .3 | the "before" pain point of an explainer |
| low | **cry** | tear streams and flicking drops, wailing mouth | blue tint | sobbing hiccup on the beat, arms at the face | .8 | exaggerated pain point ("another failed campaign"), comedy |
| low | **bored** | narrow eyes, flat mouth | none | a big sigh every 4 beats, arms hanging | .2 | "the old way is boring" opener |
| low | **sleepy** | heavy lids, small o mouth | zzz | slow breathing and rocking | .2 | "your ads put people to sleep", night or late-hours beats |
| low | **ko** | X eyes | pale, circling stars | squashed flat and tilted, arms limp | 1 | knocked out by complexity or price; a competitor "loses" |
| hot | **angry** | angry slants, gritted teeth | flush tint, vein-pop | 18 Hz tremble, squash on the beat | .8 | frustration with the old way |
| hot | **furious** | red glowing eyes, **lunchbox lid open with teeth** | strong flush, steam | violent shake, hop on beats, arms flailing | 1.2 | the comedic peak of a pain point (a hidden fee) |
| hot | **determined** | determined slants with a glint, flat mouth | none | forward lean, alternating arm pumps (marching) | .7 | "let's fix this", a call to action, the onboarding journey |
| hot | **disgusted** | squeeze eyes, wobbly mouth | green tint | leans away, shudders every 2 beats | .8 | reacting to the competitor or the "before" product |
| alarm | **surprised** | wide eyes, O mouth | `!` (fades) | stretched, lifted, arms up | 1.3 | **the reaction take** to a reveal: price drop, feature, stat |
| alarm | **scared** | big white eyes with darting pupils | pale tint, sweat | fast trembling, stretched, arms up | 1.1 | risk or "are you losing customers?" hooks |
| alarm | **nervous** | looking eyes, wobbly mouth | pale, sweat | eyes dart each beat, shuffling, fidgeting | .5 | anticipation before a reveal, a deadline |
| alarm | **confused** | mismatched narrow/wide eyes, wobbly mouth | `?` | head-tilt sway, one arm scratching | .6 | the explainer's "how does this work?" setup |
| alarm | **dizzy** | swirl eyes | circling stars | wobbling orbit sway | .7 | information overload, "too many tools" |
| mind | **neutral** | slit eyes, no mouth | none | a gentle beat bob | .3 | the rest state between acted beats |
| mind | **thinking** | eyes looking up-right, flat mouth | `...` dots | tilted, one arm at the chin, the other tapping | .4 | considering options, the setup of a comparison |
| mind | **idea** | shiny eyes, grin | **light bulb with real glow** | bob, one arm raised high | 1.1 | **the eureka beat**: discovering the product or solution |
| mind | **shy** | looking down-left, wobbly mouth, full blush | none | squashed, swaying, fidgeting arms | .3 | a cute brand humility moment, a "thank you" end card |

**A useful emotional arc template for a 15–30 s ad:**

`bored`/`confused` (pain) -> `surprised` (reveal) -> `idea` (understanding) -> `excited`/`starstruck`
(benefit) -> `proud`/`happy` (resolution, logo).

For explainers: `thinking` -> `confused` -> `idea` -> `determined` -> `relieved`.

### 4.3 Face parts

- **Eyes (24):**
  - normal, look, wide (these three blink every ~3.3 s, phased by `seed`);
  - happy, closed, sleepy, wink, narrow, angry, determined, sad, teary (wobbling pooled tears), cry
    (streams and flying drops), squeeze, shine;
  - scared (jittering pupils), blank, spark (star), red (glowing), heart (pulses on the beat), x,
    swirl (spins), dot, shades (sunglasses with glint, a profile version with the arm to the ear).
  - A pair gives mismatched eyes. `lookX`/`lookY` aim the pupils, and `squint` closes any eye shape.
- **Mouths (16):** o, O, smile, grin, flat, wobble, cat, frown, smirk, laugh, open, wail (vibrates),
  teeth, tongue, pout, yawn. `null` means no mouth, Clawd's resting face.
- **Lunchbox lid** (`lid` 0..1, front view only):
  - The top of the body hinges open to show a dark mouth, tongue and staggered teeth that never
    cross.
  - Use it for fury, chomping or shouting.
  - Reel uses: "eats the competition", gobbling up a messy pile of tasks, a big "WOW" shout with no
    text.
- **Body colour:**
  - `tint`: pale (fear), flush (anger), blue (sadness), rosy (love), green (disgust), gold (pride), or
    any hex, with strength `tintK`.
  - `gloom`: an indigo forehead wash with hanging lines.
  - `blush`: cheeks, hatched above .6.

### 4.4 Hats and accessories (`hat:`)

| hat | look | reel use |
|---|---|---|
| party | pink cone with an ochre pompom | anniversaries, launches, "Black Friday is here" |
| hard | yellow hard hat | "under construction", building or renovation clients, "we build your funnel" |
| crown | gold crown with gems | the customer is king, premium tier, a #1 claim |
| halo | ochre ring | the "good choice", guilt-free products |
| wizard | indigo cone with a star | AI or automation "magic", tips and tricks |
| hood | violet cone (wizard shape) | mystery, a sneak-peek |
| top | black top hat with a red band | elegant, events, a "presenting..." intro |
| fedora | dark fedora with a red band | detective or investigator, "we analysed your account" |
| band | red headband | sport, hustle |
| sweatband | cream sweatband with red stripes | fitness clients, "workout" metaphors |
| beanie | teal beanie with a pompom | winter campaigns, casual |
| bow | pink bow | cute, gifting |
| flower | cream daisy | spring, organic, beauty and wellness |
| headphones | violet over-ear | music, podcasts, "listen" CTAs |
| cat | clay cat ears + whiskers (front and 3/4) | pet-brand clients, cute |

- **Face pieces:** `masq` (a violet masquerade mask: mystery deal or launch), `mask` (a violet bandit
  band: "steal this deal") and `bowtie` (a rose bow tie: formal, the host).
- Any client prop goes in the hooks: `draw(u, sw)` paints on the body (a logo badge, an apron, a
  name-tag shape) and `armR` holds a product.

### 4.5 Emotes (18): painted reaction marks, never letters

`emote(kind, x, y, s, k, age)` can be drawn anywhere, e.g. over a product or a phone screen.

| emote | what | reel use |
|---|---|---|
| `!` | ochre bang with wobble | notice or alert, "new" |
| `?` | sky-blue question mark | a question hook, "did you know?" |
| `!!` | double bang | big news, urgency |
| `!?` | bang + question | shock and disbelief at a price or result |
| `zzz` | painted Z shapes drifting up | boredom, the old way |
| `sweat` | two drops | nervous, relief, effort |
| `spark` | twinkling 4-point stars | something shiny or new, a premium sparkle on a product |
| `heart` | one heart pulsing on the beat | a like, a favourite |
| `hearts` | three floating hearts | love it, reviews, social proof |
| `anger` | red comic vein-pop that pulses | frustration |
| `steam` | puffs from both sides | fury, also a hot coffee or food product |
| `bulb` | light bulb with real glow and rays | the idea or solution moment |
| `dots` | "..." appearing in sequence | thinking, loading, "typing..." |
| `scribble` | an ink scribble cloud | confusion, chaos, messy workflow |
| `music` | two bobbing notes | music, vibe, audio products |
| `swirl` | violet spiral | dizzy, hypnotised |
| `stars` | three stars circling the head | KO, dazed, or a "5-star" playful nod |
| `cloud` | personal grey rain cloud with rain | gloom, a bad day before the product |

- `steam`, `stars`, `cloud`, `bulb` and `scribble` sit over the head; the rest sit at the top corner.
- `emoteK` (0..1) gives the pop with overshoot; `emoteAge` drives the looping ones.

### 4.6 Motion and acting helpers (shown on views.jpg row 2)

| helper | what it does | reel use |
|---|---|---|
| walk (side) | side view + `walk` phase: diagonal leg pairs swing and lift | travelling between beats, "the customer journey" |
| `turn` / `spinView` | drawn turn through the key views with a smear | turning to the camera to address the viewer, turning to a reveal |
| smear | dry-brush streaks + speed lines behind a fast move | a zip in or out of frame, whip-pan transitions |
| `jump` | crouch, stretch, arc, squash-land | celebration, hopping onto a product, onto a stat |
| `take` | squash, then a big stretch that springs back | **the reaction to any reveal**; pair it with `surprised` |
| lid | lunchbox mouth | chomp, shout |
| `stroll` | an eased walk that stops facing front | walk on, stop, present |
| `spring` / `ring` | damped wobble after events | settles for props, logos and hats landing |
| `arcPt` | a thrown arc | tossing a product or coin, a "send" gesture |
| `onTwos` | 12-drawing timing | a snappier hand-drawn feel |
| `shakeXY` | camera shake | impacts, a big stat landing |

### 4.7 Dances: `move(style, t, seed)` / `dancer(x, y, u, style, t, extra)`

All beat-locked; combine one with a face (`{ ...move('bounce', t), eyes: 'happy', mouth: 'grin' }`).

| style | what | reel use |
|---|---|---|
| bounce | bob with alternating arm swings | the default music-sync loop |
| hop | big hops, arms up | hype, a drop |
| roof | arms up, "raise the roof" | the celebration end card |
| sway | side-to-side lean | chill, lifestyle |
| spin | a drawn spin through the key views once a bar | a flourish on a bar line |
| wave | one arm waving | hello or goodbye, the CTA "come visit" |
| walk | beat-locked walk cycle | marching to a beat |
| run | fast legs, lean forward, arms pumping | "hurry, sale ends", speed claims |
| idle | small bob | background characters |
| stomp | heavy alternating stomps | power, a strong claim |
| shimmy | quick side shimmy, arms up | playful promo |
| mix | changes style every 2 bars | a long music-video loop |

### 4.8 Transitions, camera, light and paper

- **Transitions:**
  - `brushWipe` (shot to shot, in brand colours via `cols`);
  - `iris` (open on or close to a character);
  - `irisShape` (a client logo silhouette, a heart, a star, a speech-bubble shape as the iris:
    strong for end cards);
  - `flash`.
  - The guide's other options (whip pan + smear, match cut, cut on action, camera carry, fade or push
    from paper) are techniques, not helpers.
- **Camera:** `camBegin`/`camEnd` drift and push; `kf` camera paths; `shakeXY`; `toScreen` for aiming.
- **Light:** `glow` for lamps, screens, stars, magic, a product "shine" and the bulb emote.
- **Paper:** the cream paper texture and multiplied grain + vignette on every frame. The paper can show
  through, which is a valid look.

### 4.9 Demo props and set pieces (`src/scenes/demo.js`, examples to learn from, not to copy)

- **`sky(t, horizon, ripple)`:**
  - a night wash;
  - violet and indigo watercolour clouds;
  - 42 twinkling stars, each on its own clock and boil seed;
  - a moon;
  - an optional **ripple**: a wave of twinkles spreading from a point (a great "it worked!" payoff).
- **`hill(cx, cy, rx, ry, col, t, tufts)`:** wash + fill ellipse hills with swaying grass tufts.
  `hillY()` puts characters on the slope (and tilts them to it).
- **`starling(x, y, r, {glow, sad, rot})`:**
  - a five-point star character with a face: sad or happy, dim to bright glow;
  - **the template for turning a client's product into a sidekick character.**
- **`sparkle(x, y, r, k)`:** a popping 4-point sparkle.
- **Falling-star trail:** a `ribbon` through the star's last 7 positions (a closed-form motion trail).
- **Shot A:**
  - iris open -> `sleepy` -> star falls (with camera push and shake on landing) -> `surprised` ->
    `idea` -> turn -> side trot down the slope -> brush wipe.
- **Shot B:**
  - the wipe continues -> trot -> stop -> 3/4 turn -> crouch -> lift the star overhead -> wind-up ->
    throw on an arc with a sparkle trail -> sky ripple -> `love` -> wave -> star twinkles back ->
    iris to Clawd, hold, shut.
  - Every read has a timing note.

---

## 5. How a client reel can use it

| reel moment | what to build with the kit |
|---|---|
| **Brand mascot** | Redraw Clawd's body as the client's mascot or product-as-character, in their colours (section 6). Use the 31 emotions as its acting library across a series |
| **Explainer host** | A medium-shot host (u ≈ 24) who reacts to each point: `confused` at the problem, `idea` at the solution, `determined` at the steps. Props via `armR`; diagrams painted in `paint()` beside it |
| **Reaction moment** | A 1–2 s cutaway inside a motion-graphics reel: `surprised` + `take` + `!` right after a stat or price reveal; `starstruck` at a feature; `ko` at "the old way" |
| **Hook (first 2 s)** | Open mid-action: a smear-zip into frame, a take, `!!`. Never open on a still character |
| **Transitions** | `brushWipe` in brand colours between motion-graphics scenes gives the whole reel a hand-made seam; an `irisShape` of the logo is the outro |
| **End card** | Mascot `proud`/`happy` + `roof` or `wave` dance on the beat beside the logo (logo and CTA from our own type layer) |
| **Music-driven promo** | Set `bpm`/`offset` from `beats.py`; every idle, dance and pulse locks to the track |
| **Series content** | One mascot, a different emotion and hat per episode: a consistent, cheap-to-extend character library |

**Where it doesn't fit:** product UI, data, kinetic type, a photographic premium look. Those stay in our
canvas/HyperFrames engines; the painted segment is cut in.

---

## 6. Adapting it to a client's character and brand colours

- **Brand colours on Clawd:**
  - Pass `col`/`dk`/`lt` per call (body, shadow side, highlight).
  - Or change `PAL.clay`/`PAL.clayDk`/`PAL.clayLt` once. `clawd()` reads `o.col || PAL.clay`; note
    the default highlight is a hard-coded `#F5B394`, not `PAL.clayLt`.
  - Mood tints then mix into the brand colour automatically.
  - Keep `dk` about 25–35% darker than `col`, and `lt` lighter and warmer.
- **The world palette:**
  - Replace `PAL` entries with a small palette built from the brand (2 or 3 brand colours plus soft
    neutrals).
  - Keep `paper` and `ink` soft: no #000 or #FFF.
  - **Watch pigment mixing:** brand yellow over brand blue turns green. Layer light over dark with
    `wash` at 255, and use `glow()` for anything that shines.
- **Wipes in brand colours:** `brushWipe(p, [brand1, brand2])`.
- **A different character:**
  - Write `mascot(x, y, u, o)` modelled on `clawd()`:
    - `boilSeed` per part (`rs('body')`, `rs('arm' + which)`...);
    - a body outline from `rectPts`/`rrPts`/`ellPts`/`ribbon` painted with `wash` + a separate ink
      pass;
    - shading via one or two `fill` shapes (or washes, for speed);
    - arms with `armL`/`armR` hooks;
    - its own `VIEWS` table (front/q/side/qback/back) so `turn()`/`spinView()` work unchanged.
  - **Reuse the acting for free:**
    - `feel()`, `emotions()` and `move()` return character-agnostic pose fields (`dy`, `sq`, `rot`,
      `dx`, `aL`, `aR`, `lookX`, `lookY`, `squint`, `blush`, `gloom`, `emote`...).
    - So any character that honours those fields inherits all 31 emotions, the takes and the 12
      dances.
    - Call `eyes(u, o, sw, sides)`, `mouth(u, m, sw)` and `emote(...)` inside your character's
      transform (eyes are laid out at ±2.5u, -6u in a 10u-wide box: scale and translate to fit).
  - Add brand-specific emotions to `EMO` (eyes, mouth, tint, emote, `take`, `body(t)` using `_b(t)`
    for the beat).
- **Product as character:** follow `starling()`: the product's silhouette as one `paint` shape + ink,
  a simple face (two dot eyes and a line mouth), a `glow` for shine, `sad`/happy variants. Then it can
  be carried in `armR`, thrown on `arcPt`, and react.
- **Client logo:**
  - Never as a painted bitmap inside the frame. Use it as an `irisShape` silhouette (point list from
    its outline) or overlay it in our compositor.
  - Painting a logo with p5.brush distorts it, which brand guidelines won't allow.
- **Format 9:16:**
  - Change `const W = 1920, H = 1080` in `core.js` to `1080, 1920`.
  - Change `<canvas id="out" width height>` and the CSS `aspect-ratio` in `studio.html`.
  - Optionally change `--window-size` in `render.mjs`.
  - `paper`, `grain`, `brushWipe`, `iris` and `flash` all read W/H. `sheets.js` is laid out for
    landscape (sheets only).
  - Stage vertically: Clawd lower-middle at u ≈ 28–40 (it's wide, so in 1080 px use a closer size than
    in 16:9), keep clear of the platform UI zones in `motion-studio/CLAUDE.md` (top 250 px, bottom
    400 px, right 140 px), and stack set pieces vertically.
  - **Tested here** (section 8): u = 44 reads as a medium close-up on 1080 px wide.
- **Text and claims:** the kit's no-text rule stays for the painted layer. Headlines, prices and CTAs go
  on top in our type layer, timed with the reads (the painted act leaves room for the copy, then the
  copy lands, one read at a time).

---

## 7. Where it plugs into our reel pipeline

1. **Brief -> storyboard.**
   - Use the guide's `STORYBOARD.md` format (logline, world, motif, arc, shots with timed reads, a
     transition at every seam) for the character segments.
   - Its "write the reads" timing sheet is worth adopting for the **whole reel**, not just the
     character parts.
2. **Build:**
   - A project copy of the kit per client (`cp -r` the skill folder, as SKILL.md says).
   - Set `PROJECT.bpm`/`offset` from our `beats.json` so the painted segment shares the reel's pulse.
3. **Review:**
   - The kit's `--sheet`/`--strip`/`--crop`/`--crop-at` is better than our `stills.mjs` for character
     work: strips show every frame of a take.
   - Use the same scoring loop from `motion-studio/CLAUDE.md`.
4. **Render:**
   - `--frames --workers=N` then `--encode --chrome=...` (resumable). Here, plan ~5 s/frame low-fill
     and ~45 s/frame full-fill; see section 8.
   - Output 24 fps 1080p (or 1080x1920 after the format change).
5. **Composite into the reel:**
   - Bring the MP4 in as a full-frame segment or cutaway.
   - Conform to our 60 fps by **duplicating frames** (`ffmpeg -i clawd.mp4 -vf fps=60 ...`). Don't
     interpolate: hand-drawn holds are the look.
   - Seams: a `brushWipe` at both ends in the reel's colours, or a match cut on the colour field.
   - For a character **over** our motion graphics you'd need alpha (no paper, no grain, a transparent
     WebGL clear, PNG export). That's possible in principle but untested, so prefer full-frame painted
     segments.
6. **Sound:**
   - `--audio=` muxes a track. In our pipeline, the reel's master mix happens in `finish.sh`, so
     render the segment silent.
   - Place SFX (boing on the take, pop on the emote, swish on the smear) at the same times.
7. **Paper texture as a unifier:** porting `makePaper()`/`makeGrain()` into our canvas engine lets
   the motion-graphics scenes sit in the same paper as the painted ones.

---

## 8. Running it here (tested 12 Oct 2026, this container)

**Setup** (scratch copy at `$SCRATCH/cab-test/`):

```bash
cp -r references/claude-animation-base/. $SCRATCH/cab-test/ && cd $SCRATCH/cab-test
npm install                       # 4.3 s: p5 2.x, p5.brush 2.2.x, puppeteer-core 25
node gpu_probe.mjs /opt/pw-browsers/chromium-1194/chrome-linux/chrome
#   angle-vulkan / gl-egl / angle-gl-egl / kit-default  ->  "no WebGL context" (no GPU): --soft-gl is mandatory
```

**Two fixes were needed:**

1. **Fonts.**
   - Symptom: `TimeoutError: Navigation timeout of 30000 ms exceeded` at `page.goto`.
   - Cause 1: `studio.html` loads Permanent Marker from fonts.googleapis.com, and headless Chromium
     doesn't use the sandbox's HTTPS proxy, so that request hangs.
   - Fix: self-host the font (curl through the proxy works).

     ```bash
     mkdir -p assets/fonts
     curl -sS -o assets/fonts/PermanentMarker.woff2 https://fonts.gstatic.com/s/permanentmarker/v16/Fh4uPib9Iyv2ucM6pGQMWimMp004La2Cfw.woff2
     # studio.html: replace the <link ... fonts.googleapis.com ...> with
     # <style>@font-face { font-family: "Permanent Marker"; src: url(assets/fonts/PermanentMarker.woff2) format("woff2"); font-display: block; }</style>
     ```

2. **Timeouts.**
   - Cause 2, even with the font local: under SwiftShader p5's automatic first `draw()` (the first
     frame, with p5.brush shader compilation) blocks the page for **22–54 s**. `setup()` itself took
     0.27 s.
   - `render.mjs` waits with puppeteer's default 30 s navigation timeout (`networkidle0`), so it fails
     randomly.
   - Fix (in the project copy):

     ```js
     await page.goto(url + '?render', { waitUntil: 'load', timeout: 0 });
     await page.waitForFunction('window.ready === true', { timeout: 0, polling: 500 });
     ```

**Commands that work:**

```bash
CH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
node render.mjs --chrome=$CH --soft-gl --loop=emotions --sheet=1 --cols=1 --w=1920 --out=out/emotions.jpg   # model sheet
node render.mjs --chrome=$CH --soft-gl --sheet=1.0,2.6,4.4,7.5 --cols=2 --w=960 --out=out/demo_sheet.jpg    # contact sheet
node render.mjs --chrome=$CH --soft-gl --frames --range=0:1 --workers=2 && node render.mjs --chrome=$CH --encode --out=out/video.mp4   # parallel frames, then encode
node render.mjs --chrome=$CH --soft-gl --clip --range=0:4 --out=out/clip.mp4                                  # straight to MP4 (one worker)
```

**Measured timings.**

- Setup: 4 vCPU, no GPU, SwiftShader. Other sessions were rendering at the same time (load average
  4–23), so wall times are pessimistic.
- **CPU-seconds** come from sampling the whole Chrome process tree. They're the contention-proof
  number.
- **Only trust wall totals and `--clip` per-frame times.** `--sheet`'s per-frame `ms` is misleading on
  software GL: GPU work is asynchronous, so each frame's cost shows up one frame late (the first frame
  always reads ~0.25 s).

| run | result |
|---|---|
| startup (launch + the automatic first `draw()`) | 22–54 s, longer with fills in the t=0 frame |
| **emotions model sheet** (1 frame, 31 Clawds, ~190 fills) | **351 s** for the frame, 6 m 49 s total. The output matches `docs/emotions.jpg` |
| **demo contact sheet**, 4 frames (t = 1.0, 2.6, 4.4, 7.5), **with fills** | 7 m 34 s total. Repeat frames of t=2.6: 44–53 s each; 3x t=2.6 = 219 s wall, **480 CPU-s** |
| same frames with **fills turned into flat washes** (test override, below) | 3x t=2.6 = 38 s wall, **65 CPU-s** total, almost all of it startup |
| **demo 0–4 s MP4 without fills** (`--clip --range=0:4`, 96 frames) | **4.9–5.7 s/frame**, 487 s wall, 1,447 CPU-s (~15 CPU-s/frame). Correct 1920x1080 24 fps H.264 |
| **9:16 brand test** (1080x1920, blue brand Clawd u=44 with its own fills, wash-only background) | 3 frames in 64 s wall including startup (~10 s/frame), 199 CPU-s |
| **demo 0–1 s MP4 with full fills**, `--frames --range=0:1 --workers=2` + `--encode` | 24 frames in 1,016 s wall = **42 s/frame effective**, 3,385 CPU-s (~140 CPU-s/frame). Two workers barely beat one: every page shares one SwiftShader GPU process on 4 CPUs |

**What the fills cost:**

- **Watercolour `fill` is the cost driver:** about **45–60 s/frame (~110–140 CPU-s) with the demo's
  fills versus ~5 s/frame (~15 CPU-s) without**, roughly 10x. What remains is strokes (ink outlines,
  grass tufts, hatching) and washes.
- **Full 11 s demo (264 frames) here:** ~3.5–4.5 hours with fills on one worker; ~20–25 min without.
- A GPU machine is what the README's "0.1–1 s per frame" means.

**How to work here:**

1. Block and time everything with sheets and strips in a **no-fill preview mode**. It's 10x faster and
   the acting, timing and composition are identical.
2. Ship either:
   - (a) a **low-fill design**: Clawd's own ~5 fills plus 1–3 large background fills, no
     fill-per-element; or
   - (b) the full-fill look rendered on a GPU machine.
3. Use `--frames` for long renders because it's resumable. Extra `--workers` barely help on this
   4-CPU box (one shared SwiftShader GPU process); they pay off on a GPU machine.

**The no-fill preview override** (load it after `timeline.js`, remove it for the final):

```js
// src/nofill.js: watercolour fills become flat washes of the same colour and opacity
(() => { const orig = paintAt; paintAt = (pts, o) => {
  if (!o.fill) return orig(pts, o);
  const q = { ...o, fill: null }; if (!o.wash) { q.wash = o.fill; q.washOp = o.fillOp ?? 170; }
  return orig(pts, q); }; })();
```

**What no-fill looks like:**

- Clawd is nearly identical.
- Watercolour clouds and sky glows become hard-edged translucent polygons.
- The falling star's ochre trail turns into a plain cream streak.
- Backgrounds lose most of the painterly bleed, so it's a preview mode, not a finishing look.

**Ideas to try, untested:**

- Render static background fills once per boil drawing and reuse them (memoise per
  `(shot, BOILN % 3)`). It stays deterministic.
- `pixelDensity(.5)` for drafts.

**9:16 test** (it works). Edits in the project copy:

- `core.js`: `const W = 1080, H = 1920`.
- `studio.html`: canvas `1080x1920`, CSS `aspect-ratio: 9 / 16`.
- `clawd.js`: `lt: o.lt || PAL.clayLt` (it was hard-coded `#F5B394`).
- The scene sets `Object.assign(PAL, { clay: '#2F6FE4', clayDk: '#1C4AA6', clayLt: '#8DB2F7' })`.

The result: thinking -> surprised (take, `!`) -> excited (spark), with the party hat, all in brand blue
with mood tints still mixing in.

**Test artefacts** (scratchpad, not kept in the repo): `cab-test/out/{emotions.jpg, demo_sheet_fill.jpg, bench_fill.jpg, demo_fill_0-1s.mp4, strip_fill_0-1s.jpg}`,
`cab-nofill/out/{demo_sheet_nofill.jpg, demo_nofill_0-4s.mp4, contact_0-4s.jpg}`,
`cab-916/out/brand916_sheet.jpg`.

---

## 9. Pitfalls

- **Software GL is slow** (section 8): ~5 s/frame without watercolour fills and ~45–60 s/frame with
  the demo's fills. A single sheet frame with 31 Clawds took 6 minutes.
  - Preview in no-fill mode.
  - Design with washes and hatching, and save `fill` for a few large shapes.
  - Small `--w` doesn't help: the full 1920x1080 frame is still painted.
  - Final-render a fill-heavy look on a GPU machine (the README's "0.1–1 s per frame" assumes one).
- **`--sheet`'s per-frame ms is misleading on software GL** (asynchronous GPU; costs show up one frame
  late). Benchmark with `--clip` or with wall totals.
- **The 30 s navigation timeout** and the **Google Fonts link** (section 8): patch both in every
  project copy.
- **`--encode` also needs `--chrome=`** (or `CHROME_PATH`). render.mjs looks Chrome up before it checks
  the mode, so a plain `node render.mjs --encode` exits with "Chrome not found".
- **`--encode` reads `out/frames/f%05d.jpg` from frame 0.** A `--frames --range` that doesn't start at 0
  won't encode as is (use `--clip --range` for a mid-film excerpt).
- **Large watercolour fills flicker.** In the full-fill render, the big violet sky fill changed density
  visibly between boil drawings (12/s). On large background areas it reads as flicker, not boil. Keep
  big fills at low `fillOp`/`bleed`, or check a strip before committing.
- **Pure functions only:**
  - no `Math.random()`, no counters, no state between frames;
  - `hash()` for fixed randomness, `jit()`/`random()` for boil;
  - frames render out of order in parallel workers.
- **Boil jitter:** forgetting `boilSeed(key)` before each element makes static things re-boil every
  frame. A NaN in a point list throws an unhelpful
  `Failed to construct 'OffscreenCanvas'` error: guard `Math.acos` and similar.
- **Strokes at large world coordinates under zoom ~2+ collapse to a dot.** `paint()`/`inkLine()` centre
  each shape to avoid it. Shapes much bigger than the canvas can still lose their outline: draw long
  edges as canvas-sized `inkLine`s.
- **Outline weight scales with camera zoom:** scale `sw` down in close-ups or fine lines become blobs.
- **Pigment mixing:** yellow over blue turns green, and thin washes grey things out. Use `glow()` for
  light and `wash` at 255 for light-over-dark.
- **Five `WebGL: INVALID_OPERATION ... not from the associated program` warnings** once per page are
  harmless; any other page error is real.
- **Spreading overrides:** later spreads win. **Add** `dy`/`sq` when an emotion and a pose both set
  them, or the acting silently disappears.
- **Props must touch:** held items go in `armL`/`armR`; overhead items are computed from the same pose.
  Verify with `--crop`/`--crop-at`.
- **Don't copy the demo** (night sky, hills, star, two-shot structure); the guide insists.
- **Text:** the model will want to add signs or labels; the guide forbids it. In client work all copy
  belongs to our type layer.
- **Brand logos** can't be painted with p5.brush (it distorts them): overlay them or use `irisShape`.
- **Landscape-only by default:** a 9:16 reel needs the W/H/canvas edits in section 6.
- **Mascot IP:** Clawd is Anthropic's Claude Code mascot. The kit's code is MIT, but don't put Clawd
  itself in client ads. Build the client's own character on the engine.
