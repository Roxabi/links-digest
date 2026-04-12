---
title: "giak/mnemo-lite"
source: "https://github.com/giak/mnemo-lite"
date: 2025-04-24
tags: ["PostgreSQL native memory", "local semantic search", "AI agent memory", "standalone cognitive system"]
platform: github
author: "giak"
summary: "MnemoLite is a PostgreSQL-native cognitive memory system providing local embeddings and high-performance search for AI agents."
---
# giak/mnemo-lite

**URL:** https://github.com/giak/mnemo-lite
**Description:** mémoire cognitive locale, standalone avec API.
**Language:** Python
**Stars:** 0 | **Forks:** 0
**Last updated:** 2026-04-04

## README (excerpt)

<p align="center">
  <img src="static/img/logo_mnemolite.jpg" alt="MnemoLite Logo" width="200" style="border-radius: 50%;">
</p>

# MnemoLite: PostgreSQL-Native Cognitive Memory

[![Version](https://img.shields.io/badge/version-1.3.0-blue.svg?style=flat-square)](https://github.com/giak/MnemoLite)
[![Build Status](https://img.shields.io/github/actions/workflow/status/giak/MnemoLite/ci.yml?branch=main&style=flat-square)](https://github.com/giak/MnemoLite/actions) 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg?style=flat-square)](https://www.python.org/downloads/)
[![PostgreSQL Version](https://img.shields.io/badge/postgres-17-blue.svg?style=flat-square)](https://www.postgresql.org/)
[![pgvector](https://img.shields.io/badge/pgvector-0.5.1-brightgreen.svg?style=flat-square)](https://github.com/pgvector/pgvector)
[![Tests](https://img.shields.io/badge/tests-102%20passing-success.svg?style=flat-square)](https://github.com/giak/MnemoLite)

**MnemoLite v1.3.0** provides a high-performance, locally deployable cognitive memory system built *exclusively* on PostgreSQL 17. It empowers AI agents like **Expanse** with robust, searchable, and time-aware memory capabilities, ideal for simulation, testing, analysis, and enhancing conversational AI understanding.

Forget complex external dependencies – MnemoLite leverages the power of modern PostgreSQL extensions for a streamlined, powerful, and easy-to-manage solution.

## ✨ Key Features

*   **PostgreSQL Native:** Relies solely on PostgreSQL 17, `pgvector`, `pg_partman`, and optionally `pg_cron` & `pgmq`. No external vector databases or complex graph engines needed for local deployment.
*   🤖 **100% Local Embeddings:** Uses **Sentence-Transformers** (nomic-embed-text-v1.5) for semantic embeddings. Zero external API dependencies, zero cost, complete privacy.
*   🚀 **High-Performance Search:** Leverages `pgvector` with **HNSW indexing** for fast (<15ms P95) semantic vector and hybrid search directly within the database.
*   ⏳ **Time-Aware Storage:** Automatic monthly table partitioning via `pg_partman` optimizes time-based queries and simplifies data retention/lifecycle management.
*   💾 **Efficient Local Storage:** Planned Hot/Warm data tiering with **INT8 quantization** (via optional `pg_cron` job) significantly reduces disk footprint for long-term local storage.
*   🕸️ **Integrated Relational Graph:** Optional `nodes`/`edges` tables allow modeling causal links and relationships, queryable via standard SQL CTEs.
*   🧩 **Modular & API-First:** Clean REST API defined with OpenAPI 3.1 (FastAPI), facilitating integration. CQRS-inspired logical separation.
*   🖥️ **Modern Web UI v4.0:** Full-featured interface with **SCADA industrial design** using HTMX 2.0, featuring Dashboard, Search, Graph visualization (Cytoscape.js), and real-time Monitoring (ECharts). Modular CSS...