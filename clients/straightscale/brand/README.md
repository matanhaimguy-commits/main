# StraightScale brand files (the real ones)

- `wordmark-white.png`: the mark + white "StraightScale" wordmark, for dark backgrounds (images, carousels, reels).
- `symbol.png`: the mark alone (red rounded square, S-shaped channel, gold square in the top-right notch).
- `logo-full.png`: the mark + black wordmark, for light backgrounds.

Extracted 15 Oct 2026 from `motion-studio/projects/straightscale-2026-w43-3-reel-v2/overlay/logos.js` (the files the
reel end cards use) and `motion-studio/projects/straightscale-03/assets/brand/logo-full.png`.

**Never let an image or video model draw the logo** (brand-kit.md: real files only). Generate with the logo area left
calm and empty, then paste the real file: `python3 growth-engine/tools/brand_overlay.py <in> <out> --client straightscale`.
