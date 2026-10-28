# Look-bible packet for the evaluator, SS-EN-SONG-01 "Maya's quilt" (28 Oct 2026)

For the fresh evaluator before the main session decides G-HUMAN-LOOK. Producer notes only: no grades of my own.
Every sheet below has its image, its Shot Spec and its fresh visual review. "Waived" means the main session waived
those minors (delegated by Matan, plan 28 Oct); the reviewer's FAIL stays on the ledger (hero zero-defect rule).

| Sheet | Version | Image | Spec | Review | Reviewer verdict | Main session decision |
|---|---|---|---|---|---|---|
| CH-MAYA | v1 | `assets/sheets/CH-MAYA.v1.png` | `shots/SHEET-CH-MAYA.spec.yaml` | `qa/CH-MAYA.v1.review.json` | FAIL, 2 minor | Locked, minors waived |
| PR-SCRAPS | v1 | `assets/sheets/PR-SCRAPS.v1.png` | `shots/SHEET-PR-SCRAPS.spec.yaml` | `qa/PR-SCRAPS.v1.review.json` | PASS | Locked |
| PR-CLOTH | v1 | `assets/sheets/PR-CLOTH.v1.png` | `shots/SHEET-PR-CLOTH.spec.yaml` | `qa/PR-CLOTH.v1.review.json` | FAIL, 2 minor | Locked, minors waived |
| PR-ORGANIZER | v2 | `assets/sheets/PR-ORGANIZER.v2.png` | `shots/SHEET-PR-ORGANIZER.spec.yaml` | `qa/PR-ORGANIZER.v2.review.json` | FAIL, 4 minor | v3 failed on a major, so v2 is locked with its minors waived (the main session's rule) |
| SET-FRIEND | v1 | `assets/sheets/SET-FRIEND.v1.png` | `shots/SHEET-SET-FRIEND.spec.yaml` | `qa/SET-FRIEND.v1.review.json` | FAIL, 2 minor (layout only) | Open: the main session decides (waive or retake) |
| CH-FRIEND | v1 | `assets/sheets/CH-FRIEND.v1.png` | `shots/SHEET-CH-FRIEND.spec.yaml` (now the v2 spec) | `qa/CH-FRIEND.v1.review.json` | FAIL, 2 major (seated panel) | Open: v2 not generated (prompt loop limit, see below) |
| SET-OFFICE | none | | `qa/retired/SHEET-SET-OFFICE.spec.yaml` | `qa/r5/`, `qa/r6/SHEET-SET-OFFICE.spec.json` | new spec failed G-SPEC twice | Fallback: no set sheet; office shots use the plain ivory paper backdrop |

Not locked, for reference: PR-ORGANIZER v3 (`assets/sheets/PR-ORGANIZER.v3.png`, `qa/PR-ORGANIZER.v3.review.json`:
2 major, the state A April pockets are still tall cylinders; 3 minor).

## Waived minors

- **CH-MAYA v1:** V5: the needle hand hides most of the needle in the fist; it is not a clean thumb-and-index pinch.
  V23: the bottom row fades out in a feathered edge about 2% from the bottom. Clip prompts must state a clean
  thumb-and-index needle pinch.
- **PR-CLOTH v1:** V14: the pile has eight bubbles, not nine. V21: the labels look printed, not stitched. Clip
  prompts must state nine bubbles and stitched lettering.
- **PR-ORGANIZER v2:** V12: the state A April pockets are tall cylinders; state B and all March pockets are shallow
  and slanted. V14: the state B band runs a few pixels past both felt edges. V17: muted blazers, repeated faces.
  V18: copies 46% wide (spec 43%), gap 3.5%, edges inside the 4% margin. Clip prompts must state the shallow, slanted
  April pockets and the band inside the felt edges.

## Open for the main session

- **SET-FRIEND v1:** V18 and V19 only: the organizer is larger than the spec boxes (about 91% wide) and the shelf is
  wider and lower. Text, counts (8 + 8 clients), one linen and the clay look pass. Waive (and the shots follow the
  delivered layout) or one retake ($0.047).
- **CH-FRIEND:** spec fixed and G-SPEC PASS (`qa/r5/SHEET-CH-FRIEND.spec.json`). The v2 edit prompt failed three
  fresh reviews in this session (`qa/r5/`, `qa/r6/CH-FRIEND.v2.prompt.json`), each on a different new point; the
  last corrected prompt is in `qa/r6/CH-FRIEND.v2.prompt.json`. The pipeline's loop limit (2) is passed, so the
  Organic Director or the main session decides: take that corrected prompt to one more review, simplify, or escalate.
  The standing views of v1 are usable for SH09; SH08 and SH22 need the seated panel.
