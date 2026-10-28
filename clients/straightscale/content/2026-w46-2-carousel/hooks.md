# Hook gate · 2026-w46-2-carousel · SS-2026-11-W2-02

Carousel, 7 slides, carousel_self_check · Close · B3 · trust (keyword ANALIZA) · hook_type self_check · AV-01 · demand
phrase "na krahasojnë me çmimin". Idea: after the quote, 5 yes/no questions; the one that decides most is whether a
next step was agreed before the price went out.

**Result: FAIL (nothing shipped).** The cover reached A with every fresh grader across 4 rounds. Slide 2, which must
work alone, peaked at A- (panel median), so the pair does not ship. The cover is locked as the best cover; slide 2
needs one more rewrite.

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

## Round 1: 10 stacks (cover visual + headline / slide 2), self-graded
Cover visual C0: a sealed printed quote on a counter beside the red-case phone; the chat's last bubble is the owner's
quote, seen, no reply.

| # | Type | Cover headline (sq) [en] | Slide 2 (sq) [en] | Cover | S2 |
|---|---|---|---|---|---|
| 1 | self-check | "Pas ofertës: 5 pyetje që tregojnë ku ikën klienti" [After the quote: 5 questions that show where the client goes] | "Ofertë pa hap tjetër = klient që hesht." [Quote with no next step = a client who goes quiet.] | A- | A- |
| 2 | self-check | "Të krahasojnë me çmimin? 5 pyetje para se ta ulësh." [They compare you on price? 5 questions before you lower it.] | "Para se të dërgosh çmimin: a e di klienti hapin tjetër?" [Before you send the price: does the client know the next step?] | A | A- |
| 3 | self-check | "Pas ofertës, heshtje? 5 pyetje para se ta ulësh çmimin." [Silence after the quote? 5 questions before you lower the price.] | as 2 | A | A- |
| 4 | vivid sign | "Dërgove ofertën dhe klienti u zhduk? 5 pyetje." [Sent the quote and the client vanished? 5 questions.] | "Klienti që hesht pas ofertës po krahason. Me kë?" (claim too firm) | A- | B+ |
| 5 | question | "Ku shkon klienti pasi i dërgon çmimin? 5 pyetje." [Where does the client go after you send the price?] | "A u ra dakord për hapin tjetër, para çmimit?" | A- | A- |
| 6 | mistake | "Gabimi pas ofertës nuk është çmimi." [The mistake after the quote isn't the price.] (unconditional) | - | B+ | - |
| 7 | personal | "Oferta e fundit që humbe: e di pse?" [The last quote you lost: do you know why?] | as 2 | A- | A- |
| 8 | list | "5 pyetje para se ta ulësh çmimin." [5 questions before you lower the price.] (no moment) | as 2 | A- | A- |
| 9 | hidden cause | "Çmimi s'e humbi klientin. Ndoshta heshtja pas ofertës." (two readings) | - | B+ | - |
| 10 | label | "Ofertë e dërguar. Klient që hesht. 5 pyetje." (a label, overlaps W2-06) | - | B+ | - |

Fresh grader on the top 3 (2, 3, 7): 2-A cover B+ S2 B · 2-B cover A S2 B · 2-C cover B+ S2 B. Notes: drop the
envelope (most quotes go out by chat, and a sealed envelope reads "not sent"); slide 2 must carry the silence and the
stakes on its own.

## Rewrite rounds (fresh: cover / slide 2; from round 6, the median of 3)
| Round | ID | Cover | Slide 2 | Fresh |
|---|---|---|---|---|
| 2 | 2-D | "Pas ofertës, heshtje? 5 pyetje para se ta ulësh çmimin." (phone hero, "Oferta" card) | "Klienti hesht pas ofertës? E di kur flisni sërish?" | A / A- |
| 3 | 2-G | as 2-D | "Oferta u pa. Përgjigje s'ka. E di kur flisni sërish?" | A / A- |
| 4 | 2-J | as 2-D | "Oferta u pa, përgjigje s'ka. Ratë dakord kur flisni sërish?" | A / A- |
| 5 | 2-K | as 2-D | "Oferta u pa. Ratë dakord se kur do flisni sërish?" | A- / B+ |
| 6p | 2-L | as 2-D | "Ofertë pa hap tjetër? Klienti krahason, ti pret." | A / A- |
| 7p | **2-O** | as 2-D | "Klienti krahason, ti pret. Ratë dakord kur flisni sërish?" | **A / A-** |
| 8p | 2-P | as 2-D | "Pas ofertës: klienti krahason, ti pret. Ratë dakord kur flisni?" | A / B+ |

## Best candidate (NOT SHIPPED): 2-O
- **Cover (A, locked):** visual: the phone in its deep red case, large, on a kitchen-showroom counter next to a cabinet
  door sample; the chat's last bubble is the owner's quote as a document card titled "Oferta" (no amount), seen, no
  reply; no platform name. Headline (2 lines, 10 words, the 5 is the post's own count): "Pas ofertës, heshtje? / 5
  pyetje para se ta ulësh çmimin." [Silence after the quote? / 5 questions before you lower the price.] NATIVE READ
  NEEDED.
- **Slide 2 (A-):** "Klienti krahason, ti pret. / Ratë dakord kur flisni sërish?" [The client compares, you wait. / Did
  you two agree when you'd talk again?] NATIVE READ NEEDED. Named weakness: seen first, it doesn't say the comparing
  happens after the quote. When "Pas ofertës" is added (2-P) it goes over 10 words and reads long.
- Next rewrite route (ungraded): "Pas ofertës: ai krahason, ti pret." as a 2-line headline, with the yes/no question as
  item 2 on slide 3. Or regrade with the slide rendered, since the "Oferta" card can sit on slide 2 too.
- Gates checked: no price amount, no days or hours for a follow-up, nothing on what the analysis covers (D3), CTA
  untouched (brain offer facts only).
