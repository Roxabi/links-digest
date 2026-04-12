---
title: "nicobailon/visual-explainer"
source: "https://github.com/nicobailon/visual-explainer"
date: 2026-02-16
tags: ["agent skill", "HTML generation", "diagram visualization", "code review", "terminal output"]
platform: github
author: "nicobailon"
summary: "An agent skill that converts complex terminal output into styled HTML pages with interactive diagrams and tables."
---
# nicobailon/visual-explainer

**URL:** https://github.com/nicobailon/visual-explainer
**Description:** Agent skill that generates rich HTML pages or slide decks for diagrams, diff reviews, plan audits, data tables, and project recaps
**Language:** HTML
**Stars:** 7457 | **Forks:** 506
**License:** MIT License
**Last updated:** 2026-03-29

## README (excerpt)

<p>
  <img src="banner.png" alt="visual-explainer" width="1100">
</p>

# visual-explainer

**An agent skill that turns complex terminal output into styled HTML pages you actually want to read.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

Ask your agent to explain a system architecture, review a diff, or compare requirements against a plan. Instead of ASCII art and box-drawing tables, it generates a self-contained HTML page and opens it in your browser.

```
> draw a diagram of our authentication flow
> /diff-review
> /plan-review ~/docs/refactor-plan.md
```

https://github.com/user-attachments/assets/55ebc81b-8732-40f6-a4b1-7c3781aa96ec

## Why

Every coding agent defaults to ASCII art when you ask for a diagram. Box-drawing characters, monospace alignment hacks, text arrows. It works for trivial cases, but anything beyond a 3-box flowchart turns into an unreadable mess.

Tables are worse. Ask the agent to compare 15 requirements against a plan and you get a wall of pipes and dashes that wraps and breaks in the terminal. The data is there but it's painful to read.

This skill fixes that. Real typography, dark/light themes, interactive Mermaid diagrams with zoom and pan. No build step, no dependencies beyond a browser.

## Install

**Claude Code (marketplace):**
```shell
/plugin marketplace add nicobailon/visual-explainer
/plugin install visual-explainer@visual-explainer-marketplace
```

Note: Claude Code plugins namespace commands as `/visual-explainer:command-name`.

**Pi:**
```bash
curl -fsSL https://raw.githubusercontent.com/nicobailon/visual-explainer/main/install-pi.sh | bash
```

Or clone and run:
```bash
git clone --depth 1 https://github.com/nicobailon/visual-explainer.git
cd visual-explainer && ./install-pi.sh
```

**OpenAI Codex:**
```bash
git clone --depth 1 https://github.com/nicobailon/visual-explainer.git /tmp/visual-explainer

# Install skill
cp -r /tmp/visual-explainer/plugins/visual-explainer ~/.agents/skills/visual-explainer

# Optional: Install slash commands (deprecated, but works)
mkdir -p ~/.codex/prompts
cp /tmp/visual-explainer/plugins/visual-explainer/commands/*.md ~/.codex/prompts/

rm -rf /tmp/visual-explainer
```

Invoke with `$visual-explainer` or let Codex activate it implicitly. With prompts installed, use `/prompts:diff-review`, `/prompts:plan-review`, etc.

## Commands

| Command | What it does |
|---------|-------------|
| `/generate-web-diagram` | Generate an HTML diagram for any topic |
| `/generate-visual-plan` | Generate a visual implementation plan for a feature or extension |
| `/generate-slides` | Generate a magazine-quality slide deck |
| `/diff-review` | Visual diff review with architecture comparison and code review |
| `/plan-review` | Compare a plan against the codebase with risk assessment |
| `/project-recap` | Mental model snapshot for context-switching back to a project |
| `/fact-check` | Verify accuracy of a document against actual code ...