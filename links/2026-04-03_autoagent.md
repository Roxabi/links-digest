---
title: "kevinrgu/autoagent"
source: "https://github.com/kevinrgu/autoagent"
date: 2026-04-03
tags: ["autonomous agents", "agent engineering", "benchmark optimization", "Python framework", "meta-agent system"]
platform: github
author: null
summary: "AutoAgent enables AI to autonomously build and iterate on agent harnesses by modifying configurations and running benchmarks to optimize scores."
---
# kevinrgu/autoagent

**URL:** https://github.com/kevinrgu/autoagent
**Description:** autonomous harness engineering
**Language:** Python
**Stars:** 4019 | **Forks:** 450
**Last updated:** 2026-04-03

## README (excerpt)

<p align="center">
  <a href="https://www.thirdlayer.inc">
    <img src="https://www.thirdlayer.inc/thirdlayer-logo.svg" alt="thirdlayer" width="200">
  </a>
</p>

<blockquote>
<p>We're launching a product around self-configuring agents soon. <a href="https://form.typeform.com/to/ZQbnbO09">Sign up here.</a><br>We're hiring engineers. If this work interests you, reach out to <a href="mailto:hello@thirdlayer.inc">hello@thirdlayer.inc</a> with your Github link.</p>
</blockquote>

# AutoAgent

> Like autoresearch but for agent engineering. Give an AI agent a task, let it build and iterate on an agent harness autonomously overnight. It modifies the system prompt, tools, agent configuration, and orchestration, runs the benchmark, checks the score, keeps or discards the change, and repeats.

![teaser](progress.png)

The core idea is the same: you're not touching the harness Python files like you normally would as an engineer. Instead, you program `program.md`, the Markdown file that provides context to the meta-agent and defines the agent-engineering loop.

## How it works

The repo has a few files and directories that matter:

- **`agent.py`** -- the entire harness under test in a single file. It contains
  config, tool definitions, agent registry, routing/orchestration, and the
  Harbor adapter boundary. The adapter section is explicitly marked as fixed;
  the rest is the primary edit surface for the meta-agent.
- **`program.md`** -- instructions for the meta-agent + the directive (what
  kind of agent to build). **This file is edited by the human**.
- **`tasks/`** -- evaluation tasks in
  [harbor](https://github.com/laude-institute/harbor) format. In a clean
  baseline branch, benchmark payloads may be omitted and added in
  benchmark-specific branches.
- **`.agent/`** -- optional workspace artifacts for reusable instructions,
  notes, prompts, or skills.

The metric is total **score** produced by the benchmark's task test suites. The
meta-agent hill-climbs on this score.

## Quick start

**Requirements:** Docker, Python 3.10+, [uv](https://docs.astral.sh/uv/), and
whatever model-provider credentials your current `agent.py` harness requires.

```bash
# 1. Install uv (if you don't have it)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install dependencies
uv sync

# 3. Set up the environment variables required by your current agent/runtime
# Example:
cat > .env << 'EOF'
OPENAI_API_KEY=...
EOF

# 4. Build base image
docker build -f Dockerfile.base -t autoagent-base .

# 5. Add tasks to tasks/ (see Task format section below)

# 6. Run a single benchmark task
rm -rf jobs; mkdir -p jobs && uv run harbor run -p tasks/ --task-name "<task-name>" -l 1 -n 1 --agent-import-path agent:AutoAgent -o jobs --job-name latest > run.log 2>&1

# 7. Run all tasks in parallel (-n = concurrency, default 4)
rm -rf jobs; mkdir -p jobs && uv run harbor run -p tasks/ -n 100 --agent-import-path agent:AutoAgent -o jobs --job-name latest > run.log 2>&1
```

## Running the...