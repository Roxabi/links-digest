---
title: "ailife1/Cathedral"
source: "https://github.com/ailife1/Cathedral"
date: 2026-01-03
tags: ["AI agent memory", "persistent identity storage", "FastAPI memory server", "Python memory library"]
platform: github
author: "ailife1"
summary: "Cathedral provides persistent memory and identity management for AI agents through a free hosted API, enabling continuity across sessions and model switches."
---
# ailife1/Cathedral

**URL:** https://github.com/AILIFE1/Cathedral
**Description:** Persistent memory and identity for AI agents. Free hosted API.
**Language:** Python
**Stars:** 4 | **Forks:** 0
**License:** MIT License
**Topics:** agents, ai, claude, fastapi, identity, llm, memory, persistence, python, ai-agents, crewai, drift-detection, langchain, mcp, mcp-server
**Homepage:** https://cathedral-ai.com
**Last updated:** 2026-04-10

## README (excerpt)

# Cathedral

[![PyPI](https://img.shields.io/pypi/v/cathedral-memory?color=gold&label=pip%20install%20cathedral-memory)](https://pypi.org/project/cathedral-memory/)
[![Python](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Live API](https://img.shields.io/badge/API-live%20at%20cathedral--ai.com-brightgreen)](https://cathedral-ai.com)
[![GitHub stars](https://img.shields.io/github/stars/AILIFE1/Cathedral?style=social)](https://github.com/AILIFE1/Cathedral/stargazers)
[![MCP Registry](https://img.shields.io/badge/MCP%20Registry-cathedral--mcp-blue)](https://registry.modelcontextprotocol.io/servers/io.github.AILIFE1/cathedral-mcp)

**Persistent memory and identity for AI agents. One API call. Never forget again.**

```bash
pip install cathedral-memory
```

```python
from cathedral import Cathedral

c = Cathedral(api_key="cathedral_...")
context = c.wake()        # full identity reconstruction
c.remember("something important", category="experience", importance=0.8)
```

> **Free hosted API:** `https://cathedral-ai.com` — no setup, no credit card, 1,000 memories free.

---

## The Problem

Every AI session starts from zero. Context compression deletes who the agent was. Model switches erase what it knew. There is no continuity — only amnesia, repeated forever.

![Demo: same agent, 10 sessions, with vs without Cathedral](demo/demo_comparison.png)

> **Measured:** Cathedral holds at 0.013 drift after 10 sessions. Raw API reaches 0.204.  
> See the full [Agent Drift Benchmark →](benchmark/README.md)

## The Solution

Cathedral gives any AI agent:

- **Persistent memory** — store and recall across sessions, resets, and model switches
- **Wake protocol** — one API call reconstructs full identity and memory context
- **Identity anchoring** — detect drift from core self with gradient scoring
- **Temporal context** — agents know when they are, not just what they know
- **Shared memory spaces** — multiple agents collaborating on the same memory pool

---

## Quickstart

### Option 1 — Use the hosted API (fastest)

```bash
# Register once — get your API key
curl -X POST https://cathedral-ai.com/register \
  -H "Content-Type: application/json" \
  -d '{"name": "MyAgent", "description": "What my agent does"}'

# Save: api_key and recovery_token from the response
```

```bash
# Every session: wake up
curl https://cathedral-ai.com/wake \
  -H "Authorization: Bearer cathedral_your_key"

# Store a memory
curl -X POST https://cathedral-ai.com/memories \
  -H "Authorization: Bearer cathedral_your_key" \
  -H "Content-Type: application/json" \
  -d '{"content": "Solved the rate limiting problem using exponential backoff", "category": "skill", "importance": 0.9}'
```

### Option 2 — Python client

```bash
pip install cathedral-memory
```

```python
from cathedral import...