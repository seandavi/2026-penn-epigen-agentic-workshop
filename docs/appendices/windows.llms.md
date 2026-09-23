# Appendix A — Windows notes

Everything in this book works on Windows 10 (version 1809 or later) and Windows 11. Most of it works exactly as on a Mac, because you’re typing plain-English prompts and the agent deals with the operating system. This appendix collects the few places where Windows differs, so chapters can point here instead of repeating themselves.

| You want to… | On Windows | Section |
|----|----|----|
| Find your Documents folder and its full path | File Explorer; it may be inside OneDrive | [Documents](#win-documents) |
| See `.html`, `.md`, `.csv` at the end of file names | Turn on **File name extensions** | [Extensions](#win-extensions) |
| See folders like `.claude` | Turn on **Hidden items** | [Extensions](#win-extensions) |
| Type a command | PowerShell, not CMD | [PowerShell](#win-powershell) |
| Open a web page the agent made | Double-click it, or **Open with** | [Opening HTML](#win-html) |
| Use `git` ([Chapter 7: Work like a project](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/07-work-like-a-project.llms.md) only) | Git for Windows, optional; mind OneDrive | [Git](#win-git) |

Table A.1: Where Windows differs.

## A.1 Documents, and a folder’s full path

Your Documents folder is in File Explorer’s left-hand pane, under **This PC** or your name. On many institution-managed laptops, **OneDrive** has taken it over, so the real location is:

| Documents is… | Full path |
|----|----|
| Local | `C:\Users\<you>\Documents` |
| In OneDrive | `C:\Users\<you>\OneDrive\Documents` (sometimes `OneDrive - <institution>`) |

Table A.2: Where Documents usually lives on Windows.

Either is fine for this book. To see which you have, open the folder in File Explorer and click once in the address bar at the top: it switches from a breadcrumb trail to the full path, which you can copy. You can also right-click a file or folder while holding **Shift** and choose **Copy as path**.

The simplest check is the one from [Setup](../chapters/00-setup.llms.md): ask the agent “What folder are you in?” It will print the full path.

In PowerShell, this goes to your workshop folder wherever Documents is, OneDrive or not:

``` powershell
cd (Join-Path ([Environment]::GetFolderPath('MyDocuments')) agents-workshop)
```

Windows paths use backslashes (`C:\Users\...`); Macs use forward slashes. You don’t need to translate: type paths either way in a prompt and the agent will cope.

## A.2 File name extensions and hidden files

By default, File Explorer hides the end of file names, so `index.html` shows as just `index`, and `SKILL.md` as `SKILL`. This book talks about files by their full names, so **turn extensions on**:

- **Windows 11:** in File Explorer, **View → Show → File name extensions**.
- **Windows 10:** in File Explorer, the **View** tab, then tick **File name extensions**.

In the same menu, **Hidden items** shows files and folders whose names start with a dot, such as `.claude`, where Claude Code keeps skills and settings for a project ([Chapter 4: Write a skill](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/04-skills.llms.md)). Turn it on too.

> **WARNING: A file called notes.txt.txt**
>
> With extensions hidden, a file you save as `notes.txt` from Notepad can end up as `notes.txt.txt`, and a file the agent made called `AGENTS.md` looks like a file called `AGENTS`. If a file “isn’t there” when the agent says it is, turn extensions on first.

## A.3 PowerShell versus CMD

You only need a terminal if you use the `claude` command rather than the desktop app. Windows has two, and they take different commands. **Use PowerShell for every command in this book**: the installer, `cd`, `claude`, `claude mcp add` in [Chapter 5: Connect to a database (MCP)](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/05-mcp.llms.md), and `winget`. Commands shown in grey boxes for Windows are PowerShell commands.

|  | PowerShell | CMD (Command Prompt) |
|----|----|----|
| How to open | **Win + X**, then **Windows PowerShell** or **Terminal** | Start menu, “cmd” |
| The prompt looks like | `PS C:\Users\you>` | `C:\Users\you>` (no `PS`) |
| Use it for this book? | **Yes** | Only if told to |

Table A.3: Telling PowerShell from CMD.

The install command in [Setup](../chapters/00-setup.llms.md), `irm https://claude.ai/install.ps1 | iex`, is for PowerShell. If you see `'irm' is not recognized`, you’re in CMD: close it and open PowerShell. If `claude` itself is “not recognized” after installing, the install folder isn’t on your PATH yet; the fix is in [Claude Code’s terminal guide](https://code.claude.com/docs/en/terminal-guide#windows-troubleshooting). Close PowerShell and open a new window after applying it. You don’t need to run PowerShell as Administrator.

If Windows offers **Windows PowerShell (x86)**, don’t pick it: Claude Code needs the 64-bit one, without “(x86)” in the name.

> **NOTE: WSL**
>
> If you already use WSL (Linux inside Windows), you can run Claude Code there instead. You don’t need to for this book, and plugins aren’t available in WSL sessions of the desktop app, which matters for [Chapter 5: Connect to a database (MCP)](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/05-mcp.llms.md). If in doubt, use native Windows.

## A.4 Opening a web page the agent made

Several chapters end with an `.html` file: a small web page or app that runs entirely in your browser. To open one, **double-click it** in File Explorer. It opens in your default browser, usually Edge on Windows.

To choose the browser, right-click the file and pick **Open with**, then Chrome or Edge. Both are fine. The PeakPeek example in [Chapter 6: Build an app](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/06-build-an-app.llms.md) was tested in Chrome.

The address bar will show something like `file:///C:/Users/you/Documents/...`. That’s expected: the page is reading from your disk, not the internet.

## A.5 Git for Windows (optional)

**Nothing before [Chapter 7: Work like a project](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/07-work-like-a-project.llms.md) needs `git`.** That chapter uses it for version control, and offers a way round if you can’t install it.

Having Git for Windows installed also changes one thing about Claude Code: with it, the agent runs commands through **Git Bash** (the same kind of shell as on a Mac); without it, the agent uses **PowerShell**. Either works for this book, and you won’t need to learn Git Bash yourself.

To install it, either download the installer from [git-scm.com/install/windows](https://git-scm.com/install/windows) and accept the defaults on every screen, or, in PowerShell:

``` powershell
winget install --id Git.Git -e --source winget
```

Then close and reopen the desktop app or PowerShell, so it finds `git`.

Or let the agent do it:

``` default
Check whether git is installed. If not, tell me how to install Git for Windows
on this computer, and wait for me to say go before running anything.
```

On an institution-managed laptop, installing software may be blocked. That’s fine: skip it, and use the no-git route in [Chapter 7: Work like a project](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/07-work-like-a-project.llms.md).

> **WARNING: Git and OneDrive don’t mix well**
>
> OneDrive syncs files while `git` is writing them, and the two can clash, leaving a project’s history damaged. If your Documents is in OneDrive, either **pause OneDrive syncing** while you work (from the OneDrive icon in the taskbar), or keep the project in a folder outside OneDrive, such as `C:\Users\<you>\agents-workshop`, as [Chapter 7: Work like a project](https://seandavi.github.io/2026-penn-epigen-agentic-workshop/chapters/07-work-like-a-project.llms.md) suggests.

**Line endings.** Windows and Macs end lines in text files differently, and Git sometimes prints warnings about `LF` and `CRLF`. You can ignore them for everything in this book.

## A.6 If something else goes wrong

Paste the exact error into a session and ask the agent what it means. For install problems, Claude Code’s [troubleshooting guide](https://code.claude.com/docs/en/troubleshoot-install) matches error messages to fixes.
