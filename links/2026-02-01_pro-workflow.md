---
title: "rohitg00/pro-workflow"
source: "https://github.com/rohitg00/pro-workflow"
date: 2026-02-01
tags: ["claude-code", "self-correction", "memory", "ai-agents", "workflow"]
platform: github
author: "rohitg00"
summary: "A self-correcting memory system for Claude Code that captures user corrections in a persistent SQLite database and compounds learnings across sessions to reduce repetitive mistakes."
---
# rohitg00/pro-workflow

**URL:** https://github.com/rohitg00/pro-workflow
**Description:** Claude Code learns from your corrections: self-correcting memory that compounds over 50+ sessions. Context engineering, parallel worktrees, agent teams, and 17 battle-tested skills.
**Language:** JavaScript
**Stars:** 1849 | **Forks:** 169
**Topics:** claude, claude-code, cursor, workflow, agent-orchestration, ai-agents, ai-coding, ai-workflow, claude-code-plugin, claude-code-skills, claude-skills, codex, context-engineering, developer-tools, gemini-cli, hooks, productivity, self-correction, worktrees
**Homepage:** https://rohitg00.github.io/pro-workflow/infographic.html
**Last updated:** 2026-04-06

## README (excerpt)

<p align="center">
  <img src="assets/banner.svg" alt="Pro Workflow" width="100%"/>
</p>

<p align="center">
  <a href="https://github.com/rohitg00/pro-workflow/stargazers"><img src="https://img.shields.io/github/stars/rohitg00/pro-workflow?style=for-the-badge&logo=github&color=D97757&labelColor=1e1e2e" alt="Stars"/></a>
  <a href="https://www.npmjs.com/package/pro-workflow"><img src="https://img.shields.io/npm/v/pro-workflow?style=for-the-badge&logo=npm&color=E8926F&labelColor=1e1e2e" alt="npm"/></a>
  <a href="https://github.com/rohitg00/pro-workflow/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-22c55e?style=for-the-badge&labelColor=1e1e2e" alt="License"/></a>
  <a href="https://agenstskills.com"><img src="https://img.shields.io/badge/SkillKit-32%2B%20agents-f59e0b?style=for-the-badge&labelColor=1e1e2e" alt="SkillKit"/></a>
  <a href="https://rohitg00-pro-workflow.mintlify.app/"><img src="https://img.shields.io/badge/Docs-Mintlify-0D9373?style=for-the-badge&logo=mintlify&labelColor=1e1e2e" alt="Docs"/></a>
</p>

<h3 align="center">Your Claude Code gets smarter every session.</h3>

<p align="center">
  Self-correcting memory that compounds over 50+ sessions. You correct Claude once &mdash; it never makes the same mistake again.<br/>
  <b>24 skills</b> &bull; <b>8 agents</b> &bull; <b>21 commands</b> &bull; <b>29 hook scripts across 24 events</b><br/>
  Works with <b>Claude Code</b>, <b>Cursor</b>, and <b>32+ agents</b> via SkillKit.
</p>

---

## The Problem

You correct Claude the same way 50 times. You tell it "don't mock the database" on Monday and again on Friday. You explain your project conventions every new session. Context compacts, learnings vanish, mistakes repeat.

**Every Claude Code user hits this wall.**

## The Solution

Pro Workflow captures every correction in a persistent SQLite database with full-text search. Corrections compound into rules. Rules load automatically on session start. After 50 sessions, Claude barely needs correcting.

<p align="center">
  <img src="assets/self-correction-demo.svg" alt="Self-Correction Loop" width="700"/>
</p>

```
Session 1:  You → "Don't mock the database in tests"
            Claude → Proposes rule → You approve → Saved to SQLite

Session 2:  SessionStart hook loads all learnings
            Claude → Writes integration tests (no mocks)
            You → Zero corrections needed

Session 50: Claude knows your conventions, style, and preferences
            Correction rate: near zero
```

## Install (30 seconds)

```bash
/plugin marketplace add rohitg00/pro-workflow
/plugin install pro-workflow@pro-workflow
```

<details>
<summary>Other install methods</summary>

```bash
# Cursor
/add-plugin pro-workflow

# Any agent via SkillKit
npx skillkit install pro-workflow

# Manual
git clone https://github.com/rohitg00/pro-workflow.git /tmp/pw
cp -r /tmp/pw/templates/split-claude-md/* ./.claude/

# Build with SQLite support
cd ~/.claude/plugins/*/pro-workflow && npm install && np...