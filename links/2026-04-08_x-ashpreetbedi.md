---
title: "Dash v2: The self-learning data team is almost ready."
source: "https://x.com/ashpreetbedi/status/2041653884536357122?s=46"
date: 2026-04-08
tags: ["AI Agents", "SQL", "Data Engineering", "Open Source", "Dash"]
platform: x
author: "@ashpreetbedi"
summary: "Dash v2 is an open-source, self-learning data agent that uses a multi-agent team and six layers of context to answer natural language queries while automatically learning from errors."
---
Dash v2: The self-learning data team is almost ready. 

Ask a question in plain english, get an answer grounded in 6 layers of context. Free and open source.

Every engineering team needs this. Use it in slack, MCP or build a custom UI.

Text-to-SQL agents fail because schemas lacks meaning, tribal knowledge is missing, and there's no way to learn from mistakes. Dash solves this with six layers of grounded context and a learning loop.

Here's how dash works:

1) Dash is a team of agents: a engineer and an analyst. 

2) Knowledge: Six layers of context feed every query.
- Table metadata (schema, columns, relationships).
- Human annotations (metrics, business rules).
- Validated query patterns (SQL that is known to work).
- Institutional knowledge (docs, wikis).
- Learnings (error patterns and discovered fixes).
- Runtime context (live schema inspection).

3) The learning loop: The agent learns from every error.
Runs a query, hits an error, diagnoses the fix, saves it.

4) Two knowledge systems working together: 
- Curated knowledge (validated queries, business rules) - Discovered learnings (error patterns, gotchas). 

The first is maintained by you. The second is maintained by the agent.

5) Dual schema system: A structural boundary between company data and agent-managed data. 

The public schema is company data, loaded externally, read-only for agents. The dash schema is owned by the Engineer. Views, summary tables, computed data. 

When the Engineer creates dash.monthly_mrr, it records the schema and example queries to the knowledge base. The Analyst discovers it on the next search and prefers it over raw table queries. 

6) Security: Auth uses RBAC with JWT verification. Every query is scoped to user_id. The Analyst's SQL connection has default_transaction_read_only=on. The Engineer can write, but only to the dash schema. 

An eval suite tests these boundaries directly: it prompts the agents to leak credentials, execute destructive SQL, and cross schema boundaries, then verifies they can't.

7) Interfaces: One agent definition, multiple surfaces. RestAPI, Slack threads, web UI, CLI. 

8) Infrastructure: Standard Python container. Docker Compose for local dev. One-command cloud deployment. Streaming via SSE. The infrastructure layer is boring on purpose. 95% of running an agent is identical to running any other service.

What I learned building this:
The agent is the easy part. The system around it is everything. When you store memory in a database instead of files, you get multi-tenancy for free. When you enforce permissions at the database level instead of the prompt, you get security that actually holds. When you give the agent a way to save what it learns, every query makes the next one better.

You can clone it, run docker compose up, and have the full system running in minutes. 

Github: https://github.com/agno-agi/dash

TLDR: Dash is a self-learning data agent. Three specialists (Leader, Analyst, Engineer), six layers of grounded context, a learning loop that compounds with every query. Security enforced at the database level, not the prompt. One agent definition serves REST, Slack, web UI, and CLI. The agent is the easy part. The system is the product.