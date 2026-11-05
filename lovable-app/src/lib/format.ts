export function timeAgo(value: Date | string | null | undefined): string {
  if (!value) return "never";
  const d = typeof value === "string" ? new Date(value) : value;
  const m = Math.round((Date.now() - d.getTime()) / 60000);
  if (m < 1) return "just now";
  if (m < 60) return `${m} min ago`;
  if (m < 48 * 60) return `${Math.round(m / 60)} h ago`;
  return `${Math.round(m / 1440)} days ago`;
}

export function dateTime(value: Date | string | null | undefined): string {
  if (!value) return "";
  const d = typeof value === "string" ? new Date(value) : value;
  return d.toLocaleString(undefined, { dateStyle: "medium", timeStyle: "short" });
}

export const errorText = (err: unknown) => (err instanceof Error ? err.message : String(err));

export const STAGE_TONE: Record<string, "green" | "amber" | "red" | "gray" | "blue"> = {
  new: "gray",
  engaged: "blue",
  qualified: "blue",
  hot: "amber",
  booked: "green",
  won: "green",
  lost: "red",
};
