# Peak Overlap — specification

**Status:** draft. Section 6 lists open questions; **no code gets written until each one
has an answer recorded in `adr/`**.

## 1. What this is

A single web page that takes a gene annotation (GTF) and one or more peak files, works out
what kind of genomic region each peak falls in, and draws a bar chart of the proportions,
with one bar per peak file.

The question it answers is the one asked of every new ChIP-seq, CUT&RUN or ATAC-seq
experiment: *where are my peaks — promoters, gene bodies, or out in intergenic space — and
does that differ between conditions?*

It runs **entirely in the browser**. Files are read locally and never uploaded. There is
no server and no account, and the page can be hosted as a static site (GitHub Pages).

### Non-goals

- Not a genome browser. No tracks, no zooming, no per-peak inspection beyond a table.
- No BAM, bigWig, or signal. It only works with intervals.
- No nearest-gene assignment or functional enrichment. ChIPseeker and HOMER already do
  that well.
- No statistics beyond counting. A comparison against the genome background (§6, Q9)
  is descriptive, not a test.

## 2. Inputs

| Input | Formats | Notes |
|---|---|---|
| Annotation | GTF, plain or `.gz` | One file. Tested against GENCODE. |
| Peaks | BED3+, narrowPeak, broadPeak, plain or `.gz`; CSV/TSV with named `chr`/`start`/`end` columns | One or more files. Each file becomes one bar. |

The reference test data, which is real, public and already in the workshop materials:

| File | What it is | Size |
|---|---|---|
| `gencode.vM25.basic.annotation.gtf.gz` | GENCODE mouse M25, the last release on **GRCm38/mm10** | 19 MB gzipped; 630 MB and 1,302,168 lines unpacked |
| `track-a/data/differential_peaks.csv` in [golnazvahedi/epigenetics-agentic-workshop](https://github.com/golnazvahedi/epigenetics-agentic-workshop) | 49,781 H3K27ac union peaks with DESeq2 results, **mm10** | 6.7 MB |

Annotation URL:
`https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M25/gencode.vM25.basic.annotation.gtf.gz`

The peak CSV can be split into two "files" (up in knockout, down in knockout) to exercise
the multi-file path. How to split it is a user decision, not the tool's (§6, Q10).

## 3. Outputs

1. **A bar chart**, one bar per peak file, showing the proportion in each category,
   stacked to 100%. Counts are shown on hover.
2. **A table** with the same numbers: rows are peak files, columns are categories, and
   each cell holds both a count and a percentage.
3. **A settings summary** printed under the chart: the annotation file name, promoter
   window, counting rule, priority order and gene filter. A chart without its settings
   can't be interpreted or reproduced.
4. **Downloads**: the table as CSV, the chart as SVG and PNG, and a per-peak assignment
   file (the input peak plus its assigned category).

## 4. Categories

GTF files do not contain most of the categories people want. They have to be **derived**:

| Category | In the GENCODE GTF? | How to derive it |
|---|---|---|
| Promoter | No | A window around each transcript's TSS. The TSS is `start` on `+` strand and `end` on `−` strand. Window size is Q1. |
| 5′ UTR | **No.** GENCODE has a single `UTR` feature type | `UTR` segments upstream of the transcript's CDS, in transcript orientation. |
| 3′ UTR | **No**, same as above | `UTR` segments downstream of the CDS. |
| Exon (CDS / other) | Yes: `exon`, `CDS` | Directly. Non-coding transcripts have exons and no CDS. |
| Intron | No | Transcript span minus its exons. |
| Downstream / TTS | No | A window past each transcript's end. Optional (Q7). |
| Intergenic | No | Everything not covered by any of the above. |

Feature counts in `gencode.vM25.basic`, verified: 55,401 `gene`, 81,540 `transcript`,
527,731 `exon`, 428,717 `CDS`, 117,716 `UTR`. There are **no** `five_prime_UTR`,
`three_prime_UTR`, `intron` or `promoter` lines.

Categories overlap: an exon of one transcript can be an intron of another, and a promoter
can sit inside the intron of a neighbouring gene. Each peak or base therefore needs a
**priority order** to resolve which category wins (Q3).

## 5. Behaviour and constraints

### Coordinates

This is where these tools are wrong most often, and the error is always small enough to
look plausible.

- GTF is **1-based, closed**: `start..end` includes both ends.
- BED is **0-based, half-open**: `[start, end)`.
- Internally, everything is 0-based half-open. GTF `start` becomes `start − 1`, and `end`
  is unchanged.
- If an interval library uses closed intervals, conversion happens at exactly one
  boundary in the code, and a test covers it (see §7).

### Chromosome names

GENCODE writes `chr1` … `chrM`. The reference peak CSV writes `1` … `19`, `X`, `Y`. Without reconciliation, **every
peak lands in "Intergenic"** and the chart looks like a real, if boring, result. The tool
must:

- normalise names (`1` ↔ `chr1`, `MT` ↔ `chrM`);
- report how many peaks are on chromosomes absent from the annotation;
- **refuse to draw** if more than 5% of peaks are unmatched, and show the unmatched names.

### Input validation

Every peak must have a chromosome, an integer start ≥ 0, and an integer end > start.
Rows that fail are counted and reported. They are never silently dropped and never
silently parsed. See §8: the BED library turns a CSV line into `NaN` coordinates without
raising an error.

### Performance

- Target: the reference GTF plus the reference peaks, from file drop to chart in **under
  30 seconds** on a 2022-era laptop, without the tab becoming unresponsive.
- The GTF is streamed line by line and never held in memory as one 630 MB string. Gzip
  is decoded with the browser's built-in `DecompressionStream`.
- Parsing and classification run in a **Web Worker**, with a progress indicator.
- Only the columns and feature types needed are kept. Attributes are parsed for the
  handful of keys used (`transcript_id`, `gene_type`, `transcript_type`, `tag`).

### Privacy

Nothing leaves the machine: no uploads, no analytics, no CDN calls after page load. The
page must state this.

## 6. Open questions

**Every one needs an answer before implementation starts.** Record each answer as a short
decision record in `adr/`, including the reason. Where a default is offered, it's there so
there is something to disagree with, not because it's right.

| # | Question | Why it matters | Reference points | Suggested default |
|---|---|---|---|---|
| Q1 | **How big is a promoter?** | It is the single biggest driver of the "Promoter" bar. | ChIPseeker `annotatePeak`: `tssRegion = c(-3000, 3000)`. HOMER: TSS −1 kb to +100 bp. | User-settable; default ±1 kb, with the choice shown on the chart |
| Q2 | **What is being counted?** (a) peaks, assigning each to its highest-priority overlapping category; (b) peaks, by the category at the peak **centre** or summit; (c) **base pairs**, as the fraction of total peak bp in each category | (a) and (b) can differ a lot for wide peaks. The reference data has peaks up to 93,567 bp, so a single peak can span five categories. | HOMER classifies by peak centre. ChIPseeker assigns each peak one category by priority. | (b), with (c) available as a toggle |
| Q3 | **Priority order** when categories overlap | It changes the answer for every ambiguous base. | ChIPseeker default: Promoter > 5′UTR > 3′UTR > Exon > Intron > Downstream > Intergenic. HOMER: TSS > TTS > CDS exon > 5′UTR > 3′UTR > … | ChIPseeker order |
| Q4 | **Which transcripts count?** All in the file, `basic`-tagged only, protein-coding only, or one per gene | Every extra transcript adds promoters and removes introns. | GENCODE ships a separate `basic` file, which is already filtered. | Whatever is in the file, plus an optional protein-coding filter |
| Q5 | **Chromosome handling:** chrM, unplaced scaffolds, sex chromosomes | They affect both matching and the genome background (Q9). | | Keep all; report unmatched |
| Q6 | **What coordinate base is a CSV in?** | BED is 0-based by definition; a CSV is whatever its author meant. The reference CSV doesn't say. | | Assume 0-based, show a warning, and let the user flip it |
| Q7 | **Include a Downstream/TTS category?** If so, how far? | It takes peaks away from Intergenic. | ChIPseeker: "Downstream". HOMER: TTS −100 bp to +1 kb. | Off |
| Q8 | **Split Exon** into CDS vs non-coding exon? | Biologically meaningful, and costs one more colour. | HOMER separates CDS exons. | No |
| Q9 | **Show a genome background bar?** This is the genome's own composition under the same rules. | Without it, "30% promoter" has nothing to compare against. | | Yes. It's what makes the chart interpretable. |
| Q10 | **Multiple files:** how are they labelled and ordered, and is splitting one file by a column (e.g. `log2FoldChange > 0`) in scope? | Splitting the reference CSV is the natural demo. | | Label from filename, keep input order; splitting is a stretch goal |
| Q11 | **GTF parser:** use `@gmod/gtf`, or write about 40 lines by hand? | See §8. The library is stale and streams via Node's stream API. | | Hand-written, with tests |
| Q12 | **Wrong genome build.** mm10 peaks against an mm39 GTF will produce a chart, just a wrong one. | Nothing checks for it. | | Warn if the GTF header names a different assembly from one the user states |

## 7. Acceptance tests

Each test must exist and pass before the work is called done.

1. **Hand-built fixture.** A GTF with one `+` and one `−` strand transcript (two exons,
   UTRs, one intron each) and a BED file with about 12 peaks placed deliberately: inside
   the promoter window, straddling the window edge by 1 bp, on the exact first and last
   base of an exon, entirely in an intron, spanning exon and intron, beyond the gene,
   and on a chromosome absent from the GTF. **The expected category for every peak is
   written down by a human before any code runs.**
2. **Off-by-one test.** A peak at BED `[99, 100)` and an exon at GTF `100..200` must
   overlap. A peak at `[200, 201)` must not.
3. **Strand test.** The promoter of the `−` strand transcript sits past its `end`, not
   before its `start`.
4. **Name mismatch test.** Peaks named `1` against a GTF with `chr1` match after
   normalisation. With normalisation disabled, the tool refuses to draw.
5. **Bad row test.** A CSV fed to the BED path produces a clear error, not a chart.
6. **Cross-check.** With settings matched to ChIPseeker (±3 kb, ChIPseeker priority,
   same transcripts), the reference data should give proportions **close to**
   ChIPseeker's. Where they disagree, the difference gets explained, not tuned away. This
   test needs R and is run once, by hand, and recorded in the ledger.
7. **Performance.** The reference files, timed in a browser, on the numbers in §5.

## 8. Research findings

Checked on 2026-09-23 by installing the packages and running them, not from memory. Two
of the recollections this section replaced were wrong.

| Package | Version | Verdict |
|---|---|---|
| [`@gmod/gff`](https://github.com/GMOD/gff-js) | 2.1.0 | **GFF3 only; it does not read GTF.** Easy to get wrong, because GTF is often loosely called "GFF". |
| [`@gmod/gtf`](https://github.com/GMOD/gtf-js) | 0.0.9 | Reads GTF. Last release **2023-10**. Built on Node streams (it depends on `stream-browserify`). Its README says "for JBrowse, we generally encourage GFF3 over GTF". Usable, but a GTF line is nine tab-separated columns and a hand-written parser is small and easy to test. |
| [`@gmod/bed`](https://github.com/GMOD/bed-js) | 2.3.0 | Good BED parser, actively maintained (August 2026). narrowPeak uses `new BED({ type: 'bigNarrowPeak' })`; `'narrowPeak'` throws "Type not found". **It does not validate:** `parseLine('chr1,100,200')` returns `chromStart: NaN` with no error. Lines must also be filtered for headers and comments first. |
| [`@flatten-js/interval-tree`](https://github.com/alexbol99/flatten-interval-tree) | 2.0.3 | Straightforward 1-D interval tree. **Intervals are closed:** `[100,199]` and `[199,200]` overlap. Half-open BED intervals must be inserted as `[start, end − 1]`, or every boundary base is double-counted. |
| [`flatbush`](https://github.com/mourner/flatbush) | 4.6.2 | Static, very fast packed spatial index. It is 2-D, so a 1-D use needs `y = 0`. Worth considering if the interval tree is too slow to build. The GTF index is built once and never modified, which suits a static index. |
| [`@observablehq/plot`](https://observablehq.com/plot/) | 0.6.17 | One call renders a 100%-stacked bar chart: `Plot.barX(data, Plot.stackX({x: "n", y: "file", fill: "category", offset: "normalize"}))`. Vega-Lite 6.4.3 is the alternative if an interactive spec is wanted. |

Prior art for the definitions, from primary sources:

- **ChIPseeker** `annotatePeak` defaults, taken from `R/annotatePeak.R` on its `devel`
  branch: `tssRegion = c(-3000, 3000)`, `level = "transcript"`, and
  `genomicAnnotationPriority = c("Promoter", "5UTR", "3UTR", "Exon", "Intron",
  "Downstream", "Intergenic")`.
- **HOMER** `annotatePeaks.pl`, from its
  [annotation documentation](http://homer.ucsd.edu/homer/ngs/annotation.html), classifies
  "the region occupied by the center of the peak". Its TSS runs from −1 kb to +100 bp and
  its TTS from −100 bp to +1 kb. Priority is TSS, TTS, CDS exons, 5′ UTR exons, and so on.

The two most-used tools disagree on promoter size **and** on whether a peak is classified
by its centre or by any overlap. Q1 and Q2 are real decisions, not formalities.

## 9. Architecture and work breakdown

Plain ES modules, with no build step required. A small `package.json` exists only for the
test runner. Pages serves the repository root.

```
index.html            page shell, file inputs, settings form
src/gtf.js            GTF line parser → transcript models          (issue: GTF parser)
src/peaks.js          BED/narrowPeak/CSV → validated intervals     (issue: peak parser)
src/annotate.js       transcript models → category intervals       (issue: annotation model)
src/classify.js       intervals + peaks → counts                   (issue: overlap engine)
src/chart.js          counts → Plot chart + table + downloads      (issue: chart)
src/worker.js         runs the pipeline off the main thread        (issue: worker + progress)
test/fixtures/        the hand-built fixture from §7
test/*.test.js        node --test
```

**The interfaces are fixed first, so the issues can be built in parallel.** Each module
exports plain functions over plain objects:

```js
// gtf.js       parseGtfLines(asyncIterable<string>) → AsyncIterable<{chrom, start, end, strand, type, transcriptId, attrs}>
// peaks.js     parsePeaks(text, {format, zeroBased}) → {peaks: [{chrom, start, end, name}], rejected: [{line, reason}]}
// annotate.js  buildCategoryIntervals(features, settings) → Map<chrom, [{start, end, category}]>
// classify.js  classify(categoryIntervals, peaks, settings) → {counts: {category: n}, perPeak: [...], unmatchedChroms: [...]}
// chart.js     render(el, results[], settings) → void
```

All coordinates crossing these boundaries are 0-based half-open. That is the contract, and
every module's tests assert it.

### Issues

| Issue | Depends on | Parallel? |
|---|---|---|
| Record decisions for Q1–Q12 in `adr/` | nothing | **First, and done by a human** |
| Test fixture and expected answers (§7.1–7.3) | decisions | Human writes the expected answers; an agent may write the files |
| GTF parser | interfaces | ✅ |
| Peak parser and validation | interfaces | ✅ |
| Chart, table and downloads, using mock counts | interfaces | ✅ |
| Page shell, file inputs and settings form | interfaces | ✅ |
| Annotation model: derive promoter, UTR, intron and intergenic intervals | GTF parser, fixture | Single owner. This is where the bugs live. |
| Overlap engine and counting rule | annotation model, fixture | Single owner, same person as above |
| Worker, streaming and progress | parsers | ✅ once the parsers merge |
| ChIPseeker cross-check (§7.6) | everything | Human-run, recorded in the ledger |

The four parallel issues touch different files, so they merge cleanly. The
annotation-model and overlap-engine issues are kept serial and single-owner on purpose:
they are the part of the problem that is actually hard, and splitting them across agents
splits the understanding too.
