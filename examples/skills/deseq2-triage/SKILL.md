---
name: deseq2-triage
description: Triages a DESeq2 or differential-analysis results table before anyone
  builds on it — chromosome naming, missing adjusted p-values, p-value underflow,
  implausible interval widths, and above all which direction the fold change points.
  Use when the user asks to check, QC, sanity-check, triage, or look over a results
  table, differential expression output, peak table, or DESeq2 file, or asks what is
  wrong with one or whether it can be trusted.
---

## What this is for

Results tables arrive without the four facts needed to read them: the genome build,
the coordinate convention, which group is the reference, and what was filtered before
export. The numbers are fine. The context is missing, and a reader who assumes it
produces confident, wrong conclusions.

Run these checks and report. Do not fix anything.

## Instructions

1. **Load the file and report its shape** — rows, columns, and which columns look like
   standard DESeq2 output (`baseMean`, `log2FoldChange`, `lfcSE`, `stat`, `pvalue`,
   `padj`).

2. **Fold-change direction — the important one.**
   - If the table carries **per-sample count columns**, determine the direction
     empirically: for the significant rows, compare the group means against the sign of
     `log2FoldChange`, and report which group a positive value means. State how many
     rows are consistent (it should be all of them; if it is not, say so loudly).
   - If the table carries **no per-sample counts**, the direction **cannot** be
     determined from this file. Report it as `UNVERIFIABLE` and say the reference level
     has to come from the analyst or the DESeq2 script. **Do not infer it from column
     order, from group names, from which group is alphabetically first, or from what is
     typical.** Do not guess.

3. **Adjusted p-values.** Count missing/`NA` values. If any are missing, say plainly
   that a naive `padj < 0.05` filter silently discards those rows, and report how many.
   If *none* are missing, say that too — it usually means the table was filtered before
   export, so it is not the full result set.

4. **Underflow.** Count rows where `pvalue` or `padj` is exactly `0`. These are
   floating-point underflow, not certainty, and `-log10` of them is infinity — which
   will break a volcano plot or silently drop points.

5. **Coordinates, if the table has them.** Report whether chromosome names carry a
   `chr` prefix, and name the convention (`chr1` = UCSC, `1` = Ensembl). Warn that
   joining across conventions matches nothing and fails silently. Report the minimum and
   maximum interval width and flag any that are implausibly large for the assay — merged
   union peaks routinely produce them.

6. **Annotation.** Note whether any gene or feature identifier is present, and if so
   whether any identifiers are duplicated.

7. **Report.** Use three sections: **Blocking** (a wrong conclusion follows if this is
   not resolved — an unverifiable direction belongs here), **Worth knowing**, and
   **Checked and fine**. Finish with the four facts you would need from the analyst to
   read this table safely.

## Constraints

- **Report only. Do not modify the file, do not write a cleaned copy, and do not filter
  anything.** The value of a triage is knowing what is wrong; a silent fix destroys it.
- **Do not state a fold-change direction you have not demonstrated from counts.** This
  is the single most common confident error on these tables.
- Do not go on to analyse or plot the data. Report and stop.
