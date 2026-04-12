---
title: "vibeforge1111/vibeship-spark-intelligence"
source: "https://github.com/vibeforge1111/vibeship-spark-intelligence"
date: 2026-01-27
tags: ["ai companion", "self-evolving intelligence", "local-first ai", "developer tools"]
platform: github
author: "vibeforge1111"
summary: "Spark Intelligence is a local-first, self-evolving AI companion that captures work context to refine future operational behavior."
---
# vibeforge1111/vibeship-spark-intelligence

**URL:** https://github.com/vibeforge1111/vibeship-spark-intelligence
**Description:** a self-evolving intelligent companion
**Language:** Python
**Stars:** 123 | **Forks:** 36
**License:** MIT License
**Topics:** ai, claude-code, cursor, developer-tools, intelligence, local-first, machine-learning, open-source, self-evolving
**Homepage:** https://spark.vibeship.co
**Last updated:** 2026-03-02

## README (excerpt)

<p align="center">
  <a href="https://spark.vibeship.co"><img src="header.png" alt="Spark Intelligence" width="100%"></a>
</p>
<p align="center">
  <a href="https://github.com/vibeforge1111/vibeship-spark-intelligence/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="License"></a>
  <img src="https://img.shields.io/badge/python-3.10+-blue?style=flat-square" alt="Python">
  <img src="https://img.shields.io/badge/runs-100%25_local-green?style=flat-square" alt="Local">
  <img src="https://img.shields.io/badge/platform-Win%20%7C%20Mac%20%7C%20Linux-lightgrey?style=flat-square" alt="Platform">
</p>

---

Learns constantly. Adapts with your flow.
Runs 100% on your machine as a local AI companion that turns past work into future-ready behavior.
It is designed to be beyond a learning loop.

`You do work` -> `Spark captures memory` -> `Spark distills and transforms it` -> `Spark delivers advisory context` -> `You act with better context` -> `Outcomes re-enter the loop`

## What is Spark?

Spark Intelligence is a self-evolving AI companion designed to grow smarter through use.

It is:
- Not a chatbot.
- Not a fixed rule set.
- A living intelligence runtime that continuously converts experience into adaptive operational behavior, not just stored memory.

The goal is to keep context, patterns, and practical lessons in a form that your agent can actually use at the right moment.

## Beyond a Learning Loop: Intelligence Operating Flow

- Capture: hooks and events from your agent sessions are converted into structured memories.
- Distill: noisy data is filtered into reliable, action-oriented insights.
- Transform: high-value items are shaped for practical reuse (prioritized by reliability, context match, and usefulness).
- Store: distilled wisdom is persisted and versioned in local memory stores.
- Act: advisory and context updates are prepared for the right point in workflow.
- Guard: gating layers check quality, authority, cooldown, and dedupe before any advisory is surfaced.
- Learn: outcomes and follow-through are fed back to refine future recommendations.

## Install

Prerequisites:
- Python 3.10+ (Windows one-liner auto-installs latest Python 3 via `winget` when missing)
- `pip`
- Git
- Windows one-liner path: PowerShell
- Mac/Linux one-liner path: `curl` + `bash`

Windows one-command bootstrap (clone + venv + install + start + health):

```powershell
irm https://raw.githubusercontent.com/vibeforge1111/vibeship-spark-intelligence/main/install.ps1 | iex
```

Optional re-check (from repo root):

```powershell
.\.venv\Scripts\python -m spark.cli up
.\.venv\Scripts\python -m spark.cli health
```

If you already cloned the repo, run the local bootstrap:

```powershell
.\install.ps1
```

If you are running from `cmd.exe` or another shell:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -Command "irm https://raw.githubusercontent.com/vibeforge1111/vibeship-spark-intelligence/main/install.ps1 | iex"
``...