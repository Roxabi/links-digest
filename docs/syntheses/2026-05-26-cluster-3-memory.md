# Cluster 3: Local-First Agent Memory — State of the Art

*Synthesized 2026-05-26 | Sources: 25 primary files + 1 WebFetch [fetched]*

---

## 1. TL;DR — Convergent Thesis

- **Hybrid wins**: pure semantic (vector/graph) fails mathematically at scale (Ashwingop no-escape theorem); pure keyword kills usefulness; the Pareto frontier sits at exact episodic storage + semantic reasoning layer on top.
- **Human-facing memory ≠ agent-facing memory**: Karpathy wiki (readability, reflection, batch) is wrong substrate for 24/7 autonomous agents (fast fact retrieval, structured updates, scoring, decay) — see Mercury/ctrl_alt_zaid distinction.
- **Filesystem + LLM reasoning beats pure vector**: ByteRover 92.8%, Letta 74.0% on LoCoMo with zero vector DB — LLM curation over structured files outperforms embedding retrieval today.
- **Your harness, your memory**: memory is not a plugin — it's inseparable from the harness. Closed/API-backed memory = platform lock-in (hwchase17). Own your store.
- **SQLite is the right local primitive**: WAL-mode SQLite covers 99% of single-machine local-first needs — FTS5 for keyword, optional hybrid embedding for semantic, no operational cost. Graph and Deeplake are overkill for Mickael's scale.

---

## 2. Taxonomy of Approaches

| Approach | Exemplars | Storage Backend | Primary Use Case |
|---|---|---|---|
| **Wiki/Markdown (compiled)** | Karpathy gist, claude-obsidian, llm-wikid, GBrain | Markdown files + optional pgvector | Personal KB, research, domain synthesis — human-readable, browsable |
| **Structured SQL** | Mercury (SQLite+FTS5), Multica (Postgres JSONB), Tencent agent memory | SQLite / Postgres | Agent operational memory — facts, preferences, task state, 24/7 agents |
| **Hybrid semantic** | YourMemory, Honcho | SQLite/Postgres + BM25 + vector + entity graph + decay | Conversational agent long-term recall, multi-session continuity |
| **Graph** | GraphRAG-SDK (FalkorDB), GraphRAG, LightRAG | Graph DB (FalkorDB/Neo4j) + embeddings | Multi-hop retrieval, enterprise knowledge traversal |
| **Relational (no vectors)** | Multica | Postgres + JSONB | Multi-agent task orchestration — explicit skill attachment, ¬fuzzy recall |
| **Cloud/Shared brain** | Hivemind (Deeplake), ByteRover (cloud sync option) | Deeplake / proprietary cloud | Cross-agent/cross-team skill propagation |
| **Session compression** | claude-mem, Tencent agent memory, ECC | SQLite + ChromaDB / custom | Claude Code session continuity, context window cost reduction |
| **Screen/AX capture** | OpenChronicle | Markdown + SQLite | Mac-only ambient context capture from running apps |
| **Video-encoded** | Memvid | MP4 (video codec) | Compressed static knowledge base, read-mostly, no writes |
| **Forgetting-curve decay** | YourMemory | SQLite + embeddings + entity graph | Long-term personal memory with biological plausibility |

---

## 3. Critiques Landscape

### Ashwingop "No-Escape Theorem" (2026-04-10_x-ashwingop.md)

**Claim**: any system retrieving by semantic similarity will degrade (forgetting + false recall) as memory grows. Effective semantic dimensionality = 10-50 for all models regardless of nominal dims.

**Evidence**: 5 architectures tested (vector DB, graph, context window, BM25/filesystem, parametric). All pure semantic → forgetting exponent b≈0.44. BM25: b=0.000, FA=0.000 — but semantic agreement only 15.5%.

**Verdict**: mathematically correct for pure semantic retrieval. The "escape" is Option 2: exact episodic record (filesystem/SQL) + semantic reasoning layer on top. Filesystem doesn't escape interference — it avoids it by not doing semantic retrieval directly.

**Implication**: ByteRover's context tree + LLM curation IS Option 2. Karpathy wiki is also Option 2. They work because the LLM does semantic work on exact stored text, not because embeddings escape interference.

### @chrysb "Long-term memory remains unsolved" (2026-04-12_x-chrysb.md)

**Claim**: raw storage = inert; derived summaries = drift (photocopy of photocopy). Evaluation paradox: can't validate without reviewing more context than fits in a window.

**Verdict**: correct for chat-conversation use case over months/years. Less fatal for domain-knowledge or fact-based memory (Mercury 10-type taxonomy, Honcho user modeling).

### @rohit4verse "Graph is the final boss" (2026-04-26_x-rohit4verse.md)

**Claim**: markdown stacking = context reloading not memory. Real memory = graph + embeddings + traversal.

**Counter**: Ashwingop proves graph + embeddings still inherits geometric vulnerability (b=0.478). GraphRAG-SDK wins benchmarks but needs FalkorDB process. For Mickael's scale: premature.

### Wiki crowd (@karpathy, @vibemarketer, @ksimback, claude-obsidian)

**Claim**: compiled wiki > RAG. Human curation + LLM maintenance = compounding KB.

**Where right**: personal knowledge management, batch research, human-readable synthesis. @ksimback's dual-author system (author: kevin = protected) is the key refinement — prevents AI averaging out your thinking.

**Where wrong**: not suitable as primary substrate for 24/7 autonomous agents (ctrl_alt_zaid: facts not pages, continuous writes, staleness management).

### Mercury / ctrl_alt_zaid "Human ≠ Agent memory"

**Most actionable split**:
- Human-facing → wiki/markdown (readability, compounding, browsable)
- Agent-facing → structured SQLite (facts, scoring, decay, selective injection, conflict resolution)

**Both together** = practical correct answer for Lyra.

---

## 4. Storage Backend Comparison

| Backend | Operational cost (M₁ RTX 3080, Ubuntu Server) | Syncthing-friendly | Best for |
|---|---|---|---|
| **Markdown + files** | Zero. Any editor. | Yes (text files) | Human wiki, claude-obsidian, GBrain |
| **SQLite (WAL)** | Zero. Included in Python stdlib. | Yes (single-file, copy-safe in WAL mode if paused, use `.db` + `-wal` + `-shm`) | Facts, sessions, preferences, FTS5 — Lyra's current store |
| **SQLite + FTS5** | Zero (FTS5 built into SQLite). | Yes | Full-text keyword search over memories |
| **SQLite + embeddings** | Low. `sentence-transformers` (CPU model, ~500MB RAM). Optional GPU. | Yes (embed at write, search at query) | Hybrid semantic recall — YourMemory pattern |
| **Postgres + pgvector** | Medium. Needs Postgres process, ~50-200MB baseline RAM. | No (requires pg for writes — export-only sync) | GBrain at 10K+ files scale, enterprise |
| **FalkorDB (GraphRAG-SDK)** | Medium-high. Redis-protocol graph DB process. | No | Multi-hop traversal, enterprise KB |
| **Deeplake (Hivemind)** | Cloud-dependent. Local mode possible but complex. | No | Cross-team skill propagation, cloud-first |
| **ChromaDB** | Low-medium. Embedded Python process or server. | Partially (embedded mode = single file) | Semantic search mid-scale |

**Verdict for M₁**: SQLite WAL + FTS5 + optional CPU embeddings covers everything up to ~100K memory entries. Zero infra overhead. Syncthing-safe (pause before sync or use WAL checkpoint). Postgres only if Mickael scales to GBrain-level (10K+ docs).

---

## 5. Lyra Memory Architecture Proposal

### Current state (confirmed by code inspection)

Lyra already has:
- `MemoryManager` wrapping `roxabi-vault` (`AsyncMemoryDB`) — **in production**
- SQLite FTS5 via `roxabi_vault.fts`
- Optional `Embedder` + `hybrid_search` (lazy-imported, optional dependency)
- Memory types: `session`, `concept:{technology,project,decision,fact,entity}`, `preference`
- `FRESHNESS_TTL_DAYS` decay thresholds per type
- `recall()` method: last 5 sessions + concept search + preferences → token-budgeted string injection
- `IdentityAliasStore` for cross-platform user identity (Telegram ↔ Discord same user)
- Per-user `PrefsStore` in `config.db`
- `TurnStore` in `turns.db`, `MessageIndex` in `message_index.db`
- Thread continuity: `ThreadStore` for Discord threads, `TurnStore.get_last_session()` for Telegram

### Gaps

| Need | Gap | Solution |
|---|---|---|
| Per-user cross-session facts (goals, projects, relationships) | Only session summaries + concept entries; no structured fact store with scoring | Add `fact` entries in vault with confidence + freshness metadata via existing `memory_upserts.py` |
| Cross-agent shared knowledge | MemoryManager is per-agent namespace; no shared namespace | Add `shared:` namespace prefix + `recall()` param to query shared pool |
| Knowledge wiki / domain pages | No wiki layer; all memory is conversational | Optional: add `~/.roxabi/lyra/wiki/` Karpathy-style for domain knowledge (agent concepts, project docs) |
| Memory decay enforcement | `FRESHNESS_TTL_DAYS` defined but no background consolidation job | Nightly cron: `lyra maintenance --prune-stale` — purge entries past TTL or flag as stale |
| Token-aware injection scoring | `recall()` injects top-5 sessions flat; no recency/confidence scoring | Add `importance_score` + `recency_weight` to vault entries; sort before injection |

### Recommended data layout in `~/.roxabi/lyra/`

```
~/.roxabi/lyra/
├── auth.db              # grants, identity (existing)
├── config.db            # agents, prefs (existing)
├── turns.db             # turn history (existing)
├── discord.db           # discord thread sessions (existing)
├── message_index.db     # message index (existing)
├── memory.db            # roxabi-vault: sessions, concepts, facts, preferences (existing + extend)
└── wiki/                # NEW: optional domain wiki (Karpathy pattern, agent-writable)
    ├── SCHEMA.md        # wiki schema (agent instruction)
    ├── index.md         # wiki index
    ├── log.md           # ingest log
    ├── concepts/        # domain concepts
    └── entities/        # users, projects, tools
```

### Integration with NATS + hub-spoke

```
Inbound msg → SessionBuilder → Dispatcher → Agent
                                              ↓
                                    MemoryManager.recall(user_id, namespace)
                                    → inject [MEMORY] + [PREFERENCES] into system prompt
                                              ↓
                                    Agent reply
                                              ↓
                                    MemoryManager.upsert_session_summary()
                                    + upsert_concepts() (async, post-turn)
```

Post-turn memory write: publish NATS subject `lyra.memory.flush.<pool_id>` → `turn_writer` or dedicated memory-writer consumes → writes to `memory.db` (preserves sole-writer pattern per ADR-075).

### Per-user threads (Telegram/Discord)

Already handled: `TurnStore.get_last_session(pool_id)` for Telegram; `ThreadStore` for Discord threads. The `RoutingKey(platform, bot_id, scope_id).to_pool_id()` scopes by user+bot.

### Cross-agent shared knowledge

Add `shared:{namespace}` memory namespace: all agents read, designated agents write. Inject via second `recall()` call with token budget slice.

### Cross-session continuity

Already functional via `MemoryManager.recall()` → `[MEMORY]` block injection. Extend: add decay + scoring to surface most-relevant vs most-recent.

### Syncthing-friendliness

WAL mode SQLite: safe to Syncthing-sync when Lyra is not running, or use checkpoint+snapshot pattern. For live sync: `PRAGMA wal_checkpoint(TRUNCATE)` before sync trigger, or exclude `-wal`/`-shm` files and accept eventual consistency.

---

## 6. roxabi-plugins Memory

**Current state**: file-based `MEMORY.md` at `~/.claude/projects/.../memory/MEMORY.md` — auto-memory via harness. ECC pattern (2026-05-26_ecc.md) adds hooks + continuous learning on top.

**Should it become a skill graph + wiki?** Partially yes:

- `dev-core:cleanup-context` already compresses context — analogous to claude-mem's session compression
- `MEMORY.md` covers persistent cross-session facts about Mickael's preferences, project patterns, bugs fixed — this is the "agent-authored" layer
- **Recommended addition**: `roxabi-vault:vault-add` skill writes structured facts (`concept:decision`, `preference`) to vault — the MCP server is already deployed
- **Dual-author pattern** (@ksimback): protect human-written entries from agent overwrite via `author: mickael` frontmatter in MEMORY.md
- **Wiki**: claude-obsidian or llm-wikid pattern applicable for roxabi-plugins domain docs (skill specs, ADRs, patterns) — low priority

**Bottom line**: MEMORY.md is adequate for cross-session harness memory. The vault MCP already enables structured writes. No need to migrate to Obsidian unless the wiki grows past ~50 entries.

---

## 7. roxabi-1page

**Relevant?** Essentially no.

roxabi-1page = Stripe-gated static sites on Cloudflare Pages. No agent loop, no persistent users, no conversation history. Memory requirements: zero. The only adjacent concern would be if a future version adds a personalized experience per subscriber — then a serverless KV (Cloudflare KV or D1) would be the right tool, not any of the agent memory systems here.

**Verdict**: Skip all memory tooling for roxabi-1page.

---

## 8. Build / Buy / Skip Matrix

| Tool | Decision | Reason |
|---|---|---|
| **Honcho** (plastic-labs) | **Evaluate / Buy** | Best API for per-user stateful memory across Telegram/Discord; Python SDK; self-hostable (AGPL); maps directly to Lyra's user-agent-session structure |
| **Mercury** (cosmicstack-labs) | **Reference / Skip** | Good soul-file pattern + SQLite+FTS5 design is canonical; already implemented in Lyra's MemoryManager; TypeScript ≠ Lyra stack |
| **Hivemind** (activeloopai) | **Skip** | Cloud-backed Deeplake; TypeScript; Claude Code + coding agents only; ¬Lyra use case |
| **ByteRover** | **Reference / Skip** | Context tree + LLM curation pattern is canonical reference; Elastic 2.0 license; TypeScript; coding-agent oriented; token savings would apply via Lyra's own MemoryManager |
| **claude-mem** | **Adopt for roxabi-plugins** | SQLite + session compression + context injection directly for Claude Code; 48K stars = battle-tested; addresses CC session amnesia; plug in alongside MEMORY.md |
| **OpenChronicle** | **Skip** | macOS only, alpha; AX-tree capture has no Lyra equivalent; server-side Ubuntu context capture not applicable |
| **GBrain** | **Reference** | Append-only markdown + Postgres pgvector = good reference if memory.db grows to 10K+ entries; MIT; TypeScript |
| **llm-wikid** | **Adopt pattern / Skip tool** | Karpathy wiki pattern directly applicable for roxabi-plugins domain wiki; the tool itself is just a CLAUDE.md schema — implement directly |
| **claude-obsidian** | **Adopt pattern / Skip tool** | DragonScale memory + hot cache pattern applicable; 5K stars; Obsidian dependency is the friction point (no Obsidian on M₁ server) |
| **YourMemory** | **Evaluate** | Ebbinghaus decay + BM25 + vector + entity graph = most complete recall stack; 59% LoCoMo Recall@5 (2× Zep); Python; CC-BY-NC license (non-commercial only — check) |
| **Tencent TencentDB-Agent-Memory** | **Reference** | -61% tokens via mid-session compression + mermaid task maps + persona memory — three distinct techniques worth cherry-picking; Apache 2.0; C++ core |
| **GraphRAG-SDK** (FalkorDB) | **Skip** | Benchmark leader but needs FalkorDB process; overkill for personal agent; reintroduces geometric vulnerability (Ashwingop) |
| **Memvid** | **Skip** | Video-encoded text = clever hack, write-once read-many; zero support for real-time agent memory updates; curiosity only |

---

## 9. Open Questions

| Question | Source needed |
|---|---|
| Honcho self-host operational cost: does FastAPI + Postgres fit alongside M₁'s existing workload? | `gh repo clone plastic-labs/honcho` + inspect `docker-compose.yml` or equivalent |
| YourMemory license (CC-BY-NC 4.0): is commercial use blocked? Does Lyra qualify as commercial? | Read `LICENSE` in sachitrafa/YourMemory repo |
| roxabi-vault `hybrid_search` coverage: does it already implement BM25 + vector enough to match YourMemory's stack? | Read `~/projects/roxabi-vault/roxabi_vault/search.py` |
| Tencent agent memory: is the open-source repo `TencentDB/TencentDB-Agent-Memory` Python-embeddable or C++ only? | `gh repo view Tencent/TencentDB-Agent-Memory` |
| Mercury `soul.md` / `persona.md` pattern: compatible with Lyra's `src/lyra/core/persona.py`? | Read `~/projects/lyra/src/lyra/core/persona.py` |
| `memory_upserts.py`: does it already support `importance_score` + `confidence` fields? | Read `~/projects/lyra/src/lyra/core/memory/memory_upserts.py` |

---

*Files read: 25 | WebFetches: 1 (mercury-agent GitHub) | Clones: 0*
