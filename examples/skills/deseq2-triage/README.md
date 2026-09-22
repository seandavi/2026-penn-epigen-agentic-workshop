# `deseq2-triage`

A worked example skill: the checks a careful analyst runs on a differential-analysis
table before trusting it.

## Why this one

It encodes knowledge that is genuinely **not discoverable** from the data. An agent can
read a results table perfectly well and still have no idea which group is the reference,
because no results table says. That is what makes it a good skill rather than something
the agent works out on its own.

## The demo that makes the point

Run it against both tables in the Vahedi lab workshop repository:

| File | What the skill reports |
|---|---|
| `track-a/data/differential_genes.tsv` | Direction **verified from counts**: positive means higher in WT — consistent on 60/60 significant genes |
| `track-a/data/differential_peaks.csv` | Direction **`UNVERIFIABLE`**: no per-sample counts, reference level unstated |

The two files use **opposite conventions**, and neither states its own. Nobody spots
that by eye, and an agent asked to compare them will quietly assume they agree.

That is the whole argument for skills in one example: the trap is real, it is specific
to how this lab's pipelines export, and writing it down once protects everyone who
clones the repository afterwards.

## Using it

Copy the folder to `.claude/skills/deseq2-triage/` in a project and commit it, or to
`~/.claude/skills/` to have it everywhere. `SKILL.md` is read unmodified by Claude Code,
Codex CLI, Gemini CLI and Copilot.

## Extending it

The interesting version is the one where a lab adds *its own* traps — the quirk its
aligner introduces, the column its pipeline drops, the sample-name convention that
breaks a join. Those are worth a pod's hour far more than a generic checklist.
