# Sat 17 quote reel: v4 edit (mux + cover clean-up)

Date: 2026-10-18. Everything ran in the Higgsfield sandbox. Nothing was generated: the fixes are ffmpeg, PIL, numpy and OpenCV code only.
Sandbox working folder: `/home/user/daily/reel/v4/`. The cover script and check crops are in `/home/user/daily/reel/v4/cov/`.

## Deliverables

| File | media_id | CDN url | Size | md5 |
|---|---|---|---|---|
| ss-2026-10-17-reel-v4.mp4 | adbf0ae8-3d29-47af-9f14-1b818e8bb609 | https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/adbf0ae8-3d29-47af-9f14-1b818e8bb609.mp4 | 12,669,317 B | 78f99da5ab0247282823716936525dde |
| ss-2026-10-17-reel-v4-cover.jpg | 40bdf41f-dc70-49e8-bc51-04362a1c2362 | https://d2ol7oe51mr4n9.cloudfront.net/user_3CQo67nOEoDBnYQeXyEukxi74Z6/40bdf41f-dc70-49e8-bc51-04362a1c2362.jpg | 553,911 B | 8ed97abbbad23054ceb3ab32c13b27e3 |

Both PUTs returned 200 and media_confirm returned `uploaded`. A HEAD request on each CDN url returned HTTP 200 with the right content-type, and the content-length matches the local file.

## 1. Mux

Inputs: `pic.mp4` (the v3 picture: h264 1080x1920, 30 fps, 13.600 s; its own AAC track is dropped) and `n_f.wav` (the final v4 mix: pcm_s16le, 48 kHz mono, 13.572 s).

```
ffmpeg -y -v error -i pic.mp4 -i n_f.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -movflags +faststart ss-2026-10-17-reel-v4.mp4
```

Output: h264 1080x1920 30 fps (stream copy, 7.25 Mb/s), AAC 48 kHz mono at about 188 kb/s. Duration 13.600 s (audio 13.572 s). The moov atom is at byte 36, so faststart is in place.

### Loudness re-measured on the muxed file

```
ffmpeg -hide_banner -nostats -i ss-2026-10-17-reel-v4.mp4 -map 0:a -af ebur128=peak=true -f null -
ffmpeg -hide_banner -nostats -i ss-2026-10-17-reel-v4.mp4 -map 0:a -af loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json -f null -
```

| Meter | Integrated | LRA | True peak | Other |
|---|---|---|---|---|
| ebur128 (peak=true) | **-14.1 LUFS** | **4.5 LU** | **-1.9 dBFS** | threshold -24.9 LUFS; LRA low/high -17.6 / -13.1 LUFS |
| loudnorm (measure pass) | **-14.74 LUFS** | **5.50 LU** | **-1.88 dBTP** | input_thresh -25.38 LUFS, target_offset +0.72 |

These match the WAV measurement given in the brief (-14.1 / -14.75 LUFS, LRA 4.5 / 5.4 LU, true peak -1.9 dBTP). The AAC encode moved loudnorm by 0.01 LUFS and 0.1 LU and left ebur128 unchanged. The true peak stays below -1 dBTP.

## 2. Cover v4

Source: `/home/user/daily/reel/v3/ss-2026-10-17-reel-v3-cover.jpg` (1080x1920, 4:2:0).
Problem: the lit shop window at the bottom left (about x 0-330, y 1000-1790) showed small pseudo-text on the shelf packaging. One example is the red can with a white script-like mark near x 30-90, y 1470-1530; other boxes carried fake letters.

Command: `python3 /home/user/daily/reel/v4/cov/soften.py` (this writes `/home/user/daily/reel/v4/ss-2026-10-17-reel-v4-cover.jpg`)

How it works:
- **Blur**: Gaussian with sigma 9 px. It is a normalised convolution that ignores protected pixels, so neither the dark coat nor the shutter bleeds into the window.
- **Darkening**: 12 % (the blurred layer is multiplied by 0.88). Mean luma over the window (x 0-260, y 1040-1740) fell from 77.1 to 67.9, which is -11.9 %.
- **Area mask**: a rectangle covering x 0-310 and y 1000-1770, feathered with a Gaussian of sigma 10 px, which gives a soft edge about 40 px wide (right ramp about x 290-330, bottom ramp about y 1750-1790). The rectangle extends past the left image edge, so x = 0 is fully covered. The bottom was pulled in from 1790 to 1770 so that the base panel and sill below the glass blend out gradually. The lowest pseudo-text, at about y 1725, still gets the full effect.
- **Protected areas** (effect forced to exactly 0, with a 2 px grow and a 1.2 px soft edge):
  - The owner's hand, sleeve, coat and legs, traced as a polygon that follows the coat edge (about x 281 to 306 at y 1200-1370, down to x 260 at the hem at y 1500).
  - The shutter slat the hand grips, above the window top edge (y = 1021 + 0.052x). This keeps the hand-on-shutter contact sharp, and the window behind the glass reads as defocused.
- **Save**: JPEG quality 93, 4:4:4 chroma (to avoid adding more chroma loss on the headline).

Checks:
- Before the JPEG save, the change is confined to x 0-329 and y 1021-1791. The maximum pixel difference is 0 on the owner, 0 on the shutter, 0 above y 950 (all three headline lines) and 0 at x >= 345.
- After the JPEG save, PSNR against v3 is 47.9 dB on the headline band (y < 950, mean absolute difference 0.46 levels) and 47.0 dB on the owner and street side (x >= 345). The only difference there is re-encode noise.
- At 2x (four bands across y 1000-1790, before and after), no letter-like shape remains. Every shelf label and box mark is a soft colour field.
- At 4x on the red can (x 0-120, y 1440-1560), the white script mark is gone. Only a soft red and brown blob remains.
- On the edges at 3x: the coat, sleeve and hand edges are clean, with no dark halo and no sharp leftover window strip. The narrow frame strips between the window and the coat are now blurred. The shutter slat is sharp. The bottom and right ramps fade out without a visible line.
- At 200 px wide, the cover reads the same as v3. The headline is unchanged, the owner is unchanged, and the window is a warm, slightly darker bokeh that stops pulling the eye.

Check images in the sandbox, `/home/user/daily/reel/v4/cov/`:
- `b2x_0-3.jpg` (before, 2x) and `f2x_0-3.jpg` (after, 2x)
- `can4x.jpg`
- `edge_*.jpg`, `seam_top.jpg`, `seam_bot.jpg`
- `cov200_ba.jpg`, `v4_cov_200.jpg`
- `after_540.jpg`

## 3. Upload

```
media_upload files=[ss-2026-10-17-reel-v4.mp4 video/mp4, ss-2026-10-17-reel-v4-cover.jpg image/jpeg]
curl -sS -o /dev/null -w "%{http_code}" -X PUT -H "Content-Type: video/mp4"  -H "If-None-Match: *" --upload-file ss-2026-10-17-reel-v4.mp4 '<upload_url>'        -> 200
curl -sS -o /dev/null -w "%{http_code}" -X PUT -H "Content-Type: image/jpeg" -H "If-None-Match: *" --upload-file ss-2026-10-17-reel-v4-cover.jpg '<upload_url>'  -> 200
media_confirm adbf0ae8-3d29-47af-9f14-1b818e8bb609 type=video -> uploaded
media_confirm 40bdf41f-dc70-49e8-bc51-04362a1c2362 type=image -> uploaded
```
