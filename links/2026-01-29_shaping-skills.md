---
title: "rjs/shaping-skills"
source: "https://github.com/rjs/shaping-skills"
date: 2026-01-29
tags: ["Claude Code skills", "Shape Up methodology", "project shaping", "breadboarding tools"]
platform: github
author: "rjs"
summary: "A GitHub repository providing Claude Code skills for shaping and breadboarding workflows, adapting the Shape Up methodology for LLM-assisted project planning."
---
# rjs/shaping-skills

**URL:** https://github.com/rjs/shaping-skills
**Description:** Skills I use with Claude for shaping
**Language:** Shell
**Stars:** 948 | **Forks:** 69
**Last updated:** 2026-04-10

## README (excerpt)

# Shaping Skills

[Claude Code](https://claude.com/claude-code) skills for shaping and breadboarding — the methodology from [Shape Up](https://basecamp.com/shapeup) adapted for working with an LLM.

**Case study:** [Shaping 0-1 with Claude Code](https://x.com/rjs/status/2020184079350563263) walks through the full process of building a project from scratch using these skills. The source for that project is at [rjs/tick](https://github.com/rjs/tick).

## Skills

### Document skills — for collaborative work

These turn transcripts of real conversations into structured shaping documents. They're useful on real production projects where you're working with other people and want to capture what was said in a format you can act on.

**These are extremely GIGO (garbage in, garbage out).** They don't evaluate whether the material makes sense or is reasonable. They format and distill — that's it. When your inputs are good conversations with good thinking, they save a ton of time. When your inputs are bad, you get a nicely formatted bad document.

**`/framing-doc`** — Turn conversation transcripts into a framing document that captures the problem worth solving and why it was chosen over alternatives.

**`/kickoff-doc`** — Turn a shaped project kickoff transcript into a reference document for the builder, capturing what was shaped and agreed.

### Solo skills — more experimental

These are for working with Claude directly on shaping and design. They're more experimental and less battle-tested than the document skills.

**`/shaping`** — Iterate on both the problem (requirements) and solution (shapes) before committing to implementation. Separates what you need from how you might build it, with fit checks to see what's solved and what isn't.

**`/breadboarding`** — Map a system into UI affordances, code affordances, and wiring. Shows what users can do and how it works underneath — in one view. Good for slicing into vertical scopes.

## Install

```bash
# Clone the repo, then symlink each skill into your Claude Code skills directory
git clone https://github.com/rjs/shaping-skills.git ~/.local/share/shaping-skills
ln -s ~/.local/share/shaping-skills/framing-doc ~/.claude/skills/framing-doc
ln -s ~/.local/share/shaping-skills/kickoff-doc ~/.claude/skills/kickoff-doc
ln -s ~/.local/share/shaping-skills/breadboarding ~/.claude/skills/breadboarding
ln -s ~/.local/share/shaping-skills/shaping ~/.claude/skills/shaping
```

Each skill must be a direct child of `~/.claude/skills/` so Claude Code can discover it. Symlinks keep them updatable with `git pull`.

## Hook: Ripple Check

The repo includes a hook that reminds Claude to check for ripple effects when editing shaping documents. When Claude writes or edits a `.md` file with `shaping: true` in its frontmatter, the hook prompts a checklist — update affordance tables, fit checks, work streams, etc.

### Setup

1. Symlink the hook script:

```bash
mkdir -p ~/.claude/hooks
ln -s ~/.local/share/shaping-skills/hooks/shapi...