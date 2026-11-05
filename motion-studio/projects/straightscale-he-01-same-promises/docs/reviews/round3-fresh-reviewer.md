# Round 3 fresh review: renders/draft-v0-silent.mp4 (G-MOTION-FRAMES, M1 to M7)

Method: frames at every beat, 0.1 s strips at the hook, cascade, stamping, sticker, test and end card, 10 fps motion-energy
curve, crops at full size, phone-size (360 px) contact sheets. Scratch: /tmp/claude-0/-home-user/daf87212-4818-5bd8-a84b-b9fd8e52a5d9/scratchpad/review-he01/.
Formed before reading docs/review_log.md. Silent file not marked down for missing sound.

## Verdict: FAIL (four axes at 7, one blocking defect)

## Scores
| Axis | Score | Evidence behind any score below 8 |
|---|---|---|
| M1 spelling, Hebrew letter by letter | 8 | All words whole, RTL order right, punctuation on the correct (left) side, "8 מתוך 14" reads right. Only doubt is the sticker, see D1. |
| M2 no overlaps or clipping | 7 | 1.1 s "מחיר?" half cut by a reveal mask; 4.0 s source label hidden behind landing slips; 34.0-34.8 s hint line 2 "הראשונה?" cut at a hard mask edge; 24.0 s caption words on different baselines. |
| M3 safe zones and contrast | 8 | Key line starts y~320, captions y 1425-1467 (limit 1520), right edge under 940. Contrast 7:1 (label), 9.8:1 (hint), 14:1 (caption). Source label is only about 40 px type (rule: 44 px), 3.0-10.5 s. |
| M4 text on or just before its word | 8 | Estimated timings, plausible. Not judged beyond that (no voice). |
| M5 motion in first second, hook text by 0.3 s | 9 | "רק" on screen at 0.0 s, slip sliding in at 0.0, stamp lands about 1.1 s. |
| M6 brand colours and fonts only | 8 | Real logo, ivory/charcoal/red, gold only on the sticker. Sticker glyph issue (D1). Stamp is a red slab with a black ball: reads as a button, not a stamp (D4). |
| M7 generated image inside | n/a | None. |
| Hook in first 2 s | 8 | Strong: question, slip, stamp "חינם" on a headline by 1.6 s. Loses a point for D5 and for the stamp reading as a button. |
| Readability at phone size | 7 | Slip headlines in the cascade (4-10 s) are illegible at 360 px, source label small. The stamps, key line, counter and captions read well. |
| Motion quality | 7 | Stamp physics and slips good. Reveal masks clip words (D5); after 18 s the energy is low (see pacing). |
| Continuity | 8 | One desk, one stamp throughout, end card opens from the caret. |
| Pacing | 7 | Energy per second is under 1.1 for 18.5-24.5 s except the tape moment (21 s), for 25.5-30 s, and for 31-34.5 s. Cascade and stamping (6-12.5 s) are strong. Second half is slow for a short-form reel. |
| Composition | 7 | 31.7-36.0 s: top 800 px empty (slip sits low, no key line). End card (37.6-40.3 s): logo and caption centred at x~490, not 540, and lower 40% empty. |
| Brand accuracy | 8 | Logo and palette right. "Meta" appears only as a source label. |
| Message with sound off | 8 | Hook, 8 of 14 count, stamped identical column, price sticker, "המודעה שלכם" test, empty headline with caret all read. |

## Hebrew check
- Whole words, no clipped final letters in held frames. Line breaks fall at phrase points ("תפתחו את / המודעה שלכם.", "המתחרה היה יכול / לכתוב את זה?").
- Punctuation: periods, commas and "?" sit at the left end of the Hebrew line, correct. The quotes around "יועץ משכנתאות" are symmetrical.
- Numbers and mixed text: "8 מתוך 14" (8 on the right), "5.11.2026 · מודעות פעילות", "Meta" inside the RTL line all read in the right order.
- Stumble: the sticker (D1).

## Defects, worst first
| # | Time | What | Why it matters | Smallest fix | Class |
|---|---|---|---|---|---|
| D1 | 14.5-15.2 s (sticker beat, the payoff of "לפי המחיר") | Sticker shows a heavy-serif shekel sign that reads as the Hebrew letters "נם" (ligature look), and the "?" sits to its right, so in RTL it reads "? then shekel" instead of "₪?". | The only price cue in the film; a native reader sees letters, not a currency. | sticker.js: set the shekel in Heebo bold (not Frank Ruhl), put "₪" right of "?" i.e. RTL string "₪?" with dir=rtl, or add a small gap and larger size. | BLOCKING |
| D2 | 14.0-18.0 s, 19-24.5 s, 25.5-30 s, 31-34.5 s | Long low-motion runs; only one event per 2-4 s and several near-still stretches (motion energy under 1.1). | Second half of a 40 s reel can lose a scroller; hook-driven rules ask for a change every 0.5-1.5 s. | Add small events on existing beats: stamp micro-hover drift, slip settle, underline draw cadence; shorten 19-24.5 s. Cuts in timing.json, not new assets. | Polish (pacing 7) |
| D3 | 31.7-36.0 s | Top 40% of the frame is empty (no key line, slip at y 820-1230). | Banned: frame half empty for no reason; weak composition. | layout.js / viewer.js: raise the slip or keep a key line (e.g. the hint) in the top band during this beat. | Polish |
| D4 | whole film | The stamp is a red rounded slab with a black ball; at phone size it reads as a button or game pad, not a rubber stamp. | The signature device must read as a stamp with no caption. | stamp.js: add a handle silhouette (neck + wider grip) and a visible rubber face when it lands. | Polish (recommend) |
| D5 | 1.1 s, 34.0-34.8 s, 24.0 s | Word-rise reveals use a hard mask: "מחיר?" half-cut under "אתכם" at 1.1 s; hint line 2 cut mid-line; caption words on different baselines mid-rise. | Hook word clipped for about 0.15 s; reads as a glitch. | captions.js / band.js / hint.js: clip mask with 12 px bleed or fade in 2 frames; reserve the line height before the rise. | Polish |
| D6 | 3.0-10.5 s | Source label ~40 px, below the 44 px rule; at 4.0 s its second line is covered by landing slips. | House rule; label is the only proof of the number. | source.js: 46 px, move up 20 px or lower the slip band. | Polish |
| D7 | 37.6-40.3 s | End-card block centred at x~490 (caret on the left pulls it), lower 40% empty. | Looks unbalanced on the last frame held. | endcard.js: centre the logo on x=540 and place the caret outside the centring box. | Polish |
| D8 | 25-27.9 s | Stamp covers the "[הכותרת]" line for 3 s, the thing the line asks you to read. | Reads as intended threat but hides the target. | viewer.js: hover the stamp at the right of the slip. | Polish |

Blocking: D1 only. Everything else is polish, but D2, D3 and D4 hold their axes at 7; fix them to reach 8 across the table.
