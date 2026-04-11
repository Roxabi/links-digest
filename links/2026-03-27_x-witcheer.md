---
title: "Living With an AI agent - My Full Setup After 2 Months"
source: "https://x.com/witcheer/status/2037528582298194123?s=12"
date: 2026-03-27
tags: ["AI Agent", "Hermes Agent", "Local LLM", "Mac Mini", "Automation"]
platform: x
author: "@witcheer"
summary: "The author details a comprehensive two-month experiment running a fully autonomous AI agent on a local Mac Mini using the Hermes framework and a multi-model stack to perform research and daily tasks"
---
I wake up at 7am and there's a briefing in my Telegram. overnight moves, arXiv papers on AI agents, Hacker News threads worth reading, Reddit posts from r/LocalLLaMA, and a prioritised list of what I should focus on today, cross-referenced against my actual projects and deadlines.

I didn't set an alarm for any of this. I didn't open a browser. I didn't check Twitter.

an AI agent on a Mac Mini in my living room did all of it while I slept. it ran 18 scheduled jobs between 7am yesterday and 7am today. it searched the web, fetched full articles, ran shell scripts against 8 different APIs, wrote findings to memory files, drafted content for my Telegram channel, scored those drafts against my voice rules, and logged everything to a structured context system that makes tomorrow's research smarter than today's.

total monthly cost: $21.

this is the full breakdown. every component, every config, every bug I hit, every fix I found. if you want to build something like this, everything you need is here.

what we're going to talk about:

/1/ the hardware

/2/ the agent framework: Hermes Agent

/3/ the model stack

/4/ cron jobs: the autonomous research pipeline

/5/ shell scripts: the automation layer

/6/ custom skills: on-demand capabilities

/7/ ALIVE: the context system that makes everything compound

/8/ teaching an AI your writing style: the voice feedback loop

/9/ what I'd do differently (lessons from 2 months)

/10/ how to replicate this (minimum & full set up guide)

/11/ the philosophy

The Hardware

Mac Mini M4, 16GB RAM. bought it in early 2026. it sits in my living room, runs 24/7, and powers everything: the AI agent gateway, a local LLM for compression, occasional Docker containers, and all 18 cron jobs.

total disk footprint: ~120MB for the agent framework + 6.6GB for the local LLM models.

in short: this is a $600 computer the size of a sandwich. it runs my entire AI setup. there is no cloud server or GPU cluster, no monthly AWS bill. a box in the living room.

The Agent Framework: Hermes Agent

Hermes Agent is an open-source Python framework by @NousResearch. it's the backbone of everything.

the interface is a Telegram bot. I text it like I'm texting a colleague. it has access to a terminal, can read and write files, search the web, fetch full web pages, execute code, run shell scripts, and use custom skills I've written for it.

it runs as a macOS launchd service, meaning it starts on boot and restarts if it crashes.

what Hermes gives you:

Telegram bot with full tool access (terminal, files, web search, web fetch, code execution)

cron scheduler - jobs run on a schedule, results delivered to Telegram

skills system - markdown files that teach the agent new capabilities

memory system - persistent files the agent reads and writes across sessions

session management - compression, idle timeout, daily reset

MCP support - model context protocol servers for extending tool access

what it doesn't give you:

multi-model fallback chains (single fallback only, if both models fail, the job fails)

automatic session cleanup (needs manual scripting)

good writing (model limitation, not framework limitation, more on this later)

in short: think of it as an AI assistant that lives in your Telegram. but instead of just answering questions when you ask, it also runs scheduled tasks in the background, remembers things between conversations, and can use tools, like a junior employee who works 24/7, never sleeps, and has access to your terminal.

The Model Stack

this is where it gets interesting. I don't use one model. I use three, each for a different job.

Interactive Chat: GLM-5 via Z.AI

when I text the bot directly, it uses GLM-5, a Chinese model by Zhipu AI, accessed through Z.AI's coding plan at $21/month.

why GLM-5? it's the cheapest model with tool calling that actually works. it reasons well, follows complex multi-step instructions, and handles the research pipeline reliably. however, its writing is terrible. every draft sounds like AI. but I don't need it to write, I need it to research, execute, and coordinate. I handle the writing myself.

the reasoning token trap:

GLM-5 always generates reasoning tokens, internal "thinking" before it responds. there's a reasoning_effort config option in hermes that's supposed to control this. it does nothing for GLM-5. the model thinks regardless.

those reasoning tokens get stored in the conversation history. every new message includes all previous reasoning. so your context fills up fast. after 15-20 exchanges, the agent slows to a crawl because it's re-processing thousands of reasoning tokens from earlier in the conversation.

in short: imagine every time you ask your assistant a question, they re-read their entire diary from the beginning of the day before answering.

Cron Jobs: GLM-4.7 via Z.AI

all 18 automated jobs run on GLM-4.7, same provider, cheaper model. this is critical because Z.AI has a rate limit: 600 prompts per 5 hours on the coding plan. if the cron jobs used GLM-5, they'd eat through my interactive quota.

Compression: Qwen3.5 via local Ollama

this is the piece that took the longest to get right and taught me the most.

every AI model has a context window, the amount of text it can "see" at once. as conversations get longer, the context fills up. compression summarises old messages to free up space.

originally, compression used the same cloud API (Z.AI) as everything else. this created a death spiral:

cron job runs → generates messages → context grows

context hits threshold → triggers compression

compression calls Z.AI → uses API quota

more cron jobs run → more compression calls → more quota used

rate limit hit → compression fails silently → context keeps growing

context grows unbounded → agent hangs for 10+ minutes trying to process a bloated session

I didn't notice for days. the agent was just... slow. I assumed it was network latency.

the fix: run compression on a local model using Ollama. completely free. no rate limits. no API dependency.

I installed Ollama on the Mac Mini, pulled qwen3.5:4b (a 3.4GB model that runs at ~20 tokens/second on the M4 chip), and pointed compression at localhost. done.

the idle timeout discovery:

even after fixing compression, the agent was still slow during peak hours. found that the default session idle timeout was 1440 minutes - 24 hours. meaning sessions never reset during the day. they grew from 7am morning briefing through every cron job until the next morning.

changed it to 60 minutes. now sessions reset between jobs. response times went from 10+ minutes during heavy periods to under 5 seconds.

in short: imagine your desk gets covered in papers throughout the day but you never clean it. by evening, you can't find anything and every task takes 10x longer because you're shuffling through a mountain of old notes. the idle timeout is how often you clean the desk. 24 hours means you never clean it. 60 minutes means you clean it every hour. same work gets done, 100x faster.

the config that makes it work:

compression threshold 0.50 means it triggers when the context is half full. Ollama keep-alive of 5 minutes means the model auto-unloads from RAM after 5 minutes of idle, freeing memory for other tasks.

18 Cron Jobs: The Autonomous Research Pipeline

this is the core of the system. 18 scheduled jobs that run throughout the day, researching, monitoring, drafting, and maintaining the infrastructure.

every job runs on GLM-4.7. every job delivers results to Telegram. every job reads from and writes to the structured context system (more on that later).

daily schedule

07:00 - morning briefing. weather, crypto prices, stablecoin pegs, RWA sector moves, overnight research recap, top Hacker News and Reddit threads. reads all my project context files to surface what matters today.

07:30 - competitor dashboard. tracks 11+ CDP and stablecoin protocols, TVL changes, governance proposals, partnership announcements. I work in DeFi. knowing what competitors are doing before they announce it publicly is the job.

09:00 & 17:00 - dune monitor. runs on-chain query monitoring. twice daily.

10:00 - grimoire drafter. drafts posts for my Telegram channel in visual-first format.

11:00 - daily nudge. this one is different. it reads ALL my project context files across every venture, the agent itself, my content strategy, and suggests where to focus based on urgency, deadlines, and cross-project tensions. it's a priority engine.

12:00 - draft review. picks the best unposted draft, checks it against voice rules, delivers to Telegram for my review.

14:00 - research-ai. AI news, papers, agent frameworks. sources: arXiv, Reddit, Hacker News, Techmeme, news sites.

16:00 - research-arcana. redacted.

18:00 - research-defi. stablecoins, RWA, governance, competitor analysis.

20:00 - research-deepdive. picks one topic from the day's findings and goes deep. full analysis with web fetching, data compilation, and a structured report.

21:00 - health check. monitors all crons, gateway status, disk space, launchd services.

22:00 - content performance. tracks what content performed well, logs metrics.

23:00 - nightly builder. this is the wildest one. it looks at gaps identified during research like missing scripts, broken data sources, needed tools... and autonomously writes code to fill them. it has built monitoring scripts, fixed broken parsers, and created new data pipelines. while I sleep.

periodic schedule

monday/thursday 09:00 - outreach CRM. automates parts of my BD workflow.

monday 09:00 - weekly intel. competitive intelligence brief.

sunday/wednesday 20:00 - learning digest. curated learning resources from the week.

sunday 08:00 - weekly planner. reads performance data, research findings, and project states → produces a content and priority plan for the week.

hourly

every hour 9am-8pm - breaking news. RSS feeds + TVL monitoring + stablecoin peg alerts + viral tweet detection. if something moves, I know within the hour.

now, let's understand how a research cron actually works.

let me break down the research-ai job because it's the most complex. the prompt is ~3,000 words. here's what it actually does, step by step:

step 1 — source verification rules. before anything else, the prompt hammers one rule: never include a finding without a URL you actually visited. if you searched but got no results, say so. before including any finding, ask yourself: did I actually visit this URL?

this matters because GLM-4.7 hallucinates URLs. not often, but enough. this instruction reduces hallucinated sources to near-zero.

step 2 — context loading. the agent reads 7 files: its persistent memory, the operations log, research priorities, my content voice guide, voice corrections from past drafts, the AI research archive, and the relevant project context files. this means the research is guided by what I'm actually working on.

step 3 — email check. checks a bot alerts inbox using Himalaya (a CLI email client). catches newsletter alerts and automated notifications.

step 4 — arXiv scan. runs a custom Python script that queries the arXiv API for recent papers on AI agents, LLM reasoning, and tool use. filters by relevance.

step 5 — nightly builder check. did the overnight autonomous builder create any new tools? if so, note them.

step 6 — web search. diverse sources required. the prompt explicitly says: fetch Techmeme first, then Hacker News, then Reddit, then use web search to fill gaps. never rely on web search alone.

this source diversity rule exists because GLM-4.7 defaults to Reddit for everything. Reddit results rank high in search. without the explicit rule, every morning briefing was Reddit-only for days before I noticed.

step 7 — deep read. web-fetch the 2-3 most interesting articles in full.

step 8 — WRITE findings. this is mandatory. the prompt says: "a session with no writes is a failure." findings get written to the AI research archive file. this means tomorrow's session starts from a richer knowledge base.

step 9 — draft. if something is content-worthy, draft it in personal experience format. read voice corrections first.

step 10 — quality check. run check_draft.sh. must score ≥70/100 against voice rules.

step 11 — operations log. one line summarising what happened.

step 12 — context update. update the project context files with session results.

step 13 — self-check. "did I write new content to the research archive? if NO, go back and do step 8." this prevents the agent from doing all the research and then not saving anything.

in short: each research job is like sending an employee on a research mission with a 15-point checklist. load your priorities. check your inbox. scan the academic papers. read the news. actually click through and read the full articles, don't just skim headlines. write down what you found. draft something if it's interesting. check that your draft doesn't sound like garbage. log what you did. update the team on what you learned. and if you didn't write anything down, go back and do it.

35 Shell Scripts: The Automation Layer

every script lives in ~/.hermes/scripts/, chmod 700, symlinked at ~/scripts/ so the agent can call them easily.

these are the muscles of the system. the agent is the brain. the scripts are how it interacts with the world.

data source scripts

coingecko.sh - BTC/ETH/AAVE/MKR prices, 24h changes, stablecoin peg data. no API key needed.

defillama.sh - CDP protocol TVL rankings, stablecoin market caps. no API key needed.

rwa-tracker.sh - full RWA sector scan. 120+ protocols, $25B+ TVL. tracks top movers. no API key needed.

hackernews.sh - top stories from Hacker News filtered by keywords (AI, DeFi, agents, LLM). uses the Firebase API. no key.

reddit-digest.sh - top posts from r/LocalLLaMA, r/MachineLearning, r/defi. uses Reddit's public JSON endpoints. no key.

governance-tracker.sh - active governance votes on Snapshot.org for protocols I care about (Morpho, Curve, Lido). plus forum RSS feeds.

arxiv-digest.py - queries the arXiv API for latest papers on agents, reasoning, tool use. filters and formats.

fred.sh - federal reserve economic data. fed rates, inflation, money supply. free API key.

monitoring scripts

tvl-monitor.sh - caches a TVL snapshot, alerts if any tracked protocol moves >10% since last check.

stablecoin-supply-monitor.sh - detects >$100M USDT/USDC/DAI mints or burns. large supply changes signal market moves.

breaking-news.sh - combines all monitors + RSS feeds + viral tweet detection into one alert system.

health-check.sh - monitors cron job execution, launchd services, gateway status, disk space, PAT expiry dates.

content pipeline scripts

check_draft.sh - scores drafts 0-100 against my voice rules. auto-runs on every draft. anything below 70 gets flagged.

draft-review.sh - picks the best unposted draft daily, flags drafts with wrong formatting.

mark_posted.sh - moves draft to the posted archive, logs to content calendar.

log-performance.sh - records post metrics: impressions, engagement, bookmarks.

infrastructure scripts

update-walnut.sh - 77 lines of bash. prepends a timestamped log entry to the relevant project context file. called at the end of every research cron. this is the glue between the cron jobs and the context system.

compact_memory.sh - archives session logs older than 3 days, trims the operations log to 7 days. prevents unbounded growth.

github-push-nightly.sh - the paranoia script. runs 13 regex patterns scanning for leaked secrets (API keys, tokens, passwords) before pushing to Git. three layers of checks.

auto-update.sh - daily Hermes framework update trigger.

docker-cleanup.sh - removes zombie sandbox containers older than 4 hours.

in short: the scripts are like having a toolbox. the AI agent knows how to use a hammer, a screwdriver, and a wrench, but you have to give it the actual tools. each script is a tool that connects the agent to a specific data source or capability. without them, the agent can only search the web. with them, it can query DeFi protocols, scan academic papers, monitor on-chain activity, check its own health, and push code to GitHub.

none of these are complicated. most are under 50 lines. the value is in having 35 of them working together inside a scheduled system.

6 Custom Skills: on-Demand Capabilities

skills in Hermes are markdown files. you write a markdown document explaining what you want the agent to do, when, and how, and the agent reads it when invoked.

the SKILL.md file is the instruction set.

1. walnuts - cross-project context

type walnuts in Telegram → the agent reads all 5 of my project context files → synthesises a cross-venture view with priorities, blockers, and tensions.

example output:

this is my strategic dashboard. one word in Telegram, 10 seconds, full situational awareness across every project.

2. grimoire - Telegram channel drafting

drafts posts for my Telegram channel @witcheergrimoire in visual-first format: 1-4 sentences + image. includes URL verification rules because GLM-5 hallucinates URLs about 5% of the time.

3. yari-intel - competitive intelligence

on-demand market analysis: CDP TVL rankings, competitor deep dives, RWA opportunity mapping, governance tracking. combines DeFi llama data + shell scripts + web search.

4. arcana-intel - consulting market research

redacted.

5. alpha-scanner - cross-source signal detection

combines Polymarket odds, stablecoin flows, RWA momentum, social signal (Reddit + Thread Reader), and governance alpha.

6. voice-learn - the draft feedback loop

this one deserves its own section (below). in short: when I edit an AI draft before posting, this skill extracts what I changed and why, saves the lesson, and every future draft reads those lessons before writing.

in short: skills are like SOPs (Standard Operating Procedures) for the AI. you write a document saying "when I say X, do Y in this specific way." the AI reads the document at runtime and follows it. you write a markdown file and the agent has a new capability.

the beauty is iteration speed. writing a new skill takes 10 minutes. testing it takes one Telegram message. refining it takes editing a text file. compare that to building a plugin, deploying a service, wiring an API.

ALIVE: The Context System That Makes Everything Compound

this is the part most people haven't seen before, and it's the part that makes the biggest difference.

created by @stackwalnuts, ALIVE is a structured context system. think of it as a personal knowledge graph on disk. the basic unit is a "walnut", a context container for one project or domain.

the structure

each walnut has a _core/ folder with 5 files:

key.md — identity, thesis, connections to other walnuts

now.md — current phase, next action, blockers

tasks.md — urgent / active / backlog

insights.md — standing knowledge, lessons learned

log.md — session history (prepend-only, newest first)

that's it.

three integration layers to make it works perfectly:

layer 1: cron jobs WRITE to walnuts.

at the end of every research cron, the update-walnut.sh script prepends a log entry to the relevant walnut. research-ai logs to the oz-agent walnut. research-defi logs to the yari-finance walnut. research-arcana logs to the arcana walnut.

this means every walnut accumulates a history of what was researched, found, and learned, automatically.

layer 2: cron jobs READ from walnuts.

before researching, each cron reads the relevant walnut's tasks and insights. research aligns to what I'm actually working on.

research-ai reads oz-agent tasks ("improve draft quality") → searches for prompt engineering techniques specifically.

research-defi reads yari-finance tasks ("map RWA partnership opportunities") → searches for RWA protocol news specifically.

the morning briefing reads ALL walnut now.md files → surfaces what matters today across every project.

layer 3: interactive Telegram gets walnut context.

when I type walnuts, the agent reads all 5 walnut files and gives me a synthesised cross-venture view. context stays in session until idle timeout.

here's where it compounds:

I update walnut tasks (manually or via Telegram)

cron jobs read the tasks → research aligns to priorities

research produces findings → findings update the walnut log

I adjust tasks based on findings

next cron picks up adjusted priorities

research becomes more focused

findings become more relevant

repeat

each cron knows what I'm trying to accomplish. it reads my priorities before searching. it writes what it found after searching. and the next session starts smarter.

both Claude Code and Hermes Agent read and write the same files natively. same context layer.

in short: imagine you have 5 notebooks, one for each project. before doing research, you re-read the relevant notebook to remember what you're working on and what you need. after research, you write down what you found. tomorrow, you re-read again and your research is better because it builds on yesterday's notes.

ALIVE is that, except the AI agent does the re-reading and note-taking automatically, and the notebooks are structured in a way that both your interactive agent and your automated cron jobs can use.

Teaching an AI Your Writing Style: The Voice Feedback Loop

this is the technique I'm most excited about, and it's the one that costs zero dollars.

the problem

standard approach: write a better prompt. add more rules, more examples, more constraints. "write in personal experience format." "use lowercase." "no bullet points." "vary sentence length."

I have 39,000 characters of content voice instructions. the model still produces slop. more rules ≠ better output. after a certain point, the model can't integrate more abstract instructions.

the fix: correction logging

instead of telling the AI how to write, I show it what I changed.

after every post, the cycle is:

I say "I tweaked your draft" on Telegram

the voice-learn skill activates

it reads the original draft and my posted version

it extracts every difference: tone shifts, cuts, additions, word swaps

it saves each lesson to voice-corrections.md

every future drafting cron reads voice-corrections.md before writing

why corrections beat prompts

prompts say "write in personal experience format."

corrections say "you wrote 'not saying this is UST 2.0' - I cut that because preemptive hedges undercut expertise. don't do this again."

151 lines of "when you did X, I changed it to Y, because Z."

that's 151 concrete examples. specific beats abstract, every time. the model still produces AI slop, but it's better AI slop. and the corrections compound. every draft that passes through the feedback loop adds more examples.

the model can't write like a human. but it can write like a slightly-better AI that knows 151 specific things to avoid. and that's enough when the human is doing the final pass.

in short: instead of giving someone a book about how to write like you, you sit next to them every time they write, point at specific sentences, and say "don't do that, do this instead." after 28 of those corrections, they start avoiding the mistakes on their own. not perfectly. but enough that your editing time drops from 80% rewriting to maybe 50%.

What I'd Do Differently (Lessons From 2 Months)

1. start with local compression from day one. cloud API compression and rate limits creates silent failure. sessions grow unbounded and you won't notice until the agent is hanging for 10 minutes per response. local Ollama compression is free, reliable, and has zero rate limits.

2. set per-job model config immediately. don't patch the scheduler code. it gets wiped on every update. set "model": "glm-4.7" in each job's config in jobs.json. survives updates, survives patches, never needs re-applying.

3. don't trust the AI to write. build the research pipeline fast. build the voice feedback loop on day one. accept that you'll be rewriting 50-80% of every draft for weeks. the corrections compound, but slowly. get 50+ correction entries before expecting usable drafts.

4. set session idle timeout to 60 minutes. the default is often much longer. long sessions = bloated context = slow responses. short sessions = fresh context = fast responses. the research still gets saved to files between sessions.

5. enforce source diversity in prompts. if you don't explicitly force it, the model will use Reddit for everything because Reddit ranks high in search results. explicit rules: "fetch Techmeme first, then Hacker News, then Reddit, THEN use web search to fill gaps." specify the order.

6. monitor your compression pipeline. it fails silently. if the agent suddenly takes 10 minutes to respond and sends 8 messages of context dump, compression is probably broken. check the model, check the endpoint, check the manifest. ollama pull to force a clean download.

How To Replicate This

here are everything you need to run the minimum viable setup (30 minutes)

step 1: install Hermes Agent.

step 2: get Z.AI coding plan ($21/month). set these in .env:

critical: use the /coding/paas/v4 endpoint, NOT /paas/v4. the coding plan key only works on the coding endpoint.

step 3: create a Telegram bot via @BotFather. set the token:

step 4: start the gateway.

step 5: create 2-3 cron jobs. start with a morning briefing, one research session, and a breaking news monitor. edit jobs.json, set "model": "glm-4.7" on each job.

you now have a 24/7 AI agent running on your machine, accessible via Telegram, with automated research jobs.

----

if you want to go further, here are everything you need for the full setup (one weekend)

everything above, plus:

step 6: install Ollama + compression model.

configure in .env and config.yaml:

set session idle timeout to 60 minutes. set compression threshold to 0.50. set Ollama keep-alive to 5 minutes.

step 7: create 5-10 shell scripts for your data sources. pick APIs relevant to your work. most public APIs (coingecko, defillama, Hacker News, Reddit, arXiv) don't need API keys.

step 8: create 2-3 custom skills. start with a cross-project context skill (walnuts) and a content drafting skill for your domain.

step 9: set up ALIVE with 3-5 walnuts. create the folder structure, write the key.md and now.md files for each project. wire cron jobs to read/write walnuts using update-walnut.sh.

step 10: start the voice feedback loop on day one. create voice-corrections.md. every time you edit a draft, log what you changed and why. wire your drafting cron to read corrections before writing.

what you need

Mac Mini, old laptop, or any always-on machine (Linux works too - Hermes isn't mac-specific)

$21/month for Z.AI (or bring your own API key for any openai-compatible provider)

a Telegram account

patience with AI-generated content (it will be bad at first - that's normal)

what you don't need

coding experience beyond basic shell scripting

permission from anyone

The Philosophy

this isn't about building a perfect AI agent.

GLM-5 produces slop. the research hallucinates URLs sometimes. cron jobs fail. compression breaks silently. the model can't write like a human and probably never will.

but it runs 24/7. while I sleep, it scans arXiv papers, monitors stablecoin pegs, checks Reddit and Hacker News, tracks competitor TVL, and writes draft posts that I edit in the morning. when I wake up, there's a briefing in my Telegram with overnight developments and a queue of drafts to review.

the agent is persistent.

and persistence × time = compound context.

after weeks of running, the memory files have captured patterns. the walnut logs have history. the voice corrections have accumulated. each new session starts from a richer base than the last. the research gets more focused because it reads priorities before searching. the drafts get slightly better because they read corrections before writing. the priorities get sharper because the morning briefing reads what actually happened yesterday.

none of this is magic. it's in the structured context that accumulates around it.

the walnuts, the correction logs, the research archives. the AI is the engine. the context is the fuel.

and the fuel compounds.

built by @witcheer.