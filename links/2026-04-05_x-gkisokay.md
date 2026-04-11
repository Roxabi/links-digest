---
title: "Practical tips to save time and tokens when using Claude or Codex externally..."
source: "https://x.com/gkisokay/status/2040627715079098737"
date: 2026-04-05
tags: ["AI Agents", "Claude", "Debugging", "LLM", "Hermes"]
platform: x
author: "@gkisokay"
summary: "Practical tips for efficiently building and debugging Hermes and OpenClaw agents using external LLMs like Claude or Codex."
---
Practical tips to save time and tokens when using Claude or Codex externally to build or debug your Hermes and OpenClaw agents.

1. After building externally, debrief Hermes/OpenClaw on every new feature

In Hermes case, it owns the orchestration standards, memory architecture, and self-improving skill loops. Hermes itself should review any feature built outside to confirm it fits the framework before it runs.

Do the same for OpenClaw as well, to ensure it fits its execution standards.

2. Scan the whole codebase when switching LLM models

Don't assume a quick LLM swap will work. Ask Claude/Codex to audit every prompt string, config file, and env variable for stale model names. One missed reference will silently route to the wrong model, costing you hours of debugging.

3. Test viciously. Normally, agents fail new features on first runs

Define the exact desired output, watch for it, and if it doesn't appear, keep iterating until it's consistent. Repetition is the only honest test.

4. Describe symptoms, not solutions

Don't tell Claude/Codex how to fix it; describe what's wrong. "The memory isn't persisting between runs." Beat "rewrite the storage layer." Let it figure out the approach. You'll get a clearer answer and see where the actual problem is.

5. Paste the error, don't summarize it

When receiving errors from your agent, use the exact error or full log dump every time. Claude reads noise better than you do, and the part you thought was irrelevant might be the part that matters.

6. If it breaks again later, return to the same session

If the same feature fails weeks later, go back to the original Claude Code/Codex session before starting fresh. The context for what was built, why, and what was already tried is sitting there. Starting a new chat throws all of that away, and you'll loop the same decisions.

These tips should address many of the recurring questions I've been receiving. Let me know if I can help you out further.