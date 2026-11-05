// Where things are on the desk (world px; at camera scale 1 a world px is a screen px) and how the camera frames
// them. Times are never written here: every move is tied to a cue in timing.json.
(function (SS) {
  SS.layout = {
    anchor: { x: 490, y: 950 },            // screen point the camera centres on (clear of the right 140 px UI)
    desk: { x: -800, y: -800, w: 3400, h: 3600, paint: 6 },
    // pile: centre x, y, settle rotation (deg) after the drop; drop: where it falls in from (offset, extra spin)
    pile: {
      p1: [500, 1010, -2],
      p7: [230, 560, -1.5], o3: [850, 535, 2.5], p3: [190, 775, 1.5], p2: [860, 770, 2],
      p5: [205, 1250, -2.5], p4: [825, 1245, 1.5], p6: [270, 1470, 2.5], p8: [840, 1478, -1],
      o1: [-300, 1010, 3.5], o2: [1300, 1010, -3], o4: [-270, 1390, -1.5], o5: [1290, 640, 2], o6: [1330, 1430, -4]
    },
    cascade: ['p3', 'o5', 'p2', 'p5', 'p4', 'p7', 'o3', 'o1', 'p6', 'o2', 'o4', 'o6', 'p8'],   // middle rows first: no empty band
    // stamping order: hook, the four free slips (the last on the word חינם), the three save slips
    hits: { hook: 'p1', free: ['p3', 'p5', 'p2', 'p4'], save: ['p7', 'p6', 'p8'] },
    // the neat stack, bottom to top; left edges aligned so the prints line up in one column
    stack: { order: ['p6', 'p7', 'p8', 'p2', 'p3', 'p4', 'p5', 'p1'], left: 130, bottom: 1000, step: 30, every: 0.09 },
    // the six unstamped slips are pushed straight off the desk (they never come back into the shot)
    leave: { o1: [-1300, 0], o2: [1300, 0], o3: [0, -1500], o4: [-1300, 0], o5: [1300, 0], o6: [1300, 0] },
    stage: { x: 500, y: 975 },              // the cleared middle of the desk, for lines 6 to 12
    viewer: { x: 500, y: 1040, r: -0.8, w: 820, settle: [14, 6, 1.4] },
    // the competitors' slips, offsets from your settled slip: under it (below the headline), parted to the lower right
    rivals: { under: [30, 350, 2.5], part: [440, 330, -6], fan: 16 },   // tilts keep their edges off your headline   // settle: where the small bounce leaves it
    stamp: {
      start: { x: -760, y: 300, r: -18, h: 1.3 },
      wait: { x: -180, y: 945, r: -9, h: 0.42 },   // hovering at the left edge during the cascade
      ready: { x: -90, y: 880, r: -3, h: 0.62 },   // rising toward the pile just before the stamping starts
      parkPile: { x: 1160, y: 905, r: 8 },         // resting at the right edge of the pile after the last hit
      parkStack: { x: 120, y: 660, r: -7 },        // resting at the top left beside the stack
      parkViewer: { x: 240, y: 745, r: -6 },       // beside the viewer's slip
      hookLift: { dx: 40, dy: -265, r: -12, h: 0.25 },  // hovering above the hook slip after the first hit
      hover: [-262, 42],                            // offset from the viewer's slip: over its empty left, beside the headline
      exit: { x: -950, y: 820, r: -22, h: 2.0 }        // lifting toward the camera and out to the left
    },
    // framings [cue, focus x, focus y, scale]; from line 7 on the camera follows the action on the words: the
    // finger to the name, the underline as it draws right to left, the hover's dip, the backspaced line, the pointer
    camera: [
      ['start', 500, 880, 1.3], ['cam.pull', 520, 1050, 0.7], ['cam.ads', 500, 1030, 0.8], ['hits.free', 520, 1050, 0.72],
      ['stack', 480, 1000, 0.64], ['cam.stack', 470, 940, 1.3],
      ['cam.choose', 470, 915, 1.34], ['stack.away', 500, 935, 1.35],
      ['viewer.drop', 500, 960, 1.08], ['viewer.settle', 505, 975, 1.13],
      ['finger.in', 650, 990, 1.3], ['tape', 650, 995, 1.32], ['tape.press', 655, 1000, 1.37],
      ['rule.1', 690, 1080, 1.28], ['rule.2', 560, 1085, 1.26], ['rule.3', 440, 1085, 1.26], ['rule.4', 500, 1060, 1.12],
      ['hover', 470, 1190, 1.0], ['hover.drift', 450, 1185, 1.03], ['hover.dip', 470, 1200, 1.08], ['hover.lift', 480, 1190, 1.03], ['rival.part', 540, 1140, 1.1],
      ['clear', 540, 1060, 1.18], ['cam.push', 495, 975, 1.14], ['cam.pointer', 560, 1000, 1.2], ['cam.meeting', 620, 1030, 1.3],
      ['cam.caret', 700, 1075, 1.4], ['cam.save', 770, 1085, 1.6], ['cam.send', 790, 1088, 1.85]   // into the caret, step by step; the end card grows out of it
    ]
  };
})((window.SS = window.SS || {}));
