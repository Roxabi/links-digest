# Dash v2 — Self-learning Text-to-SQL Agent (X post)

**Source:** https://x.com/ashpreetbedi/status/2041653884536357122
**Date:** 2026-04-08
**Author:** @ashpreetbedi

---

**What it is**
- Text-to-SQL agent team (Leader + Analyst + Engineer) that learns from its own errors
- Free, open source → [`github.com/agno-agi/dash`](https://github.com/agno-agi/dash)
- Interfaces: REST API, Slack, web UI, CLI

### Why Text-to-SQL Usually Fails → How Dash Fixes It

| Problem | Dash solution |
|---|---|
| Schema lacks meaning | 6 layers of grounded context |
| Tribal knowledge missing | Human annotations + institutional docs |
| No learning from mistakes | Learning loop — errors → diagnosed fixes → saved |

### 6 Context Layers (fed to every query)
1. Table metadata — schema, columns, relationships
2. Human annotations — metrics, business rules
3. Validated query patterns — SQL known to work
4. Institutional knowledge — docs, wikis
5. **Learnings** — error patterns + discovered fixes
6. Runtime context — live schema inspection

### Key Insight
> The agent is the easy part. The system around it is everything.
