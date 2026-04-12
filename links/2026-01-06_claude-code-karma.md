---
title: "JayantDevkar/claude-code-karma"
source: "https://github.com/JayantDevkar/claude-code-karma"
date: 2026-01-06
tags: ["Claude Code dashboard", "session monitoring", "local-first tool", "observability dashboard"]
platform: github
author: "JayantDevkar"
summary: "Claude Code Karma is a local-first, open-source dashboard that visualizes Claude Code session data directly from ~/.claude/ files without cloud or telemetry."
---
# JayantDevkar/claude-code-karma

**URL:** https://github.com/JayantDevkar/claude-code-karma
**Description:** Dashboard for monitoring claude code sessions. 
**Language:** Python
**Stars:** 157 | **Forks:** 18
**License:** Apache License 2.0
**Topics:** agents, agentskills, claude-code, claude-code-plugin, claude-code-skills, dashboard, hooks, mcp, mcptool, mcptools, monitoring, observability, plugins, sessions, skills, visibility
**Last updated:** 2026-04-08

## README (excerpt)

<p align="center">
  <img src="docs/screenshots/banner.png" alt="Claude Code Karma" width="200" />
</p>

<h1 align="center">Claude Code Karma</h1>

<p align="center">
  <strong>Your Claude Code sessions deserve more than a terminal.</strong><br />
  A local-first, open-source dashboard that turns your <code>~/.claude/</code> data into a visual story — sessions, timelines, costs, and live activity, all on your machine.
</p>

<p align="center">
  <a href="https://www.apache.org/licenses/LICENSE-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg" alt="License: Apache-2.0" /></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.9+-blue.svg" alt="Python 3.9+" /></a>
  <a href="https://nodejs.org/"><img src="https://img.shields.io/badge/Node-18+-green.svg" alt="Node 18+" /></a>
  <a href="https://kit.svelte.dev/"><img src="https://img.shields.io/badge/SvelteKit-2-FF3E00.svg" alt="SvelteKit 2" /></a>
</p>

<br />

<p align="center">
  <a href="docs/screenshots/home.png" target="_blank">
    <img src="docs/screenshots/home.png" alt="Claude Code Karma Dashboard" width="100%" />
  </a>
</p>

## Why Claude Code Karma?

If you use Claude Code, you already have a goldmine of data sitting in `~/.claude/` — every session, every tool call, every token. But it's all buried in JSONL files you'll never read.

> **Warning: Claude Code only keeps session data for about 30 days.** Older JSONL files in `~/.claude/projects/` are automatically cleaned up. Since Karma reads directly from those files, deleted sessions will disappear from the dashboard too.

Claude Code Karma reads that local data and gives you a proper dashboard. No cloud. No accounts. No telemetry. Just your data, on your machine.

It works with both **Claude Code CLI** and **Claude Desktop** (Claude Code mode) sessions — any session that writes to `~/.claude/` shows up automatically.

## Features

### Session Browser

Browse all your Claude Code sessions in one place. Search by title, prompt, or slug. Filter by project. See live sessions at the top with real-time status badges.

<p align="center">
  <img src="docs/screenshots/sessions.png" alt="Session Browser" width="100%" />
</p>

### Session Timeline & Overview

Dive into any session to see exactly what happened — every prompt, tool call, thinking block, and response laid out chronologically. The overview tab shows key stats like message count, duration, model used, and which tools were called.

<p align="center">
  <img src="docs/screenshots/session-overview.png" alt="Session Overview" width="100%" />
</p>

<p align="center">
  <img src="docs/screenshots/session-timeline.png" alt="Session Timeline" width="100%" />
</p>

### Session Detail Tabs

Each session page has dedicated tabs that break down different aspects of what happened during the session.

**Tasks** — See all tasks Claude created and completed during the session, displayed in a flow view with status tracking.

<p align="center">
  ...