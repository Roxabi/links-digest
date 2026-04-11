---
title: "nicobailon/pi-subagents"
source: "https://github.com/nicobailon/pi-subagents"
date: 2026-04-06
tags: ["pi-extension", "subagents", "task-delegation", "async", "typescript"]
platform: github
author: null
summary: "A Pi extension for delegating tasks to asynchronous subagents with support for chains, parallel execution, and session sharing."
---
# nicobailon/pi-subagents

**URL:** https://github.com/nicobailon/pi-subagents
**Description:** Pi extension for async subagent delegation with truncation, artifacts, and session sharing
**Language:** TypeScript
**Stars:** 708 | **Forks:** 91
**Last updated:** 2026-04-09

## README (excerpt)

<p>
  <img src="banner.png" alt="pi-subagents" width="1100">
</p>

# pi-subagents

Pi extension for delegating tasks to subagents with chains, parallel execution, TUI clarification, and async support.

https://github.com/user-attachments/assets/702554ec-faaf-4635-80aa-fb5d6e292fd1

## Installation

```bash
pi install npm:pi-subagents
```

To remove:

```bash
npx pi-subagents --remove
```

If you use [pi-prompt-template-model](https://github.com/nicobailon/pi-prompt-template-model), you can wrap subagent delegation in a slash command:

```markdown
---
description: Take a screenshot
model: claude-sonnet-4-20250514
subagent: browser-screenshoter
cwd: /tmp/screenshots
---
Use url in the prompt to take screenshot: $@
```

Then `/take-screenshot https://example.com` switches to Sonnet, delegates to the `browser-screenshoter` agent with `/tmp/screenshots` as the working directory, and restores your model when done. Runtime overrides like `--cwd=<path>` and `--subagent=<name>` work too.

pi-prompt-template-model is entirely optional — pi-subagents works standalone through the `subagent` tool and slash commands. If you want reusable prompt-template workflows on top of subagents, including `/chain-prompts` and compare-style prompts like `pi-prompt-template-model`'s `/best-of-n` example, install [pi-prompt-template-model](https://github.com/nicobailon/pi-prompt-template-model) separately and copy any example prompts you want from its `examples/` directory into `~/.pi/agent/prompts/`.

## Agents

Agents are markdown files with YAML frontmatter that define specialized subagent configurations.

**Agent file locations:**

| Scope | Path | Priority |
|-------|------|----------|
| Builtin | `~/.pi/agent/extensions/subagent/agents/` | Lowest |
| User | `~/.pi/agent/agents/{name}.md` | Medium |
| Project | `.pi/agents/{name}.md` (searches up directory tree) | Highest |

Use `agentScope` parameter to control discovery: `"user"`, `"project"`, or `"both"` (default; project takes priority).

**Builtin agents:** The extension ships with ready-to-use agents — `scout`, `planner`, `worker`, `reviewer`, `context-builder`, `researcher`, and `delegate`. They load at lowest priority so any user or project agent with the same name overrides them. Builtin agents appear with a `[builtin]` badge in listings and cannot be modified through management actions (create a same-named user agent to override instead).

> **Note:** The `researcher` agent uses `web_search`, `fetch_content`, and `get_search_content` tools which require the [pi-web-access](https://github.com/nicobailon/pi-web-access) extension. Install it with `pi install npm:pi-web-access`.

**Agent frontmatter:**

```yaml
---
name: scout
description: Fast codebase recon
tools: read, grep, find, ls, bash, mcp:chrome-devtools  # mcp: requires pi-mcp-adapter
extensions:                 # absent=all, empty=none, csv=allowlist
model: claude-haiku-4-5
thinking: high               # off, minimal, low, medium, high, xhigh
skill: saf...