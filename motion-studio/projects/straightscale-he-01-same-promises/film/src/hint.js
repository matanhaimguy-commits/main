// The pointer under the viewer's slip ("מה קורה אצלכם בפגישה הראשונה?"), word by word on the voice.
(function (SS) {
  function create(ctx, key) {
    var V = ctx.layout.viewer, T = ctx.T;
    var box = SS.dom.el('div', 'hint', ctx.world);
    box.style.left = (V.x - 470) + 'px'; box.style.top = (V.y + 205) + 'px';
    var item = SS.words.build(box, key.words.map(function (w) { return w[1]; }), 'hint-line');
    var ins = key.words.map(function (w) { return T.word(key.line, w[0]).s - 0.06; });
    var out = T.cue('cam.caret');   // it drops out as the camera pushes into the caret
    return { render: function (t) { box.style.zIndex = 210; SS.words.render(t, item, ins, out); } };
  }
  SS.hint = { create: create };
})((window.SS = window.SS || {}));
