# Agentic AI Workshop — Penn Epigenetics Institute

Teaching materials for the Penn Epigenetics Institute agentic AI workshop, **Thursday 24
September 2026**. Instructor: Sean Davis.

**The book (hands-on half): <https://seandavi.github.io/2026-penn-epigen-agentic-workshop/>**

The afternoon from 14:30 is self-directed and runs from the Vahedi lab's own repository:
<https://github.com/golnazvahedi/epigenetics-agentic-workshop>.

## What's here

| | |
|---|---|
| [`book/`](book/) | The book's source (Quarto). Renders to `docs/`, which GitHub Pages serves. Writers' rules: [`book/AGENTS.md`](book/AGENTS.md) |
| [`exercises/`](exercises/) | The ledger template and the two stretch exercises the book links to |
| [`examples/`](examples/) | A worked example skill, and the specs for PeakPeek and peak overlap |
| [`adr/`](adr/) | Decision records: why the workshop is shaped the way it is |
| [`LEDGER.md`](LEDGER.md) | This repo's own work ledger, in the format the workshop teaches |

Slides live in the [`talks`](https://talks.seandavis.net) repository, under
`talks/agentic-coding/venues/`, and publish to talks.seandavis.net like every other deck.

## The day

A talk, then a book ([ADR-0007](adr/0007-talk-first-then-a-self-paced-book.md)).

| Time | Session |
|---|---|
| 10:00–12:00 | Talk: from chatbot to agent; under the hood; working well; skills and MCP. Demos and discussion. |
| 12:00–13:00 | *Lunch* |
| 13:00–14:30 | Hands-on: a short getting-started, then the book at your own pace |
| 14:30 | The Vahedi lab's self-directed afternoon |

## Building the book

```bash
uv tool install quartobot     # resolves @doi:/@pmid:/@url: citations before render
cd book && quarto render      # writes ../docs/
```

Commit `book/references.resolved.bib` and `docs/` with the source.

## Division of labour

Sean owns the talk, the book, and the slides. Golnaz Vahedi and her lab
own the logistics (room, Claude Team seats, catering, the pre-workshop email to attendees)
and the self-directed afternoon.

The book is deliberately generic — attendees are told to use their own safe material
first, and each chapter names a fallback from the Vahedi repository for anyone who hasn't
got something to hand. That keeps this session independent of the afternoon's material
while still giving everyone a guaranteed dataset.

## Attendee setup

In the book: [Setup](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/00-setup.html).
