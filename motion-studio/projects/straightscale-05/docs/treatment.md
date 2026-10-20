# Treatment: StraightScale · reel 05 "Three things, one system"

Written before the scene code; the beat sheet was re-timed after review round 1 (marked). v2 (after the independent
review of v1) changes the hook, the layout, the landing and the CTA: see section 6, which replaces section 5 for v2.

## 1. Reference measurements

### tt-rafaellfreitaas (refbank card, 1.2M plays, 8 s, logo-reveal)
Card numbers (colour-gated cut detection, re-measured): 0 cuts in 8 s (0.0 per 10 s), mean 8.0 s between big
changes, change-rhythm CV 0.0, quiet share 0.2 at 2 fps, hook change 0-2 s 0.024. The card explains why these read
"flat": the elements are tiny on a black frame, so frame difference never crosses the cut threshold. In the picture
the motion never stops for the first 5 s (a state change about every 0.5 s), then a 2 s hold on the lockup.
Palette #000000 / white dots / one brand colour (#38ea68). Type: only the brand's own wordmark, about one third of
frame width. Camera: none, flat 2D.

| Take (grammar) | Leave (content) |
|---|---|
| Start from primitive dots on a near-empty dark frame: the eye locks onto the few moving things | Pure black (ours is the brand charcoal #1F1F1F with static grain) |
| Spinner tension, then one merge into a single brand-colour ball with one glow pulse | Their green, their app icon, their wordmark |
| One soft-body move: squash on the merge, crouch, stretch along the velocity, fly out of frame, land back | The cartoon bounce sound design |
| The mark comes out of the ball (they carve it; we reveal the real file through a circle that grows from the ball) | Any redrawn or traced mark |
| The icon slides left and the wordmark is revealed letter by letter from behind it (a mask opening to the right) | The final 10% scale-down (our lockup lands at its final size on the slide spring) |
| Springs with overshoot at every step; a sting structure (tension, release, play, resolution) | Text-free film: we add a question and an end card because the owner wants a message that reads with sound off |
| End on a hold so the loop restarts from the empty frame | |

Our measured draft vs the card: see `docs/review_log.md` (pacing.py on draft 2 and v1).

## 2. Three concepts

| | A "Three things, one system" (chosen) | B "Three screens fold" | C "Three threads" |
|---|---|---|---|
| Idea | Three ivory dots labelled Posts / Replies / Follow-ups spin like a loading spinner while the question asks if the business still runs on three separate things; they merge into one crimson ball that hops out and lands as the real StraightScale mark; the wordmark writes itself; "One system. Built around your business." | Three phone-sized panels (posting, inbox, reminders) stacked like cards, each blinking for attention; they fold into one panel that becomes the mark | Three coloured threads tangle across the frame and are pulled through the S channel of the real mark, coming out as one straight line |
| Hook (0-2 s) | dots pop on three notes, labels word by word, the question from 0.78 s | three panels slam in with notification pings | a knot of threads tightening |
| Signature device | the three-dot morph into the real mark (merge, squash-stretch flight, circular mask reveal) | card fold (paper-like 3D) | thread pulled through the logo's channel |
| Style / engine | flat 2D, canvas engine, 60 fps with subframe blur | HyperFrames with 3D transforms | canvas engine, path physics |
| Risk | the ball must hand over to the real file without a visible swap | fake UI screens (house banned list) and a panel look close to film 03 | uses the S channel as a path, the device of film 02 (refbank check would fail) |

Recommendation: A. It is the batch brief's concept, it keeps every logo moment on the real file, the metaphor is
physically in the picture (three things literally become one), and the refbank check passes
(`check --category logo-reveal --devices morph,mask-reveal,word-by-word`: ok). B needs invented interface screens;
C repeats film 02's signature path device.

## 3. Art direction (chosen concept)
- Design read: a calm, premium sting. Almost nothing on screen, every move has weight, the payoff is the real mark.
  It should feel like a well-made product launch, not a cartoon.
- Palette by role: ground charcoal #1F1F1F (with static grain under 7/255 so the glow does not band); ivory #F8F6EF for
  the dots, labels, question and end lines; gold #DD9A10 only for "three", "Built around your business." and the
  rule under "one step a week."; crimson #B31217 for the ball (it warms from an ivory core in 0.16 s); the mark keeps
  its own red and gold. No gold text on ivory, no red text on charcoal.
- Type in motion: every word rises on its own spring (k 260, d 22) from 0.42 x its size below, staggered 0.09-0.14 s;
  labels pop from 16 px below; nothing fades in on its own. Exits are faster than entrances: the question lifts and
  parts around the ball in 0.2 s; the end card drops out in 0.38 s.
- Layout and focal points: one left text edge for the whole film (x 96 on 9:16, 92 on 4:5): the question top left,
  the spinner centred in the safe band (x 518) under it, the lockup's mark lands at the same left edge, the end lines
  under it. One focal point per moment: the dots, then the ball, then the mark, then the words.
- Signature device: the three-dot morph into the real mark, present from frame 1 to the lockup.
- Motion vocabulary: closed-form springs (lib/motion.js) everywhere; stepped spinner (120 degrees per beat, k 700,
  d 44), an accelerating spiral (angle grows with tau^3, radius shrinks with tau^2.3), merge pop (k 330, d 15),
  jelly wobble 6.2 Hz decaying at 5.2/s, crouch 0.25 s, ballistic flight 0.78 s with stretch along the velocity,
  landing as a damped impact (omega 36, zeta 0.5) with squash tied to the displacement, circular mask (k 150, d 24),
  FLIP slide of the mark (k 190, d 23), letter wipes every 52 ms. Transition rule: no cuts; one continuous object
  carries the film.
- Texture: flat vectors, one soft glow at the merge only, static grain over everything.
- Sound world: a quiet sampler bed (bowed vibraphone, cellos, strings) and effects that lead: three bell notes for
  the dots, soft wood ticks for the spinner, a rising air-and-cymbal swell into the merge, a resonant pop and a sub,
  a tuned low wobble that follows the squash, an upward whoosh, near-silence while the ball is off screen, a falling
  whoosh, the landing thud (gran cassa, sub, timpani A2), an airy bloom on the reveal, a glockenspiel glint on the
  gold square, a harp line under the letters, and the resolved D major add9 chord on the lockup. One shared room.
- Banned for this piece: a redrawn or recoloured mark, particle bursts, more than one glow, centred title cards,
  bouncy text, a sound for every letter, a shimmer-chord ending.

## 4. Script (on-screen only, no voice)
| # | On screen | Role |
|---|---|---|
| 1 | Still running / your business (v2: on frame 0) | question, block 1 |
| 2 | on *three* / separate things? (v2: in by 0.94 s) | question, block 2 |
| 3 | Posts · Replies · Follow-ups (labels under the dots; v2: after the question) | the three things |
| 4 | (the real StraightScale lockup) | answer |
| 5 | One system. | the idea |
| 6 | *Built around / your business.* | the promise, no claim |
| 7 | Follow for the build, / step by step. (v1: "one step a week.") | CTA (follow) |
Word count 21 on screen in 14.0 s (v1: 22 in 14.75 s). Alternative hook line (not used): "Three tools. Three logins. One you."

## 5. Beat sheet (seconds; 120 BPM grid, one beat 0.5 s; times exported from the page to `audio/events.json`)
| Time | Beat | On screen | Moving | Still | Link to next (what survives) | Audio |
|---|---|---|---|---|---|---|
| 0.00-0.34 | 1 hook | three ivory dots pop in a triangle | dots spring in with overshoot | charcoal | the dots | three vibraphone notes A4 E5 B5 + soft bubble pops |
| 0.30-2.10 | 2 labels + question | Posts / Replies / Follow-ups; the question word by word | labels rise, words rise | dots | dots and question | bowed bed A3 E4 B4 breathes in |
| 1.50-3.00 | 3 spinner | the triangle steps 120 degrees on every beat, labels ride along | 4 steps | the question | the dots | wood tick + one marimba note per step |
| 3.32-3.60 | 4 labels leave | labels drop out | labels | question, dots | dots | |
| 3.50-4.50 | 5 collapse | the dots spiral in, faster and closer | accelerating spin | question | the point where they meet | riser: air, rising tone, cymbal swell, string tremolo |
| 4.50-5.05 | 6 merge | one crimson ball with an ivory core and one glow pulse, jelly wobble | ball | question | the ball | pop + sub + glockenspiel E6 + pizz A1; tuned wobble |
| 5.05-5.30 | 7 crouch | the ball squashes down | squash | question | the ball | small air intake |
| 5.30-5.60 | 8 launch | the ball stretches and shoots up, the question parts around it and lifts away | ball, words | | the ball (leaves frame) | upward whoosh |
| 5.60-5.91 | 9 hang | empty frame | nothing | | the ball returns | near-silence (planned) |
| 5.91-6.17 | 10 fall + land | the ball drops in and lands with a squash | ball | | the ball | falling whoosh, landing thud, timpani A2 |
| 6.17-6.55 | 11 reveal | the real mark appears through a circle growing out of the ball; gold square last | circular mask | | the mark | airy bloom, glockenspiel glint, bed returns (A D E) |
| 6.55-7.00 | 12 rest | the mark alone | (spring settles) | mark | the mark | bed |
| 7.00-7.87 | 13 slide + wordmark | the mark slides left and shrinks into the lockup; letters revealed one by one from behind it | mark, letter wipes | | the lockup | soft slide air; harp D4 F#4 A4 D5 E5 |
| 7.87 | 14 lockup | the real StraightScale lockup | | lockup | lockup | resolved chord D major add9 (strings, harp roll, vibraphone, timpani D3) |
| 8.30-9.30 | 15 idea | "One system." / "Built around your business." | words rise | lockup | lockup | harp D3 |
| 9.70-10.52 | 16 CTA | "Follow for the build, / one step a week." | words rise | lockup, lines | the end card | wood click |
| 11.25-13.05 | 17 steps | a gold rule steps under "one step a week.", one word per beat; each word hops as the rule reaches it | rule, words | the rest of the card | end card | one harp note per step: A4 B4 D5 F#5 |
| 13.05-14.25 | 18 rest | full end card | nothing | everything | | the chord's tail |
| 14.25-14.75 | 19 exit / loop | everything drops out to the empty frame | text, lockup | | frame 0 (empty) | air sweep down, fade to digital silence |

Checks: beat lengths vary from 0.25 s to 2.0 s (CV 0.6, longest/shortest 8x) · a real rest after the payoff
(6.55-7.0) and at the end (13.05-14.25) · every transition names its survivor (the dots, the ball, the mark, the
lockup) · every reaction has a visible cause (the question parts where the ball passes; the mark appears out of the
ball; the letters come out from behind the sliding mark; the rule steps on the beat) · nothing new is static for
more than 4 s (longest frozen stretch in v1: see the review log) · the idea reads with the sound off (question,
picture of three becoming one, answer line, CTA).

## 6. v2 beat sheet (after the independent review of v1; replaces section 5)
What changed and why: the hook text must be on screen by 0.3 s (STANDARDS M5), all text must sit in the STANDARDS
section 6 zone (x 96 to 853, y 269 to 1248 on 9:16), the labels stacked into copies on every step, the end card sagged,
the mark was revealed high with the lower frame empty, and "one step a week" promised a weekly series that does not
exist yet. Times are exported from the page to `audio/events.json`; 120 BPM grid (one beat 0.5 s).

| Time | Beat | On screen | Moving | Still | Link to next (what survives) | Audio |
|---|---|---|---|---|---|---|
| 0.00 | 1 hook | "Still running / your business" already set (its words rose at the end of the previous loop) | first dot pops at 0.06 | the question | the question | bed enters mid-bow (A3 E4 B4) |
| 0.06-0.34 | 2 dots | three ivory dots pop in a triangle (y 980, frame centre) | dots spring in | question | the dots | three vibraphone notes A4 E5 B5 + soft pops |
| 0.48-0.94 | 3 question, block 2 | "on *three* / separate things?" word by word | words rise | block 1, dots | dots and question | bed, 3 dB over v1 |
| 0.90-1.28 | 4 labels | Posts / Replies / Follow-ups, each hanging under its own dot | labels pop | question, dots | the labelled dots | a soft harp note per label (A3 E4 B4) |
| 1.50-3.00 | 5 spinner | the triangle steps 120 degrees on every beat; labels turn with their dots and smear, never cross a dot | 4 steps | question | the dots | wood tick + marimba note per step |
| 3.40-3.70 | 6 labels leave | labels drop out | labels | question, dots | dots | |
| 3.50-4.50 | 7 collapse | the dots spiral in | accelerating spin | question | the point where they meet | riser |
| 4.50-5.05 | 8 merge | one crimson ball, ivory core, one glow pulse, wobble | ball | question | the ball | pop + sub + glockenspiel E6 + pizz A1; wobble |
| 5.05-5.30 | 9 crouch | the ball squashes on its floor | squash | question | the ball | air intake |
| 5.30-5.60 | 10 launch | the ball shoots up, the question parts around it | ball, words | | the ball (leaves frame) | upward whoosh |
| 5.60-5.84 | 11 hang | empty frame | nothing | | the ball returns | planned near-silence |
| 5.84-6.17 | 12 fall + land | the ball drops back onto the floor it left and squashes there (bottom stays on the floor) | ball | | the ball | falling whoosh, thud, timpani A2 |
| 6.17-6.55 | 13 reveal | the real mark appears through a circle growing out of the ball, near frame centre (y 980) | circular mask | | the mark | bloom, glint |
| 6.55-6.80 | 14 rest | the mark alone at centre | (settles) | mark | the mark | bed |
| 6.80-7.87 | 15 rise + slide + wordmark | the mark rises into the lockup row (y 515), then slides left and shrinks; letters revealed from behind it | mark, letter wipes | | the lockup | soft rise air, slide air, harp line |
| 7.87 | 16 lockup | the real StraightScale lockup | | lockup | lockup | D major add9 chord |
| 8.20-9.16 | 17 idea | "One system." / "Built around your business." | words rise | lockup | lockup | harp D3 |
| 9.30-10.00 | 18 CTA | "Follow for the build, / step by step." | words rise | lockup, lines | end card | wood click, vibraphone D5 |
| 10.65-11.95 | 19 steps | a gold rule steps under "step by step.", one word per beat; each word hops as the rule reaches it | rule, words | rest of the card | end card | harp A4 D5 F#5, airs |
| 11.95-13.45 | 20 rest | full end card | nothing | everything | | the chord's pad (held, not sagging) |
| 13.45-14.00 | 21 exit + loop | the end card lifts out; "Still running / your business" rises into place, and the last frame flows into frame 0 | end card out, question in | | frame 0 | air sweep down, fade to silence |

Self-check: hook text on screen at 0.00 s and the full question at 0.94 s; motion at 0.06 s; beat lengths 0.24 to
1.5 s plus the 1.5 s planned rest (CV about 0.6); a real rest after the payoff (6.55 to 6.80) and at the end (11.95 to
13.45); every transition names its survivor; every reaction has a visible cause (the question parts where the ball
passes; the ball lands on the floor it left; the mark comes out of the ball; the letters come out from behind the
mark); nothing important frozen for more than 4 s (pacing.py: longest quiet run 4.25 s, no frozen stretch); the idea
reads with the sound off. The CTA card runs 4.15 s (fully visible 3.52 s), longer than STANDARDS' 2.5 to 3 s end card
because the reading-time rule needs 3.43 s for its 29 characters; reading time wins.
