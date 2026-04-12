---
title: "campfirein/byterover-cli"
source: "https://github.com/campfirein/byterover-cli"
date: 2026-04-04
tags: ["AI memory layer", "context management", "coding agents", "LLM integration", "CLI tool"]
platform: github
author: null
summary: "ByteRover CLI is a portable memory layer for autonomous coding agents that provides persistent structured memory with cloud sync capabilities."
---
# campfirein/byterover-cli

**URL:** https://github.com/campfirein/byterover-cli
**Description:** ByteRover CLI (brv) - The portable memory layer for  autonomous coding agents (formerly Cipher)
**Language:** TypeScript
**Stars:** 4423 | **Forks:** 428
**License:** Other
**Topics:** agent, llm, mcp, memory, vibe-coding, ai, autonomous-agents, cli, coding-assistant, context-memory, developer-tools, knowledge-management, typescript
**Homepage:** https://docs.byterover.dev/
**Last updated:** 2026-04-11

## README (excerpt)

# ByteRover CLI

<div align="center">

<img src="./assets/images/logo/byterover-logo.svg" alt="ByteRover Logo" width="280" />

<p align="center">
<em>Interactive REPL CLI for AI-powered context memory</em>
</p>

<p align="center">
<a href="LICENSE"><img src="https://img.shields.io/badge/License-Elastic%202.0-blue.svg" alt="License" /></a>
<a href="https://npmjs.org/package/byterover-cli"><img src="https://img.shields.io/npm/v/byterover-cli.svg" alt="Version" /></a>
<a href="https://npmjs.org/package/byterover-cli"><img src="https://img.shields.io/npm/dw/byterover-cli.svg" alt="Downloads" /></a>
<a href="https://docs.byterover.dev"><img src="https://img.shields.io/badge/Docs-Documentation-green.svg" alt="Documentation" /></a>
<a href="https://discord.com/invite/UMRrpNjh5W"><img src="https://img.shields.io/badge/Discord-Join%20Community-7289da" alt="Discord" /></a>
</p>

</div>

## Overview

ByteRover CLI (`brv`) gives AI coding agents persistent, structured memory. It lets developers curate project knowledge into a context tree, sync it to the cloud, and share it across tools and teammates.

Run `brv` in any project directory to start an interactive REPL powered by your choice of LLM. The agent understands your codebase through an agentic map, can read and write files, execute code, and store knowledge for future sessions.

📄 Read the [paper](https://arxiv.org/abs/2604.01599) for the full technical details.

Or download our self-hosted PDF version of the paper [here](https://byterover.dev/paper).

**Key Features:**

- 🖥️ Interactive TUI with REPL interface (React/Ink)
- 🧠 Context tree and knowledge storage management
- 🔀 Git-like version control for the context tree (branch, commit, merge, push/pull)
- 🤖 18 LLM providers (Anthropic, OpenAI, Google, Groq, Mistral, xAI, and more)
- 🛠️ 24 built-in agent tools (code exec, file ops, knowledge search, memory management)
- 🔄 Cloud sync with push/pull
- 👀 Review workflow for curate operations (approve/reject pending changes)
- 🔌 MCP (Model Context Protocol) integration
- 📦 Hub and connectors ecosystem for skills and bundles
- 🤝 Works with 22+ AI coding agents (Cursor, Claude Code, Windsurf, Cline, and more)
- 🏢 Enterprise proxy support

## Benchmark Results

All benchmarks are run using the production `byterover-cli` codebase in this repository - no separate research prototype.

We evaluate on two long-term conversational memory benchmarks:

- **LoCoMo** - ultra-long conversations (~20K tokens, 35 sessions) testing single-hop, multi-hop, temporal, and open-domain retrieval.
- **LongMemEval-S** - large-scale benchmark (23,867 docs, ~48 sessions per question) testing 6 memory abilities including knowledge update, temporal reasoning, and multi-session synthesis.

**LoCoMo** - 96.1% overall accuracy (1,982 questions, 272 docs).

**LongMemEval-S** - 92.8% overall accuracy (500 questions, 23,867 docs).

<p align="center">
<img src="assets/images/benchmarks/longmemeval-s-by-category.png" alt="LongMemEval-S Bench...