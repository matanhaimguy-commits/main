// The viewer's headline line, word by word with the voice: the placeholder lights up, is struck through on "תחליפו"
// and backspaced on "אותה"; on "במשהו" the old reflex "חינם" is typed, struck on "לא" and deleted on "יכול"; then
// the caret blinks in the empty line (or, if Matan switches it on, the sample headline labelled דוגמה is typed).
(function (SS) {
  var A = SS.anim, DEL = 0.05, TYPE = 0.07;
  function create(ctx, viewer) {
    var T = ctx.T, C = ctx.content, X = ctx.example, place = C.viewer.headline, old = C.retype;
    var exOn = X.enabled && X.text, c = function (n) { return T.cue(n); };
    var tLit = c('lights'), tStrike = c('strike'), tClear = c('clear'), tType = c('retype'), tUnsay = c('unsay'), tDel = c('unsay.del'), tEx = c('example');
    var strike = SS.dom.el('div', 'v-strike', viewer.head);
    strike.style.top = (viewer.head.offsetTop + viewer.head.offsetHeight * 0.52 - 3).toFixed(1) + 'px';
    var draw = A.path(0, [{ t: tStrike, to: 1, k: 300, d: 30 }, { t: tType, to: 0, how: 'set' }, { t: tUnsay, to: 1, k: 300, d: 30 }]);
    var count = function (t, t0, step) { return Math.max(0, Math.floor((t - t0) / step + 1e-6)); };
    function text(t) {
      if (exOn && t >= tEx) return X.text.slice(0, count(t, tEx, 0.045));
      if (t >= tDel) return old.slice(0, Math.max(0, old.length - count(t, tDel, DEL)));
      if (t >= tType) return old.slice(0, count(t, tType, TYPE));
      return place.slice(0, place.length - Math.min(place.length, count(t, tClear, DEL)));
    }
    return {
      render: function (t) {
        var s = text(t), typed = exOn && t >= tEx;
        viewer.headText.textContent = s;
        viewer.headText.className = 'v-head-text' + (typed || (t >= tLit && t < tClear) || (t >= tType && t < tEx) ? ' typed' : '');
        SS.dom.show(viewer.tag, typed);
        var w = s ? viewer.headText.offsetWidth : 0, k = typed ? 0 : A.clamp(draw(t));
        SS.dom.show(strike, w > 0 && k > 0.01);
        strike.style.width = (w * k).toFixed(1) + 'px';
        var empty = t >= tClear && s.length === 0, still = empty || (t >= tType && s === old && t < tUnsay) || (typed && s === X.text);
        var since = Math.max(tClear, t >= tDel ? tDel : tClear);
        viewer.caret.style.opacity = t < tClear ? 0 : !still ? 1 : (Math.floor((t - since) / 0.53 + 1e-6) % 2 ? 0 : 1);
      }
    };
  }
  SS.headline = { create: create };
})((window.SS = window.SS || {}));
