// The red rubber stamp, seen from above. Height h (0 = on the paper) scales it toward the camera and throws its
// shadow; a hit falls fast (gravity), squashes for 2 frames and lifts. plan() turns hits and moves into paths.
(function (SS) {
  var A = SS.anim;
  function create(ctx) {
    var wrap = SS.dom.layered(SS.dom.el('div', 'stamp-wrap', ctx.world), ['overflow']);   // it enters and leaves past the edges
    var body = SS.dom.el('div', 'stamp', wrap);
    SS.dom.el('div', 'stamp-rubber', body);
    SS.dom.el('div', 'stamp-knob', body);
    var me = { el: wrap, hits: [], gone: Infinity };
    me.plan = function (start, events) {
      var xyr = [], hs = [], free = -Infinity;
      events.slice().sort(function (a, b) { return a.t - b.t; }).forEach(function (ev) {
        var pose = { x: ev.x, y: ev.y, r: ev.r };
        if (ev.kind === 'move') {
          xyr.push({ t: ev.t, to: pose, k: ev.k || 120, d: ev.d || 22 });
          hs.push({ t: ev.t, to: ev.h, k: ev.k || 120, d: ev.d || 22 });
          return;
        }
        var gap = Math.min(1, ev.t - free), fall = Math.min(0.12, 0.35 * gap);
        var ts = Math.max(free, ev.t - 0.45), travel = Math.max(0.08, ev.t - fall - ts);
        var k = Math.pow(5 / travel, 2), d = 2 * Math.sqrt(k), lift = Math.min(0.55, 0.15 + 0.6 * gap);
        xyr.push({ t: ts, to: pose, k: k, d: d });
        hs.push({ t: ts, to: lift, k: k, d: d });
        hs.push({ t: ev.t - fall, to: 0, how: 'fall', dur: fall });
        free = ev.t + Math.min(0.14, 0.4 * gap);
        hs.push({ t: free, to: 0.45, k: 240, d: 22 });
        me.hits.push(ev.t);
      });
      me.pos = A.paths({ x: start.x, y: start.y, r: start.r }, xyr);
      me.height = A.path(start.h, hs);
    };
    me.render = function (t) {
      SS.dom.show(wrap, t < me.gone);
      if (t >= me.gone) return;
      var p = me.pos(t), h = Math.max(0, me.height(t)), squash = 1;
      me.hits.forEach(function (th) { if (t >= th && t < th + 0.067) squash = 0.965; });
      SS.dom.place(wrap, p.x, p.y, p.r, (1 + 0.85 * h) * squash);
      var c = 'rgba(45,25,15,';
      body.style.boxShadow = '0 ' + (2 + 3 * h).toFixed(1) + 'px ' + (3 + 8 * h).toFixed(1) + 'px ' + c + (0.35 * Math.max(0, 1 - 3 * h)).toFixed(3) + '), ' +
        (10 + 70 * h).toFixed(1) + 'px ' + (16 + 100 * h).toFixed(1) + 'px ' + (14 + 60 * h).toFixed(1) + 'px ' + c + Math.max(0, 0.3 - 0.12 * h - 0.1 * Math.max(0, h - 1)).toFixed(3) + ')';
    };
    return me;
  }
  SS.stamp = { create: create };
})((window.SS = window.SS || {}));
