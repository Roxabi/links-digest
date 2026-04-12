---
title: "zacdcook/claude-code-semantic-memory"
source: "https://github.com/zacdcook/claude-code-semantic-memory"
date: 2026-01-29
tags: ["semantic memory system", "Claude Code plugin", "persistent memory", "transcript conversion", "local embeddings"]
platform: github
author: "zacdcook"
summary: "A persistent memory system for Claude Code that extracts learnings from past sessions and injects relevant context on every prompt."
---
# zacdcook/claude-code-semantic-memory

**URL:** https://github.com/zacdcook/claude-code-semantic-memory
**Description:** Persistent semantic memory system for Claude Code
**Language:** Shell
**Stars:** 1 | **Forks:** 0
**License:** MIT License
**Last updated:** 2026-01-29

## README (excerpt)

# Claude Code Semantic Memory System

A persistent memory system for Claude Code that extracts learnings from past sessions and injects relevant context on every prompt.

## The Problem

Claude Code sessions are stateless by default. Every time context compacts or you start a new session, Claude forgets:
- Solutions you already discovered together
- Gotchas and traps you identified
- Your infrastructure details and preferences
- Decisions you made and why

This leads to repeated mistakes, redundant conversations, and lost productivity.

## The Solution

This system gives Claude **persistent memory** across sessions:

1. **Convert** your `.jsonl` transcripts to readable markdown
2. **Extract** learnings using Claude sub-agents that process transcripts
3. **Embed** learnings with a local embedding model (nomic-embed-text)
4. **Inject** relevant memories via Claude Code hooks that fire on every prompt

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Your Prompt    │────►│  Hook Fires     │────►│  Query Daemon   │
│                 │     │  (mechanical)   │     │  (cosine sim)   │
└─────────────────┘     └─────────────────┘     └────────┬────────┘
                                                         │
                                                         ▼
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  Claude sees    │◄────│  Inject as XML  │◄────│  Top 3 memories │
│  context + mem  │     │  in context     │     │  (≥0.45 sim)    │
└─────────────────┘     └─────────────────┘     └─────────────────┘
```

---

## Quick Start

### Prerequisites

- [Node.js](https://nodejs.org/) (for transcript conversion)
- [Ollama](https://ollama.com/) (for local embeddings)
- Python 3.8+ (for the memory daemon)
- Claude Code CLI

### 1. Install Dependencies

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull the embedding model
ollama pull nomic-embed-text

# Clone this repo
git clone https://github.com/zacdcook/claude-code-semantic-memory.git
cd claude-code-semantic-memory
```

### 2. Convert Your Transcripts

Claude Code stores session transcripts as `.jsonl` files in `~/.claude/projects/`. Convert them to readable markdown:

```bash
node scripts/jsonl-to-markdown.js ~/.claude/projects/ ./converted-transcripts/
```

This extracts user messages, assistant messages (including thinking blocks), and system prompts. Tool calls and results are stripped for cleaner extraction.

### 3. Extract Learnings

Start a new Claude Code session and use the extraction prompt:

```bash
claude
```

Then paste the contents of `prompts/extract-learnings.md`. Claude will:

1. List all `.md` files in your converted transcripts folder
2. Dispatch sub-agents in parallel to process batches
3. Each sub-agent extracts structured learnings
4. Store learnings via the daemon's `/store` endpoint
5. Output to `~/extracted-learnings.jsonl`

### 4. Start the Memory Daemon

```bash
cd daemon
pip install -r requiremen...