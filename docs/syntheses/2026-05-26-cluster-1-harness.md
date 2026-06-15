# Cluster 1 — Harness > Model: Synthesis Report
> Sources: 77 harness-tagged + 14 priority files, 2026-03-26 → 2026-05-26
> Written: 2026-05-26

---

## 1. TL;DR (5 bullets)

- **Harness = product; model = commodity.** LangChain: +13.7pp on TerminalBench 2.0 by changing harness only, same model. (2026-04-05_x-nyk_builderz.md, 2026-03-30_x-0xmaxou.md, 2026-04-14_x-akshay_pachaar.md)
- **4-layer reality**: model weights → context → harness → **infrastructure** (RBAC, state persistence, distributed coordination). Most teams stop at layer 3 and build demos, not products. (2026-04-10_x-rohit4verse.md)
- **Context is the scarce resource**: giant instruction files, too many tools, and 1M-token windows are the main production failure modes. Cheapest-first compaction hierarchy is non-negotiable. (2026-04-01_x-troyhua.md, 2026-04-29_x-pawelhuryn.md)
- **Harness doesn't shrink — it shifts.** As models improve, outdated scaffolding is removed but new scaffolding is required for newly unlocked tasks. Current failure modes = configuration problems, not model ceiling. (2026-05-10_x-addyosmani.md)
- **Meta-harness is the next frontier**: automated search over harness configuration (tool ordering, context policies, stop heuristics) produces measurable gains without retraining. Stanford IRIS arXiv 2603.28052. (2026-04-23_meta-harness.md, 2026-04-08_x-howdymerry.md)

---

## 2. Convergence Map

| Principle | Sources | Strength |
|---|---|---|
| Harness quality > model quality for production outcomes | nyk_builderz, 0xmaxou, rohit4verse, akshay_pachaar, addyosmani, vtrivedy10, alphabatcher | ●●●●● |
| Layered cheapest-first compaction (microcompact → snip → summarize → collapse) | troyhua (7-layer), rohit4verse (4 strategies), akshay_pachaar (12-component), addyosmani | ●●●●● |
| Persistent memory = filesystem, not conversation history | nyk_builderz, vtrivedy10, addyosmani, akshay_pachaar | ●●●●○ |
| Tool minimalism beats bloat (Vercel cut 80%, CC 95% context reduction via lazy load) | nyk_builderz, akshay_pachaar (x2), rohit4verse | ●●●●○ |
| Prompt-cache preservation as first-class design constraint | troyhua, rohit4verse, pawelhuryn | ●●●●○ |
| Specialized agents with scoped tools > generalist with all tools | nyk_builderz, jackdishman (rules-first), akshay_pachaar, rohit4verse | ●●●●○ |
| Error recovery as first-class loop state, not outer try/catch | rohit4verse (823-line retry), alphabatcher, akshay_pachaar | ●●●○○ |
| Hooks as enforcement layer (pre/post tool, session start/stop) | addyosmani, vtrivedy10, rohit4verse | ●●●○○ |
| Async generator loop (streaming + cancellation + backpressure) | rohit4verse, alphabatcher | ●●●○○ |
| Circuit breakers on every autonomous subsystem | troyhua (7 distinct breakers), rohit4verse | ●●●○○ |
| Infrastructure = 4th layer: RBAC, isolation, distributed coord | rohit4verse, alphabatcher | ●●○○○ |
| Meta-harness: outer search loop over inner runtime policies | meta-harness (Stanford), howdymerry, link-7e66b643 | ●●○○○ |

---

## 3. Divergences / Tensions

| Tension | Camp A | Camp B | Resolution |
|---|---|---|---|
| **Harness thickness** | Anthropic: thin harness, model absorbs complexity over time; delete scaffolding as models improve | LangGraph/CrewAI: explicit control graph, thick orchestration | Task-dependent: thin for general coding, thick for multi-agent prod pipelines |
| **ReAct vs plan-and-execute** | ReAct: adapts per-step, handles unknowns | Plan+execute: 3.6x faster on bounded tasks (LLMCompiler) | Split by task type: open-ended = ReAct, structured = plan+execute |
| **Single agent vs multi-agent** | Anthropic + OpenAI: maximize single agent first, split only when >10 overlapping tools or clearly separate domains | LangChain/CrewAI: multi-agent as default pattern | Both sources agree: multi-agent adds overhead; split is justified, not default |
| **Permissive vs restrictive harness** | Ship fast, open permissions | Gate dangerous ops, approval loop | 0xmaxou + akshay_pachaar: restrictive wins in prod; permissive = "haven't had the incident yet" |
| **Review agents (same-model)** | Most sources: review agent as quality gate | 0xmaxou: two models trained together share blind spots, second validates first's errors | Divergent models only; same-model review agents have limited value |

---

## 4. Reference Architecture — Canonical Harness

```
Layer 4 — INFRASTRUCTURE
  RBAC / permission cascade (enterprise → project → user → session)
  State persistence (filesystem + git commits as checkpoints)
  Resource isolation (worktrees, sandboxes, abort propagation)
  Distributed coordination (file-lock, heartbeat, deduplication)

Layer 3 — HARNESS
  ┌─────────────────────────────────────────────────────┐
  │ Orchestration loop (async generator, 5-phase)        │
  │  Phase 1: Setup — tool budget, compaction check      │
  │  Phase 2: Model invocation (streaming, retry SM)     │
  │  Phase 3: Error recovery (loop-internal, not outer)  │
  │  Phase 4: Tool execution (read-only parallel / write │
  │           serial; streaming executor pre-fires)       │
  │  Phase 5: Continuation decision                      │
  ├─────────────────────────────────────────────────────┤
  │ Context management (cheapest first)                  │
  │   L1: Tool result storage → disk (2KB preview)       │
  │   L2: Microcompaction (cache_edits API, zero cost)   │
  │   L3: Session memory compaction (no API call)        │
  │   L4: Full compaction (1 forked API call)            │
  │   L5: Context collapse (feature-flagged)             │
  ├─────────────────────────────────────────────────────┤
  │ Memory architecture                                  │
  │   Short-term: conversation history (bounded)         │
  │   Session: session-memory/<id>.md (incremental)      │
  │   Long-term: MEMORY.md index + topic files           │
  │   Cross-session: Dreaming (background consolidation) │
  ├─────────────────────────────────────────────────────┤
  │ Tool system                                          │
  │   Progressive disclosure (skills w/ path filters)   │
  │   Concurrency classification (read‖ / write→serial) │
  │   Streaming executor (pre-fires during generation)   │
  │   Result budgeting (maxResultSizeChars)              │
  ├─────────────────────────────────────────────────────┤
  │ Error recovery state machine (per error class)       │
  │   429 → retry/cooldown/fast-mode-off                 │
  │   529 × 3 → model fallback                          │
  │   400/context-overflow → compact+retry              │
  │   Network → no-keepalive + new connection            │
  ├─────────────────────────────────────────────────────┤
  │ Permission system (7-stage cascade)                  │
  │   Hooks: PreToolUse / PostToolUse / SessionStart     │
  │   Restrictive default; approval gates for write ops  │
  ├─────────────────────────────────────────────────────┤
  │ Observability: cost/token/cache-hit dashboard        │
  └─────────────────────────────────────────────────────┘

Layer 2 — CONTEXT
  System prompt: static above cache boundary / volatile below
  Instructions: table-of-contents → structured docs/ dir
  Dynamic injection: user message / <system-reminder> tags
  Context budget per layer; alert if any layer > 40%

Layer 1 — MODEL WEIGHTS (commodity)
  Route by capability × cost (Haiku/Sonnet/Opus per task)
  Lock model at session start (cache invalidation risk)
```

**Key design invariants** (across all sources):
- Every line in AGENTS.md must trace to a specific historical failure
- Circuit breaker on every autonomous subsystem
- Verification loop closes feedback: lint/test/type-check → inject error → self-correct
- `Agent = desired_behavior ÷ harness_design` (backward design)

---

## 5. Lyra-Specific Recommendations

Lyra current state: hub-spoke, asyncio, NATS transport, multi-model via LiteLLM, Telegram+Discord adapters.

| Action | Why | Effort |
|---|---|---|
| **Add cheapest-first compaction to LLM streaming pipeline** | No evidence of compaction in `src/lyra/llm/`. Long conversations hit context limit → hard failure. Implement: tool-result offload (2KB preview) → session notes file → summarize-on-demand. (2026-04-01_x-troyhua.md) | M |
| **Classify NATS message handlers by read/write concurrency** | jackdishman (2026-04-02): ingestion must validate+enqueue only, never execute business logic inline. Current NATS dispatch may mix read/write ops. Classify handlers → read-only fan-out, write-ops serial queue with DLQ. | M |
| **Add session memory file per agent (not just conversation history)** | Lyra stores agent context in SQLite + TOML. No incremental "what changed this session" file. Add `~/.lyra/agents/<slug>/session-memory.md` updated on token growth threshold. Enables cheap compaction without API call. (2026-04-01_x-troyhua.md L3) | S |
| **Implement per-message model routing (rules-first, LLM second)** | jackdishman + 0xmaxou: classify first, escalate only when necessary. Lyra currently routes to LiteLLM proxy without intent classification. Add deterministic rule chain before LLM call: spam/rate-limit → block, known commands → handler, ambiguous → Haiku classify → Sonnet/Opus if complex. | M |
| **Add prompt cache boundary to LiteLLM system prompts** | rohit4verse + troyhua: static content above dynamic boundary. Lock model+tools at session start. Lyra rebuilds system prompt on every call (per ARCHITECTURE.md review). Extract static portions above `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` marker. | S |
| **Infrastructure: add per-adapter NATS queue with DLQ monitoring** | Clanker (2026-04-02): separate queues per platform, DLQ alerts = earliest signal of degraded external dep. Lyra has NATS but unclear DLQ on Telegram/Discord adapter failures. Add dead-letter queue + cron inspect. | M |
| **Secrets: use credential proxy pattern for bot tokens** | 2026-04-23_x-dangtony98.md (Agent Vault): agents shouldn't hold secrets directly — proxy at HTTPS layer. Lyra Quadlet injects bot tokens via `EnvironmentFile=`. Consider secrets proxy sidecar when lyra-hub runs external tool calls. | L |

---

## 6. roxabi-plugins Recommendations

Current state: dev-core plugin family (`/dev`, `/plan`, `/spec`, `/code-review`, `/clarify`, `/cleanup-context`). Multi-domain code review with Conventional Comments already in place.

| Action | Why | Effort |
|---|---|---|
| **Add harness-failure ratchet to dev-core skills** | addyosmani (2026-05-10): every agent failure → permanent rule in AGENTS.md. dev-core `/dev` skill should append to a `failure-catalog.md` on task completion: what went wrong, what rule was added. Skills then load this at start. Converts each failure into cumulative harness improvement. | S |
| **Progressive disclosure in skill loading** | rohit4verse + vtrivedy10: skills with `paths:` filter already exist in CC. Audit all dev-core skills for path-scoped activation. Skills without path filters load for every task = context waste. Add `paths:` frontmatter to at least `/code-review`, `/validate`, `/cleanup-context`. | S |
| **Split `/code-review` into planner + executor subagents** | akshay_pachaar (2026-04-14): planner-executor split prevents positive bias when model grades its own work. Current `/code-review` is single-agent. Add optional `agent: true` + separate evaluator subagent that runs blind (no fix context). (2026-04-01_x-troyhua.md: forked agent pattern) | M |
| **Add `/harness-audit` skill** | addyosmani + nyk_builderz: periodic review to remove stale rules (if no failure prevented in 30 days, remove). Skill checks CLAUDE.md, AGENTS.md, all skill files for: lines without failure provenance, rules redundant with current model capability, skills not triggered in 30+ days. | S |
| **Cache boundary in skill system prompts** | pawelhuryn (2026-04-29): lock tools at session start; adding MCP/skills mid-session invalidates cache. Skill frontmatter could declare `cache_stable: true` to signal the skill should not be loaded after session start. Tooling enforcement via pre-load hook. | S |
| **Instrument skill failure traces for meta-harness** | NousResearch hermes-agent-self-evolution (2026-04-12): GEPA reads execution traces to discover failure modes. Add structured trace output to dev-core skills (task → trace → outcome → tokens). Feed to evolutionary optimizer later. Low cost now, high value when applying meta-harness pattern. | M |
| **Adopt Organism-Oriented framing in skill documentation** | brivaelfr (2026-04-12): LLM=brain, tools=organs, harness=nervous system. Reframe plugin README — each skill is an organ with a single precise function. Document what failure each skill prevents, not what it does. | S |

---

## 7. roxabi-1page Assessment

**Honest verdict: Cluster 1 is marginally relevant.**

roxabi-1page = Stripe-gated one-page sites on Cloudflare Pages (PoC, no Quadlet, no agent).

| Applicability | Signal |
|---|---|
| No agent loop | Harness theory is irrelevant to static Cloudflare Pages delivery |
| No LLM at runtime | Context management, compaction, memory = not applicable |
| Stripe webhook handler = deterministic | jackdishman principle (rules-first, LLM-second) applies: **don't add LLM** to what rules can handle |
| Secrets security | Agent Vault pattern applies *if* 1page ever gains a server-side agent (e.g., Cloudflare Worker calling an LLM for personalization). Not yet. |
| Build-time codegen | If Claude Code is used to build/maintain 1page (likely), then harness best practices apply to Mickael's dev workflow, not to the running app |

**Actionable from this cluster (1 item only):**
- When adding any server-side LLM call to 1page (personalization, dynamic copy, etc.): follow jackdishman 5-layer event-driven architecture from day 1. Don't bolt it on. `action → effort: M when the time comes`.

---

## 8. Build / Buy / Skip Matrix

| Tool | Decision | Reason |
|---|---|---|
| **ECC** (affaan-m/ECC, 193K stars) | **Buy/Integrate (selectively)** | Harness-native operator system, Anthropic Hackathon Winner. Extract the hooks + memory optimization patterns into roxabi-plugins. Don't wholesale adopt — evaluate overlap with dev-core. (2026-05-26_ecc.md) |
| **Meta-Harness** (Stanford IRIS, arXiv 2603.28052) | **Build-later** | Framework for automated harness optimization via evolutionary search. Claude Code as default proposer agent. High value for roxabi-plugins skill evolution. Prerequisite: add structured failure traces first. (2026-04-23_meta-harness.md) |
| **hermes-agent-self-evolution** (NousResearch, ICLR 2026 Oral) | **Integrate-phase-2** | DSPy + GEPA to auto-optimize skill files. $2-10/run, no GPU. Directly applicable to dev-core skills once trace logging is in place. (2026-04-12_hermes-agent-self-evolution.md) |
| **OpenHarness** (HKUDS, 9.4K stars) | **Monitor** | Python agent infra with ohmo (Telegram/Discord/Slack). Overlaps Lyra. Good to watch but Lyra's NATS architecture is more robust for hub-spoke. (2026-04-14_openharness.md) |
| **Agent Vault** (Infisical OSS) | **Skip now / Revisit L** | Credential proxy pattern is architecturally correct. Lyra currently uses Quadlet `EnvironmentFile=` which is adequate. Revisit when lyra gains external tool calls that touch user credentials. (2026-04-23_x-dangtony98.md) |
| **Hivemind** (@deeplake/hivemind) | **Skip** | Cloud-backed shared brain across team agents. Solo dev context makes cross-agent skill propagation low-value. (2026-05-12_hivemind.md) |
| **wedow/harness** (bash, 133 stars) | **Skip** | Educational; too minimal for production. Useful as reference for understanding pure state-follower pattern. (2026-03-26_harness.md) |
| **iii** (Rust, 16K stars, ELv2) | **Monitor** | Worker/Function/Trigger backend runtime. Interesting for future Lyra infrastructure if NATS becomes insufficient. ELv2 license is non-free for SaaS. (2026-05-25_iii.md) |
| **GEPA / hone** (DSPy prompt evolution) | **Integrate-now (low cost)** | 14-word seed → 85% holdout on bug-fix. Pattern: trace failures → evolve prompts. Apply to roxabi-plugins dev-core skills. ~$2-10/run. (2026-04-20_link-7e66b643.md) |
| **awesome-harness-engineering** (ai-boost, 1049 stars) | **Bookmark** | Curated reference list. Good for ongoing discovery, not action item. (2026-04-24_awesome-harness-engineering.md) |

---

## 9. Open Questions (need WebFetch to resolve)

| Question | Source to Fetch |
|---|---|
| What exactly does ECC's `instincts` system do vs skills? How to extract patterns without full adoption? | `https://ecc.tools` + `https://github.com/affaan-m/ECC/blob/main/README.md` full |
| Stanford Meta-Harness paper full algorithm — specifically the search space definition and eval criteria | `https://arxiv.org/abs/2603.28052` |
| Does Lyra's NATS transport already implement DLQ / dead-letter queues? | `~/projects/lyra/packages/roxabi-nats/` (local read, not WebFetch) |
| arXiv 2604.14228 (Dive into Claude Code paper) — architecture diagrams and harness component list | `https://arxiv.org/pdf/2604.14228` |
| Flue framework (Fred Schott) referenced by addyosmani as harness framework — feature set vs Lyra needs | `https://github.com/FredKSchott/flue` (if exists) |
| iii engine ELv2 license: exact restrictions for internal/private use (SaaS vs internal tooling) | `https://github.com/iii-hq/iii/blob/main/engine/LICENSE` |

---

## Source Index

Priority files read:
`2026-04-01_x-troyhua.md` · `2026-04-10_x-rohit4verse.md` · `2026-04-05_x-nyk_builderz.md` · `2026-03-30_x-0xmaxou.md` · `2026-04-08_x-howdymerry.md` · `2026-04-23_meta-harness.md` · `2026-04-24_awesome-harness-engineering.md` · `2026-04-26_x-burkov.md` · `2026-04-02_x-jackdishman.md` · `2026-05-10_x-addyosmani.md` · `2026-04-11_x-alphabatcher.md` · `2026-04-12_x-brivaelfr.md` · `2026-04-12_hermes-agent-self-evolution.md` · `2026-04-14_x-akshay_pachaar.md` · `2026-04-14_openharness.md` · `2026-04-24_x-akshay_pachaar.md` · `2026-04-29_x-pawelhuryn.md` · `2026-05-26_ecc.md` · `2026-03-26_harness.md` · `2026-03-10_x-vtrivedy10.md` · `2026-04-20_link-7e66b643.md` · `2026-05-12_hivemind.md` · `2026-05-25_iii.md` · `2026-04-23_x-dangtony98.md`

Total: 24 source files read. 0 WebFetches performed.
