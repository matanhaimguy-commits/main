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
| # | Voice (client language) | English check | On screen |
|---|---|---|---|
Word budget: N words ≈ N/2.4 s. Hook line A / alt hook B.

## 5. Beat sheet (on the voice or beat grid)
| Time | Beat | Voice | On screen | Moving | Still | Link to next (what survives) | Audio |
|---|---|---|---|---|---|---|---|
Checks: beat lengths vary (CV >= 0.25, longest >= 4x shortest) · a rest of >= 1 s after the hook ·
every transition names its survivor · every reaction has a visible cause · nothing new is static for > 4 s.
