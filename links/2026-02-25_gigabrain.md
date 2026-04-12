---
title: "legendaryvibecoder/gigabrain"
source: "https://github.com/legendaryvibecoder/gigabrain"
date: 2026-02-25
tags: ["AI agent memory", "local-first storage", "SQLite database", "memory management plugin"]
platform: github
author: "legendaryvibecoder"
summary: "Gigabrain is a local-first memory layer for AI agents that captures, recalls, and syncs conversations across OpenClaw, Codex, and Claude platforms."
---
# legendaryvibecoder/gigabrain

**URL:** https://github.com/legendaryvibecoder/gigabrain
**Description:** Local-first memory layer for OpenClaw, Codex App, and Codex CLI: capture, recall, dedupe, and native sync.
**Language:** JavaScript
**Stars:** 189 | **Forks:** 20
**License:** MIT License
**Topics:** ai-agent, memory, openclaw, plugin, sqlite, ai-tools, claude, codex, local-first, mcp, obsidian, typescript
**Homepage:** https://github.com/legendaryvibecoder/gigabrain
**Last updated:** 2026-04-08

## README (excerpt)

# Gigabrain

<p align="center">
  <strong>Local-first memory for AI agents.</strong>
</p>

<p align="center">
  <a href="https://github.com/legendaryvibecoder/gigabrain/releases"><img src="https://img.shields.io/github/v/release/legendaryvibecoder/gigabrain?include_prereleases&style=for-the-badge" alt="GitHub release"></a>
  <a href="https://www.npmjs.com/package/@legendaryvibecoder/gigabrain"><img src="https://img.shields.io/npm/v/@legendaryvibecoder/gigabrain?style=for-the-badge" alt="npm version"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
  <a href="https://github.com/legendaryvibecoder/gigabrain/stargazers"><img src="https://img.shields.io/github/stars/legendaryvibecoder/gigabrain?style=for-the-badge" alt="GitHub Stars"></a>
  <img src="https://img.shields.io/badge/node-%3E%3D22-brightgreen?style=for-the-badge" alt="Node >=22">
</p>

<p align="center">
  <a href="docs/configuration.md">Configuration</a> ·
  <a href="CHANGELOG.md">Changelog</a> ·
  <a href="CONTRIBUTING.md">Contributing</a> ·
  <a href="SECURITY.md">Security</a> ·
  <a href="https://github.com/legendaryvibecoder/gigabrain/discussions">Discussions</a>
</p>

---

**Gigabrain** is a local-first memory stack for [OpenClaw](https://openclaw.ai) agents, Codex App, Codex CLI, Claude Code, and Claude Desktop. It converts conversations and native notes into durable, queryable memory, then injects the right context before each prompt so agents stay consistent across sessions.

Built for production use: SQLite-backed recall, deterministic dedupe/audit flows, native markdown sync, world model, Obsidian surface, and an optional web console for memory operations.

## Supported clients

| Host surface | Install | What Gigabrain owns |
| --- | --- | --- |
| **OpenClaw** | `openclaw plugins install` | Registry, native sync, recall orchestration, audit/nightly, memory-slot provider |
| **Codex App / CLI** | `npm install` + setup | Shared project/user memory store, MCP tools, checkpoints, maintenance |
| **Claude Code** | `npm install` + setup | Shared project/user memory store, MCP tools, managed `.mcp.json` wiring |
| **Claude Desktop** | `claude:desktop:bundle` | Same MCP-backed memory store and tools as Claude Code |

## Quickstart

### OpenClaw

```bash
openclaw plugins install @legendaryvibecoder/gigabrain
cd ~/.openclaw/extensions/gigabrain && npm run setup -- --workspace /path/to/workspace
npx gigabrainctl doctor --config ~/.openclaw/openclaw.json
```

> [Full setup guide](docs/setup-openclaw.md)

### Codex App / Codex CLI

```bash
npm install @legendaryvibecoder/gigabrain
npx gigabrain-codex-setup --project-root /path/to/repo
.codex/actions/verify-gigabrain.sh
```

> [Full setup guide](docs/setup-codex.md)

### Claude Code / Claude Desktop

```bash
npm install @legendaryvibecoder/gigabrain
npx gigabrain-claude-setup --project-root /path/to/repo
.claude/actions/verify-gigabrain.sh
```

> [Full setup gui...