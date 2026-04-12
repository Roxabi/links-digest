---
title: "ksimback/hermes-ecosystem"
source: "https://github.com/ksimback/hermes-ecosystem"
date: 2026-04-08
tags: ["hermes-agent", "nous-research", "ai-agents", "directory", "rag"]
platform: github
author: null
summary: "Hermes Atlas is a curated directory and RAG-powered chatbot mapping the Hermes Agent ecosystem with over 80 tools and integrations."
---
# ksimback/hermes-ecosystem

**URL:** https://github.com/ksimback/hermes-ecosystem
**Description:** 🗺️ Hermes Atlas — the community map of every tool, skill, and integration for Hermes Agent by Nous Research. Live at hermesatlas.com
**Language:** HTML
**Stars:** 179 | **Forks:** 9
**Topics:** ai-agents, ecosystem-map, hermes-agent, nous-research, hermes-atlas
**Homepage:** https://hermesatlas.com
**Last updated:** 2026-04-11

## README (excerpt)

# 🗺️ Hermes Atlas

**The community-curated map of every tool, skill, and integration for [Hermes Agent](https://github.com/NousResearch/hermes-agent) by [Nous Research](https://nousresearch.com).**

🌐 **Live site:** [hermesatlas.com](https://hermesatlas.com)

---

## What is this?

Hermes Atlas is a living directory of the Hermes Agent ecosystem. Hermes Agent (the self-improving AI agent from Nous Research) launched in February 2026 and immediately spawned a fast-growing community of skills, plugins, integrations, deployment templates, and forks. This site is the canonical map of all of it.

**Features:**
- **80+ quality-filtered repos** across 12 categories — every project security-reviewed before inclusion
- **Live star counts** fetched from the GitHub API and cached in Redis
- **Sparklines and trending badges** showing growth over time
- **RAG-powered chatbot** ("Ask the Atlas") that answers questions about Hermes Agent grounded in 27 research files
- **Search, sort, filter** across the entire ecosystem
- **Light and dark mode** with OS preference detection
- **Mobile responsive**

## How it works

```
┌─────────────────────────────────────────────────────────────┐
│  hermesatlas.com (Vercel static + serverless)               │
│                                                              │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐    │
│  │ index.html  │  │ /api/stars   │  │ /api/chat        │    │
│  │ (the map)   │  │ (live data)  │  │ (RAG chatbot)    │    │
│  └─────────────┘  └──────┬───────┘  └────────┬─────────┘    │
│                          │                    │              │
│                          ▼                    ▼              │
│                   ┌──────────┐         ┌────────────┐       │
│                   │  Redis   │         │ OpenRouter │       │
│                   │  Cloud   │         │  (Gemma 4) │       │
│                   └────┬─────┘         └────────────┘       │
│                        │                                     │
│                        ▼                                     │
│                  ┌──────────┐                                │
│                  │ GitHub   │                                │
│                  │ GraphQL  │                                │
│                  └──────────┘                                │
└─────────────────────────────────────────────────────────────┘
```

**Stack:**
- **Frontend:** Vanilla HTML/CSS/JavaScript (no framework, no build step)
- **Hosting:** Vercel (static + serverless functions)
- **Cache:** Redis Cloud (1hr TTL on star counts, daily history snapshots)
- **LLM:** OpenRouter with fallback chain (Gemma 4 31B → Gemma 4 26B → Gemini 3 Flash)
- **Embeddings:** OpenAI text-embedding-3-small (computed once at build time, cached as static JSON)
- **Retrieval:** Hybrid BM25 + cosine similarity, MMR re-ranking, conversation-aware query rewriting

## Repository structure

```
hermes/
├── index.html              # The map (sin...