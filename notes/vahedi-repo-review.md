# Pre-workshop review — `golnazvahedi/epigenetics-agentic-workshop`

Reviewed 2026-09-22, two days before the workshop. Read-only; nothing in that repository
was modified. Recorded here because we depend on its datasets as the fallback material for
Exercise 1.

## Provenance

| | |
|---|---|
| Repository created | **2026-09-22 16:33 UTC — the same day Golnaz emailed about it** |
| Last push | 2026-09-22 17:52 UTC |
| Commits on `main` | 5, spanning **1 h 21 min**, one continuous session |
| Contributors | `golnazvahedi` — 5 of 5 commits. No other human account appears anywhere |
| Co-authorship | All five commits carry `Co-Authored-By: Claude` (Fable 5 on three, Fable 5.1 on two) |
| Pull requests | 2, both opened and merged by Golnaz. **0 comments, 0 reviews.** PR #2 was open for 28 seconds |
| Issues | 0 |
| Pages | Enabled and built, source `main` `/docs` |

Golnaz's email says she has asked her trainees to verify each exercise. **As of this review
there is no evidence in the repository that this has begun** — no commits, branches, issues,
or PR comments from anyone but her. That is not a criticism; the repo is a few hours old and
verification would not necessarily leave a trace yet. It does mean we should not assume the
exercises have been run by a human.

The collaborator list requires push access and returned 403, so whether trainees have been
added cannot be determined from the API.

## Numeric claims — all verified, 12 of 12

Every quantitative claim in `track-a/data/README.md` was checked directly against the data
files. This matters because these numbers are exactly what a language model fabricates
plausibly, and the repository was written with one.

**`differential_peaks.csv`** — H3K27ac, TCF-1 KO vs EV

| Claim | Stated | Actual | |
|---|---|---|---|
| Rows | 49,781 | 49,781 | ✅ |
| `padj` missing | 0 | 0 | ✅ |
| `padj` < 0.05 | 15,653 | 15,653 | ✅ |
| padj<.05 & log2FC > +1 (gained) | 2,202 | 2,202 | ✅ |
| padj<.05 & log2FC < −1 (lost) | 3,056 | 3,056 | ✅ |
| `pvalue` exactly 0 | 4 | 4 | ✅ |
| Peak width min / max | 180 / 93,567 | 180 / 93,567 | ✅ |
| Chromosome names lack `chr` prefix | yes | yes (21 values: `1`…`X`,`Y`) | ✅ |

**`differential_genes.tsv`** — B-cell RNA-seq, CTCFBSKO vs WT

| Claim | Stated | Actual | |
|---|---|---|---|
| Genes | 24,596 | 24,596 | ✅ |
| Passed independent filtering | 3,614 | 3,614 | ✅ |
| `padj` NA | 20,982 | 20,982 | ✅ |
| `padj` < 0.05 | 60 | 60 | ✅ |
| Duplicated gene symbols | 16 | 16 | ✅ |
| Top hits | Jun, Plk2, Myc, Cd83, Irf4, Irs2, Ccr7, Nr4a1 | identical, in order | ✅ |
| `Jun` counts / log2FC | 3465, 4023 vs 1718, 2237; −1.13 | identical | ✅ |

The fold-change direction claim also holds: `Jun` has roughly twice the counts in the
knockout and a log2FC of −1.13, confirming positive = higher in WT for that file.

**Conclusion: the datasets and their documentation are sound.** Exercise 1 can rely on
them. Whoever wrote that README checked their numbers, or got lucky twelve times.

## `make_qc_report.py` — all four planted bugs verified

Run with dependencies present, it crashes exactly as Card 5 promises. All four bugs are
real and match the card's hints one for one:

| | Line | Bug | Card 5's hint |
|---|---|---|---|
| 1 | 27 | `peaks["fdr"]` — the column is `padj` | the crash |
| 2 | 22 | `start - end` → every width is negative | "can a peak have a *negative* width?" |
| 3 | 27 | `> padj_cutoff` → selects the non-significant peaks | "does 'significant' mean padj *above* the cutoff?" |
| 4 | 32 | `np.log10(pvalue)` — missing the minus sign | "which way should a volcano plot point?" |

The stated correct output — 49,781 peaks and 15,653 significant — matches the values
verified independently above. **Card 5 is sound.**

## Repository churn — where the risk sits

From the file-level timeline: `track-a/data/` is the *most recently rewritten* part of the
repo. The real datasets landed wholesale at 17:12 (+99,205/−2,441), replacing simulated
ones, and were touched again at 17:36. `track-b/` has been untouched since 16:47 —
**meaning all four pod briefs were written against the simulated data and never re-read
after the real data replaced it.**

I checked, and Track B survives the swap: its only references into `track-a/data/` are
`make_qc_report.py` (Pod 4) and the folder as a stand-in for "your lab's output" (Pod 1),
both of which still hold and arguably read better against real data. Worth a glance from
her trainees all the same, since nobody has looked at those files since the ground moved
under them.

## Three operational risks worth passing to Golnaz

**1. `make_qc_report.py` needs `pandas` and `matplotlib`.** Card 5 opens with "first, see it
fail yourself: `python3 make_qc_report.py differential_peaks.csv`". On a machine without
those installed — which is most fresh laptops — it fails with `ModuleNotFoundError`, not the
intended `KeyError: 'fdr'`. The teaching beat lands as a setup error instead. Either the card
should say to let the agent handle the dependencies, or setup should install them. **This is
the only real defect found.**

**2. Pod 3 requires a 111 MB download per laptop**, on conference wifi, late in the
afternoon. Worth pre-staging on a USB stick or shared drive, or having TAs pull it in the
morning. This is the single highest-variance item in her repository.

**3. Minor inaccuracy in `track-a/data/README.md`:** `counts_matrix.csv` is described as
"the raw counts from `differential_genes.tsv`, nothing else", but it also carries
`gene_symbol` and `gene_type`. That's deliberate and necessary — Card 3 asks for
protein-coding genes only, which needs `gene_type` — so the file is right and the sentence
is wrong. Harmless, one-line fix.

## What this changes for us

Nothing about the taught session. We hand off at 14:00 and the afternoon is hers to run.
The one dependency in our direction is Exercise 1's fallback file, and it has now been
verified independently.

Worth mentioning the three risks above to her, framed as things a second pair of eyes
caught rather than as a review of her work.
