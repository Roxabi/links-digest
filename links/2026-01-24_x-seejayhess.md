---
title: "The Swarm Has Arrived"
source: "https://x.com/seejayhess/status/2015148706471846275"
date: 2026-01-24
tags: ["AI", "agents", "Claude", "swarms", "coordination"]
platform: x
author: "@seejayhess"
summary: "Claude Code's new task system enables true agent swarms by providing isolated 200k token context windows per sub-agent and enforced dependency management for parallel task execution."
---
Agent Swarms Are Here

We've been talking about agent swarms for years. Multiple AI agents coordinating on complex tasks, spawning sub-agents, managing dependencies in parallel. The demos always looked great and then you'd try to use them on real work and watch everything fall apart.

This week I was in the middle of a big auth refactor when I saw Claude Code's new task system drop. I wanted to push it to its limits, so I created a massive task list and had it orchestrate sub-agents to execute the whole thing...and it nailed it?

I think we just crossed something that most people haven't noticed yet.

The Thing Everyone Gets Wrong

Most people see the task system and think "oh, new todos." Which... sure, that's what it is. But, now your tasks survive /clear, they survive session restarts, and if you set the CLAUDE_CODE_TASK_LIST_ID environment variable they'll even survive closing your terminal.

But most people are looking at the wrong part.

The task system is fundamentally a coordination layer. It lets multiple agents work in parallel, track what depends on what, and share state that survives beyond any single conversation.

Think of it this way: before, Claude was a single brain trying to hold an entire complex project in its head at once. Now Claude can break work into pieces, hand those pieces off to separate agents that each have their own context window, and coordinate everything through a shared dependency graph. That's a completely different capability.

How It Actually Works

Here's what the task system is doing:

Each task can spawn its own sub-agent, and each sub-agent gets a fresh 200k token context window that's completely isolated from the main conversation. This is the key thing that makes the whole system work.

Think about what that isolation gives you. Agent 1 is digging through authentication code and building up this whole mental model of how sessions are handled. Agent 2 is off refactoring database queries and holding schema details. Agent 3 is working through tests and tracking which assertions need to change. None of them are polluting each other's context or getting confused by what the others are doing because they literally can't see each other.

This is so different from the old approach where Claude is trying to hold everything in one conversation. That works for small stuff, but once you're doing anything complex you hit this wall where Claude is trying to remember decisions from earlier while also implementing new things while also tracking which files have been touched. Context management, context management, context management. Stuff falls through the cracks.

With the task system, each agent gets to focus on one thing. And when a task completes, anything that was blocked by it automatically unblocks and the next wave of work kicks off. The coordination is baked into the structure instead of being something Claude has to actively manage.

Dependencies Are the Real Feature

The unsung hero here is blockedBy

This isn't a suggestion. Task #3 literally cannot start until tasks #1 and #2 are both complete. The system won't let it proceed, which means Claude can't accidentally skip ahead or forget a prerequisite step because the structure itself enforces the order.

Without dependencies, Claude has to hold the entire plan in its working memory. For small tasks that's fine, but for anything complex the plan starts degrading the moment Claude's context fills up or you run /clear. You end up having to re-explain what you wanted, what's done, what's left, what depends on what. The plan only exists in Claude's head, which makes it fragile.

With dependencies, you've externalized the plan into a structure that survives context compaction, survives session restarts, survives you coming back to a project three days later. The graph doesn't forget and it doesn't drift. It never needs to be re-explained because it was never stored in memory to begin with.

This is why Ralph was all the craze for reanchoring. Anthropic just killed Ralph.

The Workflow Change

Before the task system, my Claude Code sessions would go something like:

Ask Claude to do something complex

Watch it get maybe 60% of the way there

Notice it forgot step 2 while working on step 5

/clear and start over

Repeat until frustrated

With the task system:

Ask Claude to break down the work

Review the task graph

Let it run

Tasks complete in order because that's the only order they can complete in

The structure enforces correctness. The dependency graph exists outside Claude's context window, so there's nothing to forget.

Free Parallelism

Here's something that took me a while to fully appreciate: you can have seven to ten sub-agents running at the same time.

Think about what that means - if you gave Claude a 10-task project the old way, it would work through them sequentially, task 1 then task 2 then task 3, even if half of them were completely independent and could be done in any order. Claude would still go through them one at a time because everything was happening in a single conversation thread.

With the task system, Claude looks at the dependency graph and spawns everything that can run in parallel. Tasks 2, 3, and 4 don't depend on each other? All three agents spin up at once, each with its own context window, each working independently. You just got 3x faster without doing anything different.

It picks the right model for each job too - Haiku for quick searches, Sonnet for implementation work, Opus when you need heavy reasoning. You're not thinking about resource allocation or cost management, you just define the dependencies and the system handles all the orchestration automatically.

Persistence

Set one environment variable:

export CLAUDE_CODE_TASK_LIST_ID="my-project"

Now your tasks live in ~/.claude/tasks/my-project/. Start a new session tomorrow, they're still there. Different terminal, same task list. Multiple Claude sessions working on the same project can all see and update the same tasks.

This is where it gets interesting for longer-running work. A refactor that spans a few days, a feature you keep coming back to. The task graph becomes the project's persistent state, independent of any conversation.

I've started treating the task list as the source of truth for bigger projects. Instead of re-explaining everything when I come back to something, I let Claude check the task list to see where we left off. The structure carries the context forward.

Getting Started

Getting into this is pretty simple:

Ask Claude to do something complex

If it creates tasks automatically, let it run

If not, tell it to "break this down into tasks with dependencies"

Hit Ctrl+T to see the task view

Watch it work

For persistence, add this to your shell profile:

export CLAUDE_CODE_TASK_LIST_ID="your-project-name"

That's basically it. The system handles the orchestration, the parallelization, the dependency tracking.

Where This Is Going

Right now you're working with Claude as the main agent. You give it something complex, it breaks the work down, creates a dependency graph, spawns sub-agents to handle the pieces. That's what we've been talking about.

But those sub-agents are just Claude instances with their own context windows. There's no reason they can't use the same task system themselves.

Follow that for a second.

You ask Claude to refactor an entire codebase. It breaks that into subsystems - auth, database, API routes, frontend, tests. Spawns five sub-agents.

Now the auth agent looks at its piece and decides it's still complex. So it breaks the auth work down further - login, logout, sessions, password reset, token refresh. Creates its own dependency graph. Spawns its own sub-agents.

You're three layers deep. Three layers deep:

And nothing stops layer 3 from spawning layer 4. The architecture doesn't have a built-in ceiling - the only constraints are managing context and cost, not capability.

Right now we're at layer 2. But the scaffolding for going deeper is already there.

I've been thinking about what this means for software development more broadly.

For decades the core skill was writing code. Then it shifted to architecting systems. Then to orchestrating teams. Each level meant thinking at a higher abstraction, but the foundation was always the same - somebody was writing the actual code.

That foundation is shifting.

In a couple years, maybe less, the main skill won't be writing code or even architecting systems. It'll be defining problems clearly enough that an agent swarm can solve them. Your job becomes knowing what to build, why it matters, and what success looks like. The implementation - refactoring, testing, debugging, coordinating across services - gets delegated through layers of agents.

This isn't "AI replacing developers" - that framing misses what's happening. The role is just moving up another level of abstraction, same as it does every decade or so. You're becoming the top of a coordination hierarchy that can execute at a scale that would have needed 20 people not long ago.

And here's the thing that keeps me up at night: whoever figures this out early is going to have leverage that's hard to overstate.

Right now if you want to build something ambitious you need funding, a team, months of runway. Soon you'll just need a credit card and the ability to describe what you're building clearly enough that agents can execute. The barrier to building software is collapsing - not in the "everyone can code" way people have said for years, that was always kind of bullshit because most people don't want to write code. This is different. This is the barrier collapsing for people who know what they want to build but don't want to spend six months building it themselves.

That's a different world.

I don't know exactly how this unfolds. But I'd bet three years from now someone ships a production application in an afternoon that takes a team six months today. There might be bottlenecks I'm not seeing, but the direction is clear.

We've been talking about agent swarms for years. This is the first time I've seen the architecture actually work in practice.

The task system looks like a to-do list, but what's running underneath is a coordination layer for hierarchical multi-agent systems. The checklist is just the UI.

You're not managing tasks anymore. You're directing a swarm.

And we're only at layer two.