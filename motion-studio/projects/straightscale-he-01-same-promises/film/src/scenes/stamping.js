// What the stamp does, in order: the hook hit and the turn-over that shows its face, waiting at the left edge, the
// four free hits (the last on the word חינם), the three save hits, resting beside the stack, alone on the cleared desk
// (moving on line 6's words), hopping aside for the viewer's slip, hovering beside its headline (never over it, D8),
// then taken by a hand on "לא" and pulled off the desk on "יכול". Every move is on a cue in timing.json.
(function (SS) {
  function create(ctx, slips) {
    var L = ctx.layout, T = ctx.T, S = L.stamp, V = L.viewer, H = S.hover, ev = [], hitTimes = [];
    var C = function (name) { return T.cue(name); };
    function hit(id, t) {
      var p = slips[id].printAt(t);
      slips[id].print.at = t;
      hitTimes.push(t);
      ev.push({ kind: 'hit', t: t, x: p.x, y: p.y, r: p.r });
    }
    function move(t, pose, h, k, d) { ev.push({ kind: 'move', t: t, x: pose.x, y: pose.y, r: pose.r, h: h, k: k, d: d }); }
    var at = function (dx, dy, r) { return { x: V.x + dx, y: V.y + dy, r: r }; };
    var hook = C('hit.hook');
    hit(L.hits.hook, hook);
    var hp = slips[L.hits.hook].printAt(hook), lift = S.hookLift;
    move(hook + 0.16, { x: hp.x + lift.dx, y: hp.y + lift.dy, r: lift.r }, lift.h, 110, 20);
    move(C('cam.pull'), S.wait, S.wait.h, 90, 18);
    move(C('stamp.ready'), S.ready, S.ready.h, 110, 20);
    var a = C('hits.free'), b = C('hits.free.last');
    L.hits.free.forEach(function (id, i) { hit(id, a + i * (b - a) / (L.hits.free.length - 1)); });
    var s0 = C('hits.save'), se = T.spec('hits.save').every;
    L.hits.save.forEach(function (id, i) { hit(id, s0 + i * se); });
    move(hitTimes[hitTimes.length - 1] + 0.3, S.parkPile, 0, 100, 20);
    move(C('stack') + 0.2, S.parkStack, 0.35, 70, 16);
    move(C('stack') + 1.2, S.parkStack, 0, 120, 22);
    // line 6: alone on the desk
    var st = L.stage;
    move(C('stamp.slide'), { x: st.x - 30, y: st.y, r: -10 }, 0.15, 60, 15);
    move(C('stamp.settle'), { x: st.x, y: st.y, r: -3 }, 0, 160, 24);
    move(C('stamp.rise'), { x: st.x, y: st.y - 10, r: -3 }, 0.24, 120, 20);
    move(C('stamp.drift'), { x: st.x + 45, y: st.y - 20, r: 5 }, 0.24, 70, 16);
    move(C('stamp.sit'), { x: st.x + 45, y: st.y - 20, r: 4 }, 0, 220, 26);
    // line 7: hop aside for the viewer's slip
    move(C('stamp.aside'), S.parkViewer, 0.25, 160, 25);
    move(C('viewer.drop') + 0.1, S.parkViewer, 0, 200, 26);
    // line 9: beside the headline, on the empty left of the slip; its shadow stays off the words
    move(C('hover'), at(H[0], H[1], -4), 0.45, 70, 15);
    move(C('hover.drift'), at(H[0] + 18, H[1] - 22, 2), 0.42, 60, 15);
    move(C('hover.dip'), at(H[0] + 10, H[1] + 10, -2), 0.22, 90, 16);
    move(C('hover.lift'), at(H[0] - 10, H[1] - 10, -5), 0.5, 70, 15);
    var held = at(H[0] - 10, H[1] - 10, -5);
    move(C('hand.in'), held, 0.32, 200, 26);                 // the hand takes hold
    move(C('stamp.pull'), S.exit, S.exit.h, 30, 11);          // and pulls it off the desk
    var stamp = SS.stamp.create(ctx, ctx.content.slips[L.hits.hook].stamp);
    stamp.plan(S.start, ev);
    stamp.turns([[C('stamp.flip'), 180], [C('stamp.flipback'), 360]]);
    stamp.gone = C('stamp.pull') + 2.2;   // out of the shot by then
    return stamp;
  }
  SS.stamping = { create: create };
})((window.SS = window.SS || {}));
