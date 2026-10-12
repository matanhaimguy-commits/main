// Scene list (times locked to plan/beats.json word timings).
import { C, text, charcoalBg } from "../lib.js";
import s01 from "./s01_hook.js";
import s03 from "./s03_patchwork.js";
import s09 from "./s09_promise.js";
import s13 from "./s13_cta.js";

const todo = (id, start, end, label) => ({ id, start, end, draw(ctx) { charcoalBg(ctx); text(ctx, label, 540, 900, { size: 44, weight: 700, color: C.stone, align: "center" }); } });

export const scenes = [
  s01,                                                        // 0.00 hook
  todo("s02_price", 3.0, 4.7, "S2 · çmimi (to build)"),
  s03,                                                        // 4.70 patchwork
  todo("s04_wall", 9.55, 13.6, "S4 · ~1.800 reklama (to build)"),
  todo("s05_compare", 13.6, 17.4, "S5 · vetëm çmimin (to build)"),
  todo("s06_thread", 17.4, 18.5, "S6 · ja çfarë bën (to build)"),
  todo("s07_reviews", 18.5, 22.65, "S7 · lexo komentet (to build)"),
  todo("s08_one", 22.65, 26.6, "S8 · një premtim (to build)"),
  s09,                                                        // 26.60 promise
  todo("s10_quilt", 31.1, 35.05, "S10 · kudo (to build)"),
  todo("s11_logo", 35.05, 37.05, "S11 · StraightScale + prova (to build)"),
  todo("s12_offer", 37.05, 42.66, "S12 · analizë falas (to build)"),
  s13,                                                        // 42.66 CTA
];
