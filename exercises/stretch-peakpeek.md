# Stretch — Spec First, Then Build: PeakPeek

**An afternoon, not a slot.** This one is for after 14:00, or for anyone who finished the
morning early.

**PeakPeek is a page that tells you what's in a peak file.** Drop in a BED or narrowPeak
file, or paste a URL, and it shows you how many peaks there are, how wide they are, which
chromosomes they're on, and what's wrong with the file. Give it several files and it
lines them up side by side.

You'll hand a finished spec to your agent and get the whole page back **in one prompt**.
Then you'll spend the rest of the afternoon on the parts that are yours: checking whether
the numbers are right, and changing the page to do what *you* want.

**Everything stays on your laptop.** No GitHub account, no `git`, no Node, no server. You
open the page by double-clicking a file. If you have `git`, use it; nothing here depends
on it.

The point is not the page. It's that **a spec good enough to build from in one go is
where the work actually happened**, and the checking is still yours.

## What you'll need

- Your agent, as in the morning
- A browser. Chrome is what the spec was checked in.
- A new, empty folder, **not** inside either workshop repository

## 1. Set up (5 minutes)

Make the folder, and put the spec and a ledger in it. If you have `curl` (macOS, Linux and
Windows 10 or later all do):

```bash
mkdir peakpeek && cd peakpeek
curl -sLO https://raw.githubusercontent.com/seandavi/2026-penn-epigen-agentic-workshop/main/examples/peakpeek/SPEC.md
curl -sL https://raw.githubusercontent.com/seandavi/2026-penn-epigen-agentic-workshop/main/exercises/LEDGER-template.md -o LEDGER.md
```

No `curl`? Open [`SPEC.md`](../examples/peakpeek/SPEC.md) and the
[ledger template](LEDGER-template.md) in the browser and save them into the folder.

## 2. Read the decisions (10 minutes)

SPEC.md §6 lists eleven decisions, each with a suggested default. **Read them before the
agent does.** Change any you disagree with, in SPEC.md itself. Two matter most, because
they change numbers without changing how the page looks:

- **Q2**: is a CSV 0- or 1-based? The Vahedi file doesn't say.
- **Q4**: what does "coverage" mean when peaks overlap each other?

Then pick two rows of §7's answer table and **check them by hand** against the fixture
just above it. It takes five minutes, and it's the one check in the project that doesn't
depend on the agent being right.

## 3. Build it, in one prompt

> Build PeakPeek, exactly as described in SPEC.md in this folder, in one go.
>
> - Take every suggested default in §6, and record them briefly in adr/.
> - Write examples/fixture.bed and examples/fixture.js from §7, using §7's table for the
>   answers. Never change those answers to make a test pass: if the code disagrees, the
>   code is wrong or you should stop and tell me.
> - Build §8's issues 1 to 6 in order, then run the checks in issue 7 that you can. Tick
>   §8's boxes as you meet them.
> - Everything must work by double-clicking index.html and test.html: no server, no
>   packages, no build step.
> - When you're done, tell me what you checked, how, and what you couldn't check.

If you changed a decision in step 2, "every suggested default" becomes "the decisions in
§6 as I've edited them", and §7's answers may change too: work those out yourself first.

**How long?** Our test run of exactly this prompt, from an empty folder with only
SPEC.md in it, took **about 15 minutes**, and the page worked first time: the numbers we
checked all matched §2. Your agent and model may be slower. Get a coffee.

While it works, **watch whether it checks or asserts.** Does it open the page in a
browser, or say "this should work"? Does it run `test.html`, or only write it? At the end,
compare what it says it checked with what it could actually have seen.

If you have `git`: `git init && git add -A && git commit -m "First build"`. If not, copy
the folder to `snapshots/first-build/`. You'll want to get back here.

## 4. Check it (20 minutes)

Now it's your turn. Double-click `test.html`, then `index.html`. Then, ledgering each:

- **Predict first.** SPEC.md §2 lists five ENCODE files. Which will have the widest peaks?
  The narrowest? Write it in the ledger, *then* paste the URLs into the page.
- **Drop `examples/fixture.bed` into the page.** Does it give §7's answers? A mismatch is a
  bug, or a decision you now disagree with. Both are worth knowing.
- **Does `chr10` come after `chr2`?** Sorting as text puts it first, and the chart still
  looks fine.
- **Paste a Zenodo URL** (§7, test 5). A good error message is a feature. "Something went
  wrong" is a bug.
- **Load the Vahedi CSV by URL, and flip the 0-/1-based setting.** Which numbers move?
- **Put the fixture next to an ENCODE file.** Can you still see the fixture in the
  side-by-side charts? If not, what should they show? (SPEC.md §3.3 says; did the agent
  read it?)
- **Cross-check one file with a tool that isn't the page** (§7, test 6). Ask your agent for
  an `awk` or R one-liner, and check it doesn't reuse the page's own code. Explain every
  difference. Don't tune it away.

## 5. Make it yours (the rest of the afternoon)

This is where the time goes. Change the page, **one idea at a time**, and after each:
`test.html` still passes, the fixture still gives §7's answers, and a ledger entry says
what you asked for and how you checked it. Snapshot or commit before each idea, so a bad
one costs nothing.

Some ideas. Better: your own.

- **Your own files.** Load peak files from your own work. What does the page get wrong,
  or not say, that you'd want to know?
- **The histograms look flat.** With several files on one 0–100 % axis, broad
  distributions nearly vanish. What would you rather see?
- **R writes large round numbers as `1.5e+07`.** The spec rejects that. Should it?
  Change §6 first, then the code, and see whether the agent updates both.
- **Peaks per megabase**, using chromosome lengths from a `chrom.sizes` URL (UCSC's allows
  web pages to read it).
- **Overlap between two files**: how many peaks in A touch a peak in B.
- **A shareable link** that reloads the same URLs.

**Watch the spec.** Does the agent update SPEC.md when the behaviour changes, or does the
code quietly drift away from it? Asking for both, every time, is the habit to practise.

## Success looks like

A page that opens with a double-click, numbers you'd defend at lab meeting, at least one
change that's yours, and a ledger that says **what was checked and how**.

## Going further: build it the long way

The one-prompt build hides three things a real project can't: **writing the spec**,
**making the decisions yourself**, and **several agents building at once**. To try them:

- **Get your own spec** before reading ours. Paraphrase this rather than pasting it:

  > I want a web page I can open by double-clicking a file: no server, nothing to
  > install. I give it one or more peak files, uploaded or as URLs, and it tells me
  > what's in them: how many peaks, their widths, which chromosomes, and anything wrong
  > with the file. With several files, show them side by side. **Don't write any code.**
  > Write a specification. Before you rely on anything the page will need, **try it in a
  > real browser.** List every decision I need to make as an open question with a
  > suggested default. Include a small test file, acceptance tests, and issues that
  > could be built in parallel without touching the same files, as checklists.

  Where it differs from ours is the interesting part. Did it find that a double-clicked
  page **can't load JavaScript modules**, or read the files next to it? Did it try
  ENCODE with a headless browser, get a **403**, and conclude ENCODE blocks web pages?
  (It blocks *headless* browsers.) Every row of SPEC.md §5 was checked by running
  something; a spec written from memory gets several wrong.
- **Write each §6 decision as a short record** in `adr/`, in your own words, and the
  fixture's answers yourself, into `examples/fixture.js`, before any code exists.
- **Build issues 1–5 in parallel**, one agent per issue, in the same folder. Each issue
  owns different files, so no branches are needed. Tell each agent: *"Build issue N from
  SPEC.md §8. Edit only the files it owns. Don't edit SPEC.md: tell me which boxes you
  believe are met, and what you checked."* Then review each one yourself before you tick
  its boxes. If you use `git`, **commit named files only** while agents are working: `git
  commit -a` sweeps up every agent's half-written code. (We did exactly that building our
  copy; an agent noticed.)

SPEC.md §9 lists what the folder should hold by the end.

## Second step, optional: put it on GitHub

**Only if you have `git` and a GitHub account, and only once the page works.** Everything
so far stayed on your laptop. This step publishes it: the code, the decisions, the
ledger, and a live copy of the page at a public URL. That's outward-facing, so the
prompt makes the agent show you everything before anything leaves your machine.

> Help me publish this project on GitHub. **Before you run anything that touches
> GitHub, show me the full plan and wait for my yes.**
>
> 1. If this folder isn't a git repository yet, make it one. If there are snapshot folders,
>    fold them into the history as commits, oldest first. Add a .gitignore for data files
>    and anything else that shouldn't be published. List every file that will be
>    published, and flag anything that looks private: data, names, email addresses, keys.
> 2. Add an MIT LICENSE, and a short README section on how to open the page.
> 3. Create a repository on my account (ask me whether public or private) and push.
> 4. Turn each issue in SPEC.md §8 into a GitHub issue with the same checkboxes: file the
>    finished ones as closed, and link each one to the ledger entry that checked it.
>    Turn the ideas from step 5 I didn't get to into open issues.
> 5. Publish the page with GitHub Pages, from the main branch. Then open the live URL,
>    load one ENCODE file by URL, and tell me whether it worked.
> 6. Add a ledger entry for all of this.

What to notice:

- **Did it actually wait?** Step 3 is the point of no return for a public repository.
- **What did it want to publish?** A `data/` folder of downloaded peak files, a
  snapshot with your name in a path, a ledger entry that quotes a colleague. Read the list.
- **GitHub Pages is served over `https://`**, not `file://`. What changes? Loading your own
  files keeps working, and so do the URLs, but the page is now reachable by anyone. Is
  that what you want?
- **After this, work changes shape.** Issues and pull requests replace the checklists,
  and branches replace "edit only your files". The
  [peak-overlap exercise](stretch-spec-then-build.md) and
  [peakwhere](https://github.com/seandavi/peakwhere) show that version.

## The full-size version

[Spec first, then build: peak overlap](stretch-spec-then-build.md) is the same process
at the scale of a real project: an annotation, an overlap engine, GitHub issues and
pull requests, and parallel agents in git worktrees. It is more than an afternoon.
[peakwhere](https://github.com/seandavi/peakwhere) is that spec built end to end by
agents, with every decision, review and near-miss on the record.
