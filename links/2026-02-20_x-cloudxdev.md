---
title: "📂 Claude Code Tasks — how to set up shared task lists for subagents , Bookmar..."
source: "https://x.com/cloudxdev/status/2024787905852387329?s=46"
date: 2026-02-20
tags: ["Claude Code", "Subagents", "Task Management"]
platform: x
author: "@cloudxdev"
summary: "A guide on configuring shared task lists in Claude Code to enable parallel subagent coordination and real-time task tracking."
---
📂 Claude Code Tasks — how to set up shared task lists for subagents , Bookmark it

My Setup:
1. Add this to your ~/.claude/CLAUDE.md:
```
## Tasks

Auto-create tasks when work has 3+ steps, dependencies, or spans multiple files. ALWAYS create tasks when spinning up subagents.

- Subagents get full task access: create, update, mark complete
- Tasks support dependencies (blocks/blockedBy) — use them for ordered work
- For single-step or trivial work, skip tasks — just do it
```

2. To share a task list across sessions or subagents:
```
CLAUDE_CODE_TASK_LIST_ID=my-project claude
```
Works with claude -p and the Agent SDK too. All sessions with the same ID see real-time updates.

3. Fan out parallel workers:
TASK_LIST="my-feature"

# First session creates the plan
CLAUDE_CODE_TASK_LIST_ID=$TASK_LIST claude -p "Create tasks for: 1) build API 2) write tests 3) add docs. Set dependencies."

# Then spin up workers
CLAUDE_CODE_TASK_LIST_ID=$TASK_LIST claude -p "Pick up the next pending task and complete it" &
CLAUDE_CODE_TASK_LIST_ID=$TASK_LIST claude -p "Pick up the next pending task and complete it" &
wait

Tasks are stored in ~/.claude/tasks/ — you can build your own tooling on top of them.