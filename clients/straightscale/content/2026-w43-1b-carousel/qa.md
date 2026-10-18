# 2026-w43-1b-carousel · QA

- [x] Made with GPT Image 2.5 (Higgsfield), 4:5 at 2k, the w43 carousel cover as style reference; exported 1080x1350 JPEG.
- [x] Every letter read at full size (ë, ç, apostrophes). Two stray specks removed by an edit pass (slide 4 above "rezervuan", slide 6 beside the ë of "të").
- [x] Facts only from the brand kit; no numbers, results, clients or prices. One ask.
- [ ] **Native Albanian read** of the image text and the caption.

## Logo fix (18 Oct, edits only, 0 credits)
- v3: the drawn logo removed from all 7 slides and the real file pasted at one box ([98,1233,393,1288]) on every slide
  (`qa/v3_edit.py`). Fresh reviews: slides 2 to 7 PASS (pre-existing minors only), G-SET PASS; the cover FAILED on
  its swipe arrow sitting 19 px above the logo line (`qa/SL01.v3.review.json`).
- v4 cover: the arrow moved 20 px down onto the logo line, the gap refilled (`qa/v4_cover_edit.py`). Fresh hero
  review PASS with zero defects (`qa/SL01.v4.review.json`); G-SET v4 PASS with one pre-existing minor (slide 5's
  kicker starts 20 px left) (`qa/SET.v4.review.json`).
- In the hub (item 5, still a draft): cover v4 + slides 2 to 7 v3, `hosted.json` updated.
