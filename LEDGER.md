# Ledger — workshop preparation

This repository keeps the ledger it teaches. Same five fields as
[`exercises/LEDGER-template.md`](exercises/LEDGER-template.md), because material that
asks attendees to record their verification should be able to show its own.

Each entry names **who did what**: *SD* for Sean Davis, who sets direction and makes
the calls, and *agent* for work carried out under that direction. Verification is
attributed the same way, because who checked something is part of how much it is
worth.

Entries 1–5 were written on 2026-09-23 and backdated to 2026-09-22, the day the work
was done. They are reconstructed from the session rather than recorded as it happened,
which is itself worth noting in a ledger: the *Checked how* fields describe checks that
were genuinely performed, and nothing has been added that wasn't.

---

## Entry 1 — Workshop page and prerequisites

**Asked** — For an attendee-facing page with the schedule and setup instructions, plus
a prerequisite email the organiser could send.

**Agent did** — Wrote `docs/index.html` on the visual system of the Vahedi lab's
existing plan page. Drafted the email. Collapsed setup to one real step — install an
agent — plus a single prompt that clones the materials and reads a file back, which
tests install, sign-in, command execution and materials in one action.

**Checked how** — Served the page locally and viewed it in a browser at desktop width,
light and dark. Found and fixed two real defects: the `.flow` grid put `<b>`, `<p>` and
`<pre>` into separate cells so body text collapsed into a 44px column; and an inline
`<b>Code</b>` inherited `display:block` and broke onto its own line.

**Confidently wrong** — The first version was written without looking at it. Both
layout defects would have shipped.

**Keep** — Render and look at any page before calling it done. The HTML parsed clean
and validated; it was still visibly broken.

---

## Entry 2 — Vahedi lab datasets verified before relying on them

**Asked** — Whether the datasets underpinning Exercise 1's fallback could be trusted.

**Agent did** — Reviewed the repository's provenance and checked every quantitative
claim in its data README against the files themselves.

**Checked how** — Recomputed all twelve numeric claims directly from the CSV and TSV:
row counts, adjusted p-value thresholds, directional peak counts, p-value underflow,
peak width extremes, independent-filtering counts, duplicate gene symbols, and the
ranked top hits. All twelve matched exactly. Separately confirmed the planted-bug
script fails as documented — four bugs, each matching its hint — and that its stated
correct output matches the independently computed values.

**Confidently wrong** — Nothing caught in the data. The repository was written with an
agent in a single 81-minute session with no human review, which is why it was checked
rather than assumed; the numbers held up.

**Keep** — Three operational findings were reported back to the organiser separately:
a `pandas`/`matplotlib` dependency that turns an exercise's opening beat into an import
error, a 111 MB download that needs pre-staging, and one inaccurate sentence.

---

## Entry 3 — Deck built, deployed, and its QR codes found dead

**Asked** — For a deck for the taught session, in the existing `talks` monorepo.

**Agent did** — Read the repo's conventions and authoring skill first, then composed a
33-slide venue deck from nine shared fragments plus venue-specific slides. Added a
canvas ChIP-seq signal track to the title slide. Built, ran the doctor, deployed.

**Checked how** — `talks build` (0 failed) and `talks doctor` (10 checks, all passed).
Viewed four slides in a browser and compared vertical rhythm against an existing deck
to confirm the layout matched house style rather than being broken. After deploying,
requested every URL the deck's QR codes encode.

**Confidently wrong** — The QR codes were generated before their targets existed, so
three of the four pointed at 404s — including the one repeated on four exercise slides.
Caught only because the question "is that live somewhere?" was asked. Separately,
`gh run watch` was given a run ID resolved before the new run registered, so it watched
an already-finished run and reported success prematurely.

**Keep** — Generate a QR code after its target exists, not before. And when waiting on
CI, resolve the run by commit SHA rather than by "most recent".

---

## Entry 4 — Exercises rewritten as menus

**Asked** — To drop the prescribed-dataset framing, offer real tasks people want done,
and remove an exercise step that wouldn't work.

**Agent did** — Rewrote Exercises 1 and 2 around menus. Rebuilt Exercise 2 on the
premise that agents read projects well, so a memory file is only worth writing for what
was never discoverable — removing the with-and-without comparison. Added an
app-building option and gave Exercise 3 a menu of skill ideas.

**Checked how** — Requested every API endpoint before publishing it. ENCODE, 4D
Nucleome and GEO E-utilities all returned 200 with usable JSON; the canonical Roadmap
Epigenomics metadata path returned 404 and was therefore named without a URL. Corrected
an ENCODE count that paired a filtered figure with an unfiltered endpoint.

**Confidently wrong** — A bulk slide replacement in the deck silently deleted the
speaker notes on all three exercise slides. Caught by counting notes blocks (13 → 10),
not by reading the diff.

**Keep** — The Roadmap 404 is the reason to check endpoints rather than recall them —
this is the exact failure the workshop teaches, caught in the workshop's own material.

---

## Entry 5 — Decision records and this ledger

**Asked** — For ADRs and a ledger, with items backdated, and GitHub issues filed first
to exercise issues as trackers.

**Agent did** — Filed [#1](../../issues/1), [#2](../../issues/2) and
[#3](../../issues/3), then wrote `adr/` with a README, a template and five backdated
records, plus this ledger. Removed two `notes/` drafts now out of scope.

**Checked how** — Confirmed the ADRs sat outside the Pages-served directory, since
`docs/` is this repository's site source and Jekyll would publish them and rewrite
their `.md` links to `.html`, breaking the index.

**Confidently wrong** — First wrote them to `docs/adr/`, copying the `talks` repo
convention without noticing that `docs/` means something different here.

**Keep** — A convention borrowed from another repository carries that repository's
assumptions with it.

---

## Entry 6 — Six proposed topics, triaged into stage and appendix

**Asked** — *SD* proposed six additions to the deck: pointers to Claude Science and
that these are skills, harness-versus-model performance, benchmarks and how to read
them, higher-order workflows with skills, specifying goals for autonomous work, and
git/GitHub coordination including worktrees.

**Agent did** — Researched Claude Science against Anthropic's own announcement rather
than the secondary coverage that surfaced first. Costed the six against the schedule
and pushed back: 100 minutes of teaching against 85 of exercises in a four-hour window
leaves no slack, so six topics would have cost an exercise. Proposed a split — three on
stage, benchmarks folded into speaker notes, developer material as a non-presented
appendix.

*SD* chose the tiered option, confirmed the developer material should be appendix-only,
then asked for that section expanded as reference for afternoon questions.

*Agent* then wrote three on-stage slides (specifying goals, harness versus model,
Claude Science), demoted `A server is three decisions` into the appendix to pay for
them, and built an eight-slide appendix: four primitives, the specify/implement/review
loop, reviewing the diff, sub-agents, the relocated server slide, version control and
worktrees, and decisions an agent will obey. 33 slides to 43.

**Checked how** — *Agent*: `talks build` (0 failed) and `talks doctor` (10 checks,
all passed); confirmed 43 rendered sections and grepped the built HTML for each new
slide's heading. Claude Science figures — 60+ skills, the named databases, the
platforms and plans — were taken from Anthropic's own page, after a search summary
had already offered plausible-looking numbers from third-party write-ups.
*SD*: direction and scope calls throughout; content not yet reviewed.

**Confidently wrong** — *Agent* edited the deck while still on the
`agents-md-consolidation` branch, which would have mixed an unrelated documentation
refactor into the deck commit. Caught before committing, only because of a habit of
checking `git rev-parse --abbrev-ref HEAD` before a commit, not because anything
warned.

**Keep** — Check the branch before editing, not before committing. And when a search
summary hands over numbers, go to the primary source before putting them on a slide —
the secondary write-ups here disagreed with each other, which is the same failure the
deck spends a slide warning about.

---

## Entry 7 — Stretch exercise: a peak-overlap app, specified before built

**Asked** — *SD* wanted a full-size but quick application that would show off parallel
agents, a GitHub project and issues. *SD* proposed the subject: a browser-only tool that
plots how peaks overlap gene regions from a GTF, and asked for libraries over
hand-rolled interval code. *SD* then asked for a specification with research findings
and open questions, and an exercise with a prompt paraphrase and setup steps. Midway,
*SD* redirected: link to the spec rather than inlining it in the exercise.

Along the way *SD* asked the agent to install `pi-web-agent` for its own use. No package
by that exact name exists on npm; the nearest was `@demigodmode/pi-web-agent`, from a
publisher the agent didn't recognise. The agent asked before installing, since a web
extension runs with the agent's own permissions. *SD* redirected research to a Gemini
sub-agent instead.

**Agent did** — Suggested the libraries from recall, then checked every one on npm and
ran the key ones before writing anything down. Wrote `examples/peak-overlap/SPEC.md`,
with twelve open questions, acceptance tests and a parallel work breakdown, and
`exercises/stretch-spec-then-build.md`. Placed the exercise outside the taught session
as an afternoon stretch, consistent with ADR-0006.

**Checked how** — *Agent*: `npm view` on every package named. Installed and ran
`@flatten-js/interval-tree`, `@gmod/bed` and `@observablehq/plot`. Downloaded GENCODE
vM25 basic and counted its feature types. Pulled `differential_peaks.csv` from the
Vahedi repository and confirmed its chromosome names and width range. Read ChIPseeker's
defaults from its source and HOMER's from its documentation.
*SD*: not yet reviewed.

**Confidently wrong** — *Agent*, in conversation: named `bed-utils` and
`js-interval-tree`, **neither of which exists on npm**, and said `@gmod/gff` reads GTF,
which it doesn't. The spec was also about to say `new BED({type: 'narrowPeak'})` would
work; it throws, and the right type is `bigNarrowPeak`. Separately, the Gemini CLI that
was meant to do the web research failed on authentication, because its free tier no
longer supports that client. The research was done from primary sources instead.

**Keep** — Invented package names are a supply-chain risk, not just a mistake: anyone
can register one later. `npm view` before `npm install`, every time an agent names a
package. And the peak CSV's `1` against GENCODE's `chr1` would have put every peak in
"Intergenic" and still drawn a plausible chart.

---

## Entry 8 — Reference data for the stretch exercise: a GFF3 and five peak files

**Asked** — *SD*: supply links to a GFF3 and three to five peak files, ideally from
different types of experiment, so participants can try the app themselves. *SD* then
authorised installing bedtools for checking.

**Agent did** — Chose GENCODE M25 (the last mm10 release, to match the Vahedi peaks)
and five ENCODE files from adult male mouse thymus: H3K4me3, H3K36me3, H3K27me3, CTCF
and DNase-seq, plus H3K27ac as an optional sixth. Thymus was picked because it is mostly
T cells, which suits the TCF-1 data, and because ENCODE has all five assay types for it.
Added them to SPEC.md §2 and a download block to the exercise. Revised the spec to prefer
GFF3 and added a biology-prediction test and a bedtools cross-check route.

**Checked how** — *Agent*: downloaded every file and confirmed HTTP 200, a valid gzip,
mm10, the peak counts, and chromosome names against the annotation. Ran the exercise's
download block verbatim in a clean directory. Classified peak centres (promoter ±1 kb >
exon > intron > intergenic) two independent ways: a Python script reading the GTF, and
bedtools reading the GFF3. They agreed to within 0.1% on every file:

| File | Promoter | Exon | Intron | Intergenic |
|---|---|---|---|---|
| H3K4me3 `ENCFF674JZY` | 68.9% | 4.1% | 15.7% | 11.2% |
| H3K27ac `ENCFF974HMO` | 33.3% | 3.8% | 40.0% | 22.9% |
| H3K36me3 `ENCFF853BYO` | 3.4% | 22.5% | 71.5% | 2.6% |
| H3K27me3 `ENCFF478UYW` | 42.1% | 8.3% | 25.4% | 24.2% |
| CTCF `ENCFF714WDP` | 45.5% | 6.1% | 25.7% | 22.8% |
| DNase `ENCFF979ULB` | 36.8% | 4.5% | 32.2% | 26.5% |

These are deliberately not in the spec, so nobody tunes to them. They are here as an
instructor's reference for one set of settings only. Measured `@gmod/gff` streaming the
GENCODE GFF3: 12 s before the first feature, and a 5.6 GB peak heap.
*SD*: not yet reviewed.

**Confidently wrong** — *Agent* was about to recommend `@gmod/gff` for GFF3 input
because it is maintained and browser-compatible, both true. Measuring it showed it
buffers the whole file, because GENCODE writes no `###` sync marks. Separately, the first
ENCODE query used a wrong field name and returned **zero files without an error**. An
empty result looked like "ENCODE has no mouse peaks" until the query was checked. And the
first DNase pick was a 4-day-old hybrid mouse next to 2-month-old adults. It was caught
by reading the experiment's biosample summary, not the file listing.

**Keep** — An empty query result is not an answer; check the query before believing it.
"Maintained and browser-compatible" says nothing about how a library behaves on *your*
file. And the CTCF file's promoter fraction is high for CTCF and carries ENCODE's
*extremely low read depth* audit. Kept on purpose, and labelled, because "the code is
right but is the data?" is the next question the exercise should provoke.

---

## Entry 9 — Copilot review of PR #5: five findings, five fixes

**Asked** — *SD* requested a lite Copilot review of PR #5 and asked the agent to watch
for it.

**Agent did** — Polled the PR until the review arrived, about ten minutes later. Assessed
each of the five findings against the spec rather than accepting them wholesale. All five
held up:

1. **High.** The parser contract keyed transcripts on `transcript_id`, a GTF convention.
   Standard GFF3 uses `ID` and `Parent`. GENCODE copies `transcript_id` into its GFF3,
   so the gap would have passed every test on GENCODE and failed on any other GFF3. The
   contract now normalises from `ID`/`Parent`, and the fixture's GFF3 omits
   `transcript_id` so the test can catch it.
2. **High.** The spec recommended Plot, forbade a build step, and forbade CDNs, so a
   static page couldn't import it. Libraries are now bundled once into a checked-in
   `vendor/` directory by one `npm run vendor` script.
3. **Medium.** It never said whether unmatched peaks counted toward the 100%. They are
   now excluded from the denominator and reported per file.
4. **Medium.** The genome background needs chromosome lengths, which a GTF lacks. Lengths
   now come from GFF3 `##sequence-region` lines or an optional chrom.sizes file, and the
   bar is hidden otherwise.
5. **Low.** "The workshop repository" was ambiguous with two repositories in play. The
   exercise now names the Vahedi repository and gives copy and direct-download commands.

**Checked how** — *Agent*: bundled Plot and the interval tree with esbuild, and
confirmed the bundles have no remote imports and load and run as ES modules (394 KB and
9 KB). Confirmed that GENCODE M25's GFF3 has `##sequence-region` lines for all 22
chromosomes and its GTF has none. Confirmed that no GENCODE exon has multiple parents,
that UCSC's `mm10.chrom.sizes` returns 200, and that the direct Vahedi CSV link returns
200 with 49,782 lines.
*SD*: not yet reviewed.

**Confidently wrong** — *Agent* wrote a spec that contradicted itself (a recommended
library it had also made impossible to load) and a parser contract that only worked
because GENCODE is unusually generous with attributes. Neither was caught by the agent's
own checks, which ran the libraries in Node, where bare imports resolve. It took a second
reviewer reading the spec as a whole. Also, one verification command flooded the output
by grepping minified code.

**Keep** — A second reviewer, even a lite automated one, reads the document as a whole,
not piece by piece. Testing in Node is not testing in a browser. And a reference file
that is unusually complete, like GENCODE's GFF3, hides the bugs a less complete file
would expose. Write the fixture to the standard, not to the example.
