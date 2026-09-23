# Writing this book: rules for agents (and people)

The hands-on half of the Penn Epigenetics Institute agentic AI workshop, 24 Sept 2026.
Why the day is shaped this way: [ADR-0007](../adr/0007-talk-first-then-a-self-paced-book.md).
This file is not rendered.

## Who reads it

Bench scientists and bioinformaticians, many of whom have never used a coding agent
and don't write code. About 40 people in a room from 13:00 to 14:30, with Sean there;
then anyone, alone, later. **Every chapter must make sense read alone, without Sean.**
Some are on **Windows**. Most will use the **Claude desktop app** (its Code tab);
some the `claude` CLI; a few Google Antigravity (it replaced Gemini CLI), Codex or Copilot. Name Claude Code where a
step is specific to it, and say what the equivalent is elsewhere when it matters
(ADR-0004: tool-neutral, Claude Code supported).

## The shape of every chapter

Discussion drives the activity, as in RBiocBook
(`~/Documents/git/RBiocBook/control_statements.qmd` is a good model of voice).

1. **Opening prose: why.** A few paragraphs. The problem, and what goes wrong without
   this. No bullet lists here.
2. `## What you'll learn`: three to five bullets.
3. **Concepts**, with at least one figure or table.
4. `## Worked example`: a real prompt in a block, what the agent did, what we
   checked, what we found (including what went wrong). Real, not invented: if you
   show an output, you produced it, or you say it's illustrative.
5. `## Your turn`: the activity. **Your own material first, a fallback second**
   (ADR-0002). Prompts to paste go in fenced blocks (```` ```default ````; ```` ```text ```` renders without a
   copy button).
6. `## What to notice`, and `## Check yourself`: how you know it worked.
7. `## Going further`: optional, short, links.

Aim for 20–40 minutes of reading-and-doing per chapter. Length: roughly 1,500–3,000
words. Prose paragraphs, not walls of bullets.

## Style

- **British spelling.** Plain words. Short sentences. Bold for the one phrase that
  matters in a paragraph, not more.
- **Don't claim more than was verified.** If a step wasn't tested, say "check this on
  the day" rather than inventing UI text. Never invent menu names, button labels or
  output. Sources for Claude Code: <https://code.claude.com/docs/en/> (append `.md` to
  a page URL to fetch it as text, e.g. `desktop.md`, `setup.md`, `skills.md`, `mcp.md`,
  `memory.md`, `discover-plugins.md`).
- **Privacy callout** wherever someone might paste their own data: nothing identifiable,
  nothing unpublished they aren't allowed to share, no patient data.
- **Lines under 92 characters** in the source.

## Quarto features to use

- **Callouts:** `.callout-note`, `.callout-tip`, `.callout-warning`,
  `.callout-important`. Give each a `## Title`. Use a
  `::: {.callout-note collapse="true"}` titled "On Windows" for Windows differences,
  and link to the Windows appendix, `@sec-windows`.
- **Margin notes:** `::: {.column-margin}` for asides, definitions and small figures.
- **Figures:** every chapter needs at least one. Label them `#fig-<chapter>-<name>`,
  give alt text (`fig-alt=`), and a caption. Images go in `book/images/`, named
  `<chapter>-<name>.png|svg`. Lightbox is on, so screenshots can be full width.
  - **Diagrams:** Quarto's native ```` ```{mermaid} ```` blocks, with `%%| label:
    fig-…` and `%%| fig-cap:`. Keep them small (≤ 10 nodes).
  - **Screenshots of web pages:** `node /Users/davsean/Documents/git/peakpeek-tools/check.mjs
    <file-or-url> --shot /private/tmp/x.png [--width 1200] [--wait ms] [--ua normal]`
    (real Chrome), then copy into `book/images/`. Don't screenshot anything showing
    private data, email addresses or tokens.
- **Tables** for comparisons (Markdown pipe tables, with `: Caption {#tbl-…}`).
- **Cross-references:** chapter IDs are fixed; use them as `@sec-…`:

  | File | ID |
  |---|---|
  | `chapters/00-setup.qmd` | unnumbered: link it as `[Setup](…/00-setup.qmd)` |
  | `chapters/01-website.qmd` | `sec-website` |
  | `chapters/02-ledger.qmd` | `sec-ledger` |
  | `chapters/03-teach-your-agent.qmd` | `sec-teach` |
  | `chapters/04-skills.qmd` | `sec-skills` |
  | `chapters/05-mcp.qmd` | `sec-mcp` |
  | `chapters/06-build-an-app.qmd` | `sec-app` |
  | `chapters/07-work-like-a-project.qmd` | `sec-project` |
  | `appendices/windows.qmd` | `sec-windows` |

  A chapter starts `# Title {#sec-id}`, with no YAML title.

## References: quartobot

Cite with persistent identifiers in the prose: `@doi:10.…`, `@pmid:…`, `@url:https://…`,
e.g. `[@doi:10.1186/s13059-014-0550-8]`. quartobot resolves them before render into
`references.resolved.bib`. **Check every key resolves before using it:**
`quartobot resolve @doi:10.x/y --output -`. Never cite a paper you haven't confirmed
exists and says what you claim. Cite sparingly: a key paper or two per chapter, plus
the documentation you rely on.

## Links

- Files in this repository: absolute GitHub links,
  `https://github.com/seandavi/2026-penn-epigen-agentic-workshop/blob/main/<path>`.
  For something an agent should download: `https://raw.githubusercontent.com/seandavi/2026-penn-epigen-agentic-workshop/main/<path>`.
- The Vahedi lab's repository (the afternoon's material and the fallback data):
  <https://github.com/golnazvahedi/epigenetics-agentic-workshop>. Link to it; don't
  copy from it; don't make a chapter depend on their exercises (ADR-0001).
- PeakPeek, finished: <https://github.com/seandavi/peakpeek>,
  live at <https://seandavi.github.io/peakpeek/>.

## Rendering while agents share this folder

Don't render in place: several writers work at once and the pre-render step writes a
shared file. Copy and render elsewhere:

```bash
rm -rf /private/tmp/bk-<key> && mkdir -p /private/tmp/bk-<key> &&
cp -R book /private/tmp/bk-<key>/book && cd /private/tmp/bk-<key>/book && quarto render
# output: /private/tmp/bk-<key>/docs/
```

Then copy back only the files you own. Don't commit, don't run git commands that change
anything, and edit no file you don't own.
