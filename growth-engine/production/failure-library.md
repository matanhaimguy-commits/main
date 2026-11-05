# Failure Library

The patterns that keep breaking our pictures, each with its prevention (what the prompt must say), its detection
(what the reviewer must look at) and its fix route. VISUAL-QA.md section 8 (the spec names this file `qa/failure-library.md`).

- **Who reads it:** the Prompt Reviewer on every run (check P12: a prompt that matches a pattern without its prevention
  fails), the Visual and Take Reviewers (detection), the visual planner when writing Shot Specs.
- **Who writes it:** every FAIL is logged automatically to `failure-log.csv` by `pipeline.py record`. The Organic
  Director reads that log in the Monday memo: a failure that is not yet a pattern here becomes a new FL entry the
  same week (next number, dated, with where it was seen). A pattern seen 3 times despite its prevention gets a
  stronger prevention or a simpler default shot.
- **Edit pass:** a fix route the gate allows as STANDARDS 1 "Edit pass" says: the asset's own previous version as the
  single image reference (role `edit_source`) and a narrow instruction. It is a new version, counts as one attempt and
  gets its own full review. Any other reference goes into a regenerate, not an edit pass.
- **Format:** one entry per pattern, in this exact shape.

---

### FL-01 Text over hands
- Seen: 15 Oct 2026, whiteboard still (F1): the last letters of "PËRSËRITET" and "NUMËR" ran over the presenter's fingers and wrist.
- Pattern: a hand near written text gets letters painted over the skin. Image models paint text as a layer with no depth.
- Prevention (prompt): say which is in front; keep the hand below or beside the last word with clear space; write "no letter touches his hand or sleeve"; end every line well before the surface edge.
- Detection (review): a 2x crop of every hand next to text (Shot Spec region kind `hand` and `text`); V10.
- Fix route: edit pass to remove letters from skin; if it repeats, move the hand away from the text (simplify).

### FL-02 Object structure wrong
- Seen: 15 Oct 2026, same whiteboard still (F2): marker tray halfway down, a second board continuing below it.
- Pattern: double boards, two trays, warped frames, chairs with floating legs, doors hinged on both sides.
- Prevention (prompt): describe the object's structure in one line ("a single wall-mounted whiteboard with one aluminium frame and one marker tray along its bottom edge only").
- Detection (review): tile review; V8.
- Fix route: regenerate with the structure line; if it repeats, frame the object tighter so less structure shows.

### FL-03 Action not happening
- Seen: 15 Oct 2026, haircut storyboard panel 1 (F3): blades open above the strand, lower blade behind the fingers.
- Pattern: an action written as a noun ("scissors cutting hair", "writing on the board") comes back posed, not happening.
- Prevention (prompt): write actions as contact points: "the two blades are closing across the strand, 2 cm below her fingers; cut tips falling at the blade line".
- Detection (review): physics crop of the action region; V7 (stills), T9 (video).
- Fix route: regenerate with contact points; then simplify (show the moment just after: the cut strand in her hand).

### FL-04 Empty story props
- Seen: 15 Oct 2026, diploma story (F4): rolled certificate, then an empty gold frame on the wall.
- Pattern: a story-critical prop (diploma, certificate, screen, frame, letter, sign) comes back blank because the prompt said "no text" or gave no content.
- Prevention (prompt): a prop sheet for every story-critical prop, attached in every shot it appears; a content line (materials, layout, seal, colours, 1 to 3 exact words); targeted negatives ("no text on walls") never a blanket "no text". `pipeline.py spec-check` blocks a blanket "no text" next to a story prop.
- Detection (review): V12, V13.
- Fix route: edit pass with the content line as the instruction (the image's own previous version is the only reference); if the prop still reads wrong, regenerate with the content line and the prop sheet attached.

### FL-05 Empty background frames and screens
- Seen: 15 Oct 2026, salon shots: two empty gold frames on the back wall.
- Pattern: frames, screens, signs and books in the background read as placeholders.
- Prevention (prompt): a background rule per set: fill them (a framed flower print, a calendar, a plant) or leave them out.
- Detection (review): V12, V11.
- Fix route: edit pass (fill or remove); add the rule to the set sheet so it never comes back.

### FL-06 Faceless or blob anatomy in close-ups
- Seen: 15 Oct 2026, haircut panel 1: the head under the hair was a featureless pink dome.
- Pattern: a body part at the edge of a close-up loses its features.
- Prevention (prompt): name the visible body parts ("seen from behind and slightly to the side: ear, neck and the top of the cape visible").
- Detection (review): face and head crop; V6.
- Fix route: regenerate with the named parts; or reframe so the part is fully in or fully out.

### FL-07 Video without a storyboard; prompt ignores the attached images
- Seen: 15 Oct 2026, a Claude Code video run (F6).
- Pattern: the storyboard step and the H3 prompt card were skipped; the video prompt never said what each image was.
- Prevention: the hard gate. `.claude/hooks/generation_gate.py` blocks a talking or multi-shot clip unless image 1 is a storyboard with G-VIS-BOARD and G-CONTINUITY PASS, and the prompt's reference map was reviewed (P2).
- Detection: ledger check (`pipeline.py status`).
- Fix route: make the storyboard; it can't be skipped.

### FL-08 Phone vanishes mid-gesture
- Seen: Oct 2026, StraightScale round 5 UGC ad (U2).
- Pattern: a prop in hand with no instruction gets dropped, swapped or made to vanish during a gesture.
- Prevention (prompt): a hands and props line in every shot, including what stays in hand between shots; an object the script doesn't need is not in the still at all.
- Detection (review): T3 on the frame contact sheet.
- Fix route: cut around it if the edit can; else retake with the hands line.

### FL-09 Frozen background in video
- Seen: Oct 2026, StraightScale round 5 UGC ad: everyone but the speaker frozen.
- Pattern: H3 freezes everything the prompt doesn't move.
- Prevention (prompt): a background action line in every shot: 2 or 3 named people doing named actions; stills made with the background already mid-action (a posed background stays frozen). `spec-check` blocks a realistic Shot Spec without `background_action`.
- Detection (review): T6; V20 on the start still.
- Fix route: retake with the background line; or cut tighter on the speaker.

### FL-10 Gibberish banners and signs in H3
- Seen: Oct 2026, several H3 takes.
- Pattern: walls, banners and screens fill with fake letters.
- Prevention (prompt): "no captions, no text, no readable screens" plus "plain surfaces" for walls and banners; story text only on named props.
- Detection (review): T5 (video), V11 (stills).
- Fix route: crop or cover in the edit if small; retake if it sits in the subject area.

### FL-11 Cloned character in one panel; floating person
- Seen: Pillow Pool song storyboards (before the storyboard gate existed).
- Pattern: the same character appears twice in a panel; people float above floors and seats.
- Prevention (prompt): name each character once with "one instance"; a physics line ("both feet on the floor", "seated on the chair, weight on the seat").
- Detection (review): V4, V7.
- Fix route: regenerate the panel; simplify the crowd.

### FL-12 "Same pose, different man" across models
- Seen: drama ads, adjacent close-ups made by different models.
- Pattern: mixing models (or references) in adjacent shots changes the face.
- Prevention: same model and same references in the same order for adjacent close-ups; podcast start frames only from the one master two-shot.
- Detection (review): G-CONTINUITY across the boards; T2 across clips.
- Fix route: regenerate the odd shot from the master references.

### FL-13 Model-drawn logo
- Seen: 15 Oct 2026, StraightScale: the style reference `STYLE@v1` (SS-LIB-STYLE, G-VIS-SHEET, V24 major: the mark and wordmark were redrawn, not the real file) and the carousel drafts whose prompts asked the model for the logo strip (the old full cover `90dad300` failed its review for it).
- Pattern: a prompt that asks for the client's logo gets a lookalike: wrong shape, wrong red, wrong type. Image models can't copy a mark, and brand-kit.md says real files only.
- Prevention (prompt): the prompt never asks for the logo. It leaves the bottom-left corner calm, dark and empty ("bottom-left corner calm, dark and empty: no logo, no text there"). After the review the real file is pasted with `growth-engine/tools/brand_overlay.py <in> <out> --client <slug>` (it refuses a busy or bright corner).
- Detection (review): V24 on a 2x crop of the logo zone (a Shot Spec region on the bottom-left corner), compared with the real file in `clients/<slug>/brand/`.
- Fix route: an edit pass (STANDARDS 1; the failed version as the single `edit_source` reference) that clears the bottom-left corner to the calm dark background; the result is a new version with its own review, then `brand_overlay.py` pastes the real file. If the corner can't be cleaned, regenerate with the corner left empty.

---

## How to add a pattern
```
FL-<next number> <short name>
Seen: <date>, <client/post/asset>, <what happened>
Pattern: <the general failure>
Prevention (prompt): <the exact words or rule that prevents it>
Detection (review): <the crop or check that catches it>
Fix route: <edit pass | regenerate | simplify | retake | cut in the edit>
```
