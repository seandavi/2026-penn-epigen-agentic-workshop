# ADR-0006 — Advanced material ships as a non-presented appendix

**Date:** 2026-09-22
**Status:** accepted (refines [ADR-0002](0002-exercises-are-menus.md); partially revisits
the cut recorded there)

## Context

Six topics were proposed for the deck: pointers to Claude Science, harness-versus-model
performance, how to read benchmarks, higher-order workflows with skills, specifying
goals for autonomous work, and git/GitHub coordination including worktrees.

All six are good. The session has no slack: 100 minutes of teaching against 85 of
exercises inside a four-hour window. Six topics at five minutes each is thirty minutes
that would have to come out of the exercises, which would mean dropping one.

Two of the six — the multi-stage workflow loop and git/worktrees — are also the
developer material deliberately cut earlier on the grounds that most of this room does
not run multi-stage agent pipelines.

Separately, the afternoon is self-directed and someone will ask an advanced question
we have no slide for.

## Decision

Three topics go on stage, and must earn their place by displacing something:
specifying goals, Claude Science, and harness-versus-model. Benchmarks fold into the
harness slide's speaker notes rather than taking a slide. `A server is three decisions`
is demoted from Part 4 to pay for the additions.

The remainder ships as an **appendix after the close, which is not presented**. The
deck is `handout: true`, so appendix slides reach every reader of the notes PDF at zero
cost in stage time.

Appendix slides MUST stand alone. They are a lookup table for a question asked at 3pm,
not a sequence — reveal's menu jumps straight to any of them.

## Consequences

Good: the exercises keep their 85 minutes, which is the part of the day that changes
behaviour. Advanced questions have an answer that is already written rather than
improvised. The computational minority get the material they want without the rest of
the room sitting through it.

Bad: a deck that is longer than the talk. Anyone reading the handout cold has to
understand that the appendix was not delivered, which the divider's notes have to say
explicitly. And appendix content is unrehearsed — presenting from it live is a
different risk than presenting from the session proper.

The Claude Science slide carries a dependency we do not control: it is beta, on paid
plans, and the product may change. Its argument must not rest on anyone adopting it —
the transferable claim is that `SKILL.md` is the unit of composition in serious
tooling, which survives the product changing.
