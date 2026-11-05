// A rubber-stamp print: one word in uneven red ink inside a double border, multiplied into the paper so the typed
// headline shows through. Every print has the same face size (one stamp); the word is fitted inside it.
(function (SS) {
  var FACE = { w: 400, h: 160 }, A = SS.anim;
  function create(slipEl, word, seed, slipW) {
    var rnd = SS.rng.mulberry32(seed);
    var e = SS.dom.el('div', 'print', slipEl);
    var w = SS.dom.layered(SS.dom.el('span', 'print-word he', e, word), ['overlap', 'occlusion']);
    e.style.width = FACE.w + 'px'; e.style.height = FACE.h + 'px';
    var natural = w.offsetWidth;
    w.style.fontSize = Math.min(124, 112 * (FACE.w - 64) / natural).toFixed(1) + 'px';
    var mask = 'url(' + SS.textures.ink(FACE.w, FACE.h, seed) + ')';
    e.style.webkitMaskImage = mask; e.style.maskImage = mask;
    var left = 20 + rnd() * 6, top = slipEl.offsetHeight - FACE.h - 10 - rnd() * 6, r = (rnd() < 0.5 ? -1 : 1) * (2.5 + rnd() * 4);
    e.style.left = left + 'px'; e.style.top = top + 'px';
    var print = {
      el: e, r: r,
      // centre of the face in slip-local px (from the slip's top-left)
      cx: left + FACE.w / 2, cy: top + FACE.h / 2,
      at: Infinity,
      render: function (t) {
        var dt = t - print.at, on = dt >= 0;
        SS.dom.show(e, on);
        if (!on) return;
        var spread = A.clamp(dt / 0.08);              // ink spreads in 80 ms
        e.style.transform = 'rotate(' + r.toFixed(2) + 'deg) scale(' + (0.97 + 0.03 * spread).toFixed(4) + ')';
        e.style.opacity = (0.84 + 0.14 * spread).toFixed(3);
        w.style.textShadow = '0 0 ' + (0.4 + 1.4 * spread).toFixed(2) + 'px rgba(190,15,24,0.55)';
      }
    };
    return print;
  }
  SS.ink = { create: create, FACE: FACE };
})((window.SS = window.SS || {}));
