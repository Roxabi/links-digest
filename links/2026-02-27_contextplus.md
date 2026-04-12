---
title: "ForLoopCodes/contextplus"
source: "https://github.com/ForLoopCodes/contextplus"
date: 2026-02-27
tags: ["mcp server", "semantic search", "code analysis", "typescript"]
platform: github
author: "ForLoopCodes"
summary: "Context+ is an MCP server providing semantic intelligence tools for large-scale engineering using RAG and AST analysis."
---
# ForLoopCodes/contextplus

**URL:** https://github.com/ForLoopCodes/contextplus
**Description:** Semantic Intelligence for Large-Scale Engineering. Context+ is an MCP server designed for developers who demand 99% accuracy. By combining RAG, Tree-sitter AST, Spectral Clustering, and Obsidian-style linking, Context+ turns a massive codebase into a searchable, hierarchical feature graph.
**Language:** TypeScript
**Stars:** 1760 | **Forks:** 136
**License:** MIT License
**Topics:** mcp-server
**Homepage:** https://contextplus.vercel.app
**Last updated:** 2026-04-06

## README (excerpt)

# Context+

Semantic Intelligence for Large-Scale Engineering.

Context+ is an MCP server designed for developers who demand 99% accuracy. By combining RAG, Tree-sitter AST, Spectral Clustering, and Obsidian-style linking, Context+ turns a massive codebase into a searchable, hierarchical feature graph.

**While you're here, check out my other project Airena. Curate a team of AI agents and face head-to-head with other orchestrators. First place on the leaderboard gets a $1600 prize!**

https://github.com/user-attachments/assets/a97a451f-c9b4-468d-b036-15b65fc13e79

## Tools

### Discovery

| Tool                         | Description                                                                                                                                                      |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `get_context_tree`           | Structural AST tree of a project with file headers and symbol ranges (line numbers for functions/classes/methods). Dynamic pruning shrinks output automatically. |
| `get_file_skeleton`          | Function signatures, class methods, and type definitions with line ranges, without reading full bodies. Shows the API surface.                                   |
| `semantic_code_search`       | Search by meaning, not exact text. Uses embeddings over file headers/symbols and returns matched symbol definition lines.                                        |
| `semantic_identifier_search` | Identifier-level semantic retrieval for functions/classes/variables with ranked call sites and line numbers.                                                     |
| `semantic_navigate`          | Browse codebase by meaning using spectral clustering. Groups semantically related files into labeled clusters.                                                   |

### Analysis

| Tool                  | Description                                                                                                                   |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `get_blast_radius`    | Trace every file and line where a symbol is imported or used. Prevents orphaned references.                                   |
| `run_static_analysis` | Run native linters and compilers to find unused variables, dead code, and type errors. Supports TypeScript, Python, Rust, Go. |

### Code Ops

| Tool              | Description                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `propose_commit`  | The only way to write code. Validates against strict rules before saving. ...