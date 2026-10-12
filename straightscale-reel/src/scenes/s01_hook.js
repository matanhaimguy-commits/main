// S1 · Hook (0.00–3.00) "Të shkruajnë 'Sa kushton?'... dhe zhduken?"
import { C, SANS, W, text, rr, ep, popIn, prog, E, shadow, noShadow, charcoalBg, rng, lerp } from "../lib.js";

export default {
  id: "s01_hook", start: 0, end: 3.0,
  draw(ctx, t) {
    charcoalBg(ctx);
    const enter = ep(t, 0, 0.45, E.outQuart);
    const px = 540, pw = 560, ph = 1000, top = 250 + (1 - enter) * 90;
    const gone = ep(t, 2.08, 2.6); // customer disappears
    ctx.save(); ctx.globalAlpha = enter;
    // phone body
    shadow(ctx, 60, 30, "rgba(0,0,0,0.55)");
    ctx.fillStyle = "#111"; rr(ctx, px - pw / 2, top, pw, ph, 70); ctx.fill(); noShadow(ctx);
    ctx.strokeStyle = "#3a3632"; ctx.lineWidth = 3; rr(ctx, px - pw / 2, top, pw, ph, 70); ctx.stroke();
    const sx = px - pw / 2 + 16, sy = top + 16, sw = pw - 32, sh = ph - 32;
    ctx.save(); rr(ctx, sx, sy, sw, sh, 56); ctx.clip();
    ctx.fillStyle = C.ivory; ctx.fillRect(sx, sy, sw, sh);
    // header
    ctx.fillStyle = "#EFEAE0"; ctx.fillRect(sx, sy, sw, 150);
    ctx.fillStyle = "#1a1a1a"; rr(ctx, px - 70, sy + 14, 140, 30, 15); ctx.fill(); // notch
    const avA = 1 - gone * 0.75;
    ctx.globalAlpha = enter * avA;
    ctx.fillStyle = C.stone; ctx.beginPath(); ctx.arc(sx + 70, sy + 100, 30, 0, Math.PI * 2); ctx.fill();
    text(ctx, "K", sx + 70, sy + 112, { size: 32, weight: 800, color: C.ivory, align: "center" });
    ctx.globalAlpha = enter;
    text(ctx, "Klient i ri", sx + 120, sy + 96, { size: 30, weight: 700, color: C.ink, alpha: avA });
    const online = gone < 0.5;
    ctx.fillStyle = online ? "#3BA55C" : "#9a948a";
    ctx.beginPath(); ctx.arc(sx + 128, sy + 122, 7, 0, Math.PI * 2); ctx.fill();
    text(ctx, online ? "online" : "offline", sx + 142, sy + 131, { size: 24, weight: 500, color: "#7d776d" });
    // customer bubble "Sa kushton?"
    const b = popIn(t, 0.88, 0.32);
    if (t > 0.86) {
      ctx.save();
      const bx = sx + 34, by = sy + 260;
      ctx.translate(bx, by + 50); ctx.scale(b, b); ctx.translate(-bx, -(by + 50));
      ctx.globalAlpha = enter * (1 - gone * 0.6);
      shadow(ctx, 16, 6, "rgba(0,0,0,0.12)");
      ctx.fillStyle = C.marble; rr(ctx, bx, by, 330, 104, 34); ctx.fill(); noShadow(ctx);
      ctx.beginPath(); ctx.moveTo(bx + 10, by + 104); ctx.lineTo(bx - 8, by + 118); ctx.lineTo(bx + 34, by + 96); ctx.fill();
      text(ctx, "Sa kushton?", bx + 30, by + 66, { size: 44, weight: 700, color: C.ink });
      text(ctx, "09:41", bx + 330 - 16, by + 132, { size: 20, weight: 500, color: "#9a948a", align: "right" });
      ctx.restore();
      // notification ring
      const ring = prog(t, 0.9, 1.5);
      if (ring > 0 && ring < 1) {
        ctx.strokeStyle = `rgba(212,175,55,${0.7 * (1 - ring)})`; ctx.lineWidth = 6;
        ctx.beginPath(); ctx.arc(bx + 165, by + 52, 80 + ring * 140, 0, Math.PI * 2); ctx.stroke();
      }
    }
    // owner reply (right) + typing dots
    if (t > 1.3 && t < 1.62) {
      ctx.fillStyle = C.charcoal; rr(ctx, sx + sw - 160, sy + 430, 120, 64, 32); ctx.fill();
      for (let i = 0; i < 3; i++) {
        const a = 0.4 + 0.6 * Math.abs(Math.sin((t * 8) + i));
        ctx.fillStyle = `rgba(248,246,239,${a})`; ctx.beginPath(); ctx.arc(sx + sw - 128 + i * 28, sy + 462, 7, 0, Math.PI * 2); ctx.fill();
      }
    }
    if (t >= 1.62) {
      const r = popIn(t, 1.62, 0.3);
      const bw = 400, bx = sx + sw - 34 - bw, by = sy + 420;
      ctx.save(); ctx.translate(bx + bw, by + 60); ctx.scale(r, r); ctx.translate(-(bx + bw), -(by + 60));
      ctx.fillStyle = C.charcoal; rr(ctx, bx, by, bw, 132, 34); ctx.fill();
      text(ctx, "Përshëndetje! Çmimi", bx + 28, by + 56, { size: 32, weight: 600, color: C.ivory });
      text(ctx, "varet nga...", bx + 28, by + 100, { size: 32, weight: 600, color: C.ivory });
      ctx.restore();
      if (t > 2.15) text(ctx, "Shikuar ✓✓", bx + bw - 6, by + 172, { size: 22, weight: 600, color: "#4F8FD9", align: "right", alpha: ep(t, 2.15, 2.4) });
    }
    // customer leaves: dust particles from avatar
    if (gone > 0 && gone < 1) {
      const r = rng(3);
      for (let i = 0; i < 26; i++) {
        const a = r() * Math.PI * 2, d = 20 + gone * (60 + r() * 120);
        ctx.fillStyle = `rgba(142,134,123,${(1 - gone) * 0.9})`;
        ctx.beginPath(); ctx.arc(sx + 70 + Math.cos(a) * d, sy + 100 + Math.sin(a) * d - gone * 40, 3 + r() * 4, 0, Math.PI * 2); ctx.fill();
      }
    }
    ctx.restore(); // clip
    ctx.restore();
  },
};
