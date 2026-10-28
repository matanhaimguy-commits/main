# carousel-machine, organic adapter

Pass this file, the full Post Card and `growth-engine/production/STANDARDS.md` with every `carousel-machine` call for
an organic carousel (`carousel_*` formats) or a single image (`image_*`, "carousel-machine (1 slide)"). The skill's
method stays: idea score, formats, the six story positions, the body copy rules, the style locks, the continuity plan,
cover and slide 2 as anchors, the 8f known failures and the Step 9 checks. What changes: the hook comes from Hook Lab in
carousel mode, a fresh agent cold-reads the slide copy, every slide gets a Shot Spec and a reviewed prompt, a fresh
visual reviewer (G-VIS-SLIDE per slide, G-SET for the set) replaces the skill's own critic loop, and the real logo is
pasted after review. Where this file or STANDARDS.md disagrees with the skill, they win for organic posts (section 9).
Built from carousel-machine v3 (`SKILL.md`, 345 lines) and `production/audit/carousel-machine.json`. "Line" means a
SKILL.md line. Sources for the organic rules: ORGANIC-OS.md 7.3 and 7.4.

## 1. The skill's steps on the 16-step pipeline
Carousels and single images are the `still` production family (standards.json `families`): steps 4, 5, 8 and 12 are
`na`; step 3 is the slide copy, step 10 the slide generation, step 11 G-VIS-SLIDE, step 13 G-SET.

| Skill step (lines) | Step | Gate in the ledger | Who |
|---|---|---|---|
| 0 Brand kit, 1 Brief (45 to 61) | 0 | G-BRIEF | Claude, from brain.json, brand-kit.md, style-bible.md and the card. No question round: the card gives the goal (`job`), the belief, the pillar, the ask (`cta_type`, `cta_keyword`), never a free brief |
| 2 Idea score, 3 Format (63 to 112) | 1 | G-IDEA | Claude; the Organic Director checks Content Map fit. The idea is the card's `narrow_product` (ORGANIC-OS 7.2); the 6-test score picks between angles inside it. The "Offer link" test (line 88) becomes "leads to the card's CTA for its job" |
| 4 Story map (114 to 132) | 1 | G-IDEA | The one-sentence argument and one line per story position. No slide copy yet |
| 5 Hook, the cover (134 to 154) | 2 | G-HOOK | `pipeline.py budget` first (the concept frames are the run's first generations, STANDARDS 10); hook-agent in Hook Lab carousel mode, a concept frame per finalist stack, then a fresh grader (section 2) |
| 6 Body copy and self-check (156 to 175) | 3 | G-SCRIPT 85+ | script-agent; fresh cold readers (section 3). The `still` family's step 3 has no G-HUMAN-SPINE (standards.json `step_gate_by_family.still`): the master stack pick is written in the G-HOOK note |
| (no audio, timeline, storyboard, edit) | 4, 5, 8, 12 | none | `pipeline.py step <slug> <post_id> <n> --status na` |
| 8b Continuity plan, one scene line per slide (227 to 234) | 6 | G-PLAN, G-SPEC per slide | visual-planner: `shots/SLnn.spec.yaml` and `qa/carousel-plan.md`; a fresh prompt-reviewer in spec mode |
| 7 Style bible (177 to 212) | 7 | G-HUMAN-LOOK (once per client) | StraightScale: done (STYLE-TOP@v1 on `runs/SS-LIB-STYLE`, section 5). A new client builds its own on its LIB run |
| 8a Setup and cost (216 to 225) | 9 | G-BUDGET | `pipeline.py budget` again once steps 0 to 8 are closed: it re-prices the whole carousel, and step 9 closes only on a G-BUDGET recorded after them (STANDARDS 10) |
| 8c to 8e Cover rounds, slide 2, slides 3 to N (236 to 258) | 10 | G-PROMPT-IMG per slide version | fresh prompt-reviewer; the gate checks every call |
| 8f Fixes, 9.1 to 9.2 copy checks (260 to 275) | 11 | G-ASSETS: G-VIS-SLIDE per slide, G-VIS per concept frame | fresh visual-reviewer (section 7); step 11 closes when every asset's latest version passed its own gate |
| Logo paste (new) | 11 | none (a file step) | `brand_overlay.py` after G-VIS-SLIDE PASS |
| 9.3 to 9.5 Connection, design, critic loop (276 to 286) | 13 | G-SET, G-DIRECTOR | fresh visual-reviewer in set mode replaces the critic loop; then the Organic Director |
| 10 Caption, 11 Package (288 to 304) | 14 | G-HUMAN-FINAL | hub draft; Matan approves on the Content page |
| 12 Measure and learn (306 to 318) | 15 | G-LEARN | the analyst at 72 h and 7 d |

On fail (STANDARDS 9): 3 FIX loops on the copy with new readers every loop, then the owner (G-HUMAN-ESCALATE); 2
prompt loops, then the Organic Director; 3 attempts per slide (an edit pass or a cover round is one attempt), then
G-HUMAN-ESCALATE.

## 2. The hook: Hook Lab in carousel mode (step 2)
Hook Lab has no carousel row (audit). Carousel mode is its static mode (a 2-channel stack: image and headline) applied
to the cover, plus the slide 2 rule. There is no spoken channel.
- **The stack:** the cover scene (one focal object, big and close, the problem where it lives in the business: the
  phone in the deep red case, the empty booking calendar, per the B2B profile in `hook-lab-organic.md`), the cover text
  (an optional label of 6 words or fewer, the headline, an optional subline of 6 words or fewer) and slide 2 (the line
  that pays the cover). Write the cover from the most interesting line in the step 1 story map (keeps line 135); the
  slide copy at step 3 then pays the approved cover. Hook before script is the pipeline's order (AI-VIDEO-PIPELINE 1).
- **Headline: 4 to 10 words** (STANDARDS 6; the skill's "at most 12 words", line 137, is overruled), split into 2 or 3
  lines of about 12 characters; each line is its own text surface of 6 words or fewer (check P6). Readable at 200 px
  wide. Example (the approved 15 Oct cover): label "PËR PRONARËT E BIZNESEVE", headline "7 gjëra që po / të
  kushtojnë klientë / çdo javë", subline "Numëro sa prej tyre i bën."
- **10 stacks** (hook-lab-organic), covering the skill's five variation types (line 138: more controversial, more
  specific, no hype, the founder's words, withholding). The skill's 4 PASS/FAIL gates (lines 139 to 144) stay as a
  pre-filter. Its gate 2 ("a specific number or concrete outcome") with an empty proof bank means a concrete outcome,
  never an invented number. A count of the post's own items ("7 gjëra") is structure, not a claim.
- **Hook Lab's 9 gates, read for a carousel:** 1 the right owner thinks "that's me" from the cover alone; 2 the scene
  and the headline say one thing; 3 the problem is in the scene and in the headline; 4 the cover works at 200 px with
  no caption; 5 the seam: slide 2 pays this cover and would fail under a different one (line 120); 6 a question is
  still open after slide 2; 7 no product, brand name, price or offer on the cover or slide 2; 8 every fact is in
  brain.json; 9 the tone and Meta rules (mock the mistake, never the owner; no "your [condition]"; no guarantees).
- **Grading:** Hook Lab grades and keeps 3 stacks (a master and 2 variants, 2 hook types at least). A fresh grader
  gets only the persona card (AV-01 from the brain, at night, phone in hand, "a carousel appears in your feed") and,
  per stack, the concept frame with its cover text on top at 200 px wide, the cover text and slide 2. G-HOOK passes
  when the master stack is A or A+ on both channels from both graders and the grader gets the topic from slide 2
  alone.
- **Concept frames** (AI-VIDEO-PIPELINE step 2: "Concept frame per finalist, viewed at phone size with the text hook
  on top"; `hook-lab-organic.md` "Concept frames are gated stills"): one per finalist stack, as cheap stills at the
  section 6 settings (`gpt_image_2_5`, 1 credit each). Each serves its own hook Shot Spec (`H-01A` to `H-01C`:
  `format: carousel_slide`, `aspect: "4:5"`, the stack's cover scene, the top 40% a calm dark wall, the bottom-left
  corner calm and empty) and is a hero `still` asset (`pipeline.py asset <slug> <post_id> H-01A --type still --shots
  H-01A --hero`) with STYLE-TOP as its only reference: G-SPEC (`spec-check`, then a fresh prompt-reviewer) and
  G-PROMPT-IMG before the call, G-VIS after (zero defects).
  The model draws no words on it: the stack's cover text is laid on top in code (ImageMagick) for the grader. These
  are the run's first generations, so `pipeline.py budget` runs before them (STANDARDS 10). The master's passed
  concept frame is image 2 of the cover's reference map (section 6), so the cover keeps the scene that was graded.
- **The master pick:** the skill's "human look when one is available" (line 138) is delegated. Claude picks the master
  stack and writes the reason in the G-HOOK note. The `still` family's ledger asks for no G-HUMAN-SPINE (standards.json
  `step_gate_by_family.still`, step 3 is G-SCRIPT only); the owner sees the cover at G-HUMAN-FINAL.
- Record: `pipeline.py gate <slug> <post_id> G-HOOK --status PASS --by "hook-lab + fresh grader" --note "<master>;
  picked because ..."`.

## 3. Slide copy and the fresh cold read (step 3)
- **Kept from the skill:** one idea per slide; a headline of 7 words or fewer on body slides; list items of 5 words or
  fewer; section labels or a counter; a TEST or action line where it fits; the banned words (line 164); read aloud;
  two editing passes. Default 10-slide shape (line 130). The SHORT and DENSE lanes follow STANDARDS 6 (only the turn
  slide breaks its lane; past the DENSE limit, split the slide); a DENSE slide holds separate items of 5 words or
  fewer.
- **Slide count 7 to 12** (STANDARDS 3). Formats the skill sizes outside it are clamped: Myth vs truth and Tool or news
  start at 7; Start here stops at 12.
- **Give the value away.** The what and the why in full, and on a method post the steps too: the reader needs no
  homework (ORGANIC-OS 7.2). The skill's "sell the how only through the ask" (line 161) is not used. The agency is
  named lightly or not at all.
- **Proof:** StraightScale's proof bank has no public entry (IP-01 is internal only). No receipts slide, no result,
  percentage or client number; show the process instead (ORGANIC-OS 7.6). "Proof every 2 to 3 slides" (line 163)
  waits until the brain holds permitted proof.
- **The last slide:** the payoff, then one ask, matching the card's `cta_type` and job (organic.json `cta_types` and
  `jobs`; ORGANIC-OS 6.2): follow, save, send, comment (an answer to a question the post asks), keyword (only a
  keyword live in brain.json; StraightScale today: only ANALIZA), DM, or book. "Book" only on a convert card, and said
  as the keyword path ("comment ANALIZA; the booking button comes in the DM", brand-kit "One path"), never as a link.
  Never a price, a discount, a guarantee or urgency. Say what happens next in plain words. Examples (ti): "Ruaje këtë
  postim." / "Dërgoja një pronari biznesi." / "Na ndiq për pjesën e dytë." / "Shkruaj ANALIZA në komente."
- **Offer posts:** only a hard offer card (`hard_offer: true`: a convert card, about 3% of output, capped by
  organic.json `stage_mix`) is about the one free offer, the free analysis. It says only what brain.json holds (free,
  45 minutes, at the office in Tirana or at the business, no obligation), with the same limits as any ask. No B8 "what
  happens in the analysis" post until decision D3. On every other post the DM carries the offer.
- **The caption is written now**, with the copy, so the same readers and fact check see it (section 8).
- **The copy gate:** Script Lab GRADE with `script-lab-organic.md` and its text-on-screen adapter (18e: each slide is a
  card, read in order). Tests about voice and timing are N/A, with the reason in the report. 100-point score, release
  at 85 or more with no critical fail.
- **The cold read** (fresh agents, never ones that saw the brief or a draft, new readers every loop):
  - Reader 1 gets the persona card and the copy in order ("Slide 1: ...", the caption last). It writes a 5-sentence
    retell and answers the six position tests: what do you want after the cover; does slide 2 pay it; where would you
    stop swiping and why; which slide changed what came before; what do you believe now and what would you do; the
    most confusing slide; would you save, send or follow it.
  - Reader 2 gets slide 2 first and alone (Instagram re-shows an unswiped carousel from slide 2), then slides 3 to N:
    what is this about, and would you keep swiping.
  - Pass: the retell matches the six positions, reader 1 names the want and the turn, reader 2 gets the topic from
    slide 2 alone. A miss rewrites only the failing slides.
- **Facts:** every fact against brain.json and brand-kit.md. Nothing that sounds like a guaranteed outcome; the brand
  kit's Never list holds (no answer-time promise, no claim that we work the client's leads: we build them a system);
  no hype words; no em dashes. No number in a line or on a screen unless it is in brain.json (STANDARDS 6); a count of
  the post's own items ("7 gjëra" on a 7-item post) is structure and must match the slides. An anecdote in the brand's
  voice is a clearly framed POV ("POV: ..."), never stated as something that happened (STANDARDS 7).
- Record: `pipeline.py gate <slug> <post_id> G-SCRIPT --status PASS --by "script-lab gate" --score <n>`, with the
  report and both reads in `runs/<post_id>/qa/script-gate.md`.

## 4. Formats (organic.json ids to the skill's formats)
| organic.json format | Skill format (length) | Ask | StraightScale notes |
|---|---|---|---|
| `carousel_framework` (trust; B3, B4) | Steal my system (8 to 10) or Contrarian plus named framework (10 to 12) | save, or ANALIZA | One step of the Only Choice System per slide (Find, Own, Attract, Convert, Close) |
| `carousel_self_check` (trust, reach, convert; B1, B3) | Self-audit checklist (8 to 10) | save, comment or ANALIZA; book on a convert card | Pairs with the live keyword. PATCHWORK is not live: never ask for it |
| `carousel_mistakes` (reach; B1, B2) | Mistakes list or Count list (7 to 9) | send | "Number 3 costs the most"; one mistake and its fix per slide |
| `carousel_teardown` (trust; B2, B3) | Teardown of a known business (7 to 9) | send | Public observation only; never a real local business mocked by name without permission (brain); never its logo in the art (rule 5) |
| `carousel_comparison` (trust, convert; B5) | Two-sided contrast (8 to 10) or Myth vs truth (7 to 9) | save, or ANALIZA; book on a convert card | A system vs a marketer or another agency for pieces (brain B5) |
| `carousel_opinion` (trust, reach; B7, B1, B2) | Hills I'll die on (8 to 10) | follow, send or comment | Positions from the contrarian vault only (C1 to C5) |
| `carousel_bts` (trust; B7; production `real`) | Start here or a BTS set (7 to 12) | follow | Real photos only. The brain has no real footage yet, so it is not made |
| `image_question` (trust, reach; 1 slide) | One slide, asset type `static` (hero; its visual gate is G-VIS, not G-VIS-SLIDE) | comment (the answer to its question), or save | A real self-check question; one image a week at most (`week_rules`) |
| `image_review_quote` (trust, convert) | One slide | | Needs a real review with permission; the proof bank has none, so it is not made |

Not made now: Win or case study (no permitted proof; B6 is not held), Start here as a founder story (needs real
photos), Tool or news drop (only after its fact and source are in the brain). The ask rotation across the week (line
40) is checked by `organic.py week-check`, not per carousel.

## 5. Look and Shot Specs (steps 6 and 7)
- **Style:** the locked style block in `clients/<slug>/style-bible.md` (its World, Thread, Palette, Type and Frame
  lines) opens every prompt, word for word, except the logo line: the Frame line's "small logo strip bottom left"
  becomes "bottom-left corner calm, dark and empty". The model never draws the logo; the real file is pasted after
  review with `growth-engine/tools/brand_overlay.py` (section 7). Source notes in brackets (such as "Organic OS 7.3")
  are not prompt text, and neither are the Format line (the settings are in section 6) and the Banned line (it goes
  into the negatives). StraightScale colours (brand-kit.md 45, style-bible.md 7 to 10): crimson **#B31217** for the
  highlight rectangles and the arrow button; mark red **#BE0F18** only inside the pasted logo file and the phone case;
  gold **#DD9A10** only for the small counter; ivory #F8F6EF type; charcoal #1F1F1F scene tone. #B31217 is the only
  saturated colour besides the small gold counter (and the phone case). "Tirana after dark"; counter top right;
  register per the brain's voice card ("ti" until D2). The skill's preset (#C8202F, 3:4, counter top left, a logo
  strip drawn by the model; lines 193, 327, 330) is replaced.
- **The style reference:** `STYLE-TOP@v1` (media `e6bc8781-70fa-4450-aa10-989160b20a2e`, role `image_references`):
  the top of the approved 15 Oct cover, registered on `runs/SS-LIB-STYLE` with G-VIS-SHEET PASS (hero, zero defects)
  and G-HUMAN-LOOK PASS (Matan, 15 Oct). The old full cover `90dad300` failed its review (a model-drawn logo, blurred
  side bands) and is never a reference.
- **The thread:** the smartphone in a deep red case (#BE0F18), changing state with the story. Screens show states
  ("a pile of unanswered messages"), never counts or invented numbers, and no real platform logos or names: "the
  inbox", "the phone" (STANDARDS 6; style-bible "Banned"; STORY-FORMATS 6.3). A readable screen is a story-critical
  prop and needs a prop sheet on the LIB run first (none exists yet); otherwise the screen is dark, face down or
  blurred.
- **People** (STANDARDS 7; brain.json D1 interim, verbatim: "AI people are only shown from behind or as clearly staged
  scenes; no AI person is presented as a real client."): no AI face as the subject. An AI business owner is hands, a
  back or a figure at a distance. The StraightScale strategist may face the camera only as the presenter in his
  clearly staged studio set (the whiteboard), AI label on, never as a client, owner or customer. A photoreal person on
  a slide follows STANDARDS 1's photoreal-slide row: `gpt_image_2_5` at 4:5 with the person's approved `gpt_image_2`
  still as a reference (`gpt_image_2` has no 4:5 output).
- **One Shot Spec per slide** (`shots/SL01.spec.yaml` to `SLnn`, VISUAL-QA 2): `format: carousel_slide`, `aspect:
  "4:5"`, `hero: true` on SL01 only; `line_text` = the slide's exact words; `must_read_in_1s`; every string in
  `text_in_image` with its surface and occlusion (label, each headline line, subline, body lines, the counter "n/N",
  the keyword on the last slide); `subjects` and `props` (the phone and its state); `hands: none visible` or a full
  hands block; `style` = the locked block (with the logo line swapped as above); `continuity` with the previous slide
  and its carry-over (phone state, the bridge element); `regions` for every text surface, hand and face, plus a
  `logo-zone` box `[0.0, 0.91, 0.4, 1.0]` of kind `other`; `must_not` with targeted negatives ("no logo or wordmark
  drawn anywhere", "no letters or objects in the bottom-left corner", "no readable words on the phone screen", "no
  borders, side bars or blurred margins"), never a blanket "no text".
- **The carousel plan** (`qa/carousel-plan.md`): the six positions (cover, slide 2, spine, turn, payoff and ask) and the
  continuity plan from line 228: one world, one thread with its state per slide, one frame, one scene line per slide,
  swipe bridges with exact edge positions, the rhythm (close or wide, dark or light) and how the turn breaks it. G-PLAN
  passes when every position has its line and every bridge names both edges.
- Then `pipeline.py spec-check` until clean, and a fresh prompt-reviewer (spec mode) records G-SPEC per slide.

## 6. Prompts and generation (steps 9 and 10)
- **Model** (STANDARDS 1): `gpt_image_2_5`, `aspect_ratio: "4:5"`, `resolution: "2k"`, `quality: "medium"` (1 credit),
  `variant: "flare"`; `count: 1`, except a cover round (`count: 4`, below). Pin them all: the model's defaults are 1k,
  low and an unpinned variant. `quality: "high"` (2.75 credits, STANDARDS 10) only to polish an approved cover. The
  skill's `low` for body slides (lines 218 to 223) and its 3:4 aspect are not used.
- **The prompt card:** VISUAL-QA 4.1's 11 blocks in order, filled with the skill's 6-part template (lines 248 to 254)
  and the DAILY.md pattern: 1 "Instagram carousel slide, portrait 4:5." and the locked style block; 2 the reference map
  ("Image 1 is the style reference: match its type, highlight box, counter, light and grade, not its text or scene.
  Image 2 is the approved cover ..."; on the cover: "Image 2 is the approved concept frame: keep its scene, focal
  object and camera"), then "Slide N of NN. Continue the exact same visual system"; 3 the focal object big and close,
  the phone's state; 4 hands; 5 actions as contact points; 6 props with content; 7 every string in quotes with its
  role, position, size and colour, the accent word in a solid crimson #B31217 rectangle, the small gold #DD9A10
  counter "n/N" top right, then "Spell exactly, letter by letter:" with every word that has ë or ç; 8 the setting, the
  calm text zone ("the top 40% is a dark calm wall"), and: "Bottom-left corner (the lowest 9% of the height, the left
  40% of the width): calm, dark, empty background with nothing in it: no logo, no letters, no objects (a logo is added
  later)."; on slides 1 to N-1 "bottom right a small crimson #B31217 round button with a white arrow", none on the
  last; 9 the camera (close or wide per the plan), 4:5, text inside a 4% margin, the bridge edge; 10 the carry-over;
  11 targeted negatives: "Render all text exactly as written, letter for letter. No other words, letters or numbers
  anywhere, including screens, signs, papers and labels. Crimson #B31217 is the only saturated colour besides the
  small gold counter and the deep red phone case. No logos, wordmarks, app names or app screens anywhere. Full-bleed
  photograph edge to edge: no borders, no side bars, no blurred margins." DAILY.md's prompt pattern has the same
  colours.
- **The model never draws the logo** (brand-kit: real files only). The skill's "logo, in prompts" (line 330) and its
  bottom logo strip are gone; `brand_overlay.py` pastes the real file after review (section 7).
- **References, same files, same order, same roles on every retake:** cover: STYLE-TOP, the master's concept frame.
  Slide 2: STYLE-TOP, the approved cover. Slides 3 to N: STYLE-TOP, the cover, slide 2; a story post with tight
  continuity goes in order and adds the previous approved slide as image 4. A reference is the job id (never a URL)
  of a version that already passed its own review (G-VIS-SLIDE; G-VIS for the concept frame): register it with
  `pipeline.py media <slug> <post_id> SL01@v<n> --id <job id> --file <file>`. The one exception is an edit pass, which
  takes the failed version itself as its only reference (section 7).
- **Register and review each slide:** `pipeline.py asset <slug> <post_id> SL01 --type cover --shots SL01 --hero`
  (slides 2 to N: `--type slide`), then `pipeline.py prompt ... SL01 --file prompts/SL01.v1.txt --media
  e6bc8781-70fa-4450-aa10-989160b20a2e:image_references <concept frame job id>:image_references`, then a fresh
  prompt-reviewer (G-PROMPT-IMG, P1 to P12); its JSON goes in with `pipeline.py record`. 2 prompt loops, then the
  Organic Director.
- **Order:** the cover, then its G-VIS-SLIDE PASS; slide 2 alone, then its PASS (the two anchors, lines 242 and 245);
  then slides 3 to N with `generate_image_batch` (12 requests at most, each exactly one registered slide version with
  its own prompt and media list; poll with `jobs_wait`; a failed request becomes a new version, never a blind retry).
- **Cover rounds** (STANDARDS 10): one `generate_image` call with `count: 4` is one round: one version of SL01 and one
  attempt, 3 rounds at most, then G-HUMAN-ESCALATE. Register the four job ids and files on that version (`pipeline.py
  media ... SL01@v<n> --id <the four job ids> --file <the four files>`). The producer never picks: a fresh
  visual-reviewer gets a contact sheet of the four at 200 px wide, names the strongest cover at phone size (V19) and
  runs the full review on that one (section 7). The skill's "2 to 4 rounds" (line 241) is replaced.
- **Budget** (STANDARDS 10): `pipeline.py budget <slug> <post_id> --planned <USD> --balance <live Atlas
  balance, USD>` (it adds 25% and checks the client's monthly USD cap in brain.json). It runs before the concept frames (step
  2), again at step 9 to re-price the whole carousel (STANDARDS 10's carousel price, which includes the 3 concept frames),
  and again before any later batch when the last G-BUDGET is over 24 h old. A cost preflight (`get_cost: true`) works
  on one `generate_image` call, not inside a batch. Check the balance again right before the batch: credits are
  shared. The brand kit's "carousels up to 30 Higgsfield credits" a week is checked by hand against the week's plan
  until the owner says which limit wins (3 carousels at their floor of about 13 are 39, over it: STORY-FORMATS 5.6);
  the gate checks the monthly cap.

## 7. Review, the logo, the set (steps 11 and 13)
- **G-VIS-SLIDE per slide:** `python3 growth-engine/tools/vqa_crops.py image <file> --run <slug>/<post_id> --asset
  SLnn@v<n>` (full image, 3x3 tiles at 2x, region crops, the 200 px thumbnail; OCR is a second opinion only), then a
  fresh visual-reviewer runs V1 to V26 and opens every file in `must_open`. It reads every letter (V9), checks the
  logo zone is empty (V11), 4:5 with text inside the 4% margin (V18), the cover headline at 200 px (V19), the style
  against style-bible.md and the reference (V21), no drawn logo (V24), the AI label rule (V26). The cover is a hero
  asset: zero defects of any severity. Other slides: zero critical, zero major, 2 minor at most. `pipeline.py record`.
  On a cover round, the crops are made from the image the reviewer picked from the contact sheet, and the report names
  it.
- **Fix routes** (VISUAL-QA 5.5 and the skill's 8f, in VISUAL-QA's order). Each fix is a new version (`pipeline.py
  asset ... SLnn --type slide` again; the cover `--type cover --hero`) with its own fresh review:
  1. **Edit pass** for a local defect (a wrong or missing letter, a speck or stray mark, letters or an object in the
     logo corner, a second saturated colour in one spot). This is the skill's edit pass (line 262), now allowed by the
     gate (STANDARDS 1 "Edit pass"): `pipeline.py prompt ... SLnn --file prompts/SLnn.v<n>.txt --media <failed
     version's job id>:edit_source`, passed in the call as `role: "image_references"` and as the only image; the
     skill's narrow edit prompt ("Keep this image exactly the same: scene, layout, colours and type style. Change only
     ...", line 262) with the word spelled letter by letter, at the section 6 settings and the quality the slide was
     made at; a fresh G-PROMPT-IMG before the call and a fresh G-VIS-SLIDE after. One attempt. Specks next
     to letters may get a local paint-out with the background colour instead, logged in `qa.md` and saved as a new
     version (`media --file`); a painted version that becomes a reference is uploaded first and its media id
     registered with `media --id`.
  2. **Regenerate** with the corrected prompt for a structural defect (a wrong count of items, a small object, type
     drift, the wrong scene or camera): the skill's known-failure line written in ("exactly FIVE", "big and close to
     the camera", "crimson #B31217 is the only saturated colour besides the small gold counter and the deep red phone
     case", the style block and anchors restored, the word spelled out and the line shortened), same references in
     the same order.
  3. **Simplify** after two fails (VISUAL-QA 5.5 route 3).
  4. 3 attempts per slide, every generation counted (the skill's "2 retakes plus edit passes", line 271, is
     replaced). Then `pipeline.py` queues G-HUMAN-ESCALATE with the best version and its report.
- **The logo, after G-VIS-SLIDE PASS:** `python3 growth-engine/tools/brand_overlay.py <in> <out> --client <slug>`
  (default `wordmark-white`, bottom left, 27% of the width, margins 6.5% and 4%). It refuses a busy or bright corner
  (exit 1): never force it; make a new version with a stronger corner rule. Add the pasted file to the same version
  with `pipeline.py media ... --file <out>`. Export: `convert in.png -resize 1080x1350! -strip -quality 90 out.jpg`
  (JPEG, under 8 MB). The skill's 1080x1440 export (lines 300, 310) is replaced.
- **G-SET, the whole set:** the skill's Step 9 connection and design checks stay; the fresh visual-reviewer in set mode
  runs them instead of the critic loop (line 286). Packet: the final pasted slides, a contact sheet in order and a 3x3
  grid with the account's recent posts when available (ImageMagick `montage`). Checks C1 and on: one world (light,
  grade, type voices, frame); the thread moves through its planned states; the bridges line up at the stated edges;
  the rhythm changes and the turn looks different; slide 2 works alone; no slide could swap with another; counters
  run 1/N to N/N; one ask, on the last slide only, and no arrow there; crimson #B31217 the only saturated colour
  besides the gold counter and the phone case; the same real logo file at the same place and size on every slide; the
  cover fits the grid. `covers` lists every slide version.
- **G-DIRECTOR:** the Organic Director checks the post does the card's job (belief, CTA) and is the best version of
  the idea: `pipeline.py gate <slug> <post_id> G-DIRECTOR --status PASS --by organic-director --note ...`.

## 8. Caption, ship, learn (steps 14 and 15)
- **Caption:** the first line restates the hook in other words with the search words (never slide 1 word for word,
  line 291); on a keyword post the keyword comes first ("Shkruaj ANALIZA në komente ..."); a body built from the last
  slide plus a plain list of the post's value, past 400 characters if it stays useful, under 2,200; one ask, the same
  as the last slide; 3 to 5 specific hashtags; at most one emoji; no em dashes. Alt text: one short line per slide in
  Albanian.
- **Hub draft** (DAILY.md section 4, status `draft`, 4:5 media): notes say "Native Albanian read needed (slide text
  and caption)" and "AI label: on" when a slide shows a photoreal AI person or a photoreal AI scene (the StraightScale
  film-still look is one), per STANDARDS 7 (D1 decides whether to extend it). An AI person is never a client and
  never carries a result. The skill's posting checklist (lines 307 to 312) is replaced: no posting from the app with
  music (the hub publishes after approval), the keyword funnel must be live (`analiza`), nothing posts before
  G-HUMAN-FINAL.
- **G-LEARN** (the analyst at 72 h and 7 d): the card's job metric (saves per reach for trust, sends per reach for
  reach, qualified DMs for convert), plus follows, profile visits and keyword comments; slide 2 against the cover
  (slide 2 should hold at least half the cover's likes; under a third, slide 2 is not paying the cover) once per-slide
  insights are connected (D6). A post at 2x the baseline is a template candidate and at 3x a template
  (organic.json `templates`; the skill's single 2x rule, line 318, is replaced). Lessons go to
  `clients/<slug>/analytics/learnings.md`, the cover's result to the client's Hook Library.

## 9. What this adapter overrides in the skill, and why
| Skill (line) | Organic rule | Why |
|---|---|---|
| Self-graded hook on 4 gates, 5 variants (137 to 144) | Hook Lab carousel mode, 10 stacks, a fresh grader; the 4 gates as a pre-filter | Issue 14; STANDARDS 12 |
| Cover hooks judged as text (134 to 154) | A concept frame per finalist stack (1 credit each), graded at 200 px with the cover text on top | AI-VIDEO-PIPELINE step 2 |
| Headline at most 12 words (137) | 4 to 10 words, each line 6 words or fewer | STANDARDS 6; P6 |
| 8-question self-check, no cold read (167 to 175) | Script Lab gate 85+ and two fresh cold readers | Issue 14; STANDARDS 9 |
| Two self-run critics (286) | Fresh visual-reviewer: G-VIS-SLIDE per slide, G-SET for the set | VISUAL-QA 10.7; STANDARDS 12 |
| 3:4 at 1080x1440 (193, 217, 300, 310) | 4:5 at 1080x1350 | STANDARDS 3: the publishing API refuses 3:4 |
| Low for body slides, high for a cover polish (218 to 223) | Medium on every slide; high only to polish an approved cover | STANDARDS 1 |
| 4 cover options a round, 2 to 4 rounds (241) | Rounds of 4 kept: one round is one version and one attempt, 3 rounds at most; a fresh reviewer picks | STANDARDS 9 and 10; VISUAL-QA 1 |
| 2 retakes plus edit passes (271) | 3 attempts in all (an edit pass is one, role `edit_source`), then the owner | STANDARDS 1 and 9 |
| Logo drawn by the model (193, 330) | Bottom-left corner left empty; the real file pasted after review | brand-kit: real files only |
| Accent #C8202F, counter top left (193, 327) | Crimson #B31217 accent, gold counter top right, #BE0F18 only in the logo file and the phone case | brain.json, brand-kit.md, style-bible.md |
| "Book" ask, the free 45-minute meeting as the ask (40, 101, 332) | The card's one ask for its job; "book" only on a convert card, said as the ANALIZA path; the free analysis only on a hard offer card | ORGANIC-OS 6.2; organic.json `cta_types` |
| Sell the how only through the ask (161) | Method posts give the steps away | ORGANIC-OS 7.2 |
| 2x baseline makes a template (318) | 2x candidate, 3x template | organic.json `templates` |
| Post from the app with quiet music (310) | The hub publishes after G-HUMAN-FINAL | CLAUDE.md: nothing posts without approval |
| No AI label rule | STANDARDS 7 on every post: label on for a photoreal AI person or scene | Issue 12 |
| "GPT Image 2" in the prose (3, 17, 34, 214) | `gpt_image_2_5` for every slide; a photoreal person uses the approved `gpt_image_2` still as a reference | STANDARDS 1 (`gpt_image_2` has no 4:5) |
