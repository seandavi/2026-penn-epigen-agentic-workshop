# Exercise 2 — Go Further, and Stop Repeating Yourself

**About 30 minutes.** Take something real a good distance, and let the friction tell you
what belongs in a memory file. Not the other way around.

## First, a correction

You may have heard that the first thing to do with an agent is write it a big context file
describing your project. Mostly you shouldn't. **Agents are very good at working out what a
project is** — they read the files, the README, the code, the data. A file that restates
what's already discoverable costs context on every turn and earns nothing.

What an agent genuinely cannot work out is what's only in your head:

- how you like things done, and what "finished" means to you
- which of the four scripts in that folder is the real one
- the constraint that looks like a mistake and isn't
- the thing you'd correct in review, every time, forever

Those are worth writing down. Nothing else is. This exercise finds yours by working until
you hit them.

## Pick something with more than one step

Either carry on with what you started in Exercise 1, or take something new:

| | Try this |
|---|---|
| **Finish and publish** | Take the site, review, or deck from Exercise 1 and get it actually done — deployed, exported, sent. |
| **A real multi-step job** | Find data → analyze it → write up what you found. Three stages, checked between each. |
| **Something you do repeatedly** | The report you rebuild monthly, the figure you remake for every talk. Do it once, properly, with the agent. |
| **A piece of writing that matters** | A grant aims page, a talk outline, a response to reviewers. Draft, then have it argue against you. |
| **A pile of documents** | A folder of PDFs, applications, or notes → a structured table you can sort and filter. |
| **Build and ship a small app** | A dashboard over a public resource — ENCODE, 4D Nucleome, GEO — or over your own lab's datasets. Then actually deploy it somewhere with a URL. |

## Do this

**1. Work for about twenty minutes.** Properly — get somewhere. Keep interrogating results
the way you did in Exercise 1.

**2. Keep a running note of the friction.** This is the actual instrument of the exercise.
Every time one of these happens, jot a line:

- you explained something **twice**
- it did something in a style you had to correct
- it asked you a question you'd already answered
- it made a reasonable choice that was **wrong for you specifically**
- you thought *"it should have known that"*

**3. Now write the file — only from that list.** Create `AGENTS.md` in the folder:

> Here's what I had to tell you or correct during this session: [your list]. Write an
> `AGENTS.md` capturing just those, as instructions for a future session. Keep it short,
> and leave out anything you could work out by reading the project yourself.

If your list is empty, **write no file**. That is a real and useful outcome, and it's the
honest answer more often than the internet suggests.

**4. Use it.** Start a fresh session, point it at the folder, and give it the next piece of
the task. Did the things you wrote down stay fixed without you saying them again?

**5. Ledger entry two.** What you had to repeat, and whether writing it down stopped it.

## A note on file names

`AGENTS.md`, `CLAUDE.md`, `GEMINI.md` — same idea, different tools. `AGENTS.md` is the one
most tools now read, so prefer it unless you know you're staying on one.

## Success looks like

A short file you'd actually keep current, every line of which traces to a moment you
watched happen — or a considered decision that you don't need one yet.

## Where this goes wrong later

Memory files rot. Conventions change and the file doesn't, and six months on it's
confidently instructing your agent to do something you stopped doing in March. If you keep
one, give it an owner and a review date, the way you would a protocol.
