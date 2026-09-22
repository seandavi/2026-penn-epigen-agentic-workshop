# Exercise 3 — Write One Skill

**About 25 minutes.** A skill is a folder with a Markdown file in it. That's the whole
mechanism. The hard part isn't writing one — it's writing one that actually fires when you
need it.

## Pick a procedure

Something you repeat and currently re-explain every time. Good candidates:

- "Generate our standard QC report from a differential peaks file" — the checks to run, the
  plots to make, the format to write it in
- "Set up a new analysis folder the way our lab does it"
- "Check a manuscript's figure callouts against the figures that exist"

**Or the fallback, which is guaranteed to work and which you'll use this afternoon:** a
skill that writes your ledger entries for you. Small, complete, and it makes the rest of
the day faster.

## Do this

**1. Make the folder.** A skill is a directory containing `SKILL.md`. The directory name
and the `name` field must match, lowercase with hyphens.

```
.claude/skills/lab-ledger/SKILL.md      # this project only, commit it
~/.claude/skills/lab-ledger/SKILL.md    # every project you work on
```

**2. Write it.** Only two fields are required:

```markdown
---
name: lab-ledger
description: Appends an entry to the LEDGER.md work log recording what was
  asked, what the agent did, how it was verified, and anything it got wrong.
  Use when the user says to log this, write it up, record what we just did,
  add to my ledger, or asks for a note of the work so far.
---

## Instructions

1. Read `LEDGER.md` in the project root. If it does not exist, create it from
   `LEDGER-template.md`.
2. Append a new numbered entry with these headings: Asked, Agent did,
   Checked how, Confidently wrong, Keep.
3. Fill **Asked** with the user's prompt verbatim — do not tidy or paraphrase it.
4. Fill **Agent did** with the actual files read or written and commands run.
5. Leave **Checked how** blank and tell the user to complete it themselves.
   **Do not fill this in on their behalf.**
6. Show the user the entry and stop. Do not commit anything.
```

Three choices worth stealing from that. `description` says **what it does, then when to use
it**, and contains the words you'd actually say. Step 5 refuses to do the one thing the
skill must never do — the verification has to be yours or the ledger is worthless. And it
says *stop*, because left unconstrained an agent will helpfully keep going.

**3. Test the description, not the body.** This is the step everyone skips and the reason
most skills quietly never fire. Write two lists:

| Should fire | Should **not** fire |
|---|---|
| "log this" | "what's in my ledger so far?" |
| "write up what we just did" | "explain how skills work" |
| "add that to my ledger" | "commit my changes" |

Now start a fresh session and try them. Did the right ones trigger it? Did the wrong ones
leave it alone? If a phrasing you'd genuinely use didn't fire, add those words to the
description and try again.

**4. Ledger entry 3** — written by the skill, if it works.

## The failure you will not notice

A skill that never triggers is indistinguishable from a skill you never wrote. There's no
error and no warning; you just get the answer you'd have got anyway. That's why the
description gets tested and the body mostly doesn't — the description is the entire
triggering signal, and the agent never sees the body until it has already decided to load it.

Lean pushy. The common failure is under-triggering, not over-triggering.

## It isn't tool-specific

`SKILL.md` is an open standard now, read by Claude Code, Codex CLI, Gemini CLI, Copilot and
others without translation. The file you just wrote works across the ones you're likely to
switch to, which is the main argument for encoding a procedure this way rather than keeping
it in your head.

## Success looks like

A skill that fires on a phrase you didn't put in the description verbatim, and doesn't fire
on a neighbouring question. That's a working interface, not a hopeful Markdown file.
