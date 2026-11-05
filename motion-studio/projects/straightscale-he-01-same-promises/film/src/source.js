// The data source under the key line while the headlines and the count are on screen.
(function (SS) {
  function create(ctx) {
    var T = ctx.T, lines = ctx.content.source;
    var box = SS.dom.el('div', 'source he', ctx.overlay);
    var items = lines.map(function (l) { return SS.words.build(box, [l], 'source-line'); });
    var tin = T.cue('source'), out = T.cue('stack');
    return { render: function (t) { items.forEach(function (it, i) { SS.words.render(t, it, [tin + i * 0.12], out); }); } };
  }
  SS.source = { create: create };
})((window.SS = window.SS || {}));
