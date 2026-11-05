export type AnyObj = Record<string, any>;

/** Sets a value inside the funnel being edited (an `undefined` value removes the key). */
export type SetFunnel = (path: (string | number)[], value: unknown) => void;

/** What every section of the funnel editor gets: the funnel as written so far, and how to change it. */
export interface FunnelFieldsProps {
  funnel: AnyObj;
  set: SetFunnel;
}
