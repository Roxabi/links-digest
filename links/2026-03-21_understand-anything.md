---
title: "Lum1104/Understand-Anything"
source: "https://github.com/Lum1104/Understand-Anything"
date: 2026-03-21
tags: ["knowledge graph", "code analysis", "multi-platform tool", "codebase visualization"]
platform: github
author: null
summary: "Understand Anything is a Claude Code plugin that converts codebases, Dockerfiles, and docs into interactive knowledge graphs for exploration."
---
# Lum1104/Understand-Anything

**URL:** https://github.com/Lum1104/Understand-Anything
**Description:** Skill that turn any codebase, Dockerfile, or docs into an interactive knowledge graph you can explore, search, and ask questions about. Multi-platform: Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.
**Language:** TypeScript
**Stars:** 8139 | **Forks:** 672
**License:** MIT License
**Topics:** claude-code, claude-skills, understandcode, codex, codex-skills, knowledge-graph, opencode-skills, antigravity-skills, gemini-cli-skills, pi-agent, business-knowledge, knowledge-base, memory
**Homepage:** https://lum.is-a.dev/Understand-Anything/
**Last updated:** 2026-04-11

## README (excerpt)

<h1 align="center">Understand Anything</h1>

<p align="center">
  <strong>Turn any codebase, Dockerfile, or docs into an interactive knowledge graph you can explore, search, and ask questions about.</strong>
  <br />
  <em>Works with Claude Code, Codex, Cursor, Copilot, Gemini CLI, and more.</em>
</p>

<p align="center">
  <a href="README.md">English</a> | <a href="README.zh-CN.md">简体中文</a> | <a href="README.zh-TW.md">繁體中文</a> | <a href="README.ja-JP.md">日本語</a> | <a href="README.tr-TR.md">Türkçe</a>
</p>

<p align="center">
 <a href="https://www.star-history.com/lum1104/understand-anything">
  <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/badge?repo=Lum1104/Understand-Anything&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/badge?repo=Lum1104/Understand-Anything" />
   <img alt="Star History Rank" src="https://api.star-history.com/badge?repo=Lum1104/Understand-Anything" />
  </picture>
 </a>
</p>

<p align="center">
  <a href="#-quick-start"><img src="https://img.shields.io/badge/Quick_Start-blue" alt="Quick Start" /></a>
  <a href="https://github.com/Lum1104/Understand-Anything/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="License: MIT" /></a>
  <a href="https://docs.anthropic.com/en/docs/claude-code"><img src="https://img.shields.io/badge/Claude_Code-8A2BE2" alt="Claude Code" /></a>
  <a href="#codex"><img src="https://img.shields.io/badge/Codex-000000" alt="Codex" /></a>
  <a href="#vs-code--github-copilot"><img src="https://img.shields.io/badge/Copilot-24292e" alt="Copilot" /></a>
  <a href="#gemini-cli"><img src="https://img.shields.io/badge/Gemini_CLI-4285F4" alt="Gemini CLI" /></a>
  <a href="#opencode"><img src="https://img.shields.io/badge/OpenCode-38bdf8" alt="OpenCode" /></a>
  <a href="https://lum1104.github.io/Understand-Anything"><img src="https://img.shields.io/badge/Homepage-d4a574" alt="Homepage" /></a>
  <a href="https://lum1104.github.io/Understand-Anything/demo/"><img src="https://img.shields.io/badge/Live_Demo-00c853" alt="Live Demo" /></a>
</p>

<p align="center">
  <img src="assets/hero.jpg" alt="Understand Anything — Turn any codebase into an interactive knowledge graph" width="800" />
</p>

---

> [!TIP]
> **A huge thank you to the community!** The support for Understand-Anything has been incredible. If this tool saves you a few minutes of digging through complexity, that's all I wanted. 🚀

**You just joined a new team. The codebase is 200,000 lines of code. Where do you even start?**

Understand Anything is a [Claude Code](https://docs.anthropic.com/en/docs/claude-code) plugin that analyzes your project with a multi-agent pipeline, builds a knowledge graph of every file, function, class, and dependency, then gives you an interactive dashboard to explore it all visually. Stop reading code blind. Start seeing the big picture.

---

## ✨ Features

### Explore the structural graph

Navig...