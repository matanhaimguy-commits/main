// Tiny DOM helpers shared by the components.
(function (SS) {
  function el(tag, cls, parent, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text !== undefined) e.textContent = text;
    if (parent) parent.appendChild(e);
    return e;
  }
  function px(n) { return n.toFixed(2) + 'px'; }
  // world placement: x, y is the element's centre; r in degrees; s scale
  function place(e, x, y, r, s) {
    e.style.transform = 'translate(' + px(x) + ',' + px(y) + ') rotate(' + (r || 0).toFixed(3) + 'deg) scale(' + (s === undefined ? 1 : s).toFixed(4) + ')';
  }
  // display, not visibility: a child left at visibility:visible would still paint inside a hidden parent after a
  // backward seek, while display:none hides the whole subtree whatever its children say
  function show(e, on) { e.style.display = on ? '' : 'none'; }
  // mark deliberate layering for the HyperFrames layout audit (ink over type, paper over paper, tape over a name)
  function layered(e, kinds) { kinds.forEach(function (k) { e.setAttribute('data-layout-allow-' + k, ''); }); return e; }
  // rotate a local offset (dx, dy) by r degrees
  function rot(dx, dy, r) {
    var a = r * Math.PI / 180, c = Math.cos(a), s = Math.sin(a);
    return { x: dx * c - dy * s, y: dx * s + dy * c };
  }
  SS.dom = { el: el, px: px, place: place, show: show, layered: layered, rot: rot };
})((window.SS = window.SS || {}));
