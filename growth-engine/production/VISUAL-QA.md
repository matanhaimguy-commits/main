> Saved verbatim from the owner's spec (15 Oct 2026). In this repo the files it names are:
> `AI-VIDEO-PIPELINE.md` = `growth-engine/production/AI-VIDEO-PIPELINE.md`; `ORGANIC-GROWTH-OS.md` = `growth-engine/ORGANIC-OS.md`.
> Implementation map: `growth-engine/production/README.md`.

# Visual QA and Hard Gates
### Spec for the content generation system: shot specs, prompt review, cold visual reviewers, mandatory storyboards, and enforcement (v1, 15 Oct 2026)

**Who this is for:** the Claude Code session that builds and runs the content machine (organic posts now, paid ads later).
**What it adds:** a quality layer on top of `AI-VIDEO-PIPELINE.md` (the 16-step order) and `ORGANIC-GROWTH-OS.md` (what to make and why). Read those first. This file covers **how every image, storyboard, prompt, video take, motion render and carousel slide gets checked before the next step is allowed to run.**

**Applies to every format:** realistic talking heads, UGC, podcast clips, animation, song ads, drama, motion graphics, carousels, static images and ads.

---

## 0. Why this exists: the failures we just shipped

These came out of real generations on 15 Oct 2026. Every one passed through the pipeline because nobody independent looked at the image against what the script needed.

| # | What happened | Where | Root cause | Which gate would have caught it |
|---|---|---|---|---|
| F1 | **Writing drawn on the presenter's hand.** The last letters of "PËRSËRITET" and "NUMËR" run over his fingers and wrist instead of stopping at the board. | Whiteboard still (talking-head reference) | The prompt asked for text on the board and a hand near the text, but never said which is in front. Image models paint text as a layer with no depth logic. | Prompt Review (no occlusion rule) and Image Review (hands + text zoom) |
| F2 | **The whiteboard is physically wrong.** The marker tray sits halfway down, and a second board continues below it. | Same still | Nothing in the prompt described the board's structure; nobody checked object structure. | Image Review (object structure) |
| F3 | **Scissors don't cut the hair.** The blades are open above the strand, the lower blade passes behind the fingers, and the "head" under the hair is a featureless pink dome. | Storyboard panel 1 (haircut) | Action described as a noun ("scissors cutting hair"), not as contact ("the closed blades meet across the strand, 2 cm below her fingers"). No physics check. | Prompt Review (action as contact points) and Image Review (action physics) |
| F4 | **The diploma is empty.** She receives a rolled certificate, then hangs a gold frame with nothing inside. Two more empty gold frames hang in the background of other shots. | Storyboards and stills (diploma story) | Our blanket negative "no text" plus a generic "diploma" made the model leave every frame blank. The story depends on that prop. | Prompt Review (story-critical prop has no content spec) and Image Review (prop content) |
| F5 | **The phone screen shows one blank speech bubble.** It reads as a placeholder, not a message. | Character panel | Same cause as F4. | Same as F4 |
| F6 | **No storyboard was generated** for a video, and the video prompt didn't describe or reference the images it was given. | Claude Code video run | The skills' storyboard step and H3 prompt card were skipped. Nothing stopped the generation call. | Hard gate: no video call without an approved storyboard and a passed prompt review (section 9) |

**Why it matters:** references feed everything downstream. A bad still becomes a bad sheet, a bad storyboard and a bad video, with every retake paid for. A 10-second review of a still is the cheapest fix in the whole machine.

---

## 1. The principle: generators never grade their own work

Every visual step has two roles:

- **Producer:** writes the prompt and generates.
- **Reviewer:** a separate, fresh agent that never saw the producer's reasoning. It gets a fixed packet: the Shot Spec, the script lines, the reference images and the output. It judges the output **against the Shot Spec, not against the prompt**, because the prompt itself may be wrong.

This is the same idea as Script Lab's cold read (a fresh agent with only the persona card and the lines). We now apply it to pictures.

Three reviewers do almost all the work:
1. **Prompt Reviewer:** before any generation. Is the prompt complete, unambiguous and correct for the model?
2. **Visual Reviewer:** after every still, sheet, storyboard, carousel slide and static. Does it show exactly what the shot needs, with no defects?
3. **Take Reviewer:** after every video clip and every motion render. Does the motion hold up frame by frame?

On top sits the **Director** (from the Organic Growth OS), who reviews the assembled piece for story and performance, not pixels.

---

## 2. The Shot Spec: the single source of truth for every picture

**Why:** a reviewer can only check what is written down. "Woman hangs her diploma" can't be checked. "The diploma is visible inside the frame: cream paper, gold seal bottom centre, the heading DIPLOMË" can.

**When:** created in pipeline step 6 (visual plan), one per shot. Carousels get one per slide. Statics get one per image. Sheets and storyboards reference the Shot Specs they serve.

**Who writes it:** the visual planner agent, from the script line table and the look bible.

**Schema** (`shots/<shot_id>.spec.yaml`):

```yaml
shot_id: S90-SEQ03-SH2
post_id: SS-2026-11-W1-03
format: animation_3d          # realistic_photo | ugc | podcast | animation_3d | claymation | 2d | song | drama | motion | carousel_slide | static
script_lines: [L14, L15]      # from the Script Lab line table
line_text: "Dhe kur e vari diplomën në mur, e kuptova."   # exact spoken or sung words over this shot
story_purpose: "Proof moment: the certificate makes her new skill real"   # why this shot exists
must_read_in_1s: "She proudly hangs her diploma"   # what a sound-off viewer must understand in one look

subjects:
  - id: CH-MIRA
    ref: sheets/CH-MIRA_v2.png        # locked sheet
    state: "hair in messy bun, cream cardigan, pink top, jeans"   # continuity state at this moment
    pose: "standing, back three-quarters to camera, both arms raised"
    expression: "proud, small smile, eyes on the frame"
    eyeline: "the frame on the wall"

hands:                             # REQUIRED whenever hands are visible
  - who: CH-MIRA
    left: "holds the left edge of the frame, fingers on the outside of the moulding"
    right: "holds the right edge of the frame"
    contact: "both hands touch only the frame, not the certificate"
    count_check: "two hands, five fingers each, both attached to CH-MIRA"

props:
  - id: PR-DIPLOMA
    story_critical: true            # true = must be clearly visible and correct
    ref: props/PR-DIPLOMA_v1.png    # prop sheet (see 4.4)
    state: "framed, behind glass, hanging level"
    content: "cream certificate paper, thin gold ornamental border, round gold foil seal with a red ribbon at bottom centre, heading 'DIPLOMË' in dark serif capitals at top, three lines of small decorative script under it (illegible is fine)"
    size_in_frame: "about 30% of frame height, clearly readable as a certificate"

text_in_image:                      # every piece of visible text, or "none"
  - string: "DIPLOMË"
    surface: "the certificate inside the frame"
    must_be_exact: true
    occlusion: "nothing covers any letter; hands stay on the frame edges"

action_physics:                     # REQUIRED for any action shot
  - "the frame hangs on one visible nail; its top edge is level"
  - "her arms reach up naturally; shoulders raised; no stretched limbs"

setting:
  ref: sets/SET-SALON_v1.png
  details: "small salon wall beside the mirror; black styling chair below right"
  background_rule: "no other picture frames in shot unless they show a picture"

camera:
  framing: "medium-wide, from behind her right shoulder"
  angle: "eye level"
  aspect: "9:16"
  safe_zones: "top 14% and bottom 35% kept free of key content (captions and UI)"

continuity:
  previous_shot: S90-SEQ03-SH1
  carry_over: ["cardigan sleeves pushed to forearms", "frame in hand from SH1"]

style: "Pixar-style 3D, warm daylight, as in style bible v2"
must_not: ["empty frame", "certificate without seal", "extra people", "text on walls", "logos"]
hero: false                         # true for frame 1, storyboard image 1, thumbnails, carousel covers: zero tolerance
```

**Rules for writing Shot Specs:**
1. **Actions are written as contact points, not nouns.** Not "scissors cutting hair" but "the two blades are closing across the strand, about 2 cm below her fingers; cut hair ends visible at the blade line; the strand runs from a real head with a face turned away".
2. **Every visible hand gets a line:** what it holds, where it touches, and what it must not cover.
3. **Every story-critical prop gets a content line.** Empty is never the default (see 4.4).
4. **Every piece of text gets the exact string, the surface, and an occlusion rule.**
5. **Background objects that could read as props get a rule:** empty frames, screens, signs, books and labels either show neutral content or are left out.
6. **One clear "must read in 1 second" line.** If you can't write it, the shot isn't designed yet.

---

## 3. Gate map: where every check sits

Numbers refer to the 16 pipeline steps in `AI-VIDEO-PIPELINE.md`.

| Pipeline step | Gate | Reviewer | Blocks |
|---|---|---|---|
| 6 Visual plan | **G-SPEC:** every shot has a complete Shot Spec | Prompt Reviewer (spec mode) | Any image prompt |
| 7 Look bible | **G-PROMPT-IMG** on each sheet prompt | Prompt Reviewer | Image generation |
| 7 Look bible | **G-VIS-SHEET** on each character, set and prop sheet | Visual Reviewer | Storyboards |
| 7 Look bible | **G-HUMAN-LOOK:** you approve the look bible once per client or series | Human | Storyboards |
| 8 Storyboards | **G-PROMPT-IMG** on each storyboard prompt | Prompt Reviewer | Storyboard generation |
| 8 Storyboards | **G-VIS-BOARD** on each storyboard (panel by panel) | Visual Reviewer | Video prompts |
| 8 Storyboards | **G-CONTINUITY** across all storyboards of the piece | Visual Reviewer (set mode) | Video prompts |
| 10 Video | **G-PROMPT-VID** on each video prompt | Prompt Reviewer | `generate_video` call |
| 11 Take QA | **G-TAKE** on each clip (frames + sync + words) | Take Reviewer | Edit |
| 12 to 13 Edit, Final | **G-FINAL** on the cut (sound-off, frames every 1.5 s, text, loudness) | Take Reviewer (final mode) + Director | Approval queue |
| Carousels | G-SPEC, G-PROMPT-IMG, G-VIS-SLIDE per slide, G-SET (whole carousel) | Prompt + Visual Reviewers | Packaging |
| Motion graphics | G-SPEC, G-MOTION-FRAMES per render, G-FINAL | Take Reviewer (motion mode) | Approval queue |

**A gate is passed only when its report file exists with `status: PASS` for that exact asset version** (section 9).

---

## 4. Prompt standards (what the Prompt Reviewer enforces)

### 4.1 Still image prompt card (stills, sheets, storyboard panels, carousel slides)
Every image prompt has these blocks, in this order:

1. **Format line:** medium and look ("Candid iPhone 15 Pro photo, vertical 9:16" or "Pixar-style 3D render, warm daylight" or the locked style block for carousels).
2. **Reference map:** one line per attached image, in upload order. "Image 1 is the storyboard layout. Image 2 is Mira: keep her exact face, bun, cardigan. Image 3 is the salon set." Never attach an image without saying what it is for.
3. **Subject and pose:** who, where in frame, pose, expression, eyeline.
4. **Hands block:** for every visible hand, what it holds, where it touches, what it must not cover. If no hands should show, say so.
5. **Action as contact points** (from the Shot Spec).
6. **Props with content:** every story-critical prop with its full content description.
7. **Text block:** exact strings in quotes, the surface, the position, letter case, and the occlusion rule ("the presenter's hand is below and to the right of the last word; no letter touches his skin"). If no text: "no text anywhere except [listed]".
8. **Setting and background:** named objects only; background people mid-action for realistic scenes; the background rule for frames, screens and signs.
9. **Camera:** framing, angle, lens feel, 9:16, safe zones.
10. **Continuity carry-over** from the previous shot.
11. **Specific negatives:** targeted ("no empty picture frames", "no second marker tray", "no text on skin"), never a blanket "no text" that kills story props.

### 4.2 Video prompt card (MiniMax H3, from hub G1, now enforced)
1. Realism line or style block.
2. **Reference line per media by token**, matching the upload order exactly: `<<<image_1>>>` is the storyboard for this sequence; `<<<image_2>>>` is Mira's sheet; `<<<audio_1>>>` is her voice slice.
3. **"Follow the storyboard in `<<<image_1>>>` shot by shot":** for each panel, state what it shows and how it moves.
4. Hands and props line for every shot, including what stays in hand between shots.
5. Timeline: "Shot 1, 0.0 to 3.2 s: ..." with one action per shot, timed to words.
6. Background action in every shot.
7. Lip-sync block, including "use `<<<audio_1>>>` exactly, word for word, at the same timing".
8. Negatives: no captions, no logos, no morphing, no objects appearing or disappearing, no text except [listed props].
9. Duration matches the audio rule in the production-standards file.

### 4.3 Prompt Reviewer checklist (G-PROMPT-IMG and G-PROMPT-VID)
The reviewer reads the Shot Spec(s), the prompt, and the list of attached files. It answers each item PASS or FAIL with evidence:

| # | Check | Fails when |
|---|---|---|
| P1 | **Coverage** | Any Shot Spec element (subject, hand, prop, text, action, setting, camera) is missing from the prompt |
| P2 | **Reference map** | An attached image isn't described; the order in the prompt doesn't match the upload order; the storyboard isn't image 1 for video |
| P3 | **Hands** | A visible hand has no instruction, or the instruction conflicts with a prop or text |
| P4 | **Action physics** | An action is a noun ("cutting", "writing") with no contact points |
| P5 | **Story props filled** | A story-critical prop has no content description, or a negative ("no text") would empty it |
| P6 | **Text exact and placed** | Text without exact quotes, surface, position or occlusion rule; strings over about 6 words per surface (split or simplify) |
| P7 | **Background traps** | Frames, screens, signs or books in the scene with no content rule |
| P8 | **Contradictions** | Two instructions that can't both be true ("hands empty" and "holds the marker") |
| P9 | **Continuity** | State differs from the previous shot's carry-over without a reason |
| P10 | **Model rules** | Breaks the production-standards file (model, resolution, aspect, `declined_preset_id`, durations, one speaker per clip) |
| P11 | **Ambiguity** | Any word a model could read two ways ("board" = whiteboard or wooden board) |
| P12 | **Known failures** | Matches a pattern in the Failure Library (section 8) without its listed fix |

**Output:** `PASS`, or `FAIL` plus a **corrected prompt**. The producer uses the corrected prompt or fixes the listed items; the reviewer checks again. **Maximum 2 prompt loops**, then the Director decides.

### 4.4 Story-critical props: the "no empty props" rule
**Why:** F4 and F5. Models leave props blank when they are unsure or told "no text".

**How:**
1. In step 7, every prop marked `story_critical` gets its own **prop sheet**: one clean image of the prop in its key states (rolled, open, framed; phone screen with the exact UI). The prop sheet is reviewed like a character sheet.
2. The prop sheet is attached as a reference in every shot where the prop appears.
3. Content is described concretely: materials, layout, seal, colours, and any exact text (short, 1 to 3 words).
4. Where exact text is unreliable, use **design that reads without words**: a certificate is recognisable from paper, border, seal and ribbon; a chat is recognisable from alternating grey and green bubbles with lines of grey text.
5. Background frames and screens: either fill them (neutral art, a calendar, a plant) or leave them out. **An empty frame on a wall is a defect.**

---

## 5. Visual Reviewer (G-VIS-SHEET, G-VIS-BOARD, G-VIS-SLIDE, statics)

### 5.1 How it looks at an image (method)
A single glance misses small defects: F1 was only obvious when zoomed. Every review uses three views, produced by a script before the reviewer starts:
1. **Full image** at native resolution.
2. **Tiles:** a 3x3 grid of crops, each upscaled 2x.
3. **Critical crops:** a 2x crop around every region the Shot Spec names: each hand, each story prop, each text surface, each face. The planner adds approximate boxes to the spec (`regions:`); if missing, use the tiles.

For storyboards, each panel is split out and reviewed as its own image, then the board is reviewed as a sequence.

For text, also run OCR (e.g. tesseract with the right language pack) as a second opinion. **The reviewer still reads letter by letter.** OCR often misreads diacritics (ë, ç), so it can flag but never pass text on its own.

### 5.2 The checklist (every image)
Each item gets PASS, FAIL or N/A, with a severity and a short evidence note pointing to the crop.

**A. Story fit**
- V1: It shows the `must_read_in_1s` moment. A stranger with the sound off would understand it.
- V2: It matches the script line it sits under (right moment, right emotion, right action).
- V3: Nothing in it contradicts the script or the brand facts.

**B. Anatomy and hands**
- V4: Correct count of hands, arms, fingers (5 per hand), legs; every hand attached to the right body.
- V5: Hands do exactly what the spec says; grip makes sense (scissors held through the handles, marker held by the barrel).
- V6: Faces: no melting, doubled features, mismatched eyes, wrong teeth; expression matches the spec.

**C. Action physics**
- V7: The action is physically real: blades closing on the strand, marker tip touching the board where the next letter would start, frame hanging from a nail, cup on the table not floating.
- V8: Objects have correct structure: a whiteboard has one frame and one tray at the bottom; chairs have legs on the floor; doors have hinges on one side.

**D. Text**
- V9: Every string matches the spec exactly, letter by letter, including diacritics and punctuation.
- V10: **Occlusion is correct:** text sits on its surface; nothing that should be in front (hand, arm, marker) is painted under or over letters. No text on skin, clothes, or air.
- V11: No unwanted text anywhere (gibberish signs, fake logos, labels).

**E. Props**
- V12: Every story-critical prop is present, visible, the right size, and **has its content** (no empty diploma, blank screen, empty frame).
- V13: Props match the prop sheet (same colour, shape, design).
- V14: No unexplained props (a phone appearing, a third scissors).

**F. Identity and continuity**
- V15: Each character matches their locked sheet (face, hair, outfit, body shape, accessories such as rings).
- V16: State matches the shot's continuity (sleeves, held objects, hair) and the previous shot.
- V17: Setting matches the set sheet.

**G. Composition and format**
- V18: 9:16 (or the slide's 3:4 / 4:5); key content inside the safe zones.
- V19: The subject is readable at phone size. Run a thumbnail check at about 200 px wide for hero images and carousel covers.
- V20: Background is alive where the format needs it (realistic scenes): people mid-action, not posed.

**H. Style and quality**
- V21: Style matches the style bible (render look, lighting, palette).
- V22: Realistic images: real skin texture, no plastic look, phone-photo realism as specified.
- V23: No artefacts: smears, seams, duplicated objects, warped straight lines, half-rendered areas.

**I. Policy and brand**
- V24: No real brand logos or trademarked characters; no real people unless approved.
- V25: Meta rules: no side-by-side before and after; no "your [condition]"; nothing that shames.
- V26: AI-person disclosure rules followed for the account.

### 5.3 Severity and pass rule
| Severity | Meaning | Examples |
|---|---|---|
| **Critical** | Breaks the story or looks broken | Text on a hand (F1), empty diploma (F4), scissors not cutting (F3), extra limb, wrong person, gibberish in the hook frame |
| **Major** | A viewer would notice; weakens trust | Board structure wrong (F2), empty background frames, prop off-model, background frozen and posed |
| **Minor** | Only visible zoomed; doesn't affect story | Slight texture smear in a corner, small lighting mismatch |

- **Hero assets** (frame 1, storyboard image 1, character and prop sheets, carousel covers, ad thumbnails): **PASS only with zero defects of any severity.**
- **Everything else: PASS with zero critical and zero major, and at most 2 minors** (each logged).

### 5.4 Report format (`qa/<asset_id>.v<n>.review.json`)
```json
{
  "asset_id": "SB-SEQ03",
  "version": 2,
  "gate": "G-VIS-BOARD",
  "reviewer": "visual-reviewer (fresh agent)",
  "status": "FAIL",
  "hero": false,
  "checks": [
    {"id": "V12", "result": "FAIL", "severity": "critical", "region": "panel 4, frame", "evidence": "Gold frame on the wall is empty. Spec PR-DIPLOMA requires cream certificate with seal and 'DIPLOMË'."},
    {"id": "V7",  "result": "FAIL", "severity": "critical", "region": "panel 1, blades", "evidence": "Blades are open above the strand and pass behind her index finger; no cut line at the blades."},
    {"id": "V6",  "result": "FAIL", "severity": "major", "region": "panel 1, head", "evidence": "The head under the hair is a smooth pink dome with no ear, face or neck."}
  ],
  "fix": {
    "route": "regenerate",
    "prompt_changes": [
      "Attach props/PR-DIPLOMA_v1.png and describe its content in panel 4.",
      "Panel 1: 'the two blades are closing across the strand, 2 cm below her fingers; cut ends visible at the blade line; the client's head is seen from behind with an ear and neck visible'."
    ]
  }
}
```

### 5.5 What happens on FAIL (fix routes, in order)
1. **Edit pass** for local defects (wrong letters, empty prop, extra finger, unwanted text): edit the image with itself as the reference and a narrow instruction. It's cheap and keeps everything else.
2. **Regenerate with the corrected prompt** for structural defects (wrong action, wrong pose, physics).
3. **Simplify the shot** if it fails twice. Change the composition so the hard thing isn't needed: hand below the text instead of beside it; show the framed diploma already on the wall, then the hand adjusting it.
4. **Escalate** after 3 attempts on one asset: the best version goes to the human queue with the review report. Never pass a known critical defect silently.

Every FAIL adds a line to the Failure Library (section 8).

---

## 6. Storyboards: mandatory, and reviewed twice

**Why:** a storyboard is the strongest control we have over H3. It fixes framing, composition, who is where and what happens in each shot. F6 happened because this step was skipped.

**Hard rules:**
1. **Every video sequence with more than one shot, and every talking or singing clip, has a storyboard.** There is no exception for "simple" shots.
2. The storyboard is **image 1** in the H3 references for that sequence.
3. Layout: 2 to 3 panels on a 16:9 canvas of 9:16 panels, or a 2x2 grid on 4:5. One panel per shot, in time order.
4. Built from the approved sheets as references (characters, set, props), never from text alone.
5. **The hook storyboard is made first** and checked at phone size with the text hook laid on it, sound off.

**Two reviews:**
- **G-VIS-BOARD (per panel):** the full section 5 checklist on each panel against its Shot Spec.
- **G-CONTINUITY (set mode, across all boards of the piece):** same faces and outfits throughout; props keep their state (rolled diploma becomes framed diploma, never blank); screen direction and geography stay consistent; the story reads in order with no missing beat when you flick through the panels with the script lines under them.

**Human:** for ads, you approve the storyboard set. For organic at volume, the reviewers' PASS is enough, and you see the boards in the daily approval queue only if a reviewer flagged an escalation. Hook storyboards always go to you.

---

## 7. Video takes and motion renders (G-TAKE, G-MOTION-FRAMES, G-FINAL)

### 7.1 Take Reviewer for generated video (every H3 / Kling clip)
**Inputs:** the storyboard, the Shot Specs, the audio slice, the clip.
**Preparation script:** extract frames at 1 per second (2 per second for clips under 6 s) plus the first and last 0.1 s; build contact sheets; run the drift check and Whisper word check from hub G6.

**Checks:**
- T1: Each shot matches its storyboard panel (framing, who, action).
- T2: Identity holds across the clip; no face drift between frames.
- T3: Hands and props: nothing appears, vanishes or changes hands without a reason; story props keep their content.
- T4: No morphing, melting, flicker, or duplicated people.
- T5: No generated text, captions or gibberish signs.
- T6: Background is alive where specified.
- T7: Lip-sync: lag measured; only one mouth moves per voice; drift steps sit in pauses (fixable) or inside words (retake).
- T8: Words: every scripted word present (Whisper against the script).
- T9: The action reads (the scissors actually close; the frame actually goes on the wall).

**Pass rule:** zero critical, zero major; drift fixable in the edit. **Retake only what the edit can't cut around.** Maximum 2 retakes per clip, then simplify the shot or escalate.

### 7.2 Motion graphics (code-rendered: HyperFrames, Canvas, Remotion and similar)
There is no image model here, so the defects are different: overlapping elements, spelling, timing and contrast.

- **Shot Spec per scene** (same schema; `format: motion`): text strings, layout positions, entry and exit timing tied to VO words, brand colours.
- **Prompt Reviewer equivalent:** reviews the scene plan and the code's text constants against the spec and the approved script, before the full render.
- **G-MOTION-FRAMES:** render preview frames every 0.5 s plus every transition's start, middle and end. The Take Reviewer (motion mode) checks:
  - M1: every word spelled exactly (letter by letter, diacritics);
  - M2: no element overlaps another unless designed; nothing clipped at the edges;
  - M3: text inside safe zones; contrast 4.5:1 or more;
  - M4: each text appears on or just before its spoken word (timing table from the VO word timestamps);
  - M5: motion in the first second; hook text on screen by 0.3 s;
  - M6: brand colours and fonts from the brand kit only;
  - M7: any generated image used inside the motion piece passed G-VIS on its own.
- Fix in code, re-render the preview, review again. Final render only after PASS.

### 7.3 Final cut (G-FINAL), every format
- Frames every 1.5 s plus every cut: no defect that slipped through.
- Sound-off watch: the story and the hook read without audio.
- Captions: exact text, timing, safe zones.
- Transcript of the final mix against the script.
- Loudness and true peak to the production-standards numbers.
- **Director's pass:** does it do the job in the Post Card (belief, CTA), and is it the best version of the idea?

---

## 8. The Failure Library (so the system gets better every week)

**Why:** most image failures repeat. Writing them down turns each failure into a rule the Prompt Reviewer enforces before the next generation.

**File:** `qa/failure-library.md`, one entry per pattern:

```
FL-01 Text over hands
Seen: 15 Oct 2026, whiteboard still (F1)
Pattern: a hand near written text gets letters painted over the skin
Prevention (prompt): say which is in front; keep the hand below or beside the last word with clear space; "no letter touches his hand"
Detection (review): 2x crop of every hand next to text
Fix route: edit pass to remove letters from skin; if repeated, move the hand away from the text
```

**Seed entries from today:**

| ID | Pattern | Prevention | Detection |
|---|---|---|---|
| FL-01 | Text painted over hands or arms | Explicit occlusion rule; hand away from the text | Hand + text crops |
| FL-02 | Object structure wrong (two trays, double board, warped frames) | Describe the object's structure in one line | Tile review, V8 |
| FL-03 | Action not happening (blades not closing, pen not touching) | Write actions as contact points | V7 physics crop |
| FL-04 | Empty story props (diploma, certificate, screen, frame) | Prop sheet + content line; no blanket "no text" | V12 |
| FL-05 | Empty background frames and screens | Background rule: fill or remove | V12, V11 |
| FL-06 | Faceless or blob anatomy in close-ups (pink dome under the hair) | Name the visible body parts ("ear and neck visible, face turned away") | V6 face and head crop |
| FL-07 | Video made without a storyboard; prompt ignores the attached images | Hard gate (section 9) | Ledger check |
| FL-08 | Phone vanishes mid-gesture (StraightScale round 5) | Hands and props line per shot | T3 |
| FL-09 | Frozen background in video | Background action line per shot | T6 |
| FL-10 | Gibberish banners and signs in H3 | "No text" plus "plain surfaces" for walls and banners | T5 |
| FL-11 | Cloned character in one panel; floating person (Pillow Pool) | One instance per character named; physics line | V4, V7 |
| FL-12 | "Same pose, different man" when mixing models in adjacent shots (drama) | Same model and references for adjacent close-ups | G-CONTINUITY |

The Prompt Reviewer's check P12 reads this file on every run.

---

## 9. Enforcement: making the gates impossible to skip

Rules in a document get skipped under pressure. F6 proves it. The gates must be **enforced by the system**, not remembered by the agent.

### 9.1 The gate ledger
One file per post: `runs/<post_id>/ledger.json`. Each asset version gets an entry:

```json
{
  "asset_id": "SEQ03-video",
  "version": 1,
  "type": "video_clip",
  "depends_on": ["SB-SEQ03@v2", "CH-MIRA@v2", "SET-SALON@v1", "PR-DIPLOMA@v1", "SLICE-SEQ03@v1"],
  "prompt_sha256": "9f1c...e2",
  "gates": {
    "G-PROMPT-VID": {"status": "PASS", "report": "qa/SEQ03-video.v1.prompt.json"},
    "G-TAKE": {"status": "PENDING"}
  }
}
```

### 9.2 A blocking hook in Claude Code
Claude Code supports **PreToolUse hooks**: a script that runs before a tool call and can block it. Use one hook on every generation tool (`mcp__Higgs__generate_image`, `generate_image_batch`, `generate_video`, `generate_video_batch`, and the ElevenLabs generation tools).

The hook script:
1. Reads the tool input (prompt text, attached media).
2. Hashes the prompt and finds the matching ledger entry.
3. **Blocks the call** with a clear message unless:
   - the asset's Shot Spec(s) exist and passed G-SPEC;
   - the prompt hash has a G-PROMPT PASS;
   - for video: a storyboard is attached as image 1, and that storyboard's version has G-VIS-BOARD and G-CONTINUITY PASS;
   - every attached reference has a passed G-VIS report for that exact version;
   - the budget check for this run has passed.
4. Allows the call and logs it otherwise.

This makes F6 impossible: a video call with no approved storyboard simply doesn't run.

### 9.3 Reviewer independence, in practice
- Reviewers run as **separate subagents** (the Agent tool), started fresh for each review. A new reviewer starts on every retry, so it doesn't anchor on the last version.
- The reviewer gets **only the packet:** Shot Spec(s), script lines, reference files, the output files and crops, the checklist, and the Failure Library. It never gets the producer's reasoning or the producer's own opinion of the image.
- The reviewer must **open every image and crop itself** (Read the files). A report that cites no crops is invalid.
- Reviewers return JSON in the report format; the orchestrator writes it to the ledger. Only the orchestrator changes gate status.

### 9.4 Human checkpoints (kept few, batched daily)
- Look bible per client or series (once).
- Hook storyboards.
- Any escalated asset (3 failed attempts).
- Final approval before anything is posted or launched.

---

## 10. Format playbooks

The same gates apply everywhere; each format adds its own checks.

### 10.1 Realistic talking head and UGC (AI people)
- **Spec extras:** reference photo for identity; phone-photo realism line; background people mid-action; props in hand per shot.
- **Extra checks:** skin texture real (no plastic); identity matches the reference; eyeline; marker, phone and paper held correctly; any writing on boards follows the text and occlusion rules.
- **Common traps:** FL-01, FL-02, FL-08, FL-09.

### 10.2 Podcast clips
- **Spec extras:** master two-shot first; start frames made only from the master; mics, headphones and mugs fixed per character.
- **Extra checks:** both people match the master; mic positions consistent; one mouth per clip; reaction shots exist.

### 10.3 Animation (3D, clay, 2D, talking objects)
- **Spec extras:** model sheet per character with proportions; inside-the-body shots need orientation (which way is up, what organ).
- **Extra checks:** on-model in every panel; the talking mouth is at least a third of the frame; style consistent across panels.

### 10.4 Song ads
- **Spec extras:** which line is sung over the shot; the singer's mouth visible for sung lines.
- **Extra checks:** only the singer mouths words; the picture changes every 1.5 to 3.5 s; THE PICTURE appears in the chorus shots.

### 10.5 Drama
- **Spec extras:** shot size, 30-degree rule, continuity-state column, geography.
- **Extra checks:** G-CONTINUITY across adjacent shots made by different models (FL-12).

### 10.6 Motion graphics
Section 7.2. Code-level review before render; frame review after.

### 10.7 Carousels
- **Spec per slide**, plus a carousel-level spec: the story positions (cover, slide 2, spine, turn, payoff and ask) and the continuity thread.
- **Gates:**
  - G-PROMPT-IMG per slide (style block present and unchanged, text exact, positions).
  - G-VIS-SLIDE per slide with letter-by-letter text checks and the 200 px thumbnail test for the cover.
  - **G-SET:** the whole set as a grid and in order. One visual world, the swipe bridges line up, the turn looks different, slide 2 works alone, no slide could swap with another.
- **Covers are hero assets:** zero defects.
- The carousel-machine's own Step 9 checks stay; the fresh-agent reviewer replaces its self-run critic loop.

### 10.8 Static images and ads
- Same as a carousel slide, plus the Hook Lab gates for the image and headline, and Meta policy checks (V25).
- Ads later run the identical pipeline. Only the CTA, the end card and the policy profile change.

---

## 11. Worked example: today's images, reviewed and fixed

### 11.1 Whiteboard presenter (F1, F2)
**Review result:** FAIL.
- **V10, critical:** the letters of "PËRSËRITET" and "NUMËR" run onto his fingers and wrist.
- **V8, major:** the marker tray sits mid-board and a second board continues below it.
- **V5, minor:** he points at line 2 with the cap end of the marker.

**Corrected prompt (key lines):**
> Candid iPhone 15 Pro photo, vertical 9:16, held at chest height by a colleague. Image 1 is the presenter: keep his exact face, beard, charcoal denim overshirt over a black T-shirt.
> He stands left of a single wall-mounted whiteboard with one aluminium frame and one marker tray along its bottom edge only.
> **Text block:** on the whiteboard, handwritten in black marker capitals:
> - top left: "CILËSI", crossed out with one red line;
> - below it, three numbered lines: "1. VLERËSIMET E KËQIJA", "2. ANKESA QË PËRSËRITET", "3. E KUNDËRTA + NUMËR".
>
> Each line ends at least 20 cm before the board's right edge.
> **Hands block:** his right hand holds a black marker by the barrel, tip forward. The tip touches the board just under the end of line 2. His hand and wrist are **below** line 2 and **right of** line 3, with clear white board between his skin and every letter. **No letter touches his hand or sleeve.** His left arm hangs relaxed.
> Background: a colleague walks past the glass wall carrying a laptop. Real skin texture, natural daylight.
> Negatives: no text anywhere else; no second whiteboard; no marker tray mid-board; no text on skin.

### 11.2 Haircut close-up (F3)
**Review result:** FAIL.
- **V7, critical:** the blades are open above the strand and do not cut; the lower blade passes behind her fingers.
- **V6, major:** the head under the hair is a featureless dome.

**Corrected Shot Spec action lines:**
> The stylist's left hand holds a 3 cm strand between index and middle finger, about 10 cm from the ends. Her right hand holds the scissors through both handles. The two blades are **closing across the strand 2 cm below her fingers**, with cut hair tips falling. The client's head is seen from behind and slightly to the side: ear, neck and the top of the cape visible.

### 11.3 Diploma (F4, F5)
**Review result:** FAIL.
- **V12, critical:** the frame being hung is empty.
- **V12, major:** two more empty gold frames hang in the background of the salon shots.
- **V12, major:** the phone shows one blank bubble.

**Fix:**
1. Make prop sheet **PR-DIPLOMA**, showing it rolled with a ribbon, open, and framed. Content: cream paper, gold border, round gold foil seal with a red ribbon at the bottom centre, heading "DIPLOMË", three lines of small decorative script. Review it like a character sheet.
2. Attach it to every diploma shot and describe its state.
3. Set background rule: "the salon wall has one mirror and one framed print of a flower; no empty frames".
4. Phone prop sheet **PR-PHONE-CHAT**: a WhatsApp-style chat, two grey and two green bubbles with short grey text lines, a contact avatar circle at the top.

---

## 12. What to build, in order

1. **Production-standards file** (from `AI-VIDEO-PIPELINE.md` section 5), which all skills and reviewers read.
2. **Shot Spec schema and writer** (section 2) in step 6 of the pipeline; a G-SPEC check.
3. **Crop and tile script** (section 5.1): full, 3x3 at 2x, region crops, panel splitter, OCR second opinion.
4. **Prompt Reviewer agent** with checklist P1 to P12 and the prompt cards (section 4).
5. **Visual Reviewer agent** with V1 to V26, severity and pass rules, JSON reports (section 5).
6. **Prop sheets** in the look bible step, with the "no empty props" rule (4.4).
7. **Storyboard step made mandatory**, plus the continuity set review (section 6).
8. **Take Reviewer agent** for video, and motion mode for code renders (section 7).
9. **Gate ledger** per post and the **PreToolUse blocking hook** on every generation tool (section 9).
10. **Failure Library** seeded with FL-01 to FL-12; P12 reads it every run (section 8).
11. **Human approval queue**, batched daily (9.4).
12. Hook the reviewers into carousel-machine (replacing its self-critic), the song, animation, podcast and drama skills, and motion. Ads reuse the same system later.

---

## 13. Reviewer agent prompts (paste-ready)

### 13.1 Prompt Reviewer
```
You are the Prompt Reviewer. You check generation prompts BEFORE any credits are spent.
You get: the Shot Spec(s) for this asset, the prompt text, the list of attached files in upload order,
the production-standards file, and the Failure Library.
You never see the producer's reasoning.
For each check P1 to P12, answer PASS or FAIL with a one-line quote from the prompt or spec as evidence.
If anything fails, write a corrected prompt that fixes every failed item and changes nothing else.
Rules:
- Every subject, hand, prop, text and action in the spec must appear in the prompt.
- Actions must be written as contact points.
- Story-critical props must have content.
- Text must be in quotes with surface, position and an occlusion rule.
- Attached images must be described in order; for video, the storyboard is image 1.
Return JSON: {status, checks[], corrected_prompt}.
```

### 13.2 Visual Reviewer
```
You are the Visual Reviewer. You have never seen how this image was made.
You get: the Shot Spec, the script lines this image serves, the locked reference sheets,
the image, a 3x3 tile set at 2x, and region crops for every hand, prop, text surface and face.
Open every file yourself before judging.
Judge ONLY against the Shot Spec and the sheets, not against what the prompt intended.
Run checks V1 to V26. For each, give PASS, FAIL or N/A, a severity (critical, major, minor),
the region, and evidence a person could verify by looking at the named crop.
Read every piece of text letter by letter, including diacritics.
Hero assets pass only with zero defects. Others pass with zero critical, zero major and at most 2 minor.
If it fails, name the fix route (edit, regenerate, simplify) and the exact prompt changes.
Return JSON in the report format.
```

### 13.3 Take Reviewer
```
You are the Take Reviewer. You check a generated video clip or motion render before the edit.
You get: the storyboard, the Shot Specs, the audio slice and its transcript,
frame contact sheets (1 per second, plus first and last frames), the drift report, and the Whisper word check.
Run T1 to T9 for generated video, or M1 to M7 for motion renders.
Report each with evidence by frame time.
Say whether each defect can be fixed in the edit (cut, offset, crop) or needs a retake.
Return JSON: {status, checks[], edit_fixes[], retake_needed, retake_prompt_changes[]}.

```

