---
title: "Building Agents That Scale: A practical guide to event-driven agent architecture"
source: "https://x.com/jackdishman/status/2039452216730222969?s=12"
date: 2026-04-02
tags: ["AI Agents", "Event-Driven Architecture", "System Design", "Scalability", "Software Engineering"]
platform: x
author: "@JackDishman"
summary: "A practical guide detailing a five-layer, event-driven architecture for building production-grade AI agents that autonomously monitor, reason, and act without human involvement."
---
In preparation for a Farcon presentation, I whipped this together to help jot down things I've picked up along the way in scaling a social agent. Hope you find it useful in building your own agent!

One Request. Twelve Steps. Zero Human Involvement.

A user posts a message on a social platform. Within three seconds, an automated system has read it, classified the intent, validated the user's identity, dispatched an action to a third-party API, logged the result, and replied; all without a single human in the loop.

This is what a production agent looks like. Not a chatbot, nor a standalone script. A program that monitors its environment, reasons about what it observes, and takes action.

I learned most of what's in this post building Clanker - a deployment agent that listens to social media posts, deciphers requests written in plain English, and executes them automatically. To non-crypto readers: think of it as a vending machine that reads tweets and executes financial transactions on demand. To date it's processed tens of millions of API requests and hundreds of thousands of in-feed social conversations. Everything here was learned the hard way.

This is the architecture guide I wish I would've had at the start.

What Is an Agent?

Most of what people call "agents" are chatbots with a personality. A true agent is a program that monitors an environment, makes decisions, and takes action based on what it perceives. It watches a stream of events and continuously reacts.

This is fundamentally different from a REST endpoint that sits idle until a client calls it. An agent has a loop:

Every agent, whether it's deploying tokens, booking flights, or triaging support tickets, runs this loop. The architecture exists to make the loop reliable, cheap, and infinitely extensible.

The Five-Layer Architecture

A production agent isn't a single process. It's five decoupled layers, each with a clear input/output contract and operate independently of one another.

The payoff of this separation is composability. Clanker handles requests from multiple platforms; each with its own schema, auth model, and quirks. The handler chain is identical for all of them though, only the ingestion layer changes. When we added a new platform, we add an adapter, not a new agent.

This also means each layer can fail independently. The queue absorbs spikes so the agent core never capsizes from a massive wave of requests. The action layer can retry failed external calls without re-running the decision logic. When Clanker's deploy queue backs up during a gas fee spike, it simply flushes once conditions normalize; no data loss, no duplicate actions.

Ingesting Events: Push vs. Pull

There are two ways to get events into your queue, and in practice you'll use both.

Webhooks (Push): An external service sends you an HTTP POST in real-time when something happens. Clanker uses webhooks for its primary social platform. Within seconds of a user mention, we receive a payload with the full message, author info, and metadata. The handler should do as little as possible: validate the signature, enqueue the job, return 200. All real processing is asynchronous.

Polling (Pull): A cron job periodically queries an API for new events. Filter by timestamp and check a `processed_ids` table to skip anything already handled. This is the fallback when a platform doesn't offer webhooks or requires a premium tier for them. It adds latency (you're limited to your polling interval) but it's dead simple and often sufficient.

Rule: always validate and enqueue in the ingestion layer. Never execute business logic there. A webhook handler that takes 500ms to respond will eventually be retried by the sender, and you'll process the same event twice.

How Agents Decide: Rules First, AI Second

This is the most important principle in this entire post:

Deterministic rules handle everything they can. LLMs fill the gaps where natural language parsing is truly necessary.

Rules are fast, cheap, predictable, and testable. LLMs are slow, expensive, stochastic, and hard to unit-test. Using an LLM where a regex would do is like hiring a consultant to check whether a number is greater than zero.

Clanker runs every incoming message through a handler chain: a sequence of checks where the first match wins:

Model Cost Optimization: Match Capability to Complexity

This is where most agent builders leave significant money on the table. If every event goes through your most capable model, you're paying frontier prices for tasks a much cheaper model handles just as well.

Principle: classify first, escalate only when necessary.

In practice, the cheapest classifier model handles the routing decision itself. A Haiku-class call that costs a fraction of a cent decides which tier (and which handler) the task belongs to. That classifier call is effectively free compared to what it saves you on mis-routed expensive calls.

Clanker's approach: deterministic rules eliminate the obvious cases first (known commands, spam patterns, rate-limit violations). What's left gets sent to a lightweight model for intent classification. Only requests that require genuine natural language reasoning - parsing open-ended instructions, resolving ambiguity - reach the more capable models.

One trap to avoid: using a powerful model as your entry point "just to be safe." The entry point should be the cheapest thing that can handle classification. Escalate explicitly. Never by default.

Structured Output: From Intent to Action

When you do use an LLM, the model returns free-form text. Your agent needs structured actions it can execute programmatically. The bridge between the two is your ability system.

Present the model with a set of typed tools such as named functions with defined parameter schemas. The model picks which tool to call and returns structured params. The API enforces valid JSON output. No regex parsing or hoping the model follows your format.

One subtlety worth calling out: platform-specific behavior belongs in the handler, not the LLM. The model's job is to parse intent and return a structured action. For example, whether to actually execute that action or deciphering whether to reply on one platform but stay silent on another, is a deterministic `if` statement in the handler. Mixing behavioral policy into your prompts makes it invisible, untestable, and fragile.

Memory: Two Distinct Problems

An agent without memory evaluates every event in isolation. It can't detect duplicate requests, track user history, or resume interrupted tasks. Memory in a production agent means two different things, and conflating them causes bugs.

Task State (Short-Term): A database row with a status field. Every multi-step task and anything that takes more than a single LLM call to complete gets a record with a lifecycle:

Every status transition is a log entry. Every failure is debuggable. When your agent crashes at 3am, you know exactly where it was and why.

Knowledge (Long-Term): This is what separates a one-shot script from a robust agent. Track every processed event by a unique message ID, so if the same event arrives twice (and it will), you skip it. Track per-user request counts, block lists, trusted accounts, and any behavioral state that should persist across sessions. This is also where you enforce idempotency by deduplicating on three layers:

Queue (deduplication IDs)

Execution layer (check processed_ids before acting)

Database (unique constraints on result records).

If two workers race to process the same event, the second one returns the first one's result instead of creating a duplicate.

The Queue Is Your Best Friend

The most important architectural decision you'll make: never execute actions inline. Always enqueue them.

The agent's job is to decide what to do. A separate worker's job is to do it. This separation has compounding benefits:

Parallelism without interference: Run separate queues for separate concerns. In Clanker's case, separate queues per platform and per third-party service. A slow or stuck external process in one queue doesn't block any of the others. This is essential when you depend on third-party APIs that can experience delays outside your control, such as blockchains.

Retry without re-deciding: If the action fails, retry just the action and not the entire perception-decision loop. Your LLM call already happened. Don't pay for it again.

Cost on dedicated infrastructure: Synchronous functions in a queue running on a dedicated worker are significantly cheaper than the same compute on serverless or edge functions billed per millisecond. Batch processing and queue workers are often where the biggest infrastructure cost savings hide.

Visibility: A queue is also a dashboard. Pending depth tells you if you're falling behind. Retry counts tell you if an external dependency is degraded. Dead letter queues tell you when a class of events is permanently broken.

When all retries are exhausted, move the task to a Dead Letter Queue, alert your team, and keep processing. Never let a poison event block the queue. Some inputs will always fail: malformed data, deleted accounts, revoked permissions. Design for this from day one.

Deployment

Match Infrastructure to Workload

Start serverless. Offload expensive or long-running compute to dedicated microservices only as needed. The agent's core logic (ingestion, classification, decision, dispatch) scales fine on serverless. The workers that do heavy lifting get their own infrastructure.

Production Hardening

These are the things that aren't optional once you're handling heavy volume.

Idempotency everywhere: Events will be delivered more than once. Workers will race. Deduplicate at every layer: the queue, the execution check, and the database. If two workers simultaneously process the same event, the second should return the first one's result - not create a duplicate, not throw an error. Build this assumption in from the start; retrofitting it onto a live system is painful.

Timeouts and staged execution: After triggering an action that depends on an external system, don't immediately try to read the result. External systems need time to propagate changes. Enqueue a follow-up job with a delay. If the result still isn't available, retry with exponential backoff. Have a fallback query strategy. Clanker's indexing flow retries with increasing delays before falling back to an alternate lookup method.

Input sanitization: Spammers will probe your agent the moment it's live. Strip HTML and scripts from all incoming content. Define null checks for every field you act on. Common attack patterns include sending the literal string "null" to trigger unhandled edge cases. Sanitize at ingestion and again before any LLM call.

Dead letter queue monitoring: A DLQ is only useful if someone is watching it. Set up an alert that fires when tasks land there. Run a cron job to inspect the DLQ daily and categorize failure reasons. Patterns in DLQ failures are often your earliest signal that an external dependency is degrading.

The Complete Picture

Key Takeaways

Want to see this architecture in action? Tag @clanker on Farcaster or X and watch what happens. -jd

My other writing: https://www.jackdishman.com/writing