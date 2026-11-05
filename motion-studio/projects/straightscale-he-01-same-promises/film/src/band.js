// The top band: each spoken line's key words in Frank Ruhl Libre, word by word on the voice. A line leaves just
// before the next key arrives; the last one (line 11's pointer) stays until the end card. The tally takes line 3.
(function (SS) {
  var LEAD = 0.08;
  function create(ctx, tally) {
    var T = ctx.T, keys = ctx.content.keys;
    var band = SS.dom.el('div', 'band', ctx.overlay);
    var firsts = keys.map(function (k) { return k.tally ? T.cue('tally.in') : T.word(k.line, k.words[0][0]).s - LEAD; });
    var items = [];
    keys.forEach(function (k, i) {
      var out = i + 1 < keys.length ? firsts[i + 1] : T.cue('endcard');   // replaced by the next line, all at once
      if (k.tally) { tally.mount(band, firsts[i], out); return; }
      var item = SS.words.build(band, k.words.map(function (w) { return w[1]; }), 'key');
      if (k.one) SS.words.fit(item); else SS.words.balance(item);
      // a word spoken at the very start is already up on frame 0
      var ins = k.words.map(function (w) { var s = T.word(k.line, w[0]).s; return s < 0.05 ? -0.4 : s - LEAD; });
      items.push({ item: item, ins: ins, out: out });
    });
    return {
      render: function (t) {
        items.forEach(function (it) { SS.words.render(t, it.item, it.ins, it.out); });
        tally.render(t);
      }
    };
  }
  SS.band = { create: create };
})((window.SS = window.SS || {}));
