---
title: "qodo-ai/qodo-skills"
source: "https://github.com/qodo-ai/qodo-skills"
date: 2026-03-24
tags: ["code review tools", "AI coding agents", "shift-left development", "developer tools"]
platform: github
author: null
summary: "Qodo Skills provides shift-left code review capabilities for AI coding agents compatible with Claude Code, Cursor, Windsurf, Cline and other platforms."
---
# qodo-ai/qodo-skills

**URL:** https://github.com/qodo-ai/qodo-skills
**Description:** 
**Language:** 
**Stars:** 22 | **Forks:** 4
**License:** MIT License
**Last updated:** 2026-04-10

## README (excerpt)

# Qodo Skills

Shift-left code review skills for AI coding agents. Bring Qodo's quality standards and code review capabilities into your local development workflow.

**Compatible with:** Claude Code, Cursor, Windsurf, Cline, and any agent supporting the [Agent Skills](https://agentskills.io) standard.

## Available Skills

### 🔧 qodo-get-rules
Fetches the most relevant coding rules from Qodo for the current coding task. Generates a semantic search query from your assignment and retrieves only the rules that matter, ranked by relevance.

**Features:**
- 🔍 Semantic search — only the most relevant rules for your specific task
- ⚖️ Severity-based enforcement (ERROR, WARNING, RECOMMENDATION)
- 🎯 Dual-query strategy (topic + cross-cutting) for comprehensive coverage
- 🚀 Auto-runs before code generation, editing, and refactoring

[View skill details](./skills/qodo-get-rules/SKILL.md)

### 🔍 qodo-pr-resolver
Fetch Qodo review issues for your current branch's PR/MR, fix them interactively or in batch, and reply to each inline comment with the decision.

**Features:**
- Multi-provider support (GitHub, GitLab, Bitbucket, Azure DevOps, Gerrit)
- Interactive issue review and auto-fix modes
- Per-issue inline comment replies and git commits
- Gerrit-native workflow: amend + push instead of per-fix commits
- Severity mapping from Qodo's action levels
- Automatic PR/MR/change summary comments

[View skill details](./skills/qodo-pr-resolver/SKILL.md)

## Installation

Install skills using the standard Agent Skills CLI:

```bash
# Install all Qodo skills
npx skills add qodo-ai/qodo-skills

# Or install individual skills
npx skills add qodo-ai/qodo-skills/skills/qodo-get-rules
npx skills add qodo-ai/qodo-skills/skills/qodo-pr-resolver
```

**Claude Code Marketplace:**
```
/plugin install qodo-skills@claude-plugins-official
```

**Works with:**
- **Claude Code** - Skills available as `/qodo-get-rules`, `/qodo-pr-resolver`
- **Cursor** - Skills available in command palette
- **Windsurf** - Skills available in flow menu
- **Cline** - Skills available via skill invocation
- **Any agent** supporting [agentskills.io](https://agentskills.io)

### Agent-Specific Directories

Skills are automatically installed to the correct location for your agent:

| Agent | Installation Directory |
|-------|----------------------|
| Claude Code | `~/.claude/skills/` or `.claude/skills/` |
| Cursor | `~/.cursor/skills/` or `.cursor/skills/` |
| Windsurf | `~/.windsurf/skills/` or `.windsurf/skills/` |
| Cline | `~/.cline/skills/` or `.cline/skills/` |

## Prerequisites

### System Requirements

- **Git** - For repository detection
  - Usually pre-installed on macOS and most Linux distributions
  - Windows: Download from https://git-scm.com/download/win
- **curl** - For HTTPS API requests (works with system SSL certificates)
  - Pre-installed on macOS, most Linux distributions, and Windows 10+
  - If needed, install via package manager or download from https://curl.se
  ```bash
  # Check i...