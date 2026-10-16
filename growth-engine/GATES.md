# Pre-publish gates and the Director review

Every post passes all gates before it reaches Matan's Approve (ORGANIC-OS 7.5). The production gates per asset (Shot
Specs, prompt and visual reviews, takes, the final cut) live in the post's run ledger and are enforced by the
generation hook: `growth-engine/production/README.md`, `VISUAL-QA.md`, `STANDARDS.md`. The agent that owns a gate writes
`pass` or `fail` into the Post Card's `gates:` map with one line of evidence in `notes`. A post with any `fail` does not
go into the hub. Automatic checks: `python3 growth-engine/tools/organic.py card-check <slug> <cards>` and
`week-check`. Nothing is published or messaged without human approval.

| Gate (card key) | Pass when | Owner | Automatic part |
|---|---|---|---|
| `map` | card complete; pillar, series, avatar on the map; belief and job fit; one language | Strategist | card-check |
| `idea` | on the map; level-4 narrow product; Trinity of Value (complete, unique, depictable); shock score 5+ (write it); the $5 test; a key visual for the first 3 s | Idea Agent | demand phrase not off-map |
| `hook` | A or A+ on the 3-channel stack; 4 S's; none of the 4 mistakes; 10 hooks written | Hook Agent | |
| `script` | value per second; lock-in zone; loops; payoff; facts-feelings-fun; length fits the card's tier (STANDARDS 8; 30 to 60 s is only the usual range for a reach reel, not a fail) | Script Agent | length check |
| `sound_off` | understandable with no audio (captions, text, visuals) | Producer | |
| `visual` | every asset's ledger gates PASS (`pipeline.py status`: G-SPEC, G-PROMPT-IMG and G-PROMPT-VID, G-VIS*, G-TAKE, G-MOTION-TEXT and G-MOTION-FRAMES by fresh reviewers, G-AUDIO per audio asset, G-ASSETS, G-SET or G-FINAL; STANDARDS 9); safe zones per STANDARDS 6 (reels: top 14%, bottom 35%, the right 21% of the lower half and 6% sides clear); no watermarks or borders; readable at phone size; motion in the first second | Producer + fresh reviewers | the generation gate, `pipeline.py` |
| `originality` | not a repost; structure borrowed, content ours; AI label per STANDARDS 7 (D1 decides whether to extend it), with "AI label: on" in the hub notes; AI people (STANDARDS 7) only from behind, hands only, at a distance or stylized (the strategist may face the camera only as a presenter in his staged studio set), never presented as real clients | Director | |
| `truth` | every number and claim in the brain or proof bank; no counts on screens or in lines unless in the brain (STANDARDS 6); anecdotes only as framed POV dramatizations; no price, discount, guarantee or urgency; no answer-time promise ("we answer within 1 hour"); sector rules | Director | proof ids, B6 rule |
| `conversion` | one ask that fits the job: follow, save, send, comment (an answer to a question), keyword (only a keyword live in the brain), dm, or book (convert posts only, said as the keyword or DM path); keyword has a live flow and a real resource; never a link (STANDARDS 5) | Conversion Agent | card-check |
| `language` | non-English copy flagged for a native read in the hub notes | Director | |
| `budget` | G-BUDGET before the run's first generation, again within 24 h of each batch and at step 9 before any video call (STANDARDS 10); spend logged in `ledger.csv`; month under the cap with a 25% retake buffer; premium pieces have their 6 assets | Producer | `ledger`, `pipeline.py budget` |
| `human` | Matan approves on the hub's Content page | Matan | hub |

## Director batch review (before the batch goes to Matan)

For each post, answer in one line each; any "no" sends the post back with the fix:
0. Does `pipeline.py status` show every gate of the run passed (no open FAIL, no PENDING owner checkpoint)?
1. Will the right buyer stop scrolling, and will the wrong one scroll past?
2. What belief does this move, and is it one step from where they are?
3. Would a business owner send this to a partner?
4. Is this the best version of this idea on Instagram right now? If not, what's missing?
5. Is every claim true and in the brain or proof bank?
6. Does the CTA follow naturally from the payoff?

Then for the batch: does `week-check` pass; is there a contrarian and a B7 post; is the mix near the stage target;
which card is the riskiest bet and why it is still worth it. Write the review into
`clients/<slug>/reviews/<week>.md`.

## Weekly memo (Director, every Monday)

Top 3 and bottom 3 posts by their job metric (`organic.py score <slug>`), the diagnosis line for each bottom post,
three decisions (keep, kill, test), and any rule change backed by 3+ posts (append to `analytics/learnings.md`).
