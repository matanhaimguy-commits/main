// The gold price tag: no price, just "₪?" (read right to left: shekel, then the question). Heebo 800, not the serif,
// so the shekel never reads as letters. It is slapped onto the top slip of the stack at `at` and rides with it.
(function (SS) {
  var A = SS.anim;
  function create(ctx, slip, text, at) {
    var e = SS.dom.el('div', 'sticker-wrap', slip.el), tag = SS.dom.el('div', 'sticker', e);   // the wrap carries the shadow
    SS.dom.el('span', 'sticker-hole', tag);
    SS.dom.el('span', 'sticker-text he', tag, text);
    var x = slip.w / 2 - 130, y = -slip.h / 2 - 58, r = -9;   // on the top edge, clear of the headline and the right UI zone
    var land = A.path(0, [{ t: at, to: 1, how: 'bounce', k: 520, d: 20 }]);
    return {
      render: function (t) {
        var on = t >= at;
        SS.dom.show(e, on);
        if (!on) return;
        var h = 1 - land(t);
        SS.dom.place(e, x - 40 * h, y - 60 * h, r - 16 * h, 1 + 0.7 * h);
        e.style.filter = 'drop-shadow(0 ' + (2 + 30 * h).toFixed(1) + 'px ' + (2 + 14 * h).toFixed(1) + 'px rgba(60,35,5,' + (0.4 - 0.15 * h).toFixed(3) + '))';
      }
    };
  }
  SS.sticker = { create: create };
})((window.SS = window.SS || {}));
