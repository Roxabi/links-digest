# Cluster 2: Skill Graphs / Skill Composition
**Synthesis: How AI agent skills should be structured, composed, and evolved**
Sources: 334 intel MDs (2026-03-26 → 2026-05-26). Files read: 22. WebFetches: 2.

---

## 1. TL;DR — 5-bullet convergent thesis

- **Atoms win reliability; compounds win leverage.** The field converged on a 3-tier model (atoms → molecules → compounds) where determinism lives low and autonomy lives high. Skills deeper than ~3 dependency levels become unreliable (Shivsakhuja 2026-04-23).
- **Progressive disclosure is the universal tax-optimization.** L1 (~100 tok) always loaded; L2 body only on trigger; L3 references on demand. Correctly applied, 20+ skills cost the same context as 1 (Saboo 2026-04-28, addyosmani 2026-05-07).
- **Resolvers are the missing governance layer.** Without a routing table, skills invent their own filing logic → silent drift in 90 days. 15% of skills become unreachable within weeks without check-resolvable audits (Garry Tan 2026-04-15).
- **Skills are trainable parameters, not static prompts.** SkillOpt (arXiv 2605.23904): optimized SKILL.md files deliver +19-25pp accuracy gains at zero inference-time cost; bounded edits (4-8/step) + held-out validation gate = textual gradient descent (koylanai 2026-05-26, [fetched]).
- **Loops beat collections.** A skill that runs in a feedback loop (diff → rule extraction → skill update) compounds across time. A static template executes once and stagnates (voxyz_ai 2026-04-03).

---

## 2. Skill Design Principles — Distilled Rules

| # | Principle | Evidence (sources) |
|---|-----------|-------------------|
| P1 | **Single-purpose atoms** — one skill does one thing, ¬calls other skills | Shivsakhuja, Saboo, atomic-agents (3 sources) |
| P2 | **Description = search index** — most important 2 lines; router sees ONLY this | Saboo 2026-04-28, koylanai 2026-05-26 |
| P3 | **Progressive disclosure L1/L2/L3** — name+desc always; body on match; refs on demand | Saboo, arscontexta, addyosmani (3 sources) |
| P4 | **Compactness > length** — median optimal skill: ~920 tokens; length ≠ quality | SkillOpt [fetched], koylanai 2026-05-26 |
| P5 | **Skills-as-actions, not static prompts** — skill = contextual behavior triggered by situation | realmcore_ 2026-04-02, voxyz_ai 2026-04-03 |
| P6 | **Every constraint traces to a real failure** — no speculative guardrails | addyosmani 2026-05-10 (harness engineering) |
| P7 | **Thin harness, fat skills** — harness is just a router; knowledge lives in skills | Garry Tan 2026-05-09, addyosmani 2026-05-10 |
| P8 | **Register in resolver immediately** — unregistered skill = capability that doesn't exist | Garry Tan 2026-04-15 |
| P9 | **Bounded edits in self-improvement loops** — 4-8 edits/step; full rewrites collapse | SkillOpt [fetched], koylanai 2026-05-26 |
| P10 | **Protected slow-state invariant** — fast-state edits ¬allowed to overwrite slow-state lessons (removing this costs −22pp on SpreadsheetBench) | koylanai 2026-05-26 |

---

## 3. Composition Patterns — Comparison Table

| Pattern | Shape | Reliability | Autonomy | Sources |
|---------|-------|-------------|----------|---------|
| **Skill Graph v1** (arscontexta) | Wikilink graph, MOC index nodes, YAML frontmatter, recursive traversal | Medium — degrades at depth >3, circular deps | Agent decides navigation | arscontexta 2026-04-05 |
| **Skill Graph v2 / Atoms-Molecules-Compounds** (Shivsakhuja) | 3-tier: atoms (deterministic, no deps) → molecules (2-10 atoms, explicit chain) → compounds (orchestrators, agent drives) | High atoms, Medium molecules, Low compounds | Compounds delegate broad autonomy | Shivsakhuja 2026-04-23 |
| **Skills-as-Actions / Threads+Forks** (Slate/realmcore_) | Skills instantiate isolated threads with scoped context; orchestration skills chain other skills; forking = synchronous interactive skills | High per-thread | Thread = scoped episode, returns compressed state | realmcore_ 2026-04-02 |
| **Resolver + Fat Skills** (Garry Tan) | 200-line routing table → dispatches to skill; each skill consults resolver before writing; check-resolvable audits | High when resolver maintained | Skills fat, harness thin | Garry Tan 2026-04-15, 2026-05-09 |
| **Hybrid Graph (ADK 2.0)** | Directed graph, deterministic nodes + AI-driven nodes; Coordinator-Specialist prevents God agent | High: mandatory structure enforced by framework, ¬skippable | AI flexibility within node, ¬skip nodes | GoogleCloudTech 2026-04-23 |
| **Skill Loop / Feedback** (voxyz_ai) | cron → skill runs → diff against edits → rule extraction → skill update | Improves over time | Growing autonomy as loop iterates | voxyz_ai 2026-04-03 |

**Key insight**: v1 → v2 evolution = less open-ended graph traversal, more explicit choreography at low levels + intentional autonomy delegation at high levels only.

---

## 4. Skill Lifecycle — Write → Test → Optimize → Evolve

```
Write               Test                 Optimize            Evolve
────────────────    ──────────────────   ─────────────────   ──────────────────
SKILL.md folder     Trigger evals        Darwin-skill        Feedback loops
L1 description      (50 sample I/O)      8-dim scoring       diff → rules
L2 body             check-resolvable     ratchet: keep if    nightly review
L3 references       weekly audit         score↑, revert if↓  skill v1→v1.3+6mo
YAML frontmatter    cross-modal eval     SkillOpt: 4-8       slow/fast state split
~920 token target   per-skill effect     bounded edits       protected invariant
```

**Darwin-skill** (alchaincyf, 1449★):
- 8 dimensions (60pts structure + 40pts effectiveness, total 100)
- 5-phase cycle; human-in-loop between phases
- Ratchet: score only ascends; auto-revert regressions
- Each skill optimized in isolation (1 editable asset at a time)

**SkillOpt** (arXiv 2605.23904, koylanai):
- Formal: SKILL.md as trainable parameter; optimizer model proposes edits; validation gate (held-out set) accepts/rejects
- Results: +19.1pp (Claude Code), +24.8pp (Codex), +23.5pp (GPT-5.5 direct chat)
- Transfer: Codex-optimized skill → Claude Code hit +59.7pp on SpreadsheetBench
- Protected-section invariant: slow-state (persona, voice) ≠ editable by fast-state optimizer; removes it → −22pp

**Self-improving loop** (voxyz_ai):
- Trigger: cron → collect edits → aggregate 10-15 same-type diffs → classify → distill rule → write to SKILL.md
- Writing skill evolved v1.0→v1.3 in 6 months autonomously

---

## 5. roxabi-plugins Audit

**Inventory:**
- 18 plugin families, 65 skills total
- Families: dev-core (34), web-intel (8), gitnexus (6), logo-generator (3), content-lab (2), compress (1), composition-patterns (1), 1b1 (1), + 10 singletons
- External marketplaces: brand-voice, forge, marketing, design, product-management, etc. (Anthropic knowledge-work-plugins + roxabi-forge)

### 5.1 — Skills that should be split (→ atoms)

| Current skill | Issue | Split recommendation |
|---------------|-------|---------------------|
| `dev` | Compound orchestrator masquerading as entry point — already chains 14 sub-skills correctly, but the SKILL.md itself is 340+ lines. The description covers too much. | Keep as compound; extract `dev-pipeline-router` logic into a resolver reference file; description should be 2 lines max |
| `web-intel/analyze-url` | Bundles: fetch + extract + analyze + score — 4 distinct operations | atom: `url-fetch` + atom: `url-extract` + molecule: `url-analyze` |
| `web-intel/benchmark` | Competes with `analyze-url`; both do competitive analysis | Audit overlap; likely merge or differentiate clearly |
| `implement` | Spawns agents + writes code + wires worktrees — multi-concern | Keep as molecule; ensure atoms (`worktree-setup`, `agent-spawn`) are separate |
| `code-review` | Review + verdict + inline PR comments — 3 operations | Keep as molecule; consider exposing `review-findings` atom separately |

### 5.2 — Skills that should be molecules (sequenced atoms)

| Candidate | Currently | Make explicit |
|-----------|-----------|---------------|
| `dev` (Frame→Shape→Build→Verify→Ship) | Already implicit | Already molecule-of-compounds — correct |
| `pr` (branch detect + create + link) | Single skill | Explicit chain: `branch-detect → pr-create → issue-link` |
| `ci-watch → validate → review` | 3 separate skills invoked by dev | Formalize as `verify-pipeline` molecule (currently implicit via dev compound) |
| `logo-design + logo-explore-ai + logo-explore-svg` | 3 skills with implicit order | Make a `logo-pipeline` molecule |

### 5.3 — Skills that should be compounds (orchestrators)

| Candidate | Assessment |
|-----------|-----------|
| `dev` | Already correct compound — 14-step pipeline, human gates at Frame/Shape/Build |
| `init` | Should be compound: env-setup + stack-setup + github-setup + seed-docs chain |
| Missing: `content-creation-pipeline` | huashu-skills has this (topic-gen → research → write → review → publish); roxabi content-lab is 2 skills; should be a compound orchestrating voice-style + video-recipe + compress |

### 5.4 — Overlap audit with external repos

| roxabi-plugins skill | Overlaps with | Recommendation |
|---------------------|---------------|----------------|
| `dev/spec` | addyosmani/agent-skills `/spec` (44.7k★) | Check description differentiation; Roxabi's is SDLC-coupled, Addy's is standalone — keep, sharpen description |
| `dev/plan` | addyosmani `/plan` | Same — differentiation is the dev pipeline integration |
| `dev/code-review` | addyosmani `/review` | Roxabi adds inline PR comment posting; keep, note the delta |
| `web-intel` family | Warp oz-skills (SEO/accessibility audit) | ¬overlap — web-intel is analysis + synthesis; Warp is DevOps/audit |
| `content-lab` | huashu-skills (21 content skills) | huashu is CN-oriented (douyin, wechat, weibo); content-lab is EN voice/video. No conflict. |
| `compress` | ECC (193k★) memory optimization | ¬overlap — compress is content compression for humans; ECC is agent context management |
| `composition-patterns` | arscontexta skill graph, Shivsakhuja v2 | This is the meta-skill — should reference SkillOpt + darwin-skill patterns; update it |

### 5.5 — Skills missing a SOUL/personality layer

The Garry Tan "SOUL.md / Daydreams" pattern (garrytan 2026-05-09): skills should know *who* they're writing for (personal context graph, voice, judgment).

| Gap | Impact |
|-----|--------|
| No `voice-guide` slow-state file across dev-core skills | dev-core outputs are harness-neutral; no personality |
| `content-lab/voice-style` exists but isolated | Not referenced by other content skills |
| No cross-skill resolver in roxabi-plugins | 10/18 plugin families likely have hardcoded assumptions (per Garry Tan's audit finding: 10/13 skills bypassed resolver) |
| No `check-resolvable` equivalent | Unknown % of skills unreachable via current plugin manifest |

**Critical gap**: roxabi-plugins has no RESOLVER.md / routing table. The Claude Code plugin system uses `description` field as the implicit resolver, but:
- No trigger eval test suite
- No check-resolvable audit
- No filing rules doc for data outputs
- Estimated 15% skills potentially unreachable (extrapolating Garry Tan's audit)

**Recommendation**: Add `plugins/shared/references/resolver-rules.md` + weekly `check-resolvable` audit CI step.

---

## 6. Lyra Recommendations

Lyra = hub-spoke NATS-dispatched workers on M₁ (RTX 3080, 24/7), Python/uv, Telegram+Discord.

### Should Lyra have a skill system?

**Yes, but differently from CC skills.** NATS workers = natural atoms. The mapping:

| CC Skill concept | Lyra NATS equivalent |
|-----------------|---------------------|
| Atom | Individual NATS subject handler (e.g. `lyra.clip.transcribe`) |
| Molecule | Worker that subscribes to coordinating subject, chains 2-5 atom subjects |
| Compound | `lyra-hub` orchestrator — dispatches to molecule workers |
| Resolver | `lyra-hub` routing table in system prompt / NATS subject manifest |
| Progressive disclosure | Worker-local context; hub only sees subject + summary; full context stays in worker |
| Skill loop | NATS message with diff → hub distills rule → updates hub system prompt |

**Concrete recommendations:**

1. **Hub = thin router** — lyra-hub's system prompt should be a resolver (100-200 lines), dispatching to workers by intent pattern. ¬cram domain knowledge into hub.

2. **Workers = fat skills** — each NATS worker (clipool, stt, tts, gh-helper) is an atom. Document them with SKILL.md-style headers (name, description, triggers, outputs) in `lyra/docs/worker-manifest.md`.

3. **Add a `check-resolvable` equivalent** — test suite of 20-30 sample intents → expected NATS subject. Run weekly. Workers that exist but can't be reached by hub = dead weight.

4. **Molecule pattern for multi-step flows** — e.g., Telegram message → stt (atom) → llm inference (atom) → tts (atom) → voice reply (atom) should be orchestrated by a molecule worker, not hub. Hub dispatches to `lyra.voice-pipeline`, not to 4 separate atoms.

5. **Skill evolution via feedback** — after each interaction, NATS message to `lyra.feedback` subject; nightly consolidation → rule proposals → human review → hub system prompt update. Mirrors voxyz_ai's feedback loop.

**NATS as execution model aligns naturally with Slate's thread model** (realmcore_ 2026-04-02): NATS subjects = scoped thread contexts; compressed return messages = thread result payloads; QueueGroup = parallel atom execution. Lyra is already close to the Slate architecture — formalize it.

---

## 7. roxabi-1page Assessment

**Verdict: Not relevant. Skip.**

roxabi-1page = Stripe-gated single-page sites on Cloudflare Pages. Static HTML, no agent runtime, no skill dispatch, no NATS, no LLM inference in the hot path.

Skills/composition patterns apply when: agent decides between multiple actions, context management is a constraint, or skills evolve from feedback.

roxabi-1page has none of these. The only tangential relevance:
- Could use a `1page-template` skill in roxabi-plugins to scaffold new sites
- Could use web-intel skills to audit landing pages post-deploy

Both are build-time tooling concerns, not runtime architecture. File under "build tools can use skills, product doesn't need a skill system."

---

## 8. Build/Buy/Skip Matrix

| Tool | Stars | Description | Recommendation |
|------|-------|-------------|----------------|
| **darwin-skill** (alchaincyf) | 1449★ | 8-dim scoring + ratchet optimizer for SKILL.md | **BUY** (install) — directly applicable to 65 skills in roxabi-plugins. Run quarterly. |
| **SkillOpt** (arXiv 2605.23904) | paper | Formal text-gradient optimizer, +19-25pp gains | **WATCH** — no released tool yet; paper is very recent (2026-05). Implement darwin-skill first as practical proxy. |
| **addyosmani/agent-skills** | 44.7k★ | 7 SDLC slash commands, dev lifecycle | **SKIP** — dev-core already covers this with better integration (pipeline state, tiers, worktrees). Audit descriptions for differentiation. |
| **huashu-skills** | 794★ | 21 CN content creation skills | **SKIP** — EN market, different platform (douyin/wechat). Ideas worth borrowing: end-to-end pipeline compound pattern, 3-pass proofreading atom. |
| **Warp oz-skills** | — | DevOps: SEO, accessibility, Terraform | **SKIP** — no overlap with roxabi-plugins focus. |
| **ECC** (affaan-m) | 193k★ | Harness optimization: skills + instincts + memory + security | **REFERENCE** — too monolithic to adopt wholesale; borrow: instincts pattern (rules derived from failures), memory optimization hooks |
| **arscontexta** (Skill Graph v1) | — | 250-file wikilink knowledge graph | **SKIP FOR NOW** — v1 graph pattern is superseded by v2 atoms/molecules in reliability. Relevant only if roxabi-plugins adds deep knowledge domains (legal, trading). |
| **ADK 2.0 patterns** (Google) | — | 5 orchestration patterns, Coordinator-Specialist | **REFERENCE** — Hybrid Graph pattern worth adopting in Lyra hub design; Coordinator-Specialist already implicit in lyra-hub architecture. |
| **GBrain/GStack** (Garry Tan) | 87k+ | Brain OS + fat skills + resolver + check-resolvable | **REFERENCE** — resolver pattern + check-resolvable + trigger evals directly actionable for roxabi-plugins. Don't install GBrain (personal knowledge system); extract patterns only. |
| **atomic-agents** (BrainBlend) | 5.8k★ | Python framework, atomic/composable agents | **SKIP** — Python library for custom agent builds; roxabi-plugins is CC skills, different abstraction layer. |

---

## 9. Open Questions

These require additional investigation (WebFetch / further research):

| Question | Where to look |
|----------|--------------|
| Does randomlabs.ai/blog/skill-chaining have public content? | Fetched — page returned empty (likely JS-rendered or auth-gated). The Intel MD (realmcore_ 2026-04-02) contains the full blog post in `<details>` — already captured. |
| What is the SkillOpt "protected section" concrete syntax? | arXiv 2605.23904 full PDF — fetched abstract; need full paper for implementation details. |
| What does ECC's "instincts" pattern look like concretely? | github.com/affaan-m/ECC — README mentions it but details require deeper read |
| What does the Garry Tan check-resolvable meta-skill look like? | github.com/garrytan/gbrain — `check-resolvable` skill source |
| Does roxabi-plugins currently have any resolver/trigger eval system? | Read `.claude-plugin/marketplace.json` — check if descriptions act as implicit resolver triggers |
| What is roxabi-forge's skill taxonomy? | github.com/Roxabi/roxabi-forge — forge-* skills (forge-presentation, forge-epic, etc.); are they atoms or compounds? |

---

## Appendix: Source File Map

| Key insight | Source file |
|-------------|-------------|
| Skill Graph v1 (wikilinks, YAML, MOC) | `2026-04-05_x-arscontexta.md` |
| Atoms/Molecules/Compounds 3-tier | `2026-04-23_x-shivsakhuja.md` |
| Skills-as-actions, knowledge overhang, threads | `2026-04-02_x-realmcore_.md` |
| Folder anatomy, progressive disclosure L1/L2/L3 | `2026-04-28_x-saboo_shubham_.md` |
| Darwin-skill, 8-dim scoring, ratchet | `2026-04-20_darwin-skill.md` |
| SkillOpt, trainable params, bounded edits | `2026-05-26_x-koylanai.md` + [fetched arxiv] |
| Skill loops, feedback, nightly review | `2026-04-03_x-voxyz_ai.md` |
| Agent-skills SDLC slash commands | `2026-04-11_agent-skills.md`, `2026-05-07_agent-skills.md` |
| Karpathy 4 principles (Think/Simple/Surgical/Goal) | `2026-04-14_andrej-karpathy-skills.md` |
| ADK 2.0 orchestration patterns | `2026-04-23_x-googlecloudtech.md` |
| Resolver, routing table, check-resolvable | `2026-04-15_x-garrytan.md` |
| SOUL.md, fat skills, skillify, book-mirror | `2026-05-09_x-garrytan.md` |
| Harness engineering, ratchet, progressive disclosure | `2026-05-10_x-addyosmani.md` |
| Warp open-source skills | `2026-05-07_x-warpdotdev.md` |
| ECC: skills+instincts+memory+security | `2026-05-26_ecc.md` |
| huashu-skills, 21 content pipeline skills | `2026-04-26_huashu-skills.md` |
| Atomic agents Python framework | `2026-03-24_atomic-agents-tab-readme-ov-file.md` |
| Agent harness 12-component anatomy | `2026-04-14_x-akshay_pachaar.md` |
