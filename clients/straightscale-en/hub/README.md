# Hub business profile, English (draft)

`profile.en.json` is an English `profile` for the hub business that answers @straightscale_ DMs (the Social Agent
app, `lovable-app/`). It replaces the Albanian setup the business still runs (brain decision E10). **Draft only: it has
not been applied, and the live app and its database were not touched.**

Written 28 Oct 2026 from these sources only: `../brain.json` and `../brain.md` (offer, avatar, voice, constraints,
messaging draft), `../research/buyer-phrases-en.md` (buyer words in `audience`), and the WORDS Sheet and its funnels
in `motion-studio/projects/straightscale-en-02/resource/` (`WORDS.md`, `funnel/README.md`, `funnel/*.funnel.json`).
The schema is `BusinessSchema.profile` in `lovable-app/src/agent/config/schema.ts`; `lovable-app/src/agent/ai/prompts.ts`
puts every field into the DM prompt, the follow-up and the comment triage prompt.

## Validation

```
bun clients/straightscale-en/hub/tools/validate.ts
```

It parses the file with the app's own zod schema (`BusinessSchema.shape.profile`), fails on keys the schema would
drop, and lists the placeholders the app's audit (`hasPlaceholders` in `lovable-app/src/agent/logic/audit.ts`) would
block live sending on. Result on 28 Oct 2026: **PASS**, 10 fields, 9 FAQ entries, 2 placeholders (`faq[2].a`,
`faq[3].a`, both decision E3). A file with `goal` removed fails, so the check is real.

## Field by field: what changes from the Albanian profile

Summary of the Albanian setup as recorded in `clients/straightscale/brain.json`, not a copy of the live profile
(read the live one with `python3 growth-engine/tools/hub.py client <slug>` before applying).

| Field | Albanian setup | English draft |
|---|---|---|
| `about` | the Albanian business, office in Tirana | the whole client-getting system for founder-led coaches, consultants and agency owners, worldwide, in English |
| `offers` | the Client Engine, a 12-month partnership in Silver, Gold and Diamond packages; free 45-minute analysis in Tirana or at the business | one offer, the five steps in order (Research, Offer, Organic, Funnel, Paid ads last); free business analysis with a look at the competitors' ads; the WORDS Sheet; no prices in chat |
| `audience` | Albanian businesses (exact text not in the repo) | AV-01, the lumpy-pipeline owner, about $20K to $50K a month, with three verbatim buyer lines |
| `goal` | book the free 45-minute analysis (keyword ANALIZA) | ask the main bottleneck, then hand off to a person who sends a voice note and invites to the free analysis; the bot never books |
| `qualifying_questions` | not recorded in the repo | the main bottleneck (Matan's pick, 28 Oct, word for word from the WORDS funnel), plus "what do you sell, and who to" only when unclear |
| `faq` | not recorded in the repo (the brain's facts: packages, office, analysis) | what we do, price (not in DMs), the analysis, booking, "another agency?", guarantees (none), the WORDS Sheet, who we work with, results (no numbers) |
| `policies` | not recorded in the repo | 24-hour window only, no cold DMs, a price question gets "no prices in DMs" and the bottleneck question, hand off on results, contracts or anything not written, no push when the question is unanswered |
| `voice` | Albanian (register per `clients/straightscale/brain.json`) | calm and direct, English, "you", the buyer's own words, no emoji, no hype |
| `never` | not recorded in the repo | no results, prices, proof numbers, the Albanian offer, the sales team or CRM (E2), the AI VSL, lead follow-up, attacks on referrals, em dashes, hype, invented urgency |
| `extra` | not recorded in the repo | the WORDS routing from `funnel/README.md`, the "columns" reply, and how each bottleneck maps to the five steps |

## Gaps Matan must fill

1. **The free business analysis (E3):** what it covers beyond the competitors' ads, how long, call or in person, what
   the person keeps. Placeholder: `faq[2].a` (TODO).
2. **How it is booked (E3):** a booking link, a calendar or a person in the DM. Placeholder: `faq[3].a` (TODO). If it
   is a link, add it to the business's `links` (for example id `analysis`, `when`: "after a team member invited them")
   and mention it in `goal`.
3. **Who answers the hand-offs and sends the voice note (E3).** The draft assumes a person does; the app notifies the
   owner and pauses the AI in that thread.
4. **Price and what happens after the analysis (E4).** The draft never quotes a price; nothing to fill unless Matan
   wants a line such as "price on the call".
5. **Proof (E5):** no result is quoted. When the evidence files are in, a case-studies answer can replace `faq[8]`.
6. **Approve the messaging (E11):** `about` and the "another agency?" answer reuse the draft one-liner, boilerplate
   and contrast line.
7. **Business settings outside `profile`** (not in this file): `timezone` (unknown, E9), `lead_form.language` (`en`),
   a `words-sheet` link (the PDF URL `funnel/create.sh` uploads) if the bot should resend the sheet, and
   `ai.followup.enabled`: the WORDS routing says "no answer, no push", so the follow-up may be switched off.
8. **My choice, check it:** "No emoji" in `voice`. The brain records only "calm, direct".

The audit blocks live sending while either TODO is left, so the profile cannot go live half-filled.

## How it would be applied (not done)

- **Business editor** (recommended): the hub dashboard → Businesses → the business that holds @straightscale_ → paste
  each field into the Profile form, or put the whole `profile` block into the Advanced (YAML) tab, then Save. Do it
  with the business not live, test from a tester account, then switch the analiza funnels off and add the WORDS
  funnels (`motion-studio/projects/straightscale-en-02/resource/funnel/create.sh`).
- **`hub.py`:** it can only read a business (`hub.py clients`, `hub.py client <slug>`) and add funnels; it has no
  command that writes a profile, so it is for checking the current profile before and after, not for applying this.

## Checked against the rules

ORGANIC-OS 8.5 and `.claude/agents/conversion-agent.md`:

| Rule | Status |
|---|---|
| One qualifying question, the main bottleneck | pass: first in `qualifying_questions`, verbatim from the funnel |
| Qualified → a human setter, short voice note, invite to the free analysis | pass: `goal` and `extra` |
| Not qualified → free resource, no push | pass: `extra` and `policies` |
| Only inside the 24-hour window, no cold DMs | pass: `policies` |
| Button before the link, 10 to 60 minute wait, tags | funnel's job (`words*.funnel.json`, `after_delay_minutes: 20`) |
| WhatsApp hand-off, EUR 50 deposit | left out: neither is in the English brain |
| Facts only from the brain; no invented numbers, results, clients, reviews or prices | pass: the only numbers are the brain's $20K to $50K and the WORDS Sheet's counts |
| No em dashes, no hype words | pass (searched the file) |
| Never publish or message customers | pass: not applied |

ORGANIC-OS 8.1 and the conversion agent's 10-line profile check are about the Instagram profile itself (name, bio,
pinned posts, highlights); they do not apply to this file. The two lines that touch it: the booking link (gap 2) and
the lead-magnet link (gap 7).
