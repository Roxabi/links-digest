---
title: "wbelk/claude-qmd-sessions"
source: "https://github.com/wbelk/claude-qmd-sessions"
date: 2026-03-03
tags: ["claude", "session-memory", "qmd", "markdown", "hooks"]
platform: github
author: "wbelk"
summary: "Claude Code skill that converts JSONL session transcripts into searchable markdown and indexes them in qmd for persistent memory across sessions."
---
# wbelk/claude-qmd-sessions

**URL:** https://github.com/wbelk/claude-qmd-sessions
**Description:** Persistent chat session memory for Claude Code with qmd. Index updates itself via Claude hooks.
**Language:** JavaScript
**Stars:** 35 | **Forks:** 3
**Last updated:** 2026-03-08

## README (excerpt)

# qmd-sessions

Claude Code skill that converts JSONL session transcripts into searchable markdown and indexes them in [qmd](https://github.com/tobi/qmd).

## Installation

1. Copy the skill directory to your Claude Code skills folder:

```bash
cp -r . ~/.claude/skills/qmd-sessions/
```

2. Start a new Claude Code session and run:

```
/qmd-sessions
```

The skill walks through all setup interactively — output directory, conversion, qmd collection, embeddings, MCP server, hooks, and CLAUDE.md guidance. Each step prompts for confirmation.

## What it does

1. Reads session JSONL files from `~/.claude/projects/`
2. Extracts user messages + assistant text responses (skips tool_use, tool_result, thinking blocks)
3. Outputs organized markdown: `{project}/{date}-{slug}-{id}.md`
4. Indexes in qmd for semantic + keyword search via MCP

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Skill definition — step-by-step setup with user prompts |
| `convert-sessions.js` | Conversion script (bulk + `--session` modes) |
| `hook.js` | PreCompact/SessionEnd/SessionStart hook — converts session, restores context, updates qmd index |
| `lib.js` | Shared utilities: config, pgrep guard, qmd update+embed, session file lookup, turn extraction |
| `refresh.js` | Outputs CLAUDE.md files + recent turns from multiple sessions to stdout |
| `config.json` | Persisted output directory + `loadContextOnStartup` flag |

## Usage

```
/qmd-sessions           # Full setup wizard
/qmd-sessions refresh   # Load CLAUDE.md files + last ~50 exchanges into context
```

`refresh` outputs both CLAUDE.md files and the last ~50 exchanges (100 turns, capped at 14,000 characters) collected from recent sessions into context. Useful for manually restoring context in a fresh session.

The setup wizard walks through interactively: output directory, conversion, verification, then checks for Bun, qmd, collection, embeddings, MCP server, hooks, and CLAUDE.md guidance.

## Hooks

Four Claude Code hooks keep the index current and restore context (configured in `~/.claude/settings.json`):

- **PreCompact** — converts session before context compaction, runs `qmd update && qmd embed`
- **SessionEnd** — converts session on exit, runs `qmd update && qmd embed`
- **SessionStart (compact/resume/clear)** — converts the session, then outputs both CLAUDE.md files and the last ~50 exchanges (from multiple recent sessions, sorted by cwd match, capped at 14,000 characters) to stdout so Claude receives instructions and conversation context after compaction.
- **SessionStart (startup)** — outputs CLAUDE.md files to stdout. If `loadContextOnStartup` is enabled in config.json, also outputs the last ~50 exchanges (same as compact/resume/clear, but without session conversion).

All hooks use `pgrep -f "qmd.*embed"` to skip embed if another session's embed is already running.

## Prerequisites

- [Bun](https://bun.sh/) (qmd runtime)
- Node >= 22 (Metal GPU acceleration)
- [qmd](https://github.com/tobi/qmd) >...