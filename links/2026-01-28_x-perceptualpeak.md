---
title: "WOW!!! If you have semantic memory tied to your UserPromptSubmit hooks, you M..."
source: "https://x.com/perceptualpeak/status/2016353615619961303?s=46"
date: 2026-01-28
tags: ["semantic memory", "PreToolUse hook", "workflow efficiency"]
platform: x
author: "@PerceptualPeak"
summary: "Zac explains how adding semantic memory to PreToolUse hooks creates self-correcting AI workflows by retrieving relevant context mid-stream."
---
WOW!!! If you have semantic memory tied to your UserPromptSubmit hooks, you MUST ALSO include it in your PreToolUse hook. I promise you - it will be an absolute GAME CHANGER. It will put your efficiency levels are over 9,000 (*vegeta voice*). 

How many times have you sat there, watching Claude code go through an extended workflow, just to notice it start to go down a path you just KNOW will be error filled - and subsequently take it forever to FINALLY figure it out? 

The problem with relying strictly on the UserPromptSubmit hook for semantic memory injection is the workflow drift from your original prompt. The memories it injects at the initiation of your prompt will be less and less relevant to the workflow the longer the workflow is. 

Claude has a beautiful thing called thinking blocks. These blocks are ripe for the picking - filled with meaning & intent - which is perfect for cosign similarly recall. Claude thinks to itself, "hmm, okay I'm going to do this because of this", then starts to engage the tool of its choice, and BOOM:

PreToolUse hook fires, takes the last 1,500 characters from the most recent thinking block from the active transcript, embeds it, pulls relevant memories from your vector database, and injects them to claude right before it starts using its tool (hooks are synchronous). This all happens in less than 500 milliseconds. 

The result? 

A self correcting Claude workflow. 

Based on my testing thus far, this is one of the most consequential additions to my context management system I've implemented yet. 

Photos: ASCII chart showing the workflow of the hook, and then two real use-cases of the mid-stream memory embedding actually being useful. 

If you already have semantic memory setup, just paste this tweet and photos into Claude code and tell it to implement it for you. Then enjoy the massive increase of workflow efficiency :)