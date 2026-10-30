import type { StudioGate } from "@/lib/api/studio";

/** The latest record of each gate (per asset), in first-seen order: what a collapsed step shows. */
export function latestGates(gates: StudioGate[]): StudioGate[] {
  const by = new Map<string, StudioGate>();
  for (const g of gates) by.set(`${g.gate}|${g.asset ?? ""}`, g); // a later record replaces the value, not the position
  return [...by.values()];
}

/** "SB-H01@v2 Storyboard review", or the gate's human name, or its code. */
export const gateLabel = (g: StudioGate) => [g.asset, g.label || g.gate].filter(Boolean).join(" ");
