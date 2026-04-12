---
title: "MonsieurBarti/code-graph-ai"
source: "https://github.com/MonsieurBarti/code-graph-ai"
date: 2026-02-22
tags: ["code intelligence engine", "dependency graph tool", "multi-language parser", "Rust CLI tool", "AI developer tool"]
platform: github
author: "MonsieurBarti"
summary: "A high-performance Rust-based code intelligence engine that indexes TypeScript, JavaScript, Rust, Python, and Go codebases into a queryable dependency graph with Claude Code integration."
---
# MonsieurBarti/code-graph-ai

**URL:** https://github.com/MonsieurBarti/code-graph-ai
**Description:** 
**Language:** Rust
**Stars:** 5 | **Forks:** 2
**License:** MIT License
**Last updated:** 2026-03-15

## README (excerpt)

# code-graph

<p align="center">
  <img src="assets/banner.png" alt="Code Graph AI" />
</p>

High-performance code intelligence engine that indexes TypeScript, JavaScript, Rust, Python, and Go codebases into a queryable dependency graph. Built in Rust, designed for AI agents.

Gives [Claude Code](https://docs.anthropic.com/en/docs/claude-code) direct access to your codebase's structure via hooks-based integration -- no source file reading needed. One `code-graph setup` command installs transparent PreToolUse hooks that auto-approve CLI calls and enrich search queries with structural graph data.

## Features

- **Multi-language parsing** -- TypeScript, TSX, JavaScript, JSX, Rust, Python, and Go via tree-sitter with full symbol extraction (functions, classes, interfaces, types, enums, components, methods, properties, structs, traits, impl blocks, macros, pub visibility, async/sync functions, decorators, type aliases, struct tags)
- **Python parsing** -- functions (sync/async), classes, variables, type aliases (PEP 695), decorators with framework detection (Flask, FastAPI, Django)
- **Go parsing** -- functions, methods, type specs, struct tags, `//go:` directives as decorators, visibility by export convention, go.mod resolution
- **Decorator/attribute extraction** -- unified across all 5 languages with framework inference (NestJS, Flask, FastAPI, Actix, Angular)
- **Dependency graph** -- file-level and symbol-level edges: imports, calls, extends, implements, type references, has-decorator, child-of, embeds
- **Import resolution** -- TypeScript path aliases (tsconfig.json), barrel files (index.ts re-exports), monorepo workspaces, Rust crate-root module resolution with Cargo workspace discovery, Python package resolution, Go module resolution
- **25 CLI commands** -- find definitions, trace references, blast radius analysis, circular dependency detection, 360-degree symbol context, project statistics, graph export, file structure, file summaries, import analysis, dead code detection, clone detection, graph diff, decorator search, clustering, call chain tracing, rename planning, diff impact, project registry management, daemon control, hooks setup
- **Hooks-based Claude Code integration** -- `code-graph setup` installs PreToolUse hooks that transparently intercept tool calls, auto-approve CLI invocations, and enrich Grep/Glob searches with structural graph data
- **Background daemon** -- `code-graph daemon start` launches a persistent background process that watches for file changes and keeps the graph index up to date automatically
- **Multi-project registry** -- `code-graph project add` registers project aliases for cross-project queries with `--project` flag on any query command
- **Interactive web UI** -- `code-graph serve` launches an Axum backend + Svelte frontend with WebGL graph visualization, file tree, code panel, search, and real-time WebSocket updates
- **RAG conversational agent** -- hybrid retrieval (structural graph + vector embeddings),...