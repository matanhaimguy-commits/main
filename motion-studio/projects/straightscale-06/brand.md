# Brand system: StraightScale (film 06)

Taken from the client's own material, never invented: `clients/straightscale/brand-kit.md` (facts, voice, colours,
type), `motion-studio/projects/straightscale-03/brand.md` (logo files and measured colours).

## Sources
- Logo: `film/assets/brand/wordmark-white.png` (640x213, white wordmark, for dark grounds), `logo-full.png` (black
  wordmark), `symbol.png`: the owner's files (Google Drive, 5 Oct 2026). Gold square inside wordmark-white.png
  measured at x 108-136, y 48-76 (29 px), colour about #E6A505; red symbol about #C8121B.
- Fonts: `film/assets/fonts/` (Playfair Display, Montserrat; OFL), copied from straightscale-03.

## Colour (roles in this film)
| Token | Hex | Role | Source |
|---|---|---|---|
| charcoal | #1F1F1F | ground (with seeded grain and a soft vignette) | brand kit |
| ivory | #F8F6EF | headline, clock, body, message bubbles | brand kit |
| grey | #9B958D | note, open-hour flats, axis and day labels | derived, not a new colour: brand-kit marble #EDE4D6 at 60 % over charcoal #1F1F1F = (155, 149, 141). Computed in the page as `C.grey = mixHex(C.marble, C.char, 0.6)`. Proposed for the brand kit as the secondary-text tint (the kit is not edited from a film project) |
| mark-gold | #DD9A10 | the one accent: "closed", the climbs, CLOSED, answers, ANALIZA, the tip square | brand kit / symbol.png |
| mark-red | #BE0F18 | only inside the real logo | brand kit |
Contrast rules kept: no gold text on ivory; no red text on charcoal. All sampled text checks pass WCAG AA
(HyperFrames check: 111/111 in v1, 98/98 in v2 after the axis labels were thinned). Grey on charcoal is 5.5:1.

## Type system (1080x1920; 4:5 values in brackets)
| Role | Family / weight | Size px | Line height |
|---|---|---|---|
| headline, system line | Playfair Display 700 (closed: 700 italic, gold) | 80 [72] | 88 [78] |
| note | Montserrat 500, grey | 44 [42] | 54 [50] |
| math lines, list | Montserrat 700 | 50-52 [48-50] | 62-64 [58-60] |
| payoff "Closed 108." (v2) | Montserrat 700, "108" 800 tabular, gold | 80 [76] | own line, +8 px |
| clock | Montserrat 800 tabular | 116 [104] | 1.0 |
| chip | Montserrat 800 caps +14 % | 38 [36] | |
| riding value | Montserrat 800 tabular, gold | 56 | |
| Comment / ANALIZA. | Playfair 700 italic / Montserrat 800 gold | 100 / 124 [96 / 120] | |
| CTA body | Montserrat 600 | 50 [48] | 66 [62] |
| axis / day labels | Montserrat 700 / 700 (v2: axis labels only at 0, 40, 80, 120) | 34 / 27 (v1: 30 px 600, every 20) | |

## Layout
- 9:16 safe zone: no text or logo in the top 14 % (269 px), the bottom 20 % (384 px) or the right 140 px. Left margin
  96 px. Checked every 0.05 s by `tools/textcheck.mjs`.
- 4:5: 60 px margin all round (feed, no overlay), left margin 80 px.

## Voice and tone
Calm, direct, practical; short lines; English for this batch. No prices, results, clients, reviews, guarantees,
deadlines, "within 1 hour", "we chase your leads", hype words or em dashes.

## Do / don't
- Do: one accent; real logo only, revealed by a mask; numbers only from the stated example and its arithmetic.
- Don't: redraw the mark, add glow, put counts or names on the message bubbles.
