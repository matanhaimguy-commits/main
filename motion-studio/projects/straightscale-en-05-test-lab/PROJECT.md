# StraightScale EN · EN 05 "The post that knew" (part four: Organic)

Workflow: `readymerce-hook-lab` with `growth-engine/adapters/hook-lab-organic.md`, `readymerce-script-lab` with
`growth-engine/adapters/script-lab-organic.md`, story format from `growth-engine/production/STORY-FORMATS.md`; the
motion-reel skill for the build later. Docs: `docs/hook-stacks.md`, `docs/script-lab.md`, `docs/script.md`.

## Series (shared by EN 04, 05, 06; set by the session that made them, 28 Oct 2026)
- Account @straightscale_ (English, global). Avatar AV-01 "the lumpy-pipeline owner": founder-led coaches, consultants
  and agency owners whose months are lumpy (persona card: `../straightscale-en-03-song/docs/script-lab.md` section 2).
- Picture: Patchwork Marketing in its DIY form (every fix sewn on alone), the song's cloth world: the method is one cloth
  (the buyers' words) and every piece is cut from it, in order.
- Order of the method (vault note "StraightScale EN offer"): Research, Offer, Organic, Funnel, Paid ads. Part one is the
  song "Maya's quilt" (EN 03), part two is EN 02 (Research: where to find your buyers' words). This series continues:
  EN 04 = part three, Offer · EN 05 = part four, Organic · EN 06 = part five, Funnel. Paid ads (sung in the song) would be
  part six; the order is an owner question (summary).
- Each reel teaches one step the song only promised, so a follower gets the next piece; each ends on a follow CTA for
  the next part (reach job; no live keyword on the EN page).
- Facts only from the repo and the vault: the offer sheet, the buyer quotes already cited with ids in EN 01, EN 02 and
  the song's docs. No invented numbers, results, clients or quotes; no proof numbers (evidence files not collected).
  Names are composites in a stylized world. Never the not-sold angles (reply speed, lead follow-up, sales scripts).
- Copy rules: no em dashes, no hype words, "you/your", text hook 4 to 10 words, the name Patchwork Marketing never in the
  hook, no offer in the hook, StraightScale named at most on the end card.
- Spend: none. No image, video or audio generation in this stage.

## Brief
- Step this reel teaches: Organic: posts cut from the offer, each one built on a buyer sentence, run as the free test lab that shows which message brings the right buyers (offer sheet step 3 and the mechanism "organic first, then paid").
- Story template: `object_speaks` (STORY-FORMATS 3.4, ST3 via DEV-F1 talking part, Hook Lab HL-T1)
- Format: `reel_animation_short` (tier B, O30, animation style `claymation`, the song's world)
- Reference: `ig-papertiger-animation` (brand-ad; signature device before-after, plus character-host, reaction-shot): a smug host character watches a before turn into an after. `refbank.py check --client straightscale --devices before-after,character-host,reaction-shot --category brand-ad`: ok, no
  repeats against the last films (28 Oct). The song (EN 03) is not in the refbank ledger; checked by hand: no shared
  device or category with its claymation song cut. Log with `refbank.py log` only after delivery.
- Platform: 9:16 1080x1920 master, voiced, captions (sound-off read must carry it).
- CTA: follow for the next part (reach job).

## Status
Stage: script & VO (script v2 on the approved v2 master hook EN05-B: escalated to Matan after Script Lab)
Current version: script v2 final draft (loop 4), 87 words, about 34.8 s, gate 80/100 (best loop 2: 82), no critical fail (`docs/script.md`); no picture, no audio
Next step: Matan answers the escalation question (`docs/script-v2-loops.md`, "Escalation"); then one more gated loop or the concept frame
Blockers / open questions: Hook Lab v3 (Matan's A/A+ bar) did not reach the bar in 3 rounds; the best stack and its fix await the master decision (`docs/hook-lab-v3.md`); the approved text hook ("it's shouting") and spoken hook ("you're shouting") differ by one
word; process-only payoff (no proof files); the series numbering ("the next part")

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 28 Oct | **Hook Lab v3** (Matan: "only A and A+ hooks, clarity above all"): 10 new stacks from organic breakouts (HF) in buyer words, code check, 3 rounds of 2 fresh blind graders; **no stack reached A/A+ on all channels from both graders**. Best: EN05-R3b: text "Boosted a post and got nothing? Wrong post.", spoken "Boosted a post, got zero leads? You picked the wrong one." (round 3: V B+ / A-, T A- / A-, S A- / A). Graders' named fix, not yet graded: frame 1 shows "0 leads" on the post, not zero hearts. The v2 master is unchanged (`docs/hook-lab-v3.md`, `docs/hooks-v3.json`) | take the best stack; one more round on the named fix; keep the v2 master | Matan's bar; the main session's 3-round limit | Claude (proposal); Matan or the main session for him (pending) |
| 28 Oct | **Escalated** (script v2): spine A rewritten on the master v2 hook EN05-B, spoken hook word for word; Script Lab 4 loops (draft + 3 rewrites), 12 fresh cold readers (listen-only, skeptic, sound-off); scores 73, 82, 78, 80; no critical fail; not released (under 85). Recommended: A, the text hook matches the spoken hook word for word, then one more loop on the loop 2 draft | A: text hook = spoken hook + one loop; B: accept at 80; C: a narrator instead of the talking post (spine change) | Script Lab cap reached | Claude (escalation), Matan (pending) |
| 28 Oct | Hooks v2 (master EN05-B) | Matan | "much better and stronger"; next time base hooks on organic breakouts, not ads |
| 28 Oct | Hooks v1 rejected (Matan: unclear, not the buyers' words, written English, not proven formats). Hooks v2 built only from proven sources (Hook Library HA ads 30+ days or HF outliers 3x+) and verbatim buyer phrases; all pass `organic.py hooks`. Master = the ad-proven stack. The script release candidate is ON HOLD: it was written on the v1 hook and must be rewritten on the v2 master once Matan approves it, with the new "said, not written" rule | v1 kept; more AI grading rounds | an AI grade is opinion; proof is a post or ad that already won with this buyer | Matan (rejection), Claude (v2) |
| 28 Oct | GATE 4 decided: spine A "The post that got paid for" (the boosted post explains why nothing happened), no result shown; the hooks it was asked with (v1) were later rejected, see the row above; the script waits for the v2 hooks | B, C, more hook rounds | the writer's recommendation | Matan |
| 28 Oct | GATE 4: spine A "The post that got paid for" (ST3 on the talking post), B "Two posts" (ST6), or C "The push button" (ST8); riders: text hook, CTA wording, payoff picture | A, B, C (`docs/script-lab.md` 8 and 9) | Claude recommends A: the only spine with a graded opening, written to release candidate at 85 | Matan (pending) |
| 28 Oct | Spine A taken through WRITE: 4 loops (first draft + 3 rewrites), 85/100 at loop 4, no critical fail; labelled provisional | stop at loop 3 (critical fail) | the skill's 3 rewrite loops; loop 3 failed on "a free test" used before it was explained | Claude |
| 28 Oct | Master text hook swapped to "Quiet month? She paid to push a post. Nothing." (round 4, T A / A-); "...It wasn't the post." sent back to the Hook Lab | keep the graders' favourite text | Script Lab test 12: on spine A's body it read as a contradiction; one extra fresh sound-off read confirmed the swap (no script word changed) | Claude |
| 28 Oct | CTA "Follow for the next part: the page those buyers land on." with a "Part four" label on the end card, instead of "Follow for part five: ..." | the brief's "part five" | two cold readers stopped on "part five? what were one to four?"; the meaning (part five, Funnel) is unchanged; Matan may restore the number | Claude (Matan to confirm) |
| 28 Oct | Payoff shows a process (the buyers choose one post and walk toward the door), never a result; the CLIENTS pockets stay empty | a few clients in the pockets, as the song's owner-approved payoff | STORY-FORMATS 3 "the payoff shows a process"; no proof file; flagged because every sound-off reader asked "did she sign anyone?" | Claude (Matan to confirm) |
| 28 Oct | G-HOOK: not passed after 5 rounds of two fresh blind graders each; best stack recorded; taken to GATE 4 | more rounds | the cap in the brief (5 rounds); every grader's last A- is the visual at 1 s (a phone with a face reads cute first), which needs a real concept frame (no generation in this stage) | Claude, owner informed |
| 28 Oct | Persona card: the song's card plus two sentences ("you post content yourself... once or twice you put a little ad money behind a post"; "content has been a black box", Q-E-0183) | the song's card unchanged | the reel's moment (a paid push) must be in the persona's life, without naming the cause | Claude |
| 28 Oct | Template, format and reference as in the brief | the other STORY-FORMATS templates; refbank pick list | each reel of the series uses a different template and format from the song and from each other; refs pass `check` | Claude |

## Approvals
| Date | What (brief, concept, script, VO, styleframes, cut vN) | By | Notes |
|---|---|---|---|

## Log
- 28 Oct · folder made from `templates/project`; brief, template, format and reference set · ok
- 28 Oct · Hook Lab: 10 stacks graded, 3 kept; G-HOOK 5 rounds, 10 fresh blind graders (tool-less agents, persona
  card + H-01 spec in words only); not passed, best master recorded · `docs/hook-stacks.md`
- 28 Oct · Script Lab: brief card, persona, structure pick, ladder, 3 spines, recommendation, GATE 4 question; spine A
  through 4 loops with 9 fresh cold readers (listen-only and sound-off per loop, plus one hook-swap check); 85/100,
  release candidate, provisional · `docs/script-lab.md`, `docs/script.md`
- 28 Oct · no generation, no paid calls, nothing committed (the parent session commits)
- 28 Oct · hooks v1 rejected by Matan; hooks v2 from proven formats in docs/hook-stacks.md and docs/hooks.json (all PASS) · script on hold
- 28 Oct · Matan approved hooks v2 (master EN05-B) · script rewrite on it is next
- 28 Oct · script v2 on hook EN05-B: Script Lab 4 loops, 12 fresh cold readers, final 80/100 (best 82), escalated · `docs/script.md`, `docs/script-v2-loops.md`; v1 script moved to `docs/script-v1.md`
- 28 Oct · Hook Lab v3 on Matan's A/A+ bar: 10 stacks, 3 blind rounds, 6 fresh graders; best stack recorded, bar not reached · `docs/hook-lab-v3.md`
- 28 Oct · Hook Lab v3 round 4 (the graders' named fixes, 2 new graders): `EN05-R4` V A- / A-, T B+ / A-, S A- / A; the A/A+ bar not met, v2 master unchanged · `docs/hook-lab-v3.md`
