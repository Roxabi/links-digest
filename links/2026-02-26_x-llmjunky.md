---
title: "CODEX MULTI AGENT PLAYBOOK: SWARMS LVL. 1"
source: "https://x.com/llmjunky/status/2027032974202421336?s=46"
date: 2026-02-26
tags: ["multi-agent systems", "swarm orchestration", "agent planning", "subagent coordination"]
platform: x
author: "@LLMJunky"
summary: "This guide teaches how to effectively plan and orchestrate multi-agent swarms by emphasizing clear specifications, dependency mapping, and proper context management."
---
Greetings learners! Welcome.

In Part 1, you learned what subagents are, how they work under the hood, and the key differences between Orchestrators and Workers that you need to understand before putting them to work.

In Part 2, you learned how to define custom agents, assign models and reasoning levels, and write the prompts that tell the orchestrator when and how to spawn each role.

In many cases, you're going to want to define agent roles so that you can plan with one model and execute with another. Everything we covered before feeds directly into what we're building here.

You can download Custom Agent Roles here.

Now it's time to put all of that together. This is the part where things get fun.

Swarms are what happen when you stop thinking about subagents as a novelty and start thinking about them as a workforce.

Instead of one agent grinding through random tasks, you're coordinating multiple agents executing in parallel, each with its own clear scope, working toward the same goal.

But here's the thing: throwing a bunch of agents at a problem without a strategy is a recipe for conflicts, wasted tokens, and slop. The difference between a swarm that works and one that doesn't comes down to three things: how you plan, how you orchestrate, and the quality of the context you give your agents.

That's what this guide is about. Let's get into it.

The Plan.md

First things first: for you to get the most out of swarms, your planning has to be exceptional. Ambiguity is your enemy. Every unclear requirement, every vague acceptance criteria, every "figure it out" you leave in the spec is going to multiply across however many agents you launch.

One agent drifting is annoying. Five agents drifting in parallel is a disaster.

If you're not confident in your ability to select the most optimal frameworks and tools, here's a tip:

When the agent stops during the planning process to ask you clarifying questions. Instead of blindly accepting the first option on every question, stop.

Take your time to understand the gravity of those choices. Open another agent session. Tell it what you're trying to build and ask it to explain the options to you:

"Help me choose the best tech stack for my product. Ask me questions and guide me to the most optimal solutions"

Be part of the process. This is how you learn. It's much easier to do early research than pivot to something else after you've already built it.

The majority of your time should be spent developing a careful and detailed spec that you know intimately and have crafted with intent. It's okay to have the agent recommend suggestions, but you should at least try to understand their function, and use your best judgement to move forward.

If you're running swarms, you are the architect. The agents are the builders. An architect who doesn't understand the blueprint is likely to end up with a token-expensive mess.

The Swarm Planner Skill

With that out of the way, I built a special skill for planning. For implementing using swarms, it is a helpful resource. And helpful resources can be found at the bottom of this blog.

The "swarm planner" skill was designed to stop and ask questions any time the model detects ambiguity, but the primary benefit is that it will build dependency maps into your plan - which will come in handy later.

If you would like to opt for your own planning methods, you can simply add this to your prompt instead. It will add a dependency map to any plan:

Orchestration

The orchestration layer is the most important aspect of utilizing swarms. Because you have spent a great deal of time formulating a high-quality plan, there's already a great deal of vital context in the context window.

I recommend you do not reset context before implementing the plan.

If your context is low (less that 40% left), you can opt to compact, but because you're using subagents, the parent session will not use a great deal of tokens.

The orchestrator serves these critical functions:

Manage the state of plan implementation

Call subagents as needed

Provide subagents their prompt

Validate the subagents' work

Resolve conflicts

Ensures the project is continuously moving forward towards success

Because the orchestrator understands the full scope of the plan, it is uniquely positioned to prompt subagents. And that is one of its most important functions.

In addition to the plan, the orcs manage the state of every single agent, all the file names and paths, as well as the overall state of the project itself directly in its context window. It knows who, what, where, when, why, and how. 

It doesn't need to worry about the minutia, think of it like a foreman on the job. It's role is to make sure the project moves along the right path, and to fix any problems when they come up. 

And that is exactly what makes it so incredibly powerful.

I typically employ one of two strategies for implementation: Swarm Waves and Super Swarms. Which one you choose depends on how much you value accuracy vs. speed.

Swarm Waves

Swarm Waves launch one subagent per unblocked task, in waves. If you want to ensure the highest level of accuracy and the fewest tokens burned, this is the safest path forward.

With this method, if there's only one unblocked task, it will only launch one agent. If there's eight unblocked tasks, it will launch eight agents. Simple.

Similar to Ralph Loops, the orchestration layer will loop over the plan to look for unblocked tasks, and continuously launch new agents as their dependencies become unblocked, until all tasks are done.

This creates the fewest conflicts, because every task that depends on another task will be done in the expected order.

If you remember, in the planning phase, we already created a dependency map, so the orchestration agent knows exactly which tasks can launch in parallel at any given time.

Super Swarms: Total Parallelism

Another strategy is to launch as many subagents as your machine can handle at once, regardless of dependencies.

This method is really fast, and just as fun.

If you go this route, skip the dependency map. Explicitly guide the orchestrator to launch as many agents as you have configured in your config file.

Note: Codex has a base max of just six parallel agents at one time. To increase the number of parallel agents Codex is allowed to call at one time, increase the `max_threads` count in your config file.

This example would allow you to launch up to 16 subagents at once.

Note: There is a point where too many agents may cause 429 errors. If this happens, reduce the max_thread count.

Because all/most tasks are being done in parallel, this will lead to increased conflicts. It is a challenge for Codex to write a file with dependencies when the dependee does not yet exist. But, it's not impossible.

In fact, with good context, we can avoid a lot of problems.

In my testing, I have found that the orchestrator agent is quite adept at identifying these conflicts in real time, and handling their resolution on the tail end of the plan's implementation.

But we need to do more than just launch subagents. We need to ensure the results are the highest quality we can get on the first pass. If we take the time to get the details right, it can be the difference between a disappointing result and a genuinely good result.

Or at the very least, good for a first pass. You're always going to have to iterate on the details to make something truly great.

The Secret Sauce: Context Engineering

I'm not using this as some fancy buzzword, although it is.

This is what makes or breaks your parallelism. To get the best result from your subagents, you need to ensure that each agent is getting the optimal context to ensure the highest quality outcomes.

Now, Codex does a pretty good job at prompting subagents in general, but we can take it further. We don't have to leave it up to chance. We can dictate exactly what our agents are prompted, when they are called, and what they should be used for.

That is important. I believe that by giving our orchestration agent guidelines to follow when calling subagents, we can reliably get consistently high quality outcomes when invoking agents. And we do this by "front loading" the subagent's context with every meaningful detail we can provide.

This is especially important when using a small & fast model like Spark because it will reduce the number of tool calls it needs to do to gather context for a task, and its reduced accuracy is far less of a factor when its been given the entire roadmap for success up front.

No guessing. No ambiguity. Just clear, up-front instructions and acceptance criteria.

This allows accomplishes two things:

It allows your orchestration agent to fill a very specific role: to keep the project moving, clear conflicts, provide context, call agents, and review outputs. They are the orchestrator's only responsibilities.

And because of this, you can extend your context window incredibly far. 

Secondly, front-loading detailed context saves tokens.

This is how you utilize agents like Spark, which only have a 128K token context window, to your advantage.

Spark is not good for long context tasks, or back and forth conversation. What is IS good at, though, is completing singular tasks. When you give a Spark subagents clearly defined and well-documented tasks, they shine. 

In short, taking time to control and manage the context  your orchestration agent is providing to each subagent, will set them up for success. Don't leave it to chance. Craft the context framework yourself.

How to Control Subagent Prompts

Well, good news for you. That's the easy part. Codex is the most steerable model on the planet. If you tell it to do something, it will.

Thus, I've created a skill that makes this as simple as invoking it. But rather than just tell you "hey, use this skill," I'd really like it if you actually read it. This is not the entire skill (though you should also read that, too), but it is the most important part to this conversation.

This is the subagent prompt template. It is given to your orchestrator as the framework to create its prompts for your subagents. It provides essentially every meaningful detail an agent could be given as the initial prompt.

All of the [bracketed sections] are variables that your orchestration agent will automatically provide every subagent.

In this template, you will see careful and deliberate guidance for both your orchestrator to fill out the necessary information, as well as the subagent on exactly how it should complete its task.

There's no gaps. No ambiguity. Just thorough and clear guidelines on what it should do, where it should look, and what is expected of it before it yields.

Why This Framework Works

Your agents have amnesia, so if you set one off in your codebase with minimal context, it will have to call many tools, read many files, to discover context before it can start work. Furthermore, this is potentially ambiguous, which may lead to drift.

With this template, every agent understands:

What the task is and why it exists within the larger spec

Which files it depends on (full paths and expected contents)

It knows where the plan is, and is instructed to read it.

State of the project (within the plan & commits)

It knows the filenames it needs to work on, and its paths.

Which other tasks it relates to, and their function.

Acceptance criteria and testing methodology

Step-by-step implementation instructions

This is how you set your subagents up for success.

By ensuring we give clear and comprehensive up-front context, it will use fewer tokens and tool calls in the initial exploration phase. As mentioned before, this is especially crucial when using small/fast models like Spark.

A Note on Model & Reasoning

What model should I use? What reasoning level?

I want to answer a quick question that will undoubtedly come up on how to use this method effectively. The answer will depend on what type of subscription/API limitations you have.

The only hard rule I have is that you should be using one of the larger models for orchestration.

My general strategy is as follows.

Pro Subscriptions:

Plan with GPT 5.2 High or 5.3-Codex High (once GPT 5.3 releases, I'll probably use that)

Orchestrate with 5.3-Codex High

Subagents with Spark xHigh or 5.3-Codex High

Plus/Business Subscriptions:

Plan with GPT 5.2 High or 5.3-Codex High

Orchestrate with 5.3-Codex Medium

Subagents with 5.3-Codex Medium

The great news is, you can now configure all of this in your config file so you don't have to swap any of this around manually. Once you decide on the system you'd like to use, Codex can manage it all for you.

In the example above, it will plan on Codex 5.3 xHigh, Orchestrate on High, and if you want to implement with Spark, you would use my "Sparky Skills" to implement the plan.

You can customize this to your liking. To get "Sparky" agent role definition, head over to my Github.

The default subagent worker uses Codex 5.3 Medium by default, so you don't need to configure any agents if you just want to use the base.

Damn that was long

If you made it this far, you must really want to learn. I'm impressed. I know this is a lot of information to digest, but I assure you that once you get in there and start getting your hands dirty in Codex, it's all fairly straightforward.

There are many strategies and layers to using multi-agents, and this was just the first. You can create much more complex systems that take these skills to the next level, and in future blogs, I will cover some of these systems. But for now, I wanted to start with the more digestible basics.

This is now my preferred way to code. I don't want you to walk away from this and think you need to use subagents. It is not necesssary. You can do everything you need to do inside of single agent sessions, but I think once you learn to wield them properly, they are a really great tool to speed up your workflows.

The other reason I enjoy them is because as good as Codex is at compaction, I love that you can build these rather complex apps/systems inside of single sessions without needing to compact often (or at all). It truly enables some horrendously long-horizon tasks if you create the right scaffolding.

It's rather beautiful to watch it work.

Demo: Kanban Built With Spark Swarms

I didn't want to leave you with just a wall of text, so I implemented a quick app that I've been wanting to build for myself: a personal task manager for my day-to-day workflow.

I used Codex 5.3 High to plan and orchestrate, and Codex 5.3 Spark High to implement the 7-phase plan. Now, Codex can create and manage tasks for me in my own private ClickUp app, all built with very little effort.

The fun part of this particular test is that it wasn't a perfect run. I steered it regularly, and one of the agents seemingly got stuck committing its work (it would have eventually cleared itself). On top of that, I was trying something new: having the orchestrator write tests before it called a subagent, so that the Spark agent had a test it needed to make pass before yielding.

I had never done it quite like that before. Previously, I always let the orchestrator test the subagent's work after they were done. Unfortunately, I forgot to put that in the original prompt, so I quickly had to steer Codex to write the tests before calling the agents.

And you know what? It worked fantastic. I believe I will be using this method moving forward as more Test (First) Driven Development.

That's the beauty of this tool. It's highly intelligent and highly collaborative. Not some rigid calculator.

So long story short: you got to see how both myself and Codex were adapting on the fly. That's a real-world example of how you can, and should, still be part of the process.

To get access to my custom Agent Roles, and Skills, including the ones mentioned in this blog, visit my Github at https://github.com/am-will/codex-skills.

To understand how to use the Swarm Planner and Parallel Task skills, I highly recommend you read the README here: https://github.com/am-will/swarms

If you enjoyed this content, please do me a huge favor and hit all the bottons on the bottom of this post. Like, share, bookmark, comment. All the things. Let me know what you liked, didn't like etc. It takes a great deal of effort to write something like this, so your support would mean a ton.

-Will