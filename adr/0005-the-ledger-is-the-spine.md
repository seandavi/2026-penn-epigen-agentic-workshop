# ADR-0005 — The ledger is the spine of the day

**Date:** 2026-09-22 (recorded 2026-09-23)
**Status:** accepted

## Context

The day's central claim is that an agent's errors are fluent, confident, and
indistinguishable from its correct output — so verification is not a formality but the
step that makes the work usable.

Saying that from the front of a room changes nobody's behaviour. It needs an artifact.

We also needed something to connect three otherwise independent exercises, and
something that survives the 14:00 handover into an afternoon we do not run.

## Decision

Every attendee keeps a `LEDGER.md` from the first exercise onward. Five fields per
entry: **Asked**, **Agent did**, **Checked how**, **Confidently wrong**, **Keep**.

*Checked how* must never be blank. Exercise 3's recommended skill reads the ledger back
and reports which entries have an empty one.

This repository keeps a ledger of its own work in the same format — see
[ADR-0002](0002-exercises-are-menus.md) for why the material has to be credible on its
own terms.

## Consequences

Good: the verification habit becomes a visible gap rather than a good intention. An
empty field is uncomfortable in a way "I meant to check" is not. It gives the
unstructured afternoon a spine that costs the Vahedi lab nothing to enforce, and it is
the share-out material at the close.

Bad: it is bookkeeping, and some people will resent it. It costs three minutes per
exercise out of thirty. If the room treats it as busywork the mechanism fails, so it
has to be introduced as the point rather than as admin.

*Confidently wrong* must be framed so that "nothing caught" is a legitimate entry,
otherwise diligent attendees will invent failures to fill the box.

## Correction (2026-09-23)

Two things this record left implicit, made explicit at SD's request:

- **The agent writes the ledger**, when asked or, under a standing instruction, on its
  own. The attendee must read each entry and correct *Checked how*; the attendee must
  not accept the agent's account of its own checking as written.
- **The ledger records what matters, not everything.** An entry covers a piece of work
  someone may later need to know about, usually several prompts. Small tweaks must not
  get entries of their own.
