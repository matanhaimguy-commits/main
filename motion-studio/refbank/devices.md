# Signature devices

This is the catalogue of film devices in the reference bank. A device is a piece of film grammar you can reuse: a
camera move, a transition, a structure, a type treatment or a material. The bank holds 107 cards: 81 TikTok and
Instagram reels, 15 YouTube Shorts (talking, conversation and story reels, added 28 Oct 2026) and 11 onetake craft
films. Each card's first device is its signature, the idea the film hangs on.

This file covers 72 devices:
- the 47 devices that are the signature of at least one card in the first bank;
- 17 secondary devices that 4 or more cards use;
- 8 talk devices from the 28 Oct 2026 YouTube Shorts (section "Talk").

Rarer devices (countdown, map-zoom, paper-cutout, progress-ring and others) are not covered; find them with
`search --tag`.

## How to use it

1. Find the client's message in the "Pick by message" table and read the 2-4 devices it suggests.
2. Pick one signature device and at most one or two supporting devices.
3. Open the example cards (`cards/<id>.md`) for timed beat maps.
4. Check the concept against the client's history.

```bash
R=motion-studio/refbank/tools/refbank.py
python3 $R search --tag zoom-through-scale                  # every card that uses a device
python3 $R search --tag before-after --max-difficulty 2     # only the cheap ones
python3 $R pick --client <client> --fit local-service --n 6 # fresh references for this client
python3 $R check --client <client> --category ui-saas --devices zoom-through-scale,whip-pan
```

`search --tag` matches any tag list on a card, so a device slug finds every card that uses it. The device is the
card's signature only when it is listed first. `pick` and `check` enforce the house rules:
- one signature device per film;
- no signature device from the client's last 3 films;
- at most one device shared with the client's last film.

## Reading an entry

The italic line under each heading gives three facts:
- how many cards use the device as their signature, out of all cards that use it;
- the difficulty range of those cards (1 is easy; 5 is not practical in our stack);
- the hooks those cards open with.

Entries run from most to least useful within each group. Plays are as captured in October 2026. Cards without plays
are onetake craft films: study only (PolyForm Noncommercial), but the best guides to how a device is built.

`thought-bubble` is a signature in the bank but is not in TAGS.md yet. Add it there before logging a film with it.

## Engines

- **canvas**: our 2D engine. It has closed-form `spring()` from `lib/motion.js` and subframe motion blur, and fakes 3D
  by projection. Every frame is a pure function of `seek(t)`.
- **HyperFrames**: HTML and GSAP on one paused timeline. Search its 447 registry effects first. It also has a Three.js
  adapter on software WebGL.
- **Lemo**: the Lemo-Opuscar painterly styles.
- **CAB**: Claude Animation Base characters.
- **collage**: the halftone paper-collage route.
- **footage**: plates the client shoots.
- **gen-image, gen-video, gen-3d**: paid, and only with approval.

Bake every simulation once, with a seed and a fixed step, then read its frames by time.

## Pick by message

| Message | Best devices | Example cards |
|---|---|---|
| We save you time | `zoom-through-scale`, `chain-reaction`, `split-screen`, `before-after` | onetake-clearing (dive to the one free half hour), onetake-knockon (one press, ten tasks done), onetake-unbroken (an hour broken vs whole), tt-peanar3d 6.0M (stop doing it by hand) |
| Before/after transformation | `before-after`, `mask-reveal`, `transformation-sequence`, `reverse-play` | tt-vfxbyhassaan 33M, ig-papertiger-animation 4.7M (reveal in the mirror), tt-arts-help 76M, tt-uede-art 39M |
| Our process, step by step | `object-carries-camera`, `assembly-build`, `timeline-progression`, `asmr-foley` | tt-madebyoddly 1.2M (logo train rides the steps), tt-allthebrickstogether 21M, tt-babyinside7 62M, tt-smile-bam 70M |
| The hidden cost of X | `escalation-ladder`, `literal-metaphor`, `rack-focus`, `seamless-loop` | tt-lights-are-off 130M (a bigger mouth behind the threat), tt-thequinettos 136M, ig-divyansh-fx-attention 348K (attention is expensive), tt-thelovelyhorrorshow 50M (the loop that never ends) |
| A number that matters | `chart-grow`, `escalation-ladder` with `big-number`, `giant-product`, `counter-ticker` | tt-foil-finance 1.5M, tt-bluxcamp 45M, tt-bricodepot 1.7M (500 pages turned into weight), onetake-ebb |
| We are different from everyone | `versus-compare`, `glitch-cut`, `pose-to-pose-comedy`, `reaction-shot` | tt-blick-thegobbler 140M, tt-pastel-shark 19M (old vs new), tt-sabujak-io 2.1M (underestimated, then the work), tt-joinpressbook 1.9M |
| Product launch | `giant-product`, `morph`, `typing-caret`, `dolly-follow` | tt-why-cgi 98M, tt-rafaellfreitaas 1.2M, onetake-launch, tt-benfryc 2.1M |
| How it works | `x-ray-cutaway`, `node-diagram`, `chain-reaction`, `assembly-build` | tt-smart-doctor 61M, tt-martaraile 3.8M, tt-greenscreencut 23M, tt-spectrazeeua5 8.8M |
| Social proof without testimonials | `pov-camera` with a real crowd, `screen-in-frame`, `reaction-shot`, `glitch-cut` (portfolio drop) | tt-anyma 71M (crowd in the foreground), tt-maxmill-ae 2.5M (real work on a real desk), tt-expalinervideos 12M (a real first-time user), tt-sabujak-io 2.1M |
| An offer / CTA | `escalation-ladder` (of persuasion), `thought-bubble`, `match-cut` (swap cut), `word-by-word` ending on a comment ask | tt-foohfooh 5.0M, ig-tall8tiny 4.5M, tt-hellobossfilms 2.7M, ig-hiddenemotions-001 2.6M |
| Explain a confusing topic | `versus-compare`, `stick-figure`, `literal-metaphor`, `minecraft-voxel` | tt-explainedbyalistair 21M, tt-clearmindtalks 28M, tt-thebioswitch 5.6M, tt-explainedusing-minecraft 4.7M |
| Logo or brand reveal | `morph`, `type-morph`, `cutting-slicing`, `inflate-deflate` | tt-rafaellfreitaas 1.2M, tt-skalitude-show 24M, tt-travisragsdale 3.4M, tt-studiotoericht 6.4M |
| Our range, menu or catalogue | `match-cut` (swap cut), `beat-sync-hits`, `softbody` ("it all fits"), `lyric-sync-type` | tt-hellobossfilms 2.7M, ig-satisfy3dverse 109M, tt-zech3d 3.0M, tt-ripkuroi 5.6M |
| Behind the scenes, proof of craft | `before-after` (process, then product), `screen-in-frame`, `assembly-build` (speed build) | tt-sushmitagabriel 12M, tt-kotsarevm 23M, tt-nicky-blender 20M, tt-jen-k4rt 4.7M |
| Event, drop or date teaser | `lyric-sync-type`, `shape-wipe`, `3d-type`, `creature-reveal` | tt-noot-ify 9.1M, tt-nemu-etoile 3.0M, tt-platsae 6.6M, tt-anyma 71M |
| The customer's pain, in their words | `word-by-word`, `literal-metaphor`, `pose-to-pose-comedy`, `rack-focus` | ig-hiddenemotions-001 2.6M, tt-thequinettos 136M, tt-oyehoye4k 13M, ig-divyansh-fx-attention 348K |
| Sell a service in a conversation (coach, consultant, agency) | `roleplay-dialogue`, `step-plan`, `escalation-ladder` (additive levels), `quadrant-matrix`, `prop-analogy` | yt-thefutur-money-first 154K (15.8x), yt-patrickdang-thirty-days 31K (17.7x), yt-codie-five-levels 214K (11.6x), yt-alexberman-orange 567K (90x) |
| A founder's story | `rise-fall-turn`, `mentor-quote`, `street-interview` | yt-noahkagan-tire-shop 8.4M (13.0x), yt-leila-character 27K (11.7x), yt-noahkagan-first-class 2.0M (3.1x) |

## Camera and space

### zoom-through-scale
*4 of 6 · diff 2-4 · hooks: beautiful-first-frame, wait-for-it, scale-shock*

- **What it is:** One unbroken zoom between levels of scale: a year to a day to a half hour, a pixel to a desktop, a
  wordmark to a city, a room to a phone screen. Each level is drawn in its own units under one transform, so type
  stays sharp at 300-440x. The zoom eases in log space, anchored to the target's screen position.
- **Why it holds:** The viewer is always inside something they have already seen. Each level asks what is inside the
  next one.
- **Examples:** Signature: tt-bymike0404 4.9M, tt-keyn-my 2.1M, onetake-clearing, onetake-pith. Also: tt-studiorat
  18M, tt-t1zzy-1 3.0M.
- **Build it here:**
  - **canvas:** a page for each level, and a log-zoom spring with a screen-space anchor. Fade detail in by on-screen
    size. Never scale bitmaps.
  - **Phone portal:** footage, with a corner-pinned screen in HyperFrames.
  - Difficulty 3, or 2 with footage.
- **Business uses:**
  - Salon: a fully booked month, then a dive to the one free slot and "Book it".
  - Taxi firm: the wordmark becomes the town, and the car becomes the tracking dot.
  - Course platform: start inside one letter, then pull out to the course.
- **Watch out:** Plan something new at every level, or it is just a slow push.

### x-ray-cutaway
*2 of 5 · diff 2-4 · hooks: question, text-headline, relatable-pov*

- **What it is:** The shell of a closed object turns see-through to show the working parts. In one camera move the
  wall fades to about 40%, the camera tips top-down and holds 6 s while the parts move on the sound, then returns to
  frame one. The 2D trick is a green-screen phone slid over a closed box, keyed to a plate of the open box.
- **Why it holds:** It answers the question everyone has: what is inside? Sound synced to the motion rewards the
  hold.
- **Examples:** Signature: tt-smart-doctor 61M, tt-martaraile 3.8M. Also: tt-babyinside7 62M, tt-thebioswitch 5.6M,
  tt-zackdfilms92 4.5M.
- **Build it here:**
  - **Stylised:** canvas layers with a fake-3D tilt.
  - **Photoreal:** a client GLB in HyperFrames Three.js, or gen-3d.
  - **Phone trick:** ffmpeg chromakey (similarity about 0.15, blend 0.05).
  - Difficulty 2 (phone trick) to 4 (photoreal).
- **Business uses:**
  - Dental clinic: a tooth turns glassy, and the camera tips down into the root canal.
  - Skincare shop: a phone slides over a sealed gift box and shows the products inside.
  - Appliance brand: the shell fades, and the brew chamber cycles on a click track.
- **Watch out:** Photoreal anatomy painted in 2D looks wrong. Go stylised or get a real model.

### screen-in-frame
*3 of 6 · diff 2-3 · hooks: text-headline, series-hook, wait-for-it*

- **What it is:** The work plays on a real monitor or tablet, filmed by a phone from about 1.2 m. It fills the middle
  third of the frame, with the desk, the software and the hands visible. A fixed "POV: ..." caption names the series.
  Often the hands make the piece first (3-5 s), then play it (2-7 s).
- **Why it holds:** It reads as someone's real work, not an ad. Making it, then playing it, shows the how before the
  wow.
- **Examples:** Signature: tt-kotsarevm 23M, tt-maxmill-ae 2.5M, tt-matthewmotiondotcom 2.5M. Also: tt-bymike0404
  4.9M, tt-martaraile 3.8M, tt-keyn-my 2.1M.
- **Build it here:**
  - Build the piece in HyperFrames.
  - The client films their own monitor playing it.
  - Or corner-pin it into a desk photo in canvas, with drift and screen glow.
  - Difficulty 2.
- **Business uses:**
  - SaaS founder: "Would you pay for this?", then the feature plays on the office monitor.
  - Agency: "POV: we make ads for local brands", with one real business per episode.
  - Coffee roaster: the logo bursts into beans on a tablet at the counter.
- **Watch out:** Small type will not read inside a filmed screen. Use big shapes and one accent colour on black.

### pull-back-reveal
*0 of 8 · diff 2-5 · hooks: wait-for-it, text-headline*

- **What it is:** The film ends by pulling back, usually from 1x to about 0.15x in 1-2 s on a spring. The wide view
  shows what the parts were part of: a domino course shaped like the icon, or a brush circle that is the o of the name.
  Hold it long enough to read.
- **Why it holds:** It answers the "what is this making?" question raised by the close-ups.
- **Examples:** tt-arts-help 76M, tt-vfxbyhassaan 33M, tt-jen-k4rt 4.7M, onetake-knockon, onetake-unbroken (+3 more).
- **Build it here:**
  - In canvas, one scale transform with a spring settle.
  - Draw in scene units, so the wide view stays sharp.
  - Design the final layout first.
  - Difficulty 2-3.
- **Business uses:**
  - Online shop: packed, shipped, delivered, and the course turns out to be the logo.
  - Web agency: the founder's clip shrinks into the hero image of the live site.
- **Watch out:** The final shape must be the client's real mark or product, and it must read at 360 px.

### rack-focus
*1 of 2 · diff 2-3 · hooks: bold-claim, text-headline*

- **What it is:** Each spoken phrase gets one centred prop on a plain field. Focus pulls replace cuts: the old prop
  blurs out as the new one sharpens from the same radius, in about 0.2 s (tens of px on a 1080 frame). One accent
  colour marks each key word.
- **Why it holds:** There are no hard cuts, and a new prop arrives every 1-2 s.
- **Examples:** Signature: ig-divyansh-fx-attention 348K (behind StraightScale reel 03). Also: onetake-overlap.
- **Build it here:**
  - In canvas, make the blur radius a spring on each layer.
  - Draw the props in code for the client. The hard part is keeping them specific, not generic icons.
  - Difficulty 2.
- **Business uses:**
  - Bookkeeper: what late books cost, shown with an overdue stamp and a cash-flow line.
  - Physio clinic: what waiting costs, shown with a clock hand, a booking ring and the real services.
- **Watch out:** StraightScale has already used it. Generic props turn it into a template.

### top-down-plan
*0 of 6 · diff 3-4 · hooks: wait-for-it, mid-action-start*

- **What it is:** The camera looks straight down. Height shows only through shadow offset and blur, plus a slight
  scale-up. It reads a layout as a plan, or swaps what the ground means. In tt-letwins the floor beside a bed is a
  skyscraper drop, then a hard cut in the same frame shows floorboards.
- **Why it holds:** It shows a whole system at once, and a change of ground can carry a reveal.
- **Examples:** tt-letwins 133M, tt-smart-doctor 61M, tt-allthebrickstogether 21M, tt-spectrazeeua5 8.8M (+2 more).
- **Build it here:**
  - In canvas, scale shadows by zoom by hand.
  - For live action, mount the phone on the ceiling, shoot two takes and use a static mask.
  - Give objects coloured edges, and use face-up labels at 44 px or more.
  - Difficulty 3.
- **Business uses:**
  - Bookkeeper: one upload runs through sorted, matched and filed.
  - Mattress shop: the bed's edge is a canyon, then a cut to the floor and the wider bed.
- **Watch out:** Without motion or a change of ground, it is just a diagram.

### one-take-camera
*0 of 6 · diff 3-4 · hooks: wait-for-it, beautiful-first-frame*

- **What it is:** One camera and no cuts. Scenes change as the camera travels, zooms or whips, or as an object
  transforms. The camera leads its subject by 0.1-0.2 s, with springs on position and log zoom. A faint far layer
  makes the movement readable.
- **Why it holds:** There is never a cut to leave on.
- **Examples:** tt-allthebrickstogether 21M, onetake-clearing, onetake-ebb, onetake-launch, onetake-one-dot,
  onetake-pith.
- **Build it here:**
  - Use one canvas rig and one world.
  - In HyperFrames, make sections sub-compositions under one camera.
  - A fixed-camera draft of onetake-one-dot was rejected because the camera did not lead the subject.
  - Difficulty 3-4.
- **Business uses:**
  - Event organiser: three event types typed into one bar, each opening its real poster.
  - Flat-pack furniture: the camera rises with the build.
- **Watch out:** Keep each section to 3-4 s, or the travel drags.

### pov-camera
*1 of 11 · diff 1-5 · hooks: scale-shock, impossible-object, beautiful-first-frame*

- **What it is:** The camera is a person: a plane passenger, a balcony bystander, a swimmer or a diver. Their position
  stays in frame (a window across about 20% of a corner, a stranger's shoulder, their own fins). The shot is handheld
  or floating, with one consistent parallax.
- **Why it holds:** It puts the viewer in the scene and makes the impossible feel filmed.
- **Examples:** Signature: tt-vaporama-vision 95M. Also: tt-borisao-blois 156M, tt-lights-are-off 130M, tt-why-cgi
  98M, tt-cgsick 77M (+6 more).
- **Build it here:**
  - Footage first: a gimbal at water level, or a plate shot from a balcony.
  - Drawn: a canvas camera spline with a seeded bob and a foreground frame layer.
  - gen-video gives weak camera control.
  - Difficulty 2 with footage, 4 drawn.
- **Business uses:**
  - Hotel: a dawn float through their real, empty pool.
  - Boat tours: a window view of a huge shadow in the bay, then the boat heads out.
- **Watch out:** Give it a boundary, a far goal and one detail that escalates, or it is a screensaver.

### dolly-follow
*1 of 3 · diff 3-4 · hooks: beautiful-first-frame, guess-challenge*

- **What it is:** The camera tracks beside its subject at a fixed offset. On a product, a close long lens slides along
  the edge so features arrive in order, each with 1-3 s, one physical action and one small caption. On a moving
  subject, a lag spring keeps it in the centre third.
- **Why it holds:** The next thing is always entering frame, and a quiet tour reads as premium.
- **Examples:** Signature: tt-benfryc 2.1M. Also: ig-satisfy3dverse 109M, tt-thexoutliners 23M.
- **Build it here:**
  - Use client renders or macro photos in HyperFrames, with lateral pans and layer parallax.
  - Physical actions need render sequences.
  - Difficulty 3 with renders, 5 without.
- **Business uses:**
  - Homeware shop: a lamp tour ending on a relit "Available now" card.
  - Equipment maker: macro pans over real machine photos.
- **Watch out:** The reference uses 22-26 px captions; our minimum is 44 px. Keep the restraint in the type weight,
  not the size.

### orbit
*0 of 5 · diff 3-5 · hooks: beautiful-first-frame, sound-hook*

- **What it is:** A slow, steady arc of 90 degrees or less around a hero object. It ends on a hold, or lands on a new
  view such as top-down or a buoy carrying the logo. It proves the object is 3D.
- **Why it holds:** Parallax shows volume, and the slow pace gives viewers time to look.
- **Examples:** tt-smart-doctor 61M, tt-nicky-blender 20M, tt-platsae 6.6M, tt-kaybojesendk 3.1M, onetake-domino.
- **Build it here:**
  - canvas fake 3D. Stacked-copy extrusion holds only to about 35 degrees.
  - Three.js for one mesh.
  - gen-video or gen-3d for photoreal.
  - Difficulty 3-4.
- **Business uses:**
  - Developer: an arc around the scale model, landing on the project name.
  - Coffee machine brand: an orbit, then the shell turns see-through.
- **Watch out:** Without a reveal at the end of the arc, it is a turntable.

## Transitions

### morph
*3 of 9 · diff 2-4 · hooks: wait-for-it, text-headline, brand-name-drop*

- **What it is:** One object never leaves the screen; each new state is that object reshaped. A dot becomes a caret,
  a ring, a ball, then the dot on the i of the name. Boxes spring their position, size and corner radius into the next
  box in 0.3-0.5 s, with slight overshoot. A logo can land the same way, as a blob that squashes about 30%.
- **Why it holds:** Nothing appears from nowhere, and viewers wait to see what the object becomes.
- **Examples:** Signature: tt-rafaellfreitaas 1.2M, onetake-one-dot, onetake-skill-demo. Also: tt-skalitude-show 24M,
  tt-kotsarevm 23M, tt-maxmill-ae 2.5M (+3 more).
- **Build it here:**
  - **Shapes:** canvas, with each state a parametric shape and springs from `lib/motion.js`.
  - **Boxes:** HyperFrames FLIP-style morphs.
  - **Logo endings:** a mask over the official SVG.
  - For a circle-to-path change, cut the ring and map its arc length onto the path.
  - Difficulty 2-3.
- **Business uses:**
  - Payments app: the logo dot becomes the transfer caret, then a balance curve, then the logo again.
  - Invoicing tool: an invoice line becomes a payment card, then a paid row.
  - Restaurant: three drops of sauce merge and land as the round logo.
- **Watch out:** Container morphs on their own look like every SaaS reel (onetake-skill-demo was rejected for this).
  Add a concept, and never redraw the logo.

### mask-reveal
*3 of 7 · diff 2-3 · hooks: mid-action-start, wait-for-it, familiar-ip*

- **What it is:** A shape cuts through one layer to show another. Giant words, 50-90% of frame height, can sit
  between the plate and the matted subject. Light can flood the frame and drain as rings that open on the next scene.
  Two halftone plates can read as noise until they line up.
- **Why it holds:** Layers add depth, and every opening asks what is behind it.
- **Examples:** Signature: tt-wonton-aep 18M, onetake-ebb, onetake-overlap. Also: tt-brknsergio 46M,
  ig-papertiger-animation 4.7M, tt-martaraile 3.8M, tt-rafaellfreitaas 1.2M.
- **Build it here:**
  - **Text behind the subject:** HyperFrames with client footage and local matting (the embedded-captions workflow
    or `hyperframes remove-background`). Pick slow subjects so the mattes stay clean.
  - **Rings and halftones:** canvas, with dithered gradients and multiply blending.
  - Difficulty 2-3.
- **Business uses:**
  - Estate agent: one giant selling-point word per room, behind the agent.
  - Day spa: the booking time floods with light, and the rings open on the confirmation.
  - Wedding planner: two names in two inks; the ampersand appears only when the plates line up.
- **Watch out:** Text behind the subject is a trend look. It needs a real subject and a real line.

### match-cut
*3 of 6 · diff 2-3 · hooks: text-headline, sound-hook, mid-action-start*

- **What it is:** A hard cut where one thing keeps its position, scale or silhouette while everything else changes.
  It can be the same top-down lock-off with new ground, or a jump pose cut to a drawn hero in the same silhouette (5 s
  cycles: 1.5 s live, 0.5 s portal, 2.5 s world, 0.5 s back). It can also be a locked table where only the product
  swaps, about every 0.5 s on the beat.
- **Why it holds:** The eye carries the motion across the cut, so the change reads as one event.
- **Examples:** Signature: tt-letwins 133M, tt-brknsergio 46M, tt-hellobossfilms 2.7M. Also: tt-bymike0404 4.9M,
  tt-audiosorf 3.6M, tt-nemu-etoile 3.0M.
- **Build it here:**
  - Cut client footage in HyperFrames.
  - Shoot on a tripod with taped marks and locked exposure, all in one session.
  - Draw the far side of each cut in Lemo or canvas, tracing the live pose.
  - Difficulty 2-3.
- **Business uses:**
  - Cafe: a TV remote zaps the table through the menu, one item per beat.
  - Travel agency: a bounce on a hotel bed, then a dive into four painted destinations.
  - Insurance broker: a desk beside a drawn flood, then a cut to the dry office.
- **Watch out:** Any position mismatch reads as a mistake. Shoot from a shoot sheet.

### seamless-loop
*2 of 15 · diff 1-4 · hooks: sound-hook, beautiful-first-frame*

- **What it is:** The last frame leads straight into the first. A closed cycle swaps its state back (two 4 s cycles,
  so frame 8.0 equals frame 0.0), or a machine runs an exact 3.0 s period. A whip loop ends in a directional blur that
  the first frame resolves, matched in direction and colour.
- **Why it holds:** Replays count as watch time, and late arrivals stay for the start.
- **Examples:** Signature: tt-thelovelyhorrorshow 50M, tt-crannyjr-utd 24M. Also: tt-blick-thegobbler 140M,
  tt-lights-are-off 130M, ig-satisfy3dverse 109M (+10 more).
- **Build it here:**
  - In canvas, make the cycle period divide the film length, and compare the first and last frames.
  - For a whip loop, share one streak layer across both ends.
  - Trim generated video to the cycle and cross-fade the join.
  - Difficulty 1-2.
- **Business uses:**
  - Bookkeeping SaaS: each cube eats a receipt and becomes the next one, until the app sorts it.
  - Barbershop: a clipper pass, a mirror turn and a nod, then a whip back to the start.
- **Watch out:** An end card breaks the loop. Put the brand inside the cycle.

### object-carries-camera
*1 of 2 · diff 2-3 · hooks: brand-name-drop, series-hook, wait-for-it*

- **What it is:** A moving object carries the camera from scene to scene. The logo's arrow, cut into 5-6 cars, rides
  a metro line. At each station a circle wipe centred on the train opens a card showing a "NOW AT" pill, a giant word
  and the product step. At the end the train reverses back into the logo.
- **Why it holds:** A route turns each stop into a promised arrival, and the logo carries both the reveal and the
  structure.
- **Examples:** Signature: tt-madebyoddly 1.2M. Also: tt-keyn-my 2.1M.
- **Build it here:**
  - Use canvas, and vectorise the logo with `tools/vectorize_mark.py`.
  - Place each car by arc length along the track.
  - Put the wipe radius on a spring, and morph back into the mark over 0.6 s.
  - Difficulty 3.
- **Business uses:**
  - Bakery: the logo scooter rides order, bake, box, deliver.
  - SaaS: the logo rides sign up, connect, import, launch, with each card a real screen.
- **Watch out:** Part of the logo must be able to move plausibly. Keep it to five or six stops at most.

### cut-on-beat
*0 of 16 · diff 2-3 · hooks: sound-hook, familiar-ip, pattern-interrupt*

- **What it is:** Every cut, word swap or world change lands on a beat. A typical rate is a cut every 0.5-1 s, with
  one 1-1.5 s hold as the only rest.
- **Why it holds:** When picture and sound agree, the film feels right before the viewer knows why.
- **Examples:** tt-crannyjr-utd 24M, tt-studiorat 18M, tt-wonton-aep 18M, tt-sushmitagabriel 12M (+12 more).
- **Build it here:** Run `beats.py audio/track.wav > beats.json`, then cut from that grid. The music must be generated,
  licensed or supplied. Difficulty 2.
- **Business uses:**
  - Gym: a member's real lift, cut on the beat.
  - Restaurant: the menu, one item per beat.
- **Watch out:** Equal cut lengths read as slides (the onetake-motion-web drafts were rejected for this). Vary them.

### whip-pan
*0 of 7 · diff 2-4 · hooks: text-headline, familiar-ip, beautiful-first-frame*

- **What it is:** A camera move of about 0.3 s with heavy directional blur, landing somewhere new. It might cross a
  table to whatever a face was reacting to, or snap the camera back out of a zoom.
- **Why it holds:** It adds a burst of energy, and its blur hides cuts, joins and loop points.
- **Examples:** tt-crannyjr-utd 24M, tt-wonton-aep 18M, tt-ripkuroi 5.6M, tt-joinpressbook 1.9M (+3 more).
- **Build it here:** Canvas subframe blur gives the best result. HyperFrames has whips in its registry, or add blur to
  footage in post. Difficulty 2.
- **Business uses:**
  - SaaS: the sales lead stares at an engineer's terminal, then a whip to the clean dashboard.
  - Developer: a whip tilt from the empty plot to the finished building.
- **Watch out:** Use two or three at most in a film; more is noise.

### shape-wipe
*1 of 3 · diff 2-3 · hooks: sound-hook, brand-name-drop*

- **What it is:** A circle or block wipe brings in a new flat-colour world in about 0.25 s. One emblem, about 15% of
  frame width, stays fixed near the centre throughout. Each world has one saturated colour and one family of elements,
  and the emblem's ring changes style each time.
- **Why it holds:** The fixed emblem anchors the eye, so the world can change very fast.
- **Examples:** Signature: tt-nemu-etoile 3.0M. Also: tt-ripkuroi 5.6M, tt-madebyoddly 1.2M.
- **Build it here:**
  - Make SVG rings in HyperFrames, after searching the registry.
  - Put one wipe on each bar from `beats.py`.
  - Keep one ring family, with one element type per world.
  - Difficulty 2.
- **Business uses:**
  - Festival: the logo holds while the wipes flip through stages, food and line-up.
  - SaaS launch: the app icon holds while each world shows one feature's icons.
- **Watch out:** Random worlds read as a student exercise. Give each world a reason.

### glitch-cut
*1 of 4 · diff 2-4 · hooks: sound-hook, relatable-pov*

- **What it is:** The outgoing shot smears into vertical colour bars (2-10% of frame width, 0.3-0.5 s), and the next
  shot resolves out of them. As a signature it drives a two-part film: 6 s of lo-fi selfies and a dismissive quote, a
  hard cut to black on the punchline, then polished work at 1-2 s per clip.
- **Why it holds:** The jump from scrappy to polished is both the joke and the proof.
- **Examples:** Signature: tt-sabujak-io 2.1M. Also: tt-zackdfilms92 4.5M, tt-jydnfilms 3.5M, tt-matthewmotiondotcom
  2.5M.
- **Build it here:**
  - Use the glitch effects in the HyperFrames registry, applied to the client's real selfies and portfolio.
  - Trend audio cannot ship in client files, so build the punchline with a generated track.
  - Difficulty 2.
- **Business uses:**
  - Agency: "They asked if we just make logos", then real campaigns.
  - Kitchen fitter: "My uncle said I just put up cupboards", then finished kitchens.
- **Watch out:** As decoration, the glitch is a stock look.

### reverse-play
*1 of 1 · diff 1 · hooks: pattern-interrupt, mid-action-start*

- **What it is:** A real take played backwards. The wearer starts in the product and then throws it off to one side.
  Reversed, the piece leaps onto her and swallows her in about 2 s. A locked tripod shot of the product in motion
  follows.
- **Why it holds:** The motion is wrong in a way the brain cannot place, and the payoff comes within 2 s.
- **Examples:** Signature: tt-uede-art 39M.
- **Build it here:**
  - Shoot a locked, vertical, full-body frame.
  - At the end of the real take, hold still for 1 s.
  - Reverse, trim and grade.
  - Difficulty 1.
- **Business uses:**
  - Outerwear shop: a puffer coat leaps onto the model.
  - Bedding store: a duvet flies onto the bed and lands flat.
- **Watch out:** It needs a dramatic shape or texture. Walking and liquids look wrong in reverse.

## Structure

### before-after
*5 of 15 · diff 2-4 · hooks: transformation-promise, text-headline, relatable-pov*

- **What it is:** One subject in two states, with the change staged as the payoff. The strong versions join the
  states physically: the raw frame shrinks into its exact spot in the final over about 1.5 s, the steps land on a
  locked hero shot, or one "before" screen is repaired rule by rule. A 0.8-1 s black "loading" beat can split process
  from product.
- **Why it holds:** The promise arrives in the first second, and the viewer stays to see it kept.
- **Examples:** Signature: tt-vfxbyhassaan 33M, tt-sushmitagabriel 12M, tt-peanar3d 6.0M, ig-papertiger-animation
  4.7M, tt-chartosaur 1.7M. Also: tt-letwins 133M, tt-smile-bam 70M, tt-clearmindtalks 28M (+7 more).
- **Build it here:**
  - **Results:** footage in HyperFrames, with a spring scale on the shrinking frame.
  - **Software:** the client's real UI. Tween its fills on fixed geometry, so each fix reads as one object changing.
  - **Characters:** gen-video, CAB or canvas.
  - Difficulty 2-3.
- **Business uses:**
  - Gardener: a bare yard under "3 weeks of work" grows from plan lines into the real garden.
  - Accountant: a messy monthly summary, fixed by a three-letter rule.
  - Pet groomer: a muddy dog arrives, and the reveal comes in the grooming mirror.
- **Watch out:** A swipe between two photos is a stock template. The after must be real work; never invent results.

### assembly-build
*6 of 10 · diff 2-4 · hooks: text-headline, mid-action-start, transformation-promise*

- **What it is:** The thing builds itself from its real parts in true build order, and the name appears only at the
  end. Every part makes a physical entrance. Pieces fly from one off-frame source on short arcs and snap in bottom up,
  or layers of 1-1.5 s alternate direction (unfold, rain, roll on as a wave, slide).
- **Why it holds:** The viewer predicts the result and stays to check, and a part lands every second.
- **Examples:** Signature: tt-allthebrickstogether 21M, tt-nicky-blender 20M, ig-viscous-realm 10M, tt-spectrazeeua5
  8.8M, tt-ppt-hadi 6.9M, tt-jen-k4rt 4.7M. Also: tt-arts-help 76M, tt-vfxbyhassaan 33M (+2 more).
- **Build it here:**
  - Use isometric canvas, with 40-200 parts in 8-12 stages.
  - Fly each part on a parabola with a spring settle, and have the camera follow the growing edge.
  - Use HyperFrames SVG for frameworks, with a visible cursor.
  - Difficulty 3 stylised, 4 near photoreal.
- **Business uses:**
  - Developer: the real floor plans stack up into the building.
  - Burger bar: the house burger builds itself, ending on its real menu name and price.
  - Consultancy: its 4-step method as interlocking pieces, ending "Which step do you skip?"
- **Watch out:** Parts that fade in are not a build.

### versus-compare
*3 of 5 · diff 1-3 · hooks: contrast-split, text-headline*

- **What it is:** Two things in one locked frame, with everything constant except the difference. In the rule of
  three, A meets A, B meets B, then A meets B and they collide. Characters stand at 20% and 80% of the width, beats
  last about 1.6 s, and the third cuts on impact. Simpler forms are a host pointing at one of two photos, or old and
  new side by side.
- **Why it holds:** Side by side, people compare without trying, and the third beat is a punchline they half expect.
- **Examples:** Signature: tt-blick-thegobbler 140M, tt-explainedbyalistair 21M, tt-pastel-shark 19M. Also:
  tt-matthewmotiondotcom 2.5M, onetake-unbroken.
- **Build it here:**
  - Animate canvas characters pose to pose, or use CAB.
  - Build a three-pose host in HyperFrames.
  - Hold the impact for 2 frames.
  - Difficulty 1-3.
- **Business uses:**
  - Aesthetic clinic: "Botox. Filler. What's the difference?"
  - Language school: kisses, then handshakes, then one of each, colliding.
  - Rebrand: the real old logo stands stiff beside the new one, which moves.
- **Watch out:** Never mock a named competitor. Use pairs that customers really mix up.

### escalation-ladder
*4 of 8 · diff 1-4 · hooks: wait-for-it, number-ladder, guess-challenge*

- **What it is:** The same setup repeats, with one variable stepped up each round, while rig, camera and timing stay
  fixed. The variable can be softness in 11-point steps, a face count multiplied by four (about 3.5 s a round), a
  bigger predator framing the last, or a more absurd excuse. The last rung can break the pattern.
- **Why it holds:** A counter or a growing threat keeps the viewer waiting, and a twist on the last rung drives
  comments.
- **Examples:** Signature: tt-lights-are-off 130M, tt-bluxcamp 45M, tt-2f2g-labs 10M, tt-foohfooh 5.0M. Also:
  tt-vaporama-vision 95M, tt-greenscreencut 23M (+2 more).
- **Build it here:**
  - Write one canvas choreography and change one parameter per round.
  - Bake any simulation per rung.
  - Sell scale with haze, soft focus and slow speed.
  - Difficulty 2-4.
- **Business uses:**
  - Mattress shop: the same weight drops on a cross-section as the firmness climbs.
  - Insurance broker: a small leak, then storm clouds close in from the frame edges.
  - Gym: "Your trainer who will say anything to get you to the 6 am class."
- **Watch out:** Every rung number must be real and sourced. Use five rungs at most.

### chain-reaction
*2 of 2 · diff 3-5 · hooks: wait-for-it, beautiful-first-frame, mid-action-start*

- **What it is:** Every beat is physically caused by the one before. Dominoes ease in slowly and finish fast, and each
  interval is about 10% shorter, so the run speeds up. A pull-back reveals that the course traces the product icon.
  In a variant, each unit is one pixel of a picture, on a resolution ladder up to 100 x 100.
- **Why it holds:** Viewers need to see the next piece fall, and the acceleration builds tension.
- **Examples:** Signature: onetake-knockon, onetake-domino.
- **Build it here:**
  - Use canvas, all closed-form: each fall time is the path distance divided by the front speed.
  - Give tiles coloured edges, with labels at 44 px or more.
  - Draw only the tiles in view.
  - Difficulty 3 (knockon) to 5 (domino).
- **Business uses:**
  - Bookkeeper: one receipt upload knocks through sorted, matched and filed.
  - Online shop: an order click rolls through packed, shipped and delivered, across the logo.
  - Event: tickets topple into the real date graphic.
- **Watch out:** Only craft films use it so far, so there is no social proof yet. It must land on the brand.

### timeline-progression
*1 of 4 · diff 1-4 · hooks: text-headline, bold-claim, number-ladder*

- **What it is:** A process told against a visible clock in a fixed frame. A "Day N" title sits above a picture band,
  with the series title below. Each chapter is exactly 8 s, with one camera idea and one plain sentence. A date readout
  ticking at a steady rate (66 years in 13 s) works the same way.
- **Why it holds:** The counter keeps the viewer waiting, and equal chapters make the length predictable.
- **Examples:** Signature: tt-babyinside7 62M. Also: tt-thexoutliners 23M, tt-foil-finance 1.5M, tt-madebyoddly 1.2M.
- **Build it here:**
  - HyperFrames for the frame and the timing.
  - canvas for stylised cutaways.
  - gen-video only for photoreal, with one locked prompt and seed.
  - Difficulty 3-4.
- **Business uses:**
  - Dental clinic: "Implant healing, Week 1 to Week 12".
  - Physio clinic: "Torn ligament, Day 1 to Day 60".
  - Bakery: "Sourdough, Hour 1 to Hour 8".
- **Watch out:** Use real, sourced stages only, and no more than eight chapters.

### transformation-sequence
*1 of 8 · diff 2-4 · hooks: pattern-interrupt, mid-action-start, beautiful-first-frame*

- **What it is:** A tool changes a material, and both states stay visible. Each marker stroke shows as flat paint,
  then turns into grass about 0.5 s behind the nib. There are three strokes: the shape is guessable after two, and a
  pull-back confirms it.
- **Why it holds:** The lag shows the tool as the cause, and guessing the shape is a small win.
- **Examples:** Signature: tt-arts-help 76M. Also: tt-smile-bam 70M, tt-thelovelyhorrorshow 50M, tt-studiorat 18M
  (+4 more).
- **Build it here:**
  - Draw in canvas, over a locked plate.
  - Grow 40-80 seeded blades per cm on a `spring()` that starts 0.5 s after the nib passes.
  - Give the plate and the overlay the same drift.
  - Difficulty 3.
- **Business uses:**
  - Landscaper: a phone number drawn on a fence grows into turf.
  - Estate agent: a house outline drawn on a wall sprouts ivy.
  - Eco cleaner: a drawn leaf grows into moss, then wipes clean.
- **Watch out:** Without the lag between the two states, it is just a cross-fade.

### list-of-n
*0 of 10 · diff 1-3 · hooks: direct-address, mid-action-start*

- **What it is:** A run of 4-8 items given one treatment. The frame or cycle stays fixed while the item changes, and
  the count or the stakes often climb.
- **Why it holds:** The rhythm becomes predictable, and rising stakes turn the list into a ladder.
- **Examples:** tt-brknsergio 46M, tt-greenscreencut 23M, tt-explainedbyalistair 21M, tt-valor-humano3 8.1M (+6
  more).
- **Build it here:** Build one item cycle as a component and feed it data. Difficulty 1-2.
- **Business uses:**
  - Coffee shop: the drink pairs that customers confuse.
  - Branding agency: a bakery's name, then its pack, its window and its hashtag.
- **Watch out:** Without order or escalation, it is a slideshow.

### series-episode
*0 of 8 · diff 1-4 · hooks: series-hook, number-ladder*

- **What it is:** One numbered part of a series ("Day 3 of...", "Part 8"), with a fixed title band and a fixed format.
  Only the subject changes.
- **Why it holds:** A number promises more, which earns follows.
- **Examples:** tt-borisao-blois 156M, tt-smile-bam 70M, tt-bluxcamp 45M, tt-explainedbyalistair 21M (+4 more).
- **Build it here:** Make a HyperFrames template with slots for the variable content. Difficulty 1-2.
- **Business uses:**
  - SaaS: "My dad tries our invoicing app, Part 3".
  - Physio clinic: "Every desk habit that wrecks your back", one habit per episode.
- **Watch out:** Only promise a series the client will make, and make episode one stand alone.

## Type

### word-by-word
*2 of 20 · diff 1-4 · hooks: bold-claim, text-headline, relatable-pov*

- **What it is:** Text appears one word or one letter at a time, in sync with the voice. Each phrase is centred and
  sized to fill the width. Letters pop in from small with a quick fade, and one key word per line takes the accent
  colour. A sparse variant pairs long holds with a burst of one-word cuts.
- **Why it holds:** The text sets the pace and cannot be skimmed, and the accent word gives the eye a target.
- **Examples:** Signature: ig-hiddenemotions-001 2.6M, onetake-motion-web. Also: tt-clearmindtalks 28M,
  tt-thexoutliners 23M, tt-studiorat 18M (+15 more).
- **Build it here:**
  - Use the HyperFrames registry text effects, or canvas.
  - Get timings from `hyperframes transcribe`.
  - Keep body text at 44 px or more, and split long lines rather than shrinking them.
  - Difficulty 1.
- **Business uses:**
  - Couples coach: a monologue in customers' own words, ending "comment TALK for the guide".
  - Gym: "At first every workout feels easy...", ending on the timetable.
  - Accountant: a founder's year, from excitement to tax panic.
- **Watch out:** As a signature it scores the lowest wow (2 on both cards), so it usually works best as the caption
  layer under another device.

### lyric-sync-type
*7 of 11 · diff 2-3 · hooks: sound-hook, familiar-ip, pattern-interrupt*

- **What it is:** Type cut to a sung or spoken line, with a new picture for each word or phrase, about every 0.5 s.
  The picture acts the words out. It can be a hero object in a small cycle locked to the timing, a prop the line is
  written on, a literal pun, a collage card, or a hard black-and-white flip.
- **Why it holds:** Sound and picture lock on every syllable, and something new arrives twice a second.
- **Examples:** Signature: tt-studiorat 18M, tt-noot-ify 9.1M, tt-ripkuroi 5.6M, tt-audiosorf 3.6M, tt-jydnfilms 3.5M,
  tt-krxsh3 2.2M, tt-zresinn 1.8M. Also: tt-skalitude-show 24M, tt-wonton-aep 18M (+2 more).
- **Build it here:**
  - Time it in HyperFrames from transcription and `beats.py`.
  - Make the looks in collage, canvas or Lemo watercolor.
  - Build a kit of 5-8 layout templates, and drive every cycle from the timestamps.
  - Difficulty 2-3.
- **Business uses:**
  - Movers: "Comin' to your side of town", with a toy van, a compass and the phone number.
  - Fashion shop: the slogan, one card per word, made from scans of its own fabrics.
  - Wellness practice: the founder's promise, over a seedling that grows on every stressed word.
- **Watch out:** We never use the original songs. Generate or license the music, or use the client's voice. Cut any
  pun that needs explaining.

### typing-caret
*1 of 9 · diff 2-4 · hooks: text-headline, wait-for-it, bold-claim*

- **What it is:** Text typed with a caret, at about 6-8 characters per 0.5 s. As a signature it is a recurring anchor.
  One prompt bar returns three times, with a shorter input each time: a sentence, four words, then one word. Each
  send grows the bar into the next section, and finally the caret writes the name.
- **Why it holds:** Viewers read ahead and wait for the word to finish. The shrinking inputs speed the film up.
- **Examples:** Signature: onetake-launch. Also: tt-wonton-aep 18M, tt-oyehoye4k 13M, tt-settigation 1.2M (+5 more).
- **Build it here:**
  - Use HyperFrames sub-compositions with container morphs and registry typing.
  - Keep each section to 3-4 s, and the whole film to 18-22 s.
  - Difficulty 2-4.
- **Business uses:**
  - Agency: one brief bar opens onto three real projects.
  - Restaurant group: "table for two", "lunch" and "late" each open a real venue.
- **Watch out:** A prompt bar reads as an AI product. Use the client's real UI.

### big-number
*0 of 4 · diff 1-4 · hooks: number-ladder, wait-for-it*

- **What it is:** One huge number is the subject: timer digits filled with light, a count above each rung, or a date
  under a chart. It changes in steps, and the picture responds.
- **Why it holds:** A number reads faster than a sentence, and it asks the viewer to judge it.
- **Examples:** tt-bluxcamp 45M, tt-thebioswitch 5.6M, tt-foil-finance 1.5M, onetake-ebb.
- **Build it here:** Use tabular figures and masked fills inside the glyphs. Difficulty 1-2.
- **Business uses:**
  - Yoga studio: the class timer floods with light at zero.
  - Data SaaS: real tested row counts, each loading smoothly.
- **Watch out:** Every number needs a source and a date in PROJECT.md.

### word-stack
*0 of 5 · diff 2-4 · hooks: wait-for-it, familiar-ip*

- **What it is:** Words stacked one per line, with the last word often the largest, up to about 15% of frame height.
  Variants include an acronym stacked as chapter markers, and walls of one repeated word sliding in opposite
  directions.
- **Why it holds:** It fills a vertical frame and reads at a glance.
- **Examples:** tt-skalitude-show 24M, tt-jydnfilms 3.5M, tt-zresinn 1.8M, tt-chartosaur 1.7M, onetake-launch.
- **Build it here:** Set the type in HyperFrames. Use canvas when many rows move. Difficulty 2.
- **Business uses:**
  - Analytics SaaS: "three things your report is missing", as an acronym.
  - Coach: word walls of "stop waiting".
- **Watch out:** Give the stack a job, such as a chapter or a punchline.

### type-morph
*1 of 2 · diff 3 · hooks: wait-for-it, brand-name-drop, mid-action-start*

- **What it is:** Letters made from the brand's material, or turning into it. A reaction-diffusion field of stripes,
  each about 3% of frame width, is biased by text masks so the stripes trace the letters. Each word forms in about
  0.5 s, holds for up to 1 s, then melts back.
- **Why it holds:** The text has to form out of the texture, so the viewer waits for it.
- **Examples:** Signature: tt-skalitude-show 24M. Also: tt-kotsarevm 23M.
- **Build it here:**
  - Run Gray-Scott in canvas on a grid about 400 cells wide, with the text masks biasing the feed rate.
  - Bake it to frames.
  - Difficulty 3.
- **Business uses:**
  - Skincare brand: the name forms in a growing cell pattern.
  - Coffee roaster: the wordmark bursts into beans that fall into the bag.
- **Watch out:** Use one to three short words only.

### 3d-type
*1 of 3 · diff 2-3 · hooks: sound-hook, pattern-interrupt*

- **What it is:** Each word is a solid object. It is extruded to about 30-40% of its cap height, with bevels, chrome
  or gloss, and rim light. The camera flies past or around it with heavy blur, and each beat swaps the world behind
  it.
- **Why it holds:** A word that is an object stands out in a feed of flat captions.
- **Examples:** Signature: tt-platsae 6.6M. Also: tt-ripkuroi 5.6M, tt-t1zzy-1 3.0M.
- **Build it here:**
  - In canvas, draw each word 24-32 times along a projected depth vector, then the face.
  - Cut before the word turns more than about 35 degrees.
  - Difficulty 3.
- **Business uses:**
  - Nightclub: each act appears as a chrome word.
  - Streetwear brand: the real drop date, one word per beat.
- **Watch out:** Client relevance is low (2). No generic particles or glow.

### type-on-path
*1 of 2 · diff 3 · hooks: sound-hook, pattern-interrupt, familiar-ip*

- **What it is:** Words sit on rings, spirals and curves in 3D, along a forward camera path through a particle
  tunnel. Bold words are extruded.
- **Why it holds:** The flight never stops, and each word is a gate to fly through.
- **Examples:** Signature: tt-t1zzy-1 3.0M. Also: tt-krxsh3 2.2M.
- **Build it here:**
  - In canvas, draw seeded particles as streaks.
  - Place glyphs on a ring or helix, projected by depth.
  - Slow down on key words, and check legibility at 360 px.
  - Difficulty 3.
- **Business uses:**
  - Festival: act names on rings the camera passes through.
  - Streamer: a catchphrase on a spiral, flying into the logo.
- **Watch out:** Client relevance is low (2). Tint the tunnel in the brand colour.

## Graphics

### node-diagram
*1 of 3 · diff 2 · hooks: guess-challenge, beautiful-first-frame, bold-claim*

- **What it is:** A relationship drawn as plumbing. One source at the top feeds a trunk that splits into eight
  branches, leading to a 2 x 4 grid of receivers. For each option, the compatible branches fill in about 0.4 s and
  those receivers flip on a spring. Beats last about 3.6 s, and the count climbs to all eight.
- **Why it holds:** Viewers guess which receivers will open, and the full tree is the payoff.
- **Examples:** Signature: tt-greenscreencut 23M. Also: tt-ppt-hadi 6.9M, ig-divyansh-fx-attention 348K.
- **Build it here:**
  - Use HyperFrames SVG with stroke-dashoffset fills and a moving gradient head.
  - Draw each receiver in two illustrated states.
  - Difficulty 2.
- **Business uses:**
  - SaaS: each plan tier lights up the integrations it includes.
  - Insurance adviser: each policy fills the life events it covers.
  - Restaurant: each dish lights up the diets it suits.
- **Watch out:** The mapping must be the client's real data. Generic icons ruin it.

### chart-grow
*1 of 2 · diff 1-3 · hooks: text-headline, bold-claim, wait-for-it*

- **What it is:** A chart draws itself against a ticking date clock. One step line has a glowing tip, and a big date
  readout sits below. The y-axis rescales on each new high, so every step reads as a jump. The chart sits over the
  subject's photo, darkened to about 25%.
- **Why it holds:** Viewers wait for the next step, and for the end of the line.
- **Examples:** Signature: tt-foil-finance 1.5M. Also: onetake-one-dot.
- **Build it here:**
  - Use HyperFrames SVG from a data file, after checking the registry's chart blocks.
  - For long spans, run 4-6 years per second, with a tick on each step.
  - Difficulty 1.
- **Business uses:**
  - Estate agent: the median asking price, from land-registry data.
  - SaaS: integrations per release, from the changelog.
  - Accountant: tax deadline extensions, from the official record.
- **Watch out:** It only works if the fact is surprising and true. Cite the source.

### stick-figure
*2 of 2 · diff 2 · hooks: relatable-pov, bold-claim, series-hook*

- **What it is:** A minimal figure acts out each sentence on a fixed stage: one ground line, one figure and one prop
  per idea. Earlier props dim. Colour appears only once or twice, and always means something. A variant alternates
  illustration, figure and punchline cards, changing about every 1.35 s.
- **Why it holds:** The figure could be anyone, so viewers see themselves in it.
- **Examples:** Signature: tt-clearmindtalks 28M, tt-valor-humano3 8.1M.
- **Build it here:**
  - Draw stroked pictograms in canvas or SVG.
  - Build a 6-pose rig and a reusable prop kit, and let text cards carry a third of the beats.
  - Difficulty 2.
- **Business uses:**
  - Physio clinic: "The more you sit, the more it hurts to stand."
  - Finance coach: a figure on a hamster wheel of minimum payments.
  - Team SaaS: "Every useless meeting, explained".
- **Watch out:** The fixed stage and the colour rule are what keep it from looking cheap.

### split-screen
*1 of 4 · diff 3-4 · hooks: contrast-split, beautiful-first-frame*

- **What it is:** Two halves run on one timeline and differ in one condition. A brush draws the same circle on both
  halves. On the left, each notification lifts the brush and breaks the line; the right half finishes whole. Then the
  left half falls away.
- **Why it holds:** A shared clock makes the difference undeniable.
- **Examples:** Signature: onetake-unbroken. Also: tt-sushmitagabriel 12M, ig-viscous-realm 10M, tt-zackdfilms92
  4.5M.
- **Build it here:**
  - Use canvas: one path, with the interruptions speeding up and the shake on one half only.
  - On 9:16, split top and bottom.
  - Difficulty 3.
- **Business uses:**
  - Bookkeeper: one month drawn as a line, with one half stalling on missing receipts.
  - Physio clinic: the same walk, broken against smooth.
- **Watch out:** A left-right split is too narrow for 9:16.

### ui-card-stack
*1 of 7 · diff 2-3 · hooks: text-headline, bold-claim, direct-address*

- **What it is:** UI elements treated as physical cards. Code boxes lift 4-6 px as each digit lands, 0.35 s apart.
  Then they fan out (about -20 to +20 degrees), stack into a deck and morph into a status icon, all in one motion.
- **Why it holds:** Turning inputs into objects makes a dry UI feel tactile.
- **Examples:** Signature: tt-settigation 1.2M. Also: tt-peanar3d 6.0M, tt-bymike0404 4.9M, tt-maxmill-ae 2.5M (+3
  more).
- **Build it here:**
  - Use HyperFrames, built from the client's real UI tokens, with CSS 3D around one pivot.
  - Make the card 900 px wide on a 1080 frame.
  - Difficulty 2.
- **Business uses:**
  - Fintech: a typed code locks into the app's real security badge.
  - Checkout: a discount code flips into the order summary.
- **Watch out:** "Cards on a flat background" as the whole idea is banned.

### cursor-demo
*0 of 8 · diff 2-3 · hooks: wait-for-it, mid-action-start*

- **What it is:** A pointer is on screen whenever something responds. In builds, the cursor and selection handles
  stay visible, so the result reads as made, not revealed.
- **Why it holds:** The cursor stands in for the viewer's hand, and every change has a cause.
- **Examples:** tt-ppt-hadi 6.9M, tt-maxmill-ae 2.5M, tt-benfryc 2.1M, tt-settigation 1.2M (+4 more).
- **Build it here:** Use the HyperFrames registry cursors, or a spring-driven pointer in canvas. Difficulty 2.
- **Business uses:**
  - Booking app: tapping a real time slot opens the confirmation.
  - Spreadsheet SaaS: one click, and the sheet fills itself.
- **Watch out:** Use real UI only. A cursor that never clicks is filler.

### counter-ticker
*0 of 4 · diff 1-4 · hooks: number-ladder, contrast-split*

- **What it is:** A number counts while the picture changes: a date clock, a stepped readout, a countdown, or a tally
  of broken pieces.
- **Why it holds:** It shows progress and promises an end value.
- **Examples:** tt-2f2g-labs 10M, tt-foil-finance 1.5M, onetake-ebb, onetake-unbroken.
- **Build it here:** Use tabular figures, with a tick on each step placed from the event times. Difficulty 1.
- **Business uses:**
  - Meditation app: the session counts down and floods at zero.
  - Shoe shop: a cushioning readout climbs with each foot strike.
- **Watch out:** Never count to a made-up number.

### grid-mosaic
*0 of 5 · diff 2-5 · hooks: beautiful-first-frame, text-headline*

- **What it is:** Many small units in a grid that make one picture or system: a year of day squares (52 x 7), phones
  as pixels, or nine versions of one person.
- **Why it holds:** A grid reads as order, and one cell that changes is easy to spot.
- **Examples:** tt-zackdfilms92 4.5M, tt-nemu-etoile 3.0M, onetake-clearing, onetake-domino, onetake-ebb.
- **Build it here:** In canvas, draw only the visible cells and cache the settled ones. Difficulty 2-3.
- **Business uses:**
  - Clinic: a fully booked month with one open slot.
  - Estate agency: a grid of plots, then a dive into one listing.
- **Watch out:** With no single cell to follow, it is wallpaper.

## Simulation and material

### rigid-body-drop
*0 of 8 · diff 2-5 · hooks: wait-for-it, sound-hook, brand-name-drop*

- **What it is:** Hard objects fall, bounce once or twice, and settle with weight: ingredients raining down, a ball
  descending a wall of targets, or a crane load cracking the tarmac. The motion is closed-form arcs, not live
  simulation.
- **Why it holds:** Weight reads instantly, and landings are natural sound beats.
- **Examples:** ig-satisfy3dverse 109M, tt-2f2g-labs 10M, ig-viscous-realm 10M, tt-audiosorf 3.6M (+4 more).
- **Build it here:**
  - In canvas, use seeded closed-form arcs.
  - Each landing gets a hard stop, 2 frames of shake and some dust.
  - To land on the beat, solve backwards from the beat times.
  - Difficulty 2-3.
- **Business uses:**
  - Snack brand: the real ingredients from the label land one per beat.
  - Builders' merchant: the new price list lands in their own yard.
- **Watch out:** Without squash, shake and a contact shadow, it looks like clip art.

### softbody
*1 of 6 · diff 3-4 · hooks: impossible-object, wait-for-it*

- **What it is:** Objects under hard rules that behave like jelly. Falling-block pieces squash about 15%, wobble for
  1-2 s and tilt into gaps. The last piece is slightly too big, so it squeezes in over about 3 s, deforming its
  neighbours.
- **Why it holds:** Soft physics inside hard rules is satisfying and slightly wrong, and the last squeeze holds
  viewers.
- **Examples:** Signature: tt-zech3d 3.0M. Also: tt-why-cgi 98M, tt-marblemannequin 63M, tt-hati-hati-mas 63M (+2
  more).
- **Build it here:**
  - In canvas, build each piece as a ring of edge points on springs, with area pressure. Simulate it, then bake it.
  - Fake fur with seeded strokes.
  - Difficulty 3-4.
- **Business uses:**
  - Movers: boxes in the brand colours squeeze into the van: "it all fits".
  - Furniture store: cushions in the store's real fabrics fall into an alcove.
- **Watch out:** Real fur and softbody are 3D jobs, so commit to a stylised look.

### cutting-slicing
*2 of 2 · diff 3 · hooks: beautiful-first-frame, sound-hook, wait-for-it*

- **What it is:** A precise machine cuts soft material on an exact loop, in one locked high shot. In one example, a
  press shears foam at about 30 degrees and the slab breaks away (9 s cycle). In another, a wire carves two rings,
  then the floor slides them away (3.0 s cycle).
- **Why it holds:** A crisp machine against squashy material, timed to dry foley. The loop doubles watch time.
- **Examples:** Signature: tt-marblemannequin 63M, tt-travisragsdale 3.4M.
- **Build it here:**
  - Draw an isometric canvas scene.
  - Make the shear a spring-driven skew of 8 corners, and light the groove edges.
  - Carve the client's logo, vectorised, as the cutting path.
  - Difficulty 3.
- **Business uses:**
  - Agency: the client's logo carved into foam, as a looping reveal.
  - Bakery: laminated dough sheared into a croissant slab.
- **Watch out:** Without placed foley, it is half as good.

### beat-sync-hits
*2 of 4 · diff 1-4 · hooks: sound-hook, guess-challenge*

- **What it is:** Every impact is a note. In one example, a ball bounces down a wall of objects that light up as the
  notes play, and a follow-cam keeps it centred. In another, a ball bounces inside a ring that shrinks on every hit,
  so the hits speed up on their own.
- **Why it holds:** Ear and eye agree on every hit, and a mystery tune adds a guessing game.
- **Examples:** Signature: ig-satisfy3dverse 109M, tt-brainboxkey 3.5M. Also: tt-smart-doctor 61M, tt-platsae 6.6M.
- **Build it here:**
  - In canvas, solve backwards from the beat times: arc durations first, then target positions.
  - Export the hits as `window.EVENTS`.
  - Difficulty 1-4.
- **Business uses:**
  - Toy shop: each target is a real product that lights up on its beat.
  - Music school: a week-one scale, ending "Can you name it?"
- **Watch out:** It is only relevant when the targets are the client's products. The music must be licensed.

### inflate-deflate
*1 of 1 · diff 4 · hooks: text-headline, guess-challenge*

- **What it is:** A full-frame, glossy, inflated panel is sucked onto a hidden mould. A dimple appears at 1.0 s, then a
  ring wave at 1.5 s, then folds that track the outline. The shape snaps in at about 4 s, then relaxes for 5 s. The
  camera is locked, with light from the front and top.
- **Why it holds:** It is a guess-the-shape challenge, with time to read the answer.
- **Examples:** Signature: tt-studiotoericht 6.4M.
- **Build it here:**
  - Build a 2.5D height field in canvas: a pillow minus the logo's distance field, on a spring-eased progress.
  - Add fold noise, and shade each pixel.
  - Difficulty 4.
- **Business uses:**
  - Mattress brand: the surface sinks into its logo letter.
  - Wedding planner: satin forms the couple's initials.
- **Watch out:** It will not match a real cloth simulation, and it is slow to render.

### cloth-sim
*0 of 4 · diff 4 · hooks: number-ladder, text-headline, wait-for-it*

- **What it is:** Fabric drops, drapes, stretches or tears. In the bank it supports a ladder (finer folds on each
  rung) or a build (a caramel wave that is really a thick sheet).
- **Why it holds:** Folds forming are pleasing to watch, and rising detail rewards waiting.
- **Examples:** tt-bluxcamp 45M, tt-2f2g-labs 10M, ig-viscous-realm 10M, tt-studiotoericht 6.4M.
- **Build it here:**
  - Build Verlet cloth in canvas, bake it per frame, and shade each quad by its normal.
  - Grids from 16 to 128 points per side form a ladder.
  - Difficulty 3 stylised.
- **Business uses:**
  - Upholstery brand: its fabric drops at the thread counts it really sells.
  - Bakery: cream rolls over a sponge as a wave.
- **Watch out:** Photoreal draping is outside our stack.

### minecraft-voxel
*1 of 2 · diff 1-4 · hooks: series-hook, familiar-ip, mid-action-start*

- **What it is:** A topic explained as a blocky game world. Each role is a named character with one visual tag, and
  each rule is a game mechanic the audience already knows. Each phrase gets one cut and one caption word (about 70
  px). The last line names the real subject.
- **Why it holds:** Familiar rules make a hard topic easy, and the late reveal pays off.
- **Examples:** Signature: tt-explainedusing-minecraft 4.7M. Also: tt-expalinervideos 12M.
- **Build it here:**
  - Draw our own isometric world in canvas, with no game assets.
  - With about 45 shots in 70 s, reuse a small kit of sets.
  - Difficulty 3-4.
- **Business uses:**
  - Mortgage broker: "Interest rates, explained using a lemonade stand".
  - SaaS: per-seat pricing, explained with a pizza party.
- **Watch out:** No game IP and no look-alike characters.

## Character

### literal-metaphor
*2 of 4 · diff 2-4 · hooks: relatable-pov, bold-claim, beautiful-first-frame*

- **What it is:** A saying or a feeling made physical. "My arm is dead" becomes a stone arm that moves only when the
  other hand lifts it, then drops with weight, in an ordinary room on a locked camera. In a variant, each phrase gets
  one literal picture, and colour carries the argument: blue for calm, red for panic.
- **Why it holds:** Viewers recognise it from their own lives, and it reads with the sound off.
- **Examples:** Signature: tt-thequinettos 136M, tt-thebioswitch 5.6M. Also: tt-clearmindtalks 28M, tt-studiorat 18M.
- **Build it here:**
  - Live action: a practical prop limb on camera, or gen-video object replacement checked frame by frame.
  - Cartoon: CAB.
  - Picture per phrase: canvas line art, or gen-image.
  - Difficulty 3-4.
- **Business uses:**
  - Physio clinic: after a day at the desk, his neck is a stone column.
  - Gym: the day after leg day, her legs are concrete pillars.
  - Financial adviser: "Why do good earners still feel broke before payday?"
- **Watch out:** Make no performance claims for the product. Each picture must fit its phrase.

### character-host
*2 of 9 · diff 1-4 · hooks: direct-address, contrast-split, series-hook*

- **What it is:** One presenter stays fixed while the background changes. One form is a keyed host in the lower left,
  over a full-bleed image for each idea held for 3-7 s. The other is one host, in one place, acting out each idea with
  the same props throughout.
- **Why it holds:** A face builds trust and frees the background to move fast.
- **Examples:** Signature: tt-zackdfilms92 4.5M, tt-girlinbluestudios 1.7M. Also: tt-blick-thegobbler 140M,
  tt-explainedbyalistair 21M (+5 more).
- **Build it here:**
  - Film the founder, remove the background locally, and assemble in HyperFrames.
  - Drawn hosts use canvas or CAB.
  - Generated hosts struggle to stay consistent.
  - Difficulty 2 with footage, 4 generated.
- **Business uses:**
  - Branding agency: "If I rebranded a corner bakery".
  - Dental clinic: one host at one mirror acts out two myths, then the real cause.
- **Watch out:** Label generated concept images as concept work.

### reaction-shot
*2 of 12 · diff 1-5 · hooks: relatable-pov, wait-for-it, impossible-object*

- **What it is:** A face shows the feeling about something seen, or not yet seen. In the withheld form, a deadpan
  face stares at an off-screen "that" for 5 s, a passer-by reacts the same way, then a whip reveals it. In the
  picture-in-picture form, a real facecam reacts a beat after the screen.
- **Why it holds:** People watch faces, and a hidden cause keeps them waiting.
- **Examples:** Signature: tt-expalinervideos 12M, tt-joinpressbook 1.9M. Also: tt-thequinettos 136M, tt-letwins 133M,
  tt-cgsick 77M (+7 more).
- **Build it here:**
  - Use footage, recording the screen and the face together.
  - Animation cannot fake a genuine reaction.
  - Difficulty 1-2, but casting is the real work.
- **Business uses:**
  - SaaS: "My dad tries our invoicing app", with his facecam over the real screen.
  - Accountancy firm: a client's face at tax season, then a shoebox of receipts.
- **Watch out:** Scripted reactions look fake.

### pose-to-pose-comedy
*1 of 6 · diff 2-3 · hooks: text-headline, contrast-split, sound-hook*

- **What it is:** Held drawings swap on hard cuts, with no in-betweens. One line is said three ways, one pose each,
  while the caption retypes. The holds shrink from 2.5 s to 2.0 s to 1.5 s. The last pose mirrors the first, so the
  film loops.
- **Why it holds:** The joke is in the contrast, and each pose lands faster than the last.
- **Examples:** Signature: tt-oyehoye4k 13M. Also: tt-blick-thegobbler 140M, tt-thelovelyhorrorshow 50M,
  tt-pastel-shark 19M (+2 more).
- **Build it here:**
  - Draw three poses in canvas or SVG, with a typing effect.
  - Use an approved voice.
  - Write the three moods first.
  - Difficulty 2.
- **Business uses:**
  - Coffee shop: the cup mascot says "We're open" bright, half-asleep, then caffeinated.
  - Gym: "Leg day", said eager, dreading, then unable to stand.
- **Watch out:** It needs a mascot with a clear silhouette.

### thought-bubble
*1 of 1 · diff 3 · hooks: wait-for-it, relatable-pov · not in TAGS.md yet*

- **What it is:** In the first 2 s, the character's wish appears as a picture in a cloud bubble. The ending recreates
  that picture almost exactly, but somewhere unexpected. The middle is one decision, one action and one result, in
  shots of 1-2.5 s.
- **Why it holds:** The destination is known, so the fun is in the route.
- **Examples:** Signature: ig-tall8tiny 4.5M.
- **Build it here:**
  - Generate shot by shot in gen-video from one character sheet, or paint in CAB.
  - Pop the bubble on a canvas `spring()`.
  - Difficulty 3.
- **Business uses:**
  - Restaurant: a tired worker pictures the signature dish, books, and the last shot shows that dish at the table.
  - Cleaner: a parent pictures a spotless sofa, and the ending is exactly that.
- **Watch out:** The route must be the client's offer.

### creature-reveal
*2 of 6 · diff 1-5 · hooks: scale-shock, pattern-interrupt, impossible-object*

- **What it is:** Something ordinary or huge turns out to be alive. In one form, a giant figure on a black LED wall
  at night is lit only on the figure, so the wall vanishes, and it is filmed from inside the crowd. In the other, a
  street object with a face opens a jaw, unrolls a 3 m tongue and pops out bouncing eyes every 3-4 s.
- **Why it holds:** A face where none should be is hard to scroll past.
- **Examples:** Signature: tt-anyma 71M, tt-hati-hati-mas 63M. Also: tt-borisao-blois 156M, tt-lights-are-off 130M (+2
  more).
- **Build it here:**
  - LED: our content on black, played on the client's real screen and filmed by phones.
  - Street creature: a canvas verlet tongue over a locked plate.
  - Difficulty 3 for our part.
- **Business uses:**
  - Drinks brand: its vending machine spits out bouncing cans.
  - Event agency: the mascot on the festival's LED wall, filmed from the crowd.
- **Watch out:** The LED version needs a real big screen at night.

## Sound

### voiceover-explainer
*1 of 16 · diff 1-4 · hooks: text-headline, relatable-pov, direct-address*

- **What it is:** A calm narrator drives the film, and every clause gets its own shot, cut exactly on it. Nouns become
  props on a neutral void, actions become follow shots, and the captions are 1-3 bold words.
- **Why it holds:** Short clauses with new pictures leave no dead seconds. The voice serves viewers with sound on,
  and the captions serve those with it off.
- **Examples:** Signature: tt-thexoutliners 23M. Also: tt-babyinside7 62M, tt-clearmindtalks 28M,
  tt-explainedbyalistair 21M (+12 more).
- **Build it here:**
  - Ask first whether there is a voiceover. Use the client's voice or ElevenLabs, and transcribe for timings.
  - Use 14 shots at most, from 4-5 canvas sets.
  - Duck the music 10-20 dB.
  - Difficulty 3.
- **Business uses:**
  - Locksmith: a real local break-in, ending on "how did they get in?".
  - Accountant: the town's biggest public tax mistake.
- **Watch out:** Use real, sourced stories only.

### asmr-foley
*1 of 4 · diff 3-4 · hooks: beautiful-first-frame, wait-for-it*

- **What it is:** A care procedure told at macro scale, with a gloved hand always in frame. Each step uses one tool,
  makes one change to the material and has one sound, and ends only when the surface visibly improves. A second
  problem, visible from the start, is solved two thirds of the way in.
- **Why it holds:** Sound plus visible improvement every few seconds, with a payoff mid-film.
- **Examples:** Signature: tt-smile-bam 70M. Also: tt-marblemannequin 63M, tt-babyinside7 62M, tt-travisragsdale 3.4M.
- **Build it here:**
  - In canvas, paint before and after plates of one macro.
  - Reveal the after through masks that follow each tool's path.
  - Place the foley from the event times.
  - Difficulty 3.
- **Business uses:**
  - Dentist: a stained molar, scaled and polished.
  - Car detailer: a dirty alloy wheel, with a stone freed from the tread.
- **Watch out:** We cannot listen ourselves. Run `tools/audio_qa.py` and ask a human.

### silence-before-hit
*0 of 4 · diff 2-4 · hooks: text-headline, wait-for-it*

- **What it is:** A planned freeze or near-silence right before the biggest moment. It might be a 1 s hold before a
  whip, a calm hold before a burst of cuts, or black before the drop.
- **Why it holds:** The rest makes the hit land harder.
- **Examples:** tt-jydnfilms 3.5M, onetake-clearing, onetake-launch, onetake-motion-web.
- **Build it here:** Keep it truly frozen, since a slow push still counts as motion, and duck the music. Difficulty 1.
- **Business uses:**
  - Club night: black, then a white flash on the drop.
  - Clinic: the free slot lands, the frame freezes, then "Book it".
- **Watch out:** A hold much longer than a second loses people. Use it once per film.

### trending-audio
*0 of 14 · diff 1-4 · hooks: mid-action-start, sound-hook*

- **What it is:** The film rides a sound that is trending on the platform. Its punchline sets the cut, and its shape
  (setup, then drop) is the film's structure.
- **Why it holds:** Viewers know the sound and wait for its payoff.
- **Examples:** tt-uede-art 39M, tt-crannyjr-utd 24M, tt-allthebrickstogether 21M, tt-nicky-blender 20M (+10 more).
- **Build it here:** Never put trending audio in client files. The client posts with the platform's sound, or we
  rebuild the shape with licensed music. Difficulty 1.
- **Business uses:**
  - The "underestimated" format: a setup line, then a drop into the real work.
  - A reverse-play reveal.
- **Watch out:** Licensing is a risk, and trends go stale within weeks.

## FOOH and CGI

### giant-product
*3 of 3 · diff 3-4 · hooks: scale-shock, impossible-object, brand-name-drop*

- **What it is:** The client's real product at building size (10-15 m) in a real place, proving its own claim: soft
  enough to bounce on, or heavy enough to crack the tarmac. A bystander's phone films it, with people for scale. The
  logo sits on something in the world, such as a buoy, not in an overlay.
- **Why it holds:** The scale shocks from the first frame, and the product is both the joke and the proof.
- **Examples:** Signature: tt-why-cgi 98M, tt-kaybojesendk 3.1M, tt-bricodepot 1.7M.
- **Build it here:**
  - **Photoreal:** a client plate, then an approved gen-image still, then gen-video.
  - **Stylised:** a fake-3D box with the real cover on a canvas pendulum `spring()`. Land it with a hard stop, a
    shake, a crack decal and dust.
  - Hide the moment of contact inside motion.
  - Difficulty 3-4.
- **Business uses:**
  - Builders' merchant: the new price list lands in their own yard.
  - Shoe shop: a giant midsole becomes the town-square trampoline.
  - Bakery: a house-sized pastry sits in the town fountain.
- **Watch out:** Show the benefit, don't state it. Budget for retries, and mark it as CGI where rules require.

### fooh-composite
*2 of 8 · diff 3-4 · hooks: impossible-object, scale-shock*

- **What it is:** An impossible event composited into handheld phone footage of a real place. One way is absence
  first: a dashed outline marks where a landmark stood, the camera searches the sky for about 6 s, then finds it far
  away under helicopters. Another is a window frame, with known objects as small as 2-4% of the frame to show scale.
- **Why it holds:** It looks like something that really happened, filmed by someone like the viewer.
- **Examples:** Signature: tt-borisao-blois 156M, tt-cgsick 77M. Also: tt-thequinettos 136M, tt-why-cgi 98M,
  tt-arts-help 76M (+3 more).
- **Build it here:**
  - Use client footage plus gen-video.
  - Draw overlays in HyperFrames, such as a dashed outline built with stroke-dashoffset.
  - Hide seams inside a whip tilt, and keep objects far away.
  - Difficulty 4.
- **Business uses:**
  - Removals: the client's office is gone, then spotted under drones heading to the new address.
  - Developer: a dashed outline of the tower on the empty plot, then the tower arrives.
  - Boat tours: a huge shadow under the bay, then the boat heads out.
- **Watch out:** It is the highest-wow group (4.1 on average) and the most expensive. Keep it playful, never like
  real news.

## Talk
Added 28 Oct 2026 from 15 YouTube Shorts that sell services or ideas through talk. Proof is views over the channel's
median (latest 48 Shorts), shown as the multiple. None of these cards was watched: TranscriptAPI gave the words and
their timing, but frames could not be fetched, so the visual parts below are build suggestions, not measurements.

### roleplay-dialogue
*1 of 1 · diff 2 · hooks: bold-claim, direct-address*
- **What it is:** a rule said to camera in under 9 s, then the same person plays the seller in a mock call against a
  second voice that answers in short plain lines, and the scene runs to a real outcome (often a no).
- **Examples:** yt-thefutur-money-first 154K (15.8x).
- **Build it here:** a two-sided call transcript as kinetic type (current and previous line only), two voices
  (paid, with approval), or two cab characters, or the owner and a teammate on one camera.
- **Business uses:** coach (ask where the last three clients came from first), agency (ask the budget before you
  write anything), StraightScale (ask what they already tried).
- **Watch out:** 15+ turns get unreadable on a phone; cut to the turns that carry the lesson.

### step-plan
*2 of 4 · diff 1-2 · hooks: if-i-had-to, mid-action-start*
- **What it is:** "If I had to [goal] in [time], here's exactly what I'd do", then numbered steps, each shown on a
  real screen or object as it is said, ending on a comment keyword.
- **Examples:** Signature: yt-patrickdang-thirty-days 31K (17.7x), yt-noahkagan-millions-views 3.3M (5.1x). Also:
  yt-patrickdang-s-tier, yt-patrickdang-client-tom.
- **Build it here:** step chips stacking at the top, one real screen per step (never invented UI).
- **Business uses:** "If my referrals stopped tomorrow, here's what I'd do this month."

### prop-analogy
*1 of 2 · diff 2 · hooks: question, contrast-split*
- **What it is:** one everyday object handed to two people; one resells it, the other transforms it. The object stays,
  the choice changes.
- **Examples:** yt-alexberman-orange 567K (90x, the biggest breakout in the batch).
- **Build it here:** split screen, one drawn object, a three-shape morph on the transform side (`spring()`).
- **Business uses:** one referral: wait for the next, or turn its words into the next post.

### quadrant-matrix
*1 of 1 · diff 2 · hooks: bold-claim, contrast-split*
- **What it is:** two labels on a line, then "there's a second piece everybody misses" draws a second axis, making a
  2x2; a self-test places the viewer; the payoff points into one corner.
- **Examples:** yt-codie-oxygen-dessert 65K (3.5x).
- **Build it here:** axes draw on, labels drop, a gold marker walks to the winning corner.
- **Watch out:** the second axis is the re-hook at the midpoint; do not show the full grid up front.

### mentor-quote
*1 of 1 · diff 1 · hooks: bold-claim*
- **What it is:** a blunt claim, then a mentor's words quoted in full, then the exact line the speaker started saying
  to people because of it, then the principle. The weakness is said first and turned into the reason to choose.
- **Examples:** yt-leila-character 27K (11.7x).
- **Build it here:** owner on camera, or the quote as a handwritten note, the line typed as a message.

### rise-fall-turn
*2 of 3 · diff 1-2 · hooks: mid-action-start, bold-claim*
- **What it is:** start mid-story with an age or a result, two quick falls, then one repeatable behaviour (a
  question asked to the right people) that turns it, a short rise, a pointer to the long version.
- **Examples:** yt-noahkagan-tire-shop 8.4M (13.0x), yt-patrickdang-client-tom 5.8K (3.3x).
- **Build it here:** the owner tells it; faceless, a timeline line that dips on the falls, panels per beat.
- **Watch out:** real stories only, told by their owner; no invented results.

### street-interview
*1 of 2 · diff 2 · hooks: question, relatable-pov*
- **What it is:** one nosy money question asked to a stranger in frame 1, then the same three follow-ups (what
  exactly, how much, what advice).
- **Examples:** yt-noahkagan-first-class 2.0M (3.1x). The same channel's other Shorts in this format range from
  0.07x to 13x, so the format alone does not win.
- **Build it here:** footage with consent forms, or two drawn characters with speech bubbles.

### qa-cold-open
*2 of 4 · diff 1-2 · hooks: question*
- **What it is:** someone else asks the question (off camera or typed), the expert answers before 4 s. The count or
  the topic is in the question, so the viewer knows the length.
- **Examples:** yt-leila-trust 9.7K (4.2x), yt-thefutur-three-books 150K (15.4x).
- **Watch out:** the Hook Library says question hooks lose on Instagram (principle 4); these won on YouTube Shorts,
  where the asker is someone else. Test before relying on it.

## Combinations that work

Each row pairs one signature device with one supporting device and a hook, as the cards do. The support serves the
signature; it never competes with it.

| Signature + support | Hook | Film idea | From |
|---|---|---|---|
| `zoom-through-scale` + `whip-pan` | beautiful-first-frame | Clinic: a booked month, a dive to the one free slot, "Book it" lands, a whip back out to the logo. | onetake-clearing |
| `before-after` + `pull-back-reveal` | transformation-promise | Gardener: "3 weeks of work" over a bare yard; the garden builds from plan lines; the owner's clip shrinks onto the real lawn. | tt-vfxbyhassaan |
| `versus-compare` + `pose-to-pose-comedy` | contrast-split | Language school: cheek kisses, handshakes, then one of each collides; the end card offers the class. | tt-blick-thegobbler |
| `chain-reaction` + `top-down-plan` | wait-for-it | Bookkeeper: one receipt upload knocks through sorted, matched, filed; the pull-back shows the course is the mark. | onetake-knockon |
| `giant-product` + `pov-camera` | scale-shock | Running shoe shop: a giant midsole in the town square, filmed on a passer-by's phone as people bounce on it. | tt-why-cgi |
| `escalation-ladder` + `big-number` | number-ladder | Data SaaS: real tested file sizes, 1,000 to 1,000,000 rows, open smoothly; the last rung in a generic spreadsheet greys out. | tt-bluxcamp |
| `literal-metaphor` + `word-by-word` | question | Physio clinic: "Why does your back feel worse after a weekend of rest?" One literal picture per phrase, one word per beat. | tt-thebioswitch |
| `match-cut` + `cut-on-beat` | mid-action-start | Cafe: a hand with a TV remote zaps the table through the real menu, one item per beat, looping mid-cycle. | tt-hellobossfilms |
| `object-carries-camera` + `shape-wipe` | brand-name-drop | Bakery: the logo scooter rides order, bake, box, deliver; circle wipes open each stop; the ride folds back into the logo. | tt-madebyoddly |
| `screen-in-frame` + `morph` | price-or-value-question | SaaS founder: "Would you pay for this?", then the feature plays on the office monitor as one morphing button. | tt-maxmill-ae |
| `glitch-cut` + `silence-before-hit` | relatable-pov | Kitchen fitter: "My uncle said I just put up cupboards." A frozen beat on black, then finished kitchens on the drop. | tt-sabujak-io |
| `x-ray-cutaway` + `beat-sync-hits` | beautiful-first-frame | Dental clinic: a tooth turns glassy, the camera tips into it, the nerve pulses on a heartbeat, and it loops to the clean tooth. | tt-smart-doctor |

Before committing to a pairing, run `check` for the client. The signature must not match the signature of any of
their last 3 films, and the pair may share at most one device with their last film.
