---
title: "Btw you can add `context: fork` to run a skill in an isolated subagent. The m..."
source: "https://x.com/lydiahallie/status/2033603164398883042?s=46"
date: 2026-03-16
tags: ["claude", "agents", "subagent", "coding", "context-fork"]
platform: x
author: "@lydiahallie"
summary: "The author explains that adding `context: fork` allows running a skill in an isolated subagent, giving it a fresh context window while returning only the final result to the main context."
---
Btw you can add `context: fork` to run a skill in an isolated subagent. The main context only sees the final result, not the intermediate tool calls

It gets a fresh context window with CLAUDE.md + your skill as the prompt. The `agent` field even lets you set the subagent type! https://t.co/pzVAPWHCwJ