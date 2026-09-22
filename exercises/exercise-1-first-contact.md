# Exercise 1 — First Contact

**About 30 minutes.** The point is not the output. The point is watching an agent work on
real material — yours — and then refusing to take its word for anything.

## Pick something you actually want

Pick from this list, or bring your own. The best choice is something you've been meaning
to do and haven't. Nothing here needs you to write code.

| | Try this |
|---|---|
| **A website** | Build a personal or lab site from scratch, or refresh the one you've been ignoring. "Here's my CV and three paper PDFs — make me a site." |
| **A literature review** | "Find recent work on X, read the top sources, and write me a two-page synthesis — note where they disagree with each other." |
| **Your CV** | Hand it over. "What's missing, what's stale, what reads badly?" Then have it fold in your last two years and reformat the whole thing. |
| **Slides from a paper** | Yours or any open-access one. "Turn this into a 12-slide talk with speaker notes, for a lab-meeting audience." |
| **A messy spreadsheet** | Any sample sheet, submission manifest, or collaborator's file. "Make this tidy, and give me a list of every change you made." |
| **A data file** | Something you already have. "Tell me what's in it, flag anything suspicious, and plot it." |
| **An app or dashboard** | "Fetch ENCODE's histone ChIP-seq experiments and build me a page I can filter by cell type, assay, and lab." Public metadata, no key, no server. |
| **Find something** | "Find me candidate journals for this manuscript, with scope, turnaround, and fees." Or public datasets matching criteria you specify. |

**Nothing to hand?** Use `track-a/data/differential_peaks.csv` from the workshop repository
— a real DESeq2 table of differential H3K27ac peaks, straight out of a pipeline with
nothing tidied up.

### If you pick the app

These are public, keyless, and were confirmed responding the day before the workshop.
Hand your agent the URL and describe the page you want — it will work out the rest.

| Resource | Endpoint | Holds |
|---|---|---|
| **ENCODE** | `https://www.encodeproject.org/search/?type=Experiment&format=json` | 28,642 experiments — 3,992 of them histone ChIP-seq. Cell type, assay, lab, file lists. Add `&assay_title=Histone+ChIP-seq` to narrow |
| **4D Nucleome** | `https://data.4dnucleome.org/search/?type=ExperimentSetReplicate&format=json` | 3,392 chromatin-architecture experiment sets — Hi-C and friends |
| **GEO** | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gds&term=...&retmode=json` | everything, if you can phrase the query |

Roadmap Epigenomics is also a fine target, but its metadata has moved around — asking
your agent to *find* the current table is a decent test in itself. Watch whether it
verifies that what it found actually loads, or just asserts a URL.

## Do this

**1. Describe the goal, not the steps.**

One sentence about what you want to end up with. Resist the urge to specify *how* — that's
the habit you're here to break, and a long specified prompt turns an agent back into a
chatbot.

Then *watch it*. It will look at your files, write something, run it, hit an error, and fix
the error. Three things to notice while it does:

- **You described an outcome.** No copying code or text back and forth.
- **The loop:** plan → act → check → adjust. You can interrupt at any point.
- **It asks permission** before touching things. Notice what it asks about and what it doesn't.

**2. Iterate by talking.** Don't like it? Say so in plain English — "too long", "wrong
tone", "make the labels readable", "drop the third section". Directing by conversation is
half the value of these tools and most people underuse it.

**3. Now interrogate it.**

> How do I know this is right? Show me your checks.

And the sharper version, which is where the real failures live:

> What did you assert here that I didn't tell you and you couldn't have checked?

**4. Open your ledger.** Copy `LEDGER-template.md` to `LEDGER.md` and fill in entry one.
Three minutes. Be honest in the **Confidently wrong** field.

## What to watch for

The failure mode is never that it refuses or produces nonsense. It's that it produces
something **fluent, plausible, and wrong in one specific place** — an invented citation, a
date it couldn't have known, a fold-change direction it guessed, a confident claim about
what a file contains.

Every task on that list has a version of this:

- the literature review with a DOI that doesn't resolve
- the CV that quietly upgrades a submitted paper to published
- the data file where it assumed which group was the reference
- the journal list with a fabricated turnaround time

Find yours. That's the exercise.

## Success looks like

Something you'd actually keep, and a ledger entry whose **Checked how** field describes
something you personally did.
