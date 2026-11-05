# Treatment: StraightScale · 06 "The 108-hour week"

Written before the scene code, updated after review. Each section answers a question a director would be asked.

## 1. Reference measurements: steal / leave
Reference: `motion-studio/refbank/cards/tt-foil-finance.md` (TikTok, 1.5M plays, 119k likes, 13 s, data-infographic,
devices chart-grow, counter-ticker, timeline-progression, big-number; calm piano score; no voiceover). The clip itself
is not in this container, so its numbers come from the card (measured 14 Oct 2026):
cuts 0.0 per 10 s, 13.0 s between big changes, change-rhythm CV 0.0, quiet share at 2 fps 0.16, hook change 0-2 s 0.01.
Category medians (HANDOFF.md section 7.3, data-infographic, n = 5): 0.7 cuts per 10 s, 3.75 s between big changes,
hook energy 0.16.

| Steal (grammar) | Leave (content) |
|---|---|
| The whole film readable at 0 s: a plain, true-sounding headline over a dark ground, an empty chart, a big clock | Switzerland/Liechtenstein, their photo, their data, their music |
| One step line with a value label riding its tip; the y axis rescales on new highs so steps read as jumps | The light-blue line and glowing endpoint (glow on UI is banned here) |
| A big date-time readout under the chart ticking at a constant rate | Months and years: we tick hours and days of one example week |
| Steps at uneven moments keep the viewer waiting for the next one | A tail of 4 flat seconds: our tail carries the system line and the CTA |
| Calm piano; no voice; the title is the script | A track we do not own |
| End on "now" (the clock lands back on Mon 09:00) | |

Registry check before hand-building (house rule): `mk-line-graph`, `data-chart`, `animated-bar-chart`,
`decline-chart`, `beat-timeline` exist, but none is a live step chart driven by a clock with an auto-scaling axis, so
the chart is hand-built in SVG inside the composition.

## 2. Concepts
The batch brief fixed the concept; two alternatives were considered and are offered as follow-ups.

| | A: The 108-hour week (chosen) | B: The dark house | C: One inbox, two clocks |
|---|---|---|---|
| Idea | A step chart climbs only in the closed hours of one example week while a day-and-time counter ticks; bubbles arrive in the dark columns | A 7 x 24 grid of hour cells; open hours light up like windows, closed hours stay dark while bubbles pile on them, then the system lights every cell | Split top/bottom: the same week with and without a system; the bottom inbox empties as the top one fills |
| Hook (0-2 s) | Headline readable at frame 0, clock already ticking, first step at 0.56 s | A wall of 168 dark cells with a few lit | Two identical clocks start together |
| Signature device | chart-grow + counter-ticker | grid-mosaic | split-screen |
| Engine | HyperFrames (SVG + type) | HyperFrames or canvas | canvas |
| Risk | Text-heavy; must stay readable at phone size | 168 cells are small on a phone | Two timelines halve the size of everything |

`refbank.py check --client straightscale --category data-infographic --devices chart-grow,counter-ticker,timeline-progression,big-number --palette dark`
returned "ok: no repeats against the last films" (previous films: kinetic-type, spectacle-world, kinetic-type, brand-ad).

## 3. Art direction
- Design read: a calm strategist showing an owner one honest piece of arithmetic. Editorial, quiet, exact.
- Palette by role: ground charcoal #1F1F1F (with seeded grain and a soft vignette, baked once); ink ivory #F8F6EF;
  secondary warm grey #9B958D (note, open-hour flats, axis labels); accent mark-gold #DD9A10 for everything that
  means "closed hours" (the word closed, the climbs, CLOSED, the answer squares, ANALIZA); open-hour columns ivory at
  7.5 % opacity; red only in the real logo. No gold text on ivory, no red text on charcoal.
- Type in motion: every line rises out of its own mask on a spring (no fades); exits leave faster than entrances,
  upward for the top block and downward for the lower block. Headline Playfair Display 700 80 px; note Montserrat 500
  44 px; clock Montserrat 800 116 px tabular; labels 27-38 px.
- Layout (9:16): headline y 300, note y 588, message lane y 730, plot 160-920 x 838-1218, day labels y 1258,
  chip y 1300, clock y 1346. Everything inside x 96-940 and y 269-1536. 4:5 has its own table (headline y 80, plot
  150-990 x 556-880, clock y 1000).
- Signature device: the step chart with the ticking day-and-time counter, present from frame 0 to the fold at 17.6 s;
  its tip square survives to the end as the caret and the logo's gold square.
- Motion vocabulary: closed-form springs (`spring(t, k, d)` from motion-studio/lib/motion.js) for every entrance,
  rescale, punch and flight; a constant clock (18 h/s) with a power ease-out for the last 14 hours; transitions are
  carries (label flies into its sentence, light sweeps the closed hours, chart folds onto its baseline, square hops).
- Texture: static grain on charcoal only. No particles, no glow.
- Sound world: felt-softened upright piano in A minor, one chord per day; cello/viola/violin sections enter mid-week
  and build into the weekend; a soft clock tick every third hour (16th notes), a low pulse on every closing; a
  glockenspiel ping (unresolved degrees) for each message, a rising harp answer (C pentatonic) for each answer; two
  planned silences (after the landing, before the turn to C major); the ending is a piano and strings cadence
  V to I on the logo, then a decay.
- Banned for this piece: a centred card layout, counts on bubbles, names, any number not derived from the example.

## 4. Script (on-screen only, no voice)
| # | On screen (English) | Words | Reading rule need / got |
|---|---|---|---|
| 1 | Hours a week your business is closed while clients still write. | 11 | 2.4-2.9 s per line / 13.5 s |
| 2 | Example: open 09:00 to 19:00, Monday to Saturday. | 8 | 2.6-3.2 s / 13.6 s |
| 3 | 168 hours in a week. / You are open 60. / Closed 108. | 11 | 2.2-2.6 s per line / 4.2-5.5 s |
| 4 | A system answers in those hours: | 6 | 2.4 s per line / 3.2 s |
| 5 | instant replies, / follow-up, / booking. | 4 | 2.0-2.5 s per item / 2.0-2.6 s |
| 6 | Comment ANALIZA. | 2 | 2.0 s / 5.5 s |
| 7 | The booking button for the free 45-minute analysis comes in the DM. | 12 | 2.4-3.0 s per line (5.2 s as one block) / 5.6 s |
Rule: max(1.5 s, non-space characters / 15 + 1.5 s) from the first fully visible frame (`tools/textcheck.mjs`).
Alt hook (not used): "Your shop closes at 19:00. Your clients don't."

## 5. Beat sheet (on the music grid: 90 BPM, D_k = 0.556 + 1.333 k, one day per bar)
| Time | Beat | On screen | Moving | Still | Link to next (what survives) | Audio |
|---|---|---|---|---|---|---|
| 0.00-0.56 | Hook | Headline, note, empty chart with six open-hour columns, "0 h", OPEN, Mon 09:00 | clock ticking, tip sliding along zero | headline | the tip square | soft piano E5 + A3 on frame 0, ticks |
| 0.56-7.22 | Weekdays | each evening the line climbs (gold), each morning it flattens (grey); a bubble pops each night; CLOSED/OPEN chip flips; day name rolls; axis rescales on Wed and Fri | tip, counter, bubbles, column light, axis | headline | the line keeps going | Am F C G Am F, low pulse on each closing, ticks on 16ths, pings |
| 7.22-9.89 | Weekend | the climb does not stop on Saturday night; Sunday has no flat; the clock slows into Mon 09:00 | tip, counter (slowing), 4 bubbles | | the riding number | strings build, Dm, slowdown ticks become a rising piano run |
| 9.89-11.22 | Landing + rest | 108 h punches, OPEN, Mon 09:00; then frozen 1.03 s | punch only | everything after 10.19 | the number 108 | E major hit + pulse, then silence 1 |
| 11.22 | Math 1 | clock row leaves; "168 hours in a week." | light sweeps the time axis | chart | | Am, air sweep L to R |
| 11.89 | Math 2 | "You are open 60." | open flats turn ivory, columns brighten | | | F |
| 12.56 | Math 3 | "Closed 108." (v2: set at 80 px, the payoff is the biggest line on screen) | the 108 drops from the tip and slides into its sentence; climbs pulse | | the 108 lands in the sentence | E + low pulse, air |
| 13.39-14.22 | Swap | headline exits up; "A system answers / in those hours:" rises | lines | chart | the chart | silence 2, then C major (the turn) |
| 14.22-16.00 | Answers | "instant replies," "follow-up," "booking." one by one | the open-hour light sweeps over every closed column; each bubble turns gold and its three dots become a check (v2; v1 had a 20 px badge) | | the lit chart | harp answers rising in C pentatonic, strings |
| 16.00-17.56 | Rest | everything lit and answered | nothing | all | | quiet Am, violas |
| 17.56-19.22 | CTA | top text leaves, then the chart folds onto its baseline, then the maths leave (v2: sequenced, at most three movers); "Comment" rises; ANALIZA typed letter by letter behind the gold square caret; body rises; from 18.72 s the square goes the long way round (right of the body copy, down, in under it) to the logo | fold, square, typing | | the square | F, air, soft key clicks; whoosh over the whole hop, G pickup at 18.89 |
| 19.22-21.22 | Logo | the square lands on the logo's gold square; the real wordmark-white.png is revealed by a clip that grows out of it | clip reveal | text | | C major + low pulse (cadence V-I) |
| 21.22-24.00 | End | gold rule draws under ANALIZA; hold | rule (0.5 s) | all after 21.7 | | C6 piano + glockenspiel (v2: louder, the message ping resolved to the tonic), decay to silence |

Self-check: beat lengths (big-change units) 0.56 / 6.67 / 2.67 / 1.33 / 0.67 / 0.67 / 0.83 / 0.83 / 1.78 / 1.56 /
1.67 / 2.0 / 2.78 s: CV 0.85 (>= 0.25), longest 12.0x the shortest (>= 4x). A real rest after the hook's payoff
(10.19-11.22 s, frozen) and before the CTA (16.0-17.56 s). Every transition names its survivor (tip square, number,
chart, lit chart, square). Every reaction has a visible cause (the clock passing a closing causes the climb and the
pulse; the light front causes each answer). Nothing new is static for more than 4 s (pacing.py: no frozen stretch
over 3 s). The idea reads with the sound off (all on-screen).
