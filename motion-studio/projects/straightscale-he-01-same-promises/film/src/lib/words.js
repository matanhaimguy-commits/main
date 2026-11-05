// A line of words that rise into place one by one and leave the same way. No hard mask edge: each word rises a short
// way while its ink comes up from 60 % to full over 3 frames (never washed out, never half cut). A title too wide for
// its box breaks into two rows, the second right-aligned under the first (Hebrew reads from the right). Used by the
// top band, the captions and the end card.
(function (SS) {
  var A = SS.anim, RISE = 38, INK = 0.1, FIRST = 0.6, OUT = 0.16;   // % of word height, seconds, starting ink
  function build(parent, words, cls) {
    var line = SS.dom.el('div', 'wline he ' + (cls || ''), parent);
    var block = SS.dom.el('div', 'wblock', line), row = SS.dom.el('div', 'wrow', block);
    var spans = words.map(function (w) { return SS.dom.el('span', 'winner', SS.dom.el('span', 'wmask', row), w); });
    return { line: line, block: block, rows: [row], spans: spans };
  }
  function widths(item) {
    var gap = parseFloat(getComputedStyle(item.rows[0]).columnGap) || 0;
    var ws = item.spans.map(function (s) { return s.parentNode.offsetWidth; });
    return { gap: gap, ws: ws, sum: function (a, b) { var t = 0; for (var i = a; i < b; i++) t += ws[i] + (i > a ? gap : 0); return t; } };
  }
  // if the words do not fit on one row, move the tail into a second row so the two are nearly equal
  function balance(item) {
    var m = widths(item), n = m.ws.length;
    if (m.sum(0, n) <= item.line.clientWidth || n < 2) return;
    var best = 1, score = Infinity;
    for (var k = 1; k < n; k++) {
      var sc = Math.max(m.sum(0, k), m.sum(k, n));
      if (sc < score) { score = sc; best = k; }
    }
    var row2 = SS.dom.el('div', 'wrow', item.block);
    item.spans.slice(best).forEach(function (s) { row2.appendChild(s.parentNode); });
    item.rows.push(row2);
  }
  // shrink the font until the words fit on one row
  function fit(item) {
    var m = widths(item), max = item.line.clientWidth, fs = parseFloat(getComputedStyle(item.line).fontSize);
    var sum = m.sum(0, m.ws.length);
    if (sum > max) item.line.style.fontSize = (fs * max / sum * 0.98).toFixed(1) + 'px';
  }
  // ins: start time per word; out: time the line leaves (Infinity to stay); cut: vanish at out instead of leaving
  function render(t, item, ins, out, cut) {
    var on = t >= ins[0] - 0.001 && t < out + (cut ? 0 : OUT + 0.05);
    SS.dom.show(item.line, on);
    if (!on) return;
    item.spans.forEach(function (s, i) {
      var dt = t - ins[i], up = A.spring(dt, 520, 38), ink = dt < 0 ? 0 : FIRST + (1 - FIRST) * A.clamp(dt / INK);
      var leave = t >= out ? A.clamp((t - out) / OUT) : 0;
      s.style.transform = 'translateY(' + ((1 - up) * RISE + leave * leave * RISE).toFixed(2) + '%)';
      s.style.opacity = (ink * (1 - leave)).toFixed(3);
    });
  }
  SS.words = { build: build, balance: balance, fit: fit, render: render };
})((window.SS = window.SS || {}));
