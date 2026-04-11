---
title: "Anthropic just banned Claude subscriptions from powering OpenClaw."
source: "https://x.com/gkisokay/status/2040352080196755780?s=12"
date: 2026-04-04
tags: ["AI Agents", "LLM Architecture", "Cost Optimization", "Multi-Model Stack", "OpenClaw"]
platform: x
author: "@gkisokay"
summary: "The author describes a resilient multi-LLM agent stack that uses local models for volume and subscriptions for execution to avoid service bans and minimize costs."
---
Anthropic just banned Claude subscriptions from powering OpenClaw.

Here's why my stack was already built for this.

I never ran Opus 4.6 through a subscription for OpenClaw or Hermes. It runs in Claude Code for complex external dev only. Same with GPT-5.4 in Codex.

The internal agent runtime is a completely different stack:

1. Qwen3.5 9B runs locally. $0. Always on. Feeds the subconscious ideation loop 24/7. Beats GPT-OSS-120B by 13x. Awesome.

2. MiniMax M2.7 is the agent's backbone. 97% skill adherence, built for agents, $0.30/M tokens. The $10 plan allows for 1500 calls every 5 hours. Amazing.

3. GPT-5.4 mini is the Hermes brain. debates ideas with the subconscious, builds output, ~$0.075 avg per run. It's smart enough to orchestrate your entire system, and you can actually use your subscription plan here via OAuth. Incredible!

Over the last 24 hours, the subconscious ran 15 times, for a total of $1.58. Not too shabby for an always-improving agentic system.

The lesson is to build your agent stack on a multiple LLM stack.

Local models handle volume. Generous subscription models handle execution and judgment. You own the cost structure.

Full-stack breakdown in the table. (see image)