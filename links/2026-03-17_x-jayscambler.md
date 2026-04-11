---
title: "autocontext: The Recursive Self-Improving Loop that Many are Calling AGI"
source: "https://x.com/JayScambler/status/2033971974284714355"
date: 2026-03-17
tags: ["AI Agents", "Recursive Self-Improvement", "Infrastructure", "autocontext", "Persistent Memory"]
platform: x
author: "@JayScambler"
summary: "The article introduces autocontext, a closed-loop optimization infrastructure that enables AI agents to learn from past runs by analyzing results and updating a shared knowledge base, effectively"
---
Look, is that title a bit of hyperbole? Ya, I'll admit it is, but maybe this is an early glimpse into the infrastructure and harnessing that AGI will require beyond the model level.

The Problem

Your agent works. Then the context window fills up, the provider compacts the conversation, and it forgets the thing it figured out twenty minutes ago. You restart. It makes the same mistake. You patch the prompt. It works for a week. Then a different failure mode shows up and you're back to reading logs at 2am.

This is the actual day-to-day of harness engineering. Not the "look at my agent book a flight" demo. The part where you're trying to figure out why your agent solved the same problem correctly in generation 3, forgot how in generation 7, and is now confidently doing something worse than what it started with.

The root cause isn't the model. It's the infrastructure. Agents have no persistent memory across runs. No mechanism to carry forward what worked and what didn't. Every invocation starts cold. The context window is a goldfish brain - useful for the current conversation, useless for institutional knowledge.

autocontext is the feedback loop that's missing.

What autocontext Actually Does

autocontext runs your agent against a task repeatedly. After each run, a multi-agent team analyzes the results and updates a shared knowledge base. The next run inherits everything the previous run learned.

The loop looks like this:

Competitor generates a strategy for the task

Translator converts raw competitor output into a validated, structured JSON strategy

Analyst examines what happened (findings, root causes, recommendations)

Coach distills the analysis into a playbook update and competitor hints

Architect proposes and generates tooling improvements

Curator gates the quality of playbook updates and consolidates lessons

An Orchestrator sequences the entire pipeline, handling parallel execution, retry logic, and the handoff between agents. It's the conductor: it doesn't generate content, but nothing runs without it.

Each generation runs through tournament matches (for game scenarios) or LLM judge evaluation (for agent tasks) with Elo-based progression gating. Strategies that don't improve get rolled back. Knowledge only persists when it's validated.

This isn't prompt engineering. It's a closed-loop optimization system with persistence.

Game Scenarios vs Agent Tasks

autocontext ships with two kinds of scenarios and the distinction matters.

Game scenarios are adversarial environments with clear win conditions. Think capture-the-flag, resource allocation under constraints, multi-agent coordination problems. They exist because games give you something most agent benchmarks don't: an objective scoring function that doesn't depend on an LLM judge's opinion. When your agent's Elo rating goes up, it actually got better. No ambiguity.

Agent tasks are the open-ended problems that look more like real work. Things like write an incident postmortem, design a clinical trial protocol, construct a formal mathematical proof, draft a cybersecurity incident response plan. These use LLM judges with multi-dimensional rubrics. Describe what you want in natural language and autocontext generates a spec, builds a rubric, and starts the improvement loop.

The two are complementary. Games give you hard guarantees the harness can't fake - if knowledge accumulation is working, scores go up against real opponents. Agent tasks give you domain flexibility to point the same loop at any problem you can describe.

Beyond Code: Where This Gets Interesting

The scenario system is deliberately domain-agnostic. The escalation tests we've been running internally go well beyond software engineering:

Formal proofs: constructing and verifying step-by-step mathematical arguments, where each round tightens logical rigor

Clinical trial design: protocol generation for drug trials with randomization, demographics, and regulatory constraints

Geopolitical wargaming: crisis response planning with competing stakeholder objectives and escalation dynamics

Financial portfolio optimization: regime-aware allocation strategies that adapt to macroeconomic indicators

Cybersecurity incident response: triage, containment, and remediation planning against evolving threat scenarios

Drug interaction analysis: evaluating compound pairs for safety and efficacy

Ecosystem simulation: multi-cycle environments where agents must adapt across changing conditions

The pattern is the same in every case: run, evaluate, learn, persist, repeat. The harness doesn't care whether the agent is writing code or designing a clinical protocol. It cares whether the output got better.

Why Knowledge Accumulation Matters

The playbook is the key abstraction. It's a living document that grows across runs. It contains:

Strategies that worked, with the scores that proved they worked

Strategies that failed, with specific failure modes to avoid

Tier-specific rules (e.g., "when resources are low, keep total commitment under 1.05")

Generated tools that automate analysis patterns the architect discovered

When we ran autocontext against a simple grid capture-the-flag scenario with the live Anthropic API, it accumulated 33 distinct lessons across 2 generations. Strategies evolved from generic parameter sweeps to tier-classified approaches with specific resource density thresholds. The playbook went from empty to 5,870 characters of actionable operational knowledge that help future agents one-shot the same scenario.

That knowledge transfers to new runs. An agent starting fresh with a populated playbook outperforms one starting cold. That's the compounding effect and why context compaction is the enemy.

The Judge Makes or Breaks Everything

Evaluation quality determines whether the loop improves or just churns. The judge subsystem is where most of the engineering went:

Multi-dimensional rubrics. Each task defines specific dimensions (accuracy, clarity, actionability, etc.). The judge scores each dimension independently. This means revisions can target the weakest dimension instead of blindly rewriting everything.

Parse resilience. LLM outputs are messy. The judge has a 4-tier fallback parser: marker-delimited JSON → raw JSON extraction → regex patterns → structured retry. In adversarial testing, malformed judge outputs get thrown at the loop and it recovers cleanly every time.

Adversarial validation. Tested with vague rubrics ("Is it good? Rate quality."), contradictory criteria ("Be extremely technical" AND "Be understandable by a 5-year-old"), and hallucination-prone tasks. The system handled all of them. The hallucination test was most impressive: fabricated claims scored 0 across all dimensions, and the revision correctly stated the source material may not exist.

Frontier-to-Local: Start Expensive, End Cheap

One of the more ambitious pieces: autocontext can distill strategies from frontier models into local models.

We started with MLX on Apple Silicon deliberately. A huge number of developers building with agents (especially in the OpenClaw and Claude Code ecosystems) are on M-series Macs. MLX gives you native Metal acceleration with no CUDA dependency, no cloud GPU rental, no Docker gymnastics. If you have a MacBook Pro, Mac Studio, or Mac Mini with enough unified memory, you already have the hardware for local inference.

The workflow:

Run discovery with Claude Opus 4.6 or GPT-5.4 (or really whatever model you prefer)

Export training data from the run database

Train a small local model via MLX on Apple Silicon (Soon to support CUDA)

Route future competitor runs through the local model when it's strong enough

Fall back to the frontier model when the local model is weak

This isn't theoretical. The full pipeline is implemented: export, training loop with git-based experiment state machine, MLX model with GQA attention and RoPE, safetensors checkpoints, and an MLXProvider that plugs into the same generation loop.

Training requires Apple Silicon (MLX uses Metal directly). There's also a file-based bridge that lets sandboxed agents trigger host-side training via launchd watchers. The agent writes a request JSON. The host picks it up, trains, writes back a result. No network exposure, no elevated permissions.

What's in the Box

CLI: autoctx run kicks off a scenario. autoctx serve starts the dashboard. autoctx mcp-serve exposes tools for agent integration. There are commands for replaying runs, exporting training data, benchmarking, and more.

Dashboard: real-time view of runs, generations, scores, and playbook evolution via WebSocket streaming

MCP server: plug autocontext into any MCP-compatible agent (Claude Code, Cursor, OpenClaw, etc.) and let it drive evaluation and improvement loops programmatically

Natural language task creation: describe what you want ("an agent that triages security incidents") and autocontext generates the spec, rubric, and runnable task

Multi-provider support: Anthropic, OpenAI-compatible APIs, Ollama, vLLM, and MLX local inference

Installable packages: pip install autoctx for the full Python control plane (CLI, dashboard, training, MCP server). npm install autoctx for the TypeScript evaluation and improvement loop with shared SQLite storage, embeddable in Node workflows

The agent-task pipeline is particularly useful: describe what you want in natural language ("I want an agent that writes incident postmortems"), and autocontext generates a spec, validates it, creates a runnable task with a multi-dimensional rubric, and starts the improvement loop.

Why Open Source, Why Now

autocontext started as internal tooling. Evaluation infrastructure was the bottleneck on every project. Every agent deployment eventually needed some version of "figure this out and make it better. give it your all. don't make any mistakes" in an endless human feedback loop until maybe the model figured out the probelm.

Karpathy's autoresearch work and the community energy around recursive self-improvement convinced me the timing was right. These ideas (knowledge accumulation, harness-driven optimization, frontier-to-local distillation) are converging fast. A lot of people are building pieces of this independently.

Keeping it closed when the community is working on the same problems felt like the wrong call. So here it is.

Standing on Shoulders of Giants

autocontext didn't emerge in a vacuum. Several projects and people directly shaped how we think about recursive improvement, agent evaluation, and knowledge accumulation (especially in the past week). In no particular order:

@karpathy : autoresearch planted the seed for the entire training/distillation pipeline. The idea that agents could drive their own research and learning loops is foundational to what autocontext became.

@a1zhang & @lateinteraction : The Refinement Loop Model (RLM) directly inspired our REPL-Loop Mode, where multi-turn LLM sessions replace single-shot analysis. The recursive self-improvement framing shaped the core architecture.

@snwy_me : Helios shaped our operator experience: the cockpit for long-running runs, monitor semantics, session notebooks, and escalation-based provider consultation. Safety-preserving UX for autonomous agents is hard, and Helios showed a path.

@GeoffreyHuntley : Ralph, and now Latent Patterns, pushed our thinking on how agents should surface and persist learned behavior.

@gepa_ai : GEPA influenced our approach to prompt and policy optimization, especially the use of actionable side information and Pareto-frontier search for candidate improvement.

@alxfazio : Plankton was an early reference point for thinking about lightweight agent architectures that punch above their weight.

@realmcore & @0xrandomlabs : Slate informed how we think about evaluation infrastructure and agent benchmarking.

@varun_mathur : Hyperspace AGI for frontier peer-to-peer work applying the autoresearcher pattern. Proving these ideas work in distributed settings validated the direction.

@cex1gt & @vvaiyr : SOMA directly influenced our later architecture for multi-stage improvements, which evolved into the core harness, distillation sidecar, and runtime routing.

@jianxliao : TinyAGI/fractals — a clean recursive agentic task orchestrator that informed how we think about task decomposition and agent coordination.

666ghj : MiroFish for novel approaches to agent refinement.

@_colemurray :  background-agents and his work with Open Inspect. Cole asked the right questions about the recursive improvement loop that made the implementation better.

@kais_rad  & @tunahorse21  — For reviewing early builds and being fearless testers. The kind of feedback that only comes from people actually trying to break things.

*Note for OpenClaw agents: autocontext exposes an MCP server (autoctx mcp-serve) and a CLI-first contract for agent integration. See autocontext/docs/agent-integration.md for setup instructions, JSON output contracts, and SDK options.

What's Next

This is the beginning, not the finish line. There's a lot more coming:

Deeper scenario families for domains like legal reasoning, scientific research, and multi-agent negotiation

Tighter integrations with agent frameworks, tools, and MCP ecosystems

More documentation on how to build custom scenarios for your specific domain

Performance and cost optimization tooling for production deployments

I'll be publishing follow-up articles and posts showing how I use autocontext day-to-day applied to problems that go well beyond software engineering. If that sounds interesting, follow me. This is going to get weirder and more useful from here.

Get Started

The repo: github.com/greyhaven-ai/autocontext

Contributions, issues, and feedback welcome. If you're building agents that need to get better over time, this is for you.

Follow me on X (@JayScambler) for updates, applied use cases, and the occasional unhinged take on where all of this is heading.