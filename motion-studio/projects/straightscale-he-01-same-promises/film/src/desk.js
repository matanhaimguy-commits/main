// The desk: one marble surface under the whole film (one continuous top-down shot), with fine pores on top.
(function (SS) {
  SS.desk = {
    create: function (ctx) {
      var D = ctx.layout.desk, e = SS.dom.el('div', 'desk', ctx.world);
      e.setAttribute('data-layout-ignore', '');   // decorative surface, larger than the frame on purpose
      e.style.left = D.x + 'px'; e.style.top = D.y + 'px';
      e.style.width = D.w + 'px'; e.style.height = D.h + 'px';
      var veins = SS.textures.marble(Math.round(D.w / D.paint), Math.round(D.h / D.paint), D.paint, 2026);
      var pores = SS.textures.grain(220, 7, 0.05);
      e.style.backgroundImage = 'url(' + pores + '), url(' + veins + ')';
      e.style.backgroundSize = '220px 220px, 100% 100%';
      return { render: function () {} };
    }
  };
})((window.SS = window.SS || {}));
