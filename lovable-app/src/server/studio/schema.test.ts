// @vitest-environment node
import { describe, expect, it } from "vitest";
import { FileInput, RunInput } from "./schema";
import { runInput, step } from "./test-fixtures";

describe("studio input schema", () => {
  it("only takes http(s) links, and needs a link for audio, images and video", () => {
    expect(FileInput.safeParse({ key: "k", label: "Song", kind: "audio", url: "https://cdn.example/song.mp3" }).success).toBe(true);
    expect(FileInput.safeParse({ key: "k", label: "Song", kind: "audio", url: "javascript:alert(1)" }).success).toBe(false);
    expect(FileInput.safeParse({ key: "k", label: "Song", kind: "audio", markdown: "la la" }).success).toBe(false);
    expect(FileInput.safeParse({ key: "k", label: "Script", kind: "doc", markdown: "# Script" }).success).toBe(true);
    expect(FileInput.safeParse({ key: "k", label: "Script", kind: "doc" }).success).toBe(false);
  });

  it("knows the gate and step states", () => {
    expect(RunInput.safeParse({ ...runInput(), steps: [{ ...step(0, "done"), gates: [{ gate: "G-X", status: "MAYBE" }] }] }).success).toBe(false);
    expect(RunInput.safeParse({ ...runInput(), steps: [{ ...step(0, "done"), status: "later" }] }).success).toBe(false);
  });
});
