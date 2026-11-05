// Wires the film together: reads timing.json, builds every part, and drives them from one paused GSAP timeline.
// Each part is a pure function of time (render(t)), so any frame can be painted cold, in any order.
(function (SS) {
  function variables() {
    var hf = window.__hyperframes, v = hf && hf.getVariables ? hf.getVariables() : {};
    return { enabled: !!v.exampleEnabled, text: v.exampleText || '' };
  }
  SS.main = {
    build: function (root, tl) {
      var T = SS.timing.make(SS.timing.load('timing.json'));
      var ctx = {
        T: T, layout: SS.layout, content: SS.content, example: variables(),
        world: root.querySelector('#world'), overlay: root.querySelector('#overlay'),
        paper: SS.textures.grain(256, 11, 0.07)
      };
      var desk = SS.desk.create(ctx);
      var pile = SS.pile.create(ctx);
      var stamp = SS.stamping.create(ctx, pile.slips);
      var sticker = SS.sticker.create(ctx, pile.slips[SS.layout.stack.order[SS.layout.stack.order.length - 1]], SS.content.sticker, T.cue('sticker'));
      var viewer = SS.viewer.create(ctx);
      var hint = SS.hint.create(ctx, SS.content.keys.filter(function (k) { return k.hint; })[0]);
      var camera = SS.camera.create(ctx, stamp.hits);
      var tally = SS.tally.create(ctx, stamp.hits);
      var parts = [desk, pile, sticker, viewer, hint, stamp, camera, SS.band.create(ctx, tally), SS.source.create(ctx),
        SS.captions.create(ctx), SS.endcard.create(ctx, camera, viewer.caret)];
      var render = function (t) { parts.forEach(function (p) { p.render(t); }); };
      // One linear tween is the film clock. Its property is a getter/setter, so GSAP paints the frame every time it
      // renders the tween, even when a seek suppresses callbacks (onUpdate would be skipped then); lazy: false so the
      // first render is never deferred to a later tick.
      var now = 0, clock = { t: function (v) { if (v === undefined) return now; now = v; render(v); } };
      tl.fromTo(clock, { t: 0 }, { t: T.duration, duration: T.duration, ease: 'none', lazy: false }, 0);
      render(0);
      return tl;
    }
  };
})((window.SS = window.SS || {}));
