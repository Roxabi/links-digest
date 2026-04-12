---
title: "You've set up OpenClaw, Now What? Why skills beat agents - and save you thousands in fees."
source: "https://x.com/jordymaui/status/2024251460553199935?s=46"
date: 2026-02-18
tags: ["AI agents", "skills vs agents", "context management", "token costs", "multi-agent systems"]
platform: x
author: "@jordymaui"
summary: "Using skills within a single AI agent is more effective than running multiple agents, as skills preserve context and reduce coordination costs."
---
I had 8 agents running at the same time. An Opus "brain" coordinating Kimi agents for writing, development, design, research. Each one with its own API key, its own context, its own bills. It looked like the future.

It was a mess.

Agents forgot what other agents were doing. Context got lost between handoffs. I was spending more time managing the agents than actually getting stuff done. And the cost? Don't even ask.

If you read my last article, you've got OpenClaw running. You've got your bot talking to you on Telegram or Discord. You've filled out SOUL.md and USER.md. Your agent knows who you are.

Now, before you keep reading - please stop, give this a bookmark/like and get yourself signed up to weeklyclaw.com

Now comes the question everyone hits next - "how do I make it actually do things?"

And this is where most people - myself previously included - go completely sideways.

What skills actually are

Skills are not agents. This is the bit that trips people up.

An agent is a separate brain. It has its own memory, its own context window, its own personality. Spinning up a new agent is like hiring a new employee who knows nothing about your company and has never met anyone on the team.

A skill is a set of instructions that your existing agent can follow. Same brain. Same memory. Same context. Just a new capability.

Think of it like this - you don't hire a separate person every time you need a different task done at work. You learn new skills. Or you reference a manual. Your brain stays the same. Your knowledge carries over. You just know how to do more things. It's like the limitless pill, but permanent.

That's what skills do for your agent.

When I tell Momo to scan my Twitter, he loads the X skill. When I ask about finances, he loads the finance skill. When I need content written, he loads the writing skill. Same agent. Same memory of who I am, what I like, what I've said before. He just pulls up the right playbook.

One brain. Many skills. Full context. Way cheaper.

The Jarvis trap

Scroll through any AI community right now or probably, just your X feed. You'll see dashboards with 6, 8, 12 agents. One for email. One for code. One for research. One for scheduling. A "supervisor" agent telling them all what to do. Screenshots that look like mission control at NASA. And don't get me wrong, it's cool - I love seeing pixel agents running around a mission control.

But it's mostly bollocks.

Here's what actually happens. You spin up Agent A for writing and Agent B for research. Agent A needs information that Agent B found. But Agent A has no idea what Agent B knows. They don't share context. They don't share memory. They're separate brains in separate rooms shouting through walls.

So you build a "coordinator" agent to manage them. Now you've got three agents and the coordinator is burning tokens just passing messages back and forth. The writing agent asks for research, the coordinator relays it, the research agent responds, the coordinator relays it back. Every message costs money. Every handoff loses nuance.

Then something goes wrong - and you have no idea which agent broke. Was it the coordinator? The research agent? Did context get lost in translation? You're debugging a system instead of doing work.

I know because I lived this. 8 agents. Multiple API keys. Hundreds of dollars in token costs. And the output? Worse than one decent agent with the right setup.

The real difference - context

This is the thing nobody talks about when they're showing off their multi-agent dashboards.

Context is everything. When my agent, momo writes a tweet for me, he knows my voice because he's been talking to me for weeks. He knows my opinions. He knows what topics I care about. He knows I hate corporate buzzwords and that I write in fragments or NEVER want to use an mdash ever again.

If I had a separate "writing agent" it would know none of this. I'd have to re-explain my preferences every time. Or maintain a separate config file. Or build some janky system to sync personality data between agents. All of which costs time, tokens and sanity.

With skills, the context is just there. Because it's the same agent. He read SOUL.md once. He remembers.

When my momo scans X accounts and then I ask him to write a thread based on what's trending - he already knows. He scanned it. The information is in his head. No handoff. No relay. No coordinator tax.

How skills work in practice

A skill in OpenClaw is basically a folder with a SKILL.md file. That file tells your agent how to behave when it's doing that specific task.

My setup right now:

- X skill - handles scanning accounts, writing tweets and threads, analysing engagement, content strategy. One skill for the full loop.

- Writing skill- my voice, my rules, my banned words, my sentence structure. Anything long-form runs through this.

- Finance skill - tracks my budget, payments, income. Knows my financial situation without me repeating it, even my business accountings.

- Sport.Fun skill - everything related to my work. Brand voice, strategy docs, key people, product details.

- The Larry skill - @oliverhenry's free social media engine. Content creation, TikTok posting, scheduling through Postiz - fully automated. One skill got him 8 million views in a week without touching his phone.

You can sign up to Postiz for automating through ANY social here btw:
https://postiz.pro/jordymaui

And a few more, i'll share another time... can't tell you EVERYTHING about Momo and his secret sauce now can!

Each one is a markdown file. No API keys. No separate instances. No extra cost.

When I type in my #x-scan Discord channel, Momo knows to load the X skill. When I'm in #finances, he loads the finance skill. The channel tells him which hat to wear.

But here's the key - he still knows everything else too. If I'm in the finance channel and mention something about work, he has that context. Because he's one agent. Skills add capability without removing context.

Are you seeing the clear differences now?

When you actually need multiple agents

Listen, I'm not saying multi-agent setups are always wrong. There are real use cases.

Heavy isolated tasks. If you need an agent to go off and do 30 minutes of deep research without clogging up your main conversation, spawn a sub-agent. It does the work, reports back, and dies. OpenClaw supports this natively - your main agent can kick off background tasks that run in isolation and announce results when they're done. This is how I actually operate.

Different models for different jobs. Maybe you want a cheaper model grinding through data while your main agent stays on the good stuff. Fair enough. For example, I use sonnet for some X scanning work - due to not much logic needed, just pure scraping.

Shared environments. If multiple people need to interact with an agent in a work context, a separate agent with its own permissions makes sense.

But for personal use? One agent. Skills. Done.

The money bit

Let's be real about cost because this is where multi-agent setups get painful fast.

Every agent burns tokens. Every message, every piece of context, every handoff between agents - tokens. When you've got 8 agents running, you're paying 8 times for context loading, 8 times for personality files, 8 times for memory retrieval.

With one agent and skills, you load context once. SOUL.md once. USER.md once. The skill file is usually a few hundred lines of markdown. Tiny cost.

I went from burning through hundreds on multi-agent API costs to running everything on a flat Claude Max subscription. $90 a month. One agent. Unlimited skills. That's less than what I was spending per week on the old setup. And despite the recent FUD - no, Claude Max is NOT being banned. So you do NOT need to convert to API tokens that cost a fortune. (thank god)

How to set up your first skill

If you've followed the first article, you've got OpenClaw running. Here's how to add a skill.

The simplest version - create a folder in your workspace's skills directory with a SKILL.md file inside it. That file contains instructions for your agent.

Example - say you want a skill for writing emails in your voice:

Then literally ask your agent to create an 'Email skill'

And give it enough context to understand:

When writing emails for [your name]:
- Keep them short. 3-5 sentences max.
- Start with the person's name, no "Dear" or "Hi there"
- Sign off with just your name
- Match formality to the recipient
- Never use "just following up" or "hope this finds you well"
- Don't use mdashes

That's it literally it. Your agent reads this when it needs to write an email. Same brain, new instructions - and you can develop it as you go.

You can also install community skills from ClawHub - pre-built skills that other people have made. Your agent can do this for you. Just say "install the [name] skill" and it handles the rest.

Some Examples of Skills doing real damage - Larry's story

This isn't theoretical. Skills are already generating real results for real people.

My friend Oliver Henry (@oliverhenry) built an OpenClaw agent called Larry. Larry runs a social media skill that handles content creation, scheduling, and posting - fully automated. One agent. One skill. No multi-agent circus. I've mentioned it once already, I literally use it.

The results? 8 million TikTok views in a single week. $4,000 earned in 24 hours. New paying subscribers converting daily.

And here's the best part - he gave the skill away for free. You can install it right now from ClawHub and have your agent doing the same thing. One skill file. No extra API keys. No separate agents. Just your existing bot with a new capability. You can simply ask your agents to 'install Larry skill' and they will do so.

Larry uses Postiz for the scheduling and posting side - it's an open-source social media tool that connects to X, TikTok, LinkedIn, all of it. Your agent writes the content, Postiz handles the distribution. If you want to try it, here's my link once more - incase you didn't get it the first time: https://postiz.pro/jordymaui. I personally use this even outside of automation btw.

Anyway - the point isn't that Larry is special or that Ollie is my pal. The point is that this is what one skill on one agent looks like when it's set up properly. No coordinator agents. No message relaying. No debugging which of your 8 agents broke. Just a skill that knows what to do. And it's translatable across every agent, always.

The setup that actually works

Here's what I'd recommend after running this for months:

1. One main agent. Give it a proper personality. Fill out the context files. Let it get to know you.

2. Skills for every repeating task. If you do it more than twice, make a skill for it.

3. Channels as departments. Each channel maps to a skill. Walk into a channel, your agent knows what mode to be in.

4. Sub-agents for heavy lifting only. Background tasks that take ages. Not daily operations.

5. Memory files for continuity. Daily notes, long-term memory, heartbeat checks. Your agent wakes up fresh each session - files are how it remembers.

This setup has replaced what I was trying to do with 8 separate agents. It's faster, cheaper, and honestly just works better. The context sharing alone makes it worth it.

Please stop building mission controls

I get the appeal. I really do. The multi-agent dashboard looks like the future. It feels like you're building something powerful.

But powerful and useful are different things. I've had both setups. The 8-agent F16 Flightdeck dashboard and the single-agent-with-skills approach. The second one actually gets stuff done.

The best AI setup isn't the most complex one. It's the one that disappears into your workflow and just helps. One brain that knows you, knows your voice, knows your goals - and picks up the right skill for whatever you throw at it.

Skills are the play.

So, Whats Next?

Now, i'm building the BEST and LARGEST OpenClaw community possible by building: WeeklyClaw (weeklyclaw.com)

Sign up for the early access because I am putting SO much into this.
DAILY and WEEKLY news on everything OpenClaw.

And yes, you can just feed it to your agent to digest too.
But also... maybe I just make a paid skill so you don't even need to read it, and your agent knows it allllll anyway? ;)

And as per usual - Any Questions? Drop them below. I'll do my best to answer them, perhaps even make a community for all of this too.

I appreciate all the engagements, bookmarks etc and will continue to push the boundaries of mainstream OpenClaw know how.

Cheers, @jordymaui and of course - my boy - @loyalmomobot
Make sure you give him a follow and give him a treat, he deserves it.