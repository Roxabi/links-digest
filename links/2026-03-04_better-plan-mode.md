---
title: "jnemargut/better-plan-mode"
source: "https://github.com/jnemargut/better-plan-mode"
date: 2026-03-04
tags: ["AI coding skill", "project planning", "visual decision documents", "interactive HTML"]
platform: github
author: "jnemargut"
summary: "Better Plan Mode is an AI coding skill that transforms project planning into visual, interactive HTML decision documents with comparison tables and recommendations."
---
# jnemargut/better-plan-mode

**URL:** https://github.com/jnemargut/better-plan-mode
**Description:** An AI coding skill that transforms project planning into visual, interactive HTML decision documents
**Language:** 
**Stars:** 50 | **Forks:** 6
**License:** MIT License
**Last updated:** 2026-04-09

## README (excerpt)

# Better Plan Mode

An AI coding skill that transforms project planning into a visual, interactive decision-making experience. Instead of quick yes/no prompts, you get rich HTML documents with side-by-side options, visual previews, comparison tables, and a persistent decision history.

![Better Plan Mode in action](demo.gif)

## What It Does

When you're starting a new project or feature, Better Plan Mode walks you through every meaningful decision, one at a time, with:

- **4 options per decision** with a clear recommendation and plain English explanations
- **Visual previews** -- rendered UI mockups for design decisions, flow diagrams for interaction decisions, sitemaps for navigation decisions, architecture diagrams for technical decisions
- **Comparison tables** showing how options stack up across relevant dimensions
- **A decision history** saved as HTML files you can revisit anytime
- **A landing page** showing all decisions at a glance with status tracking

### Decision Categories

| Category | What It Covers | Visual Preview |
|----------|---------------|----------------|
| **Technical** | Tech stack, database, auth, hosting, API design | Architecture diagrams, code samples |
| **Visual/UX** | Style direction, color, typography, component design | Rendered HTML/CSS mockups |
| **Interaction** | User flows, onboarding, how key actions work | Step-by-step flow diagrams |
| **Information Architecture** | Navigation, content hierarchy, page structure | Mini sitemaps, nav visualizations |

## Install

The skill is a single `SKILL.md` file. Drop it into the right directory for your AI coding tool.

**Claude Code:**
```bash
git clone https://github.com/jnemargut/better-plan-mode ~/.claude/skills/better-plan-mode
```

**Codex:**
```bash
git clone https://github.com/jnemargut/better-plan-mode ~/.codex/skills/better-plan-mode
```

**Gemini CLI:**
```bash
git clone https://github.com/jnemargut/better-plan-mode ~/.gemini/skills/better-plan-mode
```

**Cursor:**

Cursor uses `.mdc` rule files instead of a skills directory. Copy the skill content into a rule:
```bash
mkdir -p .cursor/rules
cp SKILL.md .cursor/rules/better-plan-mode.mdc
```
Then open `.cursor/rules/better-plan-mode.mdc` and replace the frontmatter with:
```yaml
---
description: "Enhanced planning mode that presents decision points as rich HTML documents with visual previews, comparison tables, and recommendations."
alwaysApply: false
---
```

The skill should work with any AI coding tool that supports custom instructions or skill files. If yours uses a different directory, just put `SKILL.md` wherever your tool looks for skills or prompts.

## Usage

Invoke the skill with:

```
/better-plan-mode I want to build a neighborhood book-sharing app where people can list books, browse nearby, and request to borrow
```

Or any project description:

```
/better-plan-mode A dashboard for tracking my fitness goals with charts and social features
```

### During Planning

Each decision opens as an ...