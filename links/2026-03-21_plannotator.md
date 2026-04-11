---
title: "backnotprop/plannotator"
source: "https://github.com/backnotprop/plannotator"
date: 2026-03-21
tags: ["ai-coding", "code-review", "developer-tools", "typescript", "open-source"]
platform: github
author: null
summary: "Plannotator is a visual tool for annotating and reviewing AI coding agent plans and code diffs, enabling team collaboration and direct feedback to agents."
---
# backnotprop/plannotator

**URL:** https://github.com/backnotprop/plannotator
**Description:** Annotate and review coding agent plans and code diffs visually, share with your team, send feedback to agents with one click.
**Language:** TypeScript
**Stars:** 4087 | **Forks:** 273
**License:** Apache License 2.0
**Topics:** claude-code, opencode, obsidian, pi-mono, plan-mode, codex
**Homepage:** https://plannotator.ai
**Last updated:** 2026-04-11

## README (excerpt)

<p align="center">
  <img src="apps/marketing/public/og-image.webp" alt="Plannotator" width="80%" />
</p>

# Plannotator

Interactive Plan & Code Review for AI Coding Agents. Mark up and refine your plans or code diffs using a visual UI, share for team collaboration, and seamlessly integrate with **Claude Code**, **Copilot CLI**, **Gemini CLI**, **OpenCode**, **Pi**, and **Codex**.

**Plan Mode Demos:**
<table>
<tr>
<td align="center" width="50%">
<h3>Claude Code</h3>
<a href="https://www.youtube.com/watch?v=a_AT7cEN_9I">
<img src="apps/marketing/public/youtube.png" alt="Claude Code Demo" width="100%" />
</a>
<p><a href="https://www.youtube.com/watch?v=a_AT7cEN_9I">Watch Demo</a></p>
</td>
<td align="center" width="50%">
<h3>OpenCode</h3>
<a href="https://youtu.be/_N7uo0EFI-U">
<img src="apps/marketing/public/youtube-opencode.png" alt="OpenCode Demo" width="100%" />
</a>
<p><a href="https://youtu.be/_N7uo0EFI-U">Watch Demo</a></p>
</td>
</tr>
</table>

**New:** [Code Review](https://x.com/backnotprop/status/2031145299738263567?s=20)


### Features

<table>
<tr><td><strong>Visual Plan Review</strong></td><td>Built-in hook</td><td>Approve or deny agent plans with inline annotations</td></tr>
<tr><td><strong>Plan Diff</strong></td><td>Automatic</td><td>See what changed when the agent revises a plan</td></tr>
<tr><td><strong>Code Review</strong></td><td><code>/plannotator-review</code></td><td>View git diffs or remote PRs. Package annotations and ask AI about the code as you review.</td></tr>
<tr><td><strong>Annotate Any File</strong></td><td><code>/plannotator-annotate</code></td><td>Annotate any markdown file and send feedback to your agent</td></tr>
<tr><td><strong>Annotate Last Message</strong></td><td><code>/plannotator-last</code></td><td>Annotate the agent's last response and send structured feedback</td></tr>
</table>

#### Sharing Plans

Plannotator lets you privately share plans, annotations, and feedback with colleagues. For example, a colleague can annotate a shared plan, and you can import their feedback to send directly back to the coding agent.

**Small plans** are encoded entirely in the URL hash. No server involved, nothing stored anywhere.

**Large plans** use a short link service with **end-to-end encryption**. Your plan is encrypted with AES-256-GCM in your browser before upload. The server stores only ciphertext it cannot read. The decryption key lives only in the URL you share. Pastes auto-delete after 7 days.

- Zero-knowledge storage, similar to [PrivateBin](https://privatebin.info/)
- Fully open source and **self-hostable** ([see docs](https://plannotator.ai/docs/guides/sharing-and-collaboration/))

## Install

- [Claude Code](#install-for-claude-code)
- [Copilot CLI](#install-for-copilot-cli)
- [Gemini CLI](#install-for-gemini-cli)
- [OpenCode](#install-for-opencode)
- [Pi](#install-for-pi)
- [Codex](#install-for-codex)

## Install for Claude Code

**Install the `plannotator` command:**

**macOS / Linux / WSL:**

```bash
cur...