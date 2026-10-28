# Script Lab, organic adapter

Pass this file and the full Post Card with every `readymerce-script-lab` call for an organic reel. Script Lab's
belief ladder, line table, cold read and 85/100 gate still apply. These rules replace its paid-ad parts.
Source: ORGANIC-OS.md 7.3.

- **Structure** (pick one, name it): problem-solution, breakdown, case study, list, tutorial, myth vs truth, tier list
  bridge, "never ever", borrowed interest, personal story.
- **Lock-in zone:** the 2 to 4 sentences after the hook confirm the claim and pass a trust check (a proof anchor from
  the brain, production care, relatability). No proof in the bank: show the process (7.6).
- **But / therefore**, never "and then". Every answer opens the next question. Second-best point first, best point
  second.
- **Value per second:** mark every line green (keep), yellow (trim), red (cut); cut to about a third of the first draft.
- **Facts, feelings, fun:** one number or logic beat (only from the brain), one emotional beat, one twist or light moment.
- **Payoff in the last 3 to 5 s:** the twist or result. End on a loop back to the hook, or a CTA that is the natural
  next step of the payoff. No "follow for more" endings.
- **Organic CTA ladder instead of the offer close** (ORGANIC-OS 7.3 and 6.2): follow for the series → save → send to a
  partner → comment KEYWORD for the resource → DM / book, plus `comment` (an answer to a question the post asks, not a
  keyword). Use the card's `cta_type`; it must fit the card's job as `config/organic.json` `jobs` lists it (reach:
  follow, save, send, comment, keyword; trust: keyword, save, comment, follow, send; convert: keyword, dm, book).
  `keyword` only for a keyword marked live in the brain (StraightScale: ANALIZA). `book` only on a convert post, and
  said as the keyword or DM path ("comment ANALIZA; the booking button comes in the DM", brand kit "One path"). Never a
  link, price, discount, guarantee or urgency (STANDARDS 5, end card).
- **Hard offer posts** (about 3% of output, ORGANIC-OS 6.2): a convert post about the client's one free offer
  (StraightScale: the free analysis), with the same limits as every convert post. No "what happens in the analysis"
  (B8) post until decision D3.
- **Length:** the card's tier decides (STANDARDS 8, the single source for lengths); the script gate's length check
  passes when the runtime fits that tier. "30 to 60 s for reach" is only the default range for a reach reel, not a fail
  for an O15 quote reel or an O30 short. Never over 90 s until the owner confirms a longer limit (STANDARDS 8). Word
  budget at the cast voice's measured pace.
- **Voice:** `reel_motion` is always voiced (owner rule, 15 Oct 2026, in `config/organic.json`); the AI voice means the
  AI label is on (STANDARDS 7). Other formats are voiced or silent as their format and adapter say. Captions carry every
  voiced line with the sound off. (brand-kit.md's budget note "voiceover only on flagship reels" does not match the
  `reel_motion` rule; the owner is asked to align them.)
- **Cold reader** reads as AV-01 from the brain, scrolling at night, sound off first.
- **Said, not written** (owner rule, 28 Oct 2026): every voiced line is something an owner says out loud to a friend:
  short common words, the buyers' own words (`research/buyer-phrases-en.md`) for the problem, no written-register or
  marketing words ("quote", "solutions", "leverage", "framework", "proposal") unless the buyers wrote them. The plain
  check in `organic_os/hook_plain.py` is the same list; a cold reader who stumbles on a word is a fail for that line.

## Rungs, tiers and scoring for organic (from the Script Lab read, 15 Oct 2026)
- **Paid rungs out:** rungs 10 Value, 11 Safety and 12 Now (offer, guarantee, urgency) don't exist in organic posts.
  They are replaced by **one CTA rung** that fits the card's job. Critical fail 2 ("a rung the tier requires is
  missing") counts against the organic rung list below, so a script is never failed for having no offer.
- **Organic tiers** (seconds in STANDARDS 8; this list only names the shapes): O15 (one point), O30 (myth buster ST6,
  mistake ST7 short, hidden cause ST3 compact, demo ST14; the animation short; the song short), O60 (the story tier: POV
  day ST4, hidden cause ST3, two futures ST5, challenge ST17 episode, drama POV, song), O90 (only with a stated reason).
  Podcast runs only at C45. "No story under 55 s" becomes **no full discovery story under 45 s**; under 45 s use the
  compact shapes.
- **Tiers per concept:** tier A story pieces (`tier: "A"` in `config/organic.json`: animation, song, drama) keep the
  owner spec's rule (AI-VIDEO-PIPELINE step 1): the concept gets a story tier (O60) and a short tier (O30), each written
  on its own and released on its own (85+), never a trim of the main script; the short is one of the piece's 6 derived
  assets (ORGANIC-OS 7.7). Tier B and C posts are written at one tier, the card's. Why: they are single cuts that test
  an angle cheaply before any upgrade (ORGANIC-OS 7.7 rule 1) and make no derived short; a podcast runs only at C45;
  an angle that wins is upgraded to a tier A piece, which then gets both tiers.
- **Rungs per organic tier:** O15 1-2 (recognition, CTA); O30 recognition, cause in one picture line, the fix (method),
  CTA; O60 recognition, stakes (the accommodation), failed fix, aha (hidden cause, THE PICTURE), mechanism in one or two
  lines, lived payoff, CTA; identity close optional.
- **Scorecard re-weight:** the 10 points of "Offer, risk reversal and CTA" become: CTA fits the job (4), the CTA's
  jobs (the action, what happens next, the effort, the reason: 4), DM-funnel match (the keyword DM continues the
  reel's promise in the same words: 2). Pricing and guarantee lines are N/A. Test 15's urgency check and test 16's
  guarantee and "later" objection items are N/A.
- **The "product"** is usually the method (the UMS) or the insight. The reveal plan says "method named after the aha"
  and the agency is named lightly or not at all ("how we do it for clients" at most).
- **Structures by name** (GRADE must name one): problem-solution = ST2, breakdown = ST3 or ST9, case study = ST11
  (real case only), list = ST7, myth vs truth = ST6, personal story = ST4 or ST16, challenge = ST17, demo = ST14,
  two futures = ST5. Story templates in `growth-engine/production/STORY-FORMATS.md` name their ST code.
- **Persona card for B2B:** the owner (AV-01), at night, phone in hand, "a reel starts playing in your feed", "would
  you follow / save / send it?" instead of "would you tap?". The retell asks what the post taught, not what the product is.
- **Two cold reads:** listen-only (Script Lab's) and **sound-off** (captions and on-screen text only, as most reels are
  watched muted).
- **Claims:** no legal team checks small clients' posts, so the cold-read gate also checks every fact against the
  brain's facts and proof bank; nothing that sounds like a guaranteed outcome. No counts in a line or on a screen unless
  the number is in brain.json (screens show states: "a pile of unanswered messages"); no real platform names or logos on
  screen ("the inbox", "the phone"); anecdotes in the brand's voice only as clearly framed POV dramatizations
  ("POV: ..."), never stated as something that happened (STANDARDS 6 and 7).
- **Albanian pace:** budget words at the cast voice's measured pace (STANDARDS 4: 2.5 words/s before casting; the
  StraightScale narrator voice is in STANDARDS 1); numbers as words; brand names spelled for the TTS.
- **Release record:** the verdict line goes into the ledger: `pipeline.py gate <slug> <post_id> G-SCRIPT --status PASS
  --by "script-lab gate" --score <n>` (85+ and no critical fail), with the gate report saved in `runs/<post_id>/qa/script-gate.md`.
  Songs: the speech passes first, then the lyrics pass the lyric gate; the run's one G-SCRIPT record is written after
  both, its note naming both scores (STANDARDS 9).
- **Organic LEARN:** per post at 72 h and 7 d (the analyst): map the retention drop-offs to line numbers where the
  insight exists, else the skip rate and average watch time; add 1 or 2 lessons to `clients/<slug>/analytics/learnings.md`
  and the hook result to the client's Hook Library.
