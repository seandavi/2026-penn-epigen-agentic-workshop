# ADR-0002 — Exercises are menus of the attendee's own work

**Date:** 2026-09-22 (recorded 2026-09-23)
**Status:** accepted

## Context

The first draft of the exercises pointed everyone at one prescribed file — a real
DESeq2 peak table with instructive quirks. It was a good file and the wrong default.

Two problems. A room of forty doing the identical task produces a share-out where
nobody has anything to say. And the audience is mixed: for a bench scientist with no
analysis in their week, a peak table is someone else's work, and the exercise teaches
that these tools are for other people.

The attendees, meanwhile, all have something they have been meaning to do and haven't.

## Decision

Every exercise is a menu. The first option is always the attendee's own material, and
the brief says plainly that none of it requires writing code.

The prescribed dataset survives as a named fallback for anyone who arrives with nothing
in mind. It must not be presented as the default.

## Consequences

Good: people work harder on something they wanted done. The share-out is worth having,
because everyone did something different. The day generalises beyond epigenomics
without becoming generic, since the failure modes taught are still the field's own.

Bad: we cannot predict what breaks. Forty different tasks is forty different ways to
get stuck, and roving support is harder than a room doing one thing. The menu items
have to be sized so that most are finishable in thirty minutes, which rules out some
of the more interesting options.

We accept that some attendees will pick something too big. The briefs and the speaker
notes both tell them to scope down, and that is the best available mitigation.
