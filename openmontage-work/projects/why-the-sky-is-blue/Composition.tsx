import React from "react";
import {
  AbsoluteFill,
  Audio,
  CalculateMetadataFunction,
  Easing,
  Sequence,
  interpolate,
  random,
  spring,
  staticFile,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont as loadFredoka } from "@remotion/google-fonts/Fredoka";
import { loadFont as loadNunito } from "@remotion/google-fonts/Nunito";

// ----------------------------------------------------------------------------
// ATELIER (BESPOKE) — "Sunlight, Sorted by Color". Hand-authored for this piece.
// See art-direction.md. No stock registry components are imported.
// ----------------------------------------------------------------------------

const { fontFamily: TITLE } = loadFredoka("normal", { weights: ["500", "600"] });
const { fontFamily: BODY } = loadNunito("normal", { weights: ["600", "700"] });

const C = {
  space: "#05081A",
  navy: "#0B1430",
  indigo: "#141B4D",
  cerulean: "#3B8BEB",
  skyLight: "#8FD0FF",
  sunCore: "#FFF4D6",
  sunGlow: "#FFD27A",
  amber: "#FF9A4A",
  rose: "#F2617A",
  dusk: "#2B2D6E",
  text: "#F5F2EA",
};
const SPECTRUM = ["#FF4D4D", "#FF9A3C", "#FFE15A", "#4CD787", "#3B8BEB", "#9B6BFF"];
const W = 1920;
const H = 1080;

export interface Word {
  text: string;
  start: number;
  end: number;
}
export interface SceneTiming {
  id: string;
  start: number;
  end: number;
}
export interface SceneProps {
  fps: number;
  durationSeconds: number;
  narration: string;
  music: string;
  musicVolume: number;
  words: Word[];
  scenes: SceneTiming[];
  hideCaptionsAfter: number;
}

// ---------- helpers ----------
const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const ease = Easing.bezier(0.45, 0, 0.25, 1);
const ramp = (t: number, a: number, b: number) => interpolate(t, [a, b], [0, 1], { ...clamp, easing: ease });

const useLocalTime = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return { t: frame / fps, frame, fps };
};

const pop = (frame: number, fps: number, atSec: number, damping = 14) =>
  spring({ frame: frame - atSec * fps, fps, config: { damping, stiffness: 120, mass: 0.8 } });

// Sine wave path from x0 to x1 (drawn up to xHead), centred on y.
const wavePath = (x0: number, xHead: number, y: number, lambda: number, amp: number, phase: number) => {
  if (xHead <= x0) return "";
  const pts: string[] = [];
  for (let x = x0; x <= xHead; x += 4) {
    const yy = y + amp * Math.sin(((x - x0) / lambda) * Math.PI * 2 + phase);
    pts.push(`${pts.length === 0 ? "M" : "L"}${x.toFixed(1)},${yy.toFixed(1)}`);
  }
  return pts.join(" ");
};

const Glow: React.FC<{ id: string; std?: number }> = ({ id, std = 6 }) => (
  <filter id={id} x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation={std} result="b" />
    <feMerge>
      <feMergeNode in="b" />
      <feMergeNode in="SourceGraphic" />
    </feMerge>
  </filter>
);

// Scene wrapper: soft fade in/out around each scene.
const SceneFade: React.FC<{ dur: number; children: React.ReactNode; fadeIn?: number; fadeOut?: number }> = ({
  dur,
  children,
  fadeIn = 0.45,
  fadeOut = 0.45,
}) => {
  const { t } = useLocalTime();
  const o = Math.min(ramp(t, 0, fadeIn), 1 - ramp(t, dur - fadeOut, dur));
  return <AbsoluteFill style={{ opacity: fadeIn === 0 ? 1 - ramp(t, dur - fadeOut, dur) : o }}>{children}</AbsoluteFill>;
};

const Label: React.FC<{ x: number; y: number; text: string; color?: string; size?: number; o?: number; anchor?: "start" | "middle" | "end" }> = ({
  x,
  y,
  text,
  color = C.text,
  size = 38,
  o = 1,
  anchor = "middle",
}) => (
  <text x={x} y={y} fill={color} opacity={o} fontFamily={TITLE} fontWeight={500} fontSize={size} textAnchor={anchor}>
    {text}
  </text>
);

// A diatomic molecule: two overlapping spheres.
const Molecule: React.FC<{ x: number; y: number; r: number; rot: number; color: string; o?: number; blur?: number }> = ({
  x,
  y,
  r,
  rot,
  color,
  o = 1,
  blur = 0,
}) => (
  <g transform={`translate(${x},${y}) rotate(${rot})`} opacity={o} style={blur ? { filter: `blur(${blur}px)` } : undefined}>
    <circle cx={-r * 0.62} cy={0} r={r} fill={color} />
    <circle cx={r * 0.62} cy={0} r={r} fill={color} />
    <circle cx={-r * 0.85} cy={-r * 0.35} r={r * 0.28} fill="#ffffff" opacity={0.45} />
  </g>
);

// ---------- sc1: Sun + Earth in space ----------
const Stars: React.FC<{ n: number; seed: string; t: number; o?: number; maxY?: number }> = ({ n, seed, t, o = 1, maxY = H }) => (
  <g opacity={o}>
    {new Array(n).fill(0).map((_, i) => {
      const x = random(`${seed}x${i}`) * W;
      const y = random(`${seed}y${i}`) * maxY;
      const r = 0.8 + random(`${seed}r${i}`) * 1.8;
      const tw = 0.55 + 0.45 * Math.sin(t * (1 + random(`${seed}s${i}`) * 2) + i);
      return <circle key={i} cx={x} cy={y} r={r} fill="#ffffff" opacity={tw * 0.8} />;
    })}
  </g>
);

const SceneSpace: React.FC<{ dur: number }> = ({ dur }) => {
  const { t, frame, fps } = useLocalTime();
  const sun = { x: 380, y: 540 };
  const earth = { x: 1540, y: 540 };
  const beamHead = interpolate(t, [0.6, 3.0], [sun.x + 80, earth.x - 62], { ...clamp, easing: ease });
  const halo = pop(frame, fps, 4.45, 12);
  const pulse = 1 + 0.04 * Math.sin(t * 2.2);
  return (
    <SceneFade dur={dur} fadeIn={0.6}>
      <AbsoluteFill style={{ background: `radial-gradient(ellipse at 50% 50%, ${C.navy} 0%, ${C.space} 70%)` }}>
        <svg width={W} height={H}>
          <defs>
            <Glow id="g1" std={10} />
            <radialGradient id="sunG">
              <stop offset="0%" stopColor={C.sunCore} />
              <stop offset="55%" stopColor="#FFF0C2" />
              <stop offset="100%" stopColor={C.sunGlow} stopOpacity={0} />
            </radialGradient>
            <radialGradient id="earthG" cx="35%" cy="35%">
              <stop offset="0%" stopColor="#5FB7E8" />
              <stop offset="60%" stopColor="#1F6FA8" />
              <stop offset="100%" stopColor="#0C2E52" />
            </radialGradient>
            <radialGradient id="haloG">
              <stop offset="70%" stopColor={C.skyLight} stopOpacity={0} />
              <stop offset="82%" stopColor={C.skyLight} stopOpacity={0.9} />
              <stop offset="100%" stopColor={C.cerulean} stopOpacity={0} />
            </radialGradient>
          </defs>
          <Stars n={140} seed="s1" t={t} />
          {/* sun */}
          <circle cx={sun.x} cy={sun.y} r={180 * pulse} fill="url(#sunG)" opacity={0.55} />
          <circle cx={sun.x} cy={sun.y} r={72} fill={C.sunCore} filter="url(#g1)" />
          {/* beam */}
          <line x1={sun.x + 80} y1={sun.y} x2={beamHead} y2={sun.y} stroke="#ffffff" strokeWidth={7} strokeLinecap="round" filter="url(#g1)" opacity={0.95} />
          <circle cx={beamHead} cy={sun.y} r={10} fill="#ffffff" filter="url(#g1)" opacity={t > 0.6 && t < 3.1 ? 1 : 0} />
          {/* earth + atmosphere */}
          <circle cx={earth.x} cy={earth.y} r={62 + 40 * halo} fill="url(#haloG)" opacity={halo} />
          <circle cx={earth.x} cy={earth.y} r={62} fill="url(#earthG)" />
          <path d={`M${earth.x - 30},${earth.y - 20} q18,-16 36,-4 q10,14 -6,24 q-20,6 -30,-20z`} fill="#3E9B6E" opacity={0.85} />
          <path d={`M${earth.x + 8},${earth.y + 18} q20,-6 30,8 q-8,16 -26,10z`} fill="#3E9B6E" opacity={0.8} />
        </svg>
      </AbsoluteFill>
    </SceneFade>
  );
};

// ---------- sc2: white light is every color ----------
const LAMBDAS = [270, 235, 205, 180, 155, 128];
const SceneSpectrum: React.FC<{ dur: number }> = ({ dur }) => {
  const { t } = useLocalTime();
  const node = { x: 470, y: 540 };
  const xEnd = 1720;
  const beamIn = interpolate(t, [0, 0.7], [0, node.x], { ...clamp, easing: ease });
  const labels = ramp(t, 4.3, 5.0);
  return (
    <SceneFade dur={dur}>
      <AbsoluteFill style={{ background: `linear-gradient(180deg, ${C.space} 0%, ${C.navy} 100%)` }}>
        <svg width={W} height={H}>
          <defs>
            <Glow id="g2" std={5} />
          </defs>
          {/* faint grid */}
          {new Array(13).fill(0).map((_, i) => (
            <line key={i} x1={150 * i} y1={0} x2={150 * i} y2={H} stroke="#ffffff" opacity={0.03} />
          ))}
          <line x1={0} y1={node.y} x2={beamIn} y2={node.y} stroke="#ffffff" strokeWidth={7} strokeLinecap="round" filter="url(#g2)" />
          <circle cx={node.x} cy={node.y} r={14 + 3 * Math.sin(t * 4)} fill="#ffffff" filter="url(#g2)" opacity={ramp(t, 0.5, 0.8)} />
          {SPECTRUM.map((col, i) => {
            const y = node.y + (i - 2.5) * 100;
            const head = interpolate(t, [0.7 + i * 0.12, 2.6 + i * 0.12], [node.x + 60, xEnd], { ...clamp, easing: ease });
            const phase = -t * Math.PI * 1.4;
            // fan connector from node to wave start
            const fan = ramp(t, 0.6 + i * 0.1, 0.9 + i * 0.1);
            return (
              <g key={col}>
                <path d={`M${node.x},${node.y} C${node.x + 30},${node.y} ${node.x + 30},${y} ${node.x + 60},${y}`} stroke={col} strokeWidth={4} fill="none" opacity={fan} />
                <path d={wavePath(node.x + 60, head, y, LAMBDAS[i], 28, phase)} stroke={col} strokeWidth={5} fill="none" strokeLinecap="round" filter="url(#g2)" />
              </g>
            );
          })}
          {/* wavelength brackets */}
          <g opacity={labels}>
            <line x1={xEnd - LAMBDAS[0]} y1={node.y - 250 - 52} x2={xEnd} y2={node.y - 250 - 52} stroke={SPECTRUM[0]} strokeWidth={3} />
            <line x1={xEnd - LAMBDAS[0]} y1={node.y - 312} x2={xEnd - LAMBDAS[0]} y2={node.y - 292} stroke={SPECTRUM[0]} strokeWidth={3} />
            <line x1={xEnd} y1={node.y - 312} x2={xEnd} y2={node.y - 292} stroke={SPECTRUM[0]} strokeWidth={3} />
            <Label x={xEnd - LAMBDAS[0] / 2} y={node.y - 325} text="long wave" color={SPECTRUM[0]} size={34} />
            <line x1={xEnd - LAMBDAS[5]} y1={node.y + 250 + 52} x2={xEnd} y2={node.y + 250 + 52} stroke={SPECTRUM[5]} strokeWidth={3} />
            <line x1={xEnd - LAMBDAS[5]} y1={node.y + 292} x2={xEnd - LAMBDAS[5]} y2={node.y + 312} stroke={SPECTRUM[5]} strokeWidth={3} />
            <line x1={xEnd} y1={node.y + 292} x2={xEnd} y2={node.y + 312} stroke={SPECTRUM[5]} strokeWidth={3} />
            <Label x={xEnd - LAMBDAS[5] / 2} y={node.y + 350} text="short wave" color={SPECTRUM[5]} size={34} />
          </g>
        </svg>
      </AbsoluteFill>
    </SceneFade>
  );
};

// ---------- sc3: the molecules ----------
const SceneMolecules: React.FC<{ dur: number; startAt: number }> = ({ dur }) => {
  const { t, frame, fps } = useLocalTime();
  const zoom = interpolate(t, [0, 1.8], [0.35, 1], { ...clamp, easing: ease });
  const n2 = pop(frame, fps, 2.2);
  const o2 = pop(frame, fps, 2.85);
  const layers = [
    { n: 26, rMin: 8, rMax: 12, blur: 0, o: 0.55, speed: 6 },
    { n: 16, rMin: 16, rMax: 22, blur: 0, o: 0.85, speed: 12 },
    { n: 5, rMin: 34, rMax: 44, blur: 10, o: 0.22, speed: 22 },
  ];
  return (
    <SceneFade dur={dur}>
      <AbsoluteFill style={{ background: `radial-gradient(ellipse at 40% 50%, ${C.indigo} 0%, ${C.space} 85%)` }}>
        <svg width={W} height={H}>
          <defs>
            <Glow id="g3" std={4} />
          </defs>
          {/* faint light waves passing through the air */}
          {[0, 3, 4].map((ci, k) => (
            <path key={ci} d={wavePath(0, W, 300 + k * 240, LAMBDAS[ci], 18, -t * 3 + k)} stroke={SPECTRUM[ci]} strokeWidth={3} fill="none" opacity={0.35 * ramp(t, 0.8, 1.6)} filter="url(#g3)" />
          ))}
          <g transform={`translate(${W / 2},${H / 2}) scale(${zoom}) translate(${-W / 2},${-H / 2})`}>
            {layers.map((L, li) =>
              new Array(L.n).fill(0).map((_, i) => {
                const seed = `m${li}-${i}`;
                const x = (random(seed + "x") * (W + 200) - 100 + t * L.speed) % (W + 200);
                const y = random(seed + "y") * H;
                const r = L.rMin + random(seed + "r") * (L.rMax - L.rMin);
                const isN2 = random(seed + "k") < 0.78; // air is ~78% nitrogen
                const rot = random(seed + "o") * 180 + t * (random(seed + "w") * 20 - 10);
                return <Molecule key={seed} x={x} y={y} r={r} rot={rot} color={isN2 ? "#9CC9FF" : C.text} o={L.o} blur={L.blur} />;
              }),
            )}
            {/* two hero molecules with labels */}
            <Molecule x={760} y={500} r={26} rot={20 + t * 6} color="#9CC9FF" />
            <Molecule x={1200} y={610} r={26} rot={-30 - t * 5} color={C.text} />
          </g>
          <g opacity={n2} transform={`translate(${760},${430 - 10 * n2})`}>
            <rect x={-62} y={-44} width={124} height={58} rx={29} fill="#9CC9FF" opacity={0.18} />
            <Label x={0} y={0} text="N₂" color="#BFDcff" size={40} />
          </g>
          <g opacity={o2} transform={`translate(${1200},${540 - 10 * o2})`}>
            <rect x={-62} y={-44} width={124} height={58} rx={29} fill={C.text} opacity={0.15} />
            <Label x={0} y={0} text="O₂" size={40} />
          </g>
        </svg>
      </AbsoluteFill>
    </SceneFade>
  );
};

// ---------- sc4: red passes, blue splashes (signature) ----------
const SceneSplash: React.FC<{ dur: number }> = ({ dur }) => {
  const { t, frame, fps } = useLocalTime();
  const m = { x: 900, y: 560 };
  const redHead = interpolate(t, [0.2, 2.2], [-50, W + 50], { ...clamp, easing: Easing.inOut(Easing.quad) });
  const blueHead = interpolate(t, [1.2, 2.3], [-50, m.x - 40], { ...clamp, easing: Easing.in(Easing.quad) });
  const hit = 2.3;
  const burst = t > hit ? (t - hit) : 0;
  const x5 = pop(frame, fps, 2.95, 11);
  const wobble = t > hit ? Math.sin((t - hit) * 18) * Math.exp(-(t - hit) * 3) * 6 : 0;
  return (
    <SceneFade dur={dur}>
      <AbsoluteFill style={{ background: `radial-gradient(circle at 47% 52%, #1B2466 0%, ${C.space} 62%)` }}>
        <svg width={W} height={H}>
          <defs>
            <Glow id="g4" std={6} />
          </defs>
          {/* red: straight through (lane slightly above centre, crossing the molecule) */}
          <path d={wavePath(Math.max(-50, redHead - 900), redHead, m.y - 8, LAMBDAS[0], 26, -t * 6)} stroke={SPECTRUM[0]} strokeWidth={6} fill="none" strokeLinecap="round" filter="url(#g4)" opacity={1 - ramp(t, 2.6, 3.2) * 0.6} />
          <Label x={140} y={m.y - 70} text="red" color={SPECTRUM[0]} size={34} o={ramp(t, 0.3, 0.7) * (1 - ramp(t, 2.0, 2.4))} anchor="start" />
          {/* blue: arrives and splashes */}
          {t <= hit + 0.05 && (
            <path d={wavePath(Math.max(-50, blueHead - 700), blueHead, m.y + 8, LAMBDAS[4], 24, -t * 8)} stroke={SPECTRUM[4]} strokeWidth={6} fill="none" strokeLinecap="round" filter="url(#g4)" />
          )}
          <Label x={140} y={m.y + 80} text="blue" color={SPECTRUM[4]} size={34} o={ramp(t, 1.3, 1.6) * (1 - ramp(t, 2.2, 2.6))} anchor="start" />
          {/* ripples */}
          {[0, 0.25, 0.5, 0.75].map((d, i) => {
            const k = Math.max(0, burst - d);
            return <circle key={i} cx={m.x} cy={m.y} r={60 + k * 520} fill="none" stroke={SPECTRUM[4]} strokeWidth={4} opacity={k > 0 ? Math.max(0, 0.8 - k * 0.5) : 0} />;
          })}
          {/* radial blue wavelets */}
          {new Array(12).fill(0).map((_, i) => {
            const ang = (i / 12) * Math.PI * 2 + 0.2;
            const k = Math.min(1, burst / 1.2);
            const r0 = 70;
            const r1 = r0 + k * 330;
            const len = 120;
            const pts: string[] = [];
            for (let s = 0; s <= len; s += 6) {
              const rr = r1 - len + s;
              if (rr < r0) continue;
              const off = 10 * Math.sin(s / 16 - t * 10);
              const x = m.x + Math.cos(ang) * rr - Math.sin(ang) * off;
              const y = m.y + Math.sin(ang) * rr + Math.cos(ang) * off;
              pts.push(`${pts.length ? "L" : "M"}${x.toFixed(1)},${y.toFixed(1)}`);
            }
            return <path key={i} d={pts.join(" ")} stroke={SPECTRUM[4]} strokeWidth={5} fill="none" strokeLinecap="round" opacity={burst > 0 ? 1 - ramp(burst, 2.2, 2.8) : 0} filter="url(#g4)" />;
          })}
          <g transform={`translate(${wobble},0)`}>
            <Molecule x={m.x} y={m.y} r={46} rot={15} color="#9CC9FF" />
          </g>
          {/* x5 */}
          <g transform={`translate(1520,330) scale(${0.6 + 0.4 * x5})`} opacity={x5}>
            <text x={0} y={0} fill={SPECTRUM[4]} fontFamily={TITLE} fontWeight={600} fontSize={170} textAnchor="middle" filter="url(#g4)">
              ×5
            </text>
            <Label x={0} y={64} text="more scattering" size={36} />
            <Label x={0} y={108} text="blue vs. red" size={30} o={0.7} />
          </g>
        </svg>
      </AbsoluteFill>
    </SceneFade>
  );
};

// ---------- sc5: blue from every direction ----------
const SceneSky: React.FC<{ dur: number }> = ({ dur }) => {
  const { t } = useLocalTime();
  const fill = ramp(t, 0, 2.6);
  const eye = { x: 1392, y: 742 };
  const top = interpolate(fill, [0, 1], [0, 1]);
  const skyTop = top < 1 ? `rgb(${Math.round(11 + (36 - 11) * top)},${Math.round(20 + (110 - 20) * top)},${Math.round(48 + (214 - 48) * top)})` : "#246ED6";
  const skyBot = `rgb(${Math.round(20 + (143 - 20) * top)},${Math.round(27 + (208 - 27) * top)},${Math.round(77 + (255 - 77) * top)})`;
  const paths = new Array(7).fill(0).map((_, i) => {
    const seed = `p${i}`;
    const sx = random(seed + "a") * 1700 + 60;
    const pts = [{ x: sx, y: -20 }];
    for (let k = 0; k < 2; k++) {
      pts.push({ x: 120 + random(`${seed}x${k}`) * 1650, y: 80 + random(`${seed}y${k}`) * 480 });
    }
    pts.push(eye);
    return pts;
  });
  return (
    <SceneFade dur={dur}>
      <AbsoluteFill style={{ background: `linear-gradient(180deg, ${skyTop} 0%, ${skyBot} 78%)` }}>
        <svg width={W} height={H}>
          <defs>
            <Glow id="g5" std={4} />
          </defs>
          {/* soft sun */}
          <circle cx={260} cy={180} r={70} fill={C.sunCore} opacity={0.9} filter="url(#g5)" />
          {/* molecules in the sky */}
          {new Array(26).fill(0).map((_, i) => (
            <Molecule key={i} x={80 + random(`sm${i}x`) * 1760} y={60 + random(`sm${i}y`) * 560} r={7} rot={random(`sm${i}r`) * 180 + t * 10} color="#E8F4FF" o={0.55} />
          ))}
          {/* zig-zag blue light to the eye */}
          {paths.map((pts, i) => {
            // comet: a bright head with a short fading trail, bouncing molecule to molecule
            const prog = ramp(t, 0.4 + i * 0.4, 2.4 + i * 0.4);
            const segs = pts.length - 1;
            const at = (u: number) => {
              const uu = Math.max(0, Math.min(segs, u));
              const s = Math.min(segs - 1, Math.floor(uu));
              const f = uu - s;
              return { x: pts[s].x + (pts[s + 1].x - pts[s].x) * f, y: pts[s].y + (pts[s + 1].y - pts[s].y) * f };
            };
            const upto = prog * segs;
            const trail = new Array(12).fill(0).map((_, k) => at(upto - k * 0.045));
            const visible = prog > 0 && prog < 1;
            return (
              <g key={i} opacity={visible ? 1 : 0}>
                {trail.slice(1).map((p, k) => (
                  <line key={k} x1={trail[k].x} y1={trail[k].y} x2={p.x} y2={p.y} stroke="#DDF0FF" strokeWidth={6 - k * 0.4} strokeLinecap="round" opacity={1 - k / 11} />
                ))}
                <circle cx={trail[0].x} cy={trail[0].y} r={9} fill="#ffffff" filter="url(#g5)" />
                {pts.slice(1, -1).map((p, k) => (
                  <circle key={k} cx={p.x} cy={p.y} r={14} fill="none" stroke="#ffffff" strokeWidth={2} opacity={upto > k + 1 ? Math.max(0, 0.7 - (upto - k - 1) * 0.6) : 0} />
                ))}
              </g>
            );
          })}
          {/* hill */}
          <path d={`M0,${H} L0,860 C420,780 880,800 1240,830 C1520,850 1720,820 ${W},800 L${W},${H} Z`} fill="#1E5A57" />
          <path d={`M0,${H} L0,930 C500,880 1100,900 ${W},880 L${W},${H} Z`} fill="#184A48" />
          {/* person looking up */}
          <g transform="translate(1380,0)">
            <rect x={-16} y={770} width={32} height={66} rx={14} fill="#0E2230" />
            <circle cx={6} cy={746} r={20} fill="#0E2230" />
            <rect x={-12} y={830} width={10} height={34} rx={5} fill="#0E2230" />
            <rect x={4} y={830} width={10} height={34} rx={5} fill="#0E2230" />
          </g>
          <circle cx={eye.x} cy={eye.y} r={10 + 6 * ramp(t, 2.6, 3.4)} fill="#ffffff" opacity={0.35 * ramp(t, 2.2, 3.0)} filter="url(#g5)" />
        </svg>
      </AbsoluteFill>
    </SceneFade>
  );
};

// ---------- sc6: why not violet ----------
const SENS = [0.35, 0.75, 1.0, 0.98, 0.62, 0.12]; // relative eye response per band (illustrative)
const SUN = [0.82, 0.9, 0.96, 1.0, 0.94, 0.58]; // relative sunlight per band (illustrative)
const SceneViolet: React.FC<{ dur: number }> = ({ dur }) => {
  const { t, frame, fps } = useLocalTime();
  const tint = ramp(t, 0.4, 1.8) * (1 - ramp(t, 6.0, 6.9));
  const q = pop(frame, fps, 2.45, 9) * (1 - ramp(t, 4.4, 5.0));
  const eyeOpen = ramp(t, 5.15, 5.6);
  const curve = ramp(t, 5.4, 6.6);
  const chart = { x: 1010, w: 780, base: 490, h: 260 };
  const bw = chart.w / 6;
  const curveBase = 830;
  const curvePts = SENS.map((s, i) => ({ x: chart.x + bw * (i + 0.5), y: curveBase - s * 190 }));
  let cd = `M${curvePts[0].x},${curvePts[0].y}`;
  for (let i = 1; i < curvePts.length; i++) {
    const a = curvePts[i - 1];
    const b = curvePts[i];
    const mx = (a.x + b.x) / 2;
    cd += ` C${mx},${a.y} ${mx},${b.y} ${b.x},${b.y}`;
  }
  return (
    <SceneFade dur={dur}>
      <AbsoluteFill style={{ background: `linear-gradient(160deg, ${C.navy} 0%, #121A44 100%)` }}>
        <svg width={W} height={H}>
          <defs>
            <Glow id="g6" std={5} />
            <linearGradient id="skyWin" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#2A77DC" />
              <stop offset="100%" stopColor="#9AD4FF" />
            </linearGradient>
            <linearGradient id="vioWin" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#5B2DB8" />
              <stop offset="100%" stopColor="#B99BFF" />
            </linearGradient>
            <clipPath id="win">
              <rect x={150} y={190} width={640} height={700} rx={40} />
            </clipPath>
          </defs>
          {/* sky window */}
          <g clipPath="url(#win)">
            <rect x={150} y={190} width={640} height={700} fill="url(#skyWin)" />
            <rect x={150} y={190} width={640} height={700} fill="url(#vioWin)" opacity={tint} />
            <path d="M150,800 C330,760 560,790 790,750 L790,890 L150,890Z" fill="#1E5A57" />
          </g>
          <rect x={150} y={190} width={640} height={700} rx={40} fill="none" stroke="#ffffff" strokeOpacity={0.25} strokeWidth={3} />
          <g opacity={q} transform={`translate(470,${560 - 20 * q}) scale(${0.7 + 0.3 * q})`}>
            <text x={0} y={60} fill="#ffffff" fontFamily={TITLE} fontWeight={600} fontSize={230} textAnchor="middle" filter="url(#g6)">
              ?
            </text>
          </g>
          {/* sunlight bars */}
          <Label x={chart.x} y={chart.base - chart.h - 40} text="sunlight" anchor="start" size={36} o={ramp(t, 3.4, 3.8)} />
          {SUN.map((v, i) => {
            const g = ramp(t, 3.55 + i * 0.1, 4.25 + i * 0.1);
            const h = v * chart.h * g;
            return <rect key={i} x={chart.x + bw * i + 14} y={chart.base - h} width={bw - 28} height={h} rx={10} fill={SPECTRUM[i]} opacity={0.9} />;
          })}
          <line x1={chart.x} y1={chart.base} x2={chart.x + chart.w} y2={chart.base} stroke="#ffffff" strokeOpacity={0.3} strokeWidth={2} />
          <circle cx={chart.x + bw * 5.5} cy={chart.base - SUN[5] * chart.h - 30} r={34} fill="none" stroke={SPECTRUM[5]} strokeWidth={3} strokeDasharray="6 6" opacity={ramp(t, 4.4, 4.8)} />
          {/* eye */}
          <g transform={`translate(${chart.x + 40},${curveBase - 240})`} opacity={ramp(t, 5.0, 5.3)}>
            <path d="M-34,0 Q0,-26 34,0 Q0,26 -34,0Z" fill="#ffffff" transform={`scale(1,${Math.max(0.05, eyeOpen)})`} />
            <circle cx={0} cy={0} r={11 * eyeOpen} fill={C.cerulean} />
            <circle cx={0} cy={0} r={5 * eyeOpen} fill="#0B1430" />
          </g>
          <Label x={chart.x + 95} y={curveBase - 228} text="your eyes" anchor="start" size={34} o={ramp(t, 5.3, 5.7)} />
          <line x1={chart.x} y1={curveBase} x2={chart.x + chart.w} y2={curveBase} stroke="#ffffff" strokeOpacity={0.3} strokeWidth={2} />
          {SPECTRUM.map((c, i) => (
            <circle key={i} cx={chart.x + bw * (i + 0.5)} cy={curveBase + 22} r={9} fill={c} opacity={ramp(t, 5.2, 5.5)} />
          ))}
          <path d={cd} stroke="#ffffff" strokeWidth={5} fill="none" strokeLinecap="round" pathLength={1} strokeDasharray="1 1" strokeDashoffset={1 - curve} filter="url(#g6)" />
          {/* blue vs violet: where the eye responds */}
          <circle cx={curvePts[4].x} cy={curvePts[4].y} r={13} fill={SPECTRUM[4]} opacity={ramp(t, 6.4, 6.8)} filter="url(#g6)" />
          <circle cx={curvePts[5].x} cy={curvePts[5].y} r={9} fill={SPECTRUM[5]} opacity={0.6 * ramp(t, 6.4, 6.8)} />
          <line x1={curvePts[4].x} y1={curveBase} x2={curvePts[4].x} y2={curvePts[4].y + 14} stroke={SPECTRUM[4]} strokeWidth={4} opacity={ramp(t, 6.4, 6.8)} />
          <line x1={curvePts[5].x} y1={curveBase} x2={curvePts[5].x} y2={curvePts[5].y + 10} stroke={SPECTRUM[5]} strokeWidth={4} opacity={0.6 * ramp(t, 6.4, 6.8)} />
        </svg>
      </AbsoluteFill>
    </SceneFade>
  );
};

// ---------- sc7: sunset ----------
const SceneSunset: React.FC<{ dur: number }> = ({ dur }) => {
  const { t } = useLocalTime();
  const warm = ramp(t, 0, 4.6);
  const sunY = interpolate(t, [0, dur], [700, 770], clamp);
  const sun = { x: 230, y: sunY };
  const viewer = { x: 1660, y: 812 };
  // Long, low light path across the frame
  const pathAt = (s: number) => {
    const x = sun.x + (viewer.x - sun.x) * s;
    const y = sun.y + (viewer.y - 20 - sun.y) * s - Math.sin(s * Math.PI) * 60;
    return { x, y };
  };
  const beamOn = ramp(t, 0.6, 1.4);
  const parts = new Array(90).fill(0).map((_, i) => {
    const ci = i % 6;
    const off = random(`pp${i}`);
    const s = (t * 0.22 + off) % 1;
    const p = pathAt(s);
    // short waves (blue/violet, some green) get scattered out of the beam along the way
    const thresholdBase = ci === 5 ? 0.18 : ci === 4 ? 0.26 : ci === 3 ? 0.55 : 2;
    const th = thresholdBase + random(`th${i}`) * 0.15;
    const scattered = t > 2.6 && s > th;
    const k = scattered ? s - th : 0;
    const y = p.y - k * 520 * (0.6 + random(`dy${i}`));
    const x = p.x + k * 140 * (random(`dx${i}`) - 0.3);
    const o = scattered ? Math.max(0, 1 - k * 3.2) : 1;
    return { x, y, c: SPECTRUM[ci], o: o * beamOn, r: 8 + random(`pr${i}`) * 4 };
  });
  const top = `rgb(${Math.round(36 + (43 - 36) * warm)},${Math.round(110 + (45 - 110) * warm)},${Math.round(214 + (110 - 214) * warm)})`;
  const mid = `rgb(${Math.round(110 + (242 - 110) * warm)},${Math.round(170 + (97 - 170) * warm)},${Math.round(240 + (122 - 240) * warm)})`;
  const bot = `rgb(${Math.round(160 + (255 - 160) * warm)},${Math.round(210 + (154 - 210) * warm)},${Math.round(255 + (74 - 255) * warm)})`;
  return (
    <SceneFade dur={dur}>
      <AbsoluteFill style={{ background: `linear-gradient(180deg, ${top} 0%, ${mid} 55%, ${bot} 80%)` }}>
        <svg width={W} height={H}>
          <defs>
            <Glow id="g7" std={8} />
            <radialGradient id="ssun">
              <stop offset="0%" stopColor="#FFF1D0" />
              <stop offset="40%" stopColor="#FFC27A" />
              <stop offset="100%" stopColor="#FF8A4A" stopOpacity={0} />
            </radialGradient>
            <linearGradient id="beamG" x1="0" y1="0" x2="1" y2="0">
              <stop offset="0%" stopColor="#ffffff" />
              <stop offset="45%" stopColor="#FFD9A0" />
              <stop offset="100%" stopColor="#FF6A3D" />
            </linearGradient>
          </defs>
          {/* thick slab of air along the horizon */}
          <path d={`M0,560 C640,520 1280,520 ${W},560 L${W},860 L0,860Z`} fill="#ffffff" opacity={0.06 + 0.06 * ramp(t, 0.8, 1.6)} />
          <circle cx={sun.x} cy={sun.y} r={210} fill="url(#ssun)" opacity={0.85} />
          <circle cx={sun.x} cy={sun.y} r={70} fill="#FFE2B0" filter="url(#g7)" />
          {/* the long path */}
          <path
            d={new Array(41).fill(0).map((_, i) => {
              const p = pathAt(i / 40);
              return `${i ? "L" : "M"}${p.x.toFixed(1)},${p.y.toFixed(1)}`;
            }).join(" ")}
            stroke="url(#beamG)"
            strokeWidth={6}
            fill="none"
            opacity={0.55 * beamOn}
            filter="url(#g7)"
          />
          {parts.map((p, i) => (
            <circle key={i} cx={p.x} cy={p.y} r={p.r} fill={p.c} opacity={p.o} />
          ))}
          {/* ground + viewer */}
          <path d={`M0,${H} L0,820 C500,790 1100,800 ${W},790 L${W},${H}Z`} fill="#2A1638" />
          <g transform={`translate(${viewer.x},0)`}>
            <rect x={-16} y={812} width={32} height={60} rx={14} fill="#140A1E" />
            <circle cx={-4} cy={792} r={19} fill="#140A1E" />
          </g>
        </svg>
      </AbsoluteFill>
    </SceneFade>
  );
};

// ---------- sc8: closing title ----------
const SceneTitle: React.FC<{ dur: number }> = ({ dur }) => {
  const { t, frame, fps } = useLocalTime();
  const l1 = ramp(t, 0.0, 0.5);
  const l2 = ramp(t, 1.15, 1.65);
  const title = pop(frame, fps, 2.35, 15);
  const sort = ramp(t, 3.0, 4.1);
  const out = 1 - ramp(t, dur - 0.9, dur);
  const shuffled = [3, 0, 5, 1, 4, 2];
  const segW = 110;
  const startX = W / 2 - segW * 3;
  return (
    <AbsoluteFill style={{ opacity: Math.min(ramp(t, 0, 0.45), out), background: `linear-gradient(180deg, #1B1745 0%, #5A3474 52%, #E9784A 100%)` }}>
      <svg width={W} height={H}>
        <Stars n={70} seed="s8" t={t} o={0.7 * ramp(t, 0.5, 2.5)} maxY={520} />
        <Label x={W / 2} y={360} text="Same air." size={52} o={l1 * (1 - 0.45 * title)} />
        <Label x={W / 2} y={432} text="Same physics." size={52} o={l2 * (1 - 0.45 * title)} />
        <g opacity={title} transform={`translate(${W / 2},${600 + 30 * (1 - title)})`}>
          <text x={0} y={0} fill={C.text} fontFamily={TITLE} fontWeight={600} fontSize={108} textAnchor="middle">
            Sunlight, sorted by color.
          </text>
        </g>
        {SPECTRUM.map((c, i) => {
          const from = shuffled.indexOf(i);
          const pos = from + (i - from) * sort;
          return <rect key={c} x={startX + pos * segW + 6} y={660} width={segW - 12} height={12} rx={6} fill={c} opacity={title} />;
        })}
      </svg>
    </AbsoluteFill>
  );
};

// ---------- captions ----------
const Captions: React.FC<{ words: Word[]; hideAfter: number }> = ({ words, hideAfter }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  if (t >= hideAfter) return null;
  // group into phrases at sentence punctuation or every 7 words
  const phrases: Word[][] = [];
  let cur: Word[] = [];
  for (const w of words) {
    cur.push(w);
    if (/[.?!,:…]$/.test(w.text) || cur.length >= 7) {
      phrases.push(cur);
      cur = [];
    }
  }
  if (cur.length) phrases.push(cur);
  const active = phrases.find((p) => t >= p[0].start - 0.05 && t <= p[p.length - 1].end + 0.2);
  if (!active) return null;
  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: 70 }}>
      <div
        style={{
          fontFamily: BODY,
          fontWeight: 700,
          fontSize: 44,
          color: C.text,
          background: "rgba(5,8,26,0.55)",
          padding: "12px 30px",
          borderRadius: 18,
          maxWidth: 1500,
          textAlign: "center",
          letterSpacing: 0.2,
        }}
      >
        {active.map((w, i) => (
          <span key={i} style={{ opacity: t >= w.start - 0.05 ? 1 : 0.45 }}>
            {w.text.replace(/^BLUE\?$/, "blue?")}{" "}
          </span>
        ))}
      </div>
    </AbsoluteFill>
  );
};

const SCENES: Record<string, React.FC<{ dur: number; startAt: number }>> = {
  sc1: SceneSpace,
  sc2: SceneSpectrum,
  sc3: SceneMolecules,
  sc4: SceneSplash,
  sc5: SceneSky,
  sc6: SceneViolet,
  sc7: SceneSunset,
  sc8: SceneTitle,
};

export const Scene: React.FC<SceneProps> = (props) => {
  const { fps } = useVideoConfig();
  const overlap = 0.45;
  const frame = useCurrentFrame();
  const t = frame / fps;
  const narrationEnd = props.words.length ? props.words[props.words.length - 1].end : 0;
  const musicVol = (f: number) => {
    const s = f / fps;
    // gentle swell after the last word
    return props.musicVolume * (1 + 0.9 * interpolate(s, [narrationEnd, narrationEnd + 0.8], [0, 1], clamp));
  };
  return (
    <AbsoluteFill style={{ background: C.space }}>
      {props.scenes.map((s, i) => {
        const Comp = SCENES[s.id];
        const isLast = i === props.scenes.length - 1;
        const dur = s.end - s.start + (isLast ? 0 : overlap);
        return (
          <Sequence key={s.id} from={Math.round(s.start * fps)} durationInFrames={Math.round(dur * fps)} name={s.id}>
            <Comp dur={dur} startAt={s.start} />
          </Sequence>
        );
      })}
      <Captions words={props.words} hideAfter={props.hideCaptionsAfter} />
      {props.narration ? <Audio src={staticFile(props.narration)} /> : null}
      {props.music ? <Audio src={staticFile(props.music)} volume={musicVol} /> : null}
      {/* keep t referenced for deterministic re-render */}
      <div style={{ display: "none" }}>{t.toFixed(2)}</div>
    </AbsoluteFill>
  );
};

export const calculateMetadata: CalculateMetadataFunction<SceneProps> = async ({ props }) => ({
  durationInFrames: Math.round((props.durationSeconds || 46.5) * (props.fps || 30)),
  fps: props.fps || 30,
  width: W,
  height: H,
});
