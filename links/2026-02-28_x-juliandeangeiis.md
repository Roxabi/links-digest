---
title: "The Coding Agent Harness: How to Actually Make AI Coding Agents Work at Scale"
source: "https://x.com/juliandeangeiis/status/2027888587975569534?s=46"
date: 2026-02-28
tags: ["AI coding agents", "Context engineering", "Agent harness", "Software development"]
platform: x
author: "@juliandeangeIis"
summary: "Success with AI coding agents at scale requires context engineering and a structured harness to manage context windows and ensure reliability."
---
Everyone's building with AI coding agents. Very few are getting consistent results.

The difference isn't the model, the IDE, or the provider. It's the agent harness: the structured system of context, tools, and guardrails you engineer around the agent so it performs reliably, every single time.

The underlying discipline is context engineering: designing and controlling everything an LLM sees before it generates a single token.

The agent harness is context engineering put into practice: the concrete implementation that turns theory into repeatable outcomes.

At MercadoLibre, we are rolling this out across nearly 20,000 developers and thousands of repositories. Here's what we've learned, what works, and what most teams are getting wrong.

Why Context Engineering?

Here's a mental model that changed how I think about AI agents:

Your AI coding agent is a brilliant new hire on day one. Fast, eager, and with zero context about your codebase, your conventions, or your architecture.

You wouldn't just say "fix this bug" or "make this feature" and move on.

You'd onboard them: docs, the tech stack, style guides, release process workflows, access to the right tools, and a mentor to review their work.

That's context engineering: building the system that surrounds the model so it can consistently do its best work.

The Agent Loop and Its Bottleneck

Popular AI coding agents like Claude Code, Cursor and Codex, all share the same fundamental loop:

Read → Plan → Code → Validate → Iterate

The agent reads your files, plans an approach, writes code, runs tests, and loops back if something fails. This loop is powerful, but every iteration consumes from the same finite resource: the context window.

The context window is the agent's live workspace for the current task. Everything the agent can reference at any given moment must fit inside it. And at every stage of the loop, it grows:

The diagram shows how tokens are allocated within a finite context window. System rules stay fixed at the top while tool results and conversation history grow with every turn.

This is the constraint we're engineering around.

System prompt and custom rules: injected at the start of every turn. If the rules aren't useful for the current task, they are wasting space.

Tool definitions: every MCP server you configure adds its schema. More tools = less room for everything else.

The Conversation history: every previous message accumulates linearly.

Tool results: file contents, terminal output, API responses. A single large file read can consume thousands of tokens in one shot.

The agent's own output: the code it writes also lives inside the context window.

Every token spent on a verbose tool result or an overly long rules file is a token not available for the actual code the agent is working on. And as the context fills up, accuracy and recall degrade, often called context rot.

Past a certain point, some studies suggest that around ~60% utilization of the context window capacity, more context makes the agent actively worse.

For more insights about context rot, I found this recent blog: https://www.morphllm.com/context-rot

Even with context windows reaching 1M or more tokens, the fundamental challenge remains.

The best agent harnesses are designed with this reality at the center: inject the right context at the right moment, avoid polluting the window with irrelevant information, and structure long-running tasks to keep it lean.

The Agent Harness: Four Levers You Need to Master

The agent harness is a structured set of controls that shape what the agent knows, what it can do, and how its work gets validated. There are four key levers:

1. Custom Rules (cursor/rules, AGENTS.md, CLAUDE.md, etc.)

This is the most accessible lever and where most teams should start. Custom rules are files that get automatically injected into the agent's context at the start of every interaction.

What goes in custom rules:

Your project's tech stack and architecture patterns

Naming conventions and code style preferences

Testing philosophy ("always write unit tests with table driven inputs")

Common pitfalls specific to your codebase

What NOT to do (anti-patterns you've seen the agent produce several times)

What doesn't belong:

Entire API documentation (too long, wastes context)

Obvious instructions ("write clean code")

Contradictory rules

The key insight: custom rules are living documents. Every time the agent makes a mistake, you may ask the agent how to improve its harness. Over weeks, your rules file becomes an incredibly effective behavioral guide.

Tips for writing effective custom rules:

Keep them under 500 lines. Be precise in your instructions.

Make them modular. Split your rules into focused files by concern: architecture, testing, code, security. This way the agent can load only what's necessary for the task.

Use few-shot examples. Models learn from examples far better than from abstract instructions, but don't overdo it with verbose examples.

Don't make everything always-on. Very few rules need to be injected in every session. Use conditional loading when your tool supports it.  This is where skills complement custom rules: move detailed, context-heavy instructions to skills that activate on demand.

2. MCP Servers (Model Context Protocol)

MCPs are how you give your agent tools beyond reading and writing files. Think of them as plugins that extend the agent's capabilities.

Out of the box, a coding agent can read files, write code, and run terminal commands. But with MCPs, it can:

Query your database to understand schema and data

Search your internal documentation or wiki

Look up internal API contracts

Interact with your CI/CD pipeline

Access design specs from Figma

Test its actual implementation

The power of MCPs is bridging the gap between the agent and your organization's knowledge. Without them, the agent is limited to what's in the repo. With them, it can access the same resources a human developer would.

They're also powerful for validation of the actual agent output, I will talk about the Feedback Loop a bit later.

3. Skills

Skills can give the agent new capabilities and domain expertise. They're the most powerful lever in the harness because they combine context injection with executable logic.

A skill is a directory with a SKILL.md entrypoint that can bundle templates, example outputs, reference docs, and executable scripts.

Only a short description stays in context so the agent knows what's available. The full content gets injected only when the skill is invoked, either by the user (/skill-name) or automatically by the agent when it detects relevance.

This on-demand loading means skills can be as detailed as needed without permanently consuming your context budget.

They come in two flavors: reference skills that inject knowledge (conventions, patterns, domain context) and task skills that give step-by-step instructions for specific actions.

But the real power is that skills can bundle and execute scripts, making the extensibility essentially infinite: from generating interactive visualizations to fetching live CI data. They can also run in isolated subagents with their own clean context window, keeping heavy tasks from polluting your main session.

Skills are programmable, context-aware, composable units of agent behavior.

4. Spec Driven Development (The Ultimate Harness)

This one deserves special attention because it reframes how you interact with agents entirely.

One of the top bottlenecks with the current Coding Agents sits between the chair and the screen: you. This is because of a communication issue.

When people start using coding agents, the average user doesn't specify enough detail, so the agent has to 'predict' the correct implementation.

An example of this: "Make a new feature to add new items from the backoffice".

Seems simple, but doesn't specify anything: tech stack, where is the backoffice, API contracts, where to store the new items.

In this case, the agent will read the current codebase, plan the implementation and may reach to a viable MVP. You add a new item from the BO and it works, also it stores the item in the existing MySQL.

But when you click again on the 'add' button, it inserts the item twice.

'It was obvious' the agent should have managed idempotency by the ID. In our business it's 'obvious' that only one role can insert items.

The issue is not the agent: it's the bare initial input.

Thats one of the main issues that Spec Driven Development comes to solve. So, what is it?

Spec Driven Development (SDD) is the practice of writing detailed specifications before the agent writes a single line of code. These specifications have: what the feature does, how it integrates with existing code, what the edge cases are, what the acceptance criteria look like, and what the test plan is.

Why is SDD context engineering in its purest form? Because the spec becomes the harness.

When you hand an agent a well-written spec, you're not just telling it what to build. You're engineering its entire context window in one shot. The spec consolidates custom rules (architecture decisions), step-by-step guidance, and acceptance criteria (like a review agent), all in a single or multiple artifacts.

The best part: you can use the agent to write the specs too.

I will extend about Spec Driven Development, frameworks, upsides/downsides and how we implement it at scale, on another post.

The Feedback Loop

The four levers above define what the agent knows and what it can do. But there's a piece that sits outside of context engineering and makes the whole system work: the feedback loop. Tests, linters, type checkers, build scripts: every tool that produces a pass/fail signal becomes a feedback mechanism the agent uses to self-correct.

The more structured feedback available, the less 'human in the loop' is needed.

One of the most powerful mechanisms for enforcing this is agent hooks: user-defined commands that execute automatically at specific points in the agent's lifecycle. Wire your validation into a Stop hook, and the agent literally cannot finish until the checks pass. It's not a suggestion it might ignore. It's an enforced gate.

I'll cover the feedback loop in depth in a dedicated post too: hooks, review agents, Stop hook patterns, and how to make the entire agent lifecycle programmable.

How We Do It at MercadoLibre, At Scale

Theory is fine, but reality knocks on the door.

Real scaling requires orchestrating these levers into a system that works across an entire organization.

There are a lot of scale issues to solve: distinct technologies and versions, thousands of (legacy) repositories, multiple knowledge domains and, of course, costs of using it wrong.

We are currently implementing Spec Driven Development, still gaining internal adoption (already for 4000 devs) as it's hard to change developers day-to-day workflows, but I’ll cover it in another post.

Here are some other practices we do:

Standardized Rules for each technology

We maintain a curated set of custom rules at the org level, tuned to all our technologies (9+) stacks, our internal libraries, and our code review standards. Teams inherit this base and then layer on repo-specific rules.

The quality of these rules is critical. Being over specific can break legacy projects. Using an external, unapproved library can cause a security breach.

Internal MCPs for our internal dev platform

We've built internal MCP servers that have internal cloud platform capabilities and context. One of the main MCPs, has the whole toolkit context to use aligned services and internal SDKs.

Internal MCPs that provide business context from RAG results or updated applications documentation.

Custom Code Review Agents

We built standalone review agents that run as part of our CI pipeline. Every PR, whether written by a human or generated by an AI coding agent, gets analyzed automatically before a human reviewer looks at it.

They return prioritized findings, so engineers see the most critical issues first instead of a flat list of comments. Human reviewers can then focus on high-level design decisions instead of catching style violations or missed conventions. Bugs are found before production.

The result: faster review cycles, more consistent code quality, and a safety net that scales with the number of PRs, not the number of reviewers.

The Bigger Picture

Context engineering isn't just a set of techniques. It's an emerging engineering discipline. And the agent harness is its tangible output: the thing you actually build, maintain, and iterate on.

As AI coding agents become more capable, the teams that win won't be the ones using the fanciest model. They'll be the ones with the best-engineered harness: custom rules, MCPs, skills, and spec-driven workflows working together as a system, with tight feedback loops to keep it all converging.

The opportunity is massive. But it requires treating AI agents not as magic boxes, but as brilliant team members that need proper onboarding, tooling, and supervision.

Where can I start? My recommendation would be with the simplest technique: custom rules or skills about best coding practices. Happy engineering!