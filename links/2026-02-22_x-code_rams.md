---
title: "Day 5 of debugging Chiti's memory."
source: "https://x.com/code_rams/status/2025371800587436344?s=46"
date: 2026-02-22
tags: ["AI agent debugging", "System prompt optimization", "Token reduction", "Memory management"]
platform: x
author: "@code_rams"
summary: "The author optimized an OpenClaw agent by removing unused skills and streamlining memory files to reduce token bloat."
---
Day 5 of debugging Chiti's memory.

Today wasn't about retrieval or indexing. 
It was about bloat.

I ran /context detail(telegram) and realized 
my agent was loading 11,887 tokens of system prompt on every new session.

51 skills. 20 of them I never used. 
200 lines of http://MEMORY.md loaded every single session. Two competing boot sequences fighting each other. 

Worst part? 
Every time I switched models, Chiti forgot everything. No handover. No write-back. Just gone.

Here's what I found:
OpenClaw only auto-reads these files on each new session: 
http://AGENTS.md, http://SOUL.md, http://TOOLS.md, http://IDENTITY.md, http://HEARTBEAT.md, http://MEMORY.md

Everything else?
http://LEARNINGS.md, daily logs, docs/, memory/ -
the agent has to read them itself. 

If the boot instruction isn't in http://AGENTS.md, 
it doesn't run.

So I cleaned house:
- Moved boot sequence to top of http://AGENTS.md
- Added write discipline (every task logs, every mistake becomes a rule in learnings/LEARNINGS.md)
- Added handover protocol before model switches
- Slimmed http://MEMORY.md from 200 lines to 90
- Moved reference docs to a docs/ folder
 - Removed 20 unused skills

Result: 
11,887 → 8,529 system prompt tokens 
51 → 32 skills 
28% lighter.

Same agent. Same models. Just less noise.

The real fix wasn't adding more files. 
It was removing the ones that weren't doing anything.

If you're running OpenClaw, try this right now:
1. /context detail - see what's actually eating your tokens
2. /skills list --json - find the skills you forgot you installed
3. Switch models. Ask "what were we working on?" If it's blank, your handover is broken.
4. Check if your boot instructions are in http://AGENTS.md. If they're anywhere else, the agent isn't reading them.

Day 1 was compaction. 
Day 2 was indexing.
Day 3 was retrieval. 
Day 4 was making it compaction-safe. 
Day 5 was realizing the problem was never memory. It was weight.