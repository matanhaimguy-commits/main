// One continuous top-down shot. The camera eases between framings with a slow spring (pans, pull-backs, one
// push-in) and shakes the desk for 3 frames on every stamp hit.
(function (SS) {
  var SHAKE = [[3.5, -2.5], [-2.5, 2], [1.2, -1]];   // px offsets on the 3 frames after a hit
  function create(ctx, hits) {
    var L = ctx.layout, T = ctx.T, a = L.anchor, k0 = L.camera[0];
    var steps = L.camera.slice(1).map(function (c) { return { t: T.cue(c[0]), to: { x: c[1], y: c[2], s: c[3] }, k: 46, d: 13.5 }; });
    var cam = SS.anim.paths({ x: k0[1], y: k0[2], s: k0[3] }, steps);
    function shake(t) {
      for (var i = 0; i < hits.length; i++) {
        var f = Math.floor((t - hits[i]) * 30 + 1e-6);
        if (f >= 0 && f < SHAKE.length) return SHAKE[f];
      }
      return [0, 0];
    }
    function toScreen(t, wx, wy) {
      var c = cam(t), j = shake(t);
      return { x: a.x + c.s * (wx - c.x) + j[0], y: a.y + c.s * (wy - c.y) + j[1], s: c.s };
    }
    return {
      toScreen: toScreen,
      render: function (t) {
        var c = cam(t), j = shake(t);
        ctx.world.style.transform = 'translate(' + (a.x - c.s * c.x + j[0]).toFixed(2) + 'px,' + (a.y - c.s * c.y + j[1]).toFixed(2) + 'px) scale(' + c.s.toFixed(5) + ')';
      }
    };
  }
  SS.camera = { create: create };
})((window.SS = window.SS || {}));
