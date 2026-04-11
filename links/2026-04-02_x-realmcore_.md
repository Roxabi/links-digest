---
title: "Skill chaining and why skills should be actions"
source: "https://x.com/realmcore_/status/2039382343581147414"
date: 2026-04-02
tags: ["AI Agents", "Skill Chaining", "LLM", "Context Management", "Slate"]
platform: x
author: "@realmcore_"
summary: "The article advocates for reframing AI agent skills as dynamic, executable actions rather than static prompts, utilizing the Slate execution model to bridge the \u0027knowledge overhang\u0027 through"
---
This article was mostly crossposted from our blog at https://randomlabs[.]ai/blog/skill-chaining

Introduction

Most agent systems treat skills as manually invoked static prompts. We @0xrandomlabs believe agent skills should more closely mirror the thing they are named after in humans: contextual behaviors that are dynamically used to solve tasks. A skill should be something the agent does not something the agent reads.

In this blog, we discuss the current limitations of agent skills implementations, our reframing, and how we instead decided to implement them in Slate. We also cover the constraints that led to our current design, and how skills can be set up for automation specifically in Slate.

First we'll start with an aside on how slate works.

A brief refresher on Slate's execution model

Knowing how Slate works will be very useful later on, so we are going to start with it here.

Slate takes incremental actions using threads.

An action is a low scope, singular step towards a goal: "Turn on the dev server", "review changes in file X for Y reason", "click through the target path on the agent"

A thread is an isolated worker with its own context window, scoped capabilities, and scoped task execution. It executes a permissioned, scoped task, and returns a compressed representation of its actions. Pssst. For the PLT people, these map relatively closely to continuations in lisp where a thread can be executed partially, returns a state that represents that portion of the execution, and can be resumed later.

To further understand how slate works and how we tackle episodic memory, check out our technical blog here

Ok, onto the actual post.

Background

In humans, skills are learned. We usually see someone else do the task we want to perform, then we attempt to replicate the behavior enough times to internalize it as a context conditioned behavior. We then continue to refine it and reuse it over time.

Skill learning in humans can be seen as mapping to LLM's in the following two ways:

Behavior cloning (of some demonstrated token sequence) during pretraining

Agentic RL during post-training (teaching useful tactics and strategies to the model)

These behaviors are then elicited at test time.

However, without continual learning in LLM's, there isn't much of a pathway to elicit behaviors that the model has knowledge of but doesn't actively choose to employ.

For the purposes of this blog, we can say that all of the strategies and tactics that the LLM doesn't naturally employ are within the knowledge overhang.

Knowledge overhang is the gap between what the model chooses to do and what the model knows how to do. Skills offer a domain specific solution to overcoming this (similar to rules) by directly injecting text that conditions the model to take actions it would not otherwise take on its own despite knowing how to do.

This is where agent skills in particular (alongside good instruction tuning) should be able to meaningfully improve performance since they allow you to introduce instructions that pull that out of distribution knowledge into in distribution behavior. This phenomena is reliant on in context learning.[1]

Rules v.s. Skills

There's a pretty obvious question: why not just do this with rules?

So that everyone reading this is on the same page:

Rules are files that your agent harness forcefully loads into the context, whereas skills follow the principle of progressive disclosure (the agent is given progressively more information about the skill).

The core benefit of this is that since skills are supposed to be context specific, the main agent does not have it's context immediately flooded with a tens of thousands of tokens of conditional instructions that aren't always useful. The prefixed context is a precious resource when effective context lengths are still well below 200k tokens.

The expectation is that the model activates and deactivates skills as necessary, dynamically choosing the out-of-distribution context it needs in different situations. (Codex seems to be the one model that actually does this btw.)

In practice what happens is the user tends to be the one activating the skills.

You'll activate skills manually for the model without any clear lifecycle management apart from activation. More importantly people treat skills, which should arguably be a potential form of hacky continual learning, as slash commands in their terminal agent.

This seems to not be the context scoped behavioral modification that we actually want from skills.

Modelling skills as contextual actions

The definition of a skill aligns more naturally with situationally useful behaviors that are context scoped and don't pollute the main context after use. This is very very similar to how you do less cognitive work to perform skills that you've already mastered.

Skills also seem to map relatively well to the idea of episodic memory. For example, while you are changing a tire on a car, you likely have a clear notion of which step in the sequence you are at. But that's the catch: you've learned a sequence of actions that have built on other learned subroutines which compose into this new skill called "changing a tire" which is now a new isolated context you can work in and remember as an "episode".

Previously all those subroutines were things you were taught in isolation (or maybe in the context of changing a tire) and then you decided to apply them all in a higher order sequence which made you successful at the task.

Learning them entirely on your own would take a lot of work, right? But someone likely taught you either the pieces or the full sequence.

In this way, being taught a skill is similar to giving a model a skill. And being taught how to sequence them is similar to giving the model a skill for how to sequence them.

But to reiterate, there's still a problem here.

The youtuber who made the video you learned from isn't benevolently watching over you and running a slash command to make you remember that you should follow the sequence or look that video back up. You are actually motivated on your own to recall what you need in order to perform the skill and apply it to this target action sequence.

So, thus emerges a better definition of what a skill should be.

Skills should be situational behaviors that are composed into larger sequences where the goal and environment state guide the usage of said skill.

If this is an apt definition and given what we know about Slate, Slate would be the perfect architecture for more natural skill use. Slate's threads provide an ability to dynamically provision permissions, prompts, and isolated contexts for taking scoped actions. Essentially everything you'd want in a permission and execution model for dynamically running skills and adding skills as a way to parameterize threads should be relatively simple.

Building dynamic skill in slate

The first thing we tested with slate was providing the main thread (the "orchestrator") a list of available skills, a way to view and search them, and a parameter for instantiating threads with skills directly.

Slates architecture, in theory, enables it to activate instances of skills while taking actions. An action in this case is simply the sequence of steps that apply a skill!

Wonderful, skills are solved, everything is great, the world is forever changed etc. etc.

Ha. No.

Our initial solution looked something like this:

We gave the main thread a skills tool with the view and list subcommands on top of its orchestration abilities.

It can then directly apply something like a frontend-engineering skill to a thread that it spins up, and that thread, for that episode, will have the skill active. The skill deactivates at the termination of the episode, and the thread's context is cleaned up!

Great, so we have context scoped skill use, and the main agent can activate a skill based on what it knows about the situations in which it should be used.

It actually worked great for things like the default Anthropic frontend skill.

However, there's a core problem: what do you do about user interaction?

There are skills that require user interaction for things like planning, decisions etc.

Here were the options we came up with:

Provide threads a tool to get a blocking popup dialog where the user can directly respond to the agent

Force threads to escalate to the main agent if they need to talk to the user, and use threads to drive the main agent's user interaction

Secret third thing.

Option 1: Direct single use dialogs

How we added this in was by providing a tool to the threads similar to an ask_question tool. The model gets to send the user a message and get a response. This is somewhat similar to a permission request dialog.

The main agent, when providing a skill that required user interaction, could be set up to provision as subagent to chat with a user.

There are two issues:

The UX is awful and would be terrible as a user

The subagent cannot actually reasonably have a conversation with the user

Both of these make interactive/conversational skills nearly impossible

Option 2: Forced thread escalation

This follows a more deterministic failure based approach. Basically we could tell a subagent "Hey, if you are given a task where you need to talk to the user, you actually can't which means you should report the problem to the orchestrator and terminate the episode".

This is obviously bad because the orchestration agent would be spawning a subagent simply for it to run into a wall and then drive the behavior of the main agent.

Not only does it burn cycles and confuse the model, but it also provides an incentive for threads to drive the behavior of the orchestrator.

We have previously gone into the issue with multi-agents and this particular solution where a thread drives the main agent puts them at the same priority level meaning that you need a consensus mechanism and is better just avoided.

Option 3: Secret third thing

We thought really hard. Our smartest friends all got in a room, and discussed exactly what we needed.

And then we realized: what if we changed the execution model?

What if not all threads were driven asynchronously and in parallel?

This line of questioning just so happened to lead to a solution that covers all possible interaction cases, yields an optimal ux, and maintains all the scoped execution benefits of threads.

We updated Slate's execution model to support a new primitive: forking!

Context forking and interactive skill use

NOTE: AS OF APRIL 1, 2026, THIS FEATURE IS IN ALPHA AND HAS BEEN PUSHED BACK TO ENSURE RELIABILITY FOR PROD

Slate previously forced all threads to run in the background which meant that a thread couldn't reasonably interact with the user for a skill.

We added synchronous forking so that the user could continue talking to an agent that was basically the same orchestrator agent, except with the added benefit that once the skill use was done, the isolation and episodic memory would still kick in.

The way this works is that Slate can choose to spawn a fork which then blocks the entire system. This is similar to running a synchronous function.

Forks cannot be continued the way that threads can be, and they immediately block all other actions taken by the orchestrator.

In the UI, they forcefully take over the ui interaction under the hood, which means the UX is just a continuous chat with the agent.

Not much changes for you as a user, but it unlocks interactive skill use.

What does all this buy you?

This buys you skill automation. By changing Slate's implementation model to include forking, it means that Slate's delegation abilities cover all the possible feature requirements for using skills as actions in threads. Since we now generically cover the space of requirements for supporting skills as subthreads, we can then start to orchestrate them.

So, we're also introducing another idea: orchestration skills

An orchestration skill is a skill that you, the user, activate as needed on the main orchestrator agent. Rather than having references to scripts and resources like a normal skill, an orchestration skill should reference... other skills!

The whole point is now you can selectively enable the model to understand the conditional activation sequences for how to use threads, forks, and skills.

You can define something like this:

------
This skill allows you to correctly implement features in the codebase.
Suggest this skill when the user wants to implement a new feature.
------

When this skill is active, you should start by forking and running the `plan` skill.
...
Once the fork has completed the planning process Slate begins implementing the plan.
...
Once you have reviewed the code, verify the output by running the `/qa` skill.
...
Once the `/qa` skill has successfully completed, you should return to the user with the results of the skill use.

Where this skill will teach the sequence of actions that it should execute using all of your other skills.

Plus, because it is again just a skill, you can have multiple different modes of operation with different packages of subroutines defined in the orchestration skill.

The main model can then go ahead and conditionally execute these subroutines in a fairly programmatic way compared to existing harnesses.

No more manually running /review at the end of your sessions!

We're happy to announce that skill chaining is finally released.

Let us know how you end up using these new capabilities or if you get stuck at team@randomlabs.ai

Appendix

The benefits of forking as a primitive in slate's execution model

Forking as a primitive also offers another benefit: as a user you can now directly work with the agent performing the actual work. What this means is you can do all the same high-touch work you would do with any other agent, but only when you need it.

Although this somewhat changes Slate's execution model, we think that the usability benefits here are very large especially while models seem to still have issues with full autonomy on brownfield projects.

Comparisons to an operating system

We find ourselves continuously moving more and more towards using unix and os terminology to describe what we are building. Slate's threads, forking, the thread permission model, viewing context as process memory etc. all seem to follow similar patterns.

It is unclear how this will continue since we are naturally coming to these conclusions.

The only reason this section is here is because the corollary has been brought up as worth pointing out by early readers of this blog and people we run into. And it was suggested to us that we take note of this explicitly as an interesting aside.

References

Kojima et al.: Large Language Models are Zero-Shot Reasoners (NeurIPS 2022)