# Agentic AI Workshop — Penn Epigenetics Institute

Teaching materials for the taught session on **Thursday 24 September 2026, 10:00–14:00**,
at the Penn Epigenetics Institute. Instructor: Sean Davis.

The afternoon after 14:00 is self-directed and runs from the Vahedi lab's own repository:
<https://github.com/golnazvahedi/epigenetics-agentic-workshop>.

## What's here

| | |
|---|---|
| [`docs/`](docs/) | The attendee-facing workshop page (GitHub Pages) |
| [`exercises/`](exercises/) | The three hands-on exercises and the ledger template |
| [`examples/`](examples/) | A worked example skill, ready to drop into a lab repo, and the specs for the two stretch exercises |
| [`adr/`](adr/) | Decision records — why the workshop is shaped the way it is |
| [`LEDGER.md`](LEDGER.md) | This repo's own work ledger, in the format the workshop teaches |

Slides live in the [`talks`](https://talks.seandavis.net) repository, under
`talks/agentic-coding/venues/`, because that's where the theme, extensions, and render
pipeline are. They publish to talks.seandavis.net like every other deck.

## The session

Short teaching blocks alternating with three exercises, each producing something the
attendee keeps.

| Time | Session |
|---|---|
| 10:00 | From chatbot to agent |
| 10:25 | **Exercise 1** — first contact, and open your ledger |
| 10:55 | Under the hood: tokens, context, and cost |
| 11:15 | *Break* |
| 11:25 | Working well: memory, context hygiene, and verifying |
| 11:45 | **Exercise 2** — teach the agent your project |
| 12:15 | *Lunch* |
| 13:00 | Reaching outside your files: skills and MCP, with a live demo |
| 13:25 | **Exercise 3** — write one skill |
| 13:50 | Takeaways, and handing over to the afternoon |
| 14:00 | Afternoon — self-directed, with the Vahedi lab |

## Division of labour

Sean owns the taught session, these exercises, and the slides. Golnaz Vahedi and her lab
own the logistics (room, Claude Team seats, catering, the pre-workshop email to attendees)
and the self-directed afternoon.

The exercises are deliberately generic — attendees are told to use their own safe material
first, and each exercise names a fallback from the Vahedi repository for anyone who hasn't
got something to hand. That keeps this session independent of the afternoon's material
while still giving everyone a guaranteed dataset.

## Attendee setup

Attendees clone the Vahedi repository (it carries the datasets and the afternoon
exercises) and read these exercises from the workshop page. Full instructions are on
[`docs/index.html`](docs/index.html).
