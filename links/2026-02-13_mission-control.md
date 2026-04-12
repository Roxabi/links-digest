---
title: "builderz-labs/mission-control"
source: "https://github.com/builderz-labs/mission-control"
date: 2026-02-13
tags: ["AI agent orchestration", "self-hosted dashboard", "task management", "multi-agent workflows", "open-source platform"]
platform: github
author: "builderz-labs"
summary: "Mission Control is an open-source, self-hosted AI agent orchestration dashboard for managing agent fleets, dispatching tasks, and tracking costs."
---
# builderz-labs/mission-control

**URL:** https://github.com/builderz-labs/mission-control
**Description:** Self-hosted AI agent orchestration platform: dispatch tasks, run multi-agent workflows, monitor spend, and govern operations from one mission control dashboard.
**Language:** TypeScript
**Stars:** 3992 | **Forks:** 686
**License:** MIT License
**Topics:** agent-orchestration, dashboard, nextjs, openclaw, sqlite, ai-agents, ai-automation, ai-dashboard, claude, developer-tools, llm, mcp, open-source, self-hosted, task-management, typescript
**Homepage:** https://mc.builderz.dev
**Last updated:** 2026-04-11

## README (excerpt)

<div align="center">

# Mission Control

**Open-source dashboard for AI agent orchestration.**

Manage AI agent fleets, dispatch tasks, track costs, and coordinate multi-agent workflows — self-hosted, zero external dependencies, powered by SQLite.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Next.js 16](https://img.shields.io/badge/Next.js-16-black?logo=next.js)](https://nextjs.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.7-3178C6?logo=typescript&logoColor=white)](https://typescriptlang.org/)
[![Tests](https://img.shields.io/badge/Tests-577%20(282%20unit%20%2B%20295%20E2E)-brightgreen)](https://github.com/builderz-labs/mission-control)
[![GitHub stars](https://img.shields.io/github/stars/builderz-labs/mission-control?style=social)](https://github.com/builderz-labs/mission-control/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/builderz-labs/mission-control?style=social)](https://github.com/builderz-labs/mission-control/network/members)
[![Last commit](https://img.shields.io/github/last-commit/builderz-labs/mission-control)](https://github.com/builderz-labs/mission-control/commits/main)
[![Open issues](https://img.shields.io/github/issues/builderz-labs/mission-control)](https://github.com/builderz-labs/mission-control/issues)

![Mission Control Dashboard](docs/mission-control-overview.png)

</div>

---

> **Alpha Software** — Mission Control is under active development. APIs, database schemas, and configuration formats may change between releases. Review the [security considerations](#security) before deploying to production.

## Contents

- [Quick Start](#quick-start)
- [Why teams adopt Mission Control](#why-teams-adopt-mission-control)
- [Use-case recipes](#use-case-recipes)
- [Getting Started with Agents](#getting-started-with-agents)
- [Documentation](#documentation)
- [Features](#features)
- [Architecture](#architecture)
- [API Reference](#api-reference)
- [Development](#development)
- [Troubleshooting](#troubleshooting)
- [Security](#security)
- [Built with Mission Control](#built-with-mission-control)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Support](#support)
- [License](#license)

<table>
<tr><td><b>32 panels</b></td><td>Tasks, agents, skills, logs, tokens, memory, security, cron, alerts, webhooks, pipelines, and more — all from a single SPA shell.</td></tr>
<tr><td><b>Real-time everything</b></td><td>WebSocket + SSE push updates with smart polling that pauses when you're away. Zero stale data.</td></tr>
<tr><td><b>Zero external deps</b></td><td>SQLite database, single <code>pnpm start</code> to run. No Redis, no Postgres, no Docker required.</td></tr>
<tr><td><b>Role-based access</b></td><td>Viewer, operator, and admin roles with session + API key auth. Google Sign-In with admin approval workflow.</td></tr>
<tr><td><b>Quality gates</b></td><td>Built-in Aegis review system that blocks task completion without sign-off.</td></tr>
<tr><td><b>Skills Hub</b...