# Prereq email — for Golnaz to send today

**Subject:** Before Thursday's AI workshop — 15 minutes of setup, please

---

Hi all,

Thursday's agentic AI workshop with Sean Davis runs **10:00–17:00 in [ROOM]**. It's
hands-on all day, on your own laptop.

**Please get set up before you arrive.** People who show up unconfigured lose the first
hour, and it's the hardest hour to get back. The good news is that only the first step is
really yours — once you have an agent installed, it can do the rest of the setup for you.

**1. Install a coding agent and sign in.**

We'll be using **Claude Code** — https://claude.com/claude-code. It's what gets
demonstrated from the front of the room, what our TAs can help you debug, and it's on the
Institute's Claude Team plan. [Add: how to get a seat, if that's needed.] The desktop app
is the easiest starting point; the command-line version is equally good if you live in a
terminal.

Already using Gemini CLI, GitHub Copilot agent mode, or Codex? Bring it — everything we
teach is tool-neutral and transfers. Your mileage will vary on the exact commands in one
exercise mid-afternoon, and we'll hand you the equivalent for your tool.

**2. Bring a laptop and a charger.**

**3. Let the agent do the rest.** Open it and paste this in:

> I'm attending a workshop on Thursday and need to get set up. Check whether git is
> installed and help me install it if not. Then clone
> https://github.com/golnazvahedi/epigenetics-agentic-workshop.git into a sensible folder,
> and read track-a/data/README.md from it and tell me in one sentence what
> differential_peaks.csv is.

It will ask permission before running commands — that's the sandbox working as designed,
and saying yes here is fine.

**You're done when** it answers with something sensible about H3K27ac ChIP-seq peaks. That
one reply proves everything: installed, signed in, able to run commands, materials
downloaded.

If it gets stuck, tell the agent what went wrong and let it troubleshoot — it's
surprisingly good at diagnosing its own setup. And if that fails, we're running a **setup
clinic during lunch**.

---

**You do not need to know how to code.** Most of the room won't. If you've ever typed a
question into ChatGPT or Claude, you have the skill that matters most. The day is built for
people starting from there.

Full details and schedule: [WORKSHOP PAGE URL]

See you Thursday,
Golnaz

---

## Notes for Sean (not part of the email)

Placeholders Golnaz needs to fill before sending:
- `[ROOM]`
- Claude Team seat instructions — **the one to chase today.** Her email says the Anthropic
  Team membership suggests most people are on Claude already, but "most" isn't "all," and
  seat provisioning is the likeliest 10:15am failure. Worth a direct question: does every
  registrant have a seat, and who grants one if not?
- `[WORKSHOP PAGE URL]` — the new `docs/index.html`, once it's live on her GitHub Pages.

**On tool choice:** kept open, with Claude Code as the supported default rather than a
requirement. The distinction that actually matters is what the lab instructions are written
in and what the TAs commit to debug — both Claude Code — not who gets turned away. Nobody
does. This also keeps faith with the Deck 2 slide arguing that SKILL.md is a cross-vendor
open standard, which would sit badly next to a single-vendor mandate.

**The one place it bites is Lab 3 (MCP).** `.mcp.json` for Claude Code, TOML for Codex,
different JSON paths for Copilot and Gemini/Antigravity. Deck 2 already has that exact
mapping — the "…or it is just a file" slide — so the lab brief can carry the table and the
tool spread becomes a teaching point instead of a support burden. Needs one added line in
the Lab 3 brief when I write it.

**Why step 3 is a single prompt rather than four instructions:** it collapses install-git,
clone, and the verification check into one action, and it makes the attendee's first
contact with an agent an experience of it being *useful* rather than a test they might
fail. It also front-loads the permission prompt, so nobody meets that for the first time in
a live exercise.
