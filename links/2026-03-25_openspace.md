---
title: "HKUDS/OpenSpace"
source: "https://github.com/HKUDS/OpenSpace"
date: 2026-03-25
tags: ["AI Agents", "Self-Evolving", "MCP", "Python", "HKUDS"]
platform: github
author: null
summary: "OpenSpace is an open-source framework designed to make AI agents smarter, low-cost, and self-evolving through skill sharing and experience aggregation across platforms like Claude Code and Codex."
---
# HKUDS/OpenSpace

**URL:** https://github.com/HKUDS/OpenSpace
**Description:** "OpenSpace: Make Your Agents: Smarter, Low-Cost, Self-Evolving" -- Community: https://open-space.cloud/
**Language:** Python
**Stars:** 4982 | **Forks:** 601
**License:** MIT License
**Last updated:** 2026-04-10

## README (excerpt)

<div align="center">

<picture>
    <img src="assets/logo.png" width="320px" style="border: none; box-shadow: none;" alt="OpenSpace Logo">
</picture>

## ✨ OpenSpace: Make Your Agents: Smarter, Low-Cost, Self-Evolving ✨

| 🔋 **46% Fewer Tokens** | **💰 $11K earned in 6 Hours** | 🧬 **Self-Evolving Skills** | 🌐 **Agents Experience Sharing** |

[![Agents](https://img.shields.io/badge/Agents-Claude_Code%20%7C%20Codex%20%7C%20OpenClaw%20%7C%20nanobot%20%7C%20...-99C9BF.svg)](https://modelcontextprotocol.io/)
[![Python](https://img.shields.io/badge/Python-3.12+-FCE7D6.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-C1E5F5.svg)](https://opensource.org/licenses/MIT/)
[![Feishu](https://img.shields.io/badge/Feishu-Group-E9DBFC?style=flat&logo=larksuite&logoColor=white)](./COMMUNICATION.md)
[![WeChat](https://img.shields.io/badge/WeChat-Group-C5EAB4?style=flat&logo=wechat&logoColor=white)](./COMMUNICATION.md)
[![中文文档](https://img.shields.io/badge/文档-中文版-F5C6C6?style=flat)](./README_CN.md)

**One Command to Evolve All Your AI Agents**: OpenClaw, nanobot, Claude Code, Codex, Cursor and etc.

<img src="assets/cli-typing.gif" width="500px" alt="openspace --query your task">

</div>

---

## 📢 News

- **2026-04-09** 💬 Multi-channel **communication gateway**. OpenSpace can now receive and respond to messages from external platforms. Ships with **WhatsApp** (Baileys bridge + QR auth) and **Feishu** (HTTP webhook) adapters, session management, attachment caching, and allowlist-based access control. See [`openspace/config/README.md`](openspace/config/README.md) for setup.
- **2026-04-07** 🌐 OpenSpace MCP now supports standalone **SSE** and **streamable HTTP** startup, making it easier for remote hosts to connect over HTTP instead of stdio and bypass stdio-bound MCP server timeout bottlenecks. See the [host integration guide](openspace/host_skills/README.md) for setup details.
- **2026-04-06** 🛠️ Fixed multiple runtime issues across grounding, MCP serving, skill evolution, and persistence, improving execution stability and recovery in long-running workflows.
- **2026-04-05** 🧭 Cleaned up LLM credential resolution: centralized `.env` loading, improved host config auto-detection, and made provider-native env handling more consistent.
- **2026-04-03** 🚀 Released **v0.1.0** — Skill quality monitoring: structural patterns extracted from high-quality skills now evaluate every new submission daily. Faster, more relevant cloud search. Production-grade vertical skill clusters emerging organically from the community. Frontend now supports Chinese (zh) i18n.
- **2026-04-02** ⚡ Cloud search upgraded for higher relevance and lower latency.
- **2026-03-31** 🛡️ Security hardening: hardened zip extraction and `import_skill` against path traversal. CLI now respects `OPENSPACE_MODEL` and `OPENSPACE_LLM_*` env vars; MiniMax compatibility; workflow ID collision fixes.
- **2026-03-29** 🔒 Pinned litellm to <1.82.7 to avoid PYSEC-2026-2 supply-chain atta...