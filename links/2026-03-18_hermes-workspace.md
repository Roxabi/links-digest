---
title: "outsourc-e/hermes-workspace"
source: "https://github.com/outsourc-e/hermes-workspace"
date: 2026-03-18
tags: ["AI agent workspace", "web terminal interface", "memory management system", "React TypeScript app", "OpenAI compatible backend"]
platform: github
author: null
summary: "Hermes Workspace is a native web workspace for AI agents that provides chat, terminal, memory, skills, and inspector features in one unified interface."
---
# outsourc-e/hermes-workspace

**URL:** https://github.com/outsourc-e/hermes-workspace
**Description:** Native web workspace for Hermes Agent — chat, terminal, memory, skills, inspector.
**Language:** TypeScript
**Stars:** 1135 | **Forks:** 118
**License:** MIT License
**Topics:** agent-ui, ai-workspace, hackathon, hermes-agent, nous-research, react, typescript
**Homepage:** https://hermes-workspace.com
**Last updated:** 2026-04-11

## README (excerpt)

<div align="center">

<img src="./public/hermes-avatar.webp" alt="Hermes Workspace" width="80" style="border-radius: 16px" />

# Hermes Workspace

**Your AI agent's command center — chat, files, memory, skills, and terminal in one place.**

[![Version](https://img.shields.io/badge/version-1.0.0-6366F1.svg)](CHANGELOG.md)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Node](https://img.shields.io/badge/node-%3E%3D22.0.0-brightgreen.svg)](https://nodejs.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-6366F1.svg)](CONTRIBUTING.md)

> Not a chat wrapper. A complete workspace — orchestrate agents, browse memory, manage skills, and control everything from one interface.

![Hermes Workspace](./docs/screenshots/splash.png)

</div>

---

## ✨ Features

- 🤖 **Hermes Agent Integration** — Direct gateway connection with real-time SSE streaming
- 🎨 **8-Theme System** — Official, Classic, Slate, Mono — each with light and dark variants
- 🔒 **Security Hardened** — Auth middleware on all API routes, CSP headers, exec approval prompts
- 📱 **Mobile-First PWA** — Full feature parity on any device via Tailscale
- ⚡ **Live SSE Streaming** — Real-time agent output with tool call rendering
- 🧠 **Memory & Skills** — Browse, search, and edit agent memory; explore 2,000+ skills

---

## 📸 Screenshots

|                 Chat                 |                 Files                  |
| :----------------------------------: | :------------------------------------: |
| ![Chat](./docs/screenshots/chat.png) | ![Files](./docs/screenshots/files.png) |

|                   Terminal                   |                  Memory                  |
| :------------------------------------------: | :--------------------------------------: |
| ![Terminal](./docs/screenshots/terminal.png) | ![Memory](./docs/screenshots/memory.png) |

|                  Skills                  |                   Settings                   |
| :--------------------------------------: | :------------------------------------------: |
| ![Skills](./docs/screenshots/skills.png) | ![Settings](./docs/screenshots/settings.png) |

---

## 🚀 Quick Start

Hermes Workspace works with any OpenAI-compatible backend. If your backend also exposes Hermes gateway APIs, enhanced features like sessions, memory, skills, and jobs unlock automatically.

### Prerequisites

- **Node.js 22+** — [nodejs.org](https://nodejs.org/)
- **An OpenAI-compatible backend** — local, self-hosted, or remote
- **Optional:** Python 3.11+ if you want to run a Hermes gateway locally

### Step 1: Start your backend

Point Hermes Workspace at any backend that supports:

- `POST /v1/chat/completions`
- `GET /v1/models` recommended

Example Hermes gateway setup:

```bash
git clone https://github.com/outsourc-e/hermes-agent.git
cd hermes-agent
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e .
hermes setup
hermes --gateway
```

If you're using another OpenAI-compa...