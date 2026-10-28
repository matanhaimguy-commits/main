# WORDS funnel (EN 02, @straightscale_)

ORGANIC-OS 8.5 and `.claude/agents/conversion-agent.md`, in the hub's funnel format (`lovable-app/src/agent/config/schema.ts`
`FunnelSchema`; stored by `POST /api/content/funnels`, which `hub.py funnel` calls). Both files validate against that
schema (checked 28 Oct 2026 with the hub's own `schema.ts`, placeholders filled).

| File | Trigger | Scope |
|---|---|---|
| `words.funnel.json` | comment "WORDS" | pinned to the EN 02 post only (`posts`), Instagram and Facebook |
| `words-dm.funnel.json` | "WORDS" sent as a DM | account-wide (for people who DM the word instead of commenting) |

## The flow
1. **Comment WORDS** on EN 02. A public reply under the comment ("Sent you a DM with the searches.").
2. **Button before any link** (`opener.mode: "tap"`): "Want me to send you the WORDS Sheet? ... about 20 minutes."
   Button: **Send it**. The tap opens the 24-hour window. No follow gate (it would cost one more tap; low_friction).
3. **The resource** (`deliver`): one line on how to use it and the button **Open the sheet**, linking to `WORDS.pdf`
   uploaded to the hub's storage.
4. **One qualifying question** (`after`): "what does a normal month bring in for you right now? Under $10K, $10K to
   $20K, $20K to $50K, or over $50K?" It maps straight onto the EN offer's buyer ($20K to $50K a month).
5. **Routing** (the hub's AI assistant reads the answer; it lives in the business profile, not the funnel, so the
   owner sets it in the dashboard):
   - **$20K to $50K, or over $50K** → qualified. The AI hands off to a person (the hub's handoff: the owner is
     notified, the AI pauses in that thread). The person sends a short voice note with a mini diagnosis from what
     they said, then invites them to the free business analysis (the offer sheet's free entry).
   - **$10K to $20K** → warm. The AI thanks them, answers questions about the sheet, and points to the next posts.
     No call invite unless they ask for one.
   - **Under $10K, or no answer** → not qualified. Thanks, the sheet, nothing else. No follow-up push.
   - Anyone who replies **"columns"** (the sheet's last line) with their niche: the AI asks the same question if not
     yet answered, then routes as above.
6. **Tags**: every message the funnel sends carries `funnel_id` (`words` or `words-dm`) and the step; the comment
   funnel is pinned to the EN 02 post, so keyword and post are attributable. The answer sits in the thread and the
   contact's stage.

Policy: messages only go inside the 24-hour window the person opened. No cold DMs.

Proposed business-profile lines for the owner to paste in the dashboard (Business → Profile), only if he agrees:
- `qualifying_questions`: "What does a normal month bring in right now? Under $10K, $10K to $20K, $20K to $50K, or
  over $50K?"
- `extra`: "WORDS funnel: $20K a month or more → hand off to a person for a voice note and the free business analysis
  invite. Under $20K → thank them, help with the sheet, no call invite unless they ask. Never quote prices or results."

## Create it (blocked here: NO_TOKEN, 28 Oct 2026)
Once `HUB_TOKEN` is set and EN 02 is posted (the post ID is needed to pin the comment funnel):

```
python3 growth-engine/tools/hub.py clients        # find the business whose Instagram is @straightscale_
bash motion-studio/projects/straightscale-en-02/resource/funnel/create.sh <that-slug> <en02-post-id>
```

`create.sh` uploads `WORDS.pdf` with `hub.py upload`, puts its public URL and the post ID into both files, and runs
`hub.py funnel` for each. Then test with a tester account (`testers` in the business) before the business is live.

## Known gap
ORGANIC-OS 8.5 step 4 says to wait 10 to 60 minutes before the qualifying question. The hub sends `after` right
after the delivery (`lovable-app/src/agent/engine/funnel.ts`, `if (delivered(outcome) && f.after)`). A delay needs a
hub change (owner decides; it goes through the hub repo with tests).
