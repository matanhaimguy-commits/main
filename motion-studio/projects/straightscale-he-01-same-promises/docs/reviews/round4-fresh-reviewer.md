# Round 4 fresh review: renders/draft-v1-silent.mp4 (G-MOTION-FRAMES, M1 to M7)

Method: 33 frames (every beat in the sheet plus mid-beat), 0.1 to 0.5 s strips on the hook, stamping, sticker, tail and end card,
phone-size (480 px sheets) and full-size crops, 10 fps mean-abs-diff motion energy per second. Scratch:
/tmp/claude-0/-home-user/daf87212-4818-5bd8-a84b-b9fd8e52a5d9/scratchpad/review-he01-r4/. Formed before reading round3 report;
docs/review_log.md not read. Silence not marked down.

## Verdict: FAIL (pacing 7; no blocking defect)

## Scores
| Axis | Score | Evidence behind any score below 8 |
|---|---|---|
| M1 spelling, Hebrew whole | 9 | All words whole, RTL right, see Hebrew check |
| M2 no overlaps or clipping | 8 | Pile headlines are cut by frame edge and by each other (4.5-10.5 s); stamp prints overlap headline text by design; end-card wordmark half-masked 36.9-37.5 s |
| M3 safe zones, contrast | 8 | Title y~270-440, captions y~1440 (limit 1520), text right edge <=940; grey fade-in words (2.0, 16.0, 19.0, 35.0 s) are low contrast for ~0.2 s |
| M4 text on or before word | 8 | Estimates only, plausible; not judged further |
| M5 motion in 1st s, hook text by 0.3 s | 9 | "רק" at 0.1 s, slip sliding in, stamp lands about 1.1 s |
| M6 brand colours and fonts | 9 | Real logo, ivory/charcoal/red, gold only on the tag. Only off-palette: dark maroon stamp face at 1.4-1.8 s |
| M7 generated image | n/a | none |
| Hook in first 2 s | 9 | Question builds word by word, stamp slams "חינם" on a real headline by 1.3 s, rest on the flip |
| Readability at phone size | 8 | Titles, captions, count, tag, end card read well. Pile headlines (4.5-12 s) are texture, not readable (about 34 px at scale 0.7) |
| Motion quality | 8 | Stamp fall, squash, tag slap, tape and tally are good. Finger shadow is a flat bar (22.0 s) |
| Continuity | 9 | One desk, one stamp, one slip; card opens from the slip |
| Pacing | 7 | Energy per second (mean diff): 3 s 1.7, 4 s 1.9, 5 s 1.15, 14 s 1.1, 19 s 1.2, 21 s 0.9, then 25-36 s: 2.05, 1.54, 1.62, 2.21, 1.08, 3.59, 1.37, 1.36, 1.77, 1.69, 0.99. About 11 s (25-36) is near-still apart from word-by-word text |
| Composition | 8 | Key line in top band all film; end card centred (logo x 540). Frame 3.0 s has a large empty middle |
| Brand accuracy | 9 | Logo, palette, fonts right. "Meta" only in the source label |
| Message with sound off | 8 | Hook, count 8 of 14, identical stamped column, "?₪" tag, stamp alone, cover-the-name test, caret all read. The finger beat is the weakest read |

## Hebrew check
- Whole words everywhere. No clipped final letters in held frames; the stamp prints "חינם", "ללא עלות", "לחסוך" read correctly.
- RTL: titles right-start and build leftward; "8 מתוך 14" correct (8 right); "5.11.2026 · מודעות פעילות" correct; "Meta" inside RTL line fine.
- Punctuation: ".", ",", "?" sit at the left end of each phrase. Quotes in חיפשתי "יועץ משכנתאות" are symmetrical.
- Tag "₪?": a proper shekel glyph at the right, "?" left, reads as "₪?" in RTL. OK.
- Line breaks fall at phrase points (רק שואלים / אתכם מחיר?; תפתחו את / המודעה שלכם; למשל, מה קורה אצלכם / בפגישה הראשונה?). Second lines are centred under the first instead of right-aligned (26.5 s "לכתוב", 33.5 s "בפגישה"): a native reader sees ragged RTL.
- Stumble: the mirrored "חינם" on the stamp face (1.4-1.8 s) reads as nonsense letters; deliberate, brief.

## What each object reads as at phone size
- Stamp (red slab, wooden knob, 1.0 s on): reads as a rubber stamp. Yes.
- Red print "חינם" with double border: yes, a stamp print.
- Stack of identical prints (13.5 s): yes, a column of red.
- Price tag (14.7 s): yes, gold hang tag with hole and "?₪".
- Blank slip "המודעה שלכם" with brackets: yes, a form to fill.
- Finger shadow (21.0-22.0 s): reads as a dark pen or ruler bar, not a finger. Takes over half a second. Weak.
- Tape (22.0 s on): reads as masking tape. Yes. But the name stays faintly legible through it for the rest of the film, so "covered" is half true.
- Underline (23.5 s on): yes, a rule under the headline.
- Caret (30-36 s): a thin vertical bar beside the rule; reads as a text cursor to most, fine.
- End card (38-40 s): charcoal, logo, "שמרו · שלחו לחבר עם עסק", blinking caret: yes.

## Defects, worst first
| # | Time | What | Why it matters | Smallest fix | Class |
|---|---|---|---|---|---|
| N1 | 25-36 s (and 3-5.5 s, 19-23 s) | Energy 1-2 for about 11 s in the tail, 1.2-1.9 at 3-5.5 s; only words change | Pacing 7: second half is the longest run without a big change; rule is 0.5-1.5 s | timing.json / viewer.js: one visible event per 1.5 s in 25-36 s (second stamp dip, slip nudge and settle, camera drift change at each spoken phrase); cut 1 to 2 s from 28-34 s | Not blocking, but holds pacing at 7 |
| N2 | 21.0-22.5 s | Finger shadow is a flat rounded bar | The instruction "cover with your finger" does not read in half a second | cover.js: taper the tip, add a nail-end and a knuckle step, darker contact edge | Polish |
| N3 | 23.5-36 s | Tape is translucent: "[שם העסק]" remains legible | Undercuts the "covered" idea | cover.js: raise tape alpha so text is under 20% | Polish |
| N4 | 36.9-37.5 s | Wordmark is half cut by the card-open mask (frame at 37.4 s) | A clipped logo for ~0.3 s | endcard.js: start the logo rise after the mask has passed its top edge, or mask the card not the logo | Polish |
| N5 | 1.4-1.8 s | Stamp face is dark maroon with mirrored "חינם" | Off-palette block and gibberish letters for the hook rest | stamp-body.js: face in #BE0F18 on lighter rubber, mirrored word at lower contrast | Polish |
| N6 | 4.5-12 s | Pile headlines cut by the right and left frame edge, under 44 px | Fine as texture; breaks the 44 px rule literally | accept, or content.js: keep 3 slips entirely inside the frame | Polish |
| N7 | 26.5, 33.5 s | Two-line titles are centre-aligned, not right-aligned | Ragged RTL | band.js: text-align right for wrapped lines | Polish |
| N8 | 2.0, 16.0, 19.0, 35.0 s | New word fades in from light grey | Low contrast for ~0.2 s | captions.js / band.js: start at 60% charcoal | Polish |
| N9 | 3.0 s | Large empty middle band after the hook | Composition dip | desk.js: land the first cascade slips earlier | Polish |

No blocking defect. To reach 8 on every axis: fix N1 (and N9 helps).

## Round 3 defects D1 to D8
| # | Verdict | Evidence |
|---|---|---|
| D1 sticker glyph | Fixed | 14.7 s: clean shekel sign at right, "?" left; reads "₪?" |
| D2 long low-motion runs | Partly fixed | 14-24 s improved (15 s 8.3, 17-18 s about 5, 24 s 7.1) but 25-36 s still 1-2, 3-5.5 s still 1.2-1.9 |
| D3 empty top 40% at 31.7-36 s | Fixed | Key line "למשל, מה קורה אצלכם בפגישה הראשונה?" in top band, slip raised |
| D4 stamp reads as a button | Fixed | Wooden knob handle, bevelled edge, and the turn-over shows a rubber face |
| D5 hard-mask clipping of words | Fixed | "מחיר?" at 1.0 s fades in (grey) with no cut; "בפגישה" and "הראשונה?" fade in whole |
| D6 source label size / covered | Fixed | Label about 46 px and not hidden by landing slips (4.5, 6.0 s) |
| D7 end card off-centre | Fixed | Logo spans x 105-376 of 480 (centre 240, equals 540 px); text centred |
| D8 stamp covers "[הכותרת]" | Fixed | 25-28 s the stamp sits left of the slip; "[הכותרת]" fully visible |

Remaining: N1 (pacing) is the one axis under 8.
