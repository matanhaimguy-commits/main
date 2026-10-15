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
- **Organic CTA ladder instead of the offer close:** follow for the series → save → send to a partner → comment KEYWORD
  for the resource → DM / book. Use the card's `cta_type`; it must fit the job (reach: follow/save/send; trust: keyword
  for a resource/save; convert: keyword/DM/book). Keyword CTAs only for keywords marked live in the brain.
- **Length:** reach reels 30 to 60 s; never over 3 minutes. Word budget at the cast voice's measured pace.
- **Every reel has a voice** (owner rule). Captions carry it with the sound off.
- **Cold reader** reads as AV-01 from the brain, scrolling at night, sound off first.

## Rungs, tiers and scoring for organic (from the Script Lab read, 15 Oct 2026)
- **Paid rungs out:** rungs 10 Value, 11 Safety and 12 Now (offer, guarantee, urgency) don't exist in organic posts.
  They are replaced by **one CTA rung** that fits the card's job. Critical fail 2 ("a rung the tier requires is
  missing") counts against the organic rung list below, so a script is never failed for having no offer.
- **Organic tiers** (STANDARDS.md "Length"): O15 (10 to 20 s, one point), O30 (20 to 35 s: myth buster ST6, mistake
  ST7 short, hidden cause ST3 compact, demo ST14), O60 (45 to 75 s: the story tier: POV day ST4, hidden cause ST3, two
  futures ST5, challenge ST17 episode), O90 (75 to 100 s, only with a stated reason). "No story under 55 s" becomes
  **no full discovery story under 45 s**; under 45 s use the compact shapes. One tier per post is enough; the short
  cut of a premium piece is one of its 6 derived assets.
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
  brain's facts and proof bank; nothing that sounds like a guaranteed outcome.
- **Albanian pace:** budget words at the cast voice's measured pace (StraightScale's narrator in STANDARDS.md); numbers
  as words; brand names spelled for the TTS.
- **Release record:** the verdict line goes into the ledger: `pipeline.py gate <slug> <post_id> G-SCRIPT --status PASS
  --by "script-lab gate" --score <n>` (85+ and no critical fail), with the gate report saved in `runs/<post_id>/qa/script-gate.md`.
- **Organic LEARN:** per post at 72 h and 7 d (the analyst): map the retention drop-offs to line numbers where the
  insight exists, else the skip rate and average watch time; add 1 or 2 lessons to `clients/<slug>/analytics/learnings.md`
  and the hook result to the client's Hook Library.
