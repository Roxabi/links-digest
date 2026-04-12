---
title: "scalyclaw/scalyclaw"
source: "https://github.com/scalyclaw/scalyclaw"
date: 2026-02-24
tags: ["self-hosted AI assistant", "messaging channel integration", "horizontal scaling architecture", "open source project"]
platform: github
author: "scalyclaw"
summary: "ScalyClaw is a self-hosted AI assistant platform connecting multiple messaging channels with shared memory and autonomous code execution."
---
# scalyclaw/scalyclaw

**URL:** https://github.com/scalyclaw/scalyclaw
**Description:** The AI That Scales With You.
**Language:** TypeScript
**Stars:** 19 | **Forks:** 5
**License:** MIT License
**Homepage:** https://scalyclaw.com
**Last updated:** 2026-03-06

## README (excerpt)

<div align="center">

<table><tr><td>

<p align="center">⚖️ <strong>DISCLAIMER</strong></p>

💚 **ScalyClaw is a passion project — open source from day one, open source forever.**

🚫 No crypto token · No paid tier · No official channels outside this repo

📬 The only way to reach us is through **GitHub** — issues, discussions, PRs

🤝 We will never ask for money or personal data — only contributions to make this better

⚠️ **This is `sudo` for AI.** ScalyClaw executes code, manages secrets, and operates autonomously. Use it carefully, review what you deploy, and never run it in an environment you don't control.

</td></tr></table>

<br />

<img src="assets/logo.svg" alt="ScalyClaw" width="64" height="64" />

# ScalyClaw

**The AI That Scales With You.**

One mind · All channels · Continuous relationship.

[![MIT License](https://img.shields.io/badge/license-MIT-10b981?style=flat-square)](LICENSE)
[![Bun](https://img.shields.io/badge/runtime-Bun-f9a825?style=flat-square)](https://bun.sh)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-10b981?style=flat-square)](#-contributing)

</div>

---

## 🧠 What is ScalyClaw?

ScalyClaw is a **self-hosted AI assistant platform** that connects to all your messaging channels with a single shared mind. It remembers everything, runs code, delegates to agents, and scales horizontally — all under your control.

---

## 🏗️ Architecture

![Architecture](screenshots/architecture.png)

| Process | Role | Scalable |
|---|---|---|
| 🧠 **Node** | Orchestrator — channels, LLM loop, guards, memory, agents, scheduling | Singleton |
| ⚡ **Worker** | Execution — code, commands, skills via BullMQ | Horizontally |
| 📊 **Dashboard** | Web UI — monitoring, config, chat | — |

Workers are independently deployable. They share nothing with the node except Redis — no shared filesystem required.

---

## 📊 Dashboard

<div align="center">

| Overview | Mind | Usage |
|---|---|---|
| ![Overview](screenshots/overview.png) | ![Mind](screenshots/mind.png) | ![Usage](screenshots/usage.png) |

| Channels | Models | Agents |
|---|---|---|
| ![Channels](screenshots/channels.png) | ![Models](screenshots/models.png) | ![Agents](screenshots/agents.png) |

| Skills | Memory | Vault |
|---|---|---|
| ![Skills](screenshots/skills.png) | ![Memory](screenshots/memory.png) | ![Vault](screenshots/vault.png) |

| MCP | Scheduler | Engagement |
|---|---|---|
| ![MCP](screenshots/mcp.png) | ![Scheduler](screenshots/scheduler.png) | ![Engagement](screenshots/engagement.png) |

| Security | Logs | Workers |
|---|---|---|
| ![Security](screenshots/security.png) | ![Logs](screenshots/logs.png) | ![Workers](screenshots/workers.png) |

| Jobs |
|---|
| ![Jobs](screenshots/jobs.png) |

</div>

---

## ✨ Highlights

| | Feature | Description |
|---|---|---|
| 💬 | **7 Channels** | Discord, Telegram, Slack, WhatsApp, Signal, Teams, Web Gateway — one memory across all |
| 🧠 | **Persistent Memory** | Hybrid vector + full-text search (sqlite-vec + FTS5). Auto-extr...