---
title: "The 5 Levels of Agentic Software"
source: "https://x.com/ashpreetbedi/status/2024885969250394191?s=46"
date: 2026-02-20
tags: ["agentic software", "coding agents", "software architecture", "progressive development"]
platform: x
author: "@ashpreetbedi"
summary: "The article outlines five progressive architectural levels for building agentic software, starting with simple tools and evolving into production systems."
---
Most teams overcomplicate agents. They start with multi-agent orchestration, autonomous reasoning loops, and over-the-top infrastructure. Then spend weeks debugging why the simplest tasks fail.

The pattern I follow is embarrassingly simple: start simple, add capabilities progressively, verify behavior at each step.

Today I'll show you the five architectural levels of agentic software:

Agent with tools

Agent with storage and knowledge

Agent with memory and learning

Multi-agent teams

Production system

We'll build a lightweight coding agent called Gcode, adding one capability at a time. Like always, I'll share code snippets for every level.

Checkout the full cookbook for code you can clone and run today.

Disclaimer: I'm human and I make mistakes, please let me know if I got something wrong.

Level 1: Agent with tools

An agent without tools is just an LLM. It can reason, but it can't do anything. Tools are what turn an LLM into an Agent. For a coding agent, the minimum viable toolset is: read files, write files, and run shell commands.

What's happening: The agent receives a task, uses CodingTools to write, edit, and run code. The `all=True` flag enables every tool in the CodingTools toolkit (read, write, edit, shell, grep, find, ls).

What's missing: Every run starts from zero. The agent can't recall previous sessions, can't follow project conventions unless you paste them into the prompt, and has no knowledge beyond the current context.

Level 2: Agent with storage and knowledge

Level 1 is stateless. Everything needs to be in the context. Level 2 fixes this problem with two additions: session storage and domain knowledge.

Storage

Storage saves every agent session, and every run in it, to a database. This gives you two things.

Chat history as context. Using storage, the agent can include the last N messages in its context window so it knows what's going on. For longer sessions, you can run compression algorithms to summarize earlier context and keep the window focused on what matters right now.

A record of what happened. Not everything needs to be sent to a third-party tracing provider. Storing sessions in your own database is the simplest way to understand what your agent did, when, and why. You own the data. You can query it, audit it, build dashboards on top of it.

Knowledge

Today's coding agents only see the files in your codebase at and nothing else. They don't have access to your architecture specs, your team's design decisions, your internal meeting notes, or the Slack thread where someone explained why you chose Postgres over DynamoDB.

That's what knowledge fixes. It gives the agent a searchable store of everything that matters to the project but doesn't need to live in the context window at all times: specs, RFPs, runbooks, architecture decision records, meeting notes, team conversations.

The key insight is that a lot of valuable context lives outside the codebase. If your team discussed a migration strategy in a meeting last month, that context should be available to the coding agent when it's working on the migration. If someone made a decision to use library X over library Y six months ago, the agent should be able to find that reasoning before it rips out X and starts from scratch.

What changed: Two additions, Knowledge backed by ChromaDb (with hybrid search for both semantic and keyword matching), and SqliteDb for session storage. The agent now:

Searches knowledge before coding. If your style guide says "use snake_case", the agent finds and follows it.

Remembers conversations: ask a follow-up question in the same session, and it has full context.

Seeding knowledge: You insert documents (text, PDF, URLs) into the knowledge base. At run time, the agent searches for relevant chunks and adds them to its context. This is basic Agentic RAG.

When to use Level 2: When the agent needs to follow standards it wasn't trained on, or when users expect multi-turn conversations. This is the sweet spot for most internal tools.

Level 3: Agent with memory and learning

The jump from Level 2 to Level 3 is the most important one. At Level 2, the agent follows rules you give it. At Level 3, it learns rules from experience.

Interaction 1000 should be better than interaction 1.

What changed:

Learning Machine: The agent gets save_learning and search_learnings tools. It decides what's worth remembering: coding patterns that worked, mistakes to avoid, user preferences. These are stored in a separate knowledge base and surfaced in future sessions.

Agentic Memory: The agent builds a user profile over time: your preferred coding style, frameworks you use, how you like explanations.

The two-session test:

In Session 2, the agent searches its learnings, finds the functional programming preference, and writes functional code.

When to use Level 3: When the agent serves the same users repeatedly and should improve over time. Personal coding assistants, team tools with shared learnings, any context where "do it the way we like it" matters.

Level 4: Multi-Agent Team

Sometimes one agent isn't enough. Level 4 splits responsibilities across specialized agents coordinated by a team leader.

Coder writes, Reviewer reads (note: write/edit/shell disabled), Tester validates. The team leader coordinates and synthesizes.

Honest caveat: Multi-agent teams are powerful but unpredictable. The team leader is an LLM making delegation decisions. Sometimes it delegates well, sometimes it doesn't. For production systems where reliability matters, prefer explicit workflows over dynamic teams. Teams shine in human-supervised settings where a human can review the output.

When to use Level 4: When you need multiple perspectives (code review is a perfect example), when tasks naturally decompose into specialist roles, or when you're building interactive tools where a human can supervise the team.

Level 5: Agentic System (Production API)

Level 5 is the runtime that turns Levels 1-4 into a production service. You upgrade from development databases to production ones, add tracing, and expose everything as an API.

What changed:

PostgreSQL + PgVector replaces SQLite + ChromaDb. Real connection pooling, real backups, real concurrent access.

AgentOS wraps your agents in a FastAPI application with a built-in web UI, session management, and tracing.

Tracing (tracing=True) gives you observability into every tool call, every knowledge search, every delegation decision.

When to use Level 5: When the agent leaves your laptop. Multiple users, uptime requirements, the need to debug production issues.

The Most Important Advice

Start at Level 1. Build the simplest agent that could solve the problem. Run it. See where it fails. Then add exactly the capability it's missing.

Most teams skip to Level 4 because multi-agent architectures look impressive in demos. Then they spend months debugging coordination failures that a single agent with good instructions would have avoided.

Think of the levels as a hierarchy of capability and remember that each level adds complexity, and complexity has a cost. Pay it only when the simpler approach has clearly failed.

Here's the cookbook with runnable code for all five levels. Clone it, run it, let me know if something's not working. I'm a human and I make mistakes.

Built with Agno - the programming language for agentic software.