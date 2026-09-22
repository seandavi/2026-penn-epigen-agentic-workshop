# ADR-0003 — Slides live in the talks repo, not here

**Date:** 2026-09-22 (recorded 2026-09-23)
**Status:** accepted

## Context

This repository holds the exercises and the workshop page. The deck could have lived
here too, which would have kept everything about the workshop in one place.

But the deck is a Quarto reveal.js project that depends on a theme, a livefigures
extension, a citation pipeline, QR generation, a build CLI, and a Cloudflare deploy
workflow — all of which live in the `talks` monorepo. Reproducing any of it here would
mean maintaining two copies.

The `agentic-coding` topic in that repo is also a deliberate fragment collection: this
deck reuses nine shared slide fragments that other venue decks share. Authoring
elsewhere would have forked them.

## Decision

The deck lives at `talks/agentic-coding/venues/2026-09-24-penn-epigenetics.qmd` in the
`talks` repository and publishes to talks.seandavis.net with every other deck.

This repository must link to the published deck rather than vendor a copy of it.

## Consequences

Good: the deck gets the theme, the handout PDF, the shared fragments, and the deploy
pipeline for free. A fix to a shared fragment reaches every deck that uses it.

Bad: the workshop's material is split across two repositories, and someone looking
here for the slides has to follow a link. The README says where they are.

Also: publishing the deck means pushing to `talks` `main`, which deploys the entire
site. That is a wider blast radius than a workshop change warrants, and it is worth
knowing before a hurried edit on the morning of.
