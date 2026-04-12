---
title: "superdesigndev/superdesign-skill"
source: "https://github.com/superdesigndev/superdesign-skill"
date: 2026-01-21
tags: ["design automation tool", "CLI design utility", "AI design assistant", "canvas design system", "coding agent skill"]
platform: github
author: "superdesigndev"
summary: "SuperDesign is a CLI tool that integrates with coding agents to help developers find design inspirations and generate design s on an infinite canvas."
---
# superdesigndev/superdesign-skill

**URL:** https://github.com/superdesigndev/superdesign-skill
**Description:** 
**Language:** 
**Stars:** 285 | **Forks:** 11
**Last updated:** 2026-03-06

## README (excerpt)

SuperDesign helps you (1) find design inspirations/styles and (2) generate/iterate design drafts on an infinite canvas.

---

# Core scenarios (what this skill handles)

1. **Help me design X** (feature/page/flow)
2. **Set design system**
3. **Help me improve design of X**

# Quickstart

Install CLI
```
npm install -g @superdesign/cli@latest
```

Install skills for any coding agent
```
npx skills add superdesigndev/superdesign-skill
```

Prompt in any agent
```
/superdesign help me design X
```

--

## Tooling overview

### A) Inspiration & Style Tools (generic, always available)

Use these to discover style direction, references, and brand context:

- **Search prompt library** (style/components/pages)

  ```bash
  superdesign search-prompts --keyword "<keyword>" --json
  superdesign search-prompts --tags "style" --json
  superdesign search-prompts --tags "style" --keyword "<style keyword>" --json
  ```

- **Get full prompt details**

  ```bash
  superdesign get-prompts --slugs "<slug1,slug2,...>" --json
  ```

- **Extract brand guide from a URL**
  ```bash
  superdesign extract-brand-guide --url https://example.com --json
  ```

### B) Canvas Design Tools

Use design agent to generate high quality design drafts:
- Create project (supports prompt / prompt file / HTML)
- Create design draft
- Iterate design draft (replace / branch)
- Plan flow pages → execute flow pages
- Fetch specific design draft

---

## Overall SOP for designing features on top of existing app:
1. Investigate existing UI, workflow
2. Setup design system file if not exist yet
3. Requirements gathering: use askQuestion tool to clarify requirements with users (Optionally use Inspiration tool to find inspiration when needed)
4. Ask user whether ready to design in superdesign OR implement UI directly
5. If yes to superdesign
  5.1 Create/update a pixel perfect html replica of current UI of page that we will design on top of in `.superdesign/replica_html_template/<name>.html` (html should only contain & reflect how UI look now, the actual design should be handled by superdesign agent)
  5.2 Create project with this replica html + design system guide
  5.3 Start desigining by iterating & branching design draft based on designDraft ID returned from project


## Always-on rules
- Design system should live at: `.superdesign/design-system.md`
- If `.superdesign/design-system.md` is missing, run **Design System Setup** first.
- Use `askQuestion` to ask high-signal questions (constraints, taste, tradeoffs).
- Always use `--json` for machine parsing.

---

## replica_html_template rules (Canvas only)

The purpose of replica html template is creating a lightweight version of existing UI so design agent can iterate on top of it (Since superdesign doesn't have access to your codebase directly, this is important context)

Overall process for designing features on top of existing app:
1. Identify & understand existing UI of page related
2. Create/update a pixel perfect replica html in `.superde...