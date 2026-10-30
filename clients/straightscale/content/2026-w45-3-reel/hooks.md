# Hooks · 2026-w45-3-reel · SS-2026-11-W1-03

Hook Gate (Hook Agent, 28 Oct 2026): readymerce-hook-lab v1.1 + `growth-engine/adapters/hook-lab-organic.md`.
Card: reel_motion (HyperFrames, voiced), 30 s, reach/send, B2, problem_aware, hook_type hidden_cause, demand phrase
"klientët nuk kthehen". Narrow product: clients who bought once don't come back because nobody invites them back.
The fix is one message after the work: name the work, ask how it is going, leave the next step open.

**Every Albanian line: native read needed (D2 "ti").** No names or numbers on the list or the chats, no counts, no
platform names or logos.

The card's draft "Klientët nuk ikin." (3 words, under the 4 to 10 rule, and an absolute claim the card asked us to
soften) was replaced. No shipped line says the clients "did not leave". Every line asks or shows instead.

## H3: the 10 hooks (own grades V/T/S)
| # | Type | Text | Spoken line 1 | V | T | S |
|---|---|---|---|---|---|---|
| 1 | hidden cause | Klientët s'u kthyen. / A i ftoi kush? | Klientët e vjetër nuk kthehen, dhe ti mendon se ikën te konkurrenti. | A- | A | A |
| 2 | stop doing | Mos e mbyll punën / pa këtë mesazh. | Mos e mbyll asnjë punë pa i dërguar klientit një mesazh pas saj. | A- | B+ | B+ |
| 3 | visual-led | Klientët e vjetër po zbehen nga lista jote. | Shiko listën e klientëve që blenë një herë. | A- | A- | B+ |
| 4 | misdirection (card) | Klientët nuk ikin. / Askush s'i fton të kthehen. | Klientët nuk ikin. Thjesht askush nuk i fton të kthehen. | A- | B+ | B+ |
| 5 | question | Kur i shkrove për herë të fundit / një klienti të vjetër? | Kur i shkrove për herë të fundit një klienti që bleu një herë? | A- | A- | B+ |
| 6 | POV | POV: klienti yt i vjetër po pret një mesazh | (claims what the client wants: cut) | B | B | B |
| 7 | hidden cause | Ja pse klientët e vjetër s'kthehen më. | ... dhe nuk është çmimi. (absolute) | A- | B+ | B+ |
| 8 | two futures | Dy klientë. / Vetëm njëri mori mesazh. | Dy klientë blenë të njëjtën gjë, por vetëm njërit i shkrove pasi mbaroi puna. | A | A- | B+ |
| 9 | teaching | Mesazhi pas punës, në 3 pjesë. | Mesazhi që i dërgon klientit pasi mbaron puna ka vetëm tri pjesë. | B+ | A- | A- |
| 10 | contrarian | Nuk është konkurrenti. / Është heshtja jote. | (aims at the viewer) | B+ | B+ | B |

## Fresh grader (G-HOOK) and rewrites
Every round used a new `claude -p` grader (persona + rubric + stacks only). Its notes changed the visual: abstract
greying list rows (B+) became a **phone chat list where every past-client thread ends in the client's
"Faleminderit!" and then sinks under new chats**. The grader called this "the strongest sound-off frame of the set".
The spoken belief "ikën te konkurrenti" became "gjetën dikë tjetër", which is closer to his words.

Decision rule (whole week): a channel is A when most independent fresh grades of that exact wording are A or A+
(on a tie, the latest wins) and no gate fails; my own grade must also be A.

| Stack | Rounds (V/T/S) | Result |
|---|---|---|
| Master | R5 A/A/A, R9 A/A/A, R10 A/A/A, R12 A/A/A | **A** |
| Variant 1 | R14 A/A/A | **A** |
| Variant 2 | R16 A/A/A | **A** |

## SHIPPED: master stack (hidden cause) · grade A
- **Visual (H-01, from frame 1):** a phone's chat list of past clients, each with a small client avatar (no names, no
  numbers). Every thread preview ends in the client's last bubble, a large and readable "Faleminderit!", with nothing
  after it. Hold for about 1 s, then the threads sink under new chats and drop off the screen.
- **Text:** "Klientët s'u kthyen. / A i ftoi kush?" (EN: Clients didn't come back. Did anyone invite them?) 7 words.
- **Spoken:** "Klientët e vjetër nuk kthehen, dhe ti mendon se gjetën dikë tjetër. Po a i ftoi kush të kthehen?"
  (EN: Old clients don't come back, and you think they found someone else. But did anyone invite them back?)
  Sentence 1 is 12 words.
- **Open question at the seam:** what would the invitation say? The payoff shows the three-part message on screen
  (card draft: "Si po të shërben [puna]? Kur të duhet sërish, më shkruaj këtu.", native read needed).

## Trial variants
1. **Question.** Same sinking threads. Text: "Klientët nuk kthehen? / Shiko ku mbaron biseda." (EN: Clients don't come
   back? Look where the chat ends.) Spoken: "Ti mendon se klientët e vjetër ikën te dikush tjetër. Shiko ku mbaron
   biseda." (EN: You think old clients went to someone else. Look where the chat ends.) Grade A.
2. **Fear moment.** Same thread list, with each "Faleminderit!" large, held for 1 s, then the threads sink. Text:
   "Klientët nuk kthehen? / Çfarë ndodh pas faleminderit?" (EN: Clients don't come back? What happens after the thank
   you?) Spoken: "Klienti tha faleminderit, dhe ti mendon se do të kthehet vetë." (EN: The client said thank you, and
   you think they'll come back on their own.) Grade A.

## Notes for the Script Agent, the Video Producer and the Director
- The key visual changed from the idea gate's "rows of a past-client list fading to grey". The new frame is still
  code-rendered (HyperFrames), with no generated still needed. The chat UI must be generic: no platform styling,
  logo or name.
- Blocked by G-HUMAN-VOICE (narrator pending) and G-HUMAN-HOOKBOARD per the card. AI label on (AI voice).
- Grader tip: start the sink by about 1.2 s so the drop-off lands inside the first 3 s.
