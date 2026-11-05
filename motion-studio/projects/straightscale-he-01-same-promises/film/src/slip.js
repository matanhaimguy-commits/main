// A paper slip with one real headline. It drops onto the desk with a short bounce, settles to its rotation, and its
// soft shadow grows as it lands. Later moves (into the stack, off the desk) come from `moves`.
(function (SS) {
  var A = SS.anim, PAD = 40;
  function shadow(h) {
    var c = 'rgba(52,38,22,';
    return '0 ' + (1 + 3 * h).toFixed(1) + 'px ' + (2 + 6 * h).toFixed(1) + 'px ' + c + (0.26 * (1 - h)).toFixed(3) + '), ' +
      (6 + 46 * h).toFixed(1) + 'px ' + (10 + 70 * h).toFixed(1) + 'px ' + (16 + 44 * h).toFixed(1) + 'px ' + c + (0.1 + 0.08 * (1 - h)).toFixed(3) + ')';
  }
  function create(ctx, id, spec, seed) {
    var rnd = SS.rng.mulberry32(seed);
    var wrap = SS.dom.layered(SS.dom.el('div', 'slip-wrap', ctx.world), ['overflow']);
    var slip = SS.dom.el('div', 'slip' + (spec.back ? ' slip-back' : ''), wrap);
    slip.style.backgroundImage = 'url(' + ctx.paper + ')';
    if (!spec.back) SS.dom.layered(SS.dom.el('p', 'slip-text he', slip, spec.text), ['overlap', 'occlusion']);
    var w = spec.back ? 560 : slip.offsetWidth, h = spec.back ? 190 : slip.offsetHeight;
    if (spec.back) { slip.style.width = w + 'px'; slip.style.height = h + 'px'; }
    slip.style.left = (-w / 2) + 'px'; slip.style.top = (-h / 2) + 'px';
    var print = spec.stamp ? SS.ink.create(slip, spec.stamp, seed + 101, w) : null;
    var me = {
      id: id, el: wrap, w: w, h: h, print: print, z: 10,
      // drop: {t, x, y, r}; moves: [{t, to: {x, y, r}, k, d}]; zs: [[t, z]]
      setup: function (drop, moves, zs) {
        // tossed in from the nearer side edge, never through the top band
        var side = drop.x < 500 ? -1 : 1;
        var from = { x: drop.x + side * (420 + rnd() * 140), y: drop.y - 60 - rnd() * 120, r: drop.r + side * (8 + rnd() * 8) };
        me.drop = drop; me.zs = zs || [];
        me.pos = A.paths(from, [{ t: drop.t, to: { x: drop.x, y: drop.y, r: drop.r }, k: 150, d: 24 }].concat(moves || []));
        me.height = A.path(1, [{ t: drop.t, to: 0, how: 'bounce', k: 230, d: 14 }]);
      },
      // where the print's centre is on the desk at time t (for the stamp to land on)
      printAt: function (t) {
        var p = me.pos(t), o = SS.dom.rot(print.cx - w / 2, print.cy - h / 2, p.r);
        return { x: p.x + o.x, y: p.y + o.y, r: p.r + print.r };
      },
      render: function (t) {
        var on = t >= me.drop.t;
        SS.dom.show(wrap, on);
        if (print) print.render(t);
        if (!on) return;
        var p = me.pos(t), hh = me.height(t), z = 10;
        me.zs.forEach(function (k) { if (t >= k[0]) z = k[1]; });
        wrap.style.zIndex = z;
        SS.dom.place(wrap, p.x, p.y, p.r, 1 + 0.42 * hh);
        slip.style.boxShadow = shadow(Math.min(1, hh)) + ', inset 0 0 0 1px rgba(80,60,40,0.07)';
      }
    };
    return me;
  }
  SS.slip = { create: create };
})((window.SS = window.SS || {}));
