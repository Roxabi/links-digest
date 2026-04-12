---
title: "CloudAI-X/opencode-workflow"
source: "https://github.com/CloudAI-X/opencode-workflow"
date: 2026-01-10
tags: ["OpenCode workflow", "AI development tools", "software automation", "developer agents", "TypeScript project"]
platform: github
author: "CloudAI-X"
summary: "OpenCode Workflow provides a universal setup with 7 agents, 12 commands, 7 skills, and 5 plugins to automate software development tasks."
---
# CloudAI-X/opencode-workflow

**URL:** https://github.com/CloudAI-X/opencode-workflow
**Description:** 
**Language:** TypeScript
**Stars:** 194 | **Forks:** 18
**License:** MIT License
**Last updated:** 2026-01-10

## README (excerpt)

# OpenCode Workflow

A universal OpenCode workflow setup with specialized agents, skills, commands, and plugins for any software project.

## What You Get

| Component    | Count | What It Does                                            |
| ------------ | ----- | ------------------------------------------------------- |
| **Agents**   | 7     | Orchestrator + 6 specialists (security, tests, docs...) |
| **Commands** | 12    | /review, /commit, /architect, /rapid, /debug...         |
| **Skills**   | 7     | Domain knowledge for APIs, testing, architecture...     |
| **Plugins**  | 5     | Auto-format, security scans, notifications...           |

## Quick Look

```
Your request ──► Orchestrator ──┬──► Code Reviewer    ──┐
                                ├──► Security Auditor ──┼──► Synthesized
                                ├──► Test Architect   ──┤    Report
                                └──► Debugger         ──┘
                                      (all parallel)
```

---

## Installation

OpenCode looks for workflow files in `.opencode/` inside your project directory. This repo uses different folder names (`agents/` instead of `agent/`) so it's easier to browse on GitHub.

### Full Install

```bash
# Clone the workflow
git clone https://github.com/CloudAI-X/opencode-workflow.git

# Create .opencode directory in your project
mkdir -p your-project/.opencode

# Copy all components (note: folder names change!)
cp -r opencode-workflow/agents your-project/.opencode/agent
cp -r opencode-workflow/commands your-project/.opencode/command
cp -r opencode-workflow/skills your-project/.opencode/skill
cp -r opencode-workflow/plugins your-project/.opencode/plugin
```

### Partial Install

Don't need everything? Pick what you want:

```bash
# Just agents and commands (no plugins or skills)
cp -r opencode-workflow/agents your-project/.opencode/agent
cp -r opencode-workflow/commands your-project/.opencode/command
```

### Folder Mapping

| This Repository | Your Project         |
| --------------- | -------------------- |
| `agents/`       | `.opencode/agent/`   |
| `commands/`     | `.opencode/command/` |
| `skills/`       | `.opencode/skill/`   |
| `plugins/`      | `.opencode/plugin/`  |

### Verify It Works

```bash
cd your-project
opencode
# Type / and Tab - should see commands like /review, /commit
# Press Tab repeatedly - should see Orchestrator as a primary agent
# Type @ and Tab - should see subagents like @code-reviewer
```

---

## How to Use

### Primary Agents (Tab to switch)

Press **Tab** to cycle between primary agents:

| Agent            | What It Does                          |
| ---------------- | ------------------------------------- |
| **build**        | Default. Full development work.       |
| **plan**         | Analysis only, no file changes.       |
| **orchestrator** | Coordinates complex multi-step tasks. |

### Subagents (@mention)

Invoke specialists by mentioning them:

```
@security-auditor Check the auth module for vulnerabi...