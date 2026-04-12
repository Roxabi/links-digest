---
title: "The Modern AI PM in the age of Agents "
source: "https://x.com/Saboo_Shubham_/status/2008742211194913117"
date: 2026-01-07
tags: ["AI agents", "Product management", "Problem shaping", "Context curation"]
platform: x
author: "@Saboo_Shubham_"
summary: "The role of product managers is shifting from translating customer needs to engineers to forming clear intent for AI agents, making problem-shaping and context curation critical new skills."
---
The job of a PM used to be translation.

You talked to customers, synthesized their problems, wrote specs, and handed them to engineers. You were the bridge between "what people need" and "what gets built." The value was in that translation layer.

That layer is compressing.

When agents can take a well-formed problem and produce working code, the PM's job shifts. You're no longer translating for engineers. You're forming intent clearly enough that agents can act on it directly.

The spec is becoming the product.

I've watched this happen with myself and dozens of other PMs. Previously, a PM would write a detailed spec, hand it off, wait for questions, clarify, wait for implementation, review, give feedback, iterate. The cycle took weeks. Now they write a clear problem statement with constraints, point an agent at it, and review working code in an hour.

The time between "I know what we should build" and "here it is" collapsed. But the work of knowing what to build didn't get easier. It got more important.

You don't need to write the code yourself. You need to know what you want clearly enough that an agent can build it. The spec and the prototype are becoming the same thing. You just describe what you want, watch it take shape, course-correct, and iterate. The bottleneck isn't implementation anymore.

And the speed of shipping is only accelerating.

I've been at Google for around 3-4 months and it feels like we've shipped years' worth of AI progress. In that window alone: Gemini 3 Pro and Flash, the Multimodal Live API, Nano Banana Pro, Deep Research Agent, Google Interactions API, ADK Java/Go/TypeScript and so much more.

Every big and small AI company is shipping at this pace, thanks to AI coding agents. The cycle times that used to define product development, from quarterly planning, monthly sprints, to weekly releases are compressing into something closer to continuous deployment of ideas.

When the implementation barrier drops this fast, the bottleneck shifts upstream. The scarce resource isn't engineering capacity anymore. It's knowing what's actually worth building.

The new PM skillset

Problem shaping: The best PMs I know have always been good at this, but it used to be one skill among many. Now it's THE skill. Can you take an ambiguous customer pain point and shape it into something clear enough that an agent or team of agents can act on it? Can you identify the constraints that actually matter? Can you articulate what success looks like?

The spec isn't a document anymore. It's a well-formed problem with clear boundaries.

Context curation: This is the skill nobody talks about, but every PM who's effective with agents has developed it. The quality of what an agent produces is directly proportional to the context you feed it.

When I first started working with agents, I'd give vague prompts: "build me a dashboard for customer feedback" I'd get something that technically worked but missed the point entirely. It didn't understand our users, our constraints, what "good" looked like for us.

Now I maintain context docs that I feed to agents before starting any project. Over time I've figured out what actually matters in these docs:

The user, specifically. Not a persona. Real details: who they are, what they care about, what makes them give up, what makes them pay attention.

The problem in their words. Direct quotes from calls, tickets, or sales notes. Their language, not your synthesis. This grounds the agent in real pain, not abstracted pain.

What good looks like. Examples your team considers well-designed. Your own past work, competitors, adjacent products. Show, don't describe.

What you've tried and why it failed. Institutional knowledge that usually lives in people's heads. The approaches you've already killed and the reasons why.

Constraints that shape the solution. Not every constraint. Just the ones that will actually change what gets built.

How you'll know it worked. Concrete, not fuzzy. Something you could actually measure or observe.

When I ask an agent to prototype something now, it's not starting from zero. It knows who we're building for, what they actually said, what good looks like, and what's already failed. The output fits because the input was specific.

Evaluation and Taste: Taste is underrated. But when agents produce output quickly and in bulk, it becomes the most important skill. Is this actually solving the problem? Does it handle the edge cases that matter? Is this the version we should ship or just the version that runs?

This is harder than it sounds. Agents will confidently produce things that look correct but miss the point entirely. You need reps to develop the taste.

There's no shortcut: you have to build things, evaluate them, learn what "good enough to ship" actually feels like versus "technically works."

The mental model shift

Here's how I think about it now:

Old model: PM figures out what to build → writes spec → engineers build it → PM reviews → iterate

New model: PM figures out what to build → PM builds it with agents → PM evaluates → iterate quickly → (when they like it) hand to engineers to go live in prod

The AI PM isn't just handing off requirements anymore. They're vibing the first iteration themselves and getting real feedback on working software, not slide decks or Figma mocks. Engineers then become collaborators on making the product better and production-ready rather than translators of your intent.

This changes your relationship with the product. You're not describing what you want and hoping it comes back right. You're shaping it directly, in real time.

Think in iterations. Let the first version be wrong. Don't try to get it perfect in your head before you start. Give the agent rich context about the problem, then let it take a rough first pass. See what comes out. React. Iterate. You'll learn more from "that's not quite right because..." than from trying to think through every edge case upfront.

I regularly have agents build two or three completely different approaches just to see which one feels right when I use it. That used to be expensive. Now it's a Tuesday afternoon with a few parallel agents.

Hold ambiguity longer. Old PM instinct was to resolve ambiguity into specs as fast as possible. New instinct is to stay in the ambiguous zone while you explore. Don't collapse to a solution too early. Let agents help you understand the solution space before you commit.

Getting started

If you're a PM who hasn't worked this way yet, here's how to start:

Pick a small problem you actually have. Not an imaginary one. Something that's annoying you right now. A report you have to manually compile. A workflow that's tedious. A prototype you wish existed.

Spend 30 minutes writing context before you prompt.  See the context curation section above for the full list.

Point an agent at it and watch what happens. Don't expect perfection. Expect a starting point. React to it. Guide it. Iterate.

Do this ten times. With different problems. Different levels of complexity. You'll develop intuition for what works, what context matters, how to evaluate output. This intuition is the new PM skill.

The PMs who will thrive are the ones who understand problems so clearly that the solution becomes obvious to them and to the agents they work with.

I switch between AI Studio, Cursor, Antigravity and Claude Code depending on the task. The tool matters less than building the muscle of working with agents daily.

Lastly, I'll leave you with this...

If your job was mostly translating customer needs into documents for engineers, that's a workflow. Workflows get automated.

If your job was "understand problems so deeply that the right solution becomes obvious," you're more valuable than ever. Agents amplify that understanding into shipped product faster than any team ever could before.

The question every PM should ask: when the translation layer disappears, what's left?

For the best PMs, the answer is everything that actually mattered.

Understanding the problem. User empathy. Judgment. Taste.

These were always part of the PM job. Now they're becoming the whole job!