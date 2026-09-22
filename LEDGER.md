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
