---
title: "0xSero/orchestra"
source: "https://github.com/0xSero/orchestra"
date: 2025-12-18
tags: ["AI orchestration plugin", "multi-agent coordination", "TypeScript project", "workflow automation", "OpenCode integration"]
platform: github
author: "0xSero"
summary: "Open Orchestra is a multi-agent orchestration plugin for OpenCode that spawns and coordinates specialized AI workers using a hub-and-spoke architecture."
---
# 0xSero/orchestra

**URL:** https://github.com/0xSero/orchestra
**Description:** 
**Language:** TypeScript
**Stars:** 273 | **Forks:** 17
**Last updated:** 2026-01-16

## README (excerpt)

<p align="center">
  
</p>

<p align="center">
  <a href="https://github.com/0xSero/open-orchestra/releases"><img src="https://img.shields.io/badge/version-v0.1.0-blue.svg" alt="Version"></a>
  <a href="https://github.com/0xSero/open-orchestra/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"></a>
  <a href="https://bun.sh"><img src="https://img.shields.io/badge/runtime-Bun-f9f1e1.svg" alt="Bun"></a>
  <a href="https://opencode.ai"><img src="https://img.shields.io/badge/platform-OpenCode-6495ED.svg" alt="OpenCode"></a>
</p>

<p align="center">
  <strong>Spawn, manage, and coordinate specialized AI workers in OpenCode</strong>
</p>

---

## Overview

**Open Orchestra** is a monorepo that ships the orchestrator plugin, control panel, and desktop shell for OpenCode.

### Repo in 10 minutes

Mental model:
- **Workers**: orchestrator-managed runtimes that do the work.
- **Workflows**: multi-step plans the orchestrator runs across workers.
- **Memory**: persistent records written by workflows and tools.

The 3 commands:
- `bun run dev` — developer loop (plugin watch + control panel)
- `bun run build` — release build (plugin + app + desktop)
- `opencode` + plugin install — user flow (add `opencode-orchestrator` to OpenCode config)

---

**Open Orchestra** is a multi-agent orchestration plugin for [OpenCode](https://opencode.ai) that enables you to spawn, manage, and coordinate specialized AI workers. It implements a **hub-and-spoke architecture** where a central orchestrator coordinates multiple specialized workers, each optimized for specific tasks.

### Why Multiple AI Workers?

Instead of asking one AI to do everything, Open Orchestra lets you use specialized workers:

| Worker | Best For | Example |
|--------|----------|---------|
| **Vision** | Analyzing screenshots, images, UI mockups | "What error is shown in this screenshot?" |
| **Docs** | Researching APIs, finding examples | "How do I use React's useEffect hook?" |
| **Coder** | Writing and modifying code | "Implement this feature" |
| **Architect** | System design, planning (read-only) | "Review this architecture" |

This specialization means better results, clearer reasoning, and the ability to run tasks in parallel.

## Prerequisites

Before installing Open Orchestra, verify you have:

| Requirement | Check Command | Expected |
|-------------|---------------|----------|
| Bun runtime | `bun --version` | 1.0.0 or higher |
| OpenCode CLI | `opencode --version` | Any recent version |
| AI Provider | `orchestrator.models` (in OpenCode) | At least one model listed |

**Quick verification:**

```bash
bun --version && opencode --version
```

**Need to configure a provider?** Add to `~/.config/opencode/opencode.json`:

```json
{
  "provider": {
    "anthropic": {
      "apiKey": "sk-ant-your-key-here"
    }
  }
}
```

See the [Quickstart Guide](./docs/quickstart.md) for detailed setup instructions.

### Key Features

- **6 Built-in Worker Profiles** - Vi...