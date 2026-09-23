# Architecture decision records

One short file per decision that would be awkward to reverse. Numbered, appended
rather than edited, and superseded rather than deleted — a decision we later reversed
stays readable, because the reasoning is the point.

Each record is three headings:

- **Context** — what situation forced a choice
- **Decision** — what we chose, in the active voice
- **Consequences** — what we now live with, including the parts we don't like

Records 0001–0005 were written on 2026-09-23 and backdated to the day the decisions
were actually taken, which was the day the workshop was planned. They are honest about
their reconstruction: see the dates in each file.

| | Decision | Date |
|---|---|---|
| [0001](0001-taught-session-ends-at-1400.md) | The taught session ends at 14:00 and hands off (timetable superseded by 0007) | 2026-09-22 |
| [0002](0002-exercises-are-menus.md) | Exercises are menus of the attendee's own work | 2026-09-22 |
| [0003](0003-slides-live-in-the-talks-repo.md) | Slides live in the talks repo, not here | 2026-09-22 |
| [0004](0004-tool-neutral-claude-code-supported.md) | Tool choice stays open; Claude Code is supported | 2026-09-22 |
| [0005](0005-the-ledger-is-the-spine.md) | The ledger is the spine of the day | 2026-09-22 |
| [0006](0006-advanced-material-ships-as-appendix.md) | Advanced material ships as a non-presented appendix | 2026-09-22 |
| [0007](0007-talk-first-then-a-self-paced-book.md) | Talk first, then a self-paced book | 2026-09-23 |

## Why `adr/` and not `docs/adr/`

`docs/` is this repository's GitHub Pages source, so anything inside it is published
as the attendee-facing site — and Jekyll rewrites `.md` links to `.html`, which would
break the index above. Project documentation lives outside the served directory.

## Writing a new one

Copy [`template.md`](template.md), take the next number, add a row above. Prefer
imperative language — *must*, *must not* — over "we generally prefer", which reads as
advisory to a human and as negotiable to an agent.
