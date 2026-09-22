# Exercise 3 — Write One Skill

**About 25 minutes.** A skill is a folder with a Markdown file in it. That's the whole
mechanism. The hard part isn't writing one — it's writing one that actually fires when you
need it.

## Pick a procedure

Something you repeat and currently re-explain every time. Pick from here or bring your own:

| | The skill |
|---|---|
| **Ledger summary** | Read `LEDGER.md` and report **who did what**: what the agent did, what you actually verified, and — the interesting part — which entries have an empty *Checked how*. A skill that audits your own discipline. |
| **Ledger entry** | The companion: append a properly-formatted entry for whatever just happened. Small, guaranteed to work, and it makes writing the ledger cost nothing. |
| **Results-table triage** | The standard checks for any results file you're handed: chromosome naming, missing adjusted p-values, impossible widths, underflowed p-values, whether the fold-change direction is stated anywhere. Encode the traps you know about once. |
| **Reference check** | Walk a draft and verify every citation resolves *and* says what the sentence claims it says. The single highest-value check in scientific writing. |
| **Paper → lab meeting** | A PDF in, ten bullets out, pitched at a named audience, plus the three questions you'd get asked. |
| **Reviewer 2** | A persona with your field's standards that attacks a paragraph before a real reviewer does. Then drafts the response. |
| **New project folder** | Scaffold an analysis directory the way *you* do it — naming, structure, where figures go, what a finished analysis looks like. |
| **Figure legend** | Bullets in, a legend out, in the style your usual journal wants. |
| **Methods paragraph** | Draft from what actually happened, marking every unknown `[PLACEHOLDER]` rather than inventing it. |

## Do this

**1. Make the folder.** A skill is a directory containing `SKILL.md`. The directory name and
the `name` field must match, lowercase with hyphens.

```
.claude/skills/ledger-summary/SKILL.md      # this project only, commit it
~/.claude/skills/ledger-summary/SKILL.md    # every project you work on
```

**2. Write it.** Only two fields are required:

```markdown
---
name: ledger-summary
description: Summarizes the LEDGER.md work log — what the agent did, what
  the human verified, and which entries were never checked. Use when the
  user asks to summarize the ledger, review the log, see what we did, or
  asks who did what or what still needs checking.
---

## Instructions

1. Read `LEDGER.md`. If it does not exist, say so and stop.
2. For each entry, extract: what was asked, what the agent did, and what
   the human verified.
3. Produce a table of entries with a one-line summary of each.
4. Then report separately:
   - entries where **Checked how** is empty or vague — list these first
   - everything recorded under **Confidently wrong**, gathered together
5. Do not fill in any missing verification yourself, and do not judge
   whether a check was sufficient. Report what is there.
```

Three choices worth stealing. The `description` says **what it does, then when to use it**,
and contains the words you'd actually say. Step 5 forbids the tempting adjacent action —
an agent that helpfully fills in your missing verification has destroyed the only thing the
ledger was for. And it says *stop*, because left unconstrained it will keep going.

**3. Test the description, not the body.** This is the step everyone skips and the reason
most skills quietly never fire. Write two lists:

| Should fire | Should **not** fire |
|---|---|
| "summarize my ledger" | "add an entry to my ledger" |
| "what did we actually check today?" | "explain how skills work" |
| "who did what in this log?" | "delete my ledger" |

Now start a fresh session and try them. Did the right ones trigger it? Did the wrong ones
leave it alone? If a phrasing you'd genuinely use didn't fire, put those words in the
description and try again.

## The failure you will not notice

A skill that never triggers is indistinguishable from a skill you never wrote. No error, no
warning — you just get the answer you'd have got anyway. That's why the description gets
tested and the body mostly doesn't: **the agent never sees the body until it has already
decided to load it.**

Lean pushy. The common failure is under-triggering, not over-triggering.

## It isn't tool-specific

`SKILL.md` is an open standard, read by Claude Code, Codex CLI, Gemini CLI, Copilot and
others without translation. The file you just wrote works across whichever you switch to,
which is the main argument for encoding a procedure this way rather than keeping it in your
head.

## Success looks like

A skill that fires on a phrase you didn't put in the description verbatim, and doesn't fire
on a neighbouring question. That's a working interface, not a hopeful Markdown file.

## If you finish early

Commit it into a shared lab repository. That's the highest-leverage version of this whole
mechanism: one person writes the procedure once, and everyone who clones the repo gets it.
For a lab with shared conventions and rotating trainees, that's worth more than anything
else here.
