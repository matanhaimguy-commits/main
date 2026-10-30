# Hook gate · 2026-w46-5-reel · SS-2026-11-W2-05 (Ad Library Spy #1)

Reel, 30 s, reel_motion · Attract · B3 · reach (sends) · hook_type teaching · AV-01 · demand phrase "paratë e
reklamave zhduken". Idea: before your next ad, open the public ad library and check 3 things in your category (which
ads have run the longest, what they all promise, what none of them says); what nobody says is your ad.

**Result: FAIL (nothing shipped).** The best stack is A- / A / A- (visual / text / spoken, panel median).

On-screen rule for this series: say "biblioteka publike e reklamave" (the public ad library) only, with stylized mock ad
cards (no brand, name, logo or real ad) and no platform named anywhere in the hook. The card's plan to name the real
library in the caption is outside the hook. The Distribution Agent should confirm it against the caller's rule: no
brand named.

## Method (same for all 7 W46 posts)
- Skill: readymerce-hook-lab v1.1 with `growth-engine/adapters/hook-lab-organic.md` (organic mode), the full Post Card,
  brain.json, content-map.json, analytics/learnings.md. Run 28 Oct 2026 by the Hook Agent.
- Round 1: 10 stacks written and self-graded; the top 3 go to a fresh grader. Rounds 2 to 8 are rewrites of the named
  weaknesses. From round 6 each set went to a panel of 3 fresh graders. A fresh grader is a new `claude -p` process
  that sees only the AV-01 persona card, the rubric (adapter 4 S's, Hook Lab per-channel rubric, grade scale) and the
  stacks, with an English gloss under each Albanian line. It never sees the card, the brain or earlier grades.
  Why a panel: one grader's verdict on identical lines moved by up to one grade between rounds. The panel's median per
  channel is the fresh grade.
- Ship rule: a stack ships only when the self-grade and the fresh median are both A or A+ on every channel. A- does not
  ship.
- No concept frames exist. Image generation was not allowed this run (shared balance nearly empty), so graders judged
  written frame specs, not pictures. That is the main reason visual channels stall at A-, and the adapter asks for a
  graded concept frame (G-VIS, `--hero`) anyway. When the balance allows, make the frames and regrade.
- Avoided: all W2, W3, W43 and W1 hooks (for example "Të shkruajnë, por nuk blejnë?", "Telefoni nuk bie?",
  "Sponsorizon postimin. Po pastaj?", "Pse të zgjodhën klientët e fundit?", "Klientët nuk ikin.", "Sa mesazhe mbetën pa
  përgjigje këtë javë?", "Një video virale është fat...") and Florina's "growth is a system" wording.
- Truth: no counts except the post's own items (5 questions, 4 things, 3 checks), no prices, guarantees, urgency,
  answer-time promises or "we answer for you". No analysis contents (D3), no AI faces (D1: hands only, from behind,
  objects), no platform names or logos on screen, no em dashes, no hype words. Register "ti" (D2 interim).
- Every Albanian line in this file is a draft: NATIVE READ NEEDED.

## Round 1: 10 stacks (self-graded)
Visual V0: stylized mock ad cards slide in as a stack, and one flips to a blank space by 1 s.

| # | Type | Text (sq) [en] | Spoken line 1 (sq) [en] | V | T | S |
|---|---|---|---|---|---|---|
| 1 | reveal | "Reklamat e konkurrentit janë publike." [Your competitor's ads are public.] | "Reklamat e konkurrentit tënd nuk janë sekret: janë në bibliotekën publike të reklamave." | A- | A- | A- |
| 2 | reveal | "Reklamat e konkurrentit nuk janë sekret." [... aren't secret.] | "Reklamat që mban konkurrenti yt mund t'i shohësh sonte, në bibliotekën publike të reklamave." | A- | A- | A |
| 3 | stakes | "Para reklamës tënde: shiko ç'paguan konkurrenti." (implies spend we can't see) | - | A- | B+ | - |
| 4 | list | "3 gjëra që i sheh te reklamat e konkurrentit." | "Hap bibliotekën publike të reklamave dhe kontrollo 3 gjëra para reklamës tënde të radhës." | A- | A- | B+ |
| 5 | payoff first | "Çfarë s'e thotë asnjë konkurrent? Ajo është reklama jote." | "Ajo që s'e thotë asnjë konkurrent në reklamat e tij, mund të jetë reklama jote." | A- | A- | A- |
| 6 | POV | "POV: lexon reklamat e konkurrentit para tij." (unclear) | - | - | B | - |
| 7 | stop doing X | "Mos e shkruaj reklamën e radhës pa parë këto." | "Mos e shkruaj reklamën tënde të radhës pa parë reklamat e konkurrentit, janë publike." | A- | A- | B+ |
| 8 | question | "E di çfarë reklamash mban konkurrenti yt?" | "E di çfarë reklamash mban konkurrenti yt? Janë publike, dhe i sheh sonte." | A- | A- | A- |
| 9 | absurd | "Spiunim i ligjshëm: reklamat e konkurrentit." (legal word, two readings) | - | B+ | B+ | - |
| 10 | reveal plus gap | "Reklamat e konkurrentit janë publike. Çfarë s'thonë?" | as 2 | A | A | A |

Fresh grader on the top 3 (10, 5, 8): 5-A V B+ T A- S B+ · 5-B V B+ T B S C · 5-C V B T B S B. None of the channels
states his stakes (ad money disappearing), and 5-B's text answers its own question.

## Rewrite rounds (fresh: V / T / S; from round 6, the median of 3)
| Round | ID | Text | Spoken line 1 | Fresh |
|---|---|---|---|---|
| 2 | 5-D | "Reklamat e konkurrentit janë publike. Çfarë s'thonë?" (desk scene with his own blank ad draft) | "Para se të paguash reklamën e radhës, shiko ato që i mban konkurrenti yt." | A- / A- / A- |
| 3 | 5-H | "Reklamat e konkurrentit janë publike. Çfarë s'thotë asnjë?" | "Para se të hedhësh para në reklamën tjetër, shiko çfarë reklamash mban konkurrenti yt." | A- / A- / A- |
| 4 | 5-I | "Reklamat e konkurrentëve janë publike. Çfarë s'thotë asnjëra?" | "Para se të hedhësh para në reklamën tjetër, shiko çfarë reklamash mbajnë konkurrentët." | A- / A- / A |
| 5 | 5-K | as 5-I | as 5-I | A- / A / A- |
| 6p | 5-N | as 5-I | "Para se të paguash reklamën tjetër, shiko çfarë reklamash mbajnë konkurrentët e tu." | A- / A- / B+ |
| 7p | 5-P | as 5-I | "Paratë e reklamës zhduken? Shiko cilat reklama mbahen më gjatë në kategorinë tënde." | A- / B+ / A- |
| 8p | **5-Q** | "Paratë e reklamave zhduken? Shiko çfarë s'thotë asnjë konkurrent." | "Reklamat e konkurrentëve janë publike, mund t'i shohësh sonte, para se të paguash tënden." | **A- / A / A-** |
| 8p | 5-R | as 5-Q | "Reklamat që mbahen më gjatë në kategorinë tënde janë publike; mund t'i shohësh sonte." | A- / A / B+ |

## Best candidate (NOT SHIPPED): 5-Q, hidden cause (his words plus the gap)
- Visual: at night, a hand holds the phone in its deep red case, filling the frame. Stylized mock ad cards stack up on
  the screen, each with a wide "REKLAMË" band, a drawn shopfront and a headline bar, and no readable brand, name or logo.
  By 1 s one card flips over to a blank space.
- Text: "Paratë e reklamave zhduken? / Shiko çfarë s'thotë asnjë konkurrent." [Ad money disappears? / See what no
  competitor says.] (9 words, his own demand phrase) NATIVE READ NEEDED.
- Spoken: "Reklamat e konkurrentëve janë publike, mund t'i shohësh sonte, para se të paguash tënden." [Competitors' ads
  are public, you can see them tonight, before you pay for yours.] NATIVE READ NEEDED.
- Weaknesses still named: the generic mock cards don't signal his trade; the spoken line is a list of three clauses.
- Truth kept: the hook never says the longest-running ads "work" (not in the brain); no "running for X days"; the 3
  is the post's own count.
- Next: regrade with the H-01 concept frame (the blank flip card is the picture that carries this hook).
