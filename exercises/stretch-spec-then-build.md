# Stretch — Spec First, Then Build

**An afternoon, not a slot.** This one is for after 14:00, or for anyone who finished the
morning early and wants to see what agent work looks like at the scale of a real
project: a specification, recorded decisions, a GitHub repository with issues, and several
agents building different parts at once.

The project is small enough to finish and real enough to be useful: **a web page that takes
a gene annotation and some peak files and draws a bar chart of where the peaks fall** —
promoter, UTR, exon, intron, intergenic. It runs entirely in the browser. Nothing is
uploaded.

The point is not the chart. It's that **the spec is where the work actually happens**, and
the agent can't do that part for you.

**This is the big one.** For an afternoon, start with [PeakPeek](stretch-peakpeek.md): the same
process on a smaller app, with no GitHub needed. To see this spec built end to end by
agents, with every decision and review on the record, look at
[peakwhere](https://github.com/seandavi/peakwhere).

## What you'll need

- Your agent, as in the morning
- `git`, and the GitHub CLI (`gh`) signed in, if you want the issues step
- The Vahedi lab repository,
  [golnazvahedi/epigenetics-agentic-workshop](https://github.com/golnazvahedi/epigenetics-agentic-workshop),
  cloned as in the morning setup, for one of the peak files
- A browser. Node is only needed for running tests.

## 1. Read the spec

Everything starts from **[`SPEC.md`](../examples/peak-overlap/SPEC.md)**. Read it before
doing anything else. It's about ten minutes, and three sections matter most:

- **§5 Coordinates and chromosome names** — the two places this kind of tool is wrong
  most often, and wrong in ways that still produce a nice-looking chart.
- **§6 Open questions** — twelve decisions only you can make.
- **§8 Research findings** — what the libraries actually do, checked by running them.
  The first draft, written from memory, recommended two packages that don't exist.

## 2. Or write your own

The spec was written by an agent, directed by a person, over about an hour. You can
reproduce something close to it. Paraphrase this rather than pasting it — the version
in your own words will ask for what you actually care about:

> I want a browser-only web page — no server, files never leave my machine — that takes a
> gene annotation (GFF3 or GTF) and one or more peak files (BED, narrowPeak, or CSV), classifies
> each peak as promoter, UTR, exon, intron or intergenic, and draws a stacked bar chart of
> the proportions, one bar per file.
>
> **Don't write any code.** Write a specification. Research which JavaScript libraries
> exist for parsing GTF and BED, for interval overlap, and for charting — install them
> and try them rather than recalling what they do, and tell me what surprised you. Look up
> how ChIPseeker and HOMER define promoters and resolve overlapping categories, from their
> own documentation.
>
> Pay particular attention to coordinate systems and chromosome naming. List every
> decision I need to make as an open question, with the reference points and a suggested
> default. Include acceptance tests I can check by hand, and split the work into issues
> that could be built in parallel without conflicting.

Then compare what you get with `SPEC.md`. **Where they differ is the interesting part.**
Did yours catch that GENCODE's GTF has no 5′/3′ UTR features, but its GFF3 does? That the
obvious GFF3 library needs 5.6 GB on GENCODE's file? That the Vahedi peaks say `1` where
GENCODE says `chr1`? Did it actually run the libraries, or describe them from
memory? **Before installing anything it names, check the package exists**
(`npm view <name>`) and look at who publishes it.

## 3. Set up the project

A directory, a git repository, and four things in it. Work in a new folder, not inside
either workshop repository:

```bash
mkdir peak-overlap && cd peak-overlap
git init
mkdir adr

# the spec — or your own version from step 2
curl -sLO https://raw.githubusercontent.com/seandavi/2026-penn-epigen-agentic-workshop/main/examples/peak-overlap/SPEC.md

# the same ledger you started this morning
curl -sL https://raw.githubusercontent.com/seandavi/2026-penn-epigen-agentic-workshop/main/exercises/LEDGER-template.md -o LEDGER.md
```

Then ask your agent to write the other two:

> Read SPEC.md. Write a two-paragraph README.md saying what this project is and that it
> is specified but not yet built. Then write adr/README.md explaining that each open
> question in SPEC.md §6 gets one short decision record here — context, decision,
> consequences — and add a template.md. **Don't answer any of the questions.**

Last, a memory file — `AGENTS.md`, or `CLAUDE.md` for Claude Code. After this morning you
know the rule: only what the agent can't discover. Here, that's roughly:

```markdown
# Working rules

- SPEC.md is the source of truth. If code and spec disagree, stop and ask.
- No implementation before every question in SPEC.md §6 has a record in adr/.
- All coordinates crossing a module boundary are 0-based half-open. No exceptions.
- The expected answers in test/fixtures/ were written by a human. Never edit them to
  make a test pass — report the failure.
- Add a LEDGER.md entry for each merged issue.
```

That fourth rule is the one that earns the file. An agent with a failing test and write
access to the expected answers will, sooner or later, fix the expected answers.

Commit: `git add -A && git commit -m "Spec, decision log, ledger"`.

## 4. Make the decisions

**This is the exercise.** Go through SPEC.md §6 and answer each question in its own record
in `adr/`. Use the agent to think — "what changes in the chart if I count base pairs
rather than peaks?" is a good question to ask it — but write the decision and the reason
yourself.

Q1 (how big is a promoter) and Q2 (what is being counted) matter most. The two most-used
tools disagree on both, and the reference data has peaks up to 93 kb wide, which is where
the counting rule stops being a detail.

Then **write the expected answers for the test fixture** (§7.1) before any code exists:
twelve peaks, each with the category it should get, worked out by hand. It takes fifteen
minutes and it's the only check in the project that doesn't depend on the agent being
right.

## 5. File the issues

If you want the repository on GitHub, create it — private is fine, and it's your call
whether it's ever public:

```bash
gh repo create peak-overlap --private --source . --push
```

Then:

> File one GitHub issue per row of the table in SPEC.md §9, with the dependencies and the
> relevant spec sections in each body. Label the parallel ones `parallel`. Show me the
> list before you file anything.

The last sentence is there because filing issues is outward-facing. Read the list.

## 6. Build in parallel

The four `parallel` issues touch different files, so they can be built at the same time.
Give each one its own **git worktree** — a second checkout of the same repository, on its
own branch, in its own folder — and run one agent in each:

```bash
git worktree add ../po-gtf     -b gtf-parser
git worktree add ../po-peaks   -b peak-parser
git worktree add ../po-chart   -b chart
git worktree add ../po-shell   -b page-shell
```

Open an agent in each folder with the same instruction:

> Implement GitHub issue #N. Read SPEC.md and adr/ first. Write tests alongside the code.
> When the tests pass, commit, push the branch, and open a pull request that says what you
> verified.

Some tools can do the fan-out for you — Claude Code can run sub-agents in parallel, and
several harnesses create the worktrees themselves. Doing it by hand once is worth it: you
see exactly what the automation is hiding.

Then **review and merge the pull requests yourself**, one at a time. Read the diff, not
the description.

The annotation model and the overlap engine come after, **one agent, one worktree, in
sequence**. That's where the bugs live, and splitting it up splits the understanding too.

## 7. Try it on real data

SPEC.md §2 lists the reference data, all public and all mm10: the GENCODE annotation, five
ENCODE peak files from mouse thymus (H3K4me3, H3K36me3, H3K27me3, CTCF, DNase-seq), and
the Vahedi lab's H3K27ac peaks. Fetch them into a `data/` folder that git ignores:

```bash
mkdir -p data && echo "data/" >> .gitignore && cd data

# annotation: GENCODE M25, the last release on mm10 (23 MB; start it early)
curl -sLO https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M25/gencode.vM25.basic.annotation.gff3.gz

# peaks: ENCODE adult mouse thymus, one file per experiment type
for acc in ENCFF674JZY ENCFF853BYO ENCFF478UYW ENCFF714WDP ENCFF979ULB; do
  curl -sLO "https://www.encodeproject.org/files/$acc/@@download/$acc.bed.gz"
done
cd ..
```

The accession numbers are the file names, so keep the table in SPEC.md handy for which
is which.

The Vahedi peaks live in the Vahedi lab's repository, not this one. Copy them in from your
clone, or fetch the file directly if you don't have one:

```bash
# from your clone (adjust the path to wherever you cloned it)
cp ../epigenetics-agentic-workshop/track-a/data/differential_peaks.csv data/

# or directly
curl -sL https://raw.githubusercontent.com/golnazvahedi/epigenetics-agentic-workshop/main/track-a/data/differential_peaks.csv -o data/differential_peaks.csv
```

**Before you load them, predict.** Which bar should be mostly promoter? Which should have
almost nothing in intergenic space? Write it in the ledger first (SPEC.md §7, test 8).
If the chart disagrees with textbook biology, suspect the code before the biology. Then
look at the CTCF bar, and at that file's ENCODE page, and decide whether you trust it.

## 8. Check it

Work through the acceptance tests in SPEC.md §7, and ledger each one. The ones that
catch real bugs:

- **Does anything land outside Intergenic?** If every peak is intergenic, chromosome names
  weren't reconciled. The chart will still look like a result.
- **The off-by-one test** — a 1 bp peak on the base just before an exon. Half-open
  against closed, and the interval library uses closed.
- **Your hand-written fixture.** Every mismatch is either a bug or an ADR you now
  disagree with. Both are worth knowing.

The cross-check (§7.6) is the best test of the lot: same settings, same data, two
independent tools. ChIPseeker works if you have R; otherwise `brew install bedtools` (or
`conda install -c bioconda bedtools`) and ask your agent for the bedtools version
— then check that it really is independent, and doesn't just reuse your app's logic.
Explain every difference. Don't tune it away.

## Success looks like

A working page, a chart you'd defend at lab meeting, and a repository where someone else
could see **what was decided, by whom, and how it was checked** — `adr/` for the first,
the pull requests for the second, `LEDGER.md` for the third.

If you run out of time after step 4, you still have the most valuable part: a spec with
every decision made, ready for any agent to build.
