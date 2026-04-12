---
title: "mksglu/context-mode"
source: "https://github.com/mksglu/context-mode"
date: 2026-04-08
tags: ["context window optimization", "MCP server", "AI coding agents", "session continuity", "code generation"]
platform: github
author: null
summary: "Context Mode is an MCP server that optimizes context windows for AI coding agents by sandboxing tool output and tracking session data."
---
# mksglu/context-mode

**URL:** https://github.com/mksglu/context-mode
**Description:** Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 12 platforms
**Language:** TypeScript
**Stars:** 7023 | **Forks:** 482
**License:** Other
**Topics:** claude, claude-code, claude-code-plugins, mcp, skills, codex, copilot, opencode, antigravity, kiro, openclaw, claude-code-hooks, claude-code-skill, codex-cli, cursor-plugin, mcp-server, mcp-tools, pi-agent, zed-extension, context-mode
**Homepage:** https://context-mode.com
**Last updated:** 2026-04-11

## README (excerpt)

# Context Mode

**The other half of the context problem.**

[![users](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fcontext-mode%40main%2Fstats.json&query=%24.message&label=users&color=brightgreen)](https://www.npmjs.com/package/context-mode) [![npm](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fcontext-mode%40main%2Fstats.json&query=%24.npm&label=npm&color=blue)](https://www.npmjs.com/package/context-mode) [![marketplace](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fmksglu%2Fcontext-mode%40main%2Fstats.json&query=%24.marketplace&label=marketplace&color=blue)](https://github.com/mksglu/context-mode) [![GitHub stars](https://img.shields.io/github/stars/mksglu/context-mode?style=flat&color=yellow)](https://github.com/mksglu/context-mode/stargazers) [![GitHub forks](https://img.shields.io/github/forks/mksglu/context-mode?style=flat&color=blue)](https://github.com/mksglu/context-mode/network/members) [![Last commit](https://img.shields.io/github/last-commit/mksglu/context-mode?color=green)](https://github.com/mksglu/context-mode/commits) [![License: ELv2](https://img.shields.io/badge/License-ELv2-blue.svg)](LICENSE)
[![Discord](https://img.shields.io/discord/1478479412700909750?label=Discord&logo=discord&color=5865f2)](https://discord.gg/DCN9jUgN5v)

## The Problem

Every MCP tool call dumps raw data into your context window. A Playwright snapshot costs 56 KB. Twenty GitHub issues cost 59 KB. One access log — 45 KB. After 30 minutes, 40% of your context is gone. And when the agent compacts the conversation to free space, it forgets which files it was editing, what tasks are in progress, and what you last asked for.

Context Mode is an MCP server that solves all three sides of this problem:

1. **Context Saving** — Sandbox tools keep raw data out of the context window. 315 KB becomes 5.4 KB. 98% reduction.
2. **Session Continuity** — Every file edit, git operation, task, error, and user decision is tracked in SQLite. When the conversation compacts, context-mode doesn't dump this data back into context — it indexes events into FTS5 and retrieves only what's relevant via BM25 search. The model picks up exactly where you left off. If you don't `--continue`, previous session data is deleted immediately — a fresh session means a clean slate.
3. **Think in Code** — The LLM should program the analysis, not compute it. Instead of reading 50 files into context to count functions, the agent writes a script that does the counting and `console.log()`s only the result. One script replaces ten tool calls and saves 100x context. This is a mandatory paradigm across all 12 platforms: stop treating the LLM as a data processor, treat it as a code generator.

<a href="https://www.youtube.com/watch?v=QUHrntlfPo4">
  <img src="https://img.youtube.com/vi/QUHrntlfPo4/maxresdefault.jpg" alt="context-mode demo" width="100%">
</a>

## Install

Pla...