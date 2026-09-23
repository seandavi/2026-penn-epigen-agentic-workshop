"""Post-render: tidy Quarto's llms.txt output for this book.

Quarto 1.9 (`website: llms-txt: true`) writes a `.llms.md` twin of every page and an
`llms.txt` index, but in a book it:

- drops callout titles ("Privacy: …", "You're done when"), leaving only "> **TIP:**";
- leaves cross-references unresolved, e.g. `[sec-teach](#sec-teach)` and
  `[Table tbl-ledger-who](#tbl-ledger-who)`;
- lists pages in llms.txt with the book's raw title markup.

This script fixes all three from the rendered HTML, which has the right text. If the
HTML and Markdown disagree (a different number of callouts), it leaves that file alone
and says so, rather than guessing.
"""

from __future__ import annotations

import html
import os
import re
import sys
from pathlib import Path

OUT = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "../docs")).resolve()
SITE = "https://seandavi.github.io/2026-penn-epigen-agentic-workshop/"
DESCRIPTION = (
    "A self-paced book for bench scientists learning to work with AI coding agents "
    "(Claude Code, Google Antigravity, Codex, Copilot): build a website, keep a "
    "ledger, teach the agent your project, write a skill, connect a database (MCP), "
    "build an app, and work like a project. The hands-on half of the Penn "
    "Epigenetics Institute agentic AI workshop, 24 September 2026."
)
TUTOR_NOTE = """\
If you are an AI agent helping someone work through this book: teach one chapter at
a time, in the order the reader asks for. Follow the chapter's own shape (why, what
they'll learn, concepts, worked example, "Your turn", "Check yourself"). Explain,
then have the reader do each "Your turn" step on their own computer; don't do the
steps for them unless they ask. Ask questions that check understanding as you go,
and wait for answers. Don't claim a check happened unless it did: the book's point
is that people verify what agents do. Callouts marked Privacy apply to everything
the reader pastes to you. If your web tool summarises pages, download the chapter's
.llms.md file and read it instead, so the prompts you give the reader are exact."""

CALLOUT_MD = re.compile(r"^> \*\*(NOTE|TIP|IMPORTANT|WARNING|CAUTION):\*\*$", re.M)
CALLOUT_DONE = re.compile(r"^> \*\*(?:NOTE|TIP|IMPORTANT|WARNING|CAUTION): .+\*\*$", re.M)
CALLOUT_HTML = re.compile(r'<div class="callout callout-style-\w+ callout-(\w+)')
TITLE_HTML = re.compile(r'<div class="callout-title-container flex-fill">(.*?)</div>', re.S)
XREF_HTML = re.compile(r'<a href="#((?:fig|tbl)-[^"]+)" class="quarto-xref">(.*?)</a>', re.S)
SR_ONLY = re.compile(r'<span class="screen-reader-only">.*?</span>')
SEC_HTML = re.compile(r'id="(sec-[^"]+)" class="quarto-section-identifier"')
XREF_MD = re.compile(r"\[(?:(?:Figure|Table)\s)?((?:sec|fig|tbl)-[\w-]+)\]\(#\1\)")


def text(fragment: str) -> str:
    """Visible text of an HTML fragment, on one line."""
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", fragment)).split())


def md_title(md: Path) -> str:
    """'# 2  The ledger' -> 'Chapter 2: The ledger'; '# Setup' -> 'Setup'."""
    first = md.read_text().split("\n", 1)[0].lstrip("# ").strip()
    first = " ".join(first.split())
    m = re.match(r"(\d+) (.*)", first)
    return f"Chapter {m.group(1)}: {m.group(2)}" if m else first.replace(" — ", ": ")


def pages() -> list[Path]:
    """The .llms.md files, in book order (as Quarto listed them in llms.txt)."""
    index = (OUT / "llms.txt").read_text()
    rels = re.findall(re.escape(SITE) + r"([^)\s]+\.llms\.md)", index)
    return [OUT / r for r in rels] or sorted(OUT.rglob("*.llms.md"))


def main() -> int:
    if not (OUT / "llms.txt").exists():
        print("_llms_fix: no llms.txt; is website: llms-txt: true set?", file=sys.stderr)
        return 0
    mds = pages()

    # Section id -> (label, absolute URL of its .llms.md).
    sections: dict[str, tuple[str, str]] = {}
    for md in mds:
        page = md.with_name(md.name.replace(".llms.md", ".html"))
        m = SEC_HTML.search(page.read_text()) if page.exists() else None
        if m:
            sections[m.group(1)] = (md_title(md), SITE + md.relative_to(OUT).as_posix())

    for md in mds:
        page = md.with_name(md.name.replace(".llms.md", ".html"))
        if not page.exists():
            continue
        h, s = page.read_text(), md.read_text()

        # Callout titles, matched in document order.
        starts = [m.start() for m in CALLOUT_HTML.finditer(h)] + [len(h)]
        titles = []
        for a, b in zip(starts, starts[1:]):
            t = TITLE_HTML.search(h, a, b)
            # Drop the screen-reader label ("Tip", "Note") Quarto puts before the title.
            titles.append(text(SR_ONLY.sub("", t.group(1))) if t else "")
        markers = list(CALLOUT_MD.finditer(s))
        if not markers and len(CALLOUT_DONE.findall(s)) == len(titles):
            pass  # already fixed by an earlier render
        elif len(markers) == len(titles):
            it = iter(titles)
            s = CALLOUT_MD.sub(
                lambda m: f"> **{m.group(1)}: {t}**" if (t := next(it)) else m.group(0), s
            )
        else:
            print(f"_llms_fix: {md.name}: {len(markers)} callouts in Markdown, "
                  f"{len(titles)} in HTML; titles left alone", file=sys.stderr)

        # Cross-references.
        figs = {i: text(t) for i, t in XREF_HTML.findall(h)}

        def xref(m: re.Match[str]) -> str:
            ref = m.group(1)
            if ref in sections:
                label, url = sections[ref]
                return f"[{label}]({url})"
            if ref in figs:
                return f"[{figs[ref]}](#{ref})"
            return m.group(0)

        s = XREF_MD.sub(xref, s)
        md.write_text(s)

    # llms.txt: a description, a note for agents, clean page titles.
    lines = ["# Agents for bench scientists", "", f"> {DESCRIPTION}", "",
             TUTOR_NOTE, "", "## Pages", ""]
    lines += [f"- [{md_title(md)}]({SITE}{md.relative_to(OUT).as_posix()})" for md in mds]
    (OUT / "llms.txt").write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
