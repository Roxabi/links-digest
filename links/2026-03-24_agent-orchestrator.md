---
title: "ComposioHQ/agent-orchestrator"
source: "https://github.com/ComposioHQ/agent-orchestrator/"
date: 2026-03-24
tags: ["orchestration", "parallel-agents", "multi-agent", "git-worktrees", "ai-agents"]
platform: github
author: null
summary: "Agent Orchestrator is an orchestration layer for managing parallel AI coding agents that autonomously handle CI fixes, code reviews, and merge conflicts using isolated git worktrees."
---
# ComposioHQ/agent-orchestrator

**URL:** https://github.com/ComposioHQ/agent-orchestrator
**Description:**  Agentic orchestrator for parallel coding agents — plans tasks, spawns agents, and autonomously handles CI    fixes, merge conflicts, and code reviews.
**Language:** TypeScript
**Stars:** 6164 | **Forks:** 833
**License:** MIT License
**Topics:** claude-code, codex-cli, orchestration, orchestrator, skills, agent-fleet, agent-swarm, git-worktrees, multi-agent, parallel-agents, parallel-coding, tmux
**Homepage:** https://composio.dev
**Last updated:** 2026-04-11

## README (excerpt)

<h1 align="center">Agent Orchestrator — The Orchestration Layer for Parallel AI Agents</h1>

<p align="center">
<a href="https://github.com/ComposioHQ/agent-orchestrator">
  <img width="800" alt="Agent Orchestrator banner" src="docs/assets/agent_orchestrator_banner.png">
</a>
</p>

<div align="center">

Spawn parallel AI coding agents, each in its own git worktree. Agents autonomously fix CI failures, address review comments, and open PRs — you supervise from one dashboard.

[![GitHub stars](https://img.shields.io/github/stars/ComposioHQ/agent-orchestrator?style=flat-square)](https://github.com/ComposioHQ/agent-orchestrator/stargazers)
[![npm version](https://img.shields.io/npm/v/%40aoagents%2Fao?style=flat-square)](https://www.npmjs.com/package/@aoagents/ao)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![PRs merged](https://img.shields.io/badge/PRs_merged-61-brightgreen?style=flat-square)](https://github.com/ComposioHQ/agent-orchestrator/pulls?q=is%3Amerged)
[![Tests](https://img.shields.io/badge/test_cases-3%2C288-blue?style=flat-square)](https://github.com/ComposioHQ/agent-orchestrator/releases/tag/metrics-v1)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=flat-square&logo=discord&logoColor=white)](https://discord.gg/UZv7JjxbwG)

</div>

---

Agent Orchestrator manages fleets of AI coding agents working in parallel on your codebase. Each agent gets its own git worktree, its own branch, and its own PR. When CI fails, the agent fixes it. When reviewers leave comments, the agent addresses them. You only get pulled in when human judgment is needed.

**Agent-agnostic** (Claude Code, Codex, Aider) · **Runtime-agnostic** (tmux, Docker) · **Tracker-agnostic** (GitHub, Linear)

<div align="center">

## See it in action

<a href="https://x.com/agent_wrapper/status/2026329204405723180">
  <img src="docs/assets/demo-video-tweet.png" alt="Agent Orchestrator demo — AI agents building their own orchestrator" width="560">
</a>
<br><br>
<a href="https://x.com/agent_wrapper/status/2026329204405723180"><img src="docs/assets/btn-watch-demo.png" alt="Watch the Demo on X" height="48"></a>
<br><br><br>
<a href="https://x.com/agent_wrapper/status/2025986105485733945">
  <img src="docs/assets/article-tweet.png" alt="The Self-Improving AI System That Built Itself" width="560">
</a>
<br><br>
<a href="https://x.com/agent_wrapper/status/2025986105485733945"><img src="docs/assets/btn-read-article.png" alt="Read the Full Article on X" height="48"></a>

</div>

## Quick Start

> **Prerequisites:** [Node.js 20+](https://nodejs.org), [Git 2.25+](https://git-scm.com), [tmux](https://github.com/tmux/tmux/wiki/Installing), [`gh` CLI](https://cli.github.com). Install tmux via `brew install tmux` (macOS) or `sudo apt install tmux` (Linux).

### Install

```bash
npm install -g @aoagents/ao
```

<details>
<summary>Permission denied? Install from source?</summary>

If `npm install -g` fails with EACCES, pr...