/** A problem with what the studio sent or what someone did, with the HTTP status to answer with. */
export class StudioError extends Error {
  constructor(
    message: string,
    readonly status = 400,
  ) {
    super(message);
    this.name = "StudioError";
  }
}
