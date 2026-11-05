// Captions in Heebo above the bottom safe zone: the spoken words the top band does not already show, in short
// chunks (a break after , . ? or every 5 words), each word rising on its own time. A chunk cuts out at the next.
(function (SS) {
  function chunks(T, keys) {
    var out = [];
    T.data.lines.forEach(function (line) {
      var key = keys.filter(function (k) { return k.line === line.id; })[0], cur = [], before = out.length;
      line.words.forEach(function (w, i) {
        if (key && i >= key.covers[0] && i <= key.covers[1]) { if (cur.length) out.push(cur); cur = []; return; }
        cur.push(w);
        if (/[,.?]$/.test(w.w) || cur.length === 5) { out.push(cur); cur = []; }
      });
      if (cur.length) out.push(cur);
      if (out.length > before) out[out.length - 1].end = line.end + 0.35;
    });
    return out;
  }
  function create(ctx) {
    var T = ctx.T, box = SS.dom.el('div', 'captions', ctx.overlay), end = T.cue('endcard');
    var list = chunks(T, ctx.content.keys).map(function (c) {
      var item = SS.words.build(box, c.map(function (w) { return w.w; }), 'cap');
      SS.words.balance(item);
      return { item: item, ins: c.map(function (w) { return w.s - 0.04; }), end: c.end };
    });
    list.forEach(function (c, i) {
      var next = i + 1 < list.length ? list[i + 1].ins[0] : end;
      c.out = Math.min(c.end || Infinity, next, end);
    });
    return { render: function (t) { list.forEach(function (c) { SS.words.render(t, c.item, c.ins, c.out, true); }); } };
  }
  SS.captions = { create: create };
})((window.SS = window.SS || {}));
