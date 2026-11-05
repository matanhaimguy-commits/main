// The headline line's underline draws in four steps, one on each word of "ותקראו רק את הכותרת".
(function (SS) {
  function create(ctx, viewer) {
    var T = ctx.T, steps = ['rule.1', 'rule.2', 'rule.3', 'rule.4'];
    var draw = SS.anim.path(0, steps.map(function (c, i) { return { t: T.cue(c), to: (i + 1) / steps.length, k: 320, d: 30 }; }));
    return { render: function (t) { viewer.rule.style.transform = 'scaleX(' + SS.anim.clamp(draw(t)).toFixed(4) + ')'; } };
  }
  SS.underline = { create: create };
})((window.SS = window.SS || {}));
