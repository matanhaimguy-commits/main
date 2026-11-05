// The counter: a digit that rolls up one step on every stamp hit (1 to 8), then "מתוך 14" opens beside it and the
// group springs to centre. In RTL the digit sits on the right: "8 מתוך 14".
(function (SS) {
  var A = SS.anim;
  function create(ctx, hits) {
    var T = ctx.T, C = ctx.content.tally, me = {};
    me.mount = function (band, tin, tout) {
      var box = SS.dom.el('div', 'wline tally he', band);
      var mask = SS.dom.el('span', 'wmask', box), inner = SS.dom.el('span', 'winner tally-row', mask);
      var num = SS.dom.el('span', 'tally-num', inner), roll = SS.dom.layered(SS.dom.el('span', 'tally-roll', num), ['overflow']);
      for (var i = 0; i <= C.count; i++) SS.dom.layered(SS.dom.el('span', 'tally-digit', roll, String(i)), ['overlap']);   // hidden in the window
      var rest = SS.dom.el('span', 'tally-rest', inner, C.of + ' ' + C.total);
      var cell = num.offsetHeight, shift = (rest.offsetWidth + parseFloat(getComputedStyle(rest).marginRight)) / 2;
      var tt = T.cue('tally.total');
      var count = A.path(0, hits.slice(0, C.count).map(function (h, i) { return { t: h, to: i + 1, k: 3000, d: 110 }; }));   // critically damped, about 3 frames
      var open = A.path(0, [{ t: tt, to: 1, k: 240, d: 25 }]);
      var item = { line: box, spans: [inner] };
      me.render = function (t) {
        SS.words.render(t, item, [tin], tout);
        roll.style.transform = 'translateY(' + (-count(t) * cell).toFixed(2) + 'px)';
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
