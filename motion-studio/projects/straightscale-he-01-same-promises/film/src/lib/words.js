// A line of words that rise into place one by one and leave the same way. No hard mask edge: each word rises a short
// way while its ink comes up over 3 frames, so a glyph is never shown half cut (review D5). Used by the top band,
// the captions and the end card.
(function (SS) {
  var A = SS.anim, RISE = 38, INK = 0.1, OUT = 0.16;   // % of the word's height, seconds
  function build(parent, words, cls) {
    var line = SS.dom.el('div', 'wline he ' + (cls || ''), parent);
    var spans = words.map(function (w, i) {
      var mask = SS.dom.el('span', 'wmask', line);
      var inner = SS.dom.el('span', 'winner', mask, w);
      if (i < words.length - 1) line.appendChild(document.createTextNode(' '));
      return inner;
    });
    return { line: line, spans: spans };
  }
  // if the words do not fit on one line, break into two lines of nearly equal width (never a lone last word)
  function balance(item) {
    var masks = item.spans.map(function (s) { return s.parentNode; });
    var gap = parseFloat(getComputedStyle(item.line).columnGap) || 0, max = item.line.clientWidth;
    var ws = masks.map(function (m) { return m.offsetWidth; });
    var sum = function (a, b) { var t = 0; for (var i = a; i < b; i++) t += ws[i] + (i > a ? gap : 0); return t; };
    if (sum(0, ws.length) <= max || ws.length < 2) return;
    var best = 1, score = Infinity;
    for (var k = 1; k < ws.length; k++) {
      var sc = Math.max(sum(0, k), sum(k, ws.length));
      if (sc < score) { score = sc; best = k; }
    }
    item.line.insertBefore(SS.dom.el('span', 'wbreak'), masks[best]);
  }
  // shrink the font until the words fit on one line
  function fit(item) {
    var max = item.line.clientWidth, fs = parseFloat(getComputedStyle(item.line).fontSize);
    var masks = item.spans.map(function (s) { return s.parentNode; }), gap = parseFloat(getComputedStyle(item.line).columnGap) || 0;
    var sum = masks.reduce(function (a, m) { return a + m.offsetWidth; }, 0) + gap * (masks.length - 1);
    if (sum > max) item.line.style.fontSize = (fs * max / sum * 0.98).toFixed(1) + 'px';
  }
  // ins: start time per word; out: time the line leaves (Infinity to stay); cut: vanish at out instead of leaving
  function render(t, item, ins, out, cut) {
    var on = t >= ins[0] - 0.001 && t < out + (cut ? 0 : OUT + 0.05);
    SS.dom.show(item.line, on);
    if (!on) return;
    item.spans.forEach(function (s, i) {
      var up = A.spring(t - ins[i], 520, 38), ink = A.clamp((t - ins[i]) / INK);
      var leave = t >= out ? A.clamp((t - out) / OUT) : 0;
      s.style.transform = 'translateY(' + ((1 - up) * RISE + leave * leave * RISE).toFixed(2) + '%)';
      s.style.opacity = (ink * (1 - leave)).toFixed(3);
    });
  }
  SS.words = { build: build, balance: balance, fit: fit, render: render };
})((window.SS = window.SS || {}));
