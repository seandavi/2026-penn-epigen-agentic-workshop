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

---

## Entry 10 — A second, smaller stretch exercise: PeakPeek

**Asked** — *SD*: the peak-overlap app is too big for an afternoon, and some attendees
won't have `git` or GitHub. Write a smaller exercise, a peak-file summariser taking
uploads or URLs, with the prompt to get the spec, the spec itself, a social-coding
checklist and the likely problems. Keep development local.

**Agent did** — Wrote `examples/peakpeek/SPEC.md` and `exercises/stretch-peakpeek.md`. The
design is one folder with `index.html` opened by double-clicking. It uses classic
scripts, no packages or build step, and a `test.html` page instead of a test runner.
Issues are checklists in the spec itself (§8): agents tick boxes, and only a person signs
an issue off. Parallel agents share one folder on disjoint files, and
history is `git` if available, otherwise folder snapshots. Indexed both from the READMEs,
and pointed the peak-overlap exercise at PeakPeek and peakwhere. *SD* chose the name
PeakPeek, and chose checklists in the spec over a separate issues file.

**Checked how** — *Agent*, all in Chrome 152 driven by `playwright-core`, because `curl`
answers a different question:

- From a double-clicked page, fetched and gunzipped ENCODE's H3K4me3 file (25,099 lines)
  and the Vahedi CSV (49,782 lines). Zenodo and `example.com` failed on CORS.
- A module import from `file://` is blocked; a classic script loads.
- Two gzip members concatenated, as `bgzip` writes them: Chrome delivers the first
  member's text, then throws "Junk found after end of compressed data". Through
  `Response.text()`, the same error surfaces as "Failed to fetch".
- The reference table in §2 was computed with `awk`, Python and `bedtools merge`. The
  fixture's answers were recomputed by a separate script from the fixture text in the
  spec.

*SD*: not yet reviewed.

**Confidently wrong** — *Agent*: the first browser test said ENCODE blocks web pages.
`curl` showed CORS headers on every hop, and the difference turned out to be the user
agent. ENCODE returns 403, with no CORS header, to `HeadlessChrome`, and serves a normal
Chrome user agent fine. The spec would have said "ENCODE URLs don't work; upload
instead". Before that, a probe bug of the agent's own (reading a response body twice)
looked like a CORS failure on GitHub, and a local test server lost to Docker, which
already held the port. The spec's first draft also said multi-member gzip is "quietly"
truncated. The test showed Chrome throws, but only after handing over the first member,
so it's truncated only if the error is ignored.

**Keep** — When a browser test fails, find out what the browser was sent before
concluding anything about the server. The test harness is part of the experiment. And
this is exactly the trap an attendee's agent will fall into, so the exercise asks them to
watch for it.

---

## Entry 11 — PeakPeek built twice: the long way, then in one prompt

**Asked** — *SD*: build PeakPeek locally as an attendee would. Then, when the long way
felt too slow: make the exercise basically a one-shot build, leaving the afternoon for
iterating on ideas.

**Agent did** — Built it the long way in `~/Documents/git/peakpeek`: decisions in `adr/`,
five workers in parallel on issues 1–5 in one folder, then issue 6, reviewing and
committing each. Then gave one fresh agent only the workshop's SPEC.md and the prompt
now in step 3. Rewrote the exercise around that: set up, read the decisions, build in
one prompt, check, then make it yours. The long way became "Going further".

**Checked how** — *Agent*, in Chrome 152 via `file://`:
- Long way: 77 tests pass; all five §2 ENCODE files and the Vahedi CSV at both
  settings match §2 through the page; `bedtools merge` agrees on CTCF and DNase.
- One-shot: 14.5 minutes from an empty folder. 62 tests pass. The fixture and CTCF
  through its page match §2; the other files are its own claim, not re-checked.

**Confidently wrong** — *Agent*, in SPEC.md, all found by building it:
- `test.html` could never read `expected.json` from `file://`; the fixture and its
  answers moved into a script.
- "CTCF has an exact duplicate line." It doesn't: two lines share chromosome, start and
  end, with different scores. The answer of 1 was right; the definition was wrong.
  The one-shot agent found it.
- "Overlapping peaks" and the side-by-side y-axis were never defined; the two builds
  chose differently (1,763 vs 3,457 CTCF overlaps; counts vs share of each file).
- *Agent*, while building: committed with `git commit -a` as workers were writing, sweeping
  up their half-written code. A worker noticed; the commit was redone.

**Keep** — With a spec this complete, a single agent built the page in a quarter of an
hour. The building was never the slow part; writing the spec and checking the result
were. So the exercise hands over the spec, and gives attendees the checking and the
changing.

---

## Entry 12 — PeakPeek: one prompt only; the finished one published

**Asked** — *SD*: simplify to the one-shot build; push PeakPeek to GitHub; leave social
coding as an issue there. Step 3 is just "what worked, what didn't", with no prediction:
part of the goal is confidence to try things. Look at the new review file.

**Agent did**
- Published `~/Documents/git/peakpeek` as
  [seandavi/peakpeek](https://github.com/seandavi/peakpeek), MIT, on GitHub Pages. Filed
  issue #1 (social coding: issues, PRs, worktrees, CI, branch protection), and #2–#5 for
  follow-ups found while building.
- Cut the exercise to four steps: make a folder with the agent (no terminal), build in
  one prompt, try it, make it yours. Parallel building, ADR-writing and the GitHub prompt
  are gone from it; the finished repo shows them.
- From the persona review (`REVIEW-stretch-peakpeek.md`, not committed): the no-terminal
  setup, a "what folder are you in?" check, "take the defaults first time", measured
  timing, an "if it goes wrong / done when" box, "Open With → Chrome", a real Zenodo URL,
  the privacy caveat for your own files, an R cross-check for RStudio users, and permission
  to stop. In SPEC.md: the dead relative link, the "no code until" status line, the
  `window.PeakPeek ||` rule, the placeholder box, the mean's tolerance; Test 7
  (predict) and §9's social-coding checklist removed.

**Checked how** — *Agent*: the live page, in Chrome 152, loads CTCF by URL (20,220 peaks)
and its `test.html` shows 77 passed, with no console errors after adding an empty favicon.
The Zenodo URL fails on CORS in Chrome (checked earlier). **Not checked:** a fresh
one-shot build from the edited SPEC.md; the edits are small, but the 15-minute figure is
from the previous version.

**Confidently wrong** — Nothing new caught this round.

**Keep** — The review's practitioner items mostly became unnecessary once the exercise
stopped teaching process. Cutting was the fix.

---

## Entry 13 — Dry run of the one-prompt exercise

**Asked** — *Agent*: check the simplified exercise end to end before calling it done.

**Agent did** — Gave a fresh agent, in an empty folder, exactly step 1's and step 2's
prompts (downloading from this branch). Fixed the seven spec gaps it reported: §4's
`summarise` and `parsePeaks` now list the fields §2 and §3 need; "main chromosomes"
covers human as well as mouse; format names agree across §3.2 and §4; scientific
notation accepts any whole number (`1.5e+07`, as R writes it); the CORS message names
wrong addresses too; test 5 gives a Zenodo URL; `test.html`'s load order points to §4.

**Checked how** — *Agent*: the build took 13.1 minutes. Its `test.html` shows 56 passed,
0 failed in Chrome 152 (re-run by me). Its own report says every §2 number matches through
the page, with Python and `bedtools` agreeing; that part is its claim.

**Confidently wrong** — *Agent*: "accept `1e+03`, reject `1.5e2`" was self-contradictory
(1.5e2 is 150, a whole number) and would have rejected real R output. Also, applying these
fixes, one replacement swallowed the sentence after it; caught on re-reading the diff.

**Keep** — Every fresh build finds something. Two builds from the same spec is cheap
insurance before a room full of people tries it.

---

## Entry 14 — Talk first, then a book

**Asked** — *SD*: divide the day into a lecture and exercises that follow, with the
hands-on part self-directed and explanatory, "akin to the chapters in RBiocBook".
10:00–12:00 talk, 13:00–14:30 hands-on. Chapters: setup; build a website from an
artefact; the ledger (with the *AI in Medicine* examples); teach the agent your
project (README vs AGENTS.md, links); a skill (deseq2-triage worked example, then
create your own, the agent writing it under your direction); an MCP connection
(anthropics/life-sciences); build an app from a starter prompt that checks the machine
and writes a spec; work like a project (ledger, ADRs, git if available). Windows too.
Quarto book, quartobot for references, lightbox, margin notes, figures. Merge PR #6.

**Agent did**
- Merged PR #6. Wrote [ADR-0007](adr/0007-talk-first-then-a-self-paced-book.md),
  superseding ADR-0001's timetable.
- Scaffolded a Quarto book in `book/`, rendering to `docs/` (Pages unchanged), and a
  writers' brief, `book/AGENTS.md`. Wrote the preface.
- Eight parallel worker agents wrote one chapter each. Chapters 1, 3, 4, 5 and 6 ran
  their worked examples for real with Claude Code 2.1.280 (`claude -p`, temporary
  folders); chapter 6's starter prompt was run twice against a scripted attendee and
  revised between runs.
- A fresh reviewer read the whole book; the same workers applied its fixes.

**Checked how** — *Agent*: before writing, PubMed's and Open Targets' MCP servers
answered `initialize` with no account (curl); the deepsense.ai servers returned 403
(unconfirmed, not broken). Claude Code's Windows install from its setup docs. The whole
book renders with no warnings; every page opened in Chrome with no unresolved
references, and copy buttons on prompts. **Taken on trust from workers:** that their
worked-example runs happened as described (their reports give times and outputs, and
chapter 4's numbers were recounted by that worker against the Vahedi data README).
**Not checked:** anything in the desktop app itself; anything on Windows; chapter 7's
prompts.

**Confidently wrong** — *Agent*: the brief told writers to use ```` ```text ```` for
prompts, which renders with no copy button; two workers caught it. The first chapter
draft of the ledger chapter used an example that broke the chapter's own rules for
"Asked" and "Checked how"; the reviewer caught it. Chapters numbered from Setup, so
file names and chapter numbers disagreed.

**Keep** — A shared brief made eight parallel chapters read as one book; a reviewer
reading the whole thing in order found what no chapter writer could: folders that
drifted, a ledger model that changed between chapters, and a timetable that didn't fit.
