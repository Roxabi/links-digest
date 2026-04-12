---
title: "🔑 you're using opus 4.6 wrong"
source: "https://x.com/godofprompt/status/2020499426389741784?s=46"
date: 2026-02-08
tags: ["AI workflow systems", "Claude Opus 4.6", "productivity automation", "prompt engineering", "compounding workflows"]
platform: x
author: "@godofprompt"
summary: "The article explains how to use Claude Opus 4.6 effectively through a five-step connected workflow system rather than isolated prompts."
---
everyone's posting Opus 4.6 benchmark comparisons.

cool. now show me the workflow.

i've been running Claude Opus 4.6 since launch. not benchmarking it. not testing trivia questions. running actual work through it, every day, for real output.

and here's what i realized after the first few days: individual prompts are a dead end.

one prompt gives you one output. you tweak it, get a slightly better output, and move on. next day you're starting from scratch again. there's no compounding. no system. just isolated moments of "that was pretty good."

the people getting real results aren't using prompts. they're running systems.

so i built one. five prompts that connect into a loop. each one feeds the next. the system gets smarter the longer you run it because context accumulates, patterns emerge, and Claude starts anticipating what you need before you ask.

here's the entire system, prompt by prompt, with the honest breakdown of what works and what doesn't.

the foundation: why a system beats a prompt collection

before the prompts, let me explain the architecture.

most people collect prompts like recipes. they bookmark 47 of them, use 2, forget the rest.

a system is different. it's a connected workflow where the output of step 1 becomes the input for step 2, and the insight from step 5 feeds back into step 1.

here's the loop:

step 1: AUDIT. figure out what's actually draining your time and energy

step 2: ARCHITECT. plan the solution before building anything

step 3: BUILD + REVIEW. execute and quality-check in one pass

step 4: REFINE. run the output through a convergence loop until it hits your bar

step 5: COMPOUND. weekly review that stacks improvements and feeds back into step 1

each step has one prompt. the prompts are designed to work together but each one is independently useful too.

you don't need to run all five from day one. start with prompt 1. add one per week. by week 5, the full loop is running and compounding.

i'll also give you the honest take on Opus 4.6 at the end. what's genuinely better, what's the same, what's worse. no hype.

let's build.

step 1: THE AUDIT (find what's actually worth automating)

this is where most people skip straight to "give me a cool prompt." wrong move. if you automate the wrong thing, you just made a fast version of something that shouldn't exist.

this prompt turns Opus 4.6 into a productivity analyst that maps your actual workflow, scores each task by energy drain and automation potential, and hands you a prioritized 4-week plan.

the key difference from a generic "help me be productive" prompt: it scores tasks on TWO dimensions. time consumed AND mental energy drained. sometimes a 15-minute task that sits in the back of your mind all day is worth automating before a 2-hour task that doesn't bother you.

here's the prompt:

when i ran this on Opus 4.6, something interesting happened. previous models would ask surface-level questions like "what's your job title?" Opus 4.6 asked things like "of the tasks you mentioned, which one do you find yourself thinking about even when you're not working on it?" That's the energy drain dimension at work. it's mapping the invisible cost, not just the visible one.

the adaptive thinking in Opus 4.6 matters here. it doesn't apply the same reasoning depth to "what time do you start work?" as it does to "how should we prioritize automation of your content pipeline vs your client onboarding?" simple questions get fast answers. complex tradeoff analysis gets genuine deliberation.

if you automate just one task per week using this plan, you'll have 4 workflows running within a month. in 3 months, 12. you'll be ahead of 99% of people still bookmarking "top 10 ai tools" threads they'll never read.

step 2: THE ARCHITECT (plan before you build)

here's where most people waste hours. they jump straight into building, hit a wall, backtrack, rebuild, hit another wall.

this prompt turns Opus 4.6 into a solution architect that creates a complete implementation blueprint BEFORE you write a single line of code or set up a single automation. it asks the questions a senior engineer would ask in a design review.

this one is especially powerful with Opus 4.6's 1M token context window. you can feed it your entire codebase, documentation, or project context and it actually holds it all in working memory while designing the solution.

the architecture prompt is the one people skip. and it's the one that saves the most time.

i used this to plan an automated content pipeline last week. my first instinct was to build a complex multi-tool workflow with Zapier, a database, and three different APIs. the Architect prompt mapped three approaches. the simplest one, a Claude-native workflow with a single Google Sheet as the database, handled 90% of my requirements. took an afternoon instead of a weekend.

that's the value of planning: you avoid building the complex thing when the simple thing works.

step 3: THE ANALYST (build and review in one pass)

this is the engineering prompt. works for code reviews, vibe coding projects, automation debugging, or any technical build.

the key design choice: instead of asking Claude to "review my code" (vague, produces generic feedback), you embed your actual engineering standards directly into the prompt. Claude reviews like a senior developer who knows how YOU think about quality.

i restructured this from a framework that's been circulating in the Claude Code community. the original was solid but overbuilt for most users. this version is tighter and works for both experienced developers and vibe coders.

Opus 4.6 handles this prompt noticeably better than previous models. the adaptive thinking scales its analysis depth to the complexity of the code. a simple utility function gets a quick review. a complex state management system gets deep analysis with genuine tradeoff reasoning across multiple concerns.

tip: customize the "engineering standards" section to match YOUR actual preferences. that's the difference between generic feedback and feedback that feels like a collaborator who knows your codebase.

for vibe coders who aren't writing code directly: this works equally well for reviewing code that Claude Code or Cursor generated for you. paste in what was generated, run this review, catch problems before they compound.

step 4: THE REFINERY (recursive improvement until convergence)

this is the pattern that makes everything else better. the concept: instead of generating once and shipping, you tell Claude to generate, score its own output against specific criteria, diagnose what's weak, rewrite, and re-score until it converges on quality.

i rebuilt this from a marketing framework into a clean, reusable system. the key improvement: it tracks the delta between versions so you can see exactly what changed and why. it also detects when it's hit diminishing returns and stops instead of endlessly rewriting.

here's how to customize the scoring criteria for different work:

for writing or content: hook strength, clarity and flow, specificity (named examples, real numbers), emotional resonance, actionability

for code: correctness, readability, edge case handling, performance characteristics, test coverage

for research or analysis: source quality, depth of reasoning, practical applicability, logical structure, intellectual honesty

for emails or outreach: tone calibration, brevity, clarity of ask, personalization, professional warmth

Opus 4.6's adaptive thinking makes this loop actually work. on previous models, the "self-scoring" was often performative. the model would say "7/10 on specificity" and then rewrite with the same level of specificity. Opus 4.6 genuinely engages deeper reasoning to diagnose root causes in its own output.

when i tested this on an article draft, v1 scored 6/10 on specificity. the model diagnosed the problem as "using generic category references instead of named companies and data points." v2 replaced generic examples with specific named sources and concrete numbers. v3 hit 9/10. the self-diagnosis was accurate, not theater.

step 5: THE COMPOUNDER (the weekly review that makes the system smarter)

this is the prompt most people would never think to build. and it's the one that turns five isolated prompts into an actual system.

every Friday (or whatever your review day is), you run this prompt. it reviews what you automated that week, what worked, what didn't, and plans the next week's automation target. over time, it builds a pattern library of what works for YOUR specific workflow.

this prompt leverages Opus 4.6's context management features. with the 1M token context window, it can hold several weeks of review history in a single conversation. the context compaction feature means it automatically summarizes older reviews to preserve space for new ones without losing the important patterns.

the compounding effect is real. week 1, you have one automation saving maybe 2 hours. week 4, you have four saving 6-8 hours. week 12, you have a dozen micro-systems running your workflow and Claude knows your patterns well enough to suggest automations you hadn't considered.

how the system connects

the five prompts aren't random. they form a cycle:

THE AUDIT identifies what to automate

→ THE ARCHITECT plans how to build it

→ THE ANALYST reviews what you built

→ THE REFINERY polishes the output quality

→ THE COMPOUNDER reviews the week and feeds insights back into the next AUDIT

each prompt makes the others better. the Architect creates cleaner plans because the Analyst's review standards are embedded in your thinking. the Refinery produces better output because the Audit identified the right tasks. the Compounder detects patterns that improve future Audits.

that's the difference between a prompt collection and a system. prompts are isolated events. systems compound.

the honest take on Opus 4.6

after running real work through it for weeks, here's where i landed:

what's genuinely better:

adaptive thinking is real. the model dynamically adjusts its reasoning depth based on task complexity. ask a simple question, get a fast answer. give it a complex multi-step problem, it actually deliberates.

this isn't marketing language. you can feel the difference in how it handles the Analyst prompt on simple vs complex code.

the 1M token context window changes what's possible for large projects. feeding an entire codebase into the Analyst prompt, or maintaining weeks of review history in the Compounder, simply wasn't feasible before. context compaction helps too. it automatically summarizes older conversation turns to preserve space without losing critical decisions.

sub-agent orchestration is a quiet upgrade. when you give Opus 4.6 a complex task, it recognizes when parts of the work would benefit from being delegated to specialized sub-processes. you don't have to prompt for this. it just does it.

what's about the same:

standard writing tasks, basic Q&A, simple content generation. if your workflow is mostly "write me a caption," you won't notice a meaningful jump. the improvements show up on complex, multi-step, reasoning-heavy tasks.

what's worse:

some users report that the optimization for precision and structured reasoning makes freeform creative output feel more mechanical.

if you want pure creative writing, test it against Sonnet before committing. also, pricing scales significantly past 200K tokens. the 1M context window is powerful but not free.

the pattern holds with every model release: about 20% of workflows genuinely improve. the other 80% stays the same. the people who benefit aren't the ones reading every benchmark thread. they're the ones who run 5 real prompts and make a decision in 30 minutes.

why this works (and why most prompt collections don't)

the problem with "500 prompts for ChatGPT" lists: they optimize for breadth. one prompt for emails. one for code. one for recipes. no connection between them. no compounding.

this system optimizes for depth. five prompts, tightly connected, that get better the longer you use them.

the uncomfortable truth about AI productivity: the tool doesn't matter nearly as much as the system around it. people chase the latest model release looking for a magic upgrade. the real upgrade is building a workflow that compounds regardless of which model you're running.

Opus 4.6 is the best model i've used for this system. but the system works on GPT-5.2 too. and it'll work on whatever ships next quarter. because the architecture is model-agnostic. the intelligence compounds in the workflow, not just the model.

start here

don't try to implement all five prompts today. that's how systems die.

here's the actual sequence:

week 1: run the Audit prompt. identify your top 4 automation targets. automate the easiest one.

week 2: run the Architect prompt on your second target. build it.

week 3: use the Analyst prompt to review what you built in weeks 1-2. fix what's broken.

week 4: run the Refinery on your most important output. see the quality jump.

week 5: run the Compounder. review everything. plan the next month.

if you automate one thing per week, you'll have 12 workflows running in 3 months. most people reading this will bookmark it and never start. the ones who run Prompt 1 tonight will have a completely different relationship with their workload by March.

copy the prompts. customize the criteria to your actual work. keep what's better, ignore what isn't.

that's the whole system.

p. s. if you want to see more AI tips & workflows, subscribe to my free newsletter here.