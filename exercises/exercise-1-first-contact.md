# Exercise 1 — First Contact

**About 30 minutes.** The point is not the output. The point is watching an agent work on
real material, and then refusing to take its word for anything.

## Pick your material

**Your own**, if you have something safe and small: a public dataset, a folder of PDFs, a
messy spreadsheet, a script that doesn't work.

**Or the fallback** — in the workshop repository:

```
track-a/data/differential_peaks.csv
```

A real DESeq2 table of differential H3K27ac ChIP-seq peaks from the Vahedi lab. It came
straight out of a pipeline and nothing about it was tidied up for teaching, which is
exactly why it's useful.

## Do this

**1. Open your agent in the folder and describe the goal, not the steps.**

> Explore `track-a/data/differential_peaks.csv`. Tell me what's in it, flag anything
> suspicious about the data, then make a volcano plot and a ranked table of the top 20
> peaks by adjusted p-value.

Then *watch it*. It will inspect the file, write code, run the code, hit an error, and fix
the error. Three things worth noticing while it does:

- **You described an outcome.** No copying code back and forth. That's the whole difference
  between a chatbot and an agent.
- **The loop:** plan → act → check → adjust. You can interrupt at any point.
- **It asks permission** before doing things that touch your machine. Notice what it asks
  about and what it doesn't.

**2. Now interrogate it.** This is the part people skip, and it's the part that matters.

> How do I know this plot is right? Show me your checks.

And then the question it genuinely cannot answer from this file:

> When log2FoldChange is positive, which group has more signal — and how do you know?

**3. Open your ledger.** Copy `LEDGER-template.md` to `LEDGER.md` and fill in entry 1.
Takes three minutes. Be honest in the **Confidently wrong** field.

## What it should have caught

If you used the fallback file, there is a lot here to find, and none of it was planted:

- chromosome names have **no `chr` prefix** (`12`, `X`, `Y`) — which will break the first
  thing you try to join it against
- four peaks have a p-value of **exactly 0**, so `-log10` gives infinity, and a volcano plot
  has to do *something* about that
- peak widths run from 180 bp to **93,567 bp**
- there is **no gene annotation** at all
- **nothing in the file says which direction the fold change points**

That last one is the real lesson. A confident answer to the direction question is a
fabricated answer — the information is not in the file. If your agent gave you one anyway,
you have just watched the single most important failure mode in these tools, on real data,
in the first half hour. Write it in the ledger.

## Success looks like

A plot you can explain, a list of things wrong with the data that you found *with* the
agent rather than *from* it, and a ledger entry whose **Checked how** field describes
something you actually did.

## If you finish early

Ask it to write the checks down:

> Write a few sanity checks for this file so these problems get caught automatically next
> time — then show me them failing on something.
