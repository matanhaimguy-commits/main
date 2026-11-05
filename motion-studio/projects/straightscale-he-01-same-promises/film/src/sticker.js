// The gold price sticker: no price, just "₪?". It is slapped onto the top slip of the stack at `at` and rides with it.
(function (SS) {
  var A = SS.anim;
  function create(ctx, slip, text, at) {
    var e = SS.dom.el('div', 'sticker', slip.el);
    SS.dom.el('span', 'sticker-text', e, text);
    var x = slip.w / 2 - 34, y = -slip.h / 2 - 26, r = -9;   // overhangs the top-right corner
    var land = A.path(0, [{ t: at, to: 1, how: 'bounce', k: 520, d: 20 }]);
    return {
      render: function (t) {
        var on = t >= at;
        SS.dom.show(e, on);
        if (!on) return;
        var h = 1 - land(t);
        SS.dom.place(e, x - 40 * h, y - 60 * h, r - 16 * h, 1 + 0.7 * h);
        e.style.boxShadow = '0 ' + (2 + 30 * h).toFixed(1) + 'px ' + (3 + 30 * h).toFixed(1) + 'px rgba(60,35,5,' + (0.35 - 0.15 * h).toFixed(3) + ')';
      }
    };
  }
  SS.sticker = { create: create };
})((window.SS = window.SS || {}));
