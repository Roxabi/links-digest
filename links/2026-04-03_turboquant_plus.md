---
title: "TheTom/turboquant_plus"
source: "https://github.com/TheTom/turboquant_plus"
date: 2026-04-03
tags: ["python", "llm", "quantization", "kv-cache-compression", "llama.cpp"]
platform: github
author: null
summary: "TurboQuant+ is a Python implementation of KV cache compression for local LLM inference, featuring experimental llama.cpp integration and validated findings on asymmetric compression strategies."
---
# TheTom/turboquant_plus

**URL:** https://github.com/TheTom/turboquant_plus
**Description:** 
**Language:** Python
**Stars:** 6111 | **Forks:** 842
**License:** Apache License 2.0
**Last updated:** 2026-04-10

## README (excerpt)

# TurboQuant+

> ### [Getting Started Guide](docs/getting-started.md) | [Configuration Recommendations](docs/turboquant-recommendations.md) | [llama.cpp Fork](https://github.com/TheTom/llama-cpp-turboquant) | [Swift MLX Fork](https://github.com/ekryski/mlx-swift-lm)

> **🍎 On Apple Silicon and want the fastest path?** Use [ekryski/mlx-swift-lm](https://github.com/ekryski/mlx-swift-lm) — Eric Kryski's Swift MLX implementation that I've been actively collaborating on. Native Swift, ~2.5x faster decode than Python mlx-lm, full TurboQuant+ support including turbo4v2 (4-bit K + 2-bit V). 144 tok/s on Qwen3.5-35B-A3B MoE at 4K on M5 Max. This llama.cpp repo is for cross-platform deployment (CUDA, ROCm, CPU, Metal).

Implementation of [TurboQuant](https://research.google/blog/turboquant-redefining-ai-efficiency-with-extreme-compression/) (ICLR 2026) with implementation work, experiments, and follow-on findings beyond the base paper. KV cache compression for local LLM inference.

## Note

This repository is an experimental integration and research workspace for TurboQuant-related work targeting `llama.cpp`. The goal is to make it easier to compare approaches, collect reproducible benchmark and quality data, and share implementation details across hardware and backends. It is not intended as a separate long-term fork or a proposal to merge the branch as a whole.

If individual pieces prove useful and stable, the intent is to upstream them incrementally as small, reviewable patches in line with `llama.cpp`'s normal contribution process.

## What's In This Branch

- Experimental TurboQuant-related integrations for `llama.cpp`
- Benchmark and quality validation across models, contexts, and hardware
- Backend-specific implementation work and performance experiments
- Documentation and writeups intended to make testing and reproduction easier
- Candidate ideas that may be worth upstreaming individually if they prove stable

## Current Findings

Three follow-on findings in this branch have been independently validated by multiple researchers across different hardware and backends:

1. **V compression is free.** Compressing the value cache (even down to 2 bits) has zero measurable effect on attention quality when key precision is maintained. Confirmed on Metal (M5 Max), CUDA RTX 4090 (@sztlink), and CUDA RTX 3090 (@HyperionMS2040). See [asymmetric K/V paper](docs/papers/asymmetric-kv-compression.md).
2. **All quality degradation comes from K compression.** This is why asymmetric configs (q8_0-K + turbo-V) rescue models where symmetric fails. Validated across Qwen, Llama, Mistral, and Command-R+ families. See [M5 Max stress test](docs/papers/m5-max-stress-test.md).
3. **Boundary layers are disproportionately sensitive.** Protecting the first 2 + last 2 layers at higher precision recovers 37-91% of the quality gap. See [Boundary V paper](docs/papers/layer-aware-v-compression.md).

Additional experiments and writeups: [Sparse V dequant](docs/papers/sparse-v-dequant...