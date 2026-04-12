---
title: "This army of @openclaw agents runs an entire company for $400/month. Here's t..."
source: "https://x.com/jacobsklug/status/2029550513747112377?s=46"
date: 2026-03-05
tags: ["AI agents", "Business automation", "Agent structure", "Company operations"]
platform: x
author: "@Jacobsklug"
summary: "Jacob Klug details how an army of OpenClaw AI agents runs a company for $400/month using specific models and workflows."
---
This army of @openclaw agents runs an entire company for $400/month. Here's the exact structure to follow.

(bookmark for later)

1/ Core

→ Jarvis (the brain)
→ Model: Opus 4.6 via Claude Max OAuth
→ Routes every task to the right sub agent automatically. YouTube URL comes in, it goes to Clipper. Research report lands, it goes to Scribe. All task routing logic lives in structured MD files the agent reads from.

2/ Research

→ Atlas (deep research analyst)
→ Model: Claude via OAuth
→ APIs: Brave Search, X API, FireCrawl
→ Cron: Every 1 hour
→ Runs deep research across X, Reddit, and the web nonstop. Trained on
MrBeast's virality framework from every podcast he did on YouTube analytics, plus Dan Koe's viral article structure. Outputs research reports and a master virality playbook MD file that the content team pulls from.

3/ Content

→ Scribe (copywriter)
→ Model: GLM 5
→ Cron: Every 3 hours
→ Takes research from Atlas and writes draft posts matched to the founder's voice and style.

→ Trendy (trend scout)
→ Model: GLM 4.7
→ APIs: X API
→ Cron: Every 2 hours
→ Scans X and Reddit for trending topics and viral patterns. Reports findings back so Scribe can write timely content around what's working right now.

4/ Design

→ Image Designer
→ Model: Nano Banana Pro (Google API)
→ Generates images on demand.

→ Video Producer
→ Models: Higgs Field API + Brok Imagine API
→ Creates AI UGC videos and video content.

→ Motion Designer
→ Model: Claude Code (OAuth) + Remotion
→ Produces motion graphics and animated content.

5/ Development

→ Clawed (senior developer)
→ Models: Claude Code (OAuth) + Codex 5.3 (API)
→ Cron: Every night at 11pm
→ Reviews entire codebase, identifies what's missing, and ships pull requests by morning. First feature it ever built was a FAQ section it realized the homepage needed. Spins up multi agents within Claude Code so one reviews, one builds, one handles security in parallel.

→ Sentinel (code reviewer + bug monitor)
→ Model: Separate LLM (acts as second review layer)
→ Cron: Every 2 hours
→ Reviews all pull requests from Clawed before anything gets merged to GitHub. Also monitors production for user reported bugs and errors.

6/ Growth

→ Atlas + Scribe working together
→ Atlas finds Reddit threads where people complain about competitors or ask for clipping tool recommendations. Scribe drafts responses. The founder copies and posts. This workflow alone drove 450+ users to the SaaS with zero ad spend.

7/ Operations

→ Clipper (clipping agent)
→ APIs: Poster API
→ On demand (triggered by Jarvis when a YouTube URL is pasted)
→ Takes YouTube URLs, clips them, adds captions, and auto schedules posts to social channels.

→ Ryder (9 to 5 support)
→ On demand
→ Handles tasks for the founder's day job. Article writing, research, daily work support.

The breakdown: 6 agents run on Claude models.

The rest run on cheaper API credits across GLM, Higgs Field, Brok Imagine, and others.

This is how solo founders are running entire companies now. The team is already built. You just have to set it up.