---
title: "how i fixed my AI agent\u0027s memory."
source: "https://x.com/the_smart_ape/status/2035643464465916052?s=46"
date: 2026-03-23
tags: ["AI Agents", "Memory Management", "Token Optimization", "Context Window", "LLM"]
platform: x
author: "@the_smart_ape"
summary: "The author proposes a three-tier memory architecture\u2014pocket, desk, and bookshelf\u2014to fix AI agent amnesia while reducing costs and avoiding performance degradation caused by large context windows."
---
AI agents forget everything. every single session.

this is the biggest problem everyone talks about with AI agents. the solution isn’t native (it might be one day), but if you don’t handle it yourself, you’ll either end up with an amnesic agent or face significantly higher API costs.

most people fix this by writing everything in MEMORY(dot)md. every decision, every bug fix, every preference, every project detail.

that file isn't just read once. it's included in every single message you send to the AI. think of it like a phone call where you have to re-read your entire diary before saying each sentence.

if the memory is 200 lines, that’s roughly 3,000 tokens burned per message just to provide context to the AI, still acceptable.

but if the memory grows to 2,000 lines, that’s around 30,000 tokens per message. at 50 messages per day, that's $112/month just for loading memory, and you haven’t even asked it to do anything yet.

some people go further and try to load their entire knowledge base. that's 150K tokens. $675/month. just for context.

but honestly the money isn't even the worst part. there's research showing that past 40K tokens of context, your agent starts following instructions worse. you're literally making it dumber by giving it more memory.

dumping everything in one file is expensive AND makes your agent worse.

the solution

i spent way too long figuring this out so let me save you the headache.

think about how you deal with information in real life. you don't carry every book you own in a backpack everywhere you go.

you keep your phone and wallet in your pocket. important stuff on your desk. everything else in a bookshelf, and you grab what you need when you need it.

same idea for your agent. three levels.

level 1: the pocket

this is your MEMORY.md. but it has to stays under 200 lines. no exceptions.

it's not a storage file. it's a table of contents. it has:

who you are (3 lines, that's enough)

what you're working on right now

a handful of active decisions

pointers to other files ("for project details, check projects.md")

hard rules ("don't sign tx without my approval")

that's it. notice what's NOT in there, project history, old bug fixes, code style preferences, API docs. all that stuff lives somewhere else.

cost: ~3,000 tokens per message. barely anything.

level 2: the desk

the trick is the agent only reads the files it actually needs for what you're asking. working on frontend? it grabs style-guide(dot)md. debugging auth? it loads gotchas(dot)md. doing something unrelated? those files stay on the shelf.

this is called progressive disclosure and honestly it's the biggest win here. someone at ClaudeFast actually measured it: 82% fewer tokens per session. that's 15,000 tokens you're not paying for every time.

all you need in MEMORY is a list so the agent knows what's available:

memory/projectsmd: what I'm building

docs/gotchasmd: stuff that bit me before

docs/architecturemd: how the system works

agent reads this mini index, figures out which files matter, loads only those. done.

level 3: the bookshelf

this one you don't need right away. but once you've got hundreds of notes, maybe you're using Obsidian or you've been running this system for a year, even selective file loading gets clunky.

that's when you add search. tools like Mem0 (open source, free) or Smart Connections (Obsidian plugin) let your agent ask questions to your entire knowledge base and get back only the relevant bits.

instead of "let me read through 50 files to find that one bug fix," it's "what do we know about OAuth bugs?" and it returns the three paragraphs that matter.

Mem0's research shows 90% less tokens used and 26% better answers compared to the "shove everything in context" approach. not a small difference.

keeping it clean

this whole system falls apart if you don't maintain it. without maintenance, you're back to a bloated mess in three months.

but the maintenance is dead simple.

daily: the agent writes raw notes about what happened. messy, complete, unfiltered. this is the inbox.

weekly: spend 10 minutes (or have your agent do it). what patterns showed up? what decisions matter long-term? keep those. dump the rest.

monthly: distill the weekly stuff into MEMORY.md. only what's still relevant makes the cut. old stuff goes to an archive folder you'll probably never open.

it's like making orange juice. start with whole oranges (daily notes), squeeze them (weekly review), keep the juice (MEMORY). the pulp goes to compost.

this loop is how MEMORY stays under 200 lines forever.

the numbers

before: 25K tokens loaded with every message. $112/month. agent confused by its own context.

after: 3K tokens base. relevant files loaded on demand. $13/month. agent that's actually sharp because it's not drowning in noise.

88% less tokens. better answers. lower bill.

how to set this up (takes 15 minutes)

step 1: make a MEMORY in your project folder. keep it under 200 lines. put in: who you are, what you're building, active decisions, file pointers, and rules. that's it.

step 2: take everything else and split it into separate files. one per topic, projects, gotchas, architecture, whatever.

step 3: add a "reference files" section in MEMORY that lists every file with a one-line description. this is your agent's map.

step 4: once a week, look at your daily notes. compress the patterns. update the relevant files. delete what's obsolete. 10 minutes max.

step 5: when you hit 50+ files, add Mem0 or Smart Connections for search. that's your upgrade path when things grow.

just text files organized well.

last say

a while back I couldn't figure out why I kept hitting my usage limit on a $200/month subscription. like. turns out half my tokens were being wasted on a massive memory file the agent was dragging around with every single message.

since I switched to this setup I've never hit that limit again. not once. same subscription, same usage, just way less waste.

my agent reads its pocket file every morning, loads what it needs during the day, and distills what it learned every night.

build a library, not a backpack.