---
title: "0xNyk/awesome-hermes-agent"
source: "https://github.com/0xNyk/awesome-hermes-agent"
date: 2026-03-23
tags: ["ai-agents", "awesome-list", "hermes-agent", "nous-research", "skills"]
platform: github
author: null
summary: "A curated GitHub list of skills, tools, integrations, and resources for Hermes Agent, a self-improving AI agent by Nous Research with built-in learning capabilities."
---
# 0xNyk/awesome-hermes-agent

**URL:** https://github.com/0xNyk/awesome-hermes-agent
**Description:** A curated list of awesome skills, tools, integrations, and resources for Hermes Agent by Nous Research
**Language:** 
**Stars:** 1115 | **Forks:** 73
**License:** Other
**Topics:** ai-agents, awesome, awesome-list, hermes-agent, nous-research, skills
**Last updated:** 2026-04-03

## README (excerpt)

<p align="center">
  <picture>
    <img src="https://raw.githubusercontent.com/NousResearch/hermes-agent/main/assets/banner.png" alt="Awesome Hermes Agent" width="600">
  </picture>
</p>

# Awesome Hermes Agent

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of skills, tools, integrations, and resources for enhancing your [Hermes Agent](https://github.com/NousResearch/hermes-agent) workflow — the self-improving AI agent built by [Nous Research](https://nousresearch.com).

Hermes Agent is the only agent with a built-in learning loop — it creates skills from experience, improves them during use, searches its own past conversations, and builds a deepening model of who you are across sessions. Run it on a $5 VPS, a GPU cluster, or serverless infrastructure. Talk to it from Telegram while it works on a cloud VM.

This list tracks the growing ecosystem around it.

> Ecosystem status (last reviewed: 2026-04-03)
> - Hermes Agent: [v0.6.0 (v2026.3.30)](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.3.30)
> - Core repo: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) (23k+ stars)
> - Latest release notes: [Hermes releases](https://github.com/NousResearch/hermes-agent/releases)

---

## Where Do I Start?

New to Hermes? Don't try to install everything at once. Here's the three-step path from zero to productive:

1. **Get running** — Follow the [Official Docs quickstart](https://hermes-agent.nousresearch.com/docs/). It covers installation, CLI, configuration, and your first conversation.
2. **Add your first skills** — Install [wondelai/skills](https://github.com/wondelai/skills) (380+ stars, actively maintained) — a cross-platform skills library that works with Hermes and other agents. Or try [litprog-skill](https://github.com/tlehman/litprog-skill) (75+ stars) for literate programming across Claude Code, OpenCode, and Hermes.
3. **Get a GUI** — Set up [hermes-workspace](https://github.com/outsourc-e/hermes-workspace) (500+ stars) for a Hermes-native workspace with chat, terminal, and skills manager. Or use [mission-control](https://github.com/builderz-labs/mission-control) (3.7k+ stars) for a broader agent orchestration dashboard with fleet management, task dispatch, and cost tracking.

Once you're comfortable, explore the full list below. Every resource is tagged with a maturity level so you know what you're getting into:

| Tag | What it means |
|-----|---------------|
| **production** | Stable, documented, actively maintained — safe to build on |
| **beta** | Works but still evolving — expect some rough edges |
| **experimental** | Proof of concept or early-stage — learn from it, don't depend on it |

---

## Contents

- [Where Do I Start?](#where-do-i-start)
- [Official Resources](#official-resources)
- [Skills & Plugins](#skills--plugins)
  - [Community Skills](#community-skills)
  - [Plugins](#plugins)
  - [agentskills.io Ecosystem](#agentskillsio-ecosystem)
  - [Skill Regist...