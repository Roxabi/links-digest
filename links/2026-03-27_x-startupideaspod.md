---
title: "How to build an AI Agent company using Paperclip"
source: "https://x.com/startupideaspod/status/2037247132927926452?s=12"
date: 2026-03-27
tags: ["Paperclip", "AI Agents", "Orchestration", "Open Source", "Startup"]
platform: x
author: "@startupideaspod"
summary: "Paperclip is an open-source orchestration layer that enables users to manage a virtual company of AI agents, solving context and tracking issues by organizing work around business goals, defined"
---
How to Use Paperclip to Run a Company of AI Agents

The orchestration tool behind 30,000 GitHub stars in 3 weeks.

The problem Paperclip solves

@dotta , the creator, was using Claude Code to build his companies. He had 20 or 30 windows open at once.

He couldn't remember what any of them were working on. He'd set them to run over the weekend. Come back Monday. No idea what was accomplished. Budget blown on tokens.

Paperclip is the tool he built to fix that.

What Paperclip actually is

An open-source orchestration layer for AI agents. You define your business goals. You hire a team of agents. You approve their work. They execute.

Think of it as the layer between "I have an idea" and "AI agents are building it right now."

It's not fully automatic like Pulsia, where you hand over your credit card and hope. It's not as manual as managing individual coding tabs. You manage at the level of business goals, org charts, and task tracking.

Step 01: Set Up Your Company

Name your company. Describe what it's trying to achieve. Create your first agent: the CEO.

Paperclip works best when you run it locally. You bring your own model. Claude Code, Codex, OpenCode: any of them work.

Hot tip from Dotta: use a frontier model for your CEO. Use cheaper models (or free ones from OpenRouter) for simpler tasks.

Your CEO agent gets a default persona, a memory system, and a heartbeat checklist.

Step 02: Understand the Memento Problem

Here's Dotta's mental model for AI agents:

Your agents are the guy from Memento. They wake up capable. They know how to code, how to write, how to spend money. But they don't know who they are, where they are, or what they're supposed to be doing.

You have to leave them Polaroids. Write tattoos on their arm. Tell them who they are and what the plan is.

That's the heartbeat. When the agent wakes up, it reads: who am I, what's my job today, what tasks are assigned to me, what's the quality bar.

When an agent does something you don't like, you go into the heartbeat config and add a rule. Example: "Set a success condition for every task. Ask QA to review before closing."

You iterate on the prompt the same way you'd coach an employee.

Step 03: Hire Your Team

Your CEO hires other agents. Engineer. QA. Video editor. Content strategist.

You approve the hires (or turn on auto-hiring once you trust the system).

Each agent can have different skills installed. Skills come from repos like skills.sh. Security audits exist but aren't bulletproof. GitHub stars are a directional signal, not a guarantee.

Dotta's own Paperclip org: CEO, CMO, UX designer, CTO, QA engineer, evals engineer, blogger, content strategist. Different agents use different models depending on the task.

Step 04: Use Routines for Recurring Work

Routines are reusable issue templates that run on a schedule.

Dotta's example: every day, read the GitHub changes merged into the main branch. Write a Discord message celebrating community contributors. Trigger it at 10 a.m. daily.

Every run is tracked. You can see tokens spent, what the agent found, what it wrote. No invisible background jobs.

Step 05: Import Proven Teams

This is where it gets interesting.

Paperclip is shipping the ability to import and export companies. Gary Tan's G-Stack. The agency-agents repo with 60,000 stars and 100+ agents. A game studio template with a creative director, producer, and technical director.

You can acqui-hire a proven team structure into your Paperclip instance. All skills, all agent configs, all referenced from remote repos so they stay updated.

The obvious question: does it actually work? Dotta's honest answer: it's unproven at scale. There are no evals yet for these massive agent repos. Paperclip is the first runtime that can actually test them.

Who's using Paperclip today

The tool has been live for about three weeks. Early adopters include:

A security review company using Paperclip to run automated security audits on client systems (they even audited Paperclip itself).

A dentist organizing foundation work and family logistics.

A roofing company exploring AI agents that find leads by cross-referencing hail data and satellite imagery with neighborhoods likely to have insurance coverage.

Marketing firms setting up agent teams alongside human teams.

The big idea: AI can do everything except know your values

Dotta's core thesis: the models can code, write, design, and plan. What they can't do is share your taste.

Your job as a founder shifts. You become the person who clearly communicates values and quality standards. Then you encode those into agent personas, skills, and heartbeat checklists.

That was always the job of a good leader. The vehicle changed. Instead of hiring employees, you're hiring agents.

What's coming next

Maximizer mode: tell the CEO to keep agents working until a project is completely done, regardless of token spend.

CEO chat: talk to any agent directly instead of creating issues for everything.

Better artifact management and onboarding.

Performance reviews: Paperclip will track feedback patterns so your agents learn from repeated corrections.

Action checklist

Install Paperclip locally from the GitHub repo (30K+ stars, open source)

Create your first company and CEO agent using a frontier model

Write a heartbeat checklist: who is this agent, what does it do, what's the quality bar

Hire your first engineer and QA agent

Set up one routine for recurring work

Browse importable companies and agent repos to shortcut your org structure