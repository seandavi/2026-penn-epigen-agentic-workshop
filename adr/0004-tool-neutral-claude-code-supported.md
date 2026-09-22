# ADR-0004 — Tool choice stays open; Claude Code is the supported default

**Date:** 2026-09-22 (recorded 2026-09-23)
**Status:** accepted

## Context

The organiser reported that most attendees are already on Claude through an
institutional Team plan. Standardising on one tool would minimise setup failures, which
are the single largest risk to a hands-on morning.

Against that: the material argues that `SKILL.md` is a cross-vendor open standard read
by more than forty products, and that procedures encoded this way are not a bet on one
vendor. Mandating a single tool while making that argument is incoherent. An earlier
run of this material at Harvard let attendees pick any of four agents.

Some attendees are also already productive in Codex, Gemini CLI or Copilot, and
forcing a switch wastes their morning.

## Decision

Any working agent is welcome. Claude Code is what gets demonstrated and what the TAs
support.

The distinction that binds is narrower than "required": the exercise briefs must be
written in one tool's commands without branching, and TA support covers that tool only.
Nobody is turned away.

## Consequences

Good: no setup failure caused by someone hesitating over which of four tools to
install. The open-standard argument stays honest.

Bad: attendees on other tools hit one genuine divergence — MCP configuration lives in a
different file for each tool. The deck carries the mapping.

We must not describe the workshop as requiring Claude Code in any attendee-facing
material.
