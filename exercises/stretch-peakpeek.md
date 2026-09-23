# Stretch — Spec First, Then Build: PeakPeek

**An afternoon, not a slot.** This one is for after 14:00, or for anyone who finished the
morning early and wants to see what agent work looks like at the scale of a real project:
a specification, recorded decisions, a checklist of issues, and several agents building
different parts at once.

The project is small enough to finish in an afternoon: **PeakPeek, a page that tells you what's
in a peak file.** Drop in a BED or narrowPeak file, or paste a URL, and it shows you how
many peaks there are, how wide they are, which chromosomes they're on, and what's wrong
with the file. Give it several files and it lines them up side by side.

**Everything stays on your laptop.** No GitHub account, no `git`, no Node, no server. You
open the page by double-clicking a file. If you have `git`, use it; nothing here depends
on it.

The point is not the page. It's that **the spec is where the work actually happens**, and
the agent can't do that part for you.

## What you'll need

- Your agent, as in the morning
- A browser. Chrome is what the spec was checked in.
- A new, empty folder, **not** inside either workshop repository

## 1. Get a spec

The finished spec is **[`SPEC.md`](../examples/peakpeek/SPEC.md)**. Before you read it,
try getting your own. Paraphrase this rather than pasting it: the version in your own
words will ask for what you actually care about.

> I want a web page I can open by double-clicking a file: no server, nothing to install.
> I give it one or more peak files, uploaded or as URLs, and it tells me what's in them:
> how many peaks, their widths, which chromosomes, and anything wrong with the file. With
> several files, show them side by side.
>
> **Don't write any code.** Write a specification. Before you rely on anything the page
> will need, **try it in a real browser**: does a page opened from a file load its
> scripts? Can it fetch a file from ENCODE, from GitHub, from Zenodo? Tell me what
> surprised you. Look at a few real peak files and list every way they could trip the
> page up.
>
> List every decision I need to make as an open question with a suggested default.
> Include a small test file I can work out the answers to by hand, acceptance tests, and
> issues that could be built in parallel by different agents without touching the same
> files. We're not using GitHub: write the issues into the spec as checklists.

Then compare what you got with `SPEC.md`. **Where they differ is the interesting part.**

- Did it find that a double-clicked page **can't load JavaScript modules**? The page
  loads blank, and the error is only in the console.
- Did it actually try fetching from ENCODE, or assert that it works? If it tried with a
  headless browser, it got a **403** and may have concluded ENCODE blocks web pages. It
  doesn't: it blocks *headless* browsers. A real one gets the file. Did your agent notice
  the difference, or report the 403 as a fact about ENCODE?
- Did it spot that some peak files **overlap themselves**, so "how much genome do these
  cover?" has two answers?
- Did it notice the Vahedi CSV **doesn't say whether it's 0- or 1-based**?

**Watch whether it verifies, or asserts.** Every row of SPEC.md §5 was checked by running
something. A spec written from memory would have got at least three of them wrong.

## 2. Set up the folder

Make the folder, and put the spec and a ledger in it. If you have `curl` (macOS, Linux and
Windows 10 or later all do):

```bash
mkdir peakpeek && cd peakpeek
mkdir adr examples

curl -sLO https://raw.githubusercontent.com/seandavi/2026-penn-epigen-agentic-workshop/main/examples/peakpeek/SPEC.md
curl -sL https://raw.githubusercontent.com/seandavi/2026-penn-epigen-agentic-workshop/main/exercises/LEDGER-template.md -o LEDGER.md
```

No `curl`? Open those two links in the browser and save them into the folder. Or use your
own spec from step 1.

Then ask your agent to write the rest of the scaffolding:

> Read SPEC.md. Write a two-paragraph README.md saying what this project is, how to open
> it, and that it's specified but not yet built. Write adr/README.md explaining that each
> question in SPEC.md §6 gets one short decision record here (context, decision,
> consequences) and add adr/template.md. **Don't answer any of the questions, don't
> write any code, and don't edit SPEC.md.**

Last, a memory file: `AGENTS.md`, or `CLAUDE.md` for Claude Code. Only what the agent
can't work out by reading the folder:

```markdown
# Working rules

- SPEC.md is the source of truth. If code and spec disagree, stop and ask.
- No code before every question in SPEC.md §6 has a record in adr/.
- Classic <script> tags only. The page must work when index.html is double-clicked.
- Edit only the files your issue owns (SPEC.md §8). If you need another, stop and ask.
- The answers in examples/fixture.js were written by a person. Never edit them to make a
  test pass.
- Don't edit SPEC.md, even your issue's checkboxes: other agents work in this folder at
  the same time. Report which boxes you believe are met; I tick them.
- Add a LEDGER.md entry when you finish an issue.
```

The fifth rule is the one that earns the file. An agent with a failing test and write
access to the expected answers will, sooner or later, fix the expected answers.

The spec's §9 is a checklist of what should be in the folder. Tick it as you go.

## 3. Make the decisions

**This is the exercise.** Go through SPEC.md §6 and answer each question in its own record
in `adr/`. Use the agent to think ("what does the side-by-side view look like if I *don't*
normalise chromosome names?" is a good question to ask it), but write the decision and
the reason yourself.

Q2 (0- or 1-based) and Q4 (what "coverage" means) matter most. Both change numbers without
changing how the page looks.

Then **write the fixture's answers yourself**, into `examples/fixture.js`, before any
code exists. SPEC.md §7 has the fixture and a table of answers for the suggested defaults.
If your decisions differ, your answers will too. Work them out by hand. It takes ten
minutes, and it's the only check in the project that doesn't depend on the agent being
right.

It's a script, not a JSON file, because a double-clicked page can't read the files next
to it (SPEC.md §4). Let the agent make the empty shell, then fill in the answers yourself:

> Create examples/fixture.bed from SPEC.md §7, and examples/fixture.js setting
> PeakPeek.FIXTURE to the same text and PeakPeek.EXPECTED to an object with a field for
> every answer in §7's table, all left as null. **Don't fill any in.**

If you have `git`, now's the moment: `git init && git add -A && git commit -m "Spec, decisions, fixture"`.
If not, copy the folder to `snapshots/decisions/`.

## 4. Build in parallel

Issues 1–5 own different files, so they can be built **at the same time, in the same
folder**. No worktrees needed: nobody touches anyone else's files. Open an agent session
for each (separate terminal tabs, or separate windows) and give each the same instruction
with its own number:

> Build issue N from SPEC.md §8. Read SPEC.md, adr/ and AGENTS.md first. Edit only the files
> the issue owns. Write tests in its tests/ file. When they pass in test.html, tell me
> which of the issue's boxes you believe are met, and exactly what you checked.

Some tools can do the fan-out for you: Claude Code can run sub-agents in parallel. Doing
it by hand once is worth it: you see what the automation is hiding.

The instruction "edit only the files the issue owns" is doing all the work that branches
and pull requests would do on GitHub. **Check it held**: before you accept an issue, ask
the agent which files it changed, and look at the folder's modification times yourself.

If you use `git`, **commit named files only while agents are working**: `git commit -a`
or `git add -A` sweeps up every agent's half-written code. (We did exactly that
building our copy; an agent noticed.)

Then **review each one**. Open `test.html` and see the tests pass *yourself*. Read the code
the agent wrote for the parts you care about. Only then tick its boxes in SPEC.md §8,
sign off its *Status* line with your name, and add a ledger entry for it.

Issue 6 comes after, **one agent, one session**: it wires everything into the page.

## 5. Try it on real data

SPEC.md §2 lists the reference data. **Before you load them, predict.** Which of the five
ENCODE files will have the widest peaks? The narrowest? Which will have the most
chromosomes? Write it in the ledger first.

Then load them two ways. Paste the URLs straight into the page: that's what the URL box is
for. And download one or two and drop them in, which is the path for any file whose
server doesn't allow web pages to read it.

Then load the Vahedi CSV, by URL, and flip the 0-/1-based setting. Which numbers move?

## 6. Check it

Work through the acceptance tests in SPEC.md §7, and ledger each one. The ones that catch
real bugs:

- **Does `chr10` come after `chr2`?** Sorting as text puts it first. The chart still looks
  fine.
- **The fixture.** Every mismatch with your answers in `fixture.js` is either a bug or a decision
  you now disagree with. Both are worth knowing.
- **A failing URL** (§7, test 5). A good error message is a feature. "Something went wrong"
  is a bug.
- **The cross-check** (§7, test 6) is the best test of the lot: the same file, a
  different tool. Ask your agent for an `awk` or R one-liner, then check it doesn't reuse
  the page's own code. Explain every difference. Don't tune it away.

## Success looks like

A page that opens with a double-click, numbers you'd defend at lab meeting, and a folder
where someone else could see **what was decided, by whom, and how it was checked**:
`adr/` for the first, the signed-off issues in SPEC.md §8 for the second, and
`LEDGER.md` for the third.

If you run out of time after step 3, you still have the most valuable part: a spec with
every decision made, ready for any agent to build.

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
>    signed-off ones as closed, and link each one to the ledger entry that checked it.
>    Leave the "Later, if you like" ideas as open issues.
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
