---
title: "andrew-yangy/gru-ai"
source: "https://github.com/andrew-yangy/agent-conductor"
date: 2026-02-22
tags: ["AI agents", "autonomous agents", "software development", "team pipeline", "context engineering"]
platform: github
author: "andrew-yangy"
summary: "gruAI is an autonomous AI agent team system that enables one-person companies to manage software development through a 15-step pipeline where agents brainstorm, build, review, and ship."
---
# andrew-yangy/gru-ai

**URL:** https://github.com/andrew-yangy/gru-ai
**Description:** Autonomous AI agent team for one-man companies. Context engineering + harness engineering drive a pipeline that brainstorms, builds, reviews, and ships.
**Language:** TypeScript
**Stars:** 123 | **Forks:** 15
**License:** MIT License
**Topics:** ai-agents, autonomous-agents, context-engineering, harness-engineering
**Last updated:** 2026-03-11

## README (excerpt)

<h1 align="center">gruAI</h1>

<h3 align="center">Stop coding with AI.<br/>Start running an AI team.</h3>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green" alt="MIT License" /></a>
  <a href="https://www.typescriptlang.org/"><img src="https://img.shields.io/badge/TypeScript-5.9-blue" alt="TypeScript" /></a>
  <a href="https://www.npmjs.com/package/gru-ai"><img src="https://img.shields.io/npm/v/gru-ai" alt="npm version" /></a>
  <a href="#"><img src="https://img.shields.io/badge/status-alpha-orange" alt="Status: Alpha" /></a>
</p>

<p align="center">
  <a href="#what-is-gruai">What Is gruAI?</a> •
  <a href="#quickstart">Quickstart</a> •
  <a href="#the-pipeline">The Pipeline</a> •
  <a href="#your-team">Your Team</a> •
  <a href="#why-is-the-output-better">Why It Works</a> •
  <a href="#the-context-tree">Context Tree</a>
</p>

<p align="center">
  <img src="docs/assets/demo.gif" alt="gruAI pixel-art office with agents working" width="720" />
</p>

---

## What Is gruAI?

### Most AI tools help you code faster. gruAI lets you stop coding entirely.

You run your AI team just like a CEO, and the agents handle the rest: engineering, marketing, operations, and more. You hand down a directive ("add dark mode to the dashboard"). Your agents brainstorm the approach, challenge your assumptions, build, review each other's work, and ship — you approve the result.

The system is designed for **depth, not speed.** Agents accumulate institutional memory across directives — lessons learned, design rationale, standing corrections. Your 10th directive runs better than your 1st because the team remembers what went wrong.

**You make decisions. Agents make software.** Every directive flows through a 15-step pipeline — triage, audit, brainstorm, plan, build, review, and ship — grounded in published research from Anthropic and OpenAI on what actually makes AI output reliable.

---

## Is gruAI Right for You?

- ✅ You're running 10+ terminals, juggling context, reprompting the same mistakes — and you want to hand down a directive and walk away
- ✅ You've been burned by agents that "review" their own code — you want reviews that are mandatory, mechanical, and impossible to skip
- ✅ Your agents forget everything between sessions — you want a team that remembers what broke last time
- ✅ You're the bottleneck for every decision, every prompt, every context refresh — you want to be the CEO, not the project manager
- ✅ You like running a one-person company with a full AI team, and you want it to actually feel that way — not like managing a chatbot farm
- ✅ You want agents that push back on your ideas before building, not agents that say yes and ship the wrong thing

---

## The Pipeline

You type: `/directive Create a landing page for gruAI`. Here's what happens next.

**1. Triage** — *Automated*

Classified **heavyweight** — touches copy, layout, SEO, and design across multiple files. Each agent gets [role-scoped context](htt...