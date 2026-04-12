---
title: "JackChen-me/open-multi-agent"
source: "https://github.com/JackChen-me/open-multi-agent"
date: 2026-04-12
tags: []
platform: github
author: null
summary: "TypeScript multi-agent framework — one runTeam() call from goal to result. Auto task decomposition, parallel execution. 3 dependencies, deploys anywhere Node.js runs."
---
# JackChen-me/open-multi-agent

**URL:** https://github.com/JackChen-me/open-multi-agent
**Description:** TypeScript multi-agent framework — one runTeam() call from goal to result. Auto task decomposition, parallel execution. 3 dependencies, deploys anywhere Node.js runs.
**Language:** TypeScript
**Stars:** 5634 | **Forks:** 2243
**License:** MIT License
**Topics:** agent-framework, ai-agents, claude, llm, model-agnostic, multi-agent, openai, orchestration, task-scheduling, typescript, anthropic, nodejs, ollama, structured-output, tool-use, gemma4
**Last updated:** 2026-04-11

## README (excerpt)

# Open Multi-Agent

The lightweight multi-agent orchestration engine for TypeScript. Three runtime dependencies, zero config, goal to result in one `runTeam()` call.

CrewAI is Python. LangGraph makes you draw the graph by hand. `open-multi-agent` is the `npm install` you drop into an existing Node.js backend when you need a team of agents to work on a goal together. Nothing more, nothing less.

3 runtime dependencies · 35 source files · Deploys anywhere Node.js runs · Mentioned in [Latent Space](https://www.latent.space/p/ainews-a-quiet-april-fools) AI News (top AI engineering newsletter, 170k+ subscribers)

[![GitHub stars](https://img.shields.io/github/stars/JackChen-me/open-multi-agent)](https://github.com/JackChen-me/open-multi-agent/stargazers)
[![license](https://img.shields.io/github/license/JackChen-me/open-multi-agent)](./LICENSE)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.6-blue)](https://www.typescriptlang.org/)
[![coverage](https://img.shields.io/badge/coverage-88%25-brightgreen)](https://github.com/JackChen-me/open-multi-agent/actions)

**English** | [中文](./README_zh.md)

## What you actually get

- **Goal to result in one call.** `runTeam(team, "Build a REST API")` kicks off a coordinator agent that decomposes the goal into a task DAG, resolves dependencies, runs independent tasks in parallel, and synthesizes the final output. No graph to draw, no tasks to wire up.
- **TypeScript-native, three runtime dependencies.** `@anthropic-ai/sdk`, `openai`, `zod`. That is the whole runtime. Embed in Express, Next.js, serverless functions, or CI/CD pipelines. No Python runtime, no subprocess bridge, no cloud sidecar.
- **Multi-model teams.** Claude, GPT, Gemini, Grok, Copilot, or any OpenAI-compatible local model (Ollama, vLLM, LM Studio, llama.cpp) in the same team. Run the architect on Opus 4.6, the developer on GPT-5.4, the reviewer on local Gemma 4, all in one `runTeam()` call. Gemini ships as an optional peer dependency: `npm install @google/genai` to enable.

Other features (structured output, task retry, human-in-the-loop, lifecycle hooks, loop detection, observability) live below the fold and in [`examples/`](./examples/).

## Philosophy: what we build, what we don't

Our goal is to be the simplest multi-agent framework for TypeScript. Simplicity does not mean closed. We believe the long-term value of a framework is the size of the network it connects to, not its feature checklist.

**We build:**
- A coordinator that decomposes a goal into a task DAG.
- A task queue that runs independent tasks in parallel and cascades failures to dependents.
- A shared memory and message bus so agents can see each other's output.
- Multi-model teams where each agent can use a different LLM provider.

**We don't build:**
- **Agent handoffs.** If agent A needs to transfer mid-conversation to agent B, use [OpenAI Agents SDK](https://github.com/openai/openai-agents-python). In our model, each agent owns one task end-to-end, with no mid-conve...