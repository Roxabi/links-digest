---
title: "Tibsfox/gsd-skill-creator"
source: "https://github.com/Tibsfox/gsd-skill-creator/blob/main/INSTALL.md"
date: 2026-01-30
tags: ["agent-based framework", "software development", "AI coding tools", "workflow automation", "adaptive learning"]
platform: github
author: "Tibsfox"
summary: "GSD Skill Creator is an adaptive learning framework for Claude Code that builds reusable knowledge from developer patterns through observation and detection."
---
# Tibsfox/gsd-skill-creator

**URL:** https://github.com/Tibsfox/gsd-skill-creator
**Description:** Introduces a comprehensive agent-based framework for guided software development (GSD)
**Language:** HTML
**Stars:** 46 | **Forks:** 6
**License:** Other
**Topics:** adaptive-learning, agent-orchestration, ai-agents, claude-code, developer-tools, mcp, multi-agent, open-source, rust, tauri, typescript, workflow-automation, ai-coding, ai-workflow, claude-code-skills, claude-skills, context-engineering, hooks, self-correction, worktrees
**Last updated:** 2026-04-11

## README (excerpt)

# GSD Skill Creator

An adaptive learning and coprocessor architecture for [Claude Code](https://docs.anthropic.com/en/docs/build-with-claude/claude-code), built as an extension to [GSD (Get Shit Done)](https://github.com/gsd-build).

```

npx get-shit-done-cc@latest

npx gsd-skill-creator@latest

```

## Table of Contents

- [The Problem: Why AI-Assisted Development Breaks Down](#the-problem-why-ai-assisted-development-breaks-down)
- [How GSD and Skill Creator Solve It Together](#how-gsd-and-skill-creator-solve-it-together)
- [The Coprocessor Architecture](#the-coprocessor-architecture)
- [GSD-OS Desktop Application](#gsd-os-desktop-application)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Security](#security)
- [License](#license)
- [Contributing](#contributing)

---

## The Problem: Why AI-Assisted Development Breaks Down

AI coding assistants are powerful in short bursts, but they degrade on sustained, complex work. The core issues:

- **Context rot** -- As a session fills its context window, the AI loses track of earlier decisions, repeats mistakes, and produces lower-quality output. By the time you're deep into implementation, the assistant has forgotten why you made the architectural choices it's now contradicting.
- **Amnesia between sessions** -- Every new session starts from zero. The AI doesn't know what worked last time, what patterns you prefer, or what it should avoid. You re-explain the same things across every conversation.
- **No workflow memory** -- Recurring sequences (test, fix, commit, verify) are executed ad-hoc every time. The AI never learns that "after a test failure, you always check the fixture data first" or that "deploy means these seven steps in this order."
- **Scaling complexity** -- A single AI session can handle a function or a file. It cannot reliably coordinate a multi-phase feature across dozens of files without losing coherence, skipping steps, or drifting from the plan.

These aren't limitations of the models themselves. They're limitations of how work is structured around them.

---

## How GSD and Skill Creator Solve It Together

**GSD** is the workflow engine. It solves context rot and scaling complexity by structuring work into phases with atomic execution boundaries. Each phase gets a fresh context window, a detailed plan, and persistent state tracking. The AI executes one well-scoped unit of work at a time, commits atomically, and hands off cleanly to the next phase. Context never rots because it never accumulates beyond what's needed for the current task.

**Skill Creator** is the learning layer that extends GSD. It doesn't replace any GSD functionality -- it observes how you work within the GSD lifecycle and builds reusable knowledge from your patterns:

- **Observe** -- Watches tool sequences, file patterns, corrections, and phase outcomes across sessions
- **Detect** -- Identifies recurring workflows using n-gram extraction and DBSCAN clustering when patterns repeat 3+ times
-...