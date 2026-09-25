# QA NOTES — batch-01

## Images (P4; local 800 px proof copies inspected with the Read tool; full-res in the Higgsfield workspace)

| id | render px | aspect ok | qa | notes | repair_of |
|---|---|---|---|---|---|
| C1-V1 | 2048×2048 | True | pass | All 8 manifest strings exact. Minor: CTA label renders white, not Ink; faint illegible marks in planner squares. Laptop matches product reference. First submission passed element ids as medias -> 404 'Media input not found' (no job, no charge); resubmitted with source job ids. / transport: sandbox c | None |
| C1-V2 | 1856×2304 | True | pass | All 7 messages plus '6:42', 'market crew', avatars D and M exact; apostrophes curly. Generic chat chrome, slate bubbles, no brand. / transport: sandbox curl -> identify -> Pillow thumbnail -> AVIF (adaptive q) -> md5 -> base64 -w76 split stdout/stderr; local base64 -d, md5 match, Pillow -> JPEG q92. | None |
| C1-V3 | 1856×2304 | True | pass | No text, logos, people or product. Receipt 'two pencil lines' detail faint/ambiguous at proof size: operator to confirm on the full-res rawUrl. / transport: sandbox curl -> identify -> Pillow thumbnail -> AVIF (adaptive q) -> md5 -> base64 -w76 split stdout/stderr; local base64 -d, md5 match, Pillow | None |
| C2-V1 | 1856×2304 | True | pass | All 8 strings exact; chart one line climbing, one flat. Minor: CTA label white, not Ink. First submission with element id -> 404 (no job); resubmitted with product source job. / transport: sandbox curl -> identify -> Pillow thumbnail -> AVIF (adaptive q) -> md5 -> base64 -w76 split stdout/stderr; lo | None |
| C2-V2 | 1856×2304 | True | pass (post-fixed) | Round-2 re-render 848aea81 failed (see attempts). Post-fixed the file on record (562421f6): all five tried lines now carry one continuous thin grey strikethrough end to end; proof line uniformly mid-grey; all 13 strings exact and unchanged; generic chrome, no brand. Unfixed version kept as images/C2 | d460ce21-aedf-491e-899b-d8167b2f608f |
| C2-V3 | 2048×2048 | True | pass | All 4 post lines exact, lowercase kept; icons without counts; no name/handle. / transport: sandbox curl -> identify -> Pillow thumbnail -> AVIF (adaptive q) -> md5 -> base64 -w76 split stdout/stderr; local base64 -d, md5 match, Pillow -> JPEG q92. Deviation: proof long side 720px instead of 800px q7 | None |
| C3-V1 | 2048×2048 | True | pass | All 5 strings exact; blank badge, keys and mug present. Minor: subhead reads near-black rather than Pine. First submission with element id -> 404 (no job); resubmitted with product source job. / transport: sandbox curl -> identify -> Pillow thumbnail -> AVIF (adaptive q) -> md5 -> base64 -w76 split  | None |
| C3-V2 | 1856×2304 | True | pass (post-fixed) | Round-2 re-render 9afff7da failed (duplicated proof line). Post-fixed the original 9bf55f43: steering-wheel emblem removed (hub now plain dark, no logo anywhere); all 5 strings exact. Residual cosmetic: the render shows a visibly wide space in 'guessed  product' inside the text box (render artefact, | None |
| C3-V3 | 2048×2048 | True | pass | PASS on repair. Original 0cabf9d1 rendered 'overherrd'. Repair 1710a8e3 (same text, spelling emphasised): 'five years of “when i'm ready.” one sentence overheard in the break room changed it.' exact, curly quotes and apostrophe correct. local_file = repair render. / transport: sandbox curl -> identi | 0cabf9d1-62f3-4842-92ca-4eb848f27329 |
| C4-V1 | 1856×2304 | True | pass | All 14 strings exact; row labels in small caps (allowed). Minor: CTA label white, not Ink. / transport: sandbox curl -> identify -> Pillow thumbnail -> AVIF (adaptive q) -> md5 -> base64 -w76 split stdout/stderr; local base64 -d, md5 match, Pillow -> JPEG q92. Deviation: proof long side 720px instea | None |
| C4-V2 | 2048×2048 | True | pass | All 8 strings exact ('11:47', search query, headline, items 1-2, curly-quoted docs line, attribution, 'Store owner: in your name.'). Generic UI, no brand. / transport: sandbox curl -> identify -> Pillow thumbnail -> AVIF (adaptive q) -> md5 -> base64 -w76 split stdout/stderr; local base64 -d, md5 ma | None |
| C4-V3 | 2048×2048 | True | pass | Headline 'Paid to have an online store built, then locked out of it' and standfirst exact (curly apostrophe in builder's). Blank masthead rule, grey byline bar, no publication name/logo; receipts illegible, folder unlabeled, laptop closed without logo, plain mug; a phone lies on the desk (screen dar | None |
| C5-V1 | 2048×2048 | True | pass | All 10 strings exact: 4-line hook on sticky note, subhead, 3 icon body lines (calendar, stairs, key), proof line with curly quotes, CTA 'Live, not stuck'. Laptop matches product reference. Minor: proof line rendered light on the Pine strip rather than Ink 75%; CTA label white rather than Ink; tally  | None |
| C5-V2 | 2048×2048 | True | pass | All 7 strings exact (3-line post card on pale blue-grey, 4 replies incl. CTA 'saving this. new goal: live, not stuck'). Every name and avatar scribbled out; generic heart/comment/share icons with no counts; no brand. / transport: sandbox curl -> Pillow thumbnail -> AVIF (adaptive q) -> md5 -> base64 | None |
| C5-V3 | 1856×2304 | True | pass | Night home desk, open silver laptop with blurred grey settings form, tally-mark sticky note, mug, notebook, pen; no people, no logo visible, no readable text at proof size. Operator: confirm at full res that the notebook scribbles and screen UI stay illegible. / transport: sandbox curl -> Pillow thu | None |

images credits used: 40 · balance after: 1629.84

## Video C1 (P5)

```
{
 "shots": [
  {
   "k": 1,
   "beat": "hook (H1) + lead",
   "job_id": "02ffd78e-bbd1-4dc3-9f04-8a0a6919c76d",
   "rawUrl": "https://d8j0ntlcm91z4.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/hf_20260925_014109_02ffd78e-bbd1-4dc3-9f04-8a0a6919c76d.mp4",
   "duration_s": 15.072,
   "requested_s": 15,
   "probe": "720x1280, 24 fps, h264 + native audio, 8,723,572 bytes",
   "spoken_line": "I have three online stores I haven't touched in years. Built, ready to be loaded. Meanwhile the shop's marketing has slowed down so much. I built one myself, then ended it. I was dealing with a lot.",
   "words": 36,
   "transcript": "I have three online stores I haven't touched in years. Built, ready to be loaded. Meanwhile, the shop's marketing has slowed down so much. I built one myself, then ended it. I was dealing with a lot.",
   "transcript_small_en": "I have three online stores I haven't touched in years, built, ready to be loaded. Meanwhile, the shop's marketing has slowed down so much. I built one myself, then ended it. I was dealing with a lot.",
   "mismatches": [],
   "qa": {
    "status": "pass",
    "notes": "word-exact (faster-whisper base and small.en). Frames 0/7.54/14.97 s: same face, hair, glasses, cardigan as the reference; mouth open mid-word (lip movement present); selfie arm framing at 0 s, settles to a propped-phone framing by mid-shot (still native UGC); no on-screen text. Flag: at 0 s the laptop lid carries a small generic logo mark low in frame (inside the bottom-20% Reels UI zone); crop or blur in the edit if it reads at feed size."
   }
  },
  {
   "k": 2,
   "beat": "failed fixes + aha (repair render)",
   "job_id": "8ab3670f-a64d-4cd8-9549-62d1586f0bca",
   "rawUrl": "https://d8j0ntlcm91z4.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/hf_20260925_020251_8ab3670f-a64d-4cd8-9549-62d1586f0bca.mp4",
   "duration_s": 14.08,
   "requested_s": 14,
   "probe": "720x1280, 24 fps, h264 + native audio, 7,436,525 bytes",
   "spoken_line": "Asked about hiring someone. Five, twenty, fifteen thousand. Seriously? Come on. Then it clicked. I'd never open this shop and walk away. My stores got exactly that. Nobody worked them after launch.",
   "words": 32,
   "transcript": "asked about hiring someone. Five, twenty, fifteen thousand. Seriously, come on. Then it clicked. I'd never opened this shop and walk away. My stores got exactly that. Nobody worked them after launch.",
   "transcript_small_en": "asked about hiring someone. Five, 20, 15,000? Seriously, come on. Then it clicked. I'd never open this shop and walk away. My stores got exactly that. Nobody worked them after launch.",
   "mismatches": [
    "'open' -> 'opened' (base only; small.en hears 'open': ASR)"
   ],
   "qa": {
    "status": "pass",
    "notes": "all seven sentences present in order (repair fixed the omission; small.en word-exact, base hears 'opened' for 'open'). Frames at 0/7.0/13.9 s viewed: same face, dark brown hair with grey, reading glasses on head, oatmeal cardigan, navy tee, same back room (rails, brass desk lamp, wooden desk) as shots 1 and 3 and the reference; mouth open mid-word at 0 s and 13.9 s (lip movement present); at 7.0 s she glances off toward the shop (the scripted gesture); no on-screen text or logos; framing native (propped selfie)."
   },
   "frames": [
    "videos/frames/C1-V-shot2-1.jpg",
    "videos/frames/C1-V-shot2-2.jpg",
    "videos/frames/C1-V-shot2-3.jpg"
   ]
  },
  {
   "k": 3,
   "beat": "product + proof + CTA",
   "job_id": "cb56b79c-6cc3-44ea-9e10-f32f5ff213c4",
   "rawUrl": "https://d8j0ntlcm91z4.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/hf_20260925_014110_cb56b79c-6cc3-44ea-9e10-f32f5ff213c4.mp4",
   "duration_s": 15.072,
   "requested_s": 15,
   "probe": "720x1280, 24 fps, h264 + native audio, 6,825,717 bytes",
   "spoken_line": "I started with the $500 Build. New store, my name, products in stages, small tests on a budget I approve. It's live. First review: keep or replace. They're still on it. Ad spend's mine. Loaded and live.",
   "words": 37,
   "transcript": "I started with the $500 build, new store, my name, products and stages, small tests on a budget I approve, it's live. First review, keep a replace. They're still on it, ad spends mine, loaded and live.",
   "transcript_small_en": "I started with the $500 build, new store, my name, products and stages, small tests on a budget I approve. It's live. First review, keep or replace. They're still on it. Ad spends mine, loaded and live.",
   "mismatches": [
    "'in stages' -> 'and stages' (both base and small.en; reduced unstressed 'in', meaning intact; operator listen-check)",
    "'keep or replace' -> 'keep a replace' (base only; small.en hears 'or': ASR error)"
   ],
   "qa": {
    "status": "pass",
    "notes": "Speech ends at 13.9 s, then a silent relieved smile to 15.07 s (end-card room). Frames 0/7.54/14.97 s: identity matches shots 1 and the reference; talking mouth at 0 s, relieved smile at end; wall clock shows small numerals (script asked hands only; not legible at feed size); laptop screen not readable; no text/logos. Product first named at about 29 s of 44 s (66%), after the belief break (C0.5)."
   }
  }
 ],
 "stitched": {
  "media_id_raw": "d5a80e70-dca1-4495-add3-aade4457f673",
  "url_raw": "https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/d5a80e70-dca1-4495-add3-aade4457f673.mp4",
  "file_raw": "C1-V-45s.mp4 (23,412,908 bytes)",
  "media_id_captioned": "ef73f978-2569-41dc-be46-bd3baae0f5fa",
  "url_captioned": "https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/ef73f978-2569-41dc-be46-bd3baae0f5fa.mp4",
  "file_captioned": "C1-V-45s-captioned.mp4 (19,623,186 bytes)",
  "upload": "PUT 200 + 200, media_confirm status uploaded (both)",
  "duration_s": 44.224,
  "clip_durations_s": [
   15.072,
   14.08,
   15.072
  ],
  "encode": "720x1280, 30 fps, h264 crf 18/19, aac 192k, faststart",
  "safe_zone_ok": true,
  "safe_zone_check": "captions rendered alone on bla
```
