# Stretch — PeakPeek: a page built in one prompt

**An afternoon, not a slot.** This one is for after 14:00, or for anyone who finished the
morning early.

**PeakPeek is a page that tells you what's in a peak file.** Drop in a BED or narrowPeak
file, or paste a URL, and it shows you how many peaks there are, how wide they are, which
chromosomes they're on, and what's wrong with the file. Give it several files and it
lines them up side by side.

You hand your agent a finished spec and get the whole page back **in one prompt**. Then
the afternoon is yours: try it, see what works and what doesn't, and change it into
something you'd use. **Nothing here can break anything.** It's a folder on your laptop
and a page you open by double-clicking.

## What you'll need

- Your agent, as in the morning. The desktop app is fine.
- Chrome. The spec was checked in Chrome; other browsers will mostly work.

## 1. Make a folder, start a new session (5 minutes)

1. Make a folder called `peakpeek` in **Documents**, in Finder or File Explorer. Not
   inside either workshop folder.
2. Start a **new** agent session on that folder. (A session left open from the morning
   is still in the old folder.)
3. Paste:

   > Download https://raw.githubusercontent.com/seandavi/2026-penn-epigen-agentic-workshop/main/examples/peakpeek/SPEC.md
   > and https://raw.githubusercontent.com/seandavi/2026-penn-epigen-agentic-workshop/main/exercises/LEDGER-template.md
   > (save it as LEDGER.md) into this folder. Then tell me what folder you're in and
   > what's in it.

The answer should end in `peakpeek` and list `SPEC.md` and `LEDGER.md`. If it doesn't,
stop and sort that out first.

## 2. Build it, in one prompt (about 15–30 minutes)

`SPEC.md` is long because the thinking is already done: what the page shows, every trap
we hit in a real browser, a small test file with its answers worked out, and the build
split into steps. **That's why one prompt can work here**, and why it won't for a project
nobody has specified yet.

The spec lists some decisions (§6), each with a suggested default. **First time through,
take them all.** Save any disagreements for step 4.

> Build PeakPeek, exactly as described in SPEC.md in this folder.
>
> - Take every suggested default in §6, and list them in adr/defaults.md.
> - Write examples/fixture.bed and examples/fixture.js from §7, using §7's table for the
>   answers. Never change those answers to make a test pass: if the code disagrees, the
>   code is wrong, or stop and tell me.
> - Build §8's issues 1 to 6 in order, ticking the boxes as you meet them.
> - Everything must work by double-clicking index.html and test.html: no server, no
>   packages, no build step.
> - When you're done, tell me what you checked, how, and what you couldn't check.

Our test run of this prompt took **about 15 minutes** with Claude Opus 5.5, from a folder
holding only SPEC.md. The page worked first time. Yours may take longer. Expect the agent
to ask permission often: letting it edit files inside `peakpeek` is fine; read anything
that reaches outside it.

**If it goes wrong:**

- **The agent stopped halfway:** say "continue". The ticked boxes in SPEC.md §8 show how
  far it got.
- **A blank page:** open Chrome's console (⌥⌘J on a Mac, Ctrl+Shift+J on Windows), and
  paste the red text to the agent.
- **Red tests in `test.html`:** ask "is the code wrong, or the expected answer?" The
  answers in §7 were worked out by hand; the code is the thing to fix.

**You're done when** `test.html` shows every test passing, and `index.html` shows a place
to drop files.

Then ask the agent: *"Save a snapshot of this folder called first-build."* You'll want to
get back here.

## 3. Try it: what works, what doesn't (20 minutes)

Open `test.html` and `index.html` in Chrome: right-click, then **Open With → Chrome**.
Then try things:

- Drop in **`examples/fixture.bed`**, the small test file. (Windows may hide the ending:
  it's the one that isn't a script.)
- Paste an ENCODE URL from SPEC.md §2 into the URL box. Then paste several.
- Paste a URL whose server doesn't let web pages read it, and see what the page says:
  `https://zenodo.org/records/7879374/files/README.md?download=1`
- Paste the Vahedi CSV (the last row of SPEC.md §2), and flip the 0-/1-based setting.
- Try anything else you're curious about.

Then write a ledger entry with two lists: **what worked** and **what didn't**. "What
didn't" includes "worked, but I don't like it". That list is step 4's to-do list.

## 4. Make it yours (the rest of the afternoon)

Hand the agent one item from "what didn't", or one of these, **one at a time**. After
each: `test.html` still passes, and a ledger entry says what you asked for and how you
checked it. Ask for a new snapshot when you're happy, so a bad idea costs nothing.

- **Your own peak files.** Dropping them into the page keeps them on your laptop; *showing
  them to the agent* sends them to it, so the morning's rule about private data applies.
- **The side-by-side histograms look flat** for files with broad peaks. What would you
  rather see?
- **R writes 15,000,000 as `1.5e+07`**, and the page rejects it. Should it?
- **A check that doesn't trust the page:** ask for a few lines of R you can run in RStudio
  that read one ENCODE file and print its peak count and median width, without looking at
  PeakPeek's code. Do they agree?
- **Peaks per megabase**, from a `chrom.sizes` file.
- **Overlap between two files**: how many peaks in A touch a peak in B.

When a change alters what the page does, ask the agent to **update SPEC.md too**, so the
spec keeps describing the page.

**First day with an agent? This is a good place to stop.** You built a working tool, and
changed it.

## Where next

- [**PeakPeek, finished**](https://github.com/seandavi/peakpeek) ([live](https://seandavi.github.io/peakpeek/)):
  the same spec built with several agents in parallel, every step reviewed and on the
  record. Its [issues](https://github.com/seandavi/peakpeek/issues) include how to run a
  project like this on GitHub.
- [**Spec first, then build: peak overlap**](stretch-spec-then-build.md): writing the spec
  yourself, at the scale of a real project. More than an afternoon.
