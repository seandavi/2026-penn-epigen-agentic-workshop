# Rules for agents working in this repository

Writing rules for the book (voice, chapter shape, cross-references, rendering) are in
[book/AGENTS.md](book/AGENTS.md). Decisions are in [adr/](adr/README.md).

## The ledger

This repository keeps the ledger it teaches ([ADR-0005](adr/0005-the-ledger-is-the-spine.md)).

- **Every substantive change gets an entry in [LEDGER.md](LEDGER.md)**, in the same
  commit series as the work: new or changed book content, exercises, ADRs, tooling.
  Typo fixes and re-renders don't need one.
- Number entries in sequence, and use the five fields: **Asked**, **Agent did**,
  **Checked how**, **Confidently wrong**, **Keep**.
- **Asked** quotes SD's words, not a paraphrase.
- **Checked how** must never be blank. Say who checked (*Agent* or *SD*), and what
  was actually run or read. List what was **not** checked, too. Never record a check
  that didn't happen.
- **Confidently wrong** records what was wrong before it was caught, including the
  agent's own mistakes. "Nothing caught" is a legitimate entry.
