---
title: "sverrirsig/claude-control"
source: "https://github.com/sverrirsig/claude-control"
date: 2026-03-21
tags: ["macOS", "Claude Code", "dashboard", "monitoring", "git"]
platform: github
author: null
summary: "A native macOS desktop application for monitoring and managing multiple Claude Code sessions in real-time, featuring auto-discovery, git integration, and quick action controls."
---
# sverrirsig/claude-control

**URL:** https://github.com/sverrirsig/claude-control
**Description:** macOS desktop dashboard for monitoring and managing multiple Claude Code sessions
**Language:** TypeScript
**Stars:** 93 | **Forks:** 12
**License:** MIT License
**Last updated:** 2026-04-10

## README (excerpt)

<p align="center">
  <img src="public/icon.png" alt="Claude Control" width="128" height="128">
</p>

<h1 align="center">Claude Control</h1>

<p align="center">
  A native macOS desktop app for monitoring and managing multiple <a href="https://docs.anthropic.com/en/docs/claude-code">Claude Code</a> sessions in real time.
</p>

When you're running several Claude Code instances across different repos and worktrees, it's hard to keep track of what each one is doing. Claude Control auto-discovers all running sessions and gives you a single dashboard with live status, git changes, conversation previews, and quick actions — without leaving the app.

![Dashboard](docs/screenshot.png)

## Features

- **Auto-discovery** — Detects all running `claude` CLI processes via the process table, uses hook events for authoritative PID-to-JSONL mapping with mtime-based fallback
- **Live status** — Classifies each session as Working, Idle, Waiting (needs input), Errored, or Finished using real-time hook events from Claude Code, with CPU/JSONL heuristic fallback
- **Git integration** — Shows branch name, changed files, additions/deletions, and detects open pull requests via `gh`
- **PR status badges** — Live CI check rollup (passing/failing/pending), review decision, unresolved threads, merge conflicts, and merged/closed state
- **Task context** — Extracts Linear issue titles and descriptions from MCP tool results to show what each session is working on
- **Conversation preview** — Shows the last assistant message, active tool, and user prompt for each session
- **Approve/reject from dashboard** — Approve or reject tool-use permission prompts directly from the dashboard without switching to the terminal
- **Keyboard shortcuts** — Number keys (1-9) to select sessions, Tab/Shift+Tab to cycle, A/X to approve/reject, Enter to focus terminal, E/G/F/P for editor/git/finder/PR
- **Desktop notifications** — Native macOS notifications when sessions finish working or need attention (configurable)
- **Notification sounds** — Subtle two-tone chime on status transitions (configurable)
- **Quick actions** — One-click buttons to focus the terminal tab, open your editor, git GUI, Finder, or PR link for any session
- **Multiple terminal support** — Full tab-level control for iTerm2, Terminal.app, kitty, and WezTerm; basic support for Ghostty, Warp, and Alacritty (see [Terminal support](#terminal-support))
- **tmux integration** — Run sessions inside tmux with per-project session grouping or manual session selection; approve/reject without terminal focus via `send-keys`
- **Configurable tools** — Choose your preferred terminal, code editor (VS Code, Cursor, Zed, etc.), git GUI (Fork, Sublime Merge, etc.), and browser (Chrome, Arc, Safari, etc.)
- **New session creation** — Create new Claude Code sessions with git worktree support, repo browsing, and custom initial prompts
- **PR workflow** — Send `/create-pr` to idle sessions and see PR links once created
- **Worktree cleanup** — Remove...