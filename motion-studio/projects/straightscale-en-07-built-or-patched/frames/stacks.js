// Frame 1 of each finalist stack (round 2; round 3 adds A, B, C). Text lines are the text hook, split for the phone.
// Labels on scraps name the buyer's own fixes in plain words, never a platform name (STANDARDS 6).
import { cloth, scrap, label, tornScrap } from './cloth.js';

const CL = { x: 120, y: 760, w: 840, h: 860 };

export const STACKS = {
  '01': {
    lines: ['Clients one month,', 'nothing the next?'],
    draw: (ctx) => { cloth(ctx, CL.x, CL.y, CL.w, CL.h); tornScrap(ctx, { x: 300, y: 980, w: 470, h: 420, rot: 22 }); },
  },
  '02': {
    lines: ['"Try a new channel."', "That's not the problem."],
    draw: (ctx) => {
      cloth(ctx, CL.x, CL.y, CL.w, CL.h); scrap(ctx, { x: 270, y: 960, w: 540, h: 460, rot: -5, lift: 0.7, thread: false });
      label(ctx, 'NEW CHANNEL', 540, 1190, 72, false);
      ctx.strokeStyle = '#BE0F18'; ctx.lineWidth = 16; ctx.lineCap = 'round';
      ctx.beginPath(); ctx.moveTo(250, 1440); ctx.lineTo(830, 940); ctx.stroke();
    },
  },
  '03': {
    lines: ['Tried everything?', 'Each fix started from zero.'],
    draw: (ctx) => {
      cloth(ctx, CL.x, CL.y, CL.w, CL.h);
      const s = [
        { x: 170, y: 830, pattern: 'gingham', rot: -6, name: 'REFERRALS' },
        { x: 560, y: 1060, pattern: 'stripes', rot: 5, name: 'COLD EMAIL' },
        { x: 170, y: 1300, pattern: 'dots', rot: -3, name: 'POSTING' },
      ];
      s.forEach((p) => scrap(ctx, { x: p.x, y: p.y, w: 350, h: 250, rot: p.rot, pattern: p.pattern, lift: 0.5, thread: false }));
      s.forEach((p) => label(ctx, p.name, p.x + 175, p.y + 125, 44));
    },
  },
  '05': {
    lines: ['Does each fix', 'start from zero?'],
    draw: (ctx) => {
      cloth(ctx, CL.x, CL.y, CL.w, CL.h);
      scrap(ctx, { x: 170, y: 1000, w: 330, h: 380, rot: -4, pattern: 'gingham', thread: false });
      scrap(ctx, { x: 580, y: 1000, w: 330, h: 380, rot: 4, pattern: 'dots', thread: false });
      label(ctx, 'FIX 1', 335, 1190, 56); label(ctx, 'FIX 2', 745, 1190, 56);
    },
  },
};

// Round 3: the buyer's three fixes, each sewn on alone and each peeling off (one shared frame for A and B).
function peeling(ctx) {
  cloth(ctx, CL.x, CL.y, CL.w, CL.h);
  const s = [
    { x: 160, y: 820, pattern: 'gingham', rot: -6, name: 'REFERRALS' },
    { x: 560, y: 1050, pattern: 'stripes', rot: 6, name: 'COLD EMAIL' },
    { x: 170, y: 1290, pattern: 'dots', rot: -4, name: 'POSTING' },
  ];
  s.forEach((p) => scrap(ctx, { x: p.x, y: p.y, w: 360, h: 260, rot: p.rot, pattern: p.pattern, lift: 1.7, float: 0.5, thread: false }));
  s.forEach((p) => label(ctx, p.name, p.x + 170, p.y + 160, 44));
}
STACKS.A = { lines: ['Clients one month,', 'nothing the next?'], draw: peeling };
STACKS.B = { lines: ['Referrals, cold email, posting.', 'None of it stuck.'], draw: peeling };
STACKS.C = {
  lines: ['"Try a new channel."', "That's not your problem."],
  draw: (ctx) => {
    cloth(ctx, CL.x, CL.y, CL.w, CL.h); scrap(ctx, { x: 270, y: 960, w: 540, h: 460, rot: -5, lift: 0.7, thread: false });
    ctx.strokeStyle = '#BE0F18'; ctx.lineWidth = 16; ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(250, 1440); ctx.lineTo(830, 940); ctx.stroke();
    label(ctx, 'NEW CHANNEL', 540, 1190, 72, false);
  },
};
