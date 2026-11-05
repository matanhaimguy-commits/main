// Textures painted once at build time from seeded noise (marble desk, paper grain, uneven stamp ink), as data URLs.
(function (SS) {
  var R = SS.rng;
  function canvas(w, h) { var c = document.createElement('canvas'); c.width = w; c.height = h; return c; }
  function smooth(a, b, x) { var u = Math.min(1, Math.max(0, (x - a) / (b - a))); return u * u * (3 - 2 * u); }

  // Marble #EDE4D6 with faint, soft veins. Painted at 1/scale of world size and stretched (veins are soft anyway).
  function marble(w, h, scale, seed) {
    var c = canvas(w, h), g = c.getContext('2d'), img = g.createImageData(w, h), d = img.data;
    var base = [237, 228, 214], vein = [196, 184, 166];
    for (var y = 0; y < h; y++) for (var x = 0; x < w; x++) {
      var wx = x * scale, wy = y * scale;
      var mott = (R.fbm(wx / 900, wy / 900, seed, 4) - 0.5) * 0.045;
      var warp = R.fbm(wx / 650, wy / 650, seed + 7, 4) * 7.5;
      var v1 = Math.abs(Math.sin((wx * 0.0011 + wy * 0.0007) * 6.283 + warp));
      var v2 = Math.abs(Math.sin((wx * -0.0006 + wy * 0.0019) * 6.283 + warp * 0.8 + 2.1));
      var vv = (1 - smooth(0, 0.05, v1)) * 0.42 * R.fbm(wx / 400, wy / 400, seed + 11, 2)
             + (1 - smooth(0, 0.03, v2)) * 0.22 * R.fbm(wx / 300, wy / 300, seed + 13, 2);
      var i = (y * w + x) * 4;
      for (var k = 0; k < 3; k++) d[i + k] = (base[k] + (vein[k] - base[k]) * vv) * (1 + mott);
      d[i + 3] = 255;
    }
    g.putImageData(img, 0, 0);
    return c.toDataURL('image/png');
  }

  // Fine grain tile (paper fibre or marble pores): transparent speckle to lay over a flat colour.
  function grain(size, seed, strength) {
    var c = canvas(size, size), g = c.getContext('2d'), img = g.createImageData(size, size), d = img.data;
    var rnd = R.mulberry32(seed);
    for (var i = 0; i < size * size; i++) {
      var n = rnd(), fibre = R.noise2((i % size) / 3, Math.floor(i / size) / 14, seed) > 0.78 ? 1 : 0;
      var dark = n < 0.5;
      d[i * 4] = d[i * 4 + 1] = d[i * 4 + 2] = dark ? 60 : 255;
      d[i * 4 + 3] = Math.round((Math.abs(n - 0.5) * 2 * strength + fibre * strength * 0.6) * 255);
    }
    g.putImageData(img, 0, 0);
    return c.toDataURL('image/png');
  }

  // Alpha mask for a rubber-stamp print: patchy coverage, dry streaks and pinholes, so the ink is never flat.
  function ink(w, h, seed) {
    var c = canvas(w, h), g = c.getContext('2d'), img = g.createImageData(w, h), d = img.data;
    for (var y = 0; y < h; y++) for (var x = 0; x < w; x++) {
      var cover = 0.84 + 0.6 * (R.fbm(x / 22, y / 22, seed, 3) - 0.42);
      var streak = R.noise2(x / 70, y / 2.6, seed + 3) > 0.76 ? 0.62 : 1;
      var hole = R.hash2(x, y, seed + 5) < 0.03 ? 0.25 : 1;
      var a = Math.min(1, Math.max(0.12, cover)) * streak * hole;
      var i = (y * w + x) * 4;
      d[i] = d[i + 1] = d[i + 2] = 0; d[i + 3] = Math.round(a * 255);
    }
    g.putImageData(img, 0, 0);
    return c.toDataURL('image/png');
  }
  SS.textures = { marble: marble, grain: grain, ink: ink };
})((window.SS = window.SS || {}));
