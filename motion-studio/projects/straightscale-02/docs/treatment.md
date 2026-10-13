# Treatment: StraightScale · Reel 02 "Klientët që kthehen"

## 1. Reference measurements
Measured with `motion-studio/tools/pacing.py` (full output in `docs/refs/pacing.txt`); studied as grammar only.

| Reference | What it is | Numbers | Take | Leave |
|---|---|---|---|---|
| onetake "one dot" (15 s) | one element transforms through every beat and lands as the brand's mark | 9% still, quiet run 2.0 s, 1 hard transition, beat CV 0.74, spread 7.6x | one survivor element; a long calm hold before the end; tiny elements in a lot of empty space | its purple palette, its UI content, 16:9 |
| onetake "clearing" (15 s) | a dive through scale: a year of cells zooms into one day and back out; the cells finally spell the name | 21% still, 2 transitions, beat CV 0.61, spread 8.7x | one saturated world colour plus one accent; the meaning is built into the artwork; the pull-back reveal | the blue, the calendar content |
| onetake "knockon" (15 s) | a chain reaction where every beat is caused by the last | 3% still, 0 transitions, CV 0.68 | visible cause for every reaction; no cuts | its tabletop props |
| our reel 01 (50 s) | kinetic type on charcoal and marble | 21% still, 3 transitions, CV 0.83 | voice as master clock, ducked music, CTA flow | its card-and-headline layout, its ivory/charcoal split (don't repeat) |

## 2. Three concepts

| | A · The S path | B · The phone book | C · Orbits |
|---|---|---|---|
| Idea | The S channel in StraightScale's own symbol is the client's path through a business. A gold token (a client) runs it. Problem: it exits and is gone, so the business pours in new ones every month. Fix: the exit curves back around to the entrance, the client returns, leaves a star, and brings a second token. Pull back: it was the logo all along | A long list of past clients in the owner's phone, all grey "last visit 7 months ago"; recall messages go out at the right time and the list lights up into bookings | Clients as satellites that orbit the business on their service's interval (6 months, 4 weeks); without the system they drift off into space; with it they return on time |
| Hook (0-2 s) | Macro inside the dark channel between red walls: a gold token races past and out of frame, "Çdo muaj fillon nga zero?" | Thumb scrolling an endless grey list | Planets flying away into black |
| Survivor at every transition | the gold token and the channel | the list | the orbit lines |
| Message in the picture | a path that leaks vs a path that loops | grey vs lit names | drifting vs returning |
| Style / engine | HyperFrames (SVG/DOM + GSAP), the real symbol PNG for the reveal | HyperFrames | HyperFrames or canvas |
| Risk | the path must sit exactly on the real mark (verified: traced centreline, `assets/brand/s_path.json`) | needs invented names (banned) and imitates WhatsApp's UI | generic space look, not ownable |

**Chosen: A.** It is built from the brand's own mark, so no other business could run it. It has one survivor element (the gold
token) and one world colour (the mark's red) with one accent (its gold). It ends on a reveal that is also the logo.
B breaks the no-invented-names rule. C is generic.

## 3. Art direction
- **Design read:** premium and calm, built from the logo, like a brand film rather than an ad. Few elements, big
  type, a lot of colour field.
- **World:** the S channel at macro scale. The channel is the dark ground (charcoal #1F1F1F with faint grain);
  the walls are the mark's red #BE0F18 with a subtle inner shadow so the channel reads as a cut; the client is a
  gold disc #DD9A10. The gold square of the mark is the business's "door" (where clients enter).
- **Palette by role:** red = the business (walls); charcoal = the path; gold = the client and every win; ivory
  text on charcoal or on red. No red text on charcoal; no gold text on ivory.
- **Type in motion:** Playfair Display 900 / italic 700 for the spoken key lines, entering by masked rise or
  riding the path; Montserrat 800 caps labels. Words land on the voice; one line on screen at a time.
- **Camera:** the camera follows the gold token along the channel (leading slightly, settling on turns); one
  pull-back at the end reveals the whole symbol; one push-in at the start.
- **Signature device:** the gold token on the S path (present in every shot).
- **Transitions:** no cuts; every beat continues the same camera move along the path.
- **Texture:** fine grain on charcoal; soft inner shadow on walls; gold token with a hard highlight (no glow).
- **Sound world:** a calm pulse with a marimba/pluck motif; the token has a soft wooden tick when it turns;
  a warm chord when the loop closes; silence before the reveal.
- **Banned here:** confetti, particles, glow, generic phone UI, invented names or numbers, cards on a flat background.

## 4. Script (v1, 88 words ≈ 37 s at 2.4 words/s, plus a 2.5 s music pause for the proof)
| # | Voice (Albanian, "ti") | English check | On screen |
|---|---|---|---|
| 1 | Çdo muaj fillon nga zero? | Every month, you start from zero? | Tokens enter, run the S, exit and vanish |
| 2 | Paguan reklama për klientë të rinj, | You pay for ads to get new clients, | new token drops in at the door |
| 3 | ndërsa ata që erdhën një herë nuk kthehen më. | while the ones who came once never come back. | the token leaves the exit and is gone |
| 4 | Por klienti më i lehtë është ai që të njeh tashmë. | But the easiest client is the one who already knows you. | the camera follows one token back |
| 5 | Çdo shërbim ka kohën e vet të kthimit. | Every service has its own time to come back. | "KOHA E KTHIMIT" |
| 6 | Te dentisti, gjashtë muaj. Te parukieri, disa javë. | At the dentist, six months. At the hairdresser, a few weeks. | chips: Dentist · 6 muaj / Flokë · 4-6 javë / Fytyrë · 4 javë |
| 7 | Dërgoji mesazh pak para asaj kohe. | Send them a message just before that time. | message: "Kanë kaluar 6 muaj nga kontrolli i fundit. T'ju ruaj një orar?" |
| 8 | Kërkoji një vlerësim kur është më i kënaqur. | Ask for a review when they're happiest. | a gold star lands on the token |
| 9 | Dhe jepi një arsye të sjellë një mik. | And give them a reason to bring a friend. | a second token joins |
| 10 | Kështu klienti kthehet. Dhe nuk vjen vetëm. | That way the client comes back. And doesn't come alone. | the exit loops back to the door; two tokens return |
| 11 | Këtë sistem e ndërtojmë ne te StraightScale. | We build this system at StraightScale. | pull-back: the path is the StraightScale symbol |
| - | (music only, 2.5 s) | | "Ekipi ynë rriti:" three growth figures from the brief |
| 12 | Analizë falas, dyzet e pesë minuta, pa detyrim. | Free analysis, 45 minutes, no obligation. | offer |
| 13 | Shkruaj ANALIZA në komente. | Comment ANALIZA. | comment field, logo lockup |

Alt hook B: "Klientin e ri e paguan. Të vjetrin e harron." (You pay for the new client. You forget the old one.)
Facts: the intervals (dental check-up 6 months, hair roots 4-6 weeks, facials 4 weeks) and the recall message come from
the user's "PHASE 2.5" offer document; the proof figures from the brief. No names, prices, invented numbers or
"we chase your leads". Native-speaker check still needed.

## 5. Beat sheet
Clock: `audio/vo.wav` (take 4 with 3.0 s of silence inserted at 30.86 s for the proof), word times in
`audio/words.json`. World units = pixels of `symbol.png`; S = camera scale (screen px per world unit).
Engine: the motion-studio canvas engine, not HyperFrames: the film is one continuous camera ride along the S at
up to ~2,600 px/s on screen, which needs real subframe motion blur (`render.mjs`, 60 fps, 4 subframes). The
mark is drawn from `assets/brand/symbol-trace.svg` (traced from the real PNG, IoU 0.999) while zoomed in, and
hands over to the real `symbol.png` / `wordmark-white.png` once the camera is at native size or smaller.

| Time (s) | Beat | Voice | On screen | Moving | Still | Link to next | Audio |
|---|---|---|---|---|---|---|---|
| 0.00-1.95 | 1 Hook | Çdo muaj fillon nga zero? | "Çdo muaj / fillon nga *zero?*" on the red top bar | camera inside the top band, S 3.4, drifting; 3 tokens race through right to left and leave; band empty on "zero" | the walls | the stream of tokens | pulse starts; whoosh per token |
| 1.95-4.18 | 2 Pay for new | Paguan reklama për klientë të rinj, | "Paguan reklama / për klientë të rinj" | camera glides right to the door (gold block, entrance slit); 3 new tokens enter through the slit, 0.5 s apart | gold block | the last token entering becomes the rider | soft tick per entry |
| 4.18-7.08 | 3 The leak | ndërsa ata që erdhën një herë nuk kthehen më. | lead "ata që erdhën një herë" + payoff "nuk kthehen më." | the ride: camera locks on the rider through the whole S (2,263 units in 2.2 s, S 3.0→2.3→2.6), out of the exit slit; the token drifts into the dark and greys out | nothing | the grey token in the dark | rising whoosh, then the music thins |
| 7.08-10.28 | 4 Turn (rest) | Por klienti më i lehtë është ai që të njeh tashmë. | "Klienti më i lehtë / është ai që të njeh." | camera settles beside the mark (S 2.4); slow drift only: the planned rest | the grey token | the token | music drops to pad |
| 10.28-12.92 | 5 Return time | Çdo shërbim ka kohën e vet të kthimit. | label KOHA E KTHIMIT; a dial ring draws around the token | ring and 12 ticks draw on; camera pushes in | token | the dial | tick on ring close |
| 12.92-17.08 | 6 Intervals | Te dentisti, gjashtë muaj. Te parukieri, disa javë. | "Te dentisti · 6 muaj" then "Te parukieri · 4-6 javë" | the arc sweeps to just before full, unwinds, sweeps again faster | token | arc stops just short | clock ticks under the sweep |
| 17.08-19.56 | 7 Recall | Dërgoji mesazh pak para asaj kohe. | "Dërgoji mesazh / pak para asaj kohe." + message card (from the offer doc) | a gold thread runs from the mark to the token; the card unfolds; on arrival the token turns gold again | arc | the token is live again | message tick, token "on" note |
| 19.56-22.20 | 8 Review | Kërkoji një vlerësim kur është më i kënaqur. | "Kërkoji një vlerësim / kur është më i kënaqur." | a gold star draws above the token and lands on it | token | star stamped on the token | bright pluck on landing |
| 22.20-24.50 | 9 Referral | Dhe jepi një arsye të sjellë një mik. | "Jepi një arsye / të sjellë një mik." | a second token rolls in from the dark and docks beside the first | the pair | the pair | second voice of the motif |
| 24.50-27.88 | 10 The loop | Kështu klienti kthehet. Dhe nuk vjen vetëm. | "Kështu klienti kthehet." then "Dhe nuk vjen vetëm." | the pair draws a gold return line around the outside of the mark and re-enters the door; camera pulls back S 2.6→0.94 | | the loop closes at the door | warm chord when the loop closes |
| 27.88-30.90 | 11 Reveal | Këtë sistem e ndërtojmë ne te StraightScale. | the traced mark hands over to the real symbol; it slides into the white lockup on "StraightScale" | tokens circulate the S and the loop; symbol shrinks into the lockup, wordmark wipes in | | the lockup | resolve; air before the proof |
| 30.90-33.95 | 12 Proof (music only) | (3.0 s pause) | "EKIPI YNË RRITI:" + 3 rows (€15K → €55K/muaj; €30K → €100K/muaj; €0 → €140K/muaj) with gold token bullets | rows rise one by one, arrows draw | lockup | rows rise out | music forward, three plucks |
| 33.95-37.50 | 13 Offer | Analizë falas, dyzet e pesë minuta, pa detyrim. | "Analizë falas" / "45 minuta" / "Pa detyrim. Në Tiranë ose te biznesi yt." | lines rise on the words | lockup | | music ducked |
| 37.50-41.00 | 14 CTA + end | Shkruaj ANALIZA në komente. | "Shkruaj" / ANALIZA typed into a gold-outlined field / "në komente." | a token presses the field; hold on the lockup | lockup | end | final chord, clean tail |

Self-checks: 14 beats from 1.9 s to 4.2 s plus the 3.0 s proof (CV 0.27, longest/shortest 2.2x across voiced
beats, but motion density varies far more: the 2.2 s ride vs the 3.2 s rest). Rest after the hook: beat 4.
Survivor at every link: the gold token (and the mark). Every reaction has a cause: the message turns the token
gold, the token draws the return line, the loop closing brings the chord. Nothing important frozen > 4 s.
Sound off: tokens leaking out vs looping back reads without the voice.
