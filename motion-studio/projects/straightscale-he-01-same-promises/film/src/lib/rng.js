// Seeded randomness and value noise. Never Math.random: the same seed gives the same desk, paper and ink every frame.
(function (SS) {
  function mulberry32(seed) {
    var a = seed >>> 0;
    return function () {
      a = (a + 0x6d2b79f5) >>> 0;
      var t = Math.imul(a ^ (a >>> 15), 1 | a);
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function hash2(x, y, seed) {
    var h = Math.imul(x | 0, 374761393) ^ Math.imul(y | 0, 668265263) ^ Math.imul(seed | 0, 2246822519);
    h = Math.imul(h ^ (h >>> 13), 1274126177);
    return ((h ^ (h >>> 16)) >>> 0) / 4294967296;
  }
  function noise2(x, y, seed) {
    var xi = Math.floor(x), yi = Math.floor(y), u = x - xi, v = y - yi;
    u = u * u * (3 - 2 * u); v = v * v * (3 - 2 * v);
    var a = hash2(xi, yi, seed), b = hash2(xi + 1, yi, seed), c = hash2(xi, yi + 1, seed), d = hash2(xi + 1, yi + 1, seed);
    return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
  }
  function fbm(x, y, seed, octaves) {
    var sum = 0, amp = 0.5, f = 1;
    for (var i = 0; i < octaves; i++) { sum += amp * noise2(x * f, y * f, seed + i * 31); f *= 2; amp *= 0.5; }
    return sum / (1 - Math.pow(0.5, octaves));
  }
  SS.rng = { mulberry32: mulberry32, hash2: hash2, noise2: noise2, fbm: fbm };
})((window.SS = window.SS || {}));
