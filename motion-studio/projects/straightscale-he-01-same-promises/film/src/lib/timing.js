// Reads the ONE timing file (timing.json: lines, words, cues, tail). Every time in the film comes from here, so new
// voice timings (tools/retime.py) move the whole film without touching code. Cues are anchored to a line or a word:
// {line, word?, edge?: "start"|"end", offset?, every?} or {at: seconds}.
(function (SS) {
  function load(url) {
    var x = new XMLHttpRequest();
    x.open('GET', url, false);
    x.send(null);
    return JSON.parse(x.responseText);
  }
  function make(data) {
    var byId = {};
    data.lines.forEach(function (l) { byId[l.id] = l; });
    function line(id) { return byId[id]; }
    function word(id, i) { var ws = byId[id].words; return ws[i < 0 ? ws.length + i : i]; }
    function spec(name) {
      var c = data.cues[name];
      if (!c) throw new Error('timing.json has no cue "' + name + '"');
      return c;
    }
    function cue(name) {
      var c = spec(name), base;
      if (c.at !== undefined) base = c.at;
      else if (c.word !== undefined) base = word(c.line, c.word).s;
      else base = c.edge === 'end' ? byId[c.line].end : byId[c.line].start;
      return base + (c.offset || 0);
    }
    var last = data.lines[data.lines.length - 1];
    return { data: data, line: line, word: word, cue: cue, spec: spec, duration: +(last.end + data.tail).toFixed(3) };
  }
  SS.timing = { load: load, make: make };
})((window.SS = window.SS || {}));
