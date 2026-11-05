// The hand behind the clearing of the desk (review round 5), seen as its shadow pointing in from the left:
// on "לא" its fingertip settles on the stamp's knob and on "יכול" it pulls the stamp off the desk, moving with it;
// on "בדיוק", "אצלכם" and "בפגישה" it flicks the competitors' slips off one by one, then withdraws.
(function (SS) {
  var A = SS.anim, TIP = { x: 16, y: 135 };   // fingertip inside the 900 x 324 shadow, before mirroring
  function create(ctx, stamp, rivals) {
    var T = ctx.T, c = function (n) { return T.cue(n); };
    var tIn = c('hand.in'), tPullEnd = c('stamp.pull') + 1.0, go = [c('rival.go1'), c('rival.go2'), c('rival.go3')];
    var wrap = SS.dom.layered(SS.dom.el('div', 'hand-wrap', ctx.world), ['overflow']);
    SS.finger.create(wrap);
    var reach = A.path(0, [{ t: tIn, to: 1, k: 600, d: 49 }]);   // there in about 0.2 s, before the pull
    // flicks: in just before each word, out after it unless the next word comes within half a second
    var steps = [];
    go.forEach(function (g, i) {
      steps.push({ t: g - 0.22, to: 1, k: 600, d: 49 });
      if (i === go.length - 1 || go[i + 1] - g > 0.5) steps.push({ t: g + 0.14, to: 0, k: 260, d: 32 });
    });
    var flick = A.path(0, steps), edge = rivals.edge;
    function place(tipX, tipY, op) {
      wrap.style.transform = 'translate(' + (tipX + TIP.x).toFixed(1) + 'px,' + (tipY - TIP.y).toFixed(1) + 'px) scaleX(-1) rotate(-4deg)';
      wrap.style.opacity = op.toFixed(3);
    }
    return {
      render: function (t) {
        var onStamp = t >= tIn && t < tPullEnd, f = flick(t), onRivals = t >= go[0] - 0.22 && f > 0.01;
        SS.dom.show(wrap, onStamp || onRivals);
        if (onStamp) {
          var p = stamp.pos(t), s = 1 + 0.85 * Math.max(0, stamp.height(t)), r = reach(t);
          place(p.x - 10 * s - 620 * (1 - r), p.y + 4, 0.8 * A.clamp(r * 1.6));
        } else if (onRivals) {
          place(edge.x - 700 * (1 - f), edge.y, 0.8 * A.clamp(f * 1.6));
        }
      }
    };
  }
  SS.hand = { create: create };
})((window.SS = window.SS || {}));
