---
title: "mgechev/skills-best-practices"
source: "https://github.com/mgechev/skills-best-practices"
date: 2026-02-24
tags: ["agent skills", "skill development", "LLM validation", "context optimization"]
platform: github
author: "mgechev"
summary: "This repository provides best practices for creating professional-grade agent skills with proper structure, LLM validation, and efficient context window management."
---
# mgechev/skills-best-practices

**URL:** https://github.com/mgechev/skills-best-practices
**Description:** Write professional-grade skills for agents, validate them using LLMs, and maintain a lean context window.
**Language:** Python
**Stars:** 1783 | **Forks:** 126
**Last updated:** 2026-03-15

## README (excerpt)

# Best Practices for Creating Agent Skills

This guide explains how to write professional-grade skills for agents, validate them using LLMs, and maintain a lean context window.

This guide is a concentrated set of best practices for creating agent skills. If you're looking for a comprehensive documentation see [Claude's docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices).

**To evaluate if your skills do well and prevent regressions, check out [skillgrade]((https://github.com/mgechev/skillgrade).**

## Structure of a skill

Every skill must follow this directory structure:

Plaintext

```
skill-name/
├── SKILL.md              # Required: Metadata + core instructions (<500 lines)
├── scripts/              # Executable code (Python/Bash) designed as tiny CLIs
├── references/           # Supplementary context (schemas, cheatsheets) 
└── assets/               # Templates or static files used in output
```

* **SKILL.md:** Acts as the "brain." Use it for navigation and high-level procedures.  
* **References:** Link directly from SKILL.md. Keep them **one level deep** only.  
* **Scripts:** Use for fragile/repetitive operations where variation is a bug. **Do not bundle library code here**;

## Optimize the frontmatter for discoverability

The `name` and `description` in the frontmatter of your `SKILL.md` are the only fields that the agent sees before triggering a skill. If they are not optimized for discoverability and specific enough, your skill is invisible.

* **Adhere to Strict Naming:** The name field must be 1-64 characters, contain only lowercase letters, numbers, and hyphens (no consecutive hyphens), and **must exactly match the parent directory name** (e.g., name: `angular-testing` must live in `angular-testing/SKILL.md`).  
* **Write Trigger-Optimized Descriptions:** (Max 1,024 characters). This is the only metadata the agent sees for routing. Describe the capability in the third person and include "negative triggers."  
  * **Bad:** "React skills." (Too vague).
  * **Good:** "Creates and builds React components using Tailwind CSS. Use when the user wants to update component styles or UI logic. Don't use it for Vue, Svelte, or vanilla CSS projects."

## Progressive disclosure and resource management

Maintain a pristine context window by loading information only when needed. **SKILL.md** is the "brain" for high-level logic; offload details to subdirectories.

* **Keep SKILL.md Lean:** Limit the main file to **\<500 lines**. Use it for navigation and primary procedures.  
* **Use Flat Subdirectories:** Move bulky context to standard folders. Keep files exactly **one level deep** (e.g., `references/schema.md`, not `references/db/v1/schema.md`).  
  * `references/`: API docs, cheatsheets, domain logic.  
  * `scripts/`: Executable code for deterministic tasks.  
  * `assets/`: Output templates, JSON schemas, images.  
* **Just-in-Time (JiT) Loading:** Explicitly instruct the agent when to read a file. It will...