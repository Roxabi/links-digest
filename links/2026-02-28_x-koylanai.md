---
title: "Finally had some time to read @trq212 and @RLanceMartin prompt-caching articl..."
source: "https://x.com/koylanai/status/2027819266972782633?s=46"
date: 2026-02-28
tags: []
platform: x
author: "@koylanai"
summary: "Muratcan Koylan synthétise des insights clés sur le prompt caching de Claude : ordonner les contenus statiques avant dynamiques, injecter les mises à jour via messages plutôt que via system prompt, ne jamais modifier les tools mid-session, et isoler les contextes par agent lors du model switching. Le cache hit rate doit être traité comme une métrique de production au même titre que l'uptime."
---
Finally had some time to read @trq212 and @RLanceMartin prompt-caching articles. They are dense and include important insights into context engineering.

1. Static-First Ordering
Claude Code's entire prompt is ordered for cache hits:
Static system prompt & tools -> CLAUDE[.]md -> Session context -> Messages

This is the same principle behind progressive disclosure architectures, but applied to inference cost. Static, per-session instructions should come before dynamic data. 

Every time dynamic content appears before static content, you're paying full price on cache misses, which also increases latency.

2. Messages Over System Prompt Mutations
Instead of updating the system prompt (which breaks cache), inject updates via tags in user messages.

For multi-turn sessions, if context changes mid-conversation, appending that as a message preserves the cache prefix. Mutating the system prompt to include updated context would be expensive.

3. Subagents for Model Switching
Switching models mid-session destroys the cache because caches are model-specific. Claude Code uses subagents with handoff messages instead.

If you're 100K tokens into a conversation with Opus, it's actually more expensive to switch to Haiku for a simple question than to just let Opus answer it. A warm cache on an expensive model beats a cold cache on a cheap model.

If your multi-agent system uses different models for different tasks, isolate each agent's context. The orchestrator passes structured handoff messages between agents rather than switching models within a single conversation thread.

4. Never Change Tools Mid-Session
Tools are part of the cached prefix. Adding or removing one invalidates the entire cache. Claude Code's Plan Mode doesn't swap tool sets, it uses EnterPlanMode / ExitPlanMode as tools themselves, with instructions delivered via messages. The tool definitions never change.

Instead of removing tools, they send lightweight stubs with defer_loading that the model can discover on demand in tool search. Full schemas load only when selected. The prefix stays stable.

5. Cache Hit Rate Is a Production Metric
Claude Code monitors prompt cache hit rate the same way most teams monitor uptime, they set alerts and treat drops as production incidents.

If you're building agents and not tracking cache_creation_input_tokens vs cache_read_input_tokens from API responses, you're missing a major cost and latency lever. Put it on your dashboard next to latency and error rate.

6. Cache-Safe Compaction
When the context window fills up, Claude Code summarizes but uses the exact same system prompt, tools, and conversation prefix so the compaction request reuses the parent's cache.

The right approach is to append the compaction instruction as a new user message. 

Same prefix = cache hit on the entire history.