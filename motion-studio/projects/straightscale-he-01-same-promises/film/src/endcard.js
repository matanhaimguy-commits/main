// The end card grows out of the blinking caret: a charcoal block opens from the caret to the full frame, then the
// white wordmark (the official file, never redrawn) and the soft call to action rise in once the card has cleared
// them (no mask edge ever cuts the logo), both centred on x = 540.
// A caret blinks after the call to action, placed outside the centred text so it never pulls it off centre.
(function (SS) {
  var A = SS.anim;
  function create(ctx, camera, caret) {
    var T = ctx.T, t0 = T.cue('endcard');
    var card = SS.dom.el('div', 'endcard', ctx.overlay);
    var markMask = SS.dom.el('div', 'ec-mark-mask', card);
    var mark = SS.dom.el('img', 'ec-mark', markMask);
    mark.src = 'assets/brand/wordmark-white.png'; mark.alt = 'StraightScale';
    var cta = SS.words.build(card, ctx.content.cta.split(' '), 'ec-cta');
    var ctaIns = cta.spans.map(function (s, i) { return t0 + 0.95 + i * 0.07; });
    var caretEl = SS.dom.el('span', 'ec-caret', card), caretAt = ctaIns[ctaIns.length - 1] + 0.2;
    var first = cta.spans[0].parentNode, last = cta.spans[cta.spans.length - 1].parentNode;   // RTL: last word is leftmost
    caretEl.style.left = (cta.line.offsetLeft + last.offsetLeft - 22).toFixed(1) + 'px';
    caretEl.style.top = (cta.line.offsetTop + first.offsetTop + (first.offsetHeight - 64) / 2).toFixed(1) + 'px';
    // the card is fully open about 0.5 s after t0; the logo and the words start after that, so no edge ever cuts them
    var open = A.path(0, [{ t: t0, to: 1, k: 90, d: 17 }]), tMark = t0 + 0.55, rise = A.path(0, [{ t: tMark, to: 1, k: 260, d: 27 }]);
    return {
      render: function (t) {
        var on = t >= t0;
        SS.dom.show(card, on);
        SS.dom.show(ctx.world, !(on && open(t) > 0.998));   // nothing of the desk is left to paint under a closed card
        if (!on) return;
        var c = camera.toScreen(t0, caret.x, caret.y), o = A.clamp(open(t));
        var hw = caret.w * c.s / 2 + 8, hh = caret.h * c.s / 2;
        var top = (c.y - hh) * (1 - o), bottom = (1920 - c.y - hh) * (1 - o), left = (c.x - hw) * (1 - o), right = (1080 - c.x - hw) * (1 - o);
        card.style.clipPath = 'inset(' + [top, right, bottom, left].map(function (v) { return v.toFixed(2) + 'px'; }).join(' ') + ')';
        mark.style.transform = 'translateY(' + ((1 - rise(t)) * 14).toFixed(2) + '%)';
        mark.style.opacity = (t < tMark ? 0 : 0.6 + 0.4 * A.clamp((t - tMark) / 0.1)).toFixed(3);
        SS.words.render(t, cta, ctaIns, Infinity);
        caretEl.style.opacity = t < caretAt ? 0 : Math.floor((t - caretAt) / 0.53 + 1e-6) % 2 ? 0 : 1;
      }
    };
  }
  SS.endcard = { create: create };
})((window.SS = window.SS || {}));
