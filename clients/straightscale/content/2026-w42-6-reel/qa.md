# 2026-w42-6-reel · QA ("Kjo javë e vështirë është për tani", Sat 17 Oct 19:30)

Made 15 Oct, before the production gates existed: a GPT Image 2.5 still, one MiniMax H3 2K keyframe clip, an ElevenLabs
`eleven_v4` narrator (take 2 of 4), an ElevenLabs music bed, burned captions, the real wordmark on the end card.
No run ledger exists for it, so G-BUDGET and the banned-model check (F8) are N/A; every later version is an edit only
(0 credits). AI label: on (photoreal AI footage and an AI narrator, STANDARDS 7).

| Version | What changed | Fresh G-FINAL review | Result |
|---|---|---|---|
| v1 (15 Oct) | the original cut | `qa/FINAL.v1.review.json` | FAIL: -15.8 LUFS, first word at 0.52 s, captions in the Reels button zone, 68 px captions, 5-word cards |
| v2 (16 Oct) | voice from 0.05 s, hook super in the top third, 80 px cards of 1 to 3 words inside the safe zone, crimson #B31217, gain + oversampled limiter to -14 LUFS | `qa/FINAL.v2.review.json` | FAIL: the two-line super covered his head after the model's cut at 0.67 s; LRA 11.2 to 13.9 LU from the end-card music fade; one 0.27 s card |
| v3 (16 Oct) | one-line super in the clear band (y 274 to 370), "është për tani," moved to a lower card, last line re-split, end-card music held, whole-mix compressor; a separate cover with the 3-line hook at 92 px (`build-v3.sh`) | `qa/FINAL.v3.review.json` | FAIL: the cover (hero) still shows shelf pseudo-text when zoomed; the compressor lifted the bed in pauses (hook pause 17 dB under the voice, rule 20) |
| v4 (16 Oct) | remixed without the compressor: music x0.8 under the hook, x0.85 in the body, x2.4 on the end card only, gain + limiter; cover shelves softened (blur and slight darken, feathered) | pending | measured before review: -14.1 LUFS (ebur128) / -14.75 (loudnorm), LRA 4.5 / 5.4 LU, true peak -1.9 dBTP; hook pauses 21 dB under the voice, body pauses 15 to 19 dB |

Accepted minors (known, not fixable without a retake): pseudo-text on the shop packaging and kiosk posters (visible only
zoomed), the shutter stops about 70% down, three shots inside the one silent H3 clip (STANDARDS 2 wants one).

Still open for a person: the native Albanian listen and read (voice, captions, caption text), and a sound-on listen on a
phone.
