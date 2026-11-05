// Covering the business name: on "תכסו" a finger's soft shadow slides over it, on "שם" the tape lands, on "האצבע"
// the finger presses the tape flat (the shadow tightens), on "ותקראו" the finger leaves.
(function (SS) {
  var A = SS.anim;
  function create(ctx, viewer) {
    var T = ctx.T;
    var tape = SS.dom.el('div', 'tape', viewer.name);
    tape.style.width = (viewer.nameText.offsetWidth + 70) + 'px';
    var finger = SS.dom.layered(SS.dom.el('div', 'finger-shadow', viewer.name), ['occlusion']);
    var tIn = T.cue('finger.in'), tTape = T.cue('tape'), tPress = T.cue('tape.press'), tOut = T.cue('finger.out');
    var land = A.path(0, [{ t: tTape, to: 1, k: 300, d: 26 }]);
    var press = A.path(0, [{ t: tPress, to: 1, k: 500, d: 26 }, { t: tPress + 0.22, to: 0.55, k: 200, d: 24 }]);
    var reach = A.path(0, [{ t: tIn, to: 1, k: 110, d: 19 }, { t: tOut, to: 0, k: 90, d: 18 }]);
    return {
      render: function (t) {
        SS.dom.show(tape, t >= tTape);
        var tp = land(t), pr = press(t);
        tape.style.transform = 'translate(' + (-140 * (1 - tp)).toFixed(1) + 'px,' + (-40 * (1 - tp)).toFixed(1) + 'px) rotate(' + (-2 - 7 * (1 - tp)).toFixed(2) + 'deg) scale(' + (1 + 0.18 * (1 - tp) - 0.035 * pr).toFixed(4) + ')';
        tape.style.boxShadow = '0 ' + (6 - 5 * pr).toFixed(1) + 'px ' + (10 - 8 * pr).toFixed(1) + 'px rgba(60,45,20,' + (0.18 - 0.1 * pr).toFixed(3) + ')';
        var f = reach(t);
        SS.dom.show(finger, f > 0.01);
        finger.style.transform = 'translate(' + (320 * (1 - f) - 18 * pr).toFixed(1) + 'px,' + (6 * pr).toFixed(1) + 'px) rotate(-5deg) scale(' + (1 - 0.08 * pr).toFixed(3) + ')';
        finger.style.opacity = (A.clamp(f) * (0.55 + 0.35 * pr)).toFixed(3);
      }
    };
  }
  SS.cover = { create: create };
})((window.SS = window.SS || {}));
