---
title: "Qwen3.5-35B-A3B Training Bug Fix — FernflowerAI GGUF"
source: "https://www.reddit.com/r/LocalLLaMA/comments/1sfwauj/qwen3535ba3buncensoredfernfloweraigguf/"
date: 2026-04-09
tags: ['Qwen3.5', 'local LLM', 'bug fix', 'MoE', 'GGUF']
platform: reddit
author: null
summary: "**Relevance to your setup:** You're running an RTX 3080 (prod) — the fixed Q4_K_L quant runs on a 3060 12GB at ~10 tok/s in LM Studio, so it should be..."
---

# Qwen3.5-35B-A3B Training Bug Fix — FernflowerAI GGUF

**Source:** https://www.reddit.com/r/LocalLLaMA/comments/1sfwauj/qwen3535ba3buncensoredfernfloweraigguf/
**Date:** 2026-04-09

---

**Relevance to your setup:** You're running an RTX 3080 (prod) — the fixed Q4_K_L quant runs on a 3060 12GB at ~10 tok/s in LM Studio, so it should be comfortable on your 3080. Worth trying if you've been using Qwen3.5 35B A3B for any long-context tasks on Lyra or voiceCLI.

**Downloads:**
- [35B GGUF (fixed)](https://huggingface.co/LuffyTheFox/Qwen3.5-35B-A3B-Uncensored-FernflowerAI-GGUF)
- [35B safetensors](https://huggingface.co/LuffyTheFox/Qwen3.5-35B-A3B-Uncensored-FernflowerAI-safetensors)
- [27B GGUF (experimental)](https://huggingface.co/LuffyTheFox/Qwen3.5-27B-Claude-4.6-Opus-FernflowerAI-GGUF)