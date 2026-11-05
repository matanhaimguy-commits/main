// The counter: on every stamp hit the digit changes with a hard cut and a small pop (1 to 8; never a half-cut roller
// digit), then "מתוך 14" opens beside it and the group springs to centre. In RTL the digit sits on the right.
(function (SS) {
  var A = SS.anim;
  function create(ctx, hits) {
    var T = ctx.T, C = ctx.content.tally, me = {}, marks = hits.slice(0, C.count);
    me.mount = function (band, tin, tout) {
      var box = SS.dom.el('div', 'wline tally he', band);
      var mask = SS.dom.el('span', 'wmask', box), inner = SS.dom.el('span', 'winner tally-row', mask);
      var num = SS.dom.el('span', 'tally-num', inner, String(C.count));
      var rest = SS.dom.el('span', 'tally-rest', inner, C.of + ' ' + C.total);
      var shift = (rest.offsetWidth + parseFloat(getComputedStyle(rest).marginRight)) / 2;
      var open = A.path(0, [{ t: T.cue('tally.total'), to: 1, k: 240, d: 25 }]);
      var item = { line: box, spans: [inner] };
      me.render = function (t) {
        SS.words.render(t, item, [tin], tout);
        var n = 0, last = -Infinity;
        marks.forEach(function (h) { if (t >= h) { n++; last = h; } });
        num.textContent = String(n);
        num.style.transform = 'scale(' + (1 + 0.16 * Math.exp(-(t - last) * 14)).toFixed(4) + ')';
        var o = A.clamp(open(t));
        rest.style.clipPath = 'inset(0 0 0 ' + (100 - 100 * o).toFixed(2) + '%)';
        box.style.transform = 'translateX(' + (-shift * (1 - open(t))).toFixed(2) + 'px)';
      };
    };
    me.render = function () {};
    return me;
  }
  SS.tally = { create: create };
})((window.SS = window.SS || {}));
