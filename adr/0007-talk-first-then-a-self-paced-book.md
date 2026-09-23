# ADR-0007 — Talk first, then a self-paced book

**Date:** 2026-09-23
**Status:** accepted. Supersedes the timetable in [ADR-0001](0001-taught-session-ends-at-1400.md).

## Context

The taught session alternated short talks with three timed exercises. Each exercise cut
the talk into pieces, left little room for questions and discussion, and assumed
everyone would finish in 25–30 minutes. The hands-on briefs were terse menus that relied
on the instructor being in the room to explain *why*. Meanwhile the stretch exercises
grew into self-contained, explanatory documents, and worked better that way.

Sean's lab already writes self-paced material this way: RBiocBook's chapters, and the
*AI in Medicine* book, where discussion drives each activity.

## Decision

Split the day into a talk and a book.

- **10:00–12:00, the talk.** No exercises inside it. Short live demos, questions and
  discussion instead.
- **12:00–13:00, lunch.**
- **13:00–14:30, hands-on, with Sean in the room.** A short getting-started, ad-libbed,
  then attendees work through the book at their own pace.
- **The book** is a set of chapters, each explaining why before asking anyone to do
  anything, in the style of RBiocBook. Every chapter must work on **Windows** as well as
  macOS, and must not require `git` unless it says so and offers a way round.

ADR-0002 still holds: each chapter's activity starts from the attendee's own material,
with a fallback.

## Consequences

- The deck loses its three exercise slots, and gains demos and discussion prompts.
- The exercises are rewritten as chapters, not edited in place.
- Nobody is expected to finish the book by 14:30. It has to make sense read alone,
  later, without Sean.
- The Vahedi lab's afternoon now starts at 14:30, not 14:00. They need to hear that.
