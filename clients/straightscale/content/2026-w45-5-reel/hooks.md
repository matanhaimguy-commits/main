# Hooks · 2026-w45-5-reel · SS-2026-11-W1-05

Hook Gate (Hook Agent, 28 Oct 2026): readymerce-hook-lab v1.1 + `growth-engine/adapters/hook-lab-organic.md`.
Card: reel_motion (HyperFrames, voiced), 30 s, convert, B5, solution_aware, hook_type comparison, CTA ANALIZA,
demand phrase "paratë e reklamave zhduken". Narrow product: the same boosted post, followed twice, once with nothing
after the click and once with a path (a reply, a second message, a booking step).

**Every Albanian line: native read needed (D2 "ti").** No euro amounts, results, counts, "we answer for you",
platform names or logos. "Sponsorizo" and "Sponsorizuar" appear as generic labels on a generic card, never in a
real platform's interface or styling.

Claim check: the shipped hook says the ad money is lost **after the click** (brain B1: "Your ads aren't failing.
Your enquiries are dying after the click."). It never says that boosts don't work, which the idea gate ruled out.

Avoided: W3-05 (freelancer vs agency vs system).

## H3: the 10 hooks (own grades V/T/S)
| # | Type | Text | Spoken line 1 | V | T | S |
|---|---|---|---|---|---|---|
| 1 | comparison | Sponsorizon postimin. / Po pas klikimit? | I njëjti euro në të njëjtin postim të sponsorizuar, me dy përfundime krejt të ndryshme. | B+ | A | A- |
| 2 | comparison (card) | Sponsorizon postimin. / Po pastaj? | I njëjti euro: një herë për një postim..., një herë për rrugën pas klikimit. (16 words) | B+ | A- | B |
| 3 | misdirection | Postimi s'dështoi. / S'kishte ku të shkonte. | Postimi që sponsorizove nuk dështoi; pas klikimit thjesht nuk kishte ku të shkonte. | B+ | A- | A |
| 4 | villain mockery | Butoni i sponsorizimit, prapë. | (implies boosts bring nothing: cut) | B+ | B | B |
| 5 | two futures | I njëjti euro. / Dy përfundime. | as 1 | B+ | A- | A- |
| 6 | question | Ku shkon klienti pasi klikon? | ... | A- | A- | A- |
| 7 | hidden cause | Ja pse sponsorizimi mbaron te shikimet. | ... | A- | A- | B+ |
| 8 | stop doing | Mos sponsorizo prapë / para se ta dish këtë. | Mos sponsorizo postimin tjetër pa ditur ku shkon klienti pas klikimit. | A | A- | A |
| 9 | POV | POV: sponsorizon prapë të njëjtin postim | ... | B+ | B+ | B+ |
| 10 | fear (his words) | Paratë e reklamave zhduken? / Shiko pas klikimit. | Paguan sponsorizimin, njerëzit klikojnë, dhe pastaj asnjë mesazh. | A- | A | A |

## Fresh grader (G-HOOK) and rewrites
New `claude -p` grader each round (persona + rubric + stacks only). Its findings:
- A split screen in the first 3 s doesn't read at phone size, and it shows the solved path too early.
- One version failed the one-claim gate (R4): coins falling through the post card said "lost in the ad" while the
  voice said "after the click".
- His own words ("paratë e reklamave zhduken") lock him in fastest.
- The frame that reads in 1 s is a click on a "Sponsorizuar" card that lands on an **empty "Mesazhet" screen with a
  comic tumbleweed**. A grader suggested a "0 new messages" label. It was refused because screens never show counts.

Decision rule (whole week): a channel is A when most independent fresh grades of that exact wording are A or A+
(on a tie, the latest wins) and no gate fails; my own grade must also be A.

| Stack | Rounds (V/T/S) | Result |
|---|---|---|
| Master | text A in R15, R16, R17; spoken A in R15, R16 (A- R17); this visual A in R17 (earlier cuts A- in R15, R16) | **A** |
| Variant 1 | R14 A/A/A- (earlier ending), R15 A/A-/A; text A in R13, R14 | **A** |
| Variant 2 | R11 A/A/A (single grade) | **A** |

## SHIPPED: master stack (fear moment, his words) · grade A
- **Visual (H-01, from frame 1):** a click pointer taps a generic post card labelled "Sponsorizuar". The view jumps to
  the messages screen, headed "Mesazhet": completely empty, with a comic tumbleweed rolling across it. No counts, no
  amounts, no real platform styling. The two-lane comparison (no path vs a path) starts **after 3 s**, in the body.
- **Text:** "Paratë e reklamave zhduken? / Shiko pas klikimit." (EN: Ad money disappears? Look after the click.)
  7 words.
- **Spoken:** "Paguan sponsorizimin, njerëzit klikojnë, dhe pastaj asnjë mesazh. Ku shkuan?" (EN: You pay for the
  boost, people click, and then not one message. Where did they go?) Sentence 1 is 8 words.
- **Open question at the seam:** where did they go? The body follows the same boosted post twice: one lane ends at
  the empty inbox, the other passes the reply, the second message and the booking step. It closes on C1 and then the
  ANALIZA CTA (brain offer facts only, nothing on what the analysis covers; D3).

## Trial variants
1. **Workaround reveal.** Visual: the red-case phone on a shop counter, a "Sponsorizuar" post card at the top of the
   screen, and a tumbleweed rolling across the empty message area below. Text: "Sponsorizon prapë, / e mesazhet
   s'vijnë?" (EN: Boosting again, and the messages don't come?) Spoken: "Sponsorizon prapë postimin, njerëzit e
   shohin, por askush s'të shkruan. Ku humbën?" (EN: You boost the post again, people see it, but nobody writes to
   you. Where did they get lost?) Grade A.
2. **Fear moment.** Same counter-phone frame (this trial changes only the super and the first line). Text:
   "Sponsorizove postimin. / Pas klikimit, asnjë mesazh?" (EN: You boosted the post. After the click, no message?)
   Spoken: "Sponsorizove postimin, njerëzit e panë, po pse askush s'të shkroi pas klikimit?" (EN: You boosted the
   post, people saw it, so why did nobody write to you after the click?) Grade A (R11, a single grade).

Dropped: the comic repeated-press variant ("Prapë sponsorizim?"). Graders split between A and B+ on its text and
visual (R7 to R19), so it is not shipped.

## Notes for the Script Agent, the Video Producer and the Director
- The key visual changed from the idea gate's "one euro coin drops into a split screen in the first second": the
  split now starts after 3 s. The card's comparison structure is unchanged.
- Blocked by G-HUMAN-VOICE (narrator pending) and G-HUMAN-HOOKBOARD per the card. AI label on (AI voice).
- One grader asked to check whether owners see this interface in Albanian or English. Keep the labels generic and
  Albanian; never copy a real interface.
