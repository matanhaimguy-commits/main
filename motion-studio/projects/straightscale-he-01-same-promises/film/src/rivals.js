// The competitors' slips: three copies of an ad laid out like yours, the same "[הכותרת]". On "המתחרה" they slide in
// under your slip, on "אחד" they line up exactly on it (word for word, you cannot tell them apart), on "כן" they slide
// away (the caption band stays clear), on "למשל" they are back under yours, and on "בדיוק", "אצלכם", "בפגישה" they are
// pushed off the desk one by one, leaving yours alone.
(function (SS) {
  var A = SS.anim;
  function slip(ctx, parent, C, w) {
    var wrap = SS.dom.layered(SS.dom.el('div', 'slip-wrap', parent), ['overflow']);
    var e = SS.dom.el('div', 'slip viewer rival', wrap);
    e.style.width = w + 'px';
    e.style.backgroundImage = 'url(' + ctx.paper + ')';
    [['v-label he', C.label], ['v-name he', C.name], ['v-head he', C.headline]].forEach(function (p) {
      SS.dom.layered(SS.dom.el('div', p[0], e, p[1]), ['overlap', 'occlusion']);   // they lie on and under yours on purpose
    });
    e.style.left = (-e.offsetWidth / 2) + 'px'; e.style.top = (-e.offsetHeight / 2) + 'px';
    return { wrap: wrap, el: e };
  }
  function create(ctx, viewer) {
    var T = ctx.T, V = ctx.layout.viewer, R = ctx.layout.rivals, c = function (n) { return T.cue(n); };
    var on = c('rival.in'), match = c('rival.match'), off = c('rival.off'), back = c('rival.back');
    var go = [c('rival.go1'), c('rival.go2'), c('rival.go3')], last = go[2] + 2;
    var rest = { x: V.x + V.settle[0], y: V.y + V.settle[1], r: V.r + V.settle[2] };
    var list = [2, 1, 0].map(function (i) {
      var s = slip(ctx, ctx.world, ctx.content.rival, V.w), d = i * R.fan;
      var under = { x: rest.x + R.under[0] + d, y: rest.y + R.under[1] + d * 0.6, r: R.under[2] + i * 2.2 };
      s.pos = A.paths({ x: under.x + 1100, y: under.y + 80, r: under.r + 10 }, [
        { t: on + i * 0.08, to: under, k: 120, d: 20 },
        { t: match + i * 0.05, to: { x: rest.x + i * 3, y: rest.y + i * 3, r: rest.r }, k: 160, d: 24 },
        { t: off + i * 0.07, to: { x: rest.x + R.off[0] + d, y: rest.y + R.off[1] + d, r: R.off[2] + i * 3 }, k: 80, d: 17 },
        { t: back + i * 0.08, to: { x: rest.x + R.back[0] + d, y: rest.y + R.back[1] + d * 0.6, r: R.back[2] + i * 1.5 }, k: 120, d: 20 },
        { t: go[2 - i], to: { x: rest.x + R.back[0] + 1350, y: rest.y + R.back[1] + 60, r: R.back[2] + 8 }, k: 90, d: 18 }   // top slip first
      ]);
      return s;
    });
    var back0 = { x: rest.x + R.back[0], y: rest.y + R.back[1] };
    return {
      edge: { x: back0.x - V.w / 2 + 6, y: back0.y },   // where the hand flicks them from (their left edge)
      render: function (t) {
        list.forEach(function (s, i) {
          var shown = t >= on && t < last;
          SS.dom.show(s.wrap, shown);
          if (!shown) return;
          var p = s.pos(t);
          s.wrap.style.zIndex = 205 + (2 - i);
          SS.dom.place(s.wrap, p.x, p.y, p.r, 1);
          s.el.style.boxShadow = '0 2px 3px rgba(52,38,22,0.22), 10px 16px 26px rgba(52,38,22,0.16)';
        });
      }
    };
  }
  SS.rivals = { create: create };
})((window.SS = window.SS || {}));
