---
title: "spiritbuun/buun-llama-cpp"
source: "https://github.com/spiritbuun/llama-cpp-turboquant-cuda"
date: 2026-03-28
tags: ["llama.cpp", "quantization", "kv-cache", "tcq", "cuda"]
platform: github
author: null
summary: "An experimental fork of llama.cpp implementing Trellis-Coded Quantization (TCQ) for KV cache compression, allowing 2-3x more context in VRAM while maintaining or beating FP16 quality."
---
# spiritbuun/buun-llama-cpp

**URL:** https://github.com/spiritbuun/buun-llama-cpp
**Description:** LLAMA Turboquant implementation with CUDA support
**Language:** C++
**Stars:** 400 | **Forks:** 35
**License:** MIT License
**Note:** This is a fork
**Last updated:** 2026-04-11

## README (excerpt)

# buun-llama-cpp

![buunslamma](buunslamma.png)

> **This is a highly experimental fork of llama.cpp. Use at your own discretion.**

A fork of [llama.cpp](https://github.com/ggml-org/llama.cpp) with **Trellis-Coded Quantization (TCQ)** for KV cache compression. 2-3x more context in the same VRAM, with quality that matches or beats FP16.

**Paper**: [Closing the Gap: Trellis-Coded Quantization for KV Cache at 2-3 Bits](https://huggingface.co/datasets/spiritbuun/turboquant-tcq-kv-cache)

## What is TCQ?

Standard KV cache quantization treats each value independently. TCQ constrains quantization indices to follow a 512-state trellis, enabling a much larger effective codebook at the same bit rate. Combined with FWHT rotation and context-adaptive norm scaling, this achieves **10-44% KL-divergence reduction** over scalar quantization at 2-3 bits per value.

At 3.25 bits per value, TCQ produces **lower perplexity than FP16** KV cache (5.802 vs 5.805).

## Build

```sh
cmake -B build \
  -DGGML_CUDA=ON \
  -DGGML_NATIVE=ON \
  -DGGML_CUDA_FA=ON \
  -DGGML_CUDA_FA_ALL_QUANTS=ON \
  -DCMAKE_BUILD_TYPE=Release

cmake --build build -j$(nproc)
```

## Recommended configurations

### turbo4 (4.25 bpv) -- lossless quality, great compression

The safe default. Virtually no quality loss vs FP16 with ~3.8x KV cache compression and no speed penalty.

```sh
./build/bin/llama-server -m model.gguf -ngl 99 -fa \
  -ctk turbo4 -ctv turbo4
```

### 3-bit TCQ (3.25 bpv) -- best quality at 3-bit

Beats FP16 quality at short context, stays within 2% at long context. ~5x KV cache compression.

```sh
./build/bin/llama-server -m model.gguf -ngl 99 -fa \
  -ctk turbo3_tcq -ctv turbo3_tcq
```

### 2-bit TCQ (2.25 bpv) -- maximum compression

~7x KV cache compression. Best for fitting very long contexts in limited VRAM.

```sh
./build/bin/llama-server -m model.gguf -ngl 99 -fa \
  -ctk turbo2_tcq -ctv turbo2_tcq
```

### Asymmetric 2.75 bpv -- best 2-bit quality

3-bit keys + 2-bit values. 15-17% lower KLD than the reverse, because adaptive alpha already compensates V quantization error.

```sh
./build/bin/llama-server -m model.gguf -ngl 99 -fa \
  -ctk turbo3_tcq -ctv turbo2_tcq
```

### Scalar turbo3 / turbo2 (3.25 / 2.25 bpv) -- no trellis

Scalar quantization without TCQ. Faster encode, worse quality than TCQ equivalents.

```sh
# 3-bit scalar
./build/bin/llama-server -m model.gguf -ngl 99 -fa \
  -ctk turbo3 -ctv turbo3

# 2-bit scalar
./build/bin/llama-server -m model.gguf -ngl 99 -fa \
  -ctk turbo2 -ctv turbo2
```

## Quality (KL-divergence, Qwen3.5-27B Q6_K, RTX 3090)

Lower is better. Measured against FP16 KV cache base logits.

| Config | bpv | KLD @2K | KLD @7K |
|--------|-----|---------|---------|
| turbo3_tcq (symmetric) | 3.25 | 0.058 | 0.074 |
| turbo3_tcq-K / turbo2_tcq-V | 2.75 | 0.078 | 0.101 |
| turbo2_tcq (symmetric) | 2.25 | 0.101 | 0.136 |

3-bit TCQ at 2K context achieves **lower perplexity than FP16** (5.802 vs 5.805) due to a mild regularizing effect fr...