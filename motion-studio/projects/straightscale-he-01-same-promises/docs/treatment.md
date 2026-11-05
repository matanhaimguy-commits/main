# Treatment: StraightScale (Hebrew) · 01 "What everyone promises"

Written before any scene code. Each section answers a question a director would be asked.

## 1. Reference measurements
References from the bank (`refbank.py pick --client straightscale-he`, 5 Nov; client has no films logged yet):
- **onetake-one-dot** (ui-saas; morph, one-take camera, typing caret). Take: one element carries the whole film in a
  single continuous shot, nothing is cut away. Leave: the dark SaaS look and the abstract dot. Study only (PolyForm NC).
- **tt-foil-finance** (data-infographic, 1.5M; counter-ticker). Take: a number that ticks up on screen while the
  voice keeps talking, so the count is the proof. Leave: the photo background and the finance topic.
- **Pattern bank (vault, research/2)**: a live audit of real ads in one field is a format that wins abroad and no
  Israeli creator in this niche uses yet; Israeli short-form hooks run 7 to 10 words, plural, concrete.
Clips are not in the container (the bank holds measured cards); pacing targets come from the cards: something big
changes every 0.5 to 1.5 s inside a continuous shot, rests are short freezes on a payoff.

## 2. Three concepts (different central visual ideas, not three versions of one)

| | Concept A: "The stamp" | Concept B: "The highlighter" | Concept C: "One caret" |
|---|---|---|---|
| Idea | Top-down desk. Paper slips, each with one real mortgage-adviser ad headline typed on it, drop onto the desk. One red rubber stamp comes down on slip after slip and prints the same word: חינם, ללא עלות, לחסוך. The pile becomes a stack of stamped, identical papers. A gold price sticker is the only thing left that differs. The viewer's own slip lands blank; the stamp hovers over it and lifts away. | The same headlines stacked as lines of text. A highlighter sweeps the repeated words on every line; the highlighted words lift off and fall into one pile, leaving the lines nearly empty except a price. | A single text caret types the search, becomes the results list, becomes a magnifier over the repeated words, becomes a price tag, and ends blinking in the viewer's own empty headline. |
| Hook (0-2 s) | The first slip drops, the stamp slams down: "חינם" in red ink. On screen: the hook line. | A highlighter stroke across a real headline. | A caret types "יועץ משכנתאות". |
| Signature device | The stamp (literal metaphor for "everyone uses the same stamp"), present in every beat. | Highlight sweep. | Morphing caret. |
| Survives each transition | The stamp and the ink. | The highlighted words. | The caret. |
| Message physically in the picture | Sameness is literally one stamp printing the same promise on everyone's paper. | Sameness is a pile of the same words. | Weaker: the caret is a carrier, not the message. |
| Style / engine | HyperFrames, 2D paper world, springs, shadows, ink texture in code. $0. | HyperFrames type. $0. | HyperFrames UI. $0. |
| Risk | Must not look like "cards on a flat background": the desk, shadows, ink and stamp physics carry it. | Close to plain kinetic type, the look the market already sees. | Needs a search screen, which pulls toward imitating Meta's UI (banned). |

Recommendation and why: **Concept A.** It is the only one where the point (everyone is using the same stamp) is in the
picture itself and reads with the sound off, it has a physical sound (the thunk) that marks every beat, and it never
imitates Meta's interface: the headlines are real text on our own paper. `refbank.py check --client straightscale-he
--category explainer-2d --devices literal-metaphor,top-down-plan,rigid-body-drop,counter-ticker,asmr-foley,voiceover-explainer`:
ok (5 Nov).

## 3. Art direction (chosen concept)
- Design read: calm, exact, a strategist's desk; tactile paper and ink, not a screen. Premium and quiet, so the one
  red stamp is loud.
- Palette by role (brand kit): desk marble #EDE4D6; paper ivory #F8F6EF with a faint grain; type charcoal #1F1F1F;
  stamp ink and accent mark-red #BE0F18 (the one accent); gold #DD9A10 only on the price sticker (never gold text on
  ivory: the sticker carries charcoal text on gold); end card on charcoal with the white wordmark.
- Type: Hebrew needs Hebrew glyphs, which Playfair and Montserrat lack. Display: Frank Ruhl Libre (a high-contrast
  serif in Playfair's spirit) for the stamp words and the key lines; UI: Heebo (clean sans, Montserrat's role) for
  the headlines on the slips and the captions. Both self-hosted from npm @fontsource. RTL throughout.
- Type in motion: headlines are already typed on the slips when they land (no typing animation); the stamp word
  appears only as ink on impact; key spoken lines appear as one line at the top third, word by word on the voice,
  and leave by being covered (a slip slides over), never by fading.
- Layout: top-down camera on the desk, slips in the middle band (y 500 to 1400), key line in the top band below the
  250 px safe zone, captions above the bottom 400 px. One focal point per beat: the slip being stamped.
- Signature device: the red stamp, in every beat, including the end (it hovers over the blank slip and lifts away).
- Motion: springs only (lib/motion.js values); slips drop with a short bounce and a settle rotation of 1 to 4 deg
  and a growing soft shadow; the stamp falls fast, 2-frame squash, a 3-frame desk shake, ink spreads in 80 ms; the
  camera is one continuous top-down shot with slow pans and one push-in on the blank slip. Something big changes every
  0.6 to 1.5 s; rests are freezes on the stamp hits that matter.
- Texture: paper grain and fibre noise (seeded), ink with uneven coverage and edge bleed, desk with faint marble veins.
- Sound: stamp thunks (one per hit, varied), paper slides and drops, a marker squeak on the tally, a calm low score
  under the voice; silence before the last line.
- Banned for this piece: any recreation of Meta's or Facebook's interface; advertiser names, logos or screenshots;
  the words "all", "everyone" or "every" about the advertisers; prices; anyone's results.

## 4. Script
The final Hebrew script with its on-screen column is `docs/script.md` section 2 (12 lines, 91 words, about 38 s at
2.4 words/s). Not approved yet (Matan's read-aloud, gate 5e). The film reads its lines and words from
`film/timing.json`; the key words on screen and the 14 headlines are in `film/src/content.js`.

## 5. Beat sheet (scratch timing: script seconds, words spread by length; no voice yet)
Every time below is a cue in `film/timing.json` anchored to a spoken word, so the real voice moves the whole sheet.

| Time | Beat | Voice | On screen | Moving | Still | Link to next (what survives) | Audio (planned) |
|---|---|---|---|---|---|---|---|
| 0.0 | Hook toss | רק שואלים אתכם מחיר? | key line word by word; slip 1 tossed in | slip lands with a bounce, shadow grows | desk | slip 1 | paper slap |
| 1.1 | Hook hit | (on "מחיר?") | stamp falls, prints חינם | gravity fall, 2-frame squash, 3-frame shake | key line | the print | stamp thunk |
| 1.3 to 2.0 | Rest + face | | stamped slip; the stamp turns over above it and shows its rubber face, mirrored חינם, then turns back | turn-over (cues stamp.flip, stamp.flipback) | slip, key line | stamp | soft turn |
| 2.0 to 5.3 | Cascade | זה כנראה מתחיל כבר במודעה. / חיפשתי "יועץ משכנתאות"... | 13 slips tossed from the sides; source line | camera pulls back to 0.7, slips land every 0.24 s | stamp waiting at the left edge | the pile | paper drops |
| 6.2 to 9.9 | Stamping | 8 מתוך 14 יועצים כותבים בכותרת חינם, או לחסוך. | tally rolls 1 to 8; prints חינם, ללא עלות, לחסוך | 4 free hits (last on "חינם"), 3 fast save hits on "לחסוך" | pile | the count | thunk per hit, varied |
| 10.2 to 11.3 | Lock (freeze) | | "8 מתוך 14" opens, source under it | "מתוך 14" wipes open | all (rest on the proof) | the 8 stamped slips | silence |
| 11.3 to 13.8 | Stack | בואו נגיד שאתם צריכים משכנתא. לפי מה אתם בוחרים? | 6 slips pushed off; 8 slide into one stack, prints form one red column | slips slide, camera pushes in | stamp parked top left | the stack | paper slides |
| 14.5 to 15.0 | Price tag (freeze) | תכלס, לפי המחיר. | gold hang tag "₪?" slapped on the stack's top edge | tag bounce | stack | the stamp | sticker slap |
| 15.2 to 17.9 | The practice | ואין לי טענות אליהם, ככה כותבים בתחום. | stack slides off, the stamp alone, centred | the stamp slides in, sits, rises, drifts, sits (one move per word) | key line | the stamp | small thunks on settle and sit |
| 18.0 to 20.4 | Your ad | אז תפתחו היום את המודעה שלכם. | blank slip lands: המודעה שלכם / [שם העסק] / [הכותרת] | stamp hops aside, slip drops, settles with a small bounce on "המודעה" | | the viewer's slip | paper slap, settle tap |
| 20.4 to 24.6 | Test | תכסו את שם העסק עם האצבע, ותקראו רק את הכותרת. | a finger's shadow over the name, the tape, pressed flat; the underline draws one step per word; the headline darkens | finger in, tape slap, press, finger out, 4 rule steps; camera follows the finger, then the rule right to left | slip | headline line | tape rip, press, pencil steps |
| 24.6 to 27.9 | Threat | המתחרה שלכם היה יכול לכתוב אותה אחד לאחד? | stamp hovers beside your headline (never over it) | hover, drift, dip toward the line, lift; camera leans in on the dip | slip | the stamp's shadow | held breath (score drops out) |
| 27.9 to 31.7 | Release | אם כן, תחליפו אותה במשהו שהוא לא יכול להגיד. | placeholder backspaced, caret blinks; stamp lifts away and leaves | backspace, slow lift | slip | the caret | soft lift whoosh |
| 31.7 to 34.6 | Pointer | למשל, מה בדיוק קורה אצלכם בפגישה הראשונה. | the pointer as the key line in the top band (stays to the end card); optional "דוגמה" slot (off) | camera push 1.14, then two drifts on "קורה" and "בפגישה" | caret blinking | caret | |
| 34.6 to 36.9 | Close | תשמרו את הסרטון, או תשלחו לחבר עם עסק. | captions; camera pushes into the caret | push to 1.55 | | the caret | silence before the card |
| 36.9 to 40.3 | End card | | charcoal opens out of the caret; white wordmark; שמרו · שלחו לחבר עם עסק, a caret blinking after it | card opens, mark and words rise | rest on the card | (end) | one soft thunk as the wordmark lands (no shimmer chord) |

Self-check (measured on `renders/draft-v1-silent.mp4` with `tools/pacing.py`): beat CV 0.57 (>= 0.25), longest beat
7.6x the shortest (>= 4x), short rests on the hook's face, the lock (10.2 to 11.3 s) and the price tag, longest quiet
run 2.58 s, nothing frozen over 3 s. Every reaction has a cause on screen (the stamp prints, the slips are pushed, the
stack is slid). The idea reads with the sound off (key lines + captions + the count + the column of identical stamps).
