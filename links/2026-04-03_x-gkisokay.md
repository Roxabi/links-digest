---
title: "I Gave My Hermes + OpenClaw Agents a Subconscious, and Now They Self-Improve 24/7 | Full Guide"
source: "https://x.com/gkisokay/status/2040044476060864598?s=12"
date: 2026-04-03
tags: ["AI Agents", "Self-Improvement", "Workflow Automation", "Hermes", "OpenClaw"]
platform: x
author: "@gkisokay"
summary: "This guide details the architecture for a \u0027subconscious\u0027 agent system that enables Hermes and OpenClaw agents to autonomously self-improve by analyzing past runs and updating their own persistent"
---
You built your Hermes and Openclaw agents to run your workflows, but the more workflows you create, the less time you have to improve them.

That is what the subconscious agent is for.

Much like a human's subconscious, it continuously problem-solves to help your agents self-improve. It brainstorms, debates, refines, and writes the results back into the system so the next run starts smarter than the last.

This is the difference between agents that guess improvements and agents that actually compound.

That means less:

background anxiety

manual ops work

repeated debugging

mental overhead

And more:

shipping

experimenting

compounding

Personally, I built the loop inside my Hermes agent workspace so it could stay close to my main workflows, stay configurable, and stay honest about what it knows.

This guide is meant to be a template for all agents, so you can point your Hermes, OpenClaw, or other agent here and have it build a similar system.

Why This Matters

Most agent systems break in the same boring ways:

They need babysitting

they drift

They burn tokens on vague exploration.

They produce output, but not momentum.

That is the trap. You spend more energy managing the system than using it.

The subconscious agent flips that.

Instead of asking, “What should this agent do right now?” the system keeps asking:

What did we learn?

What failed?

What should we try next?

What needs guardrails?

What should be frozen until it earns trust?

That is how you get a system that saves time, saves energy, saves tokens, and makes the whole stack feel a little bit like magic.

The Architecture

Think of it as a small but relentless loop:

The system gathers evidence from its latest run.

It generates candidate ideas.

It debates those ideas against hard objections with a smarter agent.

It synthesizes one recommendation that can be accepted or rejected.

It writes the result into the state.

The next run starts from that updated state instead of starting from zero.

That last part is the real unlock. Most systems “remember” in a loose, fuzzy way. This one remembers by keeping the winning direction, the rejected paths, and the next improvement in a durable workspace.

So the machine does not just answer. It learns how to answer better.

What You Actually Need To Build It

This is the part people usually skip.

A self-improving agent system needs more than prompting. At a minimum, you need:

1. A runner

Something has to coordinate the whole cycle:

load the brief

fetch current state

run ideation

run critique

run synthesis

write artifacts

hand off the result

In my setup, that is the runner. It is the control plane for the loop.

2. Persistent state

The system needs memory that survives process restarts. That usually means:

JSON for current summaries and governance

JSONL for append-only history

markdown for human-readable outputs

a stable directory structure so later runs can pick up where the last one ended

Without a durable state, the system cannot improve. It just reenacts the same conversation every time.

3. A scheduler or trigger source

You need a way to decide when the loop runs:

on a cron schedule

after new metrics arrive

after a live signal changes

after a manual review request

Please be realistic about how many times you want the subconscious to run on a given workflow each day. Too many runs can lead to excessive divergence from the original principles.

4. A transport or delivery layer

The loop is useless if nobody sees the result. So you need a way to send the output somewhere useful:

Discord (my setup)

Telegram

a file path

a dashboard

a task queue

The transport should be separate from the reasoning layer. That keeps the model from becoming tightly coupled to one output channel.

5. A model router

Different phases should use different models. For example:

cheap/local model for ideation

stronger model for challenge and synthesis

execution model for artifact generation or final writes

That split is what keeps costs sane and quality high.

6. A review and approval gate

If the system can ship directly without a human check, you are no longer building an assistant loop. You are building an autopilot.

This pattern keeps approval at the end, so the system can be smart without becoming reckless.

Of course, it's up to you to decide which tasks and workflows you want to auto-approve, but it's best to test with human approval at the end.

7. Artifact writers

The loop needs to write back into the filesystem in a predictable way. For example:

`ideas/ideas-internal.jsonl`

`debate/debate-log.jsonl.`

`winning-concept.md`

`improvement-backlog.md`

`run-summary.json`

These are the system's memories.

What it actually does in an example

Here is an example of the subconscious trying to think through content to create today. The subconscious layer creates a loop where:

1. `ideas/` stores candidate directions

The subconscious starts by thinking in options, not conclusions. In this case, it is drawing from my Base crypto AI agent research pipeline.

It looks at the evidence and generates a few possible directions. In this run, the options changed, but the mission stayed the same: Base Decision Audit, Base Signal Filter, Base Builder Triage.

That tells you the system is not guessing wildly. It is converging on one thesis: builders want practical decision tools, not more noise.

2. `debate/` stores the challenge and defence turns

This is where the idea gets tested.

The first version was challenged for being too meta, too close to yesterday’s angle, and not specific enough. That pushback matters because it forces the system to make the post more concrete.

The result is a better direction, not a different one: same core thesis, sharper execution.

3.`winning-concept.md` stores the final approved direction

By the end, the system lands on one move: a long-form article that helps Base builders decide what to ship, what to watch, and what to ignore.

The data backs that choice. The dense, utility-heavy posts performed best. The shallow posts did not.

So the recommendation is simple: do not post more. Post something that actually helps a builder make a better decision.

4.`improvement-backlog.md` stores what the next run should sharpen

The system still keeps one eye on what needs to improve next.

The current direction is strong, but it still needs to stay fresh. The next run is asking a useful question: what part of this still feels too familiar, and what would make it sharper?

That is the whole loop in one sentence: keep the win, improve the edge, and make the next run easier to trust.

That means every run leaves a trail:

What the system thought

What it resisted

What survived the critique

What should happen next?

For builders, that is the difference between “AI output” and “AI compounding.”

What changed after I added it

Before this, agents would try to guess improvements and fixes. If the fix is simple, it's not a problem. 99% of workflow fixes are typically easy. But in some cases, they are not always so clear-cut.

In this case, the subconscious became aware of the runtime drift and misalignment of the delivery outputs.

After creating 5 fresh ideas for the fix and debating them with the main brain, the recommended fix is now acceptable and easy for the coding agent to implement.

The Minimum Architecture Diagram

If you were building this from scratch, the stack would look like this:

The important part is the feedback loop. If artifacts do not feed the next run, you have a one-off generation chain.

My model stack

The setup is intentionally hybrid. For local thinking and cheap iteration, I run `qwen3.5 9B` runs locally as the fast ideation engine.

For synthesis and higher-level judgment,` ChatGPT 5.4 mini` handles the challenge, defence, and synthesis passes.

Other solid options include OpenRouter, which routes different models to each process. Also, MiniMax M2.7 is highly sophisticated for only $10/month.

The point is using the right model for the right phase. Cheap local models are great for volume and exploration. Frontier models are great for judgment and consolidation. That mix is what keeps the loop fast without making it sloppy.

What the config is really doing

The config is the policy surface for the system. It should define things like:

Which model handles which phase

How many debate rounds are allowed

What counts as evidence

When to freeze a cluster or idea

How the system should label outcomes

where the outputs should go

The code does the orchestration. The config tells the orchestration what rules to follow.

Minimal folder structure

If someone wanted to recreate the skeleton, this is the smallest shape that still makes sense:

You can rename the folders, but keep the separation:

runner code

persistent state

per-run artifacts

target definitions

human-readable briefs

The guardrails

This part matters more than the “agent magic.” Guardrails are the security layers that keep your workflows intact. It's up to you to experiment with how many or how little you prefer.

So the rules are:

evidence first

explicit states instead of fuzzy opinions

One human approval gate at the end

no automatic promotion from zero-confirmation clusters

One seed may re-enter through a manual review gate.

The next run must write its learning back into the state

This sounds simple, and that is the point.

Minimal pseudo-code

This is the loop in plain pseudocode:

The important part is the order:

inspect state

generate options

Challenge weak ideas

Choose one strong direction, if possible

persist the result

make the next run smarter

If you skip persistence, the loop is broken.

How to make it configurable for your own LLMs

If you want to adapt this for your own setup, do not hard-code the system to a single model or style. Make the loop configurable.

Here is the part you want your LLMs to be able to customize:

What counts as evidence

What the explicit states are

When to freeze output

When to allow re-entry

What the approval gate looks like

What should the next run improve

The point of this guide is to help you build a system that works for you, so there is responsibility on your end to configure this properly.

If you want to try this

If you are building AI agents, vibecoding tools, or any automated workflow, the subconscious layer is worth trying.

It helps you go from “my agents produce stuff" to “my agents improve themselves." That is a much stronger place to be.

If you want to build with people who care about these kinds of systems, join my free Discord community for AI builders.

We are sharing setup ideas, agent workflows, guardrails, and experiments that actually move the stack forward.

Remember to follow @gkisokay and reshare this article if it helps you.