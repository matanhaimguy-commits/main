# Treatment: StraightScale · Reel 03 "Qartësia"

## 1. Reference: divyansh.fx_ "Faceless video edit" (Instagram reel Da0DayIpsie, 26.4 s, 720x1280)
Frames every 0.5 s (`docs/refs/ref_contact.png`, 48 frames) and 16 detail frames (`docs/refs/detail_sheet.png`).
Transcript (Instagram): "Attention is expensive because every second your audience spends trying to understand
your message is a second of losing prospects, losing momentum, and losing opportunities. The brands leading the
market aren't louder. They're clearer, sharper, more intentional. They remove friction. They accelerate
understanding. They make decisions feel effortless because clarity isn't an advantage. It's leverage."

| Time | Beat | Picture | Device |
|---|---|---|---|
| 0.0-1.4 | Attention / is expensive | one word blurs into focus centre; "expensive" in green with tiny $ glyphs; soft green bokeh | focus pull, accent word |
| 1.5-3.0 | Because every second | a huge stopwatch hand sweeps across a dial edge, motion-blurred; "every second" in green serif italic; fine print under the line | prop in extreme close-up |
| 3.0-4.4 | your audience spends | a row of person pictograms, the centre one black inside camera focus brackets | focus brackets |
| 4.5-6.3 | trying to understand | the line with big outlined "???" behind, blurred floating cards | blur, layered depth |
| 6.5-7.0 | is a second | a countdown ring with a big number | timer ring |
| 7.5-11.0 | losing prospects / momentum / opportunities | green hexagons with line icons pop in one by one, joined by callout lines with small labels | node diagram |
| 11.5-13.5 | brands / the / market. / Aren't louder. | one word at a time, centred, green; the payoff in black serif italic | word-by-word |
| 14-21 | clearer, sharper, more intentional... | pills stack up (filled green / outlined), a growing tag cloud | pills |
| 21.5-23.7 | clarity isn't an advantage. It's leverage. | the line types on, slides left, "It's leverage." gets a hand-drawn green ellipse | typewriter, circle |
| 24-26.4 | sting | the creator's mark and handle | logo sting |

Grammar to take: white field, one saturated accent, black neutral grotesk plus a serif italic for the accent words,
very small fine print as texture, a new prop every 1-2 s, focus pulls and motion blur as transitions, soft
out-of-focus accent circles drifting in depth, centred compositions with lots of air.
Leave: the green, the English text, the pictogram style of people, the fake review cards, the creator's mark.
Pace: about 20 beats in 24 s (a new picture every ~1.2 s), beat CV 0.70 (measured on the 2 fps frame proxy).

## 2. Concept
The user asked for this concept, so the three-concept round is a choice of treatment, not of idea:
- **A (chosen) · Same grammar, our brand.** Ivory field, crimson accent, Montserrat + Playfair italic (the brand
  pair maps exactly onto the reference's grotesk + serif italic), the same prop sequence rebuilt in code, one
  added fact beat (1.800 ads saying "cilësi"), real StraightScale lockup as the sting.
- B · Charcoal inversion (dark field, gold/ivory type): reads closer to reels 01-02, further from the reference.
- C · Reference script over the reel-02 S-path world: mixes two languages of motion; rejected.

## 3. Art direction
- Field: ivory #F8F6EF with marble #EDE4D6 out-of-focus discs and crimson rings drifting slowly in depth
  (blurred, 4-12% opacity). One accent: crimson #B31217 (text and fills on ivory); charcoal #1F1F1F for type;
  gold only as small filled marks (never gold text on ivory).
- Type: Montserrat 600/700 (the grotesk), Playfair Display 700 italic for accent words; fine print in Montserrat
  500 at 26-30 px as texture only (never carrying meaning; everything that matters is 44 px or more).
- Devices: focus pulls (blur radius as a spring), motion blur from the renderer, stopwatch hand, focus brackets,
  countdown ring, hexagon nodes with callout lines, word-by-word centre words, pills, typewriter + hand-drawn
  ellipse, logo sting.
- Signature device: the crimson focus ring/bracket that "finds" the important thing in every beat.
- Banned: confetti, glow, fake UI cards or reviews, generic avatars, invented numbers, green.
- Sound: a clean ticking pulse (the stopwatch) under a muted piano/marimba bed, soft whooshes on focus pulls,
  small clicks on pills and typing, a resolved chord on "strategji", a sting on the logo.

## 4. Script (v1)
| # | Voice (Albanian, "ti") | English check | On screen |
|---|---|---|---|
| 1 | Vëmendja kushton. | Attention costs. | "Vëmendja" focus-pull, "kushton" crimson with € marks |
| 2 | Sepse çdo sekondë | Because every second | stopwatch hand sweeping, "çdo sekondë" italic crimson |
| 3 | që klienti yt harxhon | that your client spends | five figures, one in focus brackets |
| 4 | duke u munduar të kuptojë çfarë ofron, | trying to understand what you offer, | line with outlined "? ? ?" behind, blurred |
| 5 | është një sekondë | is a second | countdown ring |
| 6 | ku humbet klientë, humbet ritëm, dhe humbet mundësi. | in which you lose clients, momentum and opportunities. | three crimson hexagons with icons and callouts |
| 7 | Rreth një mijë e tetëqind reklama aktive thonë "cilësi". | About 1,800 active ads say "quality". | the word "cilësi" multiplying into noise, "1.800" and the source line |
| 8 | Bizneset që fitojnë nuk janë më të zhurmshme. | The businesses that win aren't louder. | word by word; "më të zhurmshme" serif italic |
| 9 | Flasin më qartë. Më saktë. Me qëllim. | They speak more clearly. More precisely. With purpose. | pills, filled and outlined |
| 10 | Heqin pengesat. Shpejtojnë vendimin. E bëjnë zgjedhjen të lehtë. | They remove obstacles. They speed up the decision. They make the choice easy. | more pills |
| 11 | Sepse qartësia nuk është stoli. Është strategji. | Because clarity isn't decoration. It's strategy. | typewriter; "Është strategji." circled |
| 12 | Analizë falas, dyzet e pesë minuta. Shkruaj ANALIZA në komente. | Free analysis, 45 minutes. Comment ANALIZA. | offer and comment field |
| 13 | (music) | | StraightScale lockup sting |

Alt hook: "Sa sekonda të jep klienti para se të largohet?" (How many seconds does a client give you before
leaving?) Facts: 1.800 ads (brief: Meta Ad Library, 11 Oct 2026), 45 minutes (offer). Native check needed.

## 5. Beat sheet
Clock: `audio/vo.wav` (take 1, 34.56 s), word times in `audio/words.json`; the page reads them (`audio/words.js`), so
every cue is tied to a spoken word, not retyped. Film length 37.0 s (voice + 2.4 s logo sting).
Engine: motion-studio canvas engine (focus pulls with canvas blur, a fast stopwatch hand and sliding pills need
real subframe motion blur). Signature device: crimson focus brackets that find what matters in each beat.

| Time (s) | Beat | Voice | On screen | Moving | Still | Link | Audio |
|---|---|---|---|---|---|---|---|
| 0.00-1.55 | 1 Hook | Vëmendja kushton. | "Vëmendja" focus-pulls in, brackets snap on it; "kushton." crimson italic, € marks drift up | focus pull, brackets | bokeh | brackets carry over | soft rise, bracket click |
| 1.60-2.72 | 2 Stopwatch | Sepse çdo sekondë | giant hand sweeps a crimson dial edge; "Sepse / çdo sekondë" | hand (blur) | dial | the sweep lands on the figures | clock ticks |
| 2.76-3.92 | 3 Your client | që klienti yt harxhon | five figures, brackets lock on the centre one | brackets | figures | centre figure | click |
| 4.00-6.08 | 4 Confusion | duke u munduar të kuptojë çfarë ofron, | the line over three outlined "?" and drifting blurred buzzwords | ?, buzzwords | line | blur out | airy whoosh |
| 6.32-7.16 | 5 One second | është një sekondë | a ring closes in exactly the spoken time around "1" / "sekondë" | ring | number | ring becomes the first hexagon | tick, ding |
| 7.20-11.04 | 6 Losses | ku humbet klientë, humbet ritëm, dhe humbet mundësi. | three crimson hexagons with icons pop on each "humbet", callout labels | pops, lines | | | three low pops |
| 11.36-15.12 | 7 Noise | Rreth 1.800 reklama aktive thonë "cilësi". | "1.800" with source; the word "cilësi" multiplies into a grey crowd | crowd fills | number | crowd blurs away | murmur of ticks |
| 15.20-17.88 | 8 Not louder | Bizneset që fitojnë nuk janë më të zhurmshme. | one phrase at a time, the crowd gone; italic payoff | focus pulls | | | silence then thump |
| 18.08-25.64 | 9-10 Pills | Flasin më qartë... E bëjnë zgjedhjen të lehtë. | six pills stack into a cloud, filled and outlined | pills slide in | cloud | pills blur out | six soft pops |
| 25.84-29.36 | 11 Payoff | Sepse qartësia nuk është stoli. Është strategji. | line types on, rises and greys; "Është strategji." circled by hand | typing, ellipse | | | keys, marker swish, chord |
| 29.68-34.64 | 12 CTA | Analizë falas, dyzet e pesë minuta. Shkruaj ANALIZA në komente. | offer, a 3/4 ring for 45 minutes, comment field typed | ring, typing | | | keys |
| 34.70-37.00 | 13 Sting | (music) | real StraightScale logo, brackets snap on it | brackets | logo | end | sting, clean tail |

Self-checks: 13 beats from 0.84 s to 7.6 s (CV well over 0.25); rest after the hook is the 0.4 s held stopwatch
plus the held pills cloud; the brackets survive across beats; every pop is caused by a spoken word; nothing
frozen over 4 s; sound off: costs → losses → noise → clarity → offer reads from the type alone.
