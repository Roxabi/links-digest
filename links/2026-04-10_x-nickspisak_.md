---
title: "How to Build Your Second Brain"
source: "https://x.com/NickSpisak_/status/2040448463540830705?s=20"
date: 2026-04-10
tags: ["knowledge-management", "AI", "productivity", "second-brain", "automation"]
platform: x
author: "@NickSpisak_"
summary: "This article outlines a simple method to build a personal knowledge base using a three-folder structure, automated web scraping with agent-browser, and AI-powered organization that compounds in value"
---
@karpathy  dropped a post describing how he uses AI to build personal knowledge bases.

The idea is simple: instead of keeping notes scattered across apps, you dump everything into one folder. Then you tell your AI to organize all of it into a personal wiki - summaries, connections, articles - that gets smarter every time you use it.

No special software. No database. Just folders and text files.

In under 7 minutes you'll learn:

The exact folder structure to set up (takes 2 minutes)

How to automate web scraping into your knowledge base with one CLI tool

The one-file "schema" that makes the whole system work

How to get your AI to compile raw notes into an organized wiki

The compounding trick that makes it smarter every time you use it

The health check that catches mistakes before they pile up

Follow @NickSpisak_ for practitioner-level AI implementation and Claude Code architecture content. 

Want the skill that builds this system for you? Grab the free LLM Knowledge Base skill here: https://return-my-time.kit.com/286e11f7e6

Alright let's get started...

1. Create Three Folders (2 Minutes)

Open your terminal or file explorer. Create a project folder anywhere on your computer. Inside it, create three subfolders:

That's it. This is the same structure @karpathy  uses. The raw/ folder is your junk drawer of source material. The wiki/ folder is where the AI turns that mess into something organized. The outputs/ folder is where answers to your questions live.

No apps to install. No accounts to create. Three folders.

2. Fill Your Raw Folder (10 Minutes)

This is where most people stall. They create the folders and then stare at an empty raw/ directory wondering what to put in it.

The answer: everything. Copy-paste articles into .md or .txt files. Save screenshots or diagrams as images. Export notes from whatever app you use now. Paste in meeting notes, research papers, project docs. Dump in bookmarks you've been hoarding for months.

Don't organize it. Don't rename anything. Don't clean it up. That's the AI's job.

I keep 17 raw source files across my X content pipeline - clipped articles, competitor breakdowns, analytics reports. None of it is organized by hand.

But Karpathy didn't mention the part that actually speeds this up: automated collection.

3. Automate Source Collection With Agent Browser (Optional But Powerful)

Vercel Labs just shipped agent-browser - a free CLI tool that lets your AI agent control a real browser. 26K+ GitHub stars. Two commands to install:

That second command downloads a dedicated Chrome browser. Now your AI can scrape any webpage, extract the text, and save it directly into your raw/ folder.

Here's what that looks like in practice:

That's it. The AI opens the page, grabs the article text, and you pipe it into a file in raw/. No manual copy-paste. No browser extensions.

Agent-browser handles pages that copy-paste can't touch. JavaScript-heavy sites that load content dynamically. Pages behind logins. Research papers with interactive figures. Anything that requires scrolling, clicking "load more," or navigating through menus before the content appears.

The tool uses 82% fewer tokens than Playwright MCP, which means your AI agent can scrape 5-6x more pages within the same session. I use it to pull competitor articles, trending threads, and research docs directly into my pipeline without ever opening a browser myself.

For your knowledge base, the workflow is simple: find an article you want, tell your AI "scrape this URL and save it to raw/", and agent-browser handles the rest. Your raw/ folder fills itself.

4. Write Your Schema File (5 Minutes)

This is the part most people will skip. Don't.

Create a file in the root of your project called CLAUDE.md (or AGENTS.md or README.md - the name doesn't matter, the content does). This file tells your AI what the knowledge base is about and how to organize it.

Here's a starter template you can copy right now:

@karpathy  confirmed he keeps his schema "super simple and flat" in an AGENTS.md file. No database. No plugin. Just a text file that tells the AI the rules.

This is the equivalent of what I use CLAUDE.md for across every project. It's the AI's instruction manual for your specific knowledge base.

5. Tell Your AI to Compile the Wiki (15 Minutes)

Open Claude Code (or Cursor, or any AI coding tool that can read your files). Point it at your project folder and say:

"Read everything in raw/. Then compile a wiki in wiki/ following the rules in CLAUDE.md. Create an INDEX.md first, then create one .md file per major topic. Link related topics. Summarize every source."

Then step away. Let it work.

When it's done, you'll have a wiki/ folder full of organized articles - connections you didn't see, summaries of things you forgot you saved, and an index file that makes everything searchable in seconds.

The important thing: you don't edit the wiki by hand. That's the AI's job. You read it, you ask questions against it, and the AI keeps it updated.

6. Ask Questions and Save the Answers (Ongoing)

Once your wiki has 10+ articles, start asking questions:

"Based on everything in wiki/, what are the three biggest gaps in my understanding of [topic]?"

"Compare what source A says about [concept] vs what source B says. Where do they disagree?"

"Write me a 500-word briefing on [topic] using only what's in this knowledge base."

The AI reads across your entire wiki and gives you answers grounded in your own collected material.

Save those answers back into the knowledge base. Drop the output into outputs/ or have the AI update the relevant wiki article with the new insight. Every question makes the next answer better. That's the loop.

7. Run a Health Check (Monthly)

Tell your AI:

"Review the entire wiki/ directory. Flag any contradictions between articles. Find topics mentioned but never explained. List any claims that aren't backed by a source in raw/. Suggest 3 new articles that would fill gaps."

One of the best replies to Karpathy's post came from @HFloyd : "When outputs get filed back, errors compound too." That's real. If the AI writes something slightly wrong and you save it back, the next answer builds on that wrong thing.

The fix is simple: run periodic health checks.

8. You Don't Need Obsidian (But You Can Use It)

Half the replies to Karpathy's post were people pitching Obsidian plugins. Lex Fridman uses Obsidian + Cursor. There are already three startups building dedicated tools for this.

But here's what Karpathy actually said when someone asked about his setup: "I'm trying to keep it super simple and flat. It's just a nested directory of .md files."

A folder of text files and a schema file is the entire product.

I run my whole knowledge system from the terminal with Claude Code. You could use VS Code. You could use Obsidian. You could use Notepad. The AI doesn't care what app you open the files in. What matters is the folder structure and the schema.

Obsidian with 47 plugins is the Notion trap all over again. You spend more time configuring the tool than using the knowledge base. Flat files and a good schema will outperform a fancy tool stack 90% of the time. I've watched it happen across dozens of client setups.

Stop shopping for the perfect tool. Start building.

That's the full system. Three folders, one schema file, a browser scraper, and an AI that maintains everything.

41K people bookmarked Karpathy's post. The difference between bookmarking it and benefiting from it is one weekend of setup.

Pick your topic. Create the folders. Drop in what you already have. Let the AI do the rest.

Want to skip the manual setup? Grab the free LLM Knowledge Base skill that scaffolds the entire system in 60 seconds: https://return-my-time.kit.com/286e11f7e6