// @vitest-environment node
import { afterAll, beforeAll, beforeEach, describe, expect, it } from "vitest";
import { fileMarkdown } from "./files.server";
import { upsertRun } from "./runs-upsert.server";
import { closeStudioDb, hasDb, resetStudio, studioDb, type StudioDb } from "./test-db";
import { runInput } from "./test-fixtures";

describe.skipIf(!hasDb)("studio files (Postgres)", () => {
  let db: StudioDb;
  beforeAll(async () => {
    db = await studioDb();
  });
  afterAll(() => closeStudioDb(db));
  beforeEach(() => resetStudio(db));

  const script = { key: "docs/script.md", label: "Script", kind: "doc" as const, markdown: "# Script\n\nLine one.", step: 3 };
  const song = { key: "audio/song.mp3", label: "Song", kind: "audio" as const, url: "https://cdn.example/song.mp3", step: 3, sha256: "a".repeat(64) };

  it("lists a run's files in step order, without their markdown", async () => {
    const { files } = await upsertRun(db.sql, runInput({ files: [script, song] }));
    expect(files.map((f) => [f.key, f.kind, f.has_markdown, f.markdown_chars, f.sha256])).toEqual([
      ["docs/script.md", "doc", true, 19, null],
      ["audio/song.mp3", "audio", false, 0, "a".repeat(64)],
    ]);
    expect(files[0]).not.toHaveProperty("markdown");
  });

  it("keeps the files when a push leaves them out, replaces them when given, and removes them all on []", async () => {
    await upsertRun(db.sql, runInput({ files: [script, song] }));
    expect((await upsertRun(db.sql, runInput())).files).toHaveLength(2);
    const replaced = await upsertRun(db.sql, runInput({ files: [{ ...song, label: "Song v2", url: "https://cdn.example/song2.mp3" }] }));
    expect(replaced.files.map((f) => [f.key, f.label, f.url])).toEqual([["audio/song.mp3", "Song v2", "https://cdn.example/song2.mp3"]]);
    expect((await upsertRun(db.sql, runInput({ files: [] }))).files).toEqual([]);
  });

  it("hands back a doc's markdown exactly, quotes and backslashes included", async () => {
    const text = "it's \"quoted\" \\ and 'single'";
    const { files } = await upsertRun(db.sql, runInput({ files: [{ key: "d", label: "Lyrics", kind: "doc", markdown: text }] }));
    expect(await fileMarkdown(db.sql, files[0]!.id)).toEqual({ id: files[0]!.id, label: "Lyrics", markdown: text });
    expect(await fileMarkdown(db.sql, 999)).toBeNull();
  });
});
