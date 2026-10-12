// S1 · Hook (0.00–3.00) "Të shkruajnë 'Sa kushton?'... dhe zhduken?"
// Giant typing bubble → bursts into a ransom note → letters peel off and fly away on "zhduken".
import { C, SERIF, SANS, W, H, text, rr, clamp, lerp, rng, measure } from "../lib.js";
import { spring, track, paperBg, ransomWord, ransomWidth, tape } from "../fx.js";

const L1 = "SA", L2 = "KUSHTON?";
export default {
  id: "s01_hook", start: 0, end: 3.0,
  draw(ctx, t) {
    paperBg(ctx, "#ECE4D3", 3);
    // camera: slow push, small kick on the burst
    const cam = track(t, [[0, 1.0], [0.88, 1.035], [2.08, 1.06]], 120, 22);
    ctx.translate(W / 2, 880); ctx.scale(cam, cam); ctx.translate(-W / 2, -880);

    // 1) typing bubble (0 → 0.9), cropped off the left edge
    const bub = spring(t + 0.6, 200, 20) * (1 - spring(t - 0.84, 320, 30));
    if (bub > 0.01) {
      ctx.save(); ctx.translate(430, 860); ctx.scale(bub, bub);
      ctx.fillStyle = C.charcoal; rr(ctx, -560, -230, 1000, 460, 230); ctx.fill();
      ctx.beginPath(); ctx.moveTo(-430, 170); ctx.lineTo(-560, 300); ctx.lineTo(-300, 210); ctx.fill();
      for (let i = 0; i < 3; i++) {
        const b = Math.sin(t * 9 - i * 0.9);
        ctx.fillStyle = C.ivory; ctx.globalAlpha = 0.55 + 0.45 * Math.max(0, b);
        ctx.beginPath(); ctx.arc(-200 + i * 200, -Math.max(0, b) * 34, 62, 0, Math.PI * 2); ctx.fill();
      }
      ctx.restore();
    }

    // 2) ransom note lands letter by letter on the spoken words
    const s1 = 300, s2 = Math.min(220, (980 / ransomWidth(ctx, L2, 220, 11)) * 220);
    const land1 = (i) => 0.86 + i * 0.07, land2 = (i) => 1.02 + i * 0.075;
    // 3) "zhduken": each letter peels and flies out, accelerating, spinning
    const fly = (seed, n) => (i) => {
      const p = clamp((t - (2.06 + i * 0.035)) / 0.55); if (p <= 0) return null;
      const r = rng(seed + i * 13), e = p * p;
      const ang = -Math.PI / 2 + (r() - 0.5) * 2.4;
      return { dx: Math.cos(ang) * 1500 * e, dy: Math.sin(ang) * 1700 * e - 120 * p, rot: (r() - 0.5) * 6 * e };
    };
    ransomWord(ctx, L1, W / 2, 700, s1, 5, t, land1, fly(100, L1.length));
    ransomWord(ctx, L2, W / 2, 990, s2, 11, t, land2, fly(200, L2.length));

    // a strip of tape left behind + "Shikuar ✓✓" (seen, then nothing)
    const seen = spring(t - 2.45, 220, 24);
    if (t > 2.1) tape(ctx, W / 2, 860, 260, 58, -0.06, 4, 0.7 * clamp((t - 2.1) * 4));
    if (seen > 0.01) text(ctx, "Shikuar ✓✓", W / 2, 1000 + (1 - seen) * 30, { size: 46, weight: 700, color: "#8a8378", align: "center", alpha: clamp(seen) });
  },
};
