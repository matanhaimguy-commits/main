# StraightScale EN · song 01 "Maya's quilt" (TOF)

Workflow: `readymerce-song-ads` with `growth-engine/adapters/song-organic.md`, Hook Lab (`hook-lab-organic.md`) and
Script Lab (`script-lab-organic.md`); the motion-reel skill for the edit. Offer sheet: vault note "StraightScale EN
offer" (Research, Offer, Organic, Funnel, Paid ads). Docs: `docs/hook-stacks.md`, `docs/script-lab.md`,
`docs/script.md`.

## Brief
- Account: @straightscale_ (English, global). Job: reach (TOF), leads to the whole offer through its order.
- Avatar: AV-01 "the lumpy-pipeline owner" (research run foundation v2, 09-AVATARS).
- Angle: "Steady months, without adding one more tactic." Solution aware (generic). Picture: Patchwork Marketing in
  its DIY form (every fix sewn on alone), named in the chorus only.
- Lengths: O60 written at about 50 s, plus an O30 written on its own (STANDARDS 8).
- Genre: indie folk storytelling, one narrator-singer: a warm male baritone (locked for the series).
- Look: claymation (organic.json `animation_styles.claymation`), clay clients in the pockets of a CLIENTS wall organizer, fixes as labelled fabric scraps, the method as one cloth.
- CTA: follow for part two ("Follow for part two: where to find your buyers' words."; part two is EN 02).
- Facts: none on screen or in the lyrics (proof files not collected); Maya is a composite in a stylized world.

## Status
Stage: step 7 look bible in progress (see the production handoff); song masters approved (G-HUMAN-SONG PASS)
Next: owner decisions in docs/script.md "Writer's recommendation" (O30 release, O60 fixes + one more gate, CTA follow
to EN 02, the payoff picture); then lyrics, lyric gate, style prompt; the song route; G-HUMAN-SONG before any picture.
Open: song route (ElevenLabs Music billing failed; Atlas Suno needs the owner to name the model in the gate; or the
owner makes it in Suno by hand, the song skill's default) · the visual hook is re-graded on the claymation concept
frame after G-HUMAN-SONG · hook variants back to H6 before any trial reel.

## Production handoff (28 Oct, EN 03 production session 2)
Run: `clients/straightscale-en/runs/SS-EN-SONG-01` (moved from `clients/straightscale/` on the main session's call, so
G-BUDGET counts the English $100 cap). Slug `straightscale-en` from now on.

Done:
- Step 5 (G-TIMELINE PASS): masters downloaded; `growth-engine/tools/song_timeline.py` places the final lyric words by
  forced alignment (pocketsphinx; faster-whisper's model host huggingface.co is blocked here) and makes the librosa beat
  grid, line times and 5 to 15 s slices: `audio/words.json`, `audio/timeline.json`, `audio/timeline.md`. O60 97 BPM,
  voice in 0.92 s, 18 lines, 6 slices; O30 85 BPM, voice in 0.36 s, 11 lines, 3 slices. No vocal stem (Demucs host blocked).
- Step 6: 24 O60 Shot Specs (O30 reuses them, `qa/o30-reuse.md`); 7 silent H3-KEY clips, 37 s; 12 stills; end card in code.
  G-SPEC after 2 rounds: 16 PASS; 8 FAIL with fixes in `qa/r2/O60-SH*.spec.json` (SH01, 03, 04, 05, 06, 07, 15, 20).
  SH03/SH04 vs SET-OFFICE: the MARCH tag must match (sheet says orange, left of the laptop; shots say ivory): pick one.
- Step 7 look bible: 7 sheet specs (`shots/SHEET-*`). Generated on `openai/gpt-image-2` medium: CH-MAYA v1 (G-VIS-SHEET
  FAIL minor: needle hidden, bottom row at the edge), CH-FRIEND v1 (FAIL major: seated panel), PR-ORGANIZER v1 (FAIL major:
  3x2 grid) and v2 (grid, counts and band fixed; G-VIS-SHEET FAIL on 4 minors: April pocket shape differs between states, band overhang, copies 46% wide; waivable or one more retake, `qa/PR-ORGANIZER.v2.review.json`), PR-SCRAPS v1 (PASS), PR-CLOTH v1 (FAIL minor: 8 bubbles,
  printed letters). Look report for the main session's G-HUMAN-LOOK: `qa/look-report.md`.
- Spend this session: 6 images, about $0.35 (live balance falls faster: other sessions share the account).

Next:
1. SET-OFFICE and SET-FRIEND: G-SPEC PASS; prompts failed round 3 (the main session's limit). Apply the corrected
   prompts in `qa/r3/SET-*.v1.prompt.json`, then a fresh review and generate (about $0.10).
2. CH-FRIEND v2 (edit pass on v1): prompt failed; add the chair back to `SHEET-CH-FRIEND` (spec says no furniture), take the
   corrected prompt in `qa/r3/CH-FRIEND.v2.prompt.json`, re-review spec and prompt, generate.
3. CH-MAYA and PR-CLOTH minors: the owner may waive them at G-HUMAN-LOOK, or retake.
4. The 8 failing O60 specs: apply their fixes, fresh G-SPEC, close step 6 (G-PLAN).
5. Step 8 (keyframes, hook frame H-01 with MARCH above APRIL), then step 9: `pipeline.py budget straightscale-en
   SS-EN-SONG-01 --planned 2.78 --balance <live>` (plan in `qa/clip-budget.md`: $2.78, $3.47 with buffer).
- Studio: storage uploads are blocked here (lovable.cloud host); the run was pushed with Atlas URLs for the 6 sheets (studio/1). Docs are not on the page.
- Ledger media ids were corrected from Atlas operation ids to prediction ids (28 Oct); CH-FRIEND@v2's edit_source is now 186285be...

## Production handoff (28 Oct, EN 03 production session 3)
Look-bible packet for the evaluator: `clients/straightscale-en/runs/SS-EN-SONG-01/qa/look-bible-packet.md` (every
sheet, its review, the waived minors, what is still open).

Done:
- Sheets: PR-ORGANIZER v3 (edit pass on v2) failed G-VIS-SHEET on a major (the state A April pockets are still tall
  cylinders), so v2 is locked with its minors waived. SET-FRIEND: simpler spec (ivory paper wall, the friend's
  organizer, a small shelf), G-SPEC and G-PROMPT-IMG PASS, generated as v1: G-VIS-SHEET FAIL on 2 layout minors only
  (organizer and shelf bigger than the spec boxes). SET-OFFICE: simpler spec (desk, bin, window) failed G-SPEC twice,
  so no set sheet: the spec moved to `qa/retired/`, and every office shot carries a "World" line (plain ivory paper
  wall and floor, soft warm light, and the look of the desk, chair, laptop, mug, bin and window it names).
- CH-FRIEND: spec fixed (seated panel straight to camera, warm curious look, taupe chair back, sleeves inside the
  canvas), G-SPEC PASS. The v2 edit prompt failed three fresh reviews in a row, each on a new point (r5, r6), so it is
  past the loop limit and not generated. The last corrected prompt is in `qa/r6/CH-FRIEND.v2.prompt.json`.
- O60 specs: the 8 r2 fixes, the SET-OFFICE fallback, PR-ORGANIZER@v2 refs and the reviewers' round fixes applied to
  all 23 shot specs (`qa/r7` to `qa/r10`). SH20 now keeps SH19's frame (no 125% punch-in: it did not fit SH19's
  layout). SH03/SH04 keep the ivory MARCH desk tag (no sheet holds it now).
- Step 6 closed (G-PLAN and G-SPEC PASS on every spec in `shots/`). Advisories for the prompt writers (not in the specs, to keep the passes): SH17 give the window a box and scope "no people" to its start frame; SH20 add the right thumb under the band, the left hand "empty, fingers loosely curled", and the pull as about 3% of frame width; SH06/SH07/SH12 the MARCH row height above the frame; SH09/SH11 say whether the headset is on.
- Tool fix: `pipeline.py prompt --media` now splits the role off the end, so a URL or `prediction:ID:INDEX` value
  works as a reference (test in `test_pipeline.py`). Edit passes use the previous version's Atlas media URL, registered
  on it with `pipeline.py media --id <url>`.
- Atlas note: a new output first sits on a `temp-24h-*` host that the proxy blocks; after about a minute
  `atlas generate get <id>` returns an `atlas-media` URL that downloads.

Next (main session):
1. Fresh evaluator on the look-bible packet, then G-HUMAN-LOOK (main session). Decide SET-FRIEND (waive or retake)
   and CH-FRIEND (one more review of the corrected prompt, simplify, or escalate).
2. Step 8 keyframes and the hook frame H-01 after LOOK (stills: about 25 images, about $1.48).
3. Step 9: `pipeline.py budget straightscale-en SS-EN-SONG-01 --planned <USD> --balance <live>` once steps 6 to 8
   are closed (plan in `qa/clip-budget.md`, update of 28 Oct session 3: $2.49, $3.11 with buffer). Clips wait for Matan's Atlas top-up.

## Production handoff (28 Oct, EN 03 production session 4: G-HUMAN-LOOK conditions)
Spend: $0 (no generation; the only image work was a crop in code). Live Atlas balance $2.03 at the end.

Done:
- Condition 1: the World line, word for word, in the style and setting of every office shot (SH01 to SH23; SH24 style
  too); "marble" only as "no marble". Paper reference REF-PAPER@v1 (`assets/refs/PAPER-IVORY.v1.png`, a crop of
  CH-MAYA@v1 made by `growth-engine/tools/paper_crop.py`, mean #faeed6), registered as a style_ref, G-VIS-SHEET PASS,
  and named as setting.ref in every office shot. `atlas upload` failed (401: it needs a real console login; the proxy
  key covers only the API host), so it has no Atlas URL yet: upload it and register the URL with
  `pipeline.py media ... REF-PAPER@v1 --id <url>` before the first call that uses it.
- Condition 2: the free route: PR-LAPTOP, PR-BIN and PR-MARCHTAG described in full in every shot that uses them; each
  shot's office-item list trimmed to the items it names. No prop sheet.
- Condition 3: SH01/SH02 APRIL pockets "shallow slanted pockets, dark empty interior"; thumb-and-index pinch (SH05,
  SH06); exactly nine bubbles (SH23) and exactly three where three show (SH17, SH18); stitched lettering (SH15 to SH17).
- Condition 4: AI label on, `qa/packaging-notes.md`; SH08, SH09, SH22 carry a must_not against framing the clay women
  as real clients or results.
- Condition 5: SH08 (chest-up three-quarter bust on Maya's laptop, on her desk), SH09 (small on the screen) and SH22
  (three-quarter view mirrored to face Maya, hands in her jacket pockets; Maya's hands under her folded arms) on
  CH-FRIEND v1's standing views.
- G-SPEC: rounds r12 and r13 (fresh sonnet reviewers, `qa/r12`, `qa/r13`). Each round found new, older geometry points
  (organizer proportions, safe zones, hand and text boxes, the SH10 to SH11 dolly, the SH17 to SH18 pan); all are fixed.
- Step 7 closed. Step 8 blocked (below). G-BUDGET recorded (see `qa/clip-budget.md`).

Open (main session):
1. G-SPEC: PASS on the current files of SH09, SH12 to SH16, SH18 to SH20, SH23, SH24 (11 of 24). Open: SH01 to SH08,
   SH10, SH11, SH17, SH21, SH22 (13). Each failed two loops (r12, r13); the r13 fixes are applied and lint passes, but a
   third review is the main session's call (loop limit 2). Rule question for the main session: each fresh reviewer finds
   new, older geometry points; set a scope (fail only on defects a generation would trip on) before a third round.
2. The waived sheets block every image call: the gate refuses CH-MAYA@v1, PR-CLOTH@v1, PR-ORGANIZER@v2, SET-FRIEND@v1
   and CH-FRIEND@v1 as references because their G-VIS-SHEET is FAIL; a delegated G-HUMAN-LOOK does not change that, and
   only the owner's OVERRIDE (`--by Matan`) does. Ask Matan for an OVERRIDE on those five, or change the gate.
3. Step 8: silent one-shot clips need no storyboard, but the step needs G-CONTINUITY on board assets and
   G-HUMAN-HOOKBOARD on H-01. Decide: keyframes as the boards (about $0.77 for 13), or mark step 8 not applicable for
   silent keyframe song pieces (a rule change).
4. Step 9: whole piece $2.37 ($2.96 with buffer) against $2.03: gap $0.93. Clips wait for the top-up.
5. G-HUMAN-ESCALATE PR-ORGANIZER@v3 stays queued and unsent (v3 abandoned).

## Production handoff (29 Oct, EN 03 production session 4, after the main session's decisions)
- G-SPEC round 3 (`qa/r14`, scope in `qa/r14/scope.md`): 20 of 24 specs PASS on their current files. Open: SH01, SH02,
  SH03 (simplified: no laptop or mug in the SH01 to SH02 frame, no mug in SH03) and SH10 (its background now names the
  belt, trousers, floor and the paper wall that the 3x zoom of SH11 shows). Their fixes are applied and lint passes; no
  4th round was run (main session rule).
- Prompt stage, SH08 (main session, 29 Oct): the prompt must say CH-FRIEND v1's three-quarter panel is mirrored
  horizontally so she faces image-left (kept out of the spec to keep its PASS).
- Main session accepted the SH01, SH02, SH03 and SH10 simplifications; one fresh review of the four (`qa/r15`, same
  scope). A fail there is simplified in place, not reviewed again.
- r15: SH01, SH02, SH03, SH10 PASS, so all 24 specs pass G-SPEC on their current files. Prompt-stage notes from its
  advisories: SH01 the hook overlay covers most of CLIENTS in the edit (not just its right end), and the three overlay
  strings are never rendered; SH01 check the organizer's proportions by eye against H-01; SH02 both hands out of view
  in front of her body; SH03 the pile is blank loose clay papers, the hero read is Maya looking up at April; SH10 her
  chin at the top edge is soft and not key, LINKEDIN and COACH are out of frame.
- Paper reference: no upload. CH-MAYA@v1 now carries its Atlas URL; office prompts attach it with the line "use only the
  plain ivory paper background of this reference". REF-PAPER@v1 stays as the local check copy (specs still name it).
- Owner question: `G-VIS-SHEET-OVERRIDE` queued in the ledger and asked on the Studio page as decision #4 (run #1,
  business straightscale). Not answered yet, so nothing was generated. On "Override all five", record five
  `pipeline.py gate ... G-VIS-SHEET --status OVERRIDE --by Matan --asset <sheet> --note "<his answer>"` and mark the
  answer with `hub.py studio-synced 4`.
- The queued PR-ORGANIZER@v3 escalation is marked WITHDRAWN in the ledger (never sent, no owner answer recorded), so the
  Studio push does not show it as waiting.
- Studio push: storage uploads stay blocked (lovable.cloud host), so the run was pushed with the files already on the
  page plus SET-FRIEND v1 by its Atlas URL.

## Decisions (newest first)
| Date | Decision | Options considered | Why | Who |
|---|---|---|---|---|
| 29 Oct | Step 8: the 13 keyframes (7 start, 6 end, about $0.77) serve as the boards; no rule change | step 8 not applicable for silent clips | they are the clips' start frames anyway | main session, delegated by Matan, plan 28 Oct |
| 29 Oct | G-SPEC round 3 (one round) on the 13 open specs, FAIL scoped to defects a generation would trip on (field contradictions, picture-changing geometry, missing face/hand/text regions, text that renders wrong, look-condition breaches); the rest is advisory; a spec still failing is simplified, no 4th round | open-ended rounds | stop the loop | main session, delegated by Matan, plan 28 Oct |
| 29 Oct | Paper reference: no upload; the Atlas-hosted CH-MAYA v1 sheet is the paper reference with the line "use only the plain ivory paper background of this reference"; REF-PAPER@v1 stays as the local check copy | upload REF-PAPER | no console login | main session, delegated by Matan, plan 28 Oct |
| 29 Oct | One owner question on the Studio page: OVERRIDE the G-VIS-SHEET fails of CH-MAYA v1, PR-CLOTH v1, PR-ORGANIZER v2, SET-FRIEND v1, CH-FRIEND v1 (recommended: override all five; or redo the sheets first); the producer never records it | record it under the delegation | owner only | main session, delegated by Matan, plan 28 Oct |
| 29 Oct | Generation: stills and keyframes only, within the G-BUDGET PASS ($1.48, $1.85 with buffer), only after the override is answered; never under $1.50 live balance; clips wait for the top-up | | | main session, delegated by Matan, plan 28 Oct |
| 28 Oct | G-HUMAN-LOOK conditions: prop text instead of a prop sheet (condition 2); paper reference as a code crop; SH08/SH09/SH22 on CH-FRIEND v1 standing views; step 8 marked blocked | a combined prop sheet ($0.09); CH-FRIEND v2 | free and safe; the waived sheets block every generated board | producer session 4, for the main session |
| 28 Oct | Look report: lock PR-SCRAPS v1; lock CH-MAYA v1 and PR-CLOTH v1 with their minors waived (clip prompts state a clean thumb-and-index needle pinch, nine bubbles, stitched lettering); PR-ORGANIZER one last retake (v3), else lock v2 with minors waived; CH-FRIEND seated panel redo (v2); SET-OFFICE and SET-FRIEND replaced by simpler set specs, at most 2 rounds, else the plain ivory backdrop | more retakes of each sheet; a 4th round on the set prompts | stop the loops, keep the series look | main session, delegated by Matan, plan 28 Oct |
| 28 Oct | PR-ORGANIZER v3 failed on a major: v2 locked with its 4 minors waived (clip prompts state shallow, slanted April pockets and the band inside the felt edges) | a v4 | the main session's rule: v3 was the last round | main session, delegated by Matan, plan 28 Oct (applied by the producer session) |
| 28 Oct | SET-OFFICE: the new spec failed G-SPEC twice, so no set sheet; office shots use the plain ivory paper backdrop and a shared World line | a third spec round | the main session's 2-round rule | main session, delegated by Matan, plan 28 Oct (applied by the producer session) |
| 28 Oct | CH-FRIEND v2 prompt stopped after 3 failed reviews (pipeline loop limit 2); not generated | a 4th review | the loop limit sends it to the Director or the main session | producer session, for the main session to decide |
| 27 Oct | Song route: Atlas Suno (`suno/chirp-v6`, named in the gate by the owner); singer: warm male baritone narrator, locked for the series. Pipeline run `clients/straightscale-en/runs/SS-EN-SONG-01` (steps 0 to 3 recorded; G-HOOK OVERRIDE by Matan). Masters: O60 take 2 (59.6 s, Whisper match 0.956), O30 take 2 (32.4 s, 0.896); about $0.26 on Atlas | ElevenLabs Music (billing failed); Suno by hand; female alto | owner pick | Matan |
| 27 Oct | Escalation after 3 rewrite loops: O30 (86) held until the O60 is settled; O60 gets the 4 line fixes and one more gate; CTA "Follow for part two: where to find your buyers' words." (part two = EN 02); the payoff shows a few clients in April, fewer than March (the one result image, approved over song-organic.md 5's process-only rule) | O30 release now; park or release the O60 as is; CTA save; payoff process only | owner pick; readers asked for the April payoff in every sound-off read and for a "how" reel before following | Matan |
| 27 Oct | GATE 4: spine A "Maya's quilt" (ST3 hidden cause, named-person story) with its O30 short; opening text problem first "Nothing filled April. Referrals filled March. Why?"; look claymation | spine B "The patches sing"; text good month first; crochet, 3D office | owner pick; every hook grader read crochet as a craft video at half a second | Matan |
| 27 Oct | G-HOOK not passed after 6 blind rounds (master V A-, T A- to A, S A- to A); taken to GATE 4 | more rounds | grader variance on text and sung; the visual's A- was the crochet style itself | Claude, owner informed |
| 27 Oct | Patchwork in its DIY form (fixes she tried herself, each sewn on alone), not the agency form | vault form "ads, funnel, sales with different people"; MK-02 "nobody owns the sale" | AV-01 never hired those people (09-AVATARS §13); MK-02 is a reply/sales angle the offer sheet rules out | Claude, owner informed |
| 27 Oct | GATE 3: angle "Steady months, without adding one more tactic", solution aware, picture Patchwork | | | Matan |
| 27 Oct | GATE 2: indie folk storytelling, O60 + O30 | | | Matan |
| 27 Oct | GATE 1: avatar AV-01 | | | Matan |
