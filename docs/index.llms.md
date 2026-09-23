# Agents for bench scientists

The hands-on half of the Penn Epigenetics Institute agentic AI workshop

Author

[Sean Davis](https://seandavi.github.io/)

Published

September 24, 2026

# Preface

This morning was about what an AI agent is: a model that can read your files, run commands and make things, rather than only answer questions about them. This book is the other half. It’s where you use one, on your own work, at your own pace.

Each chapter explains **why** before it asks you to do anything. Then it walks through an example we did ourselves, including what went wrong, and hands over to you. You don’t need to know how to code for any of it. You do need to read what the agent tells you, and to check the parts that matter, because the agent will not always be right, and it will rarely say when it isn’t.

## How the day works

| Time | What |
|----|----|
| 10:00–12:00 | The talk: from chatbot to agent, what’s under the hood, working well, skills and MCP |
| 12:00–13:00 | Lunch |
| 13:00–14:30 | This book, with Sean in the room. A short getting-started, then your own pace. |
| 14:30 onwards | The Vahedi lab’s self-directed afternoon ([their repository](https://github.com/golnazvahedi/epigenetics-agentic-workshop)) |

Table 1: The day

**Nobody is expected to finish the book by 14:30.** Most people will get through setup and chapters 1 and 2, and some further. The rest is written to be read alone, later, without anyone to ask.

## What’s in it

``` mermaid
flowchart LR
  accDescr: A flow diagram. Setup leads to Build a website, which leads to The ledger. Setup also leads to Teach the agent your project, which leads to Write a skill, Connect to a database, and Build an app. Build an app leads to Work like a project.
  S[0 Setup] --> W[1 Website] --> L[2 Ledger]
  S --> T[3 Teach your agent]
  T -.-> K[4 Skill]
  T -.-> M[5 MCP]
  T -.-> A[6 Build an app]
  L -.-> A
  A --> P[7 Work like a project]
```

Figure 1: How the chapters build on each other. Solid arrows: you need the earlier chapter’s folder. Dashed: helpful, not required.

| Chapter | You’ll make | Roughly |
|----|----|----|
| [Setup](chapters/00-setup.llms.md) | An agent running in a workshop folder | 15–20 min |
| [Chapter 1: Build a website](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/01-website.llms.md) | A one-page website, from a paper, a CV or a link | 20 min |
| [Chapter 2: The ledger](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/02-ledger.llms.md) | A record of what the agent did and how you checked it | 20 min |
| [Chapter 3: Teach the agent your project](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/03-teach-your-agent.llms.md) | An `AGENTS.md` for a folder of your own | 30 min |
| [Chapter 4: Write a skill](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/04-skills.llms.md) | A skill that checks a file you know well | 40 min |
| [Chapter 5: Connect to a database (MCP)](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/05-mcp.llms.md) | A connection from your agent to PubMed | 30 min |
| [Chapter 6: Build an app](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/06-build-an-app.llms.md) | A small app of your own, from a spec you wrote together | 60 min |
| [Chapter 7: Work like a project](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/07-work-like-a-project.llms.md) | The same app, with decisions, a ledger and a history | 45 min |

Table 2: The chapters

Chapters 1 and 2 go together. After that, pick what’s useful. If you do only one more, make it [Chapter 3: Teach the agent your project](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/03-teach-your-agent.llms.md): it’s the one that pays off every day.

## How to read it

- **Prompts to paste** are in grey boxes with a copy button. Change the parts in `<angle brackets>` to your own.
- **Your own material first.** Every activity works best on something you actually do. Each one also gives a fallback, usually public data from the Vahedi lab, for when you have nothing to hand or don’t want to use your own.
- **On Windows?** Look for the collapsed “On Windows” boxes, and [Appendix A: Windows notes](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/appendices/windows.llms.md).
- **Using something other than Claude?** Google Antigravity, Codex or Copilot all work for almost everything here. Where a step is specific to Claude Code, the chapter says so.

## Learn it with your agent

You can also have your agent teach you the book. Every page is published a second time as plain Markdown, which agents read more easily than a web page, and there’s an index of them at a standard address, `llms.txt` ([Howard 2024](#ref-url:https://llmstxt.org)/):

| For | Address |
|----|----|
| The index of every chapter | <https://seandavi.github.io/2026-penn-epigen-agentic-workshop/llms.txt> |
| One chapter | The chapter’s web address, with `.html` changed to `.llms.md` |

Table 3: The book, in the form an agent reads.

Start a session in the folder the chapter’s *Your turn* works in (chapter 2, for example, goes back to chapter 1’s `website` folder), so the exercises happen where they should. Then paste this, changing the chapter number:

``` default
I'm working through the book whose index is at
https://seandavi.github.io/2026-penn-epigen-agentic-workshop/llms.txt

Read the index. Then download chapter 2 into this folder with curl (or
Invoke-WebRequest on Windows) and read it from the file, so you have the exact text
rather than a summary.

I'd like to work on chapter 2 now. Can you teach me the material and then work
through the material and exercises with me? Challenge me with questions about my
understanding along the way.
```

The download matters. Some agents’ web tools pass a page through a smaller model that summarises it ([Chapter 1: Build a website](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/01-website.llms.md)’s worked example ran into this), and a summarised prompt isn’t the prompt the chapter tested. In a chat without file access, such as claude.ai, open the chapter’s `.llms.md` address in your browser and paste the text in instead. With file access, the agent leaves a copy of the chapter in your folder; that’s fine.

> **WARNING: Your tutor is an agent too**
>
> It will explain fluently and it will sometimes be wrong, about the book as about anything else. When it says something the chapter doesn’t, check the page. And it should have **you** do each step on your own computer; if it starts doing the exercises for you, say so. Everything in [Chapter 2: The ledger](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/02-ledger.llms.md) about checking its claims applies here.

> **IMPORTANT: What not to give an agent**
>
> Nothing identifiable about patients or participants. Nothing unpublished that you aren’t allowed to share. No passwords or keys. Your institution’s rules on what may go into an AI tool apply here as everywhere; when in doubt, use the fallback data.

## When something goes wrong

It will. Tell the agent what happened, in plain words, and paste the error message: it’s usually good at diagnosing its own setup. If it’s going in circles, start a new session and say what you want again, more precisely. That is not failure. It’s most of the skill.

## How this book was made

Written with agents, at Sean Davis’s direction, the day before the workshop. The decisions behind its shape are in the repository’s [decision records](https://github.com/seandavi/2026-penn-epigen-agentic-workshop/tree/main/adr), and what was asked, done and checked is in its [ledger](https://github.com/seandavi/2026-penn-epigen-agentic-workshop/blob/main/LEDGER.md), the same format [Chapter 2: The ledger](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/02-ledger.llms.md) teaches.

Howard, Jeremy. 2024. “The /Llms.txt File, V2.” September 3. <https://llmstxt.org/>.
