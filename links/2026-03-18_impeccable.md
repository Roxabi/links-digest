---
title: "pbakaus/impeccable"
source: "https://github.com/pbakaus/impeccable"
date: 2026-03-18
tags: ["AI design tool", "frontend design", "design system", "GitHub repository"]
platform: github
author: null
summary: "Impeccable is a design language and skill framework that helps AI assistants create better frontend designs through commands, anti-patterns, and domain-specific references."
---
# pbakaus/impeccable

**URL:** https://github.com/pbakaus/impeccable
**Description:** The design language that makes your AI harness better at design.
**Language:** JavaScript
**Stars:** 18467 | **Forks:** 820
**License:** Apache License 2.0
**Homepage:** https://impeccable.style
**Last updated:** 2026-04-10

## README (excerpt)

# Impeccable

The vocabulary you didn't know you needed. 1 skill, 18 commands, and curated anti-patterns for impeccable frontend design.

> **Quick start:** Visit [impeccable.style](https://impeccable.style) to download ready-to-use bundles.

## Why Impeccable?

Anthropic created [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design), a skill that guides Claude toward better UI design. Impeccable builds on that foundation with deeper expertise and more control.

Every LLM learned from the same generic templates. Without guidance, you get the same predictable mistakes: Inter font, purple gradients, cards nested in cards, gray text on colored backgrounds.

Impeccable fights that bias with:
- **An expanded skill** with 7 domain-specific reference files ([view source](source/skills/impeccable/))
- **18 steering commands** to audit, review, polish, distill, animate, and more
- **Curated anti-patterns** that explicitly tell the AI what NOT to do

## What's Included

### The Skill: impeccable

A comprehensive design skill with 7 domain-specific references ([view skill](source/skills/impeccable/SKILL.md)):

| Reference | Covers |
|-----------|--------|
| [typography](source/skills/impeccable/reference/typography.md) | Type systems, font pairing, modular scales, OpenType |
| [color-and-contrast](source/skills/impeccable/reference/color-and-contrast.md) | OKLCH, tinted neutrals, dark mode, accessibility |
| [spatial-design](source/skills/impeccable/reference/spatial-design.md) | Spacing systems, grids, visual hierarchy |
| [motion-design](source/skills/impeccable/reference/motion-design.md) | Easing curves, staggering, reduced motion |
| [interaction-design](source/skills/impeccable/reference/interaction-design.md) | Forms, focus states, loading patterns |
| [responsive-design](source/skills/impeccable/reference/responsive-design.md) | Mobile-first, fluid design, container queries |
| [ux-writing](source/skills/impeccable/reference/ux-writing.md) | Button labels, error messages, empty states |

### 18 Commands

| Command | What it does |
|---------|--------------|
| `/impeccable teach` | One-time setup: gather design context, save to config |
| `/impeccable craft` | Full shape-then-build flow with visual iteration |
| `/impeccable extract` | Pull reusable components and tokens into the design system |
| `/audit` | Run technical quality checks (a11y, performance, responsive) |
| `/critique` | UX design review: hierarchy, clarity, emotional resonance |
| `/polish` | Final pass, design system alignment, and shipping readiness |
| `/distill` | Strip to essence |
| `/clarify` | Improve unclear UX copy |
| `/optimize` | Performance improvements |
| `/harden` | Error handling, onboarding, i18n, edge cases |
| `/animate` | Add purposeful motion |
| `/colorize` | Introduce strategic color |
| `/bolder` | Amplify boring designs |
| `/quieter` | Tone down overly bold designs |
| `/delight` | Add moments of joy |
| `/adapt` | Adapt fo...