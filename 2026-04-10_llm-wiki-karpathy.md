# llm-wiki — Andrej Karpathy's Idea File for LLM-Maintained Knowledge Bases

**Source:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
**Date:** 2026-04-10
**Tags:** LLM, knowledge management, personal wiki, RAG alternative, AI agents

---

**What it is:** A shareable "idea file" (not code — intentionally) by Karpathy describing a pattern for building a personal wiki maintained by LLMs. The concept: instead of sharing an app, you share the *idea* and let your own agent build it for your setup.

**Core insight — wiki beats RAG:**

| RAG | LLM Wiki |
|-----|----------|
| Retrieves raw docs per query | Pre-synthesizes into structured markdown |
| No cross-references | Links already built |
| Repeated rediscovery | Knowledge compounds over time |

**Three-layer architecture:**

```
Raw Sources (immutable)
    ↓ ingest
The Wiki (LLM-maintained markdown pages, entities, cross-refs)
    ↓ configured by
Schema / CLAUDE.md (structure + workflow rules)
```

**Three operations:**
- `ingest` → process new docs, update existing pages
- `query` → search synthesized wiki with citations
- `lint` → health check (contradictions, orphaned pages, broken links)

**Why it works:** LLMs don't get bored or forget to update cross-references — they handle bookkeeping while you handle curation.

**The meta-idea:** In the LLM-agent era, sharing *ideas* (not code) makes more sense — your agent builds a version tailored to your exact stack and needs. This gist is a direct demonstration of that philosophy.

---

Relevant for your stack: this pattern maps cleanly onto **2ndBrain / roxabi-vault** — the vault already stores entries, and this could inform an "ingest → wiki page synthesis" layer on top of it.

**Sources:**
- [llm-wiki gist — karpathy](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [Karpathy's LLM Wiki: The Complete Guide](https://antigravity.codes/blog/karpathy-llm-wiki-idea-file)
- [Karpathy on X — original announcement](https://x.com/karpathy/status/2040470801506541998)
