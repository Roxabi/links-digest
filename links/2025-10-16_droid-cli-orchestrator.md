---
title: "aeitroc/Pln-Droid-Orchestrator"
source: "https://github.com/aeitroc/Droid-CLI-Orchestrator"
date: 2025-10-16
tags: ["AI orchestration system", "Droid plugin", "development planning", "plan execution", "task coordination"]
platform: github
author: "aeitroc"
summary: "PLN Droid Orchestrator is a Droid plugin that converts development requests into reviewed plan packages and orchestrates execution through the main agent."
---
# aeitroc/Pln-Droid-Orchestrator

**URL:** https://github.com/LLMpsycho/Pln-Droid-Orchestrator
**Description:** 🤖 PLN Droid Orchestrator - An intelligent AI orchestration system for coordinating specialized droids to accomplish complex development tasks
**Language:** 
**Stars:** 364 | **Forks:** 35
**Homepage:** https://factory.ai/
**Last updated:** 2026-03-23

## README (excerpt)

# PLN Droid Orchestrator

PLN Droid Orchestrator is a Droid plugin for structured planning and in-chat execution orchestration.

It provides a single primary command, `/pln`, that turns a product or engineering request into a reviewed plan package and then hands execution back to the main agent in the same chat.

## Install

### Install from GitHub

```bash
droid plugin marketplace add https://github.com/aeitroc/Pln-Droid-Orchestrator
```

Droid will print the marketplace name it registered. Then install the plugin:

```bash
droid plugin install pln-pipeline@<marketplace-name>
```

### Install from a local checkout

```bash
droid plugin marketplace add /absolute/path/to/pln-droid-orchestrator
droid plugin install pln-pipeline@<marketplace-name>
```

If you already have Droid running, reload commands after installation.

## Quick start

1. Open a repository in Droid.
2. Run `/pln <task description>`.
3. Let `/pln` generate the plan package under `docs/plans/`.
4. Choose **Execute here now (main-agent orchestration)** when prompted.
5. The main agent will continue in the current chat and orchestrate implementation with visible `Task` calls.

## What `/pln` produces

Each planning run produces:

- a reviewed plan document
- a machine-readable execution manifest
- one task capsule per task

These artifacts are saved under `docs/plans/` so execution can stay grounded in an explicit contract.

## How plan creation works

`/pln` does not jump straight to task generation. It builds the plan through an explicit chain so the final artifacts are reviewable and execution-ready.

### 1. Intent and scope framing

The command first classifies the request and locks scope:

- identifies the task type and expected pipeline depth
- derives a scope contract from the user request and referenced materials
- flags blocking ambiguities before planning continues

### 2. Codebase grounding

Before planner droids reason about the work, the main agent gathers grounded context with visible `Task` calls:

- `explore` finds relevant files, patterns, and boundaries
- `librarian` is added when external libraries or framework details matter
- `tla-precheck` is used when the plan touches a stateful workflow that needs formal verification

This keeps the plan tied to the real repository instead of generic assumptions.

### 3. Planning phases

The planning chain is:

1. `metis` — clarifies intent, surfaces ambiguities, identifies failure points, and assesses test strategy
2. optional design checkpoint — used for architecture or research-heavy requests, then reviewed before full planning continues
3. `prometheus` — writes the executable plan, task waves, file targets, `dispatchAgent` values, and verification steps
4. `momus` — checks the plan for executability, reference validity, and blocking gaps

If a phase finds unresolved blocking issues, the chain stops and asks for clarification instead of silently guessing.

### 4. Plan package output

Once the chain passes review, `/pln` wri...