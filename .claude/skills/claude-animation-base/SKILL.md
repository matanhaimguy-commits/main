---
name: claude-animation-base
description: Hand-painted 2D character animation in p5.js and p5.brush, starring Clawd or a character you design, using John Heibel's Claude Animation Base kit (MIT). Use when the user asks for a painterly cartoon, a character animation, a Clawd video, or names Claude Animation Base. Not for product UI or kinetic-type motion graphics.
---

# Claude Animation Base

This folder is the unchanged starter kit from github.com/JohnHeibel/ClaudeAnimationBase (see README.md and LICENSE).
Don't build inside the skill folder; copy the kit into a project first.

1. Copy the kit into a new project folder (everything here except this SKILL.md):
   `mkdir -p <project> && cp -r "<skill base directory>"/. <project>/ && rm <project>/SKILL.md`
2. `cd <project> && npm install` (p5, p5.brush, puppeteer-core).
3. Read `ANIMATION_GUIDE.md` in full before drawing anything, then follow its workflow: storyboard first,
   build shot by shot, check contact sheets, render.
4. Render with `node render.mjs --clip --out=out/video.mp4` (see README.md for sheets and stills).
   In a Claude Code cloud session there is no GPU and Chromium lives under /opt/pw-browsers, so add
   `--chrome=/opt/pw-browsers/chromium-1194/chrome-linux/chrome --soft-gl`, and ask for fewer watercolour fills to keep render times sane.
