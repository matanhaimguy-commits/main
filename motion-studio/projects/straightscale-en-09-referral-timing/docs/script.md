# EN W1-03 twin pilot: script (step 3, G-SCRIPT)

Script Lab with `growth-engine/adapters/script-lab-organic.md`. Speaker: the twin, as Matan, the founder, in his cloned
voice (brain `host`). Structure ST3 hidden cause on the calendar device. Tier O60. Producer session, 31 Oct 2026.

## The script, v3 (the words the twin says; `script-v3.spoken.txt`)
1. Some months you sign three clients. Some months, literally nothing.
2. Referrals aren't the problem. They're your best clients.
3. But can you pick the month your next one comes?
4. No. It comes when a client happens to talk about you.
5. So in the empty months, you wait.
6. You can't pick the month. But you can stop just waiting.
7. Your posts can talk about you every week.
8. But most posts sound like everyone else's.
9. The ones that land say the problem the way your buyer says it.
10. My first line? Almost word for word from a business owner's post.
11. And you're still watching.
12. Lines like that sit in your competitors' reviews and in Reddit comments.
13. We made a free PDF that finds them: twelve searches you copy and paste.
14. Comment the word WORDS, and I'll DM it to you.
15. Half an hour later, you have their words for your next post.

On screen, 0 to 3 s: "Empty months? It's not referrals. It's waiting for them." (master hook W902-R2a). Lower third:
"Matan, founder of StraightScale".

149 words: about 54 s at 2.75 words/s, 60 s at 2.5. Matan's cloned voice pace is not measured yet (step 4). If the voice
runs over 60 s, cut line 11 (4 words) first.

## Facts (every one from the brain)
- Line 1 adapts buyer phrase Q-R-0058 ("some months wed sign 3 clients other months literally nothing", r/Entrepreneur,
  21 Mar 2026). Line 10 says "almost word for word", which is true of the adaptation. "Three" is the buyer's number, not a
  result of ours.
- Lines 12 to 15: the WORDS Sheet (brain `lead_magnets`): a 5-page PDF, 12 copy-paste searches in six sources including
  competitors' Google reviews and Reddit; a first run takes 20 to 30 minutes and gives 9 to 15 buyer sentences. Sent in
  the DM.
- No result, number, client or price of ours; no proof-bank entry used (STANDARDS 7). No em dashes, no hype words.

## Loops (3 of 3 used; 2 fresh Sonnet cold readers per loop: listen-only and sound-off, AV-01 persona)
| Loop | Words | What the readers found | Score |
|---|---|---|---|
| v1 | 131 | Scroll point L7 to L9 (the same idea three times); major confusion L11 to L13 on the core rung (no bridge from "timing" to "posts"); L2 gives her a belief she doesn't hold; "the sheet" asked for before it's explained | about 70, FIX |
| v2 | 143 | Retell 5 of 5 from both readers; no scroll point; minor: "WORDS" unclear as the literal keyword, "we" never introduced, "can you pick the month" never closed, ends on effort | 85, borderline |
| v3 | 149 | Retell 5 of 5 from both readers; no scroll point (both "nearly" at L5 to L8, "post more" fatigue); minor: L6 to L7 hinge, "my first line" hard to place with sound off, "competitors' reviews" fit, StraightScale unexplained | **86** |

## Gate report, v3
SCORE  Comprehension 21/25 (retell 10, confusion 6: four minor, none major on a core rung; scroll points 5) ·
Ladder and handoffs 17/20 (the L6 to L7 hinge) · Hook 9/10 · Mechanism 9/10 · Proof 8/10 (process shown, L10 and L11;
no proof bank by rule) · CTA 9/10 (organic re-weight: fits the job 3, keyword on a reach post is a card-check warning;
the four jobs 4; DM match 2) · Emotion and identity 3/5 (the payoff is "words for your next post") · Ear 5/5 · Length
5/5 = **86/100**. Critical fails: none.
Both readers' shared doubt: how one better-worded post fills a given month. The reel does not answer it on purpose (no
result may be promised); it is the DM funnel's job (the bottleneck question, then the free analysis).
Score note: the score is the producer's own count from fresh readers' reads, not an independent grader; a fresh
evaluator should re-score before release.

## Status: written, not released
G-SCRIPT is NOT recorded and no VO asset is registered. The script ends on the WORDS keyword, and WORDS has no funnel
in the hub (31 Oct, `hub.py client straightscale`: only `analiza` and `analiza-dm`, which are the Albanian offer and
off limits for the English page). brain.json has WORDS `live: false`, `funnel_id: null`. The card keeps `cta_type: send`
so card-check passes. When the main session creates the WORDS funnel and marks the keyword live, the release steps are:
the card to `cta_type: keyword`, `cta_keyword: WORDS`; `pipeline.py asset ... VO --type voice --tool
mcp__HeyGen__create_speech`; `pipeline.py prompt ... VO --file script-v3.spoken.txt` (prints the sha256); then G-SCRIPT
PASS with `--score 86 --data '{"script_sha256": "<that hash>"}'`.
If the main session prefers the card's send CTA instead, lines 13 to 15 become a send close, and the script needs a new
cold read.
