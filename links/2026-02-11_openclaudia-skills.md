---
title: "OpenClaudia/openclaudia-skills"
source: "https://github.com/OpenClaudia/openclaudia-skills"
date: 2026-02-11
tags: ["marketing toolkit", "open-source skills", "Claude Code", "AI marketing", "SEO tools"]
platform: github
author: "OpenClaudia"
summary: "OpenClaudia provides 62+ open-source marketing skills that turn Claude Code into a full marketing department for SEO, content, email, and growth tasks."
---
# OpenClaudia/openclaudia-skills

**URL:** https://github.com/OpenClaudia/openclaudia-skills
**Description:** 34 open-source marketing skills for Claude Code. SEO, content, email, ads, analytics, and growth.
**Language:** JavaScript
**Stars:** 380 | **Forks:** 5
**License:** MIT License
**Homepage:** https://openclaudia.com
**Last updated:** 2026-04-10

## README (excerpt)

<p align="center">
  <img src="https://openclaudia.com/avatar.png" width="120" alt="OpenClaudia" />
</p>

<h1 align="center">OpenClaudia</h1>

<p align="center">
  <strong>The open-source marketing toolkit for AI coding agents.</strong><br/>
  62+ modular skills that turn Claude Code into a full marketing department.
</p>

<p align="center">
  <a href="https://www.npmjs.com/package/openclaudia"><img src="https://img.shields.io/npm/v/openclaudia?color=blue&label=npm" alt="npm version" /></a>
  <a href="https://github.com/OpenClaudia/openclaudia-skills/stargazers"><img src="https://img.shields.io/github/stars/OpenClaudia/openclaudia-skills?style=social" alt="GitHub Stars" /></a>
  <a href="https://github.com/OpenClaudia/openclaudia-skills/blob/main/LICENSE"><img src="https://img.shields.io/github/license/OpenClaudia/openclaudia-skills" alt="License: MIT" /></a>
  <a href="https://openclaudia.com"><img src="https://img.shields.io/badge/website-openclaudia.com-purple" alt="Website" /></a>
</p>

<p align="center">
  <a href="https://openclaudia.com">Website</a> · <a href="#quick-start">Quick Start</a> · <a href="USAGE.md">Usage Guide</a> · <a href="USAGE-ZH.md">使用指南</a> · <a href="#skills">Skills</a> · <a href="https://github.com/OpenClaudia/openclaudia-skills/issues">Issues</a> · <a href="CONTRIBUTING.md">Contributing</a>
</p>

---

## Why OpenClaudia?

Most AI marketing tools charge **$50–300/month** for a chat box that gives you suggestions. OpenClaudia is different:

| | SaaS Marketing Tools | OpenClaudia |
|---|---|---|
| **Price** | $50–300/month | Free & open source |
| **Execution** | Suggests copy, you do the rest | Actually writes, publishes, sends |
| **Data privacy** | Your data on their servers | Runs locally on your machine |
| **Customization** | Limited to their UI | Fork, modify, extend any skill |
| **Integration** | Walled garden | Works with 20+ APIs you already use |
| **Setup** | Sign up, onboard, learn their UI | One command: `npx openclaudia install --all` |

## Quick Start

**Prerequisites:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and authenticated.

```bash
# Install all 62+ marketing skills
npx openclaudia install --all

# Or install specific skills
npx openclaudia install seo-audit write-blog email-sequence
```

Then open Claude Code and start marketing:

```
$ claude

> /audit-seo https://mysite.com
✓ Analyzing 47 pages... SEO score: 72/100 — 12 issues found

> /write-blog "10 Tips for SaaS Growth"
✓ 2,400-word article generated with meta tags

> /email-sequence --type product-launch
✓ 6-email drip sequence created and sent via Resend

> /competitor-analysis competitor.com
✓ Full SEO, content, and positioning breakdown

> /discord-bot "New feature just dropped!"
✓ Rich embed posted to #announcements
```

### Alternative installation

```bash
# Via the skills CLI
npx skills add OpenClaudia/openclaudia-skills

# Install a single skill
npx skills add OpenClaudia/openclaudia-skills --skill seo-...