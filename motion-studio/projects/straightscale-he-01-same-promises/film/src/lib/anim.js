// Motion as a pure function of time. spring() and track() are copied from motion-studio/lib/motion.js (house springs);
// path() chains moves: each step starts at its time from wherever the value is and goes to `to` with a shape.
(function (SS) {
  function spring(t, k, d) {
    k = k || 170; d = d || 26;
    if (t <= 0) return 0;
    var w0 = Math.sqrt(k), z = d / (2 * w0);
    if (z < 1) {
      var wd = w0 * Math.sqrt(1 - z * z);
      return 1 - Math.exp(-z * w0 * t) * (Math.cos(wd * t) + (z * w0 / wd) * Math.sin(wd * t));
    }
    return 1 - Math.exp(-w0 * t) * (1 + w0 * t);
  }
  var clamp = function (x, a, b) { return Math.min(b === undefined ? 1 : b, Math.max(a || 0, x)); };
  // shapes: spring (default), bounce (spring reflected off the target: a drop that hits the desk), fall (gravity),
  // lin (constant speed), set (jump)
  function shape(st, dt) {
    if (dt <= 0) return 0;
    if (st.how === 'set') return 1;
    if (st.how === 'fall') return dt >= st.dur ? 1 : (dt / st.dur) * (dt / st.dur);
    if (st.how === 'lin') return clamp(dt / st.dur);
    if (st.how === 'bounce') { var b = spring(dt, st.k || 260, st.d || 13); return b > 1 ? 2 - b : b; }
    return spring(dt, st.k, st.d);
  }
  function path(v0, steps) {
    var s = steps.slice().sort(function (a, b) { return a.t - b.t; }), from = [];
    function at(t, n) {
      var i = -1;
      for (var j = 0; j < n; j++) if (s[j].t <= t) i = j;
      return i < 0 ? v0 : from[i] + (s[i].to - from[i]) * shape(s[i], t - s[i].t);
    }
    for (var i = 0; i < s.length; i++) from[i] = at(s[i].t, i);
    return function (t) { return at(t, s.length); };
  }
  // several channels at once: init {x, y, r}; steps [{t, to: {x, y}, how, k, d, dur}]
  function paths(init, steps) {
    var fns = {};
    Object.keys(init).forEach(function (key) {
      fns[key] = path(init[key], steps.filter(function (st) { return key in st.to; }).map(function (st) {
        return { t: st.t, to: st.to[key], how: st.how, k: st.k, d: st.d, dur: st.dur };
      }));
    });
    return function (t) {
      var out = {};
      for (var key in fns) out[key] = fns[key](t);
      return out;
    };
  }
  SS.anim = { spring: spring, clamp: clamp, path: path, paths: paths };
})((window.SS = window.SS || {}));
