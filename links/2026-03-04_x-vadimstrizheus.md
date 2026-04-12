---
title: "my 13 AI employees don't just follow instructions."
source: "https://x.com/vadimstrizheus/status/2029200944223908025?s=46"
date: 2026-03-04
tags: ["AI agent architecture", "multi-agent system", "autonomous workflow", "memory layer system"]
platform: x
author: "@VadimStrizheus"
summary: "An 18-year-old built a 13-agent AI system with identity, memory, and shared brain layers that autonomously coordinate to run a company."
---
my 13 AI employees don't just follow instructions.

they remember. they talk to each other. they self-improve.

i'm 18, and here's the exact architecture running my company right now.

every agent has 3 layers:

⎯⎯⎯

LAYER 1: IDENTITY

each employee gets a .md file at ~/.openclaw/workspace/employees/EMPLOYEE.md

this is their soul. personality. rules. tools. what model they run on.

13 agents: CLAWD (dev) 
· ATLAS (research) 
· PIXEL (design) 
· NOVA (video)
· SCRIBE (writer) 
· VIBE (motion) 
· TRENDY (viral scout) 
· SAGE (email) 
· CLOSER (outreach) 
· CLIP (clipping) 
· CONTENT (blog)
· WRITER (articles) 
· SENTINEL (QA)

36 employee files total. they read their identity on spawn. they know who they are before they do anything.

LAYER 2: MEMORY

every employee has a personal memory directory:
employees/memory/EMPLOYEE/YYYY-MM-DD.md

daily logs. what they did. what they learned. what went wrong.

when SCRIBE writes a tweet that flops, it logs why. next session, it reads that log and adjusts. when CLAWD ships a PR with a bug, it writes the lesson.

they wake up fresh. but they read their memory first. never start from zero.

LAYER 3: SHARED BRAIN

~/.openclaw/workspace/shared-brain/
21 JSON files ALL 13 agents read and write to:

intel-feed.json 
· agent-handoffs.json 
· scribe-banger-vault.json 
· scribe-tweet-queue.json 
· content-calendar.json 
· and 16 more.

the handoff pipeline:

1. TRENDY scouts viral content every 2h
2. writes to intel-feed.json
3. SCRIBE reads it on spawn
4. drafts tweets from what's trending
5. writes to scribe-tweet-queue.json
6. i approve on Telegram with one tap

no human coordinating. the JSON files ARE the communication layer.

⎯⎯⎯

http://spawn-employee.sh auto-injects on every spawn:

· identity file · last 2 days of memory · shared brain · daily logs

one command. they wake up knowing everything.

the loop:
BEFORE task → read memory + shared brain

AFTER task → WRITE lessons back to memory + update shared brain

every cycle, the system gets better.

underneath: 8 SQLite databases + a vector knowledge base (semantic search across everything that's ever happened).

⎯⎯⎯

paste this into OpenClaw to build your own:

"create an employee system: 1) employees/ dir with .md identity files per agent 2) employees/memory/AGENT/ for daily logs as http://YYYY-MM-DD.md 3) shared-brain/ with JSON files for inter-agent comms 4) spawn script that injects identity + memory + shared brain before every spawn 5) memory protocol: read before work, write lessons after 6) vector db so any agent can search everything. start with 3 agents: dev, researcher, writer."

⎯⎯⎯

13 agents. 36 identity files. 21 shared brain files. 8 databases. 1 vector knowledge base. 1 spawn script.

they don't just execute. they remember, communicate, and compound.

this is what a one-person company looks like in 2026.