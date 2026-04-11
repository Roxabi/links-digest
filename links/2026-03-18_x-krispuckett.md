---
title: "A Designer\u0027s Guide to the AI Galaxy"
source: "https://x.com/krispuckett/status/2034034332738998377"
date: 2026-03-18
tags: ["AI", "Design", "Agents", "Skills", "MCP"]
platform: x
author: "@krispuckett"
summary: "A designer\u0027s guide clarifying fundamental AI concepts\u2014Agents, Skills, Plugins, Hooks, and Oracles\u2014to establish distinct terminology for building AI systems without hype."
---
I love building with AI. I love using actual tools that handle real work. And the single biggest source of confusion I see, and get asked about:

What's an agent? What's a plugin? What's a skill? Are they the same thing?

They're not. 

So here's a designer's guide at explaining the foundations, with zero hype or hyperbole. 

Seven concepts, plain language, and a link to a starter kit.

---

1. Agents

An agent is a fully scoped AI brain. Its own workspace, its own memory, its own personality. A person on your team with their own desk.

The difference from a chatbot is autonomy. You say "research cabinet hardware for walnut kitchens." The agent decides which searches to run, which sites to check, how to organize findings. You set the goal. The agent figures out how.

Multiple agents are fully isolated. Different workspaces, different personas, different conversation histories. Agent A can't see Agent B's context unless you allow it. Important when you're designing systems where a researcher agent, a writing agent, and a project management agent each handle different tasks. 

Separate people, separate desks.

2. Skills

A skill is a self-contained folder that teaches an agent how to do a specific thing. The recipe card metaphor gets you started, but it's really a whole kitchen station: the recipe, the prep tools, reference photos, and notes from every time they've cooked this dish before.

Inside a skill folder:

SKILL.md — the core instructions

Scripts and executable code the agent can compose with

Assets — templates, reference data, example files

Configuration — first-run setup and prerequisite checks

Memory — append-only logs so the skill improves over time

The folder structure does work. Skills use progressive disclosure — read SKILL.md first, dig into subdirectories only when needed. Keeps token costs low.

If you're building skills: the description field exists for the model, not for you. The agent reads all skill descriptions at session start to decide which ones apply. Write that description as a trigger for the AI, not a human readme.

Anthropic recently published how they use skills internally:  hundreds of them across nine categories: API reference, testing, data analysis, business process automation, code scaffolding, code review, CI/CD, operational runbooks, and infrastructure ops. 

Skills aren't just personal productivity helpers. They're how you encode entire workflows into something an agent can execute.

One practical note: the highest-signal section in any skill is the gotchas. Common failure points, edge cases, things that break in ways you wouldn't predict. If you write one section well, write the gotchas.

I put together a starter skill kit — three templates you can drop into your .claude/skills/ directory and customize in ten minutes. 

Grab it here: github.com/krispuckett/starter-skill-kit

3. Plugins and MCP

Two related concepts that do similar things differently.

Plugins are code that extends the platform itself. They run inside your gateway and add entirely new capabilities — a new messaging channel, a new tool, a new CLI command. A voice-call plugin lets your agent make phone calls. No skill can do that if the capability doesn't exist yet.

Skills are knowledge. Plugins are capability.

MCP (Model Context Protocol) is an open standard — USB-C for AI. A universal connector so any model can talk to any tool server. MCP servers work with Claude, GPT, anything that speaks the protocol. Plugins only work with the platform they're built for.

Both augment what the agent can do. MCP are now an industry standard. The future will likely be a mix of MCP, CLIs (command line interface), and APIs.

4. Hooks

Hooks fire automatically when specific events happen. Session resets, messages arrive, system starts up; a hook runs a script.

Hooks don't use AI.  "When X happens, do Y." No model inference, no token cost, no ambiguity. A hook that saves your conversation summary on reset will always save it, exactly the same way.

Examples: auto-save summaries on session reset, log commands for audit, inject context on startup, run initialization scripts.

There's also on-demand hooks — registered by skills, only active during that session. A production database skill can register a hook that blocks dangerous commands while active. Type /careful and DROP TABLE gets intercepted. End the session, the guardrail goes away. Skills bring their own safety rails.

When something needs to happen reliably every time, use a hook. Don't leave it to a prompt.

5. Cron Jobs

The scheduler for the system. When you need precise times, "every Monday at 7 AM" or "every six hours", a cron job is the tool to use.

Main session injects the task into the agent's next check-in, alongside everything else it's aware of. Good for reminders.

Isolated session spins up a fresh turn with zero prior context. Good for reports. You can use a cheaper model for routine cron jobs to keep costs down.

Cron is about precision. One job, one schedule, one purpose.

6. Loops and Heartbeats

A heartbeat is the agent's periodic pulse. Every 30 minutes, the agent runs through a checklist: check email, review calendar, scan notifications. If nothing's urgent, it responds with an all-clear that gets silently suppressed. If something matters, it surfaces it.

This gives agents ambient awareness. Your agent isn't a tool you pick up and put down. It's a presence that notices things while you're focused on something else. Calendar conflict while you're deep in a design file? Caught. Client email that needs a fast reply? Surfaced before you check your inbox.

Most documentation on agent architecture misses this entirely. It's the most interesting part.

Heartbeat vs. cron: A heartbeat batches multiple checks into one turn. Context-aware, cheap, good for monitoring. Cron runs one task at one time, optionally isolated. Heartbeat says "keep an eye on things." Cron says "do this exact task at this exact time."

7. Triggers

How an agent gets activated. A category of entry points:

Direct messages — someone texts the agent

Mentions — agent responds when @mentioned in groups

Bindings — routing rules mapping messages to agents by channel, sender, or group

Commands — /reset, /status

Webhooks — external HTTP calls

Inter-agent messages — one agent tasks another

Scheduled — cron and heartbeats

Bindings are the most important in multi-agent systems. Message comes in on Telegram — does it go to research or writing? Bindings decide. You're designing an org chart for AI.

---

You've been designing for humans with roles, tools, habits, schedules, and attention triggers your whole career. 

Agent architecture is the same concepts, same design thinking,  just with AI on the other end.

If this helped at all and want to learn more,  I created a course on building your ideas through AI by creating your own personal operating system. Nine modules, everything from workspace setup to multi-agent orchestration. 

It's called NEUMA.