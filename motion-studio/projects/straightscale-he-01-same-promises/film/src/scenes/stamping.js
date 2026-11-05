// What the stamp does, in order: the hook hit, waiting at the left edge, the four free hits (the last on the word
// חינם), the three save hits, resting beside the stack, moving to the stage, hovering over the viewer's slip, leaving.
(function (SS) {
  function create(ctx, slips) {
    var L = ctx.layout, T = ctx.T, S = L.stamp, V = L.viewer, ev = [], hitTimes = [];
    function hit(id, t) {
      var p = slips[id].printAt(t);
      slips[id].print.at = t;
      hitTimes.push(t);
      ev.push({ kind: 'hit', t: t, x: p.x, y: p.y, r: p.r });
    }
    function move(t, pose, h, k, d) { ev.push({ kind: 'move', t: t, x: pose.x, y: pose.y, r: pose.r, h: h, k: k, d: d }); }
    var hook = T.cue('hit.hook');
    hit(L.hits.hook, hook);
    var hp = slips[L.hits.hook].printAt(hook), lift = S.hookLift;
    move(hook + 0.16, { x: hp.x + lift.dx, y: hp.y + lift.dy, r: lift.r }, lift.h, 110, 20);
    move(T.cue('cam.pull'), S.wait, S.wait.h, 90, 18);
    var a = T.cue('hits.free'), b = T.cue('hits.free.last');
    L.hits.free.forEach(function (id, i) { hit(id, a + i * (b - a) / (L.hits.free.length - 1)); });
    var s0 = T.cue('hits.save'), se = T.spec('hits.save').every;
    L.hits.save.forEach(function (id, i) { hit(id, s0 + i * se); });
    var last = hitTimes[hitTimes.length - 1];
    move(last + 0.3, S.parkPile, 0, 100, 20);
    move(T.cue('stack') + 0.2, S.parkStack, 0.35, 70, 16);
    move(T.cue('stack') + 1.2, S.parkStack, 0, 120, 22);
    var away = T.cue('stack.away'), st = { x: L.stage.x, y: L.stage.y, r: -4 };
    move(away + 0.1, st, 0.15, 60, 15);
    move(away + 1.3, st, 0, 120, 22);
    var vd = T.cue('viewer.drop');
    move(vd - 0.45, S.parkViewer, 0.25, 160, 25);
    move(vd - 0.05, S.parkViewer, 0, 200, 26);
    var hv = T.cue('hover');
    move(hv, { x: V.x - 40, y: V.y + 55, r: -3 }, 0.55, 70, 15);
    move(hv + 1.3, { x: V.x + 25, y: V.y + 35, r: 2 }, 0.5, 60, 15);
    move(hv + 2.4, { x: V.x - 10, y: V.y + 48, r: -1 }, 0.58, 60, 15);
    move(T.cue('stamp.exit'), S.exit, S.exit.h, 4, 4);
    var stamp = SS.stamp.create(ctx);
    stamp.plan(S.start, ev);
    stamp.gone = T.cue('stamp.exit') + 2.5;   // out of the shot by then
    return stamp;
  }
  SS.stamping = { create: create };
})((window.SS = window.SS || {}));
