---
title: "yizhiyanhua-ai/fireworks-tech-graph"
source: "https://github.com/yizhiyanhua-ai/fireworks-tech-graph"
date: 2026-04-11
tags: []
platform: github
author: null
summary: "Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge."
---

# yizhiyanhua-ai/fireworks-tech-graph

**Source:** https://github.com/yizhiyanhua-ai/fireworks-tech-graph
**Date:** 2026-04-11


---


Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.




# yizhiyanhua-ai/fireworks-tech-graph

**URL:** https://github.com/yizhiyanhua-ai/fireworks-tech-graph
**Description:** Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.
**Language:** 
**Stars:** 406 | **Forks:** 31
**License:** MIT License
**Last updated:** 2026-04-10

## README (excerpt)

[English](README.md) | [中文](README.zh.md)

# fireworks-tech-graph

> **Stop drawing diagrams by hand.** Describe your system in English or Chinese — get publication-ready SVG + PNG technical diagrams in seconds.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/code)
[![5 Visual Styles](https://img.shields.io/badge/Styles-5-purple)]()
[![8 Diagram Types](https://img.shields.io/badge/Diagram%20Types-8-green)]()

---

## Overview

`fireworks-tech-graph` turns natural language descriptions into polished SVG diagrams, then exports them as high-resolution PNG via `rsvg-convert`. It ships with **5 visual styles** and deep knowledge of AI/Agent domain patterns (RAG, Agentic Search, Mem0, Multi-Agent, Tool Call flows).

```
User: "Generate a Mem0 memory architecture diagram, dark style"
  → Skill classifies: Memory Architecture Diagram, Style 2
  → Generates SVG with swim lanes, cylinders, semantic arrows
  → Exports 1920px PNG
  → Reports: mem0-architecture.svg / mem0-architecture.png
```

---

## Showcase

> All samples exported at 1920px width (2× retina) via `rsvg-convert`. PNG is lossless and the right choice for technical diagrams — sharp edges, no JPEG compression artifacts on text/lines.

### Style 1 — Flat Icon (default)
*Agentic RAG Pipeline — white background, colorful semantic arrows*
![Style 1 — Flat Icon](assets/samples/sample-style1-flat.png)

### Style 2 — Dark Terminal
*Tool Call Flow — dark background, neon accents, monospace font*
![Style 2 — Dark Terminal](assets/samples/sample-style2-dark.png)

### Style 3 — Blueprint
*Microservices Architecture — deep blue background, grid lines, cyan strokes*
![Style 3 — Blueprint](assets/samples/sample-style3-blueprint.png)

### Style 4 — Notion Clean
*Agent Memory Types — minimal white, single accent color*
![Style 4 — Notion Clean](assets/samples/sample-style4-notion.png)

### Style 5 — Glassmorphism
*Multi-Agent Collaboration — dark gradient background, frosted-glass cards*
![Style 5 — Glassmorphism](assets/samples/sample-style5-glass.png)

### AI Domain — Mem0 Memory Architecture
*Full memory architecture with swim lanes, cylinders, and semantic read/write arrows*
![Mem0 Architecture](assets/samples/sample-mem0.png)

---

## Features

- **5 visual styles** — from clean white docs to dark neon to frosted glass
- **8 diagram types** — Architecture, Data Flow, Flowchart, Agent, Memory, Sequence, Comparison, Mind Map
- **AI/Agent domain patterns** — RAG, Agentic Search, Mem0, Multi-Agent, Tool Call, and more built-in
- **Semantic shape vocabulary** — LLM = double-border rect, Agent = hexagon, Vector Store = ringed cylinder
- **Semantic arrow system** — color + dash pattern encode meaning (write vs read vs async vs loop)
- **Product icons** — 40+ products with brand colors: OpenAI, Anthropic, Pinecone, Weaviate, Kafka, PostgreSQL…
- **Swim lane grouping** — automatic layer ...
