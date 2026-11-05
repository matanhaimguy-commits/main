# Treatment: StraightScale · Film 04 "One message, all the way"

Written before the scene code, then corrected where the build taught us something (marked "build:").

## 1. Reference measurements
**ig-satisfy3dverse** (109.2M plays, 2.7M likes, 534K shares; card `refbank/cards/ig-satisfy3dverse.md`, metrics
`refbank/metrics/ig-satisfy3dverse.json`; the clip itself could not be downloaded here, so we use the bank's
measurement, sampled every 1.5 s over 61.5 s):

| Metric | Reference | What it means for us |
|---|---|---|
| cuts per 10 s (colour-gated) | 0.16 (one cut in 61 s) | one continuous world, the camera does the editing |
| mean s between big changes | 1.54 | something big at least every 1.5 s |
| change rhythm CV | 0.15 | very regular: locked to the track's tempo |
| quiet share (2 fps) | 0.0 | no rests at all in the reference |
| hook change 0-2 s | 0.425 | already moving in frame 1 |
| palette | #d3d2ce #cbcac6 #bfbdba (pale warm greys), #aa9d93 #6f5e57 shadows, one hot ball | a pale wall and one saturated hero |
| type | 60-80 px script lettering written on the wall | captions as part of the set |

**Steal (grammar):** one hero object triggers every sound; every target answers visibly (lights, wobbles) while its
note plays, so ear and eye agree on each hit; a follow-cam that keeps the ball in the centre third; new set pieces
arriving every 1-2 s inside one continuous shot; the last frame is the first frame (loop); calls to action live in the
set, not on a card.

**Leave (content):** their ball, ducks, horns, chimes and cubes; the phonk track; their lettering and handle; the
"Guess all songs" game (our game is "watch where this client gets lost").

**Where we deliberately differ:** the reference never rests (quiet share 0.0). Our story needs one failure and one
silence, so we plan one real rest (the dark, 2.5 s); everywhere else we keep the reference's rhythm (a contact every
0.25-0.5 s, a station every 1.0 s). v1 also held the ask for 5.6 s; the independent review found that the end ran out
of energy (6.4 quiet seconds in the last 9), so v2 holds it 3.6 s inside a live end (see §6).

## 2. Three concepts (different central visual ideas)

| | A · Marble run (chosen) | B · The unanswered bubble | C · Two doors |
|---|---|---|---|
| Idea | A crimson ball (one client's message) bounces down a marble wall of stations; Reply is missing the first time | A single speech bubble sits on a phone screen while time-lapse light crosses the room; it greys, curls and drops off; then the system answers it in a chain reaction of bubbles | A split frame: the same ball enters two identical walls; left has gaps, right is complete; the halves race |
| Hook (0-2 s) | "Watch where this client gets lost." while the ball is already flying | a "seen 3 h ago" bubble ageing | "Same client. Two businesses." |
| Signature device | beat-sync-hits on a marble run, dolly-follow, seamless loop | time-lapse + chain reaction | split-screen race |
| Style / engine | canvas engine, physics solved backwards from the beat | canvas or HyperFrames | canvas |
| Risk | building a convincing 2.5D physical set without 3D | fake UI risk (house banned list), slower hook | halves the frame: labels too small at phone size |

Recommendation: A. It is the brief's concept, it carries the reference's proven mechanism (sync is the
satisfaction), the message is physical (a missing plate, a fall into a real hole), and it loops. B and C are offered
as alternatives.

`refbank.py check --client straightscale --category beat-sync --devices beat-sync-hits,marble-run,dolly-follow,seamless-loop`:
"ok: no repeats against the last films" (previous: kinetic-type, spectacle-world, kinetic-type, brand-ad).

## 3. Art direction (chosen concept)
- **Design read:** a quiet, expensive object: a pale marble wall like a gallery, brass and ivory fittings, one
  crimson ball. Calm and exact, like the brand voice. The satisfaction comes from precision (every hit on the beat),
  not from noise.
- **Palette by role:** ground = ivory/marble wall (#F6F2EA base, warm grey veins); ink = charcoal #1F1F1F (labels,
  captions); accent = crimson #B31217 (lit plates, the route, accent words), the ball in mark-red #BE0F18 shading;
  brass = mark-gold #DD9A10 (pins, pegs, tube rings, flow pulses: objects only, never text on ivory); the dark =
  charcoal (the hole and the rest). Gold text only on charcoal ("Gone."). No red text on charcoal.
- **Type in motion:** Playfair Display 700 for captions (accent words in 700 italic crimson), Montserrat 800 caps
  +5 px tracking for station labels, Montserrat 600 for the sub-labels. Captions rise out of a mask on a spring with
  opacity full early (never a fade), stagger 0.12-0.15 s per line, leave upward. All captions live in one top band
  (y 290-530 on 9:16). v2: the band is fully opaque down to 22 px under the lowest glyph row (y 549) and fades only
  below the type (to y 659), so nothing on the moving wall can ghost through a caption.
- **Layout and focal points:** the ball sits in the centre third (camera anchor y 980, aiming 0.22 s ahead); the
  current station is always between y 700 and 1500; captions in the top band; nothing key in the top 250, bottom 400
  or right 140 px. v2: the real logo sits on an ivory plate in a niche above the cradle, behind two marble doors that
  open only when the ball lands home (21.06 s) and close as the flipper arms (24.15 s); it is only ever seen in the end
  frame, at least 28 px under the band's fade (11 px in 4:5).
- **Signature device:** the ball path with beat-synced hits (beat-sync-hits + marble-run + dolly-follow), present
  in every second except the dark rest, where its absence is the point.
- **Motion vocabulary:** ballistic arcs (g = 6000 px/s²) solved backwards from the beat times; impacts squash the
  ball along the contact normal; plates dip and wobble on damped springs; pegs ring out; the camera is a critically
  damped follow (ω 9), a dive into the hole (log zoom to 3.4x), a whip up, and one pull-back to the whole map.
  Transition rule: no cuts at all; every change is the camera moving through one continuous wall.
- **Texture / material:** procedural marble (veins from turbulence), soft wall shadows offset down-right (light from
  top-left), static film grain at 3.5 % so frozen frames stay frozen.
- **Sound world:** the hits are the melody (marimba on pegs, glockenspiel + vibraphone on stations, a tubular bell on
  Reminder); a light organic beat (cajon, hats, shaker, claps once the system runs); a bowed vibraphone pad; strings
  on the map. One shared room. The planned silence carries a faint room tone (v2; v1 was digital zero). Station notes
  sit about 3 dB over the pegs (v2).
- **Banned for this piece:** platform names or logos, chat-app screens, fake UI, numbers, any glow on the type,
  particle bursts (the peg ring is one thin ring), a shimmer-chord ending.

## 4. Script (on-screen, no voice) · v2 timings
| # | On screen | Time (s) | Purpose |
|---|---|---|---|
| 1 | Watch where this / client *gets lost.* | -0.25 (loop) to 3.95 | hook, a guessing game |
| 2 | (station labels) COMMENT · REPLY (dashed, missing) | 1.5 / 3.5 | the path the viewer watches |
| 3 | *No reply.* | 3.95 to 6.35 | the cost, inside the hole |
| 4 | *Gone.* | 4.3 to 6.4 | |
| 5 | Build the / *missing step.* | 6.95 to 10.2 | the fix |
| 6 | REPLY · instant answer (plate) | 7.5 on | the first Build item |
| 7 | COMMENT · REPLY · BOOKING · REMINDER follow-up · VISIT rebooking · REVIEW · REFERRAL | 9.5 to 17.0 | the whole path, lit on the beat |
| 8 | Every step answered. | 17.25 to 19.95 | the point |
| 9 | That is a *system.* | 17.6 to 20.0 | over the whole lit map |
| 10 | Send this to an owner / who loses clients / after the *first message.* | 20.25 to 24.5 | the ask (share), 3.6 s once fully in |
| 11 | StraightScale logo (real file, behind the hatch) | 21.06 to 24.4 | the brand, shown only when the client is home |

Word budget: 40 caption words in 25 s (no voice). Reading gate (the house rule the review applies): 0.25 s per word
+ 0.5 s, fully in to the start of the exit; every cue passes (`tools/readcheck.mjs`, which also prints the stricter
Lemo-Opuscar figure as advice: the ask is 1.4 s under it by design, see §6).
Alternative hook (not used): "Follow this message. It doesn't make it."
Post caption (not on screen; the brand kit's only path): see `deliver/v2/post-caption.txt`.

## 5. Beat sheet · v2 (120 BPM; grid A from 0.0, grid B from the lock at 7.0; loop 25.0 s)
| Time | Beat | On screen | Moving | Still | Link to next (what survives) | Audio |
|---|---|---|---|---|---|---|
| 0.0-1.5 | launch | hook; closed hatch; ball on the flipper in a close shot (z 1.32), the end's push-in still settling | flipper, ball, camera follows and widens to 1.18 | band | the ball | flipper clack, marimba A4, D5 on pegs; Dm bar |
| 1.5-3.5 | first run | COMMENT lights crimson; route lights behind the ball; dashed REPLY ahead | ball hops along COMMENT, two pegs | hook text | the ball | glock+vib F5 on COMMENT, E5 C5 E5; C bar (asks for F) |
| 3.5-4.0 | the miss | ball passes through the dashed outline and falls into the opening | ball shrinks into the dark, camera dives | dashed REPLY | the hole (camera goes into it) | no note where Reply should be; fall whoosh |
| 4.0-6.5 | the dark (rest) | inside the shaft: a warm dark deepening to the far end, corner edges, rings of the shaft wall, the ball's last glint (4.0-4.4); No reply. / Gone. | rings drift outward, camera keeps sinking (3.4x to 3.9x) | the lines | the hole (camera pulls out of it) | music cut on the downbeat; room tone about -50 dBFS; far thump |
| 6.5-7.9 | rebuild | REPLY slides in and locks (7.0); Build the missing step. (6.95); instant answer opens on its face | plate on a spring, camera settles (Reply at y 1300) | wall | the wall (camera whips up it) | bowed F swell; lock = first hit after the silence |
| 7.9-9.0 | whip up | the cradle and the waiting ball, closer than pass 1 (z 1.42); hatch closed | camera whip with motion blur | caption | the ball | whoosh; quiet F bar |
| 9.0-12.6 | pass 2 | the same first phrase, shot differently: tighter, the camera swinging with the ball and leaning toward Reply | ball, swinging follow cam | caption until 10.2 | the ball | Dm, C again, a touch fuller |
| 12.5-17.0 | the full run | REPLY lights (the missing note), BOOKING, REMINDER, VISIT, REVIEW, REFERRAL, a station every 1.0 s | ball, plates, route, follow cam widening back to 1.18 | | the ball (kicked into the tube) | G5 + harp on Reply, F lands on 13.0 with the full beat |
| 17.0-20.0 | the system | Every step answered. / That is a system. over the whole lit map; light flows down the route | pull-back, flow pulses, ball in the tube, the map drifting up with it | map | the ball (tube ends at the cradle) | half-time, strings, harp climbing with the ball's height |
| 20.0-21.0 | flight home | the camera flies home ahead of the ball; the ask rises (20.25-20.51) | zoom in, ask | | the ball | soft whoosh; Bb |
| 21.0-24.15 | home | ball lands (21.0); the hatch opens on the logo (21.06-21.4); the path stays lit; taps at 22.0, 23.0, 23.5 send light pulses down it | slow push from the logo frame toward the hook's close-up | ask, logo | the ball | F lands; stone leaves + brass stop; taps; F, C bars |
| 24.15-25.0 | reset, loop | hatch closes, path lights reset, flipper arms (24.45), ask leaves (24.4-24.5), hook rises (24.75) | doors, flipper, type | | the ball (flipper fires at 25.0 = 0.0) | hatch stop; cock click; C leads into the opening Dm |

Checks: beat lengths 1.5, 2.0, 0.5, 2.5, 1.4, 1.1, 3.6, 4.4, 3.0, 1.0, 3.15, 0.85 s: CV 0.57 (>= 0.25), longest/shortest
8.8x (>= 4x) · a real rest after the hook (the dark, 2.5 s, inside the hole) · every transition names its survivor (no
cuts) · every reaction has a visible cause (lights, wobbles and notes are ball contacts; the plate slide is caused by
the rebuild line; the hatch by the landing and the flipper arming; the pulses by the taps) · nothing important frozen
> 4 s (pacing.py on the delivered master: longest quiet run 1.5 s, v1 4.42 s) · the idea reads with the sound off.

## 6. v2 revision (independent review r1, `docs/review_independent_r1.md`)
| Finding | What changed | Why this way |
|---|---|---|
| 1 major: headline over a ghosted logo (0.8-3.0, 7.9-8.3, 9.8-11.0) and a ghosted COMMENT plate under the rebuild caption | (b) the band is opaque behind every glyph row and fades only below the type; its colour follows the light, so it stays opaque through the dive and the rebuild; band windows open 0.4 s before a caption and close after its last line has left. (c) the logo got a deliberate exit and entrance: it sits behind a marble hatch that opens only when the ball lands home and closes before the loop. The rebuild framing moved Reply to y 1300 (4:5: 1085) so COMMENT settles below the fade | a wall-mounted logo above the cradle has to cross the top band whenever the follow cam descends; hiding it physically, with a cause, keeps it clean and turns it into a payoff (the brand appears when the system is complete). `tools/ghostcheck.mjs` proves it: 0 levels of deviation under every caption frame in both formats |
| 2 minor: the end ran out of energy | loop 27 s -> 25 s; the ask rises during the flight home and holds 3.6 s once fully in; the map drifts up with the ball; the path stays lit through the ask and pulses on each tap; the hatch opens and closes; the camera pushes from the logo frame into the hook's close-up; the flipper arms | no quiet run over 3 s (delivered master: 1.5 s, the planned dark) |
| 3 minor: hook change about half the reference | frame 0 is now a close shot (z 1.32) of the ball on the flipper, with the end's push-in still moving; deeper marble veins | measured 0.21-0.22 at the reference's 1.5 s step (unchanged within noise): the pale wall and the opaque band limit how many pixels change; kept the calm wall rather than cluttering it |
| 4 minor: pass 2 repeated pass 1's footage | pass 2 is shot closer (z 1.42) with a swinging follow that leans toward Reply; the whip that leads into it lands on that closer frame | same physics (the missing note must replay the same phrase), different film |
| 5 minor: the dark looked like a title card | inside the shaft: perspective edges, drifting rings, warm falloff, the ball's last glint, the camera still sinking; the rise out of it starts in the dark (6.05 s) so the wall has settled before the rebuild caption | depth, without breaking the rest |
| 6 minor: sound | room tone at about -50 dBFS under the silence; stations +2 dB, pegs -1 dB; +3.5 dB presence at 3.8 kHz; hatch, flight-home and flipper-arming foley | see `docs/review_log.md` round 4 for the numbers |
| 7 minor: ANALIZA not on screen | `deliver/v2/post-caption.txt` carries "Comment ANALIZA" as the post's path; the film keeps the share ask | the brief fixed the share line as the close |
| 8 minor: SRT duplicates the burned-in text | CHANGELOG and PROJECT.md: reference only, do not upload as closed captions | |
| 9 cosmetic: veins curled into loops | veins are now contour lines of a noise stretched along one direction with a slow warp: long, nearly straight, varying in width | |
