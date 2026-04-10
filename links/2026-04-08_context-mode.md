---
title: "Context Mode — MCP Server for AI Context Optimization"
source: "https://github.com/mksglu/context-mode"
date: 2026-04-08
tags: ['MCP', 'context optimization', 'AI coding', 'session continuity']
platform: github
author: null
summary: "An MCP (Model Context Protocol) server that optimizes context windows for AI coding agents by sandboxing tool outputs and maintaining session continui..."
---

# Context Mode — MCP Server for AI Context Optimization

**Source:** https://github.com/mksglu/context-mode
**Date:** 2026-04-08

---

An MCP (Model Context Protocol) server that optimizes context windows for AI coding agents by sandboxing tool outputs and maintaining session continuity.

### Main Features
- **Context Saving** — Sandbox tools keep raw tool output out of the context window, achieving "98% reduction" in context usage
- **Session Continuity** — SQLite database tracks "every file edit, git operation, task, error, and user decision" with FTS5 indexing and BM25 search for retrieval after context compaction
- **Think in Code** — Paradigm where the LLM writes analysis scripts instead of processing raw data directly

### Tech Stack
Node.js, TypeScript, SQLite with FTS5 full-text search, MCP protocol, plugin/hook architecture

### Supported Platforms
12 platforms including Claude Code, Gemini CLI, VS Code Copilot, Cursor, OpenCode, KiloCode, OpenClaw/Pi Agent, Codex CLI, Antigravity, Kiro, Zed, and Pi Coding Agent

### Use Cases
- Long coding sessions where context window exhaustion is a risk
- Recovery after conversation compaction to "pick up exactly where you left off"
- Teams using AI agents for complex multi-file refactoring
- Projects requiring persistent tracking of coding decisions across sessions