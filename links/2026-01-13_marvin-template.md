---
title: "SterlingChin/marvin-template"
source: "https://github.com/SterlingChin/marvin-template"
date: 2026-01-13
tags: ["AI assistant", "productivity tool", "goal tracking", "session continuity", "tool integrations"]
platform: github
author: "SterlingChin"
summary: "MARVIN is a personal AI assistant that manages appointments, tracks goals, and integrates with productivity tools like Google Workspace and Slack."
---
# SterlingChin/marvin-template

**URL:** https://github.com/SterlingChin/marvin-template
**Description:** MARVIN is your personal AI assistant that can help you connect to the apps you need and handle your day.
**Language:** Shell
**Stars:** 965 | **Forks:** 163
**License:** MIT License
**Last updated:** 2026-04-10

## README (excerpt)

# MARVIN - Your AI Chief of Staff

**MARVIN** = Manages Appointments, Reads Various Important Notifications

An AI assistant that remembers your conversations, tracks your goals, and helps you stay organized. Like having a personal chief of staff who never forgets anything.

## Why MARVIN?

MARVIN extends Claude Code with capabilities designed for getting things done:

- **Session continuity** - Pick up where you left off, even days later. Every conversation builds on the last.
- **Goal tracking** - Set work and personal goals, MARVIN monitors progress and nudges you forward.
- **Tool integrations** - Connect to Google Workspace, Microsoft 365, Atlassian, Slack, Linear, Notion, Telegram, and more.
- **Extensibility** - Add commands, agents, and skills tailored to your workflow. Create new capabilities with simple markdown files.
- **Thought partner** - MARVIN pushes back on weak ideas, asks probing questions, and helps you think through decisions. Not just a yes-man.

## Quick Start with Claude Code

1. Clone this repository:
   ```bash
   git clone https://github.com/SterlingChin/marvin-template.git
   cd marvin-template
   ```

2. Open in Claude Code:
   ```bash
   claude
   ```

3. Ask MARVIN to help you set up:
   > "Help me set up MARVIN"

That's it. MARVIN walks you through the rest: your profile, goals, workspace location, and optional integrations.

## Getting Started with GitHub Copilot CLI

Want to use Copilot CLI to set up MARVIN quickly? Here's how:

### Prerequisites

- [GitHub Copilot CLI](https://cli.github.com/) installed and authenticated

### Quick Setup

Use these Copilot commands to get started:

```bash
# Navigate to your projects directory
gh copilot suggest "clone marvin template repository"

# Run the setup script
gh copilot suggest "run setup script for marvin"

# Start MARVIN
gh copilot suggest "start marvin AI assistant"
```

The `.marvin/setup.sh` script handles the complete installation: prerequisites, workspace creation, profile setup, and shell aliases. Just follow the prompts to configure your AI Chief of Staff.

For additional integrations (Google Workspace, Slack, etc.), use:

```bash
gh copilot suggest "configure marvin integrations"
```

## What You Get

### Daily Workflow

Start your day with `/start` for a briefing: priorities, deadlines, progress toward goals. Work naturally throughout the day, MARVIN remembers everything. End with `/end` to save context for next time.

Between sessions, `/update` saves progress without ending. `/sync` pulls new features from this template into your workspace.

### Commands

| Command | What It Does |
|---------|--------------|
| `/start` | Start your day with a briefing |
| `/end` | End session and save everything |
| `/update` | Quick checkpoint (save progress) |
| `/report` | Generate a weekly summary |
| `/commit` | Review and commit git changes |
| `/status` | Check integration & workspace health |
| `/sync` | Get updates from the template |
| `/help` | Show all command...