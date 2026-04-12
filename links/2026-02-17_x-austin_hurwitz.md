---
title: "Give Your OpenClaw Agent Memory that Actually Works"
source: "https://x.com/austin_hurwitz/status/2023726021858783330?s=46"
date: 2026-02-17
tags: ["OpenClaw agent", "Memory management", "QMD search tool", "Markdown files"]
platform: x
author: "@austin_hurwitz"
summary: "The author outlines a three-step method to improve OpenClaw agent memory using QMD and a four-file organizational structure."
---
Everyone's experience with OpenClaw starts the same. It feels like this great unlock - an agent who has context on everything you do and can take actions on your behalf.

Then inevitably it hits a wall.

"I'm sorry, I don't remember what we were doing"

Memory is the biggest problem to solve and while my setup isn't fool proof it will get you in a much better place than your out of the box solution.

Step 1: Install QMD and make it the default (link:https://github.com/tobi/qmd)

Think of QMD as an on device search engine which indexes your various markdown files for more reliable, consistent, queries.

Tell your agent to always default to QMD for search and save it in it's Tools.md file.

Step 2: Split up memory into four files: long term memory,  daily notes, active tasks, and lessons.

The default memory system crams everything into a single markdown file. Over time this can become increasingly difficult for your agent to parse. Breaking the system into four files across the lifecycle of an agent's memory gives it more targeted searches depending on the context. When the agent makes a mistake be sure it always logs it in it's lessons file.

Step 3: Maintenance

Setup periodic crons as hygiene for your files.

Review memory for anything that's actually a tool and move it to tools.md

Move key lessons from daily notes and memory to lessons.md

Remove outdated context

Memory System Skill File (Point Your Agent Here)