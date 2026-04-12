---
title: "disler/pi-vs-claude-code"
source: "https://github.com/disler/pi-vs-claude-code/tree/main"
date: 2026-04-06
tags: ["github", "coding-agent", "open-source", "typescript", "comparison"]
platform: github
author: null
summary: "This GitHub repository compares the open-source Pi Coding Agent with Claude Code, offering customized instances for UI, orchestration, and safety auditing."
---
# disler/pi-vs-claude-code

**URL:** https://github.com/disler/pi-vs-claude-code
**Description:** Comparison between open source PI agent and closed source Claude Code agent
**Language:** TypeScript
**Stars:** 702 | **Forks:** 205
**Last updated:** 2026-04-11

## README (excerpt)

# pi-vs-cc

A collection of [Pi Coding Agent](https://github.com/mariozechner/pi-coding-agent) customized instances. _Why?_ To showcase what it looks like to hedge against the leader in the agentic coding market, Claude Code. Here we showcase how you can customize the UI, agent orchestration tools, safety auditing, and cross-agent integrations. 

> Watch the [video](https://youtu.be/f8cfH5XX-XU) to see pi in action.

<div align="center">
  <img src="./images/pi-logo.png" alt="pi-vs-cc" width="700">
</div>

---

## Prerequisites

All three are required:

| Tool            | Purpose                   | Install                                                    |
| --------------- | ------------------------- | ---------------------------------------------------------- |
| **Bun** ≥ 1.3.2 | Runtime & package manager | [bun.sh](https://bun.sh)                                   |
| **just**        | Task runner               | `brew install just`                                        |
| **pi**          | Pi Coding Agent CLI       | [Pi docs](https://github.com/mariozechner/pi-coding-agent) |

---

## API Keys

Pi does **not** auto-load `.env` files — API keys must be present in your shell's environment **before** you launch Pi. A sample file is provided:

```bash
cp .env.sample .env   # copy the template
# open .env and fill in your keys
```

`.env.sample` covers the four most popular providers:

| Provider         | Variable             | Get your key                                                                                               |
| ---------------- | -------------------- | ---------------------------------------------------------------------------------------------------------- |
| OpenAI           | `OPENAI_API_KEY`     | [platform.openai.com](https://platform.openai.com/api-keys)                                                |
| Anthropic        | `ANTHROPIC_API_KEY`  | [console.anthropic.com](https://console.anthropic.com/settings/keys)                                       |
| Google           | `GEMINI_API_KEY`     | [aistudio.google.com](https://aistudio.google.com/app/apikey)                                              |
| OpenRouter       | `OPENROUTER_API_KEY` | [openrouter.ai](https://openrouter.ai/keys)                                                                |
| Many Many Others | `***`                | [Pi Providers docs](https://github.com/badlogic/pi-mono/blob/main/packages/coding-agent/docs/providers.md) |

### Sourcing your keys

Pick whichever approach fits your workflow:

**Option A — Source manually each session:**
```bash
source .env && pi
```

**Option B — One-liner alias (add to `~/.zshrc` or `~/.bashrc`):**
```bash
alias pi='source $(pwd)/.env && pi'
```

**Option C — Use the `just` task runner (auto-wired via `set dotenv-load`):**
```bash
just pi           # .env is loaded automatically for every just recipe
just ext-minimal  # works for all recipes, not just `pi`
```

---

## Installation

```bash
bu...