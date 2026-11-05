// The viewer's own slip: "המודעה שלכם", the business name (covered by tape), the headline placeholder that is
// backspaced away, a blinking caret in the empty line, and the optional sample headline labelled דוגמה.
(function (SS) {
  var A = SS.anim;
  function create(ctx) {
    var V = ctx.layout.viewer, T = ctx.T, C = ctx.content.viewer, X = ctx.example;
    var wrap = SS.dom.el('div', 'slip-wrap', ctx.world);
    var slip = SS.dom.el('div', 'slip viewer', wrap);
    slip.style.width = V.w + 'px';
    slip.style.backgroundImage = 'url(' + ctx.paper + ')';
    SS.dom.el('div', 'v-label he', slip, C.label);
    var name = SS.dom.el('div', 'v-name he', slip);
    var nameText = SS.dom.layered(SS.dom.el('span', 'v-name-text', name, C.name), ['occlusion']);   // the tape covers it
    var tape = SS.dom.el('div', 'tape', name);
    var head = SS.dom.el('div', 'v-head he', slip);
    var headText = SS.dom.el('span', 'v-head-text', head, C.headline);
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
    tape.style.width = (nameText.offsetWidth + 70) + 'px';
    // caret centre on the desk once the line is empty (the end card grows out of it)
    headText.textContent = '';
    var local = { x: caret.offsetLeft + caret.offsetWidth / 2 - w / 2, y: caret.offsetTop + caret.offsetHeight / 2 - h / 2 };
    headText.textContent = C.headline;
    var o = SS.dom.rot(local.x, local.y, V.r);
    var tDrop = T.cue('viewer.drop'), tTape = T.cue('tape'), tRule = T.cue('underline'), tLit = T.cue('lights'), tClear = T.cue('clear'), tEx = T.cue('example');
    var height = A.path(1, [{ t: tDrop, to: 0, how: 'bounce', k: 230, d: 14 }]);
    var pos = A.paths({ x: V.x + 60, y: V.y - 520, r: V.r + 9 }, [{ t: tDrop, to: { x: V.x, y: V.y, r: V.r }, k: 150, d: 24 }]);
    var tapeIn = A.path(0, [{ t: tTape, to: 1, k: 300, d: 26 }]), ruleIn = A.path(0, [{ t: tRule, to: 1, k: 200, d: 26 }]);
    return {
      caret: { x: V.x + o.x, y: V.y + o.y, w: caret.offsetWidth, h: caret.offsetHeight },
      render: function (t) {
        var on = t >= tDrop;
        SS.dom.show(wrap, on);
        if (!on) return;
        var hh = height(t), p = pos(t);
        wrap.style.zIndex = 200;
        SS.dom.place(wrap, p.x, p.y, p.r, 1 + 0.42 * hh);
        slip.style.boxShadow = '0 ' + (2 + 4 * hh).toFixed(1) + 'px ' + (3 + 8 * hh).toFixed(1) + 'px rgba(52,38,22,' + (0.26 * (1 - hh)).toFixed(3) + '), ' +
          (8 + 46 * hh).toFixed(1) + 'px ' + (14 + 70 * hh).toFixed(1) + 'px ' + (22 + 40 * hh).toFixed(1) + 'px rgba(52,38,22,0.17)';
        var tp = tapeIn(t);
        SS.dom.show(tape, t >= tTape);
        tape.style.transform = 'translate(' + (-140 * (1 - tp)).toFixed(1) + 'px,' + (-40 * (1 - tp)).toFixed(1) + 'px) rotate(' + (-2 - 7 * (1 - tp)).toFixed(2) + 'deg) scale(' + (1 + 0.18 * (1 - tp)).toFixed(3) + ')';
        rule.style.transform = 'scaleX(' + A.clamp(ruleIn(t)).toFixed(4) + ')';
        // headline: placeholder, then backspaced (one char per 50 ms), then empty with a blinking caret
        var full = C.headline, n = full.length - Math.max(0, Math.floor((t - tClear) / 0.05 + 1e-6));
        var typing = exampleOn && t >= tEx, typed = typing ? X.text.slice(0, Math.floor((t - tEx) / 0.045 + 1e-6)) : '';
        headText.textContent = typing ? typed : full.slice(0, Math.max(0, n));
        headText.className = 'v-head-text' + (typing || (t >= tLit && t < tClear) ? ' typed' : '');
        SS.dom.show(tag, typing);
        var busy = (t >= tClear && n > 0) || (typing && typed.length < X.text.length);
        caret.style.opacity = t < tClear ? 0 : busy ? 1 : (Math.floor((t - tClear) / 0.53 + 1e-6) % 2 ? 0 : 1);
      }
    };
  }
  SS.viewer = { create: create };
})((window.SS = window.SS || {}));
