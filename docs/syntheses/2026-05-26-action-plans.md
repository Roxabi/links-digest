# Action Plans — 2026-05-26

> **Source:** [Cross-cluster synthesis](./2026-05-26-cross-cluster-synthesis.md) of 76 intel sources (① Harness, ② Skills, ③ Memory).
> **Scope:** Lyra · roxabi-plugins · roxabi-1page.
> **Format per item:** `goal → why → how → acceptance → effort → deps → ref`.

---

## Executive summary

| Projet | Item le plus impactant | Effort | ROI |
|---|---|---|---|
| **Lyra** | L1 — Prompt-cache boundary + per-msg routing rules-first | S+M | 🔥 -30% tokens estimé |
| **roxabi-plugins** | P1 — `resolver-rules.md` + `check-resolvable` CI | S | 🔥 100% skill reachability |
| **roxabi-1page** | Skip — sauf futur Worker CF + LLM | — | — |

**Séquencement global** : faire **P1 + L1** d'abord (parallèles, sans dépendance). Ensuite P2 (darwin-skill) débloque trace logging, qui débloque GEPA (L4/P5).

---

# 🤖 LYRA — Plan d'action

## NOW (S/M, sans dépendance, ROI immédiat)

### L1. Prompt-cache boundary dans system prompt LiteLLM
- **Why** : `troyhua` + `rohit4verse` — Lyra rebuild probable du system prompt à chaque call → cache cassé → tokens × 5-10 sur turns consécutifs.
- **How** :
  ```
  1. Lire src/lyra/llm/*.py (chercher SYSTEM_PROMPT construction)
  2. Identifier sections statiques (persona, soul, agent identity, tools list)
                       vs dynamiques (memory recall, user prefs, current turn ctx)
  3. Insérer marker explicite: # === STATIC ABOVE / DYNAMIC BELOW ===
  4. Pour LiteLLM proxy : cache_control: {type: "ephemeral"} sur le bloc statique
  5. Lock model at session start (¬switch mid-conversation)
  ```
- **Acceptance** : cache hit rate >70% sur 2-3 turns consécutifs (mesurable via LiteLLM headers `x-anthropic-cache-read`)
- **Effort** : **S** (1-2h)
- **Deps** : none
- **Ref** : `2026-04-01_x-troyhua.md`, `2026-04-10_x-rohit4verse.md`, `2026-04-29_x-pawelhuryn.md`

### L2. Per-message routing rules-first → classifier → escalate
- **Why** : `jackdishman` Clanker pattern. Aujourd'hui Lyra route tout vers LiteLLM proxy sans pre-filter → coût uniforme, latence uniforme. Avec rules-first : 60-80% messages traités sans LLM ou avec Haiku.
- **How** :
  ```
  src/lyra/dispatch/ ou nouveau src/lyra/router/
  ┌─ Layer 1: deterministic
  │   ├─ rate limit / spam ─→ drop
  │   ├─ known slash command ─→ direct handler
  │   └─ regex/keyword route ─→ specialized worker
  ├─ Layer 2: cheap classifier
  │   └─ Haiku intent classification (cached prompt, ~50 tokens)
  ├─ Layer 3: full LLM
  │   └─ Sonnet par défaut, Opus si flag explicite
  └─ Layer 4: post-hoc routing
      └─ confidence < threshold ─→ retry with bigger model
  ```
- **Acceptance** : sur 100 messages test, ≥50% n'atteignent jamais layer 3
- **Effort** : **M** (1 jour)
- **Deps** : L1 (pour préserver cache de Haiku classifier)
- **Ref** : `2026-04-02_x-jackdishman.md`, `2026-03-30_x-0xmaxou.md`

### L3. Audit lyra-hub system prompt (Garry Tan thin-router pattern)
- **Why** : Garry Tan — hub doit être ≤200 lignes de routing, ¬cram domain knowledge. Mickael's hub probable >500 lignes (à vérifier).
- **How** :
  ```
  1. wc -l sur src/lyra/hub/prompt.py (ou équivalent)
  2. Catégoriser le contenu actuel :
     [ROUTING] intent → worker subject       → garder
     [DOMAIN] connaissance verticale         → déplacer vers worker
     [VOICE] persona/soul                    → garder (slow-state)
     [TOOLS] liste outils                    → static, cache-able
  3. Cibles :
     - hub prompt = routing + voice + tools static = ≤200 lignes
     - chaque worker = domain knowledge spécifique
  ```
- **Acceptance** : `wc -l src/lyra/hub/prompt.py` ≤200 ; domain knowledge migré dans workers correspondants
- **Effort** : **M** (½ jour)
- **Deps** : none
- **Ref** : `2026-04-15_x-garrytan.md`, `2026-05-09_x-garrytan.md`

### L4. Étendre `memory_upserts.py` avec `importance_score` + `confidence`
- **Why** : `recall()` actuel injecte top-5 sessions flat. Pas de tri par importance/récence/confiance → mauvais signal-to-noise dans le contexte.
- **How** :
  ```python
  # vault entries :
  metadata: {
    importance_score: float [0..1],   # défini par agent ou via skill rule
    confidence: float [0..1],         # défini par source/extraction quality
    recency_weight: float,            # computed: exp(-age_days/half_life)
  }

  # recall() :
  final_score = α·semantic + β·importance + γ·confidence + δ·recency_weight
  # sort, then budget-trim
  ```
- **Acceptance** : 50 interactions test → 95% des injections sont jugées "pertinentes" lors d'un audit manuel ou via LLM-as-judge
- **Effort** : **S** (2-3h)
- **Deps** : `roxabi-vault` schéma migration (additive, low risk)
- **Ref** : `2026-04-27_yourmemory.md` (Ebbinghaus pattern), `2026-04-25_mercury-agent.md` (scoring)

## NEXT (M, après NOW)

### L5. Cheapest-first compaction pipeline (4-layer)
- **Why** : troyhua 7-layer arch — sans compaction, longue conversation = hard fail à context limit OU coût exponentiel.
- **How** :
  ```
  L1 ─ Tool result offload   : result >2KB → write to file, inject 2KB preview + path
  L2 ─ Microcompact          : every N turns, summarize oldest 5 turns into 1 (no LLM call si possible)
  L3 ─ Session memory file   : ~/.roxabi/lyra/agents/<slug>/session/<session_id>.md (incremental)
  L4 ─ Full compact          : 1 forked LLM call, full conversation → summary
  ```
- **Acceptance** : conversation 50+ turns reste sous 80% du context window
- **Effort** : **M** (1-2 jours)
- **Deps** : L1 (cache boundary doit exister avant compaction)
- **Ref** : `2026-04-01_x-troyhua.md` (sections L1-L5)

### L6. `worker-manifest.md` (workers comme atoms documentés)
- **Why** : Garry Tan SKILL.md-style — workers Lyra (`clipool`, `stt`, `tts`, `gh-helper`, `gh-pod`) sont des atoms naturels mais ¬documentés en frontmatter SKILL.
- **How** :
  ```yaml
  # ~/projects/lyra/docs/worker-manifest.md
  workers:
    - name: lyra.clip.transcribe
      role: atom
      input: {audio_url: str, lang: optional[str]}
      output: {text: str, segments: list[Segment]}
      triggers: ["voice message received", "transcribe audio"]
      deps: [voiceCLI-stt service]
      effort_estimate: ~3s/min
  ```
- **Acceptance** : tous workers actifs documentés ; `check-resolvable` test = 100%
- **Effort** : **S** (½ jour)
- **Deps** : L3 (savoir ce qui est routé)

### L7. Molecule worker `lyra.voice-pipeline`
- **Why** : Aujourd'hui Telegram-voice = 4 dispatches séparés (recv → stt → llm → tts → reply). Latence cumulée + hub orchestration. Pattern molecule (Shivsakhuja v2) = 1 dispatch hub → molecule orchestre les 4 atoms localement.
- **How** :
  ```
  hub dispatches: lyra.voice-pipeline {audio_url, user_id, session}
  worker lyra.voice-pipeline subscribes:
    1. await NATS req-rep: lyra.clip.transcribe
    2. await NATS req-rep: lyra.agent.reply  (LLM)
    3. await NATS req-rep: lyra.tts.synthesize
    4. publish: lyra.adapter.send {audio, user_id}
  ```
- **Acceptance** : hub system prompt size diminue (¬voir 4 patterns voix séparés) ; latence stable ou -10%
- **Effort** : **M** (1 jour)
- **Deps** : L6 (manifest pour orchestration)
- **Ref** : `2026-04-23_x-shivsakhuja.md` (molecules), `2026-04-02_x-realmcore_.md` (threads)

### L8. Shared namespace `shared:{namespace}` dans MemoryManager
- **Why** : Aujourd'hui chaque agent a son namespace isolé. Knowledge cross-agent (e.g. "Mickael utilise FR principalement") = dupliquée par agent.
- **How** :
  ```python
  # vault entries gagnent un namespace : "shared:user-profile", "shared:project-context"
  # MemoryManager.recall(agent_ns, also_query=["shared:user-profile"])
  # Write protégé : seul un agent désigné ("identity-curator") peut écrire shared:user-profile
  ```
- **Acceptance** : 1 agent écrit `shared:user-profile.lang=fr` → tous les agents le voient au recall suivant
- **Effort** : **S** (3-4h)
- **Deps** : L4 (extension memory_upserts)

### L9. NATS DLQ + monitoring sur Telegram/Discord adapters
- **Why** : Clanker pattern — DLQ = earliest signal de dépendance externe dégradée. Lyra a NATS mais DLQ status inconnu sur adapter failures.
- **How** :
  ```
  1. Audit packages/roxabi-nats/ : DLQ configuré ?
  2. Si non : add per-subject DLQ subscription
  3. Quadlet drop-in : lyra-dlq-monitor.service
     → cron 5min : check messages in DLQ, alert > N
  ```
- **Acceptance** : message échec adapter Telegram → arrive en DLQ → alert Discord/log
- **Effort** : **M** (½ jour)
- **Deps** : none
- **Ref** : `2026-04-02_x-jackdishman.md`

### L10. Nightly maintenance cron (`lyra maintenance --prune-stale`)
- **Why** : `FRESHNESS_TTL_DAYS` défini mais aucun job de purge → tables enflent.
- **How** :
  ```bash
  # nouveau CLI : lyra maintenance --prune-stale [--dry-run]
  # Quadlet timer : ~/.config/systemd/user/lyra-maintenance.timer
  # OnCalendar: daily 03:00
  ```
- **Acceptance** : `memory.db` size stable sur 30 jours d'usage normal
- **Effort** : **S** (2h)
- **Deps** : none

## LATER (L, ROI conditionnel)

### L11. Meta-harness / GEPA pour skill evolution (après trace logging)
- **Why** : Stanford Meta-Harness + NousResearch GEPA → optimisation auto des skills/prompts via recherche évolutionnaire, sans GPU.
- **Prereq absolu** : structured trace output (task → trace → outcome → tokens) doit exister d'abord.
- **Effort** : **L** (3-5 jours research + impl)
- **Ref** : `2026-04-23_meta-harness.md`, `2026-04-12_hermes-agent-self-evolution.md`

### L12. `check-resolvable` test suite Lyra
- **Why** : 20-30 sample intents → expected NATS subject. Workers non-atteignables = dead weight.
- **Effort** : **M** (1 jour)
- **Deps** : L6 (worker-manifest)

### L13. Honcho self-host eval
- **Why** : si MemoryManager+vault montre limites sur per-user statefulness multi-canal.
- **Trigger** : >100 utilisateurs actifs avec memory miss observable.
- **Effort** : **M** (1-2 jours bench)

### L14. Agent Vault credential proxy sidecar
- **Why** : si Lyra gagne des external tool calls qui touchent user credentials.
- **Trigger** : ajout d'un tool comme "post on user's Twitter" ou "read user's email".
- **Effort** : **L**

---

# 🔌 ROXABI-PLUGINS — Plan d'action

## NOW (S, ROI immédiat)

### P1. `resolver-rules.md` + `check-resolvable` CI step
- **Why** : Garry Tan audit → 10/13 skills bypassed son resolver. Extrapolation pour 65 skills Mickael : ~10 injoignables. Pur markdown, 0 code.
- **How** :
  ```
  1. Créer plugins/shared/references/resolver-rules.md :
     # Resolver rules — routing intent → skill
     - "create PR" / "open PR" / "submit PR" → dev-core:pr
     - "test this" / "add coverage" / "e2e tests" → dev-core:test
     - ... [toutes les routes]
  2. Créer plugins/shared/tests/trigger-evals.yaml :
     - intent: "I need to file a bug"
       expected_skill: dev-core:issue-triage
     - ... [30 samples min]
  3. Script check-resolvable.py : pour chaque intent, simule trigger → skill match
  4. CI step : github actions weekly, ouvre issue si <100% match
  ```
- **Acceptance** : 100% des intents test résolvent vers la skill attendue
- **Effort** : **S** (½ jour)
- **Deps** : none
- **Ref** : `2026-04-15_x-garrytan.md`

### P2. Audit `paths:` frontmatter sur skills critiques
- **Why** : rohit4verse — skills sans `paths:` chargées pour chaque task = context waste + cache invalidation.
- **How** :
  ```bash
  # 1. Inventaire :
  grep -L '^paths:' plugins/*/skills/*/SKILL.md
  # 2. Priorité : skills lourdes ou domain-specific
  # 3. Add paths: frontmatter :
  #    paths: ["**/*.py", "**/*.ts"]  # exemple
  ```
- **Acceptance** : skills `/code-review`, `/validate`, `/cleanup-context`, `/test`, `/seed-docs` ont toutes `paths:` filter
- **Effort** : **S** (1-2h)
- **Deps** : none
- **Ref** : `2026-04-10_x-rohit4verse.md`, `2026-04-28_x-saboo_shubham_.md`

### P3. `/harness-audit` skill (purge AGENTS.md sans provenance failure)
- **Why** : addyosmani — chaque règle = past failure. Règles >30j sans usage = bruit.
- **How** :
  ```markdown
  # plugins/dev-core/skills/harness-audit/SKILL.md
  Trigger: "harness audit" | "audit rules" | "prune AGENTS.md"
  Process:
    1. Scan CLAUDE.md + AGENTS.md + tous SKILL.md
    2. Pour chaque règle : grep git log / memory pour "applied at" trace
    3. Si pas d'évidence d'usage en 30j : flag for human review
    4. Output: pruning proposal markdown
  ```
- **Acceptance** : `/harness-audit` génère liste candidates à prune avec justification
- **Effort** : **S** (3-4h)
- **Deps** : none
- **Ref** : `2026-05-10_x-addyosmani.md`

### P4. Dual-author MEMORY.md (`author: mickael` frontmatter)
- **Why** : ksimback — protéger entrées humaines de l'écrasement agent (slow-state invariant).
- **How** :
  ```yaml
  # convention dans memory files :
  ---
  name: feedback_no_bidouillage
  type: feedback
  author: mickael       # ← NEW : agent ¬autorisé à modifier
  ---
  # OU :
  author: claude        # agent peut updater
  ```
  + update skill `cleanup-context` pour respecter `author: mickael`
- **Acceptance** : `cleanup-context` ne propose plus jamais de modifier entrée `author: mickael`
- **Effort** : **S** (1h)
- **Deps** : none
- **Ref** : `2026-05-06_x-ksimback.md` (dans cluster ③)

## NEXT (M, après NOW)

### P5. Installer darwin-skill + run sur top-20 skills
- **Why** : SkillOpt median optimal = ~920 tokens. Skills Mickael probablement 3-5× ça → context waste cumulatif.
- **How** :
  ```bash
  cd ~/projects/roxabi-plugins
  npx skills add alchaincyf/darwin-skill
  # Priorité d'optim (skills les + utilisées) :
  #   dev-core: dev, code-review, implement, plan, spec, fix, clarify
  #   web-intel: analyze-url, scrape, summarize, adapt
  #   marketing: content-creation
  #   brand-voice: enforce-voice
  # Run quarterly via cron / GH action
  ```
- **Acceptance** : top-20 skills passent darwin scoring (≥80/100)
- **Effort** : **M** (1-2 jours pour le run initial, ½ jour récurrent)
- **Deps** : none
- **Ref** : `2026-04-20_darwin-skill.md`

### P6. `failure-catalog.md` auto-append depuis `/dev`
- **Why** : addyosmani ratchet — chaque task failure → règle permanente. Aujourd'hui dev-core dev runs sans capitalisation.
- **How** :
  ```
  # Hook PostToolUse ou skill terminale dans /dev :
  Si task failed OR human override OR multiple retry :
    1. LLM extrait : root cause, rule pour éviter
    2. Append plugins/dev-core/references/failure-catalog.md :
       ## YYYY-MM-DD HH:MM <skill> <root-cause-tag>
       Context: ...
       Failure: ...
       Rule: ...
    3. Si rule récurrente (2+ occurrences) → promote vers CLAUDE.md / SKILL.md / AGENTS.md
  ```
- **Acceptance** : après 2 semaines d'usage, failure-catalog.md a 5-10 entrées
- **Effort** : **S** (3-4h)
- **Deps** : none
- **Ref** : `2026-05-10_x-addyosmani.md`

### P7. Split `web-intel:analyze-url` en atoms
- **Why** : Bundle de 4 ops (fetch+extract+analyze+score) → ¬réutilisable, ¬testable par concern, context lourd.
- **How** :
  ```
  ATOMS (nouvelles) :
    web-intel:url-fetch       (HTTP only, return raw)
    web-intel:url-extract     (parse content, return structured)
  MOLECULE (existante, refactor) :
    web-intel:analyze-url     = fetch → extract → analyze → score
  ```
- **Acceptance** : `analyze-url` SKILL.md ≤150 lignes ; atoms réutilisables par d'autres skills
- **Effort** : **M** (½ jour)
- **Deps** : none
- **Ref** : `2026-04-23_x-shivsakhuja.md`

### P8. Restructure `composition-patterns` = SSoT pour skill design
- **Why** : ce skill est aujourd'hui meta sans devenir LA référence du repo.
- **How** :
  ```markdown
  # plugins/shared/skills/composition-patterns/SKILL.md
  Sections :
    - Atoms / Molecules / Compounds (Shivsakhuja v2)
    - Progressive disclosure L1/L2/L3 (Saboo)
    - Resolver pattern (Garry Tan)
    - Failure ratchet (addyosmani)
    - SkillOpt protected-section invariant (slow vs fast state)
    - Liens vers darwin-skill scoring rubric
  Become THE reference skill, lue avant d'écrire/refactor toute autre skill.
  ```
- **Acceptance** : autres skills référencent composition-patterns en frontmatter `references:`
- **Effort** : **S** (3-4h)
- **Deps** : after darwin-skill scoring of existing skills (informe le contenu)

### P9. Wire `roxabi-vault:vault-add` depuis dev-core skills
- **Why** : structured facts (decisions, preferences, project context) méritent vault DB + FTS5, pas seulement MEMORY.md flat.
- **How** :
  ```
  Skills cibles : /adr (decisions), /clarify (intent), /spec (requirements)
  À la fin de chaque skill : MCP call vault-add avec category appropriée
  Cross-link : MEMORY.md gagne [[vault:id]] references
  ```
- **Acceptance** : dev-core skills écrivent dans vault, retrievable via FTS5
- **Effort** : **S** (3-4h par skill)
- **Deps** : roxabi-vault MCP server actif (déjà ✅)
- **Ref** : `2026-04-13_honcho.md` (structured facts pattern)

## LATER (L, ROI conditionnel)

### P10. Cache boundary discipline dans skills
- **Why** : pawelhuryn — adding MCP/skills mid-session invalide cache. Skills peuvent déclarer `cache_stable: true`.
- **Effort** : **M** (audit + frontmatter sweep)
- **Trigger** : si Langfuse montre cache hit rate <50%
- **Ref** : `2026-04-29_x-pawelhuryn.md`

### P11. Split `/code-review` en planner + executor subagents
- **Why** : akshay_pachaar — same-model review biaisé.
- **Effort** : **M**
- **Trigger** : si feedback humain "code-review trop indulgent"
- **Ref** : `2026-04-14_x-akshay_pachaar.md`

### P12. GEPA optimization sur skills (après traces structurées)
- **Why** : $2-10/run, no GPU, ICLR 2026 Oral.
- **Prereq** : P6 (failure-catalog) + trace logging structuré
- **Effort** : **L** (recherche + impl)
- **Ref** : `2026-04-12_hermes-agent-self-evolution.md`

### P13. Adopt SkillOpt pattern (quand outil released)
- **Trigger** : release publique d'un tool basé sur arxiv 2605.23904
- **Effort** : **M-L** au moment du release

### P14. Audit overlap descriptions vs addyosmani/agent-skills
- **Why** : 7-cmd lifecycle proche de dev-core. Risque de bruit pour utilisateurs externes.
- **Effort** : **S** (1-2h)
- **Trigger** : si plugin marketplace lancé

---

# 💳 ROXABI-1PAGE — Plan

## Verdict : SKIP (3 clusters d'accord)

Aucun agent runtime, aucun LLM hot-path, aucune persistance utilisateur.

## Règles conditionnelles (si futur)

| Condition | Action | Ref |
|---|---|---|
| Ajout d'un Cloudflare Worker + appel LLM (perso, dyn copy) | Architecture jackdishman 5-layer **dès J1** | `2026-04-02_x-jackdishman.md` |
| Personnalisation par subscriber | Cloudflare KV ou D1, ¬aucun memory tool du cluster ③ | — |
| Anti-abuse / spam detection | rules-first → classifier → LLM (jackdishman) | `2026-04-02_x-jackdishman.md` |

## Build-time tooling (orthogonal au runtime)

- `roxabi-plugins` peut inclure une skill `1page-scaffold` (build-time codegen)
- `web-intel:audit` peut tourner post-deploy sur les landing pages

→ Ces skills appartiennent à roxabi-plugins, pas au runtime 1page.

---

# 🗓 Séquencement recommandé

```
Semaine 1 (parallèle, sans dépendance)
├─ Lyra      : L1 (cache boundary)   + L4 (importance scoring)
├─ Plugins   : P1 (resolver)         + P2 (paths filter)
└─ Plugins   : P4 (dual-author)      + P3 (/harness-audit)
                                      Tous = S, total ≤2 jours

Semaine 2
├─ Lyra      : L2 (rules-first routing)
├─ Lyra      : L3 (lyra-hub audit)
└─ Plugins   : P5 (darwin-skill run sur top-20)

Semaine 3
├─ Lyra      : L5 (compaction pipeline)
├─ Lyra      : L6 (worker-manifest) + L7 (voice-pipeline molecule)
└─ Plugins   : P6 (failure-catalog) + P7 (atom split web-intel)

Semaine 4
├─ Lyra      : L8 (shared namespace) + L9 (DLQ) + L10 (nightly cron)
├─ Plugins   : P8 (composition-patterns SSoT) + P9 (vault wiring)
└─ Audit & metrics (Langfuse hookup ?)

Mois 2+
└─ LATER items : meta-harness, GEPA, Honcho eval (gated par mesures)
```

## Mesures avant/après (3 mois)

| Métrique | Mesure | Cible |
|---|---|---|
| Lyra avg tokens/turn | LiteLLM stats | -30% |
| Lyra cache hit rate | x-anthropic-cache-read | >70% |
| roxabi-plugins skills joignables | `check-resolvable` | 100% |
| roxabi-plugins skill avg tokens | darwin-skill score | ~920 median |
| failure-catalog.md entries | wc -l | 10+ après 30j |

---

*Synthèse cross-cluster détaillée : voir [`2026-05-26-cross-cluster-synthesis.md`](./2026-05-26-cross-cluster-synthesis.md).*
