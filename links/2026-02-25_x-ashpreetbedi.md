---
title: "The 7 Sins of Agentic Software"
source: "https://x.com/ashpreetbedi/status/2026708881972535724?s=46"
date: 2026-02-25
tags: ["agentic software", "AI agents", "distributed systems", "production infrastructure", "failure modes"]
platform: x
author: "@ashpreetbedi"
summary: "The article outlines seven failure modes when moving AI agents from demo to production, emphasizing infrastructure needs for state management, persistence, and multi-tenancy."
---
"Demos are easy. Production is hard" is the most recycled line in AI.

After three years building agent infrastructure, here's the truth:

Production is not the problem.
Distributed systems have always been hard.
The problem is pretending demos represent production.

Demos hide the infrastructure.
They hide state.
They hide cost.
They hide isolation.
They hide the failure modes.

Here are 7 failure modes that show up when demo meets production.

1. Treating a system like a script

The first sin is underestimating the scope of what you're building.

Most agents start as python scripts. You run it locally, it calls a model, runs tools, and returns a response. It works. You demo it. Everyone's impressed.

Then someone asks: "Can we ship this?"

So you wrap it in FastAPI and write endpoints for:

Chat

Session management

Cancellation and resume

File uploads

Auth

One endpoint becomes five.
Five become fifteen.

Then traffic spikes.
Rate limits.
429s everywhere.

Now you are building queues.
Backpressure.
Retries.
Caching.
Cost controls.

Your 200-line demo just became 2,000 lines of infrastructure.

Most agent builders think they are writing isolated programs.
In reality, they are building stateful distributed systems.

2. Forcing agents into traditional request-response

The second sin is assuming traditional web semantics apply to agents.

Traditional software gets a request, does some work, returns a response.

Agents break that contract.

Agents think, stream tool calls, spawn sub-agents, retrieve memory and change direction mid-execution.

Streaming handles latency and is mostly solved.
Start with SSE. Move to WebSockets when you need bidirectional control.

But some tasks require background execution and polling.

"Analyze this dataset and email me a report"

This is a long-running background task. Now you need:

Background execution

Job queues

Progress tracking

Completion guarantees

Add human approval and minutes become days.

Agents are not request handlers. They are long-running computations that may span sessions, humans, and systems.

3. Ignoring persistence

The third sin is ignoring durability.

Demo agents run fresh every time.

Production agents do not.

They live across sessions.

They accumulate context.

They mutate state.

They remember.

That means you must persist:

Inputs and outputs

Intermediate artifacts

State transitions

Execution traces

If your agent crashes on step 12 of 15, you must know exactly where it was.

You need:

Checkpoints

Replays

Resume semantics

Restarting is not acceptable.
Restarting might duplicate a side effect.
Restarting might lose critical context.

But persistence is not only about recovery. Durable state lets you:

Compress context instead of replaying the full history

Debug failures

Extract successful runs into reusable few-shot patterns

Analyze latency, token usage, and tool behavior to optimize cost

Without persistence, every run starts from zero.
With persistence, every run can become cheaper, safer, and smarter.

An agent without durability is a demo.
An agent with durability is a system.

You are no longer serving responses.
You are maintaining long-lived computation.

4. Ignoring multi-tenancy

The fourth sin is ignoring multi-tenancy.

Demo agents serve one user.
Production agents serve thousands.

User A's context cannot leak into User B's experience.

Passing a `user_id` is easy.
Isolating every resource the agent touches is not:

Sessions

Memory

Knowledge

Vector search

Tool outputs

Cached artifacts

Your database was not designed for multi-tenant agent workloads.
Your vector store was not either.
Your model provider definitely was not.

So you build isolation yourself:

Namespaces

Resource scoping

RBAC

Policy enforcement

One missing filter.
One incorrect join.

Now you are writing an incident report.

Isolation is optional in a demo.
It is critical in production.

5. Confusing reasoning with execution

The fifth sin is treating reasoning like execution.

Not every tool call should auto-execute.

"Look up a record" is fine.
"Delete a record" is not the same decision.
"Issue a $50 refund" might be acceptable.
"Issue a $5,000 refund" is not.

If your agent can act, it can cause damage.

Your runtime must express policy:

Which actions are free?

Which require user confirmation?

Which require admin approval?

When an action is blocked, the agent cannot crash. It must:

Pause
Persist state
Wait for approval
Resume exactly where it left off

Not restart.
Resume.
Because restarting might issue the refund twice.

Governance is not a feature.

It is part of the execution model.

6. Assuming horizontal scaling is trivial

The sixth sin is assuming horizontal scaling is trivial.

Agents are stateful.

Cloud infrastructure assumes statelessness.

Spin up more instances.
Load balance.
Any instance can serve any request.

Those assumptions conflict.

The obvious solution:

Externalize all state.
Make the app layer stateless.
Let any instance resume any session.

In theory, scaling is solved.

In practice:

One cached artifact in memory.
One missing write.
One assumption about local state.

It works perfectly on one instance.
You deploy a second.

Now sessions drift.
State disappears.
Runs resume incorrectly.

Behavior becomes unpredictable and only your users can tell.

7. Confusing observability with trust

The seventh sin is confusing visibility with safety.

Agents are non-deterministic. The same input can produce different outputs depending on context, memory, and model behavior.

The industry response has been observability:

Trace everything

Log everything

Run evaluations

Yes, you need all of that.
But observability is retrospective.
It explains what happened.
Trust constrains what is allowed to happen.

That means:

Input validation before reasoning

Guardrails on every step

Output checks before responses

Confidence thresholds that halt execution

Post-response evaluations that catch drift early

The agent should stop itself on a bad call.
Not log it for someone to discover later.

Observability tells you the past.
Trust guarantees correct execution.

These are runtime problems

None of these sins are solved by better prompts.

Calling a model is easy.
Executing a tool is easy.
Returning a response is easy.

Serving agents.
Managing sessions.
Scoping users.
Enforcing governance.
Externalizing state.
Embedding trust into execution.

Those are runtime problems.
Infrastructure problems.
Language problems.

All seven sins come from one mistake:
Treating agents like a feature instead of a new type of software.

The winners in agentic software will not be the best prompt engineers.
They will be the systems engineers.