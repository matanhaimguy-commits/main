# Continuity-first product motion: lessons distilled from onetake

Source studied: **onetake** by feitangyuan (GitHub), commit 2f5fbd3, local clone at `references/onetake/`.
These notes restate its ideas as general craft knowledge, in our own words and organisation. Paths in
`backticks` are relative to `references/onetake/` so anyone can check the original reasoning.

---

## 0. What the project is, and why we may only learn from it

**What it is.** An agent skill for making short product films: 10 to 30 s promos and teasers, plus narrated
feature walkthroughs of up to roughly a minute. Its signature is a single unbroken take: kinetic typography and
the product's actual interface are the raw material, and each new moment is produced by something already on
screen. Technically it consists of:
- one HTML page per film, whose every visual value is computed from the timestamp alone;
- a catalogue of motion primitives with measured speed profiles (springs, arrivals, transitions, collisions,
  camera);
- a frame-by-frame renderer that simulates a film camera's shutter for genuine motion blur;
- a sound pipeline that mixes synthesis and recorded foley, timed from events the page reports;
- an automated acceptance test (the author calls it an oracle) built to reject slideshow-like cuts before a
  person reviews them.

Its real value is the paper trail. `SKILL.md` and each case README record which drafts were rejected and why, and
most of its rules trace back to one specific failed cut.

**License.** PolyForm Noncommercial 1.0.0. Our agency work is commercial, so:
- No running its scripts on client work, no copying or porting anything in `lib/`, `scripts/`, `templates/` or
  `gallery/`, and no reusing its prose in deliverables or prompts.
- Its films, palettes and bundled assets are not ours to ship. Some of the bundled typefaces (Inter, Geist,
  Fraunces, Instrument, Archivo) are independently open-licensed (OFL), so if we want them we fetch them from their
  own upstream projects.
- What we may take: concepts, thresholds and lessons from failures, re-implemented by us. Sections 3 and 4
  describe the measurement tools at the level of behaviour, enough to write them from scratch. As a test I wrote a
  small energy probe of my own (scratchpad only). On the repo's shipped films its stillness readings landed within
  0.01 of the figures the author published (table in §3.4).

---

## 1. Principles

Each principle below gives the failure that motivated it, what to do instead, and the numbers where the source
has them.

### P1. "Feels like a deck of slides" has two separate causes

Clients use one complaint for two unrelated defects. A cut has to avoid both.

*Defect A, a monotonous pulse.* The motion-web film was rejected twice on this ground:
- First attempt: nine page thumbnails, 0.74 s apiece, under a camera that never paused. Only 2 % of its frames
  were static.
- Second attempt: seven full-screen pages, 1.55 s each, all built the same way (cut, push in, caption). Each
  page moved, but the identical lengths and structure made the sequence read as a slide deck anyway.
- Accepted third attempt: durations ranging from 0.22 s up to 2.6 s (coefficient of variation 0.78), roughly a
  third to a half of all frames motionless, a calm hold immediately before a closing flurry of word hits. The
  energy over time finally had a contour.

*Defect B, substitution.* A later film, "Pocket Weather Club", had fixed its pacing and passed every pacing test,
yet its first version was turned down for the same reason. In code, each section was a separate scene and showing
one hid the others, so no object ever crossed from one section to the next. The approved third version made each
section emerge from the previous one: the mascot drops onto the headline, a card expands to become the page, a
circular stage widens out of the mascot, and the characters converge into a rotating badge. The author's carry
metric read 0.00, then 0.40, then 0.75 across the three versions. None of the pacing metrics told them apart.
(`references/rhythm.md`)

*Do this:* in the beat sheet, give every transition an explicit survivor: the object that persists across it,
and how it travels, grows or changes shape. A transition with no survivor is a slide flip, however good the pacing.

### P2. Pacing targets

- Make the longest beat at least four times the shortest (for instance quarter-second word hits beside
  2.5-second holds). Numerically: standard deviation over mean of beat durations ≥ 0.25.
- Leave about a quarter of all frames completely motionless, and include at least one unbroken calm stretch of a
  second or longer. The reference launch clip the author measured was motionless 34 % of the time and close to
  motionless 57 % of the time.
- A "rest" must be literally frozen. Even a gentle 1.00 → 1.05 push-in, or a floating camera, counts as motion.
  The clearing film's first render scored only 0.178 static because every pause contained a subtle push. Freezing
  those pauses raised it to 0.294.
- Place a long lull right before the climax. In the reference, almost four seconds of slow zoom precede the
  staccato words, and that contrast does the work.
- A flurry means three or more large frame changes inside 1.5 s, and the flurries should not arrive on a fixed
  interval. They are only mandatory when the reference or the concept calls for hits. A film about one shape
  transforming may legitimately have none.
- Vary how consecutive shots finish: spring away, blur away, hard cut. Never the same exit twice running.
- The reference had about seven hard cuts across 26 s. Editing every second is a different genre.

Reconciling with our house rule ("something new every 2 to 4 s"): a 1 to 3 s motionless hold is compatible. Our
rule forbids empty stretches. onetake's forbids perpetual motion. A single small change inside an otherwise frozen
frame satisfies both.

### P3. Pick the idea before writing beats

- Draft three pitches whose *core visual idea* differs. A pitch is one line describing the image, not the product.
  Three orderings of the same cards are one pitch, not three.
- Families of ideas that led to approved films:
  - a single shape mutating through every stage (one-dot: a point becomes a text cursor, a list, a progress ring,
    a graph, a bouncing ball, and finally the tittle on an "i");
  - one continuous push through nested scales (clearing: year → day → thirty-minute slot → back to the year);
  - a Rube Goldberg sequence where each event physically triggers the next (knockon);
  - two halves showing the same period with and without the product (unbroken);
  - a ground or material that floods and recedes to reveal each new scene (ebb);
  - one recurring interface element that spawns each section (onetake launch: one input bar typed three times);
  - a process that hides the message until the right moment (overlap: two misaligned print layers; a symbol
    emerges only when they align);
  - an image that resolves as more pieces join (domino: each phone acts as a single pixel).
- For every pitch, specify: the opening image, the survivor at each transition, what the idea forbids (cards?
  cuts?), and its visual treatment. Present all three and let the client choose.
- A template is not a pitch. One demo reused the house template's beat order. It scored a perfect 1.00 on carry,
  passed every check, and was still rejected as "too similar to the previous film, no creativity" (skill-demo
  versus motion-web). Execution quality cannot compensate for a recycled idea.
- Each project gets a new visual identity: palette, staging, camera language and transition style are decided
  per film. Tools and pipelines may be reused across films. Looks may not.

### P4. Operate the camera like a person

The one-dot film with a static camera drew the note that it lacked agile tracking shots. With a camera that
pursued each beat, the same film was approved, with the reviewer saying camera and physics needed no changes.

- **Base layer:** keyframes placing the frame wherever each beat needs it. **On top:** (a) a gentle handheld
  sway built from two sine waves of different frequency (a few pixels at 1x, scaled down with zoom), switched off
  during holds; (b) a brief decaying jolt whenever something lands (roughly 4 to 16 px, quick decay); (c) a faint,
  distant dot grid behind the scene, so panning over an empty background still registers as movement.
- **Tracking versus snapping.** To track, place the camera key roughly 0.1 s *ahead* of the subject on a sine
  ease-in-out. To snap, place the key at the destination *before* the subject arrives, on an exponential
  ease-in-out. When the camera trailed a fast glide, it lost the subject entirely: the first camera render of
  one-dot did this, and only the framing check noticed.
- **Interpolate zoom logarithmically**, never linearly.
- **Extreme zoom (past ~20x):** keyframe where an anchor point should appear *on screen* plus log zoom, then
  derive the world-space camera from those. At 300x a world-space keyframe that is one pixel off throws the
  subject a whole frame-width. Apply shake in screen space too, otherwise it disappears at depth.
- **When the subject changes mid-move** (text cursor → eyes → input box), the anchor must travel with it.
  Otherwise zoom lag frames the wrong area.
- **Large zoom jumps need slack at both ends.** A 1x → 44x push squeezed into 0.54 s was still at 9x when its
  hold started. Give the push more time and give the hold enough length to include a fully settled, frozen part.
- **List what must remain visible** (for example the subject between t0 and t1, the entire logo after t2) and
  verify it frame by frame.
- **Draw each nesting level at its own native size** under a combined transform, so type stays sharp at any
  magnification. Introduce a level's fine detail based on how large its parent currently appears on screen, and
  skip drawing anything outside the frame.
- **No jolts in narrated interface films.** At 30 fps with a half-frame exposure, shake turns every glyph into a
  double image.

### P5. Show what causes each reaction

- An interface that reacts with no visible trigger feels like a screensaver. Give every reaction a trigger the
  viewer can see: a pointer following one continuous path for the whole film, or the concept's protagonist (a
  bouncing ball, a dividing dot).
- Drive the pointer *and* all simulated responses from that single path, so cause and effect cannot drift apart.
- Make clicks tactile: the pointer briefly shrinks (to about 84 % for about 0.14 s), the control dips and
  vibrates, the state changes, and mouse-down and mouse-up arrive 60 to 75 ms apart.
- Landings compress in proportion to impact speed and then oscillate out. Letters close to an impact scatter
  according to their distance from it and snap back.
- In an overhead tabletop scene, elevation is conveyed by the **shadow**: further offset and softer edge with
  height, plus a slight size increase. Note that canvas shadow blur and offsets are not affected by transforms,
  so multiply them by pixel ratio × zoom yourself or they shrink as the camera retreats.
- The pointer is the least expensive way to bridge a transition: if it triggered the change, leave it visible
  through it.

### P6. Nesting as continuity

When every level physically contains the next (year → day → open slot → booked block), nothing ever gets swapped,
so a single dive is a single shot. Problems encountered and their fixes:
- **Wrong focal point at depth.** At 230x the target slot appeared smaller than an adjacent meeting title, so
  attention went to the neighbour. Fix: zoom further, slim the target, fade neighbouring text to 25 %.
- **Name not legible.** Yellow cells among cells of 34 to 64 % white lacked luminance contrast. Fix: as the
  ripple sweeps, darken every non-name cell by 60 %.
- **Detail outside frame at 300x**, since one page pixel became five screen pixels. Fix: anchor halfway between
  the two items that both had to stay visible.
- It also runs backwards: pith begins inside a single display pixel and retreats from 440x to about 0.5x, while
  the window's outline traces itself around content that was already present.

### P7. Put the message inside the image

- The first overlap cut got "gorgeous, but what does it mean?". Adding name tags to the pointers made it less
  clear. It worked only after the idea became a physical event in the picture: two dot layers that look like
  random noise until they align, at which moment an ampersand appears where both layers print.
- clearing writes its brand name with the calendar itself: the cells that stay free form the letters, and the
  slot the film rescued is part of one letter.
- pith proves "this agent is seven tools" by pulling the seven tool icons, visible since about second four, into
  a single row, not by writing the claim as a caption.
- knockon lays out its whole contraption along a hand-drawn return-key arrow. The final wide shot reveals that
  shape as the product's own symbol.
- Prefer the product's genuine behaviour as the transition. pith's only scene change is the app's real switch
  from dark to light theme. Decorative effects that the product does not actually do (confetti, sparkles, flying
  specks) look like stock templates; the client called them cheap.

### P8. When a hard cut is allowed

- Only two places tolerate an unbridged cut: **within a rapid run of staccato hits**, and **the cut to the closing
  card**. Every other transition is bridged, or written into the beat sheet as an intentional cut with its
  justification.
- A dissolve or slide between unrelated scenes does not count as a bridge.
- Build a bridge from **one object transforming** (a container reshaping into the next layout, one layer being
  pushed into). Two different objects cross-fading at the same size may fool a viewer, but an automated check will
  score it as a substitution.
- Successive screens shown one after another remain a slideshow even if each one is animated.
- **Previewing a result and then returning counts as two cuts.** To show what's coming, overlay a lens or inset
  window on the current shot rather than leaving it.
- **Shrunken full pages hide their motion.** A page animation does not survive at ~700 px width for 0.7 s. Either
  give the page the full frame (with the pointer) for a single calm hold, or show one isolated live component of
  it inside a small card.
- Text that merely fades in feels like presentation software. Text should arrive physically: a springy upward
  move with a small scale change, with opacity reaching full early so the arrival never looks like a dissolve.
- Deliberate freezes timed to music beats felt contrived (domino v5) and were dropped.

### P9. Easing, springs and velocity

- Characterise an easing with **t80**: the fraction of the move's duration that has passed when 80 % of the
  distance is done. Small values snap then settle (the launch-film feel). Around 0.7 is a symmetrical S-curve that
  reads like a website transition if used for travel. Values: linear 0.80, smoothstep 0.71, smootherstep 0.67,
  quad-out 0.55, cubic-out 0.42, quart-out 0.33, quint-out 0.28, expo-out 0.23.
- One easing for everything homogenises the film. A cut that used smootherstep everywhere made all motion feel
  identical. Exponential snaps and springs give landings their weight.
- Specify springs by damping ratio ζ and angular frequency ω, not duration. Starting points from the library:
  rising word ζ≈0.6, ω≈22, about 26 px of travel, scale 0.94→1; card arrival ζ≈0.62, ω≈18; logo letters ζ≈0.5,
  ω≈26, offset 0.055 s per letter, with impact compression; checkbox ζ≈0.5, ω≈28, popping from 0.8 scale. For an
  Apple-native feel, convert a SwiftUI spring with ζ = 1 − bounce and ω = 2π / duration (bounce 0 for smooth,
  0.15 for snappy, 0.3 for bouncy).
- Physics that depends on the past (soft bodies, ropes, magnetic attraction) gets pre-computed in a single pass
  (240 steps per second, deterministic seed) and sampled by timestamp afterwards. Never carry state between seeks.
- Typing speed around 28 to 38 characters per second, with a steady (non-blinking) cursor while typing. Checklist
  items about 0.24 s apart. Staccato words last 0.22 to 0.36 s each and are small, uppercase type.
- The share of travel on gentle curves did *not* predict approval (57 to 72 % for approved and rejected cuts
  alike). Treat it as a descriptor, not a score.

### P10. Blur from a simulated shutter, not from a filter

- A browser screenshot captures an instant, so rapid motion renders as a row of crisp duplicates (strobing). Past
  **80 px per frame** (measured on a 1920 px long edge, at the delivery frame rate) a film without shutter blur is a
  failure.
- The proper method: for each delivered frame, evaluate the scene at several moments spread over a
  **180-degree exposure** (half of one frame interval, centred on the frame's timestamp) and average them **in
  linear light** (decode sRGB to linear, average, re-encode).
- **Sample count adapts to speed.** Choose enough samples that adjacent copies of the fastest object are only a few
  pixels apart (they aimed for ~6 px, bounded between 4 and 48 samples). A constant 8 samples left visible stepping
  on the quickest moves; one-dot's 633 px/frame opening broke into bands. The page should therefore report the
  maximum on-screen travel between any two times, camera movement and scrolling duplicates included. When it
  under-reported, fast tiles stepped.
- **Static frames cost almost nothing.** Render the first and last instant of the exposure; if they match, nothing
  moved, so output that frame directly. This requires settled frames to be bit-identical, so round settled camera
  values and wait for springs to finish ringing.
- **Do not blur through an edit.** If one gap between consecutive samples contains most of the change (about three
  times larger than any other gap), it's a cut, a word popping in, a keystroke, or a footage frame change. Average
  only the samples on the same side as the frame time, or the cut becomes a single-frame dissolve.
- CSS blur filters smear in every direction, not just along the motion. Use them for depth of field only.
- Peak speeds measured at 60 fps (double them for 30 fps): whip pan 540, circular reveal 206, tilted fly-in 189,
  container reshape 156, elastic switcher 118, camera jolt 115, push-into-card 72, simple entrances below 50. At
  30 fps most transitions exceed 80, which is why the shutter is not optional.
- Dark gradients band once encoded to 8-bit 4:2:0. Overlay a *static* noise layer at very low opacity (≤ 7/255) in
  device pixels. Because it never changes, frozen frames remain frozen.
- Our `render.mjs` already merges subframes (`--sub`). Worth adding (our own implementation): averaging in linear
  light, speed-driven sample counts from a page-reported travel function, skipping static frames, and
  cut-awareness.

### P11. Audio as one acoustic space

The original sound pass assigned a separate synthetic beep to each visual event (sine blips for words, clicks for
letters, a cartoon boing for the jelly). The client dismissed it as cheap within a minute. Diagnosis:
- pure sine tones sound like a video game; physical objects produce overtones and a burst of noise at onset;
- with no common acoustic, the effects floated above the picture rather than belonging to it;
- a sound for every event (dozens of keystrokes, letter clicks, confetti pops) turns into a slot machine;
- uniform levels with no quiet moments.

What replaced it:
- **A short list of sonic materials:** *air* (filtered noise whose centre frequency sweeps, used for whooshes and
  panned with the motion); *glass* (a struck tone with non-harmonic overtones and a brief noise onset); *wood*
  (a dull knock with a bright click on top, for keys and mouse buttons); *sub* (a low sine that drops in pitch,
  driven into saturation, for impacts); *bubble* (a resonant pop for cards settling). Combine recorded foley (CC0
  libraries) with synthesis: recordings supply texture, synthesis follows the picture precisely.
- **A single shared reverb.** Theirs: about 1.1 s decay, 12 ms pre-delay, a few early reflections. Near sounds get
  little reverb send (~15 %), distant ones a lot (60 to 70 %). Sharing one space is what glues mismatched sources
  into one soundtrack.
- **Sparser than the picture.** Sound perhaps one keystroke in three, with velocity variation. When two sounds
  would fall within 40 ms of each other, drop one. Press and release are separate hits about 60 ms apart.
- **Derive timing from the page itself.** The page exports a list of events (time, type, horizontal screen position
  for panning, intensity) plus continuous signals (a ball's speed, the rate of change of log zoom, brush pressure).
  The mix is generated from those exports, so moving a beat moves its audio automatically.
- **Signals can play instruments.** A zoom whoosh was three noise bands blended by zoom depth (deeper = brighter),
  with loudness following |d log zoom / dt|^1.3. A rolling ball was filtered noise scaled by its speed.
- **Loudness tracks visual energy.** After one breath, a hold goes silent. The impacts are the loudest moments.
  Plan silence deliberately: a muted hang time, no pad under a close-up pause.
- **Check the dynamic arc with K-weighted short-term loudness (~400 ms windows) at each beat**, not RMS. Every
  landing must measure louder than its approach. In clearing, the second dive measured as loud as its landing until
  the dive was lowered by 4 dB.
- **Locate muddiness by time window.** knockon's mix put 42 % of its energy between 100 and 300 Hz. Splitting the
  energy by band per half-second window revealed the culprit, a low marimba line with long overlapping decays.
  Raising it an octave and shortening the notes solved it. Rule of thumb: keep melodic runs at F4 or higher and trim
  their decays.
- **Phone speakers** cannot reproduce pure sub-bass, so give low hits some upper harmonics.
- **Delivered levels:** −16 LUFS integrated, true-peak −3.5 to −4 dBTP, lowered further whenever the AAC encode
  came out hotter. Effects-only drafts peaked near −8 dBFS to leave room for music. Music dipped ~5 dB under
  effects, or ~11 dB under narration (quick attack, release around 350 ms). Our house loudness stays at −14 LUFS,
  but keep the same true-peak margin after AAC.
- **For an Apple-like product feel:** lay down the action sounds first (tactile contacts, camera whooshes,
  intentional silences), then add understated music that does not cover them. One rejected mix had its effects 27 to
  35 dB under the music within their own event windows, and normalising the overall mix did not help. Compare music
  against effects inside each event window and in the shared 0.8 to 4.5 kHz range.
- **Avoid clichéd closers.** A vibraphone chord with a crotale shimmer had closed three films and was heard as
  generic. Close on the music's natural cadence or on an impact unique to the film.
- Music is royalty-free by default, with its license stored alongside the project. A commercial track only when the
  client provides it. Verify each recorded source's license before delivery, since some free libraries forbid
  redistribution of the files.
- Editing to a song: splice on bar boundaries so the drop meets the film's peak and a silent beat meets the freeze.
  Music notes from clients usually concern *how energy evolves* ("the middle drags", "the pulse vanishes after 10
  s") rather than genre.

### P12. Frame, type and hygiene

- **Generous empty space.** Around 70 % of the frame is background, and cards occupy about a quarter of the width.
  Full-frame footage appears once at most, as the calm hold.
- Text is small and medium weight, with one accent colour and a distinctive face for the name. Heavy capitals are
  reserved for the staccato beat.
- No particle systems or confetti. If a beat needs flair, animate the letters themselves (squash, wobble).
- **Deterministic rendering.** The same timestamp always yields the same frame: seeded randomness, precomputed
  simulations. Our render contract already requires this.
- Measure text only after fonts have loaded, and embed subsetted fonts so a `file://` render never substitutes a
  system face. A late-loading font invalidates every measured position.
- Hide (`display:none`) any element that has moved off screen. A blur filter on an element shifted far off-canvas
  once rendered the entire frame black.
- **Review drafts at 1080p30; render 4K60 only once the cut is approved.** Give the client a time estimate before
  any long render.

---

## 2. Translating to 9:16 reels (our own inference; the repo only shows 16:9)

- Express speeds and distances against the **long edge (1920 px)**. Then the 80 px/frame limit and the
  2-percent-of-diagonal bridge test carry over unchanged, since the diagonal is still 2203 px.
- Readability: the source's minimum is 26 px for narrated labels on a 1920-wide frame. A 1080-wide vertical frame
  is displayed smaller on a phone, so require **roughly 36 to 40 px** on a 1080-wide canvas for anything meant to be
  read, and scale a UI replica to about 85 to 90 % of the frame width when it must be read.
- Keep key subjects, text and logos out of the platform overlay zones (about the top 12 %, the bottom 20 %, and the
  icon column at the right). Our framing check should treat those bands as out of frame for readable elements.
- Hook versus stillness: paid social needs a hook within 2 s (house rule), so schedule the first frozen hold
  *after* the hook. onetake's sparse openings work only because motion arrives within half a second.
- Muted autoplay is common, so bridges and meaning must work without audio. That makes P7 more important for
  reels than for the source's films.

---

## 3. Measuring a reference clip

The point is to quantify the reference's *pacing* so ours is not flat, not to replicate its shots. The facts that
decided motion-web (34 % static frames, seven cuts in two clusters, small elements in a lot of empty space) were not
apparent from one viewing. Built from impressions, the film ended up evenly paced on two attempts.
(`references/reference-deconstruction.md`)

### 3.1 Metrics

| Metric | How to compute | Why |
|---|---|---|
| Frame energy | average absolute grey-level change between successive frames (0 to 255), at 12 fps on 320-px-wide greyscale | where motion happens |
| Energy strip | one character per 1/12 s in rows of 4 s, character index = energy ÷ 3 (clamped 0 to 9) over a ten-step ramp from blank to dense | the pacing contour at a glance |
| Static share | fraction of frames with energy < 0.5 | rests; approved 15 s films sit near 0.3 |
| Near-static share | fraction with energy < 2 | the reference was 0.57 |
| Longest calm | longest run of frames under 2, in seconds | the lull before the climax |
| Cuts | frames with energy > 18 | how many, and where they cluster |
| Flurries | any 1.5 s window with ≥ 3 frames above 8 | where the hits land |
| Row variation | std ÷ mean of the per-row (4 s) averages | coarse contour (advisory only) |
| Dominant speed | per frame, median optical-flow magnitude over moving edge pixels, in px per 1/30 s scaled to 1920 px | the character of the motion |
| Moves and t80 | spans where speed ≥ 2 for ≥ 3 frames covering ≥ 40 px; t80 per span; travel-weighted median; share of travel with t80 ≥ 0.55 | snaps versus S-curves |
| Smear ratio | on fast frames (speed ≥ 24), gradient energy parallel to the motion over gradient energy perpendicular to it, on pixels that changed | below 0.78 indicates shutter blur; crisp renders score ~0.9 or higher |

Pitfalls:
- A 24 fps source must be sampled at 24 and its speeds rescaled. Upsampling to 30 inserts duplicate frames that
  read as zero motion and fragment every move.
- Optical-flow speed describes the main motion, not individual objects, and can under-read small fast objects by up
  to ~30 %.
- Large pixel changes also come from whip pans and dives. In clearing and domino most detected "cuts" are camera
  moves. Confirm against the contact sheet.
- At 320 px the energy is inflated by fine detail on dark backgrounds (a lone dot on black, pale brush marks) and by
  any slow push-in.

### 3.2 Visual inspection (contact sheets at 4 fps, ~24 frames per sheet, plus nine evenly spaced full frames)

Record:
- the largest element's share of the frame, and whether anything ever fills it;
- what moves *within* a beat (keystrokes, checkmarks, switches, a click) versus camera moves over static images;
- the one storyline (for the measured reference: problem statement, logo, prompt being typed, task list completing,
  generated site arriving, feature cards with a click each, product shown on a display, tagline, logo);
- how things enter and exit (spring pops that overshoot, tilted blurred fly-ins, hard cuts reserved for words, no
  dissolves);
- typographic choices (size, weight, number of accents, logo face, where capitals appear).

Then draft the beat sheet before touching the composition, with columns: `time | beat | moving | static | link to
next | audio`.

### 3.3 Borrowing a style without borrowing the film

An early study that retold a new subject over a reference's beat order was halted at the first draft as pointless
imitation. What may transfer:
1. **The governing rule all objects follow.** (In their study, every word was mounted on a machine part, with
   rivets, bolts, nuts and brackets.) Reproducing the parts without the rule looks like clip art; applying the rule
   to our own subject looks like the style.
2. **The software behind it.** Recognise which effects were simply cheap in the reference's tool (echo
   duplicators, offset paths), so you can separate signature from convenience.
3. **Measurements over impressions:** exact palette hex values, the grid's spacing read off one row of pixels,
   type size derived from capital height at 1080p, proportions of recurring parts.
4. **Their vocabulary, our bridges.** The reference's hard cuts belong to its edit, not to its style. Bridge our
   transitions with the style's own components.
5. **Their grammar, our message.** Generate the beats from our own concept round, never from the reference's
   scene order.

### 3.4 Building it with ffmpeg and Python

1. Decode with `ffmpeg -i ref.mp4 -vf fps=12,scale=320:-2 -f rawvideo -pix_fmt gray -`, load into numpy, reshape to
   frames, and take the per-frame mean absolute difference. All the pacing metrics derive from this array.
2. Sheets: `ffmpeg -i ref.mp4 -vf "fps=4,scale=426:-1,tile=6x4" sheet_%02d.png`, plus nine full-resolution frames.
   (Our `review.sh` already produces a 2 fps version.)
3. Optional motion fingerprint (requires OpenCV): dense optical flow (DIS or Farneback) on 320-px greyscale, plus
   Sobel gradients for the edge mask and the smear ratio.
4. Print reference and film metrics next to each other.

Readings from my own probe on the films shipped in the repo (12 fps, 320 px):

| film | static | near-static | longest calm | pixel "cuts" | comment |
|---|---|---|---|---|---|
| motion-web | 0.53 | 0.83 | 3.1 s | 2 | one flurry around 8 to 9 s |
| one-dot | 0.38 | 0.72 | 2.8 s | 6 | dark background, moving camera |
| knockon | 0.27 | 0.61 | 3.4 s | 0 | single continuous scene |
| clearing | 0.29 | 0.50 | 4.1 s | 17 | detections are dives and the whip |
| pith | 0.30 | 0.43 | 3.3 s | 11 | |
| ebb | 0.29 | 0.42 | 3.3 s | 28 | flood and whip trigger detections |
| overlap | 0.27 | 0.37 | 1.0 s | 19 | paper slams, print run |
| unbroken | 0.63 | 0.86 | 6.6 s | 2 | sparse brush film |
| skill-demo | 0.55 | 0.86 | 2.6 s | 3 | word hits at 12 to 13 s |
| onetake launch (30 s) | 0.09 | 0.31 | 1.9 s | 70 | dense showcase; would fail a fixed 25 % rule |
| domino (25 s) | 0.02 | 0.08 | 0.5 s | 169 | 3D chain; its own reference was 0.004 static |

Conclusion: approved 15-second pieces range from **0.27 to 0.55 static** with a **2.5 to 4 s** longest calm.
Dense showcases and 3D chain reactions are valid exceptions, so when a reference exists, the stillness target
should be derived from it.

---

## 4. Specification for our own acceptance checker

onetake's acceptance test is a battery of independent checks, each reporting a value and a status (pass, warning,
fail). Only failures block the cut. The key design point is that the pacing checks are blind to substitution, so a
separate check inspects the composition directly. (Behaviour drawn from `scripts/verify_promo.py` and
`scripts/probe.py`. The following is a spec for us, not a port.)

### 4.1 Pacing checks on the rendered file

| check | criterion | comment |
|---|---|---|
| durations | std/mean of beat lengths ≥ 0.25, beat starts taken from the beat sheet | equal beats read as slides |
| stillness | ≥ 25 % of frames below energy 0.5 **and** at least 1.0 s continuously below 2 | holds must be truly frozen; with a reference, compare to it |
| flurry | some 1.5 s window holding ≥ 3 frames above energy 8 | fail only when the reference has one and we don't; else warn |
| contour | std/mean of 4 s row averages ≥ 0.35 | advisory: it passed a rejected cut (0.54) and failed an approved one (0.33) |
| audio | after encoding, peak ≤ −3 dBFS, no clipped samples, ≥ 15 % of ~83 ms windows below −40 dBFS RMS | narrated pieces always fail the quiet clause; accept that rather than tuning for it |

### 4.2 Bridge (continuity) check on the composition

Step through the composition at the delivery frame rate. At every step, collect each visible element's **persistent
id**, screen-space rectangle, effective opacity and a content key (its text, or its image source with frame
numbers stripped so a footage clip stays one element). In our pipeline the cleanest route is for each composition
to export `track(t) → {id: {x, y, w, h, opacity, key}}` in post-camera coordinates, rather than hooking every DOM
and canvas call.

1. **Weight:** visible area × opacity ÷ frame area.
2. **Overlap score between two steps:** a weighted Jaccard index. An element contributes to the intersection (with
   the smaller of its two weights) only if it exists in both steps with an identical content key; otherwise it adds
   only to the union.
3. **Cut between neighbouring steps:** overlap below 0.3, both frames non-empty. **Flurry:** three or more cuts each
   no more than 0.6 s from the previous (so they span roughly 1.5 s), with the window padded by 0.25 s on each side.
4. **Transition:** compare each step to the step 0.4 s later. Overlap below 0.2 marks a substitution window. If the
   later frame is near-empty (a fade through background), keep looking ahead up to 1.5 s. Merge windows that overlap
   into a single transition and keep its lowest-overlap pair.
5. **Classify** using elements visible on both sides with opacity ≥ 0.15:
   - **bridged:** at least one moved by ≥ 2 % of the frame diagonal **or** scaled by ≥ 10 %, measured as
     |ln(√area_after / √area_before)| ≥ 0.1;
   - **pinned:** none moved, but one is big (≥ 3 % of the frame) and unchanged with the same content key (a frame
     whose contents are swapped);
   - **unbridged:** otherwise.
6. **Excluded:** transitions inside a flurry, within the final 1.2 s (end card), or within 0.25 s of a cut the
   beat sheet marks as intended.
7. **Score** = (bridged + ½ × pinned) ÷ transitions considered (1.0 if there are none). **Fail below 0.5, warn
   below 0.7.** Reference points: rejected cuts scored 0.00 and 0.40; approved ones scored 0.56 (with a warning),
   0.75, 0.83 and 1.00.
8. Report each transition with time, dominant elements before and after, and its bridge (or "unbridged"). The
   unbridged lines are precisely the moments viewers will read as slide changes. Run this check on the first rough
   version that plays end to end: fixing an unbridged moment is an edit to the page, which costs far less than a
   new render.

Limits to cover by eye:
- A transition built from two elements (a new image fading up at a card's size while the card fades out) gets
  counted as a substitution. Either build bridges from one transforming element, or declare the cut.
- **A single continuous world produces almost no transitions.** knockon scored a perfect 1.00 from zero
  transitions. A pass computed over fewer transitions than the beat sheet contains proves nothing; inspect visually.

### 4.3 Speed check

Split every element's track into moves. A per-frame step = centre displacement + ½ × change of √area, scaled to a
1920-px edge. Moves are runs where steps ≥ 0.8 px/frame (tolerating gaps of up to 2 frames), at least 4 steps long
and 30 px of total path. A solitary jump above 60 px flanked by near-zero steps is a teleport, so zero it. Record
per move the path length, t80, peak step, and overshoot (how far it went beyond its endpoint along the net
direction); for the film, the peak and the travel-weighted median t80.
**Fail when the peak exceeds 80 px/frame in a render without shutter blur.** Blur status comes from the render log,
or from a smear ratio < 0.78. Curve statistics are informational only.

### 4.4 Visibility check

The composition lists ids that must stay visible during given time windows, optionally requiring the whole box. Fail
any sampled frame where such an element is completely outside the frame, or partly outside if the whole box is
required. Boxes must be in screen space when there is a camera. In onetake, this was the only check that caught a
camera losing its subject. For reels, count the platform overlay bands as outside the frame.

### 4.5 Two further guards

- **Seek errors:** list every timestamp where the page's seek function throws. One film failed silently from 12.8 s
  onward.
- **Variant identity:** when adding a language or refactoring, render the frozen approved version and the new one at
  sample times, and require zero differing pixels for the original variant.

---

## 5. Feature demos without screen capture

(`references/product-demo.md`)

### 5.1 Why rebuild the interface

- Text lives in data, so adding a market means filling a strings table, not reshooting.
- Vector and DOM stay crisp at 2.5x or even 44x camera magnification.
- No personal accounts, credentials or loading spinners slip into frame, and nothing moves unless we animated it.
- The effort is modest: a few hundred lines of absolutely positioned markup per screen, limited to the
  states the film actually shows.
- The price: a side-by-side comparison with the real product, and real data (5.3).

### 5.2 Collecting reference material

Non-technical clients do not cope with a shot list. Instead request a single concrete action ("open the app, choose
this option, type a slash, take a screenshot after each step"). Grab frames from what they send and inventory every
state: default, dropdown expanded, menu, selected chip, send button active.

### 5.3 Real data only

Every value, filename and chart figure on screen is read by script from output the product genuinely produced.
Attractive invented numbers are claims the product never made, and for advertising they are a compliance risk.

### 5.4 Constructing the replica

- Use the screenshot's own pixel coordinates (a Retina capture divided by two) and position each element exactly
  where it was measured. Display the replica scaled inside a window placed on the camera's plane.
- Put every string in a per-language table from the start. Build the DOM once; then a pure state function
  updates it each frame (mode, open menu, highlighted row, visible chip, active send button).
- Prefix all replica styles with one root class. In one project an unscoped, common class name clashed with the
  film's own stylesheet and drew dashed yellow outlines.
- Measure elements while they are visible and after fonts load, since hidden containers measure as zero.
- Use the measured fixed positions for the original language and width-based flow layout for other languages.
- Leave out anything the client wants hidden (user names, workspace names, download controls).
- Check the replica against each reference state at 1:1 until every remaining difference is intentional.

### 5.5 Making it readable

- Screen text size = font size × replica scale × camera zoom. Text the voice-over mentions must reach the
  legibility floor (26 px on a 1920-wide frame; see §2 for vertical). A window meant to be read should span about 70
  to 80 % of the frame's width. A wide shot that tried to fit cards, window and result at once was illegible and was
  rejected.
- Frame each operation (choose mode, select, upload, send) in its own close-up, with the camera following the
  pointer between them. Keep the wide shot for moments where the spatial relationship is the message.
- Compute highlight rectangles from the replica's own layout (summing offsets inside the replica, not using the
  camera-transformed bounding box) and paint them on the canvas. Cache the last known rectangle so a highlight can
  finish fading after its element disappears.
- Preferred highlight: a rounded rectangle wrapped tightly around the content, stroked on with an exponential
  ease-out over ~0.45 s and faded over ~0.3 s, line width corrected for zoom. Avoid hairline boxes and circles. On
  a menu entry, wrap the icon and label only. The client also liked a glow, but our house rules ban glow on UI, so
  we keep the shape and timing and drop the glow unless a client explicitly asks for it.
- The pointer targets actual element centres and each click has mouse-down and mouse-up about 75 ms apart.

### 5.6 Voice-over

- Have the client choose between 5 and 8 voices reading the same two lines. They may switch voices later, so the
  timeline must tolerate a replacement.
- Narrate continuously with pauses around 0.45 s. Use longer gaps only where the visuals continue on their own.
  Don't stretch spacing to hit a target length; the narration determines the runtime.
- **Anchor every beat to the specific word it coincides with** (for example a beat tied to the word "select"). A
  new voice then only requires new word timings, not a new edit. Take timings from alignment or speech
  recognition, but take spellings from the script, because recognisers garble brand names.
- Verify durations before committing to a length. TTS pauses at punctuation stay the same at higher speeds.
- Music beneath narration: dip it ~11 dB below the voice's RMS envelope (quick attack, ~350 ms release), and edit
  it on bar lines so its peak coincides with the film's key moment.

### 5.7 Other languages

- **One composition with a language parameter.** The original language must render pixel-for-pixel identical to
  the frozen approved version (diff the frames), and its mix byte-identical. Duplicating the composition per
  language means fixing every later bug twice.
- **Rewrite rather than translate.** Each line is rewritten for the target language's word order and natural
  length, aiming for a similar duration. When narration mentions an on-screen label, it must use the label as the
  localised replica shows it.
- Route all text through one lookup function. Display names map at draw time while the underlying data keeps its
  keys.
- When the story relies on messy input data, the mess should be local too: for Japan, mixed half- and
  full-width characters, or 9月15日 alongside 2026/9/16.
- Currency: changing the symbol without converting values is a legitimate brief; converting is a different claim.
  Confirm which.
- Fetch a CJK typeface only when the active language requires it, and place it after the house face in the
  font stack so Latin text is unaffected. Japanese TTS may require a phonetic (kana) version of each line.
- **Remap time, not beats.** Camera keys, beats, pointer path and events are authored once against the original
  narration. For a second language, a piecewise-linear mapping converts its film time into authoring time, with
  anchor points placed on **words with matching meaning** (word order differs between languages). Subtitles use the
  language's own clock, and events convert back through the inverse. Keep each segment's rate (authoring seconds per
  film second) within about **0.5 to 1.4**: slower looks like slow motion, faster looks hurried. Swapping a voice
  means repositioning anchors.
- Level-match each language's integrated loudness to the original (a denser voice once came out 5 LU louder).
- Use the correct regional end clip from the brand kit, extracted at the film's frame rate.

### 5.8 Handing off to the brand's end clip

Bring the film's subject to precisely where the logo sits in the clip's opening frame, switch to a cropped copy of
that logo while the background transitions to the clip's background colour, then play the clip. The handover is
seamless.

### 5.9 A method, not a style

Rebuilding the UI says nothing about how the film should look. The idea, palette, staging (floating window, full
frame interface, device mockup, several windows), camera language, transitions and caption treatment are chosen
fresh for each film.

---

## 6. Visual treatments and the motion vocabulary

### 6.1 Role-based palettes

A treatment is a set of **eight colour roles plus three typeface roles**. Write a composition against roles and the
treatment becomes swappable by name. It is chosen during the pitch round, never applied silently.

| role | used for | minimum |
|---|---|---|
| ground | the background, ~70 % of the frame | |
| deep | a secondary background: vignette, distant planes, recesses behind cards | |
| card | panels sitting on the ground | |
| line | hairlines, panel borders, background grid | |
| mute | captions and secondary labels | contrast ≥ 3:1 against ground |
| ink | main text and the protagonist | ≥ 4.5:1 |
| accent | the single meaningful colour | advisory (yellow on white may be intentional) |
| accent2 | occasional companion colour | advisory |
| display, text and mono faces | logo and headlines; interface copy; code and figures | subset and embedded |

The repo ships six treatments sampled from its films. They are not ours to reuse, but the moods are handy shorthand
when pitching (actual colours should come from the client's brand). Described from its swatch sheet
(`gallery/sheets/looks.png`):
- **paper**: off-white canvas, near-black text, a single green "done" colour (red as backup), a serif logo.
  Fits SaaS and productivity.
- **dusk**: deep aubergine black, one glowing purple protagonist, creamy text, a gold second accent. Fits
  single-shape concept pieces and developer tools.
- **tabletop**: warm putty-grey surface, white objects with soft shadows, a coral-orange trigger colour. Fits
  physical cause-and-effect metaphors.
- **ultramarine**: an electric cobalt field, white text, lemon yellow as the one signal. Feels like a poster rather
  than software. Fits data and scale stories.
- **riso**: cream paper, hot pink and process blue, narrow heavy headlines, overlapping inks multiply. Feels like
  print. Fits collaboration and creative tools.
- **ember**: warm parchment, chocolate text, a glowing orange, a classical serif, unhurried pacing. Fits wellness,
  focus and lifestyle brands.

**Extracting a treatment from screenshots** (worth implementing ourselves):
- ground = the most frequent colour;
- ink = the most frequent neutral with ≥ 4.5:1 contrast (≥ 7:1 if available);
- accent = whichever of 12 hue buckets collects the most strongly coloured pixels; in software UIs the accent can
  cover as little as ~0.1 % of the image;
- accent2 = the next hue family at least 60° away;
- mute, line and card = neutrals whose contrast with ground falls in the ranges 3 to 6, 1.1 to 1.6, and below 1.1;
- deep = ground darkened a little on light themes, a lot on dark themes.

### 6.2 Motion vocabulary

For each move, the repo's gallery (`gallery/sheets/<move>.png`) pairs a strip of stills with a velocity plot.
Treat the table below as a list of ideas to implement independently in our `lib/motion.js`.

**Arrivals**
| move | behaviour | use it for |
|---|---|---|
| word rise | springs upward into place with a slight scale-up; opacity done early | introductory phrases, one word per beat |
| letter drop | logo letters fall in sequence, flatten on landing, recover by spring | the product name |
| card pop / card lift | a panel springs into view; on exit it rises, grows slightly and blurs | interface panels |
| masked rise | lines slide up from behind a clipping edge, ~0.13 s apart | stacked titles, a name emerging |
| typing | constant-rate characters, cursor solid while typing then blinking | prompts, search fields |
| tick | a checkbox jumps from 80 % size when its row is reached | task lists; the final row is the payoff |
| fly-in | a screenshot sweeps in with perspective tilt (about −18° easing to −9° yaw, a few degrees of pitch, 92 % → 100 % scale), pauses ~0.9 s, sweeps out | a quick burst of outputs; not a bridge |

**Bridges (the next scene comes out of the current one)**
| move | behaviour | use it when |
|---|---|---|
| container reshape | one rectangle interpolates into another on an exponential ease-out | the pressed control *becomes* the result; the most common bridge |
| circular reveal | a disc expands from a point on the subject to cover the frame | the subject opens into its own world |
| push into card | log-scale zoom into one card among several until it fills the frame and its interior is the next scene | choosing one of many |
| arc jump | a parabolic hop between slots, landed with a squash | the protagonist chooses the next item |
| converge | several items travel on staggered curved paths into a group | many become one (toward the lockup) |
| elastic switcher | panels swap under the pointer with overshoot while their labels trail behind | options cycling under the cursor |
| badge | a rotating disc grows beneath the converging group and becomes the mark | the cast resolving into the brand |
| staccato | words hard-cut one after another | a run of hits; the legitimate place for bare cuts |
| one continuous camera | over a single world, everything persists by definition | whole-film concepts |

**Contact (cause and effect)**: *impact* (compress on contact, then oscillate out); *split on impact* (letters
scatter by distance from the hit, rebound, rejoin); *click* (dip, vibrate, change state); *pointer* (follows the hand
path, shrinks per click); *velocity stretch* (elongate along the direction of travel, narrow across it);
*pointer-driven simulations* (a magnetic button, a lagging follower, a wobbly ring, a dangling rope) for showing
micro-interactions alive inside small cards.

**Camera**: keyframed position, rotation and log-interpolated zoom; parallax layers by depth; depth-of-field blur
by distance from focus; whip pan (exponential ease-in-out, ~540 px/frame peak at 60 fps); decaying seeded jolt that
is zero before its hit; slow push for holds (which counts as motion, so not on true rests); a far dot grid that
keeps constant screen size; world-to-screen projection helpers so checks can measure screen boxes.

**Fluid backgrounds**:
- *light pool*: a persistent glow rising from below the frame, resting with its edge near 84 % of frame height;
  it floods in ≤ 0.4 s and recedes over ~1 s, and text turns white where the bright core passes. The background
  itself becomes punctuation.
- *rings*: about three concentric rings radiate from one point 0.16 s apart, and the next scene is visible inside
  the innermost one, so the flood hands over to the following scene with no wipe needed.
- *silk*: low-resolution warped noise in two octaves, upscaled with heavy blur and a single pale streak, coloured
  through a ramp with a dark band between two light ones (that is what makes it read as fabric). Use for living
  cards, wallpapers and lock screens with no content.
- *conveyor*: steady speed after a gentle start; each card's own animation runs on the belt's clock so everything
  slows down together when the belt stops.

Choosing a bridge: pressed control becomes result → container reshape; subject opens up → circular reveal; one of
many becomes the scene → push into card; subject picks next → arc jump; options switch under the pointer → elastic
switcher; cast becomes brand → converge, then badge; hits → staccato; whole world → continuous camera.

---

## 7. Observations from the example films

Every observation below comes from frames I pulled from `cases/*/*.mp4` (1 fps contact sheets plus 10 fps strips
around transitions), read against each case README.

**motion-web, 15 s.** *Seen:* very small sentence type on an off-white canvas, a serif logo with a tiny green verb
beneath it, a typing card around a fifth of the frame wide, a checklist panel, three real sites sweeping through in
perspective with blur between 7 and 9 s, four little cards with live mechanisms that a pointer pokes, one large
browser window holding around 12 s, a single small capitalised word, then a black closing card. *Takeaway:* pacing
alone can make a film work (contrasting durations, a pause before the hits, lots of empty space), but its bridge
score was only 0.56 with four unbridged transitions. It became the house template, and copying it later was
punished.

**Pocket Weather Club** (described in `references/rhythm.md`; video not included). *Takeaway:* good pacing with
pure substitution scored 0.00 and was rejected. Once the mascot, the expanding card, the opening stage and the
converging cast carried every transition, it reached 0.75 and was approved. Most bridge moves come from this film.

**one-dot, 15 s.** *Seen:* a purple point on near-black that becomes a thin cursor, branches into a four-item list
with dot bullets, sits as the cursor while a request is typed, then streaks across the frame (the shutter smear is
obvious at 5 s), becomes an outlined loading circle, straightens into a labelled spring graph, falls and bounces,
turns into the sun on a cream "film" card, and ends as the point above the "i" in the logo. *Takeaway:* when one
object's identity survives everything, continuity is automatic (score 1.00, no assets). The fixed-camera version was
rejected for lacking tracking shots, and a dim far grid gives the camera something to slide over on a black ground.

**knockon, 15 s.** *Seen:* an overhead view of a pale grey table. The pointer presses a "return" key, a red ball
rolls down a channel, flips a switch, and topples ten task tiles like dominoes. The last tile hits Send, and a
"10 tasks, done." alert leaps up, hangs with a long blurred shadow, drops and receives a checkmark. A wide shot then
shows the entire course traces a giant return-key arrow, under the product name and the line "Press once. The rest
follows." My probe found zero cuts and 27 % stillness, one world throughout. *Takeaway:* causation as continuity,
altitude via shadow, and the product's icon hidden in the layout, with the tagline describing the mechanism itself.

**clearing, 15 s.** *Seen:* an electric blue field with a year of tiny squares filling in, a dive into one day whose
schedule sharpens as it grows, a yellow line scanning down to a dashed open slot at 15:00, a yellow "Clear." block
landing in it, then at 9 s a violent zoom-out where the calendar dissolves into radial streaks (the 10 fps strip shows
true motion smear). Yellow cells ripple across the year to spell the name, closing with "Room, found in a full year."
*Takeaway:* nesting as continuity, a screen-anchored camera spanning 1x to 300x, detail that fades in by on-screen
size, the name hidden in the data, completely frozen pauses, and shutter blur that sells the whip.

**pith, 21.5 s.** *Seen:* the frame filled by enormous amber pixel cells, a pull-back through terminal output, a
window outline drawing itself, then a single-frame switch from amber dark mode to a light theme (the app's real theme
toggle). The camera dives 44x into two blocky pixel eyes in the title bar that blink and look aside, follows their gaze
down to the input field where a message is typed, then retreats to a small centred window with seven tool names lined
up below and "Pith" in lavender. *Takeaway:* borrow the product's own behaviour for the transition, make a mascot
close-up do double duty as the pause, build the claim from objects already on screen, use the product's real
typeface, and hold the music back until the window exists.

**ebb, 15 s.** *Seen:* huge high-contrast serif numerals ("25:00") in extreme close-up on warm paper, a pull-back to
the desktop timer app with rolling digits, a punch to "00:00" as orange light swamps the frame. In the 6 fps strip the
orange recedes as concentric rings from a single point, and the phone's lock screen (9:25, a "break" live activity)
appears inside the smallest ring. Then a whip down to rows of silky gradient cards at three depths, a pull-back into a
weekly grid, and the logo surfacing from the glow. *Takeaway:* a moving light can bridge every transition; rings
replace wipes; layered depth and focus falloff look expensive without any cuts.

**overlap, 15 s.** *Seen:* a cream page slapped onto a warm grey bed, out of focus at first. A pink pointer labelled
"you" and a blue one labelled "them" drag inking rollers in from opposite sides, leaving two misaligned clouds of
halftone dots. A magnifier inspects the misalignment, "them" clicks a crosshair, the blue layer jumps into alignment and
a violet ampersand appears. A run of other word pairs follows (sketch & colour, question & answer), then the name in
pink and blue, and only now does the previously locked camera push in to where the two halves of the name overlap.
*Takeaway:* the idea must exist physically (explanatory labels hurt); hold the camera still until the payoff, then let
it move; one production process (risograph) can define the entire look.

**unbroken, 15 s.** *Seen:* black background, ivory brush strokes, split down the middle. On the left, notification
chips keep interrupting the brush, leaving 17 fragments; on the right, one unbroken circle. After a pause the left half
drops away, the camera retreats, and the circle turns out to be the "o" in "unbroken", followed by "Finish the circle."
and a small red seal. My probe reads 63 % static with a 6.6 s calm stretch, so restraint can look premium.
*Takeaway:* the side-by-side concept, procedural brushwork (dozens of fine bristle lines with dry-brush gaps rather
than a few fat bands), a jolt that affects only the interrupted side, and a reminder that stillness metrics over-read
on dark backgrounds.

**skill-demo, 15 s.** *Seen:* "A launch video from one prompt." on white, then the words "one prompt." slide down
into a text field that expands around them (the 10 fps strip shows the reshape between 0.5 and 0.8 s), a command menu,
a selected chip, a loading card with ticks, a pale yellow result card with a sun, "Every kind of day.", a converging
badge, a white "ONE SKILL." on black, and a falling-letter logo. *Takeaway:* polished and bridged throughout, but it
was rejected for echoing motion-web. Passing the checks is not the same as having an idea, so the pitch round cannot be
skipped.

**onetake launch, 30 s.** *Seen:* a rounded input bar on a cream desk. A full request is typed; on send, the text lifts
and the bar balloons, blurred, into a Mac calendar window whose events pop in within 0.4 s. The week view collapses to a
phone. A shorter second request opens into a purple earbuds ad where comic-book noise words (WOOF, CLANG, BOOM, HONK)
pile up until a charging case clicks shut. The third request is a single word: the bar compresses into a line that
whips across the desk with heavy blur and turns into the opening gridline of a festival poster. Finally all three
mini-films line up above the bar and a block cursor writes the name. *Takeaway:* a recurring anchor that gets shorter each time
(sentence, four words, one word) accelerates the pacing; each sub-film has its own palette while the shared desk keeps
it unified; the music was cut so a silent beat and the hit after it land on the name. Static share is only 9 %: a
dense showcase relaxes the stillness rule, which is why stillness targets should come from the reference.

**domino, 25.6 s.** *Seen:* a rendered phone orbiting in macro, tipping in slow motion, then lines of phones
toppling, splitting into branches, a first-person ride along the leading edge, a field of dark screens that light up
together on the musical drop, and a huge field resolving a smiling vintage-computer face. The last upright phone shows
the face, winks and goes black. Built with Blender and instanced three.js, rendered through the same shutter process.
*Takeaway:* most of the feedback rounds were about the music and its energy curve (a boring middle section, the pulse
fading after 10 s, a side-to-side camera sway that felt stiff); freezes timed to beats looked staged; stillness is just
2 %, against a reference that was 0.4 % still.

---

## 8. Gate checklist for our pipeline

Items marked **[auto]** should become part of our own tooling (`motion-studio/review.sh` plus new checkers). The
rest need a human or model review with the contact sheet open.

**Gate 1, inputs**
- [ ] Reference measured **[auto]**: static share, near-static share, longest calm, cut times, flurries, energy strip,
      element scale, optionally median t80 and smear. Target numbers written down.
- [ ] For a style reference: its governing rule, its measurements (hex values, grid spacing, cap height), and which
      effects were simply cheap in its tool. Its scene order is not reused.

**Gate 2, pitch**
- [ ] Three pitches with different core visual ideas, one line each about the image.
- [ ] Each lists: the first 2 s, the survivor at each transition, what it forbids, its visual treatment (palette,
      faces, staging, camera language, transitions), and how the message is physically present in the picture.
- [ ] Nothing recycled from the previous client film (idea, treatment, camera language).

**Gate 3, beat sheet**
- [ ] Columns: time, beat, moving, static, link to next, audio.
- [ ] Durations differ by ≥ 4x and std/mean ≥ 0.25 **[auto]**.
- [ ] A frozen pause of ≥ 1 s after the hook, with no drift, sway or settling camera during it.
- [ ] Each transition names its survivor. Bare cuts only inside a staccato run or into the closing card; any other
      deliberate cut is listed with its reason.
- [ ] Every reaction has a visible trigger.
- [ ] Consecutive shots never exit the same way.
- [ ] No particles, confetti or decorative sparkle; no text that merely fades in.

**Gate 4, composition (no render yet)**
- [ ] Deterministic **[auto]**: seek to t, elsewhere, back to t and compare hashes; list any timestamp where seek
      throws.
- [ ] The page exports `track(t)` (screen-space boxes, ids, content keys), `events()`, a max-travel function, and
      must-stay-visible windows.
- [ ] Bridge score ≥ 0.7 (fail below 0.5), with each transition reported as bridged, pinned or unbridged
      **[auto]**. Fewer detected transitions than beats means checking bridges by eye.
- [ ] Visibility: listed elements inside the frame and outside the 9:16 overlay bands at every sample **[auto]**.
- [ ] Easing variety: snaps and springs where things land, not one gentle S-curve throughout (look at the
      travel-weighted t80 distribution) **[auto, advisory]**.
- [ ] Legibility: every text that must be read reaches the size floor at its displayed zoom (font size × scale ×
      zoom) **[auto]**.
- [ ] One frame per beat on a phone-sized contact sheet, scored on the house critique axes.

**Gate 5, render**
- [ ] Review drafts at 1080p30; full resolution only after approval.
- [ ] Shutter simulation on: linear-light averaging, speed-driven sample counts, static-frame skipping,
      cut-awareness **[auto]**.
- [ ] Any peak above 80 px/frame (1920 long edge) only with shutter blur **[auto]**; inspect a 12-frame strip
      around the fastest moment for stepping or banding.
- [ ] Dark gradients dithered with static noise; no banding after encoding.
- [ ] Stillness on the render: ≥ 25 % static (or in line with the reference) plus a ≥ 1 s calm run **[auto]**.
- [ ] A flurry exists if the reference or the concept has hits **[auto]**.

**Gate 6, audio**
- [ ] Audio timed from the page's exported events and signals, never from retyped times.
- [ ] Fewer sounds than beats; nothing within 40 ms of another; one shared reverb with distance-based sends.
- [ ] Holds go silent after a breath; silence is planned.
- [ ] Short-term K-weighted loudness at each beat: every landing louder than its approach, hits loudest **[auto]**.
- [ ] Band energy per half-second window: no window dominated by 100 to 300 Hz **[auto]**.
- [ ] Effects audible against music within their own event windows (RMS in the window and in 0.8 to 4.5 kHz)
      **[auto]**.
- [ ] Post-AAC peak ≤ −3 dBFS, no clipping, integrated loudness on target (house −14 LUFS) with true-peak headroom;
      ≥ 15 % quiet windows when there is no narration **[auto]**.
- [ ] No generic shimmer-chord ending; every source and track cleared for commercial use, licenses stored.

**Gate 7, interface demos and languages**
- [ ] Interface rebuilt from the client's own reference captures and compared state by state at 1:1.
- [ ] All on-screen figures and text come from real product output.
- [ ] One close-up per operation, readable window size, tight rounded-rectangle highlights (no glow by default).
- [ ] Beats pinned to narration words; the narration sets the runtime.
- [ ] Additional languages: same composition with a word-anchored time remap (rates 0.5 to 1.4); original language
      pixel-identical to the frozen approved cut **[auto]**; loudness matched per language **[auto]**; lines
      rewritten rather than translated; narration uses the localised labels.
- [ ] No camera jolts in narrated interface films.

**Gate 8, final viewing**
- [ ] One muted viewing: is the idea clear from the images alone?
- [ ] One viewing at phone size: is every word that matters readable?
- [ ] Ask: is any beat swapped rather than bridged? Does the frame ever freeze? Is there a lull before the climax?
