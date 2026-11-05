// How the stamp looks from above: a dark rubber layer under a red wooden mount, a metal neck ring and a turned wooden
// handle (shaded, its top shifted toward the camera's corner, casting a shadow on the mount). Its other side is the
// rubber face with the word cut in mirror image, shown when the stamp is turned over (angle 90 to 270 degrees).
(function (SS) {
  function create(parent, faceWord, seed) {
    var top = SS.dom.el('div', 'stamp-top', parent);
    var rubber = SS.dom.el('div', 'stamp-rubber-under', top);
    var mount = SS.dom.el('div', 'stamp', top);
    SS.dom.el('div', 'stamp-bevel', mount);
    SS.dom.el('div', 'stamp-ferrule', mount);
    SS.dom.el('div', 'stamp-neck', mount);
    SS.dom.el('div', 'stamp-knob', mount);
    var face = SS.dom.el('div', 'stamp-face', parent);
    var plate = SS.dom.el('div', 'stamp-plate', face);
    var word = SS.dom.el('span', 'stamp-face-word he', plate, faceWord);
    var mask = 'url(' + SS.textures.ink(300, 130, seed) + ')';
    word.style.webkitMaskImage = mask; word.style.maskImage = mask;
    return {
      // h: height above the paper (0 = touching); angle: turn about the vertical axis, degrees
      paint: function (h, angle) {
        var c = Math.cos(angle * Math.PI / 180), showFace = c < 0, sx = Math.max(0.02, Math.abs(c)).toFixed(4);
        SS.dom.show(top, !showFace);
        SS.dom.show(face, showFace);
        (showFace ? face : top).style.transform = 'scaleX(' + sx + ')';
        var k = 'rgba(45,25,15,';
        rubber.style.boxShadow = '0 ' + (2 + 3 * h).toFixed(1) + 'px ' + (3 + 8 * h).toFixed(1) + 'px ' + k + (0.35 * Math.max(0, 1 - 3 * h)).toFixed(3) + '), ' +
          (10 + 70 * h).toFixed(1) + 'px ' + (16 + 100 * h).toFixed(1) + 'px ' + (14 + 60 * h).toFixed(1) + 'px ' + k + Math.max(0, 0.3 - 0.12 * h - 0.25 * Math.max(0, h - 0.5)).toFixed(3) + ')';
        face.style.boxShadow = rubber.style.boxShadow;
      }
    };
  }
  SS.stampBody = { create: create };
})((window.SS = window.SS || {}));
