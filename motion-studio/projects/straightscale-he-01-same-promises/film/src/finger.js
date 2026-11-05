// The shadow of a pointing hand: a tapered fingertip, the thumb lying along the index finger, a knuckle step, then
// the back of the hand with the curled fingers, soft-edged. Drawn as SVG; cover.js (from the right) and hand.js
// (mirrored, from the left) move the same shape, so it is one hand all film long.
(function (SS) {
  var NS = 'http://www.w3.org/2000/svg';
  var HAND = 'M18 150 C18 124 36 112 66 110 L222 104 C226 88 238 72 262 68 C296 62 330 66 352 74 C420 60 520 36 640 34 L1000 30 L1000 330 ' +
    'L664 298 C626 300 604 282 572 280 C542 278 522 264 494 264 C464 264 446 250 420 246 C382 240 352 226 330 214 ' +
    'C316 208 302 202 284 200 L66 190 C38 188 18 176 18 150 Z';
  function create(parent) {
    var svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('viewBox', '0 0 1000 360');
    svg.setAttribute('class', 'finger-shadow');
    var path = document.createElementNS(NS, 'path');
    path.setAttribute('d', HAND);
    path.setAttribute('fill', 'rgba(40, 26, 12, 0.62)');
    svg.appendChild(path);
    parent.appendChild(svg);
    return SS.dom.layered(svg, ['occlusion']);
  }
  SS.finger = { create: create };
})((window.SS = window.SS || {}));
