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
| `hook` | the twin hook rule (below): in one blind run on packet-v2 with the 2 anchors, both of 2 fresh graders score the hook at least as well as both anchors on visual, text and spoken, and it fails none of the 9 checks; the visual graded on a real concept frame (gpt-image-2 on Atlas, series look; never a description); pre-grade checklist done; 4 S's; none of the 4 mistakes; 10 hooks written; at most 3 rounds, then the next idea | Hook Agent | `organic.py hooks`, `hook_rule.py` |
| `script` | 85+ within 3 rounds, else the next idea (never escalated); value per second; lock-in zone; loops; payoff; facts-feelings-fun; length fits the card's tier (STANDARDS 8; 30 to 60 s is only the usual range for a reach reel, not a fail) | Script Agent | length check |
| `sound_off` | understandable with no audio (captions, text, visuals) | Producer | |
| `visual` | every asset's ledger gates PASS (`pipeline.py status`: G-SPEC, G-PROMPT-IMG and G-PROMPT-VID, G-VIS*, G-TAKE, G-MOTION-TEXT and G-MOTION-FRAMES by fresh reviewers, G-AUDIO per audio asset, G-ASSETS, G-SET or G-FINAL; STANDARDS 9); safe zones per STANDARDS 6 (reels: top 14%, bottom 35%, the right 21% of the lower half and 6% sides clear); no watermarks or borders; readable at phone size; motion in the first second | Producer + fresh reviewers | the generation gate, `pipeline.py` |
| `originality` | not a repost; structure borrowed, content ours; AI label per STANDARDS 7 (D1 decides whether to extend it), with "AI label: on" in the hub notes; AI people (STANDARDS 7) only from behind, hands only, at a distance or stylized (the strategist may face the camera only as a presenter in his staged studio set), never presented as real clients | Director | |
| `truth` | every number and claim in the brain or proof bank; no counts on screens or in lines unless in the brain (STANDARDS 6); anecdotes only as framed POV dramatizations; no price, discount, guarantee or urgency; no answer-time promise ("we answer within 1 hour"); sector rules | Director | proof ids, B6 rule |
| `conversion` | one ask that fits the job: follow, save, send, comment (an answer to a question), keyword (only a keyword live in the brain), dm, or book (convert posts only, said as the keyword or DM path); keyword has a live flow and a real resource; never a link (STANDARDS 5) | Conversion Agent | card-check |
| `language` | non-English copy flagged for a native read in the hub notes | Director | |
| `budget` | G-BUDGET before the run's first generation, again within 24 h of each batch and at step 9 before any video call (STANDARDS 10); spend logged in `ledger.csv`; month under the cap with a 25% retake buffer; premium pieces have their 6 assets | Producer | `ledger`, `pipeline.py budget` |
| `human` | Matan approves on the hub's Content page | Matan | hub |

**The twin hook rule** (Matan, 29 Oct 2026; replaces "A or A+ from both graders", which no grader gave even to the
skill's own winners: `production/hook-grader-calibration.md`). A hook passes when, in the same blind run, both fresh
graders score it **at least as well as 2 of the `readymerce-hook-lab` skill's proven winner hooks** (the anchors,
`production/hook-calibration/anchors.json`) on **every channel (visual, text, spoken)**, and it **fails none of the 9
checks** for either grader. Each grader is compared with its own grades of the anchors in that run, and with the
stronger of the two anchors on each channel. A channel with no real grade (no concept frame yet: visual "n/a") cannot
pass. The grader packet is `production/hook-calibration/packet-v2` (the skill's rubric, a target buyer on every stack);
every grading run carries the 2 anchors, shuffled in under neutral labels (`tools/hook_packet.py`). The code is
`tools/hook_rule.py`; `pipeline.py gate ... G-HOOK --status PASS` takes only the data `tools/hook_record.py` builds
from the run (the grades, the anchors, the verdict, recomputed on every PASS).

**Replace, don't escalate** (Matan, plan of 28 Oct): a hook below that bar, or a script under 85, after at most 3 rounds, is replaced by the next idea in the bank. A take or
concept frame failing 3 times gets a simpler shot. None of these goes to Matan; he sees the hook board
(G-HUMAN-HOOKBOARD, which the main session may also take as a delegate after a fresh evaluator: STANDARDS 9) and the
finished post. Rules in `adapters/hook-lab-organic.md` (with the real-frame rule and the pre-grade checklist) and
`adapters/script-lab-organic.md`.

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
