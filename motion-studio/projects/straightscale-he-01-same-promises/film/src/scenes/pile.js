// The pile: the hook slip, the cascade of the other 13, the stamped 8 gathered into one neat stack, the 6 others
// pushed off the desk, and the stack slid away when the camera leaves for the stage.
(function (SS) {
  function create(ctx) {
    var L = ctx.layout, T = ctx.T, C = ctx.content.slips, slips = {};
    var order = ['p1'].concat(L.cascade);
    var cas = T.cue('cascade'), every = T.spec('cascade').every;
    var gather = T.cue('stack'), away = T.cue('stack.away');
    order.forEach(function (id, i) {
      var s = SS.slip.create(ctx, id, C[id], 100 + i * 7), p = L.pile[id];
      var drop = i === 0 ? T.cue('p1.drop') : cas + (i - 1) * every;
      var moves = [], zs = [[0, 10 + i]], si = L.stack.order.indexOf(id);
      if (si >= 0) {
        var tg = gather + si * L.stack.every, x = L.stack.left + s.w / 2, y = L.stack.bottom + (L.stack.order.length - 1 - si) * L.stack.step - s.h / 2;
        moves.push({ t: tg, to: { x: x, y: y, r: si % 2 ? 0.3 : -0.25 }, k: 110, d: 21 });
        moves.push({ t: away, to: { x: x - 1500 }, k: 60, d: 15.5 });
        zs.push([tg, 100 + si]);
      } else {
        var lv = L.leave[id];
        moves.push({ t: gather - 0.12 + (i % 6) * 0.04, to: { x: p[0] + lv[0], y: p[1] + lv[1] }, k: 70, d: 16 });
      }
      s.setup({ t: drop, x: p[0], y: p[1], r: p[2] }, moves, zs);
      slips[id] = s;
    });
    return { slips: slips, render: function (t) { order.forEach(function (id) { slips[id].render(t); }); } };
  }
  SS.pile = { create: create };
})((window.SS = window.SS || {}));
