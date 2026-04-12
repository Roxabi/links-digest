---
title: "How to Build Your AI Second Brain Using Obsidian + Claude Code"
source: "https://x.com/noahvnct/status/2027435582461259997?s=46"
date: 2026-02-27
tags: ["AI second brain", "Obsidian setup", "Claude Code integration", "knowledge management", "personal productivity"]
platform: x
author: "@noahvnct"
summary: "The article explains how to connect Claude Code to Obsidian vaults to create an AI-powered second brain that maintains persistent context across sessions."
---
Introduction: Why I've Been Losing Sleep Over This

Two weeks ago, I connected Claude Code to my Obsidian vault. And since then, I've been having insomnia.

Not bad insomnia. The good kind. The kind that comes when your mind is so stimulated by what you're building that it refuses to stop working, even at 2am. Every night I lie in bed thinking about new possibilities, new workflows, new ways to use this system. I've never experienced that from a tool before.

So in this article, I'm going to show you exactly what I built and why it's the most powerful AI setup I've ever used as a creator.

But before we get to the solution, I need to explain the problem. Because most people who use AI every day are running into it — and they don't even know it.

So grab a coffee, take your time, and let's dive in.

Prefer to watch? If you want to see the full setup in action, with live demos of every workflow described in this article, the video covers everything: https://www.youtube.com/watch?v=BLdO-32I6Yc

The AI Problem No One Talks About

Every time you open Claude or ChatGPT, you start from zero.

You explain who you are. You describe what you're working on. You give context about your audience, your tone, your goals. You get a decent answer. You close the tab. And the next time you open it, you do exactly the same thing all over again.

The AI does not know you. And because of that, the output is always generic.

Most people blame the prompt. But the prompt is not the problem. Context is everything when it comes to getting good AI output. Generic context produces generic results. You can spend weeks obsessing over your prompts and still get mediocre answers if the AI has no idea who you are, what you're building, and what you've already created.

The Built-in Memory Solution Is Broken

Claude and ChatGPT both have built-in memory features. They were supposed to solve this. They don't.

The problem is structural: those systems save arbitrary snippets automatically, without your control or editorial judgment. There's no hierarchy. No organization. No way to know what the AI is or isn't remembering. It mixes your projects, remembers the wrong details, and creates noise. At its worst, you get AI that inserts references from your 2am journaling session into your next business proposal. It's not a system. It's an approximation of a system.

The Real Solution: Put the AI Inside Your Second Brain

Instead of going to the AI, you put the AI inside your system.

When Claude Code opens inside your Obsidian vault, it reads your notes, your projects, your context, your writing rules. It knows who you are from the first prompt in every session. You don't re-explain anything. And it gets smarter every time you use it.

That's the fundamental shift.

My Setup: Two Tools, One System

The setup I'm using combines two tools: Obsidian and Claude Code.

Obsidian is where my second brain lives. Claude Code is the AI agent that lives inside it. Together, they create an intelligent second brain that reads, writes, and acts on my behalf.

Why Obsidian

Obsidian is free and requires no subscription. Your files live on your computer as a local folder of plain markdown files. You own your data and nobody else does.

The markdown format is universal: any app can read it, and AI reads it natively. Unlike Notion, Evernote, or OneNote, there is no proprietary format. You're not locked into anything. Even if Obsidian disappeared tomorrow, your files would still be there, readable by any text editor on earth.

What makes Obsidian particularly powerful for this setup is the direct file access. Notion stores your data in a format that isn't cleanly accessible to external AI. With Obsidian, Claude reads your files directly, with no API calls and no workarounds. You and the AI work in the same folder simultaneously, in different interfaces, with the same context.

Why Claude Code Specifically

Claude Code is a genuine agent. It doesn't just answer questions. It reads, writes, and modifies files, executes terminal commands, and can even launch sub-agents to parallelize work across your vault.

Two things make it exceptional for this use case. First, it reads a CLAUDE.md file and a memory.md file at every startup, automatically, before anything else. Second, it has full access to your file system in whichever folder you open it in, with persistent context across every conversation.

It's also extendable via MCP (Model Context Protocol) to connect to external tools, which I'll explain later.

The Terminal: Not What You Think

To use Claude Code, you need to open it in your terminal. And I know what you're thinking. You saw "terminal" and almost closed this article. Stay with me.

The terminal is not as scary as it looks. It's just an interface that lets you run commands and navigate your computer with text instead of clicks. Every click you make on your screen is a command the terminal could run. Claude Code can do all of that, plus everything you can't reach by clicking.

The visual interfaces (Claude.ai, apps, wrappers) are limited by design. They don't give Claude full access to your file system. The terminal removes that limitation. And that's where the real power lives.

The Only Three Commands You Need

You don't need to become a developer to use the terminal. You need exactly three commands:

pwd - tells you which folder you're currently in. Run it and you'll see your current location in the file system.

ls - lists all files and subfolders in the current directory. If you opened the Finder and looked at the same folder, you'd see exactly the same thing.

cd "[folder-name]" - navigates into a folder. And cd .. - takes you back one level up.

That's it. Three commands. Everything else, Claude handles.

How to Launch Claude Code in Your Vault

There are two ways to do it.

The first: open your terminal, use cd to navigate until you're inside your Obsidian vault folder, then type claude. That's all it takes.

The second, and easier one: find your vault folder in Finder, right-click on it, go to Services, and select "New Terminal at Folder." Your terminal opens directly inside the vault. Type claude and you're in.

From that moment, Claude is inside your system. It reads your context immediately. It knows your folder architecture, your projects, your writing rules. It knows more about your setup in the first prompt than most collaborators would after a week of onboarding.

CLAUDE.md and Memory: The Context That Grows

What transforms Claude Code from a useful tool into a genuine second brain is the context system. Specifically, two files: CLAUDE.md and memory.md.

Your context lives in your files, not in AI memory. That's the key insight. With Claude Code, your context is readable, editable, and fully structured markdown that you control. Everything Claude knows about you is stored in files you can open, read, and modify at any time.

CLAUDE.md: The Brain of the Brain

Claude reads CLAUDE.md at every session startup, automatically, before anything else. This file is where you store everything Claude needs to know: who you are, your current projects, your folder architecture, your writing rules, your preferences, your guidelines.

Claude can update this file as you work together. If it does something you don't like, you tell it: "Update your CLAUDE.md so you don't make that mistake again." After five sessions, Claude knows your projects, your voice, your standards, and your preferences better than most human collaborators would.

You can even do what I call meta-optimization: ask Claude how it would restructure the CLAUDE.md file to be even more efficient, then let it update the file itself. You can also ask it what information it still needs to do its best work, and have it run through a series of questions to fill in the gaps. The context compounds the more you invest in it.

You can place CLAUDE.md files at multiple levels of your vault. I have one at the root that covers my entire system architecture, and individual CLAUDE.md files inside specific folders I use frequently. When Claude navigates into those folders, it reads the local context file automatically.

memory.md: The Session Log

The memory.md file is where Claude records key decisions, patterns, and actions after each session. It gives Claude continuity across conversations and allows it to pick up exactly where you left off.

If you have to stop in the middle of a project, you tell Claude to save everything it needs for next time into its memory. The next time you open Claude and pick up that project, it remembers your progress, your decisions, and what you were building toward.

Ask Claude to update memory.md at the end of each session. Over time you'll have a detailed log of everything you've built together, every rule you've established, every decision you've made.

The Compounding Effect

Here's what this means in practice.

Use Claude Code once and it knows your folder structure. Use it five times and it knows your projects, your current focus, and your voice. Use it twenty times and it becomes your personalized operating system. It knows more about your knowledge base than you consciously remember at any given moment.

The more you use your second brain, the smarter your AI becomes. Automatically. That's the power of this entire setup.

Real Use Cases: What I Actually Do With This

I've been running this setup for two weeks. In those two weeks, it has fundamentally changed the way I work. Here are the use cases that matter most.

Knowledge Management

My Zettelkasten system has around 491 permanent notes. Claude navigates all of them.

The tasks it handles for knowledge management would have taken me hours before. It can update tags across hundreds of files after a taxonomy change, completing in minutes what used to take an entire afternoon. It finds notes that should be linked to each other but aren't. It creates new permanent notes from literature notes: reading my highlights, synthesizing the core concept, formatting the note correctly, and linking it to existing connected notes. And it surfaces thematic connections across years of notes instantly, finding clusters of ideas I had forgotten I'd written about.

To give you a concrete example: I can open Claude Code and type "find me five permanent notes in my Galaxy about the subconscious mind." Claude searches my file system, reads the relevant files, and returns five permanent notes with sources and summaries in seconds — entirely through a natural language request. (If you want to see this live, watch the video above.)

Content Creation with Full Vault Context

Before Claude writes anything, it launches sub-agents that scan my vault. It finds related Galaxy notes, past newsletters on the topic, previous content pieces, and existing outlines. The result is that content gets built on everything I've ever thought and written, not from a blank page.

The outline for this article was built using exactly this workflow.

Here's a concrete example of what this looks like: I asked Claude to find five permanent notes about the subconscious mind, then immediately asked it to write a newsletter using those notes, following my writing style, with a classic AIDA structure. Two minutes later, Claude had produced a complete draft: proper metadata, title, subject line suggestions, preview text, key takeaways, and the full email, all formatted exactly as I format my newsletters. The prompt I wrote was barely two sentences. (If you want to see this running live from start to finish, watch the video above.)

That's the leverage of having an AI that has already read everything in your knowledge base before you even ask it to create something.

Skills: Workflows as Slash Commands

This is where the system becomes exponentially powerful.

Every workflow you build with Claude Code can become a repeatable command. Here's how it works: you run a workflow with Claude, then at the end of the session you ask it to write an SOP (Standard Operating Procedure) for the process. You save that SOP as a skill file. From that point on, you type /skill-name in the chat and the entire process runs automatically.

Every workflow becomes a permanent, callable command. The system grows in capability the more you use it.

To see how fast this works: after completing the newsletter-from-Galaxy workflow, I asked Claude to turn it into an SOP and create a skill file. Two minutes later, Claude had written a complete agent definition (identity, context, eight steps, checkpoints, good and bad output examples), created the skill file, and linked everything together. A workflow that required manual effort every time became a single command. (Watch the video above to see this built in real time.)

I do this at the end of every productive session. We work through a problem together, I'm happy with the output, and I ask Claude to create a new SOP and skill based on what we just did. Over time, my skill library grows into a personal automation system built entirely around how I actually work.

MCP: Connecting Claude to External Tools

Claude Code doesn't have to stay limited to your local vault. With MCP (Model Context Protocol), you can connect it to external tools and services.

MCP is a standard that lets Claude Code communicate with external apps and APIs in real time. Without it, Claude only sees your local vault. With it, Claude can read from and act on your other tools as part of the same workflow.

Things3: Live Task Management

I've connected Claude to Things3, my task management app. Claude has live access to all my tasks, projects, and areas.

The practical application is simple: I can ask "what are my priorities for today?" and Claude reads Things3 directly to give me a real, personalized answer based on what's actually scheduled, without leaving the terminal.

Tana: Capture and Voice Notes

I use Tana as my capture system. It has great mobile widgets for instant capture via text or voice note, with auto-transcription. I assign tags to sort different types of content automatically: YouTube ideas, newsletter topics, tweet concepts.

Claude has access to my entire Tana capture system via MCP.

The most powerful thing I've built on top of this is a skill called /voicenotetoletter. When I invoke it, Claude fetches the latest voice note from my newsletter supertag in Tana, translates it near-literally from French, formats it as a complete newsletter, saves it to the correct folder in my vault, and generates a description, curiosity-based bullet points, and five subject line suggestions. An entire content pipeline runs in one command.

That's the power of MCP: your vault, your tasks, your capture system, and your content pipeline all become one integrated system operated from a single interface.

The Cost: Why This Is the Best Value Setup Available

The entire setup costs €20 per month. That's it.

Obsidian is free. Claude Pro is approximately €20/month. The MCP servers I use for Things3 and Tana are free and self-hosted on my computer.

To understand why this is exceptional value, you need to understand how most AI productivity tools work. They charge you a subscription fee and then bill API usage on top. They make margin on the API tokens you consume. Per-token billing costs significantly more per session than a flat subscription. With Claude Pro, you get substantially more usage for €20 than you'd get paying equivalent API costs through another app.

The Notion comparison is worth spelling out clearly. A lot of people built their second brain in Notion, and for years I did too. The problem with Notion is that you spend more time maintaining the system (databases, views, templates, relations) than actually using it. And when you want to connect AI, you run into the proprietary format problem: Notion's data isn't cleanly accessible to external AI, and you end up locked into Notion's own AI offering, which comes with a margin.

With Obsidian: plain text files. Claude maintains your context automatically. You don't configure anything. You just work.

The Honest Assessment: Pros and Cons

I want to be straight about what this setup is and what it demands from you.

What It Does Well

The context is persistent, readable, and grows automatically with every session. It works with your existing Obsidian vault immediately, the day you install Claude Code. It's extendable via MCP, custom skills, sub-agents, and web browsing. It's the cheapest high-power AI setup available. And every piece of context the AI has about you is stored in plain markdown files you can read, edit, and fully control at any time.

If at any point Claude's understanding of you feels off, you open the CLAUDE.md file, fix it, and that's the end of it. Full control, all in plain text.

What It Demands

Terminal comfort is not optional. The visual Claude.ai interface is weaker because it doesn't give Claude full system access. That's a structural limitation, not a bug. The power lives in the terminal, and if you want the power, you have to go there.

That said, it's genuinely not as difficult as it looks. Invest a few hours getting comfortable with pwd, ls, and cd. Practice opening folders in the terminal. Within a week, it won't feel foreign anymore. The discomfort is short. The capability is permanent.

The initial setup takes time as well: writing a solid CLAUDE.md, organizing your files into your vault, running the first calibration sessions to get Claude properly aligned with your system. But here's the workaround: you can literally dump all your files into an inbox folder and ask Claude to organize them for you according to your system. You can even point it to my YouTube videos and ask it to build the folder structure according to my methodology. Because Claude can write files and create folders, it can build the system for itself.

Finally, the setup is less effective if your primary knowledge base lives in a proprietary format like Notion or Evernote. You need local markdown files for the full experience. That said, via MCP, Claude can access content stored in other tools and import it into your vault if needed. There are always workarounds.

What About Eden?

A lot of people who follow my content originally found me through my Kortex and Eden content. So I want to be direct about where Eden fits.

I use Obsidian with Claude Code because it's the most powerful setup I know for this kind of work. All the reasons in this article support that choice. But that doesn't mean Eden is wrong for you.

Eden is a solid alternative if you're not comfortable with the terminal and have no interest in becoming comfortable with it. If you want a visual, all-in-one interface where everything lives in the same place. If you're fine with your data on the cloud. If you want features Obsidian doesn't offer natively: YouTube video transcription directly into your vault, built-in cloud storage, or native collaboration features.

Everything I've described in this article applies to Eden as well. The IPARAG folder structure, the context system, the agentic workflows: all of it translates directly. Eden's agents give you the same capabilities in a more visual environment. And because both tools use native Markdown, if you build your system in Eden and decide later you want to move to Obsidian, the migration is clean and lossless. The option is always open.

One thing to know about Eden's credits: Eden runs on the API, meaning your usage is billed per token rather than covered by a flat subscription. For light to moderate use, credits will last and you'll be fine. For heavy power use (modifying hundreds of files at once, running long agentic sessions multiple times a day), credits may burn faster than Claude Code on Claude Pro, which can get expensive quickly.

Test it against your actual usage pattern before committing to a plan.

For those of you who migrated from Kortex to Eden and have no desire to switch systems again: don't. Apply what I've shown you in this article directly inside Eden. It works. The system is the system, regardless of the tool. That's the most important thing to take away from this section.

Conclusion: How to Start Today

You now understand the most powerful AI setup I've found for creators.

The foundation is simple: context beats prompts. Always. When your AI knows your folder structure, your projects, your voice, your writing rules, and your entire knowledge base, the quality of its output changes completely. The setup compounds: every session makes Claude more useful, more personalized, and more aligned with how you think and work.

Here's how to implement this starting today:

1. Install Obsidian (free). If you already have a vault, open it.

2. Install Claude Code. Open your terminal and run npm install -g @anthropic-ai/claude-code. It will prompt you to link your Anthropic account. That's all the setup it needs.

3. Navigate to your Obsidian vault in the terminal. The easiest way: right-click your vault folder in Finder, go to Services, and select "New Terminal at Folder."

4. Type claude to launch Claude Code inside your vault.

5. Ask Claude: "Read my vault structure and write a CLAUDE.md file for me." From that first session, your AI has context. You're in.

If you want to skip the setup and start with a system already built, I've created a complete LIFE OS vault template (free): the full IPARAG folder structure, a CLAUDE.md template, note templates, skill examples, and everything you need ready to import into Obsidian. You'll find the link in the description at Noah's Ark Bank, my free collection of templates, prompts, and SOPs for building your AI second brain:

Click here to download my entire AI Second Brain Setup for free:  https://noahsark.podia.com/noah-s-ark-bank

If this changed how you think about AI: share the article. And if you haven't watched the video yet, it covers the live demos of every workflow described here: https://youtu.be/BLdO-32I6Yc

Subscribe for more content on second brain systems and building a purposeful and profitable creator business every week.

Drop your biggest question in the comments. I read and answer every single one.

Welcome back to Noah's Ark. See you soon.