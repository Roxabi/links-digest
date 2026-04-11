---
title: "How Hermes Agent remembers, learns, and becomes yours "
source: "https://x.com/sidgraph/status/2036417870473863674?s=12"
date: 2026-03-24
tags: ["Hermes Agent", "NousResearch", "AI Architecture", "Memory Systems", "Cognitive Science"]
platform: x
author: "@sidgraph"
summary: "This article provides a deep analysis of the Hermes Agent codebase, explaining how its four-part cognitive memory architecture enables persistent identity and continuous learning."
---
Recently @NousResearch launched Hermes Agent and it is killing OpenClaw, this article explores the memory system, continuous learning and persona of Hermes Agent where OpenClaw misses the design principles.

Hermes wraps the LLM in a persistence layer organized around four distinct knowledge types, each with its own storage, retrieval, and failure mode. The result is an agent that accumulates facts, teaches itself procedures, recalls past experiences, and maintains identity across platforms and time.

This article walks through how that architecture works, based on a deep analysis of the codebase (https://github.com/nousresearch/hermes-agent).

The knowledge architecture

Hermes separates knowledge into four stores that mirror a well-known taxonomy from cognitive science: declarative (what's true), procedural (how to do things), episodic (what happened), and identity (who it is). The separation isn't metaphorical, it's an engineering constraint enforced at the system prompt level.

Declarative memory lives in two bounded plaintext files: MEMORY.md (2,200 chars) for environment facts and USER.md (1,375 chars) for user profile data, plus Honcho cloud for cross-platform persistence. Agent-curated. Always in the system prompt.

Procedural memory lives in SKILL.md files, unbounded, agent-created, loaded on demand. The agent writes these itself after complex tasks.

Episodic memory is passively logged into SQLite with FTS5 full-text search. Every message goes in. Searched only when the agent needs to recall past context.

Identity is assembled from layered prompts, SOUL.md, personality presets, platform hints, and Honcho's evolving AI peer representation. Always present. Never searched. Just there.

The routing across these stores is deterministic. When the agent encounters new information, it walks a strict decision tree:

Is this about the user? → USER.md. A reusable procedure? → Skill. An environment fact? → MEMORY.md. Task-specific state? → Don't store it; it's already in the session DB.

This matters because different knowledge types have different economics. Declarative facts are cheap to store but expensive to keep current. Procedural knowledge is expensive to acquire but cheap to reuse. Collapsing them into one store, the way most frameworks dump everything into a vector DB, creates retrieval noise that scales with usage.

Local memory

Two files. 3,575 characters combined. That's the entire declarative memory budget.

The constraint is the design. Bounded stores force the agent to curate. It can't hoard every detail, it has to decide what matters, governed by priority rules: user corrections first, then preferences, then environment facts, then procedural notes. Every entry earned its place.

Three operations: add (with duplicate rejection), replace (substring match + budget check), remove. No read, memory is always visible in the system prompt.

The frozen snapshot pattern. Memory loads from disk once at session start and gets injected into the system prompt as a frozen snapshot. Mid-session writes go to disk but do NOT update the system prompt. Why? Prefix cache stability. The system prompt is cached across every turn. Modifying it invalidates the cache and every subsequent API call pays the full reprocessing cost. The frozen snapshot trades intra-session consistency for cache efficiency, a bet that memories saved now matter more in future sessions.

The parallel to human memory consolidation during sleep isn't superficial. The agent's "day" is the session. Its "sleep" is the gap between sessions, when the snapshot thaws.

The nudge interval. What triggers proactive saves? A turn counter. nudge_interval (default: 10) periodically injects a reminder for the agent to evaluate whether anything recent is worth persisting. flush_min_turns (default: 6) prevents premature flushes on short sessions. Together they create a rhythm: work → nudge → evaluate → write to disk → continue.

Security scanning. Memory files survive across sessions, making them a high-value target. Before any write, _scan_memory_content() checks for prompt injection patterns, exfiltration commands, SSH backdoor patterns, and invisible unicode characters. Atomic writes via os.replace() + fsync() ensure concurrent readers never see a partial file.

What a real session looks like

Architecture descriptions are static. Here's how the pieces fire in sequence during an actual ~25-turn session:

Turns 1–2: User asks for a navbar, then corrects the color scheme, "use dark background, I hate light themes." Counter increments.

Turns 4–10: Eight more turns refining layout. At turn 10, the nudge fires. The agent evaluates the conversation, decides the dark-theme preference is worth keeping, writes "User hates light themes" to USER.md in the background. The system prompt doesn't change, frozen snapshot holds, but the file on disk now carries that preference for every future session.

Turns 11–22: More work. Token estimate crosses the 50% threshold. Compression triggers. Phase 1: sentinel fires, auxiliary model scans middle turns, flushes additional memories. Phase 2: middle turns summarized by Gemini Flash, head and tail protected. Phase 3: session splits in SQLite, system prompt reloads from disk, now incorporating both the nudge write and Phase 1 flush — fresh prefix cache begins.

Turn 23 onward: The agent has fewer raw turns but more persistent knowledge. Next session, days later, loads USER.md and the dark-theme preference is there from turn one. No re-explanation needed.

The dual-peer model

Local memory is fast but platform-bound. For cross-session modeling, Hermes integrates with Honcho.

Most agent memory systems model the user. Honcho models both sides. A user peer (evolving representation of who the user is) and an AI peer (evolving representation of who Hermes is). Both have observe_me=True, Honcho watches what both say and builds representations from observed behavior.

Anthropic's Persona Selection Model offers a frame for why this matters: post-training doesn't create a fundamentally new entity, it refines from the space of personas learned during pre-training. Hermes operationalizes a version of this at the application layer. The agent's identity isn't merely declared in a config file, it's observed, accumulated, and updated from actual behavior. Intent (SOUL.md) sets the target. Observed behavior (Honcho's AI peer) reflects reality. Drift between the two is visible.

The prefetch cycle. Fetching Honcho context requires an HTTP round-trip. Hermes fires background daemon threads at the end of each turn to prefetch context and dialectic results. Next turn consumes them via destructive reads. Zero HTTP latency on the hot path. Only the first turn pays cold-start cost.

The skill system

Declarative memory stores facts. Episodic memory stores transcripts. Neither stores procedures. This is where Hermes diverges most sharply from typical agents.

A Skill is a structured SKILL.md with YAML frontmatter, stored in ~/.hermes/skills/ by category. The lifecycle is a closed loop:

Task arrives → agent checks the skills index (always in the system prompt as a compact listing) → match found? Load the skill. No match? Solve from scratch. Post-task: was it complex (5+ tool calls)? Offer to save as skill. Used an existing skill that failed? Patch it immediately via skill_manage(action="patch").

This mirrors on-policy distillation at the application layer. The agent learns on its own trajectories, not canned examples and refines the extracted procedure through use. The immediate-patch-on-failure mechanism is what makes the loop converge rather than oscillate.

Progressive disclosure keeps token cost manageable. Tier 1: compact index in the system prompt (~2 tokens per skill). Tier 2: full SKILL.md, loaded on demand. Tier 3: specific supporting files. The agent is always aware of what it knows how to do without paying the token cost of knowing it all in detail.

Security gate. 60+ threat patterns across six categories: exfiltration, injection, destructive commands, persistence, network, obfuscation. Trust-tiered install policy: builtin (all pass) → trusted/agent-created (block dangerous) → community (block caution+). Blocked findings trigger atomic rollback.

Persona

SOUL.md defines core identity: "You are Hermes, an AI assistant made by Nous Research." Voice philosophy: "You're a peer. You know a lot but you don't perform knowing." Anti-patterns: no emojis, no sycophancy, no hype words. A pre-send checklist: did I answer the actual question? Can I cut a sentence?

SOUL.md is user-editable. You can rewrite it entirely. The user owns the agent's voice.

The full system prompt is assembled from 12 layers in strict order:

Layers 1–10 are cached: built once per session, amortized across every turn. Layers 11–12 are ephemeral, rebuilt per API call with turn-level context. A 12-layer identity costs roughly the same at steady state as a 2-layer one, because ten layers are already in the prefix cache.

Context compression

Every LLM has a finite context window. Hermes handles overflow with a three-phase compression lifecycle:

Phase 1 Memory flush. Before any context is lost, a sentinel fires: "Save anything worth remembering." One API call, only the memory tool available. Whatever the model saves survives.

Phase 2 Compress. First 3 messages and last 4 are protected. Middle turns are summarized by Gemini Flash (T=0.3). Boundary alignment ensures tool-call/result pairs are never split. State injection appends todo snapshots and file-read history.

Phase 3  Session split + rebuild. Old session ends in SQLite with end_reason: "compression". New session gets a parent FK. System prompt reloads from disk capturing Phase 1 flush writes and prefix cache re-establishes within 1–2 turns.

The result is counterintuitive: after compression, the agent has more persistent knowledge but less raw context. Compression isn't loss. It's consolidation.

Prime Intellect's work on Recursive Language Models frames a complementary approach having the model manage its own context via a Python REPL and sub-LLMs. Their insight: context folding and efficient attention are dual problems. Hermes solves the same problem at the application layer, which makes it model-agnostic.

How the systems connect

Memory ↔ Skills. Hard boundary enforced in the system prompt: facts go to memory, procedures go to skills. A single user correction can write to both the fact to MEMORY.md, the procedure patch to the skill.

Skills ↔ Session Search. The experiential learning mechanism. Agent encounters task → searches past sessions → finds working approach → crystallizes as skill → next time loads it directly. Episodic memory is raw experience. Procedural memory is extracted expertise.

Persona ↔ Honcho. SOUL.md seeds the AI peer identity. Over time the representation evolves from actual behavior creating a dual between declared intent and observed reality.

Compression ↔ Memory. The pre-compression flush turns compression from pure loss into a consolidation event. Post-compression, the system prompt rebuilds with a fresh snapshot that includes flush writes. The prefix cache cost (1–2 turns) is real but worthwhile.

What this gets right

Bounded stores force curation. The 3,575-character memory budget isn't a compromise. It's a design choice that ensures signal density.

Passive logging, active retrieval. The episodic store captures things the agent didn't know were important. Curation happens at read time, not write time.

Security at every persistence boundary. Every crossing from ephemeral context into durable storage is a checkpoint. Defense in depth against prompt injection.

Model-agnostic. Memory is plaintext. Skills are markdown. Sessions are SQLite. Swap the underlying LLM without losing knowledge, skills, or identity.

User-owned. SOUL.md is a text file you edit. Skills are directories you inspect. Memory is local-first. Everything lives in ~/.hermes/. Not a cloud service. Infrastructure you control.

The hardest problems in agent design aren't about making models smarter. They're about giving models the right infrastructure to accumulate knowledge, refine procedures, and maintain coherence over time.

Hermes Agent is open source: github.com/NousResearch/hermes-agent

Amazing work by @NousResearch, @Teknium, @sudoingX and the team ♥️

OSS is Winning!