# Pre-publish gates and the Director review

Every post passes all gates before it reaches Matan's Approve (ORGANIC-OS 7.5). The agent that owns a gate writes
`pass` or `fail` into the Post Card's `gates:` map with one line of evidence in `notes`. A post with any `fail` does not
go into the hub. Automatic checks: `python3 growth-engine/tools/organic.py card-check <slug> <cards>` and
`week-check`. Nothing is published or messaged without human approval.

| Gate (card key) | Pass when | Owner | Automatic part |
|---|---|---|---|
| `map` | card complete; pillar, series, avatar on the map; belief and job fit; one language | Strategist | card-check |
| `idea` | on the map; level-4 narrow product; Trinity of Value (complete, unique, depictable); shock score 5+ (write it); the $5 test; a key visual for the first 3 s | Idea Agent | demand phrase not off-map |
| `hook` | A or A+ on the 3-channel stack; 4 S's; none of the 4 mistakes; 10 hooks written | Hook Agent | |
| `script` | value per second; lock-in zone; loops; payoff; facts-feelings-fun; 30 to 60 s for reach | Script Agent | length check |
| `sound_off` | understandable with no audio (captions, text, visuals) | Producer | |
| `visual` | safe zones (top 14%, bottom 20%; reels: top 250 px, bottom 400 px, right 140 px), no watermarks or borders, readable at phone size, motion in the first second; every letter read at full size | Producer | 4:5 or 9:16 sizes |
| `originality` | not a repost; structure borrowed, content ours; AI people labeled per D1 and never presented as real clients | Director | |
| `truth` | every number and claim in the brain or proof bank; no guarantees; sector rules | Director | proof ids, B6 rule |
| `conversion` | CTA fits the job; keyword has a live flow and a real resource | Conversion Agent | card-check |
| `language` | non-English copy flagged for a native read in the hub notes | Director | |
| `budget` | spend logged in `ledger.csv`; month under the cap with a 25% retake buffer; premium pieces have their 6 assets | Producer | `ledger` |
| `human` | Matan approves on the hub's Content page | Matan | hub |

## Director batch review (before the batch goes to Matan)

For each post, answer in one line each; any "no" sends the post back with the fix:
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
