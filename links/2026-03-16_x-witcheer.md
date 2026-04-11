---
title: "I migrated my entire AI agent setup from OpenClaw to Hermes Agent (@NousResea..."
source: "https://x.com/witcheer/status/2033533371821789551?s=46"
date: 2026-03-16
tags: ["AI Agent", "Hermes Agent", "NousResearch", "OpenClaw", "Migration"]
platform: x
author: "@witcheer"
summary: "The author details a 3-hour migration from OpenClaw to Hermes Agent, noting that while data transfer was quick, resolving delivery pipeline bugs regarding Telegram integration was the main challenge."
---
I migrated my entire AI agent setup from OpenClaw to Hermes Agent (@NousResearch) in ~3 hours. same Mac Mini M4. same Telegram bot. same $21/month GLM-5 brain. different engine underneath.

~/ here's what I had before: 

14 launchd agents running independently, 25 custom shell scripts, 5 research crons, a breaking news monitor checking RSS + TVL + stablecoin pegs every 30 minutes, Docker sandbox for code execution, 54 RSS feeds via newsboat, 60 memory files. 
everything wired together with bash and launchd plists. it worked, and was fragile.

~/ here's what I have now: 

1 gateway process. that's it. 
one launchd service replaces 14. 
the 5 crons became 15, I added a competitor dashboard, Dune Analytics monitoring, a Telegram channel auto-drafter, content performance tracking, an outreach CRM, and a learning digest. all created in natural language instead of crontab syntax. 23 DeFi tools via a single MCP server connection. filesystem checkpoints so the agent can undo its own mistakes.
session search across past conversations. 3 custom skills I built during the migration.

the data migration took 30 minutes. hermes claw migrate --overwrite pulled my memory files, agent personality, and API keys automatically. I copied 60 memory files and 30 scripts manually to fill what the tool missed.

getting cron delivery to Telegram working took 90 minutes. three bugs stacked on top of each other:

1. delivery targets. deliver: "telegram" doesn't resolve without a home channel env var. I had to change all 15 crons to explicit telegram:chat_id format. 

2. message length. Telegram caps messages at 4096 characters. agent research outputs are 5,000-8,000 characters. every cron delivery was silently failing. I had to patch the scheduler to auto-chunk messages at 4,000 chars.

3. launchd PATH. macOS launchd services run with a minimal PATH. npx (needed for MCP servers) wasn't found. had to use absolute path
/opt/homebrew/bin/npx. 

4. bonus bug: Python bytecode caching. after patching the scheduler code, the fix didn't take effect because .pyc files were cached. 
had to delete __pycache__ & restart the gateway. 
if you're patching Hermes source files and nothing changes, this is why.

~/ the lesson: 

migrating an AI agent isn't a data problem. the data moved in 30 minutes. it's a delivery pipeline problem. getting the agent's output to actually reach you, through the right channel, in the right format, at the right time, without silent failures, is where the hours go. that's true regardless of which framework you use.

same Oz. different brain. 15 crons running. $0 additional cost. we'll see how this holds up.