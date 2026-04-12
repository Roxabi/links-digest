---
title: "wednesday-solutions/ai-agent-skills"
source: "https://github.com/wednesday-solutions/ai-agent-skills"
date: 2026-02-02
tags: ["AI agent skills", "coding assistant tools", "code quality guidelines", "developer productivity"]
platform: github
author: "wednesday-solutions"
summary: "Pre-configured AI agent skills providing coding assistants with code quality and design standards for Vibe Coded projects."
---
# wednesday-solutions/ai-agent-skills

**URL:** https://github.com/wednesday-solutions/ai-agent-skills
**Description:** Pre-configured agent skills for Vibe Coded projects. These skills provide AI coding assistants (Claude Code, Cursor, etc.) with specific guidelines for code quality and design standards.
**Language:** JavaScript
**Stars:** 145 | **Forks:** 15
**License:** MIT License
**Topics:** claude-code, copilot, cursor, vibe-coding, agent-skills, ai-agent-skills, ai-skills, frontend-skills, product-engineering-skills, vibe-coding-skills
**Homepage:** https://www.npmjs.com/package/@wednesday-solutions-eng/ai-agent-skills
**Last updated:** 2026-03-27

## README (excerpt)

# Wednesday Agent Skills

AI skills for Wednesday Solutions projects — git discipline, PR automation, terminal dashboard, greenfield planning, and brownfield codebase intelligence with real-time chat, drift detection, and test generation.

---

## 1. Installation

### Requirements
- Node.js ≥ 18
- npm ≥ 8

**Option 1 — npx (no setup)**
```bash
npx @wednesday-solutions-eng/ai-agent-skills install
```

**Option 2 — global**
```bash
npm install -g @wednesday-solutions-eng/ai-agent-skills
wednesday-skills install
```

**Option 3 — shell (no npm)**
```bash
bash install.sh
```

Run in your project root. The installer:
1. Copies skills into `.wednesday/skills/`
2. Writes agent config files (`CLAUDE.md`, `GEMINI.md`, `.cursorrules`, `.github/copilot-instructions.md`)
3. Installs git hooks (`post-commit`, `post-merge`) for automatic graph updates
4. Prompts for optional coverage and Sonar integration
5. Symlinks skills into `~/.claude/skills/` for Claude Code discovery

---

## 2. Configuration & AI Tools

**No API key needed to use skills inside Claude Code, Cursor, or Gemini CLI.** 
When inside an AI IDE, the IDE acts as the intelligence engine — skills are standard instructions, not local scripts.

### Supported AI tools
| Tool | Configured via |
|------|---------------|
| Claude Code | `CLAUDE.md` |
| Gemini CLI | `GEMINI.md` |
| Antigravity | `~/.gemini/antigravity/skills/` (run `wednesday-skills sync`) |
| Cursor | `.cursorrules` |
| GitHub Copilot | `.github/copilot-instructions.md` |

### Environment Variables
API keys are only required for standalone CLI workflows (`plan`, `summarize`, `gen-tests`). 
Run the interactive configuration wizard:

```bash
wednesday-skills config
```

Or manually add to `.env`:
- `OPENROUTER_API_KEY` or `ANTHROPIC_API_KEY`: Used by offline LLM-backed tools.
- `GITHUB_TOKEN`: Used by `wednesday-skills dashboard` to fetch PR data.

---

## 3. Every Skill Explained

### Core Workflow Skills
| Skill | What it does |
|---------|-------------|
| `git-os` | Enforces conventional commits — no bad or ambiguous commit messages allowed. |
| `pr-review` | Gemini fix queue — categorizes PR comments by impact, applies fixes upon dev approval. |
| `deploy-checklist` | Walks through pre-deploy checks and post-deploy monitoring checklists. |
| `wednesday-dev` | Enforces import ordering, file complexity limits (max 8), and naming conventions. |
| `wednesday-design` | Asserts the use of 492+ approved UI components, design tokens, and animation patterns. |
| `sprint` | Translates ticket IDs into git branches, PR titles, and description templates automatically. |
| `greenfield` | Parallel AI personas (Architect, PM, Security) produce a comprehensive `PLAN.md` in minutes. |

### Brownfield Intelligence Skills
| Skill | What it does |
|---------|-------------|
| `brownfield-chat` | Plain-English codebase Q&A using structural graphs (zero hallucinated data). |
| `brownfield-query` | Deterministic structural queries returning dependencies, end...