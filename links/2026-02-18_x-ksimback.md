---
title: "Give your Openclaw the Memory it Needs (Full Guide)"
source: "https://x.com/ksimback/status/2024180197910864182?s=46"
date: 2026-02-18
tags: ["memory configuration", "OpenClaw setup", "agent memory", "memory failures"]
platform: x
author: "@KSimback"
summary: "This guide explains how to fix OpenClaw memory failures through configuration changes and advanced tools."
---
This guide covers the three common ways memory fails, the configuration changes that fix most issues, and the advanced tools (QMD, Mem0, Cognee, Obsidian) that make memory production-grade. Feed this article to your agent and it will thank you later because it remembers.

Introduction

Over the past month running multiple instances of @openclaw I've had my agents forget basic information, lose critical project context mid-conversation, and completely blank on decisions we made 24 hours earlier.

If you've used OpenClaw for more than a day, you've probably hit this too. Your agent "knows" things, then suddenly doesn't. You've told it your preferences multiple times. You've watched it write something to memory, then fail to recall it the next day. You start wondering if memory is actually broken.

The good news is that it can be easily fixed. It just needs a proper setup and this guide will walk you through it.

The Three Common Memory Failures in OpenClaw

Before you can fix memory, you need to understand why it breaks. OpenClaw treats memory as a suggestion, not a requirement. The agent decides what to save, when to search, and what to recall. Without explicit configuration, it forgets by default.

There are three common failure modes, and each requires a different solution.

Failure Mode 1: Memory Is Never Saved

When you tell your agent something important like your name, your preferences, a critical project decision, etc. OpenClaw doesn't force it to disk. The LLM decides whether it's worth saving.

Think about that. Your agent doesn't automatically save to memory, it's actually a judgment call made by the model in real-time.

Sometimes it saves and sometimes it doesn't, and it's not clear when it does or doesn't save. That means important context can slip through constantly because the model deemed it not worth storing.

This is like having an employee who decides on their own which meeting notes to keep and which to throw away.

Failure Mode 2: Memory Is Saved But Never Retrieved

Even when facts make it to disk, recall isn't guaranteed. OpenClaw provides a memory_search tool, but the agent has to decide to use it.

In practice, when you ask about something stored in memory, the model frequently answers from its current context window instead of searching. From your perspective, it "forgot" but in reality, it never looked.

This is like an employee who saved a document to Google Drive, but when you ask for it, they answer from memory instead of checking the actual document.

Failure Mode 3: Context Compaction Destroys Knowledge

This is the killer. To avoid hitting token limits, OpenClaw compacts context so as the context window fills up, older messages get summarized or removed. Any information that only existed in the active conversation (not yet saved to disk) is destroyed.

This applies even to MEMORY.md content, which loads at session start, and can get summarized away during a long session. The agent literally forgets mid-conversation because compaction removed context and nothing triggered a reload.

Imagine having an employee with a stack of papers on their desk. When the stack gets too tall, they throw out the oldest papers to make room without saving the important ones.

Basic Fixes: What Everyone Should Configure

Before reaching for plugins or external databases, there's a lot you can fix with configuration alone. Most cases of "my agent forgets everything" come from running the default config without any basic optimizations. 

Below are 4 basic fixes to the default config that can greatly improve how your OpenClaw memory performs.

1. Enable Memory Flush (This Is Critical)

Memory flush triggers a silent turn before compaction that prompts the agent to write durable memories to disk. This is the single most impactful change you can make.

The key insight is to customize the prompt in the compaction section of your config. The default prompt is generic. Tell it exactly what to capture and specifically include decisions, state changes, lessons, blockers. 

Also advisable to raise softThresholdTokens to 40000 to trigger flushes earlier, before the good stuff gets compacted.

2. Configure Context Pruning

Context pruning controls how old messages are removed before full compaction. Use TTL mode as a simple fix. This will also help save on your token costs as I mentioned as one of the tips in my previous article on how to reduce token costs by up to 90%.

The above config keeps messages from the last 6 hours and always preserves the 3 most recent assistant responses. This eliminates the annoying situation where you have to repeat recent messages following a context flush.

3. Enable Hybrid Search

Memory search combines vector similarity (conceptual matching) with BM25 keyword search (exact tokens), you want to enable both.

If you're not running hybrid search, you're leaving accuracy on the table. BM25 catches exact matches (error codes, project names) that vector search misses.

4. Index Past Sessions

The last simple fix is to enable session transcript indexing to recall conversations from weeks ago.

This chunks and indexes past conversations alongside your memory files. "What did we decide about the content template last Tuesday?" becomes answerable.

Advanced Memory Solutions: When Basic Config Isn't Enough

For agents running more demanding workloads like multi-day projects, multi-agent team coordination, or complex knowledge management, the built-in system can still hit limitations. Here's where to go next.

QMD: Superior Retrieval Backend

QMD, developed by @tobi the CEO of Shopify, is an opt-in replacement for the built-in SQLite indexer. It runs as a local sidecar that combines BM25 + vectors + reranking. The retrieval quality is noticeably better - this is what I'm currently using.

The easiest way to get started is have your agent review the QMD Github and talk through it before implementing, then it should be fairly easy to have your agent install it. Note: whenever installing something like a new memory system, beware of issues and make sure to have a backup before proceeding.

The killer feature with QMD is you can index external document collections. Your Obsidian vault (more on this below), project documentation, Notion exports, etc. becomes searchable via memory_search.

Mem0: Compaction-Proof External Memory

Mem0 is a YC-backed company that markets itself as the "memory layer for AI apps." Mem0 stores memories outside the context window entirely so compaction literally cannot destroy them.

Two processes run every turn:

Auto-Capture detects information and stores it without depending on the LLM's judgment.

Auto-Recall searches and injects relevant memories before the agent responds.

This solves Failure Modes 1 and 3 completely since memory is captured automatically and survives any compaction.

Mem0 installs as an OpenClaw plug-in - see this article for the 30-second installation steps.

Cognee: Knowledge Graphs

When you need to query relationships between people, places and things, then vector search isn't going to be enough. Cognee builds a knowledge graph from your data.

Cognee ingests OpenClaw's memory files to construct a graph of entities and relationships. This allows for structured representation of concepts and their connections (e.g., "Alice owns the auth module" which creates nodes for Alice with a "owns" edge for auth).

Cognee is good for scenarios requiring deep understanding of relationships and structured knowledge like enterprise settings or multi-agent teams. It might be overkill for more basic OpenClaw setups.

Installing Cognee is not trivial unless you're familiar with Docker. This article walks you through it and you can probably figure it out with the help of your agent.

Obsidian Integration

Obsidian is a popular choice as an external brain for agent memory. There are two ways to integrate it:

Symlink your memory folder

Now your agent's daily notes appear in Obsidian on all devices allowing you to review, edit, and annotate easily from your phone.

2.    Index your vault via QMD (my approach)

Everything I capture in Obsidian becomes searchable by my agents. One knowledge base, multiple access patterns. This is the most robust approach I've found so far.

It also saves you on token costs as Obsidian 1.12 shipped a CLI with commands so instead of the agent reading entire files (expensive), it can query metadata and properties.

Connecting Obsidian to your QMD for use in OpenClaw is also not trivial but your agent should be able to walk you through the steps. You can also refer to this article for connecting Claude and Obsidian for a Second Brain.

My Multi-Agent Memory Setup

I run a team of specialized agents across several instances of OpenClaw. Here's how memory works across them:

Layer 1: Private memory per agent. Each agent has its own workspace with MEMORY.md and daily notes. Private context stays private.

Layer 2: Shared reference files with a symlinked _shared/ directory containing user profile, agent roster, and team conventions. Every agent sees the same ground truth and operates from a shared set of principles.

Layer 3: QMD with shared paths. Each agent's QMD config includes the shared directory, so they can all search the same reference docs while maintaining private memory.

Layer 4: Coordination. My "Chief of Staff" agent is responsible for reading core files at session start and maintaining consistency. The specialists focus on their domains.

The key is to treat agent memory like you'd treat a human team's documentation. Some things are shared (handbook, org chart, project docs). Some things are private (personal notes, work in progress). Just build the same structure with your OpenClaw memory if using a team of agents.

The Real Fix

The basic configuration in the first part of this article really helps and the external tools help more, but the main concept is to stop expecting memory to be automatic because it just isn't - you have to configure it to be.

Once I understood that OpenClaw treats memory as suggestions, I started testing different options and researching more which led to all the recommendations in this article. What I found is that many are struggling with memory issues but the good news is that a number of tools and options exist. Now I hope you remember to feed this to your agent.

This is the latest guide in my OpenClaw series. Previously: Cost Optimization Guide (500k+ views) and Agent Teams Guide (250k+ views). Drop me a note @KSimback if you're building similar setups - always interested in how others are solving this.