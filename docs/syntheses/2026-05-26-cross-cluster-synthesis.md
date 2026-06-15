# Cross-Cluster Synthesis — 2-Month Intel Triage

**Window:** 2026-03-26 → 2026-05-26 (334 MDs in `~/.roxabi/intel/`)
**Method:** 3 parallel agents, 76 sources read, 3 WebFetches
**Targets:** Lyra · roxabi-plugins · roxabi-1page

> Reads from companion reports:
> - [`2026-05-26-cluster-1-harness.md`](./2026-05-26-cluster-1-harness.md)
> - [`2026-05-26-cluster-2-skills.md`](./2026-05-26-cluster-2-skills.md)
> - [`2026-05-26-cluster-3-memory.md`](./2026-05-26-cluster-3-memory.md)

---

## 1. Convergences fortes (≥2 clusters d'accord)

| Pattern | ① Harness | ② Skills | ③ Memory | Conséquence |
|---|---|---|---|---|
| **Filesystem > vector/cloud** | "Persistent memory = filesystem, not history" | — | ByteRover 92.8% / Letta 74% w/o vector DB | SQLite WAL + FTS5 = primitive correct |
| **Progressive disclosure** | L1-L5 compaction cheapest-first | L1/L2/L3 skill loading | `recall()` token-budgeted injection | `paths:` filters partout |
| **Failure→Rule ratchet** | addyosmani: rule = past failure | SkillOpt: bounded-edit ratchet | claude-mem: session→rules | Chain: trace → rule → SKILL.md |
| **Thin harness, fat workers** | jackdishman 5-layer event-driven | Garry Tan resolver pattern | Lyra MemoryManager déjà bon | lyra-hub ≤200 lignes |
| **Cache boundary first-class** | troyhua: static/dynamic split | `cache_stable: true` frontmatter | — | system prompt invariant |
| **Lyra NATS ≈ Slate threads** | — | realmcore_ alignment explicite | sole-writer ADR-075 préservé | Formaliser, ¬re-architecturer |
| **¬multi-agent par défaut** | "Maximize single agent first" | Coordinator-Specialist ADK 2.0 | — | Résister à la tentation |

## 2. Tensions arbitrées

| Tension | Position recommandée |
|---|---|
| Wiki Karpathy ↔ Mercury structured | **Dual layer**: SQLite (agent ops) + `wiki/` markdown optionnel (domain docs) |
| Graph vs vector vs files | **Files+SQLite** ; graph quand >10K docs (¬cas) |
| Skill Graph v1 vs v2 | **v2 atoms/molecules/compounds** (v1 wikilinks dégradent à depth>3) |
| Permissive vs restrictive harness | **Restrictive** + approval gates écriture |
| Single-agent vs multi-agent | **Single-agent first**, split seulement si >10 outils chevauchants OU domaines clairement séparés |
| ReAct vs plan-and-execute | **Task-dependent**: open-ended → ReAct ; structuré → plan+execute (3.6× plus rapide) |

## 3. Lecture stratégique par projet (1 phrase)

| Projet | Bilan |
|---|---|
| **Lyra** | Architecture **déjà 80% correcte** (NATS = atoms naturels, MemoryManager+vault = bon SQLite primitive, Quadlet = infra layer 4). Manque : compaction pipeline LLM, prompt-cache discipline, importance scoring memory, formaliser molecule layer. **¬refonte, optimisations chirurgicales.** |
| **roxabi-plugins** | Manque le **layer gouvernance** (resolver + trigger evals + check-resolvable). 65 skills → ~15% probablement injoignables. Action #1 absolue : `darwin-skill` sur top-20. |
| **roxabi-1page** | **Hors-scope** des 3 clusters. ¬forcer. Règle conditionnelle : si Worker CF + LLM call ajouté → jackdishman 5-layer dès J1. |

## 4. Build/Buy/Skip consolidé

### BUY / INSTALL maintenant

| Outil | Pour | Pourquoi |
|---|---|---|
| **darwin-skill** (alchaincyf, 1449★) | roxabi-plugins | 8-dim scoring + ratchet ; applicable direct sur 65 skills |
| **claude-mem** (48K★) | roxabi-plugins (CC sessions) | Session compression + SQLite injection ; complète MEMORY.md |
| **GEPA / hone** (DSPy, $2-10/run) | roxabi-plugins | Prérequis : trace logging structuré d'abord |

### EVALUATE / clone + bench

| Outil | Pour | Coût d'évaluation |
|---|---|---|
| **Honcho** (plastic-labs, AGPL) | Lyra | Self-host Postgres+FastAPI ; bench vs MemoryManager actuel |
| **Meta-Harness** (Stanford IRIS, arxiv 2603.28052) | roxabi-plugins | Read paper + ref impl ; after structured traces |

### EXTRACT pattern (¬installer wholesale)

| Outil | Pattern à extraire |
|---|---|
| **ECC** (affaan-m) | `instincts` (rules-from-failures) + memory optim hooks |
| **Garry Tan resolver** | `check-resolvable` + trigger evals |
| **YourMemory** (CC-BY-NC) | Ebbinghaus decay + scoring stack |
| **Tencent agent memory** (Apache 2.0) | -61% tokens compression + persona memory |
| **Mercury** | `soul.md` / `persona.md` pattern (déjà partiellement dans Lyra) |
| **GBrain** | Append-only markdown + pgvector (référence si scale >10K docs) |

### SKIP / MONITOR

| Outil | Raison |
|---|---|
| **Hivemind** (Deeplake) | Cloud + TS + coding-agent only |
| **GraphRAG-SDK** (FalkorDB) | Process supplémentaire + Ashwingop vulnérabilité géométrique |
| **Memvid** | Write-once video, ¬real-time updates |
| **OpenChronicle** | macOS-only |
| **OpenHarness** | Overlap Lyra ; NATS plus robuste |
| **addyosmani/agent-skills** (wholesale) | dev-core déjà mieux intégré ; sharpen descriptions à la place |
| **arscontexta Skill Graph v1** | Superseded par v2 atoms/molecules |
| **Agent Vault sidecar** | Quadlet `EnvironmentFile=` suffit aujourd'hui |
| **SkillOpt** (arxiv) | Pas d'outil released ; darwin-skill = proxy pratique |

## 5. Anti-patterns détectés dans Mickael's stack

| Anti-pattern | Source de détection | Où regarder |
|---|---|---|
| **System prompt rebuild à chaque call** | troyhua + rohit4verse (prompt-cache invalidation) | `src/lyra/llm/` — séparer static/dynamic |
| **NATS dispatch read+write mixés** | jackdishman (5-layer) | `packages/roxabi-nats/` — classifier handlers |
| **Skills sans `paths:` filter** | rohit4verse + Saboo | Audit `~/projects/roxabi-plugins/plugins/*/skills/*/SKILL.md` |
| **MEMORY.md écrasable par agent** | @ksimback dual-author | Ajouter `author: mickael` frontmatter |
| **Compose/wikilinks à depth>3** | Shivsakhuja v1→v2 | Si `composition-patterns` skill évoluait vers wikilinks dense |
| **¬resolver pour 65 skills** | Garry Tan audit (10/13 bypassed) | Manque `plugins/shared/references/resolver-rules.md` |
| **Domain knowledge crammé dans lyra-hub system prompt** | Garry Tan thin-router | Audit `src/lyra/hub/prompt.py` ou équivalent |

## 6. Insights non triviaux

1. **L'architecture Lyra hub-spoke est déjà l'implémentation pratique de Slate's thread model** (realmcore_ 2026-04-02). Pas besoin de re-architecturer ; juste formaliser : NATS subjects = scoped threads, QueueGroup = parallel atoms, return msg = compressed thread state.

2. **Le primitive correct (SQLite WAL + FTS5 + optional CPU embeddings) est déjà en production dans roxabi-vault**. Mickael est en avance sur 80% du marché qui débat encore vector vs graph.

3. **roxabi-plugins risk principal = silent drift via ¬resolver**. 65 skills sans table de routage = ~10 skills injoignables aujourd'hui (extrapolation Garry Tan audit). Coût d'un fix : 1 fichier markdown + 1 CI step.

4. **Le pattern "harness > model" implique que Mickael devrait investir dans `dev-core` plus que dans le choix de modèle**. LiteLLM proxy bien configuré + skills bien orchestrées > Opus brut.

5. **Cross-cluster contradiction notable** : ① recommande "delete scaffolding as models improve" (Anthropic), mais ② recommande "compound skills get fatter as ecosystem grows". Résolution : delete des règles AGENTS.md/SKILL.md sans provenance failure, conserve les compounds qui orchestrent.

## 7. Métriques cibles post-implémentation

| Métrique | État estimé | Cible 3 mois | Mesure via |
|---|---|---|---|
| Token cost moyen par turn Lyra | Inconnu (¬instrumenté) | -30% via compaction + cache boundary | Langfuse self-host |
| % skills roxabi-plugins joignables | ~85% (extrapolé) | 100% | `check-resolvable` weekly CI |
| Skill avg tokens | Inconnu (probablement 3-5K) | ~920 (SkillOpt median) | darwin-skill scoring |
| Memory recall accuracy Lyra | Inconnu | bench vs Honcho LoCoMo-style | Test set 50 interactions |
| Context cache hit rate LiteLLM | Inconnu | >70% sur turns consécutifs | Langfuse + LiteLLM headers |

## 8. Open questions (deferred WebFetches)

| Question | Source à fetch |
|---|---|
| ECC `instincts` syntaxe concrète | `https://github.com/affaan-m/ECC/blob/main/README.md` |
| Stanford Meta-Harness algo complet | `https://arxiv.org/abs/2603.28052` |
| Lyra NATS DLQ actuel | `~/projects/lyra/packages/roxabi-nats/` (read local) |
| Dive into CC paper | `https://arxiv.org/pdf/2604.14228` |
| `composition-patterns` skill état actuel | `~/projects/roxabi-plugins/plugins/*/skills/composition-patterns/SKILL.md` |
| `memory_upserts.py` schéma actuel | `~/projects/lyra/src/lyra/core/memory/memory_upserts.py` |
| roxabi-vault `hybrid_search` coverage | `~/projects/roxabi-vault/roxabi_vault/search.py` |

---

*Action plans détaillés : voir [`2026-05-26-action-plans.md`](./2026-05-26-action-plans.md).*
