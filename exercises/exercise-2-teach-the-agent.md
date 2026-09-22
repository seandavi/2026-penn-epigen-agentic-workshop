# Exercise 2 — Teach the Agent Your Project

**About 30 minutes.** An agent starts every session knowing nothing about you. A context
file is how you stop re-typing the same things forever — and this exercise measures whether
it actually helped, rather than assuming it did.

## Pick your project

**Your own**, ideally: an analysis folder, a repository, a manuscript directory, even a
folder of notes. It should be something you return to.

**Or the fallback**: use the workshop repository itself, and pretend `track-a/data/` is your
lab's standard output format.

## Do this

**1. Have the agent interview you.** Don't write the file yourself — you'll forget the
things that are obvious to you, which are exactly the things it needs.

> I want to write a context file for this project so that you — and any agent I use in
> future — start each session already knowing how it works. Interview me. Ask one question
> at a time, and look around the repository first so you don't ask me things you can work
> out yourself. When you've got enough, write `AGENTS.md`.

The "one question at a time" and "look first" instructions both matter. A list of eight
questions gets eight careless answers, and an agent that asks you what's in a folder it
could have opened is wasting the thing you're actually short of.

**2. Read what it wrote, and cut it.** This is the real skill. For every line, ask:

> Would removing this line cause a mistake?

If not, delete it. **Keep**: the commands it can't guess, the genome build, where data
actually lives, naming conventions, which script is canonical and which is abandoned, the
thing that looks like a bug and isn't. **Cut**: anything true of everyone's project,
anything discoverable from the code, and aspirational style rules nobody enforces — those
teach the agent that the file can be ignored.

Most first drafts lose half their lines here and get better.

**3. Measure it.** Start a **fresh session** — this matters, the old one already knows
everything you just discussed — and run one realistic task twice: once with the context
file present, once with it renamed out of the way.

Where did it differ? Fewer wrong guesses? Right conventions without being told? Fewer
questions back at you? Sometimes the answer is *no difference*, and that is a genuinely
useful result: it means the file is restating what the agent could already see.

**4. Ledger entry 2.** What changed between the two runs. If nothing did, write that.

## A note on file names

`CLAUDE.md`, `GEMINI.md`, `AGENTS.md` — same idea, different tools. `AGENTS.md` is the
one most tools now read, so prefer it unless you know you're staying on one. Some tools
read several; a one-line `CLAUDE.md` saying "see AGENTS.md" costs nothing.

## Success looks like

A context file short enough that you'd actually keep it current, and an opinion —
supported by two transcripts — about whether it earned its place.

## Where this goes wrong later

Context files rot. The conventions change and the file doesn't, and six months on it is
confidently instructing your agent to do something you stopped doing in March. If you take
one of these back to your lab, give it an owner and a review date, the way you would a
protocol.
