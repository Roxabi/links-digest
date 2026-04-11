---
title: "yizhiyanhua-ai/fireworks-tech-graph"
source: "https://github.com/yizhiyanhua-ai/fireworks-tech-graph"
date: 2026-04-11
tags: ["diagram-generator", "claude-code", "svg", "technical-documentation", "ai-tools"]
platform: github
author: null
summary: "Fireworks-tech-graph is a Claude Code skill that generates production-quality SVG and PNG technical diagrams from natural language descriptions using various visual styles."
---
# yizhiyanhua-ai/fireworks-tech-graph

**URL:** https://github.com/yizhiyanhua-ai/fireworks-tech-graph
**Description:** Claude Code skill for generating production-quality SVG+PNG technical diagrams. Supports 8 diagram types, 5 visual styles, and deep AI/Agent domain knowledge.
**Language:** Shell
**Stars:** 894 | **Forks:** 69
**License:** MIT License
**Last updated:** 2026-04-11

## README (excerpt)

[English](README.md) | [中文](README.zh.md)

# fireworks-tech-graph

> **Stop drawing diagrams by hand.** Describe your system in English or Chinese — get publication-ready SVG + PNG technical diagrams in seconds.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code Skill](https://img.shields.io/badge/Claude%20Code-Skill-blue)](https://claude.ai/code)
[![7 Visual Styles](https://img.shields.io/badge/Styles-7-purple)]()
[![14 Diagram Types](https://img.shields.io/badge/Diagram%20Types-14-green)]()
[![UML Support](https://img.shields.io/badge/UML-Full%20Support-orange)]()

---

## Overview

`fireworks-tech-graph` turns natural language descriptions into polished SVG diagrams, then exports them as high-resolution PNG via `rsvg-convert`. It ships with **7 visual styles** and deep knowledge of AI/Agent domain patterns (RAG, Agentic Search, Mem0, Multi-Agent, Tool Call flows), plus full support for all 14 UML diagram types.

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
*Multi-Agent Collaboration — dark gradient background, s cards*
![Style 5 — Glassmorphism](assets/samples/sample-style5-glass.png)

### Style 6 — Claude Official
*System Architecture — warm cream background (#f8f6f3), Anthropic brand colors, clean professional aesthetic*
![Style 6 — Claude Official](assets/samples/sample-style6-claude.png)

### Style 7 — OpenAI Official
*API Integration Flow — pure white background, OpenAI brand palette, modern minimalist design*
![Style 7 — OpenAI Official](assets/samples/sample-style7-openai.png)

### AI Domain — Mem0 Memory Architecture
*Full memory architecture with swim lanes, cylinders, and semantic read/write arrows*
![Mem0 Architecture](assets/samples/sample-mem0.png)

---

## Features

- **7 visual styles** — from clean white docs to dark neon to frosted glass to official brand styles
- **14 diagram types** — ...