---
title: "davidhariri/life-system"
source: "https://github.com/davidhariri/life-system"
date: 2026-02-15
tags: ["life planning system", "personal productivity", "plain-text journaling", "AI-powered organization", "self-improvement toolkit"]
platform: github
author: "davidhariri"
summary: "A plain-text life operating system powered by Claude Code for life planning, daily journaling, and decision-making inspired by Carmack and Franklin."
---
# davidhariri/life-system

**URL:** https://github.com/davidhariri/life-system
**Description:** A plain-text life operating system powered by Claude Code. Inspired by Carmack's .plan files and Franklin's systematic self-improvement.
**Language:** Shell
**Stars:** 714 | **Forks:** 48
**Last updated:** 2026-02-18

## README (excerpt)

# Life System Starter Kit

A personal life operating system powered by Claude Code. Inspired by Carmack's .plan files and Franklin's systematic self-improvement.

## What This Is

A plain-text system for life planning, daily journaling, decision-making, and task capture — with Claude Code as your thinking partner. No apps, no subscriptions. Just markdown files, a terminal, and an AI that pushes back.

## What You Get

- **Life plan** — 10-year vision, life chapters, what you're optimizing for
- **Annual goals** — Yearly bets, anti-goals, who you're becoming
- **Daily journal** — Franklin's morning question + Carmack-style timestamped log + evening reflection
- **Decision records** — Structured docs for important decisions so you can trace your reasoning later
- **Inbox** — Quick capture for tasks, ideas, and things to process later
- **Values & habits** — Your principles and daily routines, written down so Claude can hold you to them
- **People** — Notes on people you're meeting, working with, or researching
- **Research** — Deep dives on any topic — companies, technologies, markets, ideas

## Setup

### 1. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 2. Copy the CLAUDE.md

Copy `CLAUDE.md` from this directory to `~/.claude/CLAUDE.md`. This is the global instructions file that tells Claude how to work with you.

```bash
cp CLAUDE.md ~/.claude/CLAUDE.md
```

Then **edit it** — replace the placeholders with your own name, projects, paths, and preferences. The whole point is that it's yours.

### 3. Install the morning skill

The `/morning` skill is what powers the daily routine. Copy it into your Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills
cp -r skills/morning ~/.claude/skills/morning
```

Then **edit the skill files** — replace `YOURNAME` with your name in both `SKILL.md` and `reference.md`.

### 4. Install the journal script

The `jrn` command creates today's journal from the template, backfills any missing days (carrying forward uncompleted todos and active decisions), pulls in calendar events, and opens the file in your editor.

```bash
mkdir -p ~/.scripts
cp scripts/journal.sh ~/.scripts/journal.sh
chmod +x ~/.scripts/journal.sh
```

Edit `~/.scripts/journal.sh` — update `JOURNAL_DIR`, `TEMPLATE`, and `EDITOR_CMD` at the top to match your paths and preferred editor.

Then add the alias to your shell config (`~/.zshrc` or `~/.bashrc`):

```bash
echo "alias jrn='~/.scripts/journal.sh'" >> ~/.zshrc
source ~/.zshrc
```

Now just type `jrn` to open today's journal.

### 5. Set up your life directory

Copy the starter files to wherever you want your life system to live. The default assumes `~/Documents/[yourname]/`:

```bash
# Copy starter files
cp -r plan.md journal/ reference/ decisions/ people/ research/ templates/ inbox.md ~/Documents/yourname/
```

Update the paths in your `CLAUDE.md` to match wherever you put these.

### 6. Initialize git (optional but recommended)

```bash
cd ~/Documents/...