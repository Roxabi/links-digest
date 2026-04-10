---
title: "I turned my brain into a searchable wiki with Claude Code"
source: "https://x.com/vibemarketer_/status/2042226854271099342"
date: 2026-04-09
tags: ['knowledge management', 'second brain', 'Claude Code', 'LLM', 'personal wiki']
platform: x
author: null
---

# I turned my brain into a searchable wiki with Claude Code

**Source:** https://x.com/vibemarketer_/status/2042226854271099342
**Date:** 2026-04-09

---

**The core idea:** Use Claude Code to auto-ingest raw sources (articles, PDFs, meeting notes) into a structured, interlinked markdown wiki — no manual tagging or organizing required.

**Folder structure:**
```
raw/       ← drop sources here
wiki/      ← Claude Code outputs organized pages
index.md   ← maps everything
log.md     ← tracks updates
claude.md  ← project instructions for Claude
```

**Why it beats a search engine or RAG:**
- Context dies when you close an LLM session — this makes knowledge *persist*
- Uses **structured links** between concepts, not similarity search → deeper, more connected answers
- Compounds over time: by article 20, you have a dense relationship web surfing insights you'd miss manually

**Quick setup:**
1. Create a folder / Obsidian vault
2. Open in terminal + fire up Claude Code
3. Paste [Karpathy's gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) and ask Claude to implement it as a second brain
4. Drop a source into `raw/` → say *"ingest this"*

**Honest tradeoff:** Works well up to ~hundreds of pages. Millions of docs → still need a proper RAG pipeline with embeddings. For personal research or small teams, the token cost is essentially the only cost.

**Key insight worth noting:** Karpathy himself expected to need fancy RAG at ~100 articles / 500k words — well-maintained markdown indexes just worked instead.