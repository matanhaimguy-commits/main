// The viewer's own slip: "המודעה שלכם", the business name, the headline line with its caret, the "דוגמה" tag. It
// lands, settles with a small bounce on its cue, and squares up when it is left alone on the desk. What happens in
// the headline line is headline.js; the tape and the finger's shadow cover.js; the underline underline.js.
(function (SS) {
  var A = SS.anim;
  function create(ctx) {
    var V = ctx.layout.viewer, T = ctx.T, C = ctx.content.viewer, X = ctx.example;
    var wrap = SS.dom.layered(SS.dom.el('div', 'slip-wrap', ctx.world), ['overflow']);   // the camera crops it on purpose
    var slip = SS.dom.el('div', 'slip viewer', wrap);
    slip.style.width = V.w + 'px';
    slip.style.backgroundImage = 'url(' + ctx.paper + ')';
    SS.dom.el('div', 'v-label he', slip, C.label);
    var name = SS.dom.el('div', 'v-name he', slip);
    var nameText = SS.dom.layered(SS.dom.el('span', 'v-name-text', name, C.name), ['occlusion']);   // the tape covers it
    var head = SS.dom.el('div', 'v-head he', slip);
    var headText = SS.dom.layered(SS.dom.el('span', 'v-head-text', head, C.headline), ['occlusion']);   // struck through on purpose
    var caret = SS.dom.el('span', 'caret', head);
    var rule = SS.dom.el('div', 'v-rule', slip);
    var tag = SS.dom.el('div', 'v-tag he', slip, ctx.content.example.label);
    var exampleOn = X.enabled && X.text;
    if (exampleOn) {   // the sample headline must fit the one line: shrink the line's type if it is longer
      headText.textContent = X.text;
      var room = head.clientWidth - caret.offsetWidth - 12, need = headText.offsetWidth;
      if (need > room) head.style.fontSize = Math.max(44, 74 * room / need).toFixed(1) + 'px';
    }
    var w = slip.offsetWidth, h = slip.offsetHeight;
    slip.style.left = (-w / 2) + 'px'; slip.style.top = (-h / 2) + 'px';
    // where it rests after settling; once squared up (r = 0) the caret's centre there is where the end card grows from
    var rest = { x: V.x + V.settle[0], y: V.y + V.settle[1], r: V.r + V.settle[2] };
    headText.textContent = '';
    var o = { x: caret.offsetLeft + caret.offsetWidth / 2 - w / 2, y: caret.offsetTop + caret.offsetHeight / 2 - h / 2 };
    headText.textContent = C.headline;
    var tDrop = T.cue('viewer.drop'), tSettle = T.cue('viewer.settle'), tSquare = T.cue('viewer.square');
    var height = A.path(1, [{ t: tDrop, to: 0, how: 'bounce', k: 230, d: 14 }, { t: tSettle, to: 0.07, k: 420, d: 30 }, { t: tSettle + 0.12, to: 0, how: 'bounce', k: 320, d: 14 }]);
    var pos = A.paths({ x: V.x + 60, y: V.y - 520, r: V.r + 9 }, [{ t: tDrop, to: { x: V.x, y: V.y, r: V.r }, k: 150, d: 24 }, { t: tSettle, to: rest, k: 260, d: 15 }, { t: tSquare, to: { r: 0 }, k: 200, d: 20 }]);
    return {
      wrap: wrap, slip: slip, name: name, nameText: nameText, head: head, headText: headText, caret: caret, tag: tag, rule: rule,
      caretSpot: { x: rest.x + o.x, y: rest.y + o.y, w: caret.offsetWidth, h: caret.offsetHeight },
      render: function (t) {
        var on = t >= tDrop;
        SS.dom.show(wrap, on);
        if (!on) return;
        var hh = height(t), p = pos(t);
        wrap.style.zIndex = 200;
        SS.dom.place(wrap, p.x, p.y, p.r, 1 + 0.42 * hh);
        slip.style.boxShadow = '0 ' + (2 + 4 * hh).toFixed(1) + 'px ' + (3 + 8 * hh).toFixed(1) + 'px rgba(52,38,22,' + (0.26 * (1 - hh)).toFixed(3) + '), ' +
          (8 + 46 * hh).toFixed(1) + 'px ' + (14 + 70 * hh).toFixed(1) + 'px ' + (22 + 40 * hh).toFixed(1) + 'px rgba(52,38,22,0.17)';
      }
    };
  }
  SS.viewer = { create: create };
})((window.SS = window.SS || {}));
