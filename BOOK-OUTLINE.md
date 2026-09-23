# The book: chapter outline (draft for SD)

Working document, to be deleted once the chapters exist. See
[ADR-0007](adr/0007-talk-first-then-a-self-paced-book.md) for the shape of the day.

## The day

| Time | What |
|---|---|
| 10:00–12:00 | Talk: chatbot to agent, under the hood, working well, skills and MCP. Demos and discussion, no exercises. |
| 12:00–13:00 | Lunch |
| 13:00–13:15 | Getting started, ad-libbed: open chapter 0, get everyone's agent running |
| 13:15–14:30 | The book, at your own pace, with Sean in the room |
| 14:30– | The Vahedi lab's afternoon |

Most people will reach chapter 2 or 3 by 14:30. The rest of the book has to work read
alone, later.

## How every chapter is built

Like RBiocBook: discussion drives the activity.

1. **A few paragraphs on why.** What problem this solves, and what goes wrong without it.
2. **What you'll learn:** three to five bullets.
3. **A worked example**, with commentary: a real prompt, what the agent did, what we
   checked and what we found.
4. **Your turn:** the activity. Your own material first, a fallback second (ADR-0002).
5. **What to notice**, and **check yourself**: how you know it worked.
6. **Callouts** for pitfalls, privacy, and **Windows**.

Each chapter must say which **Windows** steps differ (paths, hidden file extensions,
PowerShell, opening files), and must not need `git` unless it's the git chapter.

## Chapters

### 0. Setup

- Get your agent running: the Claude desktop app or Claude Code, on macOS or Windows.
- Make a workshop folder in Documents. Start a new session there, and ask "what folder
  are you in?"
- Permission prompts: what they mean, and what's safe to allow.
- **Windows:** where Documents is, turning on file extensions, opening a terminal if
  needed. Claude Code on Windows: check what it currently requires before writing this.
- From: `docs/index.html` setup section.

### 1. Build a website

- **Why:** the fastest way to see what an agent *does*, as opposed to what a chatbot
  *says*: it makes files, and you can open the result.
- **Activity:** "Make me a one-page website about <my lab / a paper / a method I use>."
  One HTML file you double-click. Then change it twice by asking.
- **Notice:** it wrote files you can open; it may say it checked things it couldn't
  see; nothing was installed.
- **Check yourself:** it opens in your browser; you can find the file on disk.
- **Privacy:** only what you'd put on a public page.
- From: Exercise 1 (first contact), rewritten around a single tangible result.

### 2. The ledger

- **Why:** an agent's work is invisible unless someone writes down what was asked, what
  was done and how it was checked. The ledger is how you (and your PI, a reviewer, or you
  in six months) know which parts to trust. "Checked how" is the field that matters, and
  "Confidently wrong" is the one people skip.
- **Examples:** *AI in Medicine*'s
  [How this book was made](https://ai-in-medicine.seandavi.workers.dev/appendix/about)
  and its [AI ledger](https://ai-in-medicine.seandavi.workers.dev/appendix/ai-ledger);
  this repository's own `LEDGER.md`.
- **Activity:** the chapter 1 website again. Add a ledger entry for what you already
  did, honestly; then make one more change, ledgering it as you go. Then ask the agent
  to keep the ledger for you, and check what it writes.
- **Notice:** the agent's entries claim more checking than happened, unless you ask.
- From: Exercise 1's ledger half, `LEDGER-template.md`, ADR-0005.

### 3. Teach the agent your project

- **Why:** in a real analysis directory the agent can't know which data are raw, which
  scripts are current, or what "done" means. You end up repeating yourself; the fix is
  to write it down once, in files the agent reads.
- **README vs AGENTS.md:** a README is for people (what this is, how to run it);
  AGENTS.md (or CLAUDE.md) is for agents: only what an agent can't work out by reading
  the folder, as rules. **Links**: point to other documents instead of copying them
  ("the sample sheet is described in docs/samples.md"), so the agent reads them when it
  needs them and they stay in one place.
- **Activity:** an analysis folder of your own (fallback: to be chosen; not yet checked
  whether the Vahedi repository has one complex enough). Ask the agent to explore and summarise it; correct what it gets
  wrong; turn the corrections into AGENTS.md; start a new session and see whether it
  holds.
- **Windows:** CLAUDE.md vs AGENTS.md naming; hidden dot-folders.
- From: Exercise 2.

### 4. Write a skill

- **Why:** a skill is a folder of instructions and scripts an agent loads when a task
  needs it. It turns "how our lab does X" into something reusable.
- **The point to stress:** you don't write the skill. **The agent writes it, with your
  direction, and you verify it**: you say what good looks like, you test it on real
  data, you read what it does.
- **Worked example:** `deseq2-triage`, walked through: what's in the folder, why each
  part is there, what it caught on real DESeq2 output.
- **Activity:** direct the agent to write a triage skill for a result file you know well
  (fallback: the Vahedi DESeq2 output). Verify it on a file where you know the answer.
- From: Exercise 3, `examples/skills/deseq2-triage/`.

### 5. Build an app

- **Why:** an app is where agents shine and where they fail quietly. The difference is
  the spec: what it does, what it must not do, and how you'll know it's right.
- **A starter prompt** that leads the attendee, with the agent, toward an app *they*
  want:
  1. asks what they work on, and suggests ideas from their chapter 3 project;
  2. **checks what's on their machine** (a browser only? R? Python? Node? `git`?) and
     picks a build that needs nothing new, a double-click web page if in doubt;
  3. writes a **small specification** with them: what it does, what it doesn't, a small
     test case with answers worked out by hand, and the decisions to make;
  4. builds it from the spec, then says what it checked and what it couldn't.
- **Worked example:** PeakPeek: a spec good enough that one prompt built it in 13–15
  minutes, twice, and what the builds still got wrong. Also the fallback for anyone
  without an idea.
- From: PR #6 (PeakPeek exercise and spec).

### 6. Work like a project

- **Why:** a one-off app is fine; anything you'll come back to needs a record of *what
  was decided and why*, and a way back when a change goes wrong.
- **Activity:** keep improving the chapter 5 app with the agent, now with:
  - the **ledger** for every change;
  - **ADRs**: one short record per decision that would be awkward to reverse; superseded,
    never edited;
  - **git**, if you have it or can install it: a commit per change, and going back.
    If you can't, snapshots of the folder, made by the agent.
- **Worked example:** PeakPeek on GitHub (seandavi/peakpeek): spec, ADRs, ledger,
  signed-off issues; and its issue #1 for taking it further (issues, pull requests, CI).
- **Windows:** installing git (Git for Windows / `winget`); what to do if you can't.
- From: `adr/`, PeakPeek's repo, the peak-overlap exercise (as "further still").

## Open questions for SD

1. **Order:** is this 0–6 what you meant? You wrote "for 4" about the app; I've put the
   skill at 4 and the app at 5, so the app can build on chapter 3's project.
2. **"The skill chapter, but we'll need clear …"**: clear what? Clear instructions, a
   clear worked example, clear verification steps?
3. **Format:** a Quarto book on GitHub Pages, like RBiocBook, replacing `docs/index.html`?
4. **Chapter 1's website:** about their lab, a paper, or anything they like?
5. **The Vahedi lab:** 14:30 instead of 14:00. Will you tell Golnaz, or should I draft a
   note for you to send?
6. **Slides:** shall I draft the deck changes in the `talks` repo, or will you?
7. **PR #6:** merge first (chapter 5 builds on it)?
