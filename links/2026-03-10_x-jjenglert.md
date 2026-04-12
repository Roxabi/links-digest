---
title: "After a month of watching my fellow builders set up their @openclaw , I final..."
source: "https://x.com/jjenglert/status/2031486623171437016?s=46"
date: 2026-03-10
tags: ["AI agent setup", "OpenClaw tips", "autonomous agents", "persistent memory"]
platform: x
author: "@JJEnglert"
summary: "The author shares their experience setting up an OpenClaw AI agent that runs autonomously on a dedicated device and provides practical tips for configuration, training, and workflows."
---
After a month of watching my fellow builders set up their @openclaw , I finally took the plunge this past week.

Last night my agent ran overnight on a project we came up with together, and it was ready for review when I woke up this morning.

It has its own GitHub account. Its own email. Its own Twitter. It runs 24/7 on an old MacBook Pro with the lid closed. And it has enough tools connected to actually do real work.

But the magic moment wasn't the overnight build. It was something way simpler.

I told it to message me at 7:30 AM with a daily plan. And it just did it. Figured out how to do it on its own. That "figure it out" mentality from an agent that actually has access to tools and a computer felt different than anything I've used before. For the first time, it felt like something capable of doing real stuff. Not a chatbot. Something else.

And I'm just scratching the surface.

It took me about 8 hours to get here. I want to help you get there faster. Here's everything I learned along the way, plus a prompt you can copy and paste into your OpenClaw once you're set up.

Getting started

I set it up on an old MacBook Pro. Dedicated device. You want this running independently so it does not have access to your data. Having a virtual device on @Hetzner_Online is also good.

Installation took about an hour. Then I spent the next two hours having Codex tighten the security before training it anymore. Sandbox commands. Whitelist only what you need. Do this first.

Then I hit a wall. It felt like a chatbot. Limited permissions. Couldn't access tools. Couldn't browse. It took another 2-4 hours to get terminal access and Playwright browser control working. 

I used Caffeinate in terminal to keep it running with the lid closed. 

I set up dedicated accounts. GitHub, email, Twitter. Give it its own identity so it can operate independently.

Training it

- Keep your Heartbeat.md lean. It gets read every session and burns tokens if it's bloated. Identity, active projects, key preferences. That's the hot cache.

- Install a memory plugin early (ClawVault, Supermemory, or Lumen Notes). Persistent memory across sessions is what takes it from chatbot to something that knows your work.

- Build skill files for recurring output. Emails, social posts, documents. Each gets its own file with format, voice rules, examples, and a checklist. It follows these like playbooks.

- Define your agent's persona and tone. I built out voice files based on what I'd already created in Cowork and the output quality jumped immediately.

- Point it at your existing repos. It can pull context from anything you give it access to. If you've already built structure somewhere, don't rebuild it. Reference it.

Best advice I got from experienced OpenClaw builders

Force plan before execution. Make it tell you what it's going to do before it does it. Saved me from multiple rabbit holes.

Back up your repo to GitHub every night. Your config files, skills, and memory directory are the training. Lose them and you're starting over.

Think in workflows, not one-off tasks. This compounds fast.

I also applied the same repo structure from my Cowork setup guide:

Your-Workspace/
├── Heartbeat.md
├── Brain/
 │   ├── about-me.md
 │   ├── brand-voice.md
 │  └── working-preferences.md
├── Skills/
├── Projects/
└── Memory/

I'm about a week in. Still early. But I can see where this is going and I wish I'd started sooner.

If you're just getting started, here's the prompt I'd paste in on day one to fast-track the whole setup:

--

You are going to help me set up my workspace so that every future session starts with full context about who I am, what I do, and how I work. We're building the files and structure that make you useful from the first message.

Interview me in phases. Ask questions, then build files based on my answers. Don't rush. Don't assume. Ask before you build.

Phase 0: Foundation
Check if I have a Heartbeat.md file. If not, create one. Keep it lean. Recommend a memory plugin for persistent context. Ask what tools I use daily and help me connect them. Recommend sandboxing and whitelisting commands from the start.

Phase 1: Identity
Interview me to create Brain/about-me.md. Ask about my work, background, what I'm building, and positioning. Show the file. Get approval before moving on.

Phase 2: Voice
Interview me about how I want my agent to sound. Phrases I use. Phrases I'd never use. Tone shifts by context. Create Brain/brand-voice.md. Get approval.

Phase 3: Working Preferences
What I want help with. Communication style. Workflow pain points. Output preferences. Create Brain/working-preferences.md. Get approval.

Phase 4: Skill Files
For each type of recurring output, create a skill file in its own folder under Skills/. Each gets: format, voice rules, examples, quality checklist. Ask what I create most often before building.

Phase 5: Active Projects
Current projects, goals, deadlines. Individual files in Projects/.

Phase 6: Memory System
Update Heartbeat.md with a summary of everything we built. Create Memory/ directory with subfolders for people, projects, context. Add glossary.md.

Phase 7: Reference Sources
Any existing repos, docs, or files I want referenced. Organize access.

Rules: One phase at a time. Show each file before saving. If unsure, ask. Concise files. Lowercase, hyphens, .md format.

Start with Phase 0.