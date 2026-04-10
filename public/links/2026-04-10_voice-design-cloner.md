---
title: "VoiceDesignCloner — Recording-Free TTS Training Data Generator via Qwen3-TTS GUI"
source: "https://github.com/reinehonoka/Voice-Design-Cloner"
date: 2026-04-10
tags: ['TTS', 'voice cloning', 'Qwen3', 'Style-Bert-VITS2', 'Python']
platform: github
author: null
summary: "A GUI tool that solves the hardest part of building a custom TTS model: **getting training data without recording anything yourself.**"
---

# VoiceDesignCloner — Recording-Free TTS Training Data Generator via Qwen3-TTS GUI

**Source:** https://github.com/reinehonoka/Voice-Design-Cloner
**Date:** 2026-04-10

---

|
| GPU | NVIDIA CUDA |
| VRAM | 8 GB min — **16 GB recommended** |
| Python | 3.10–3.12 |

Your RTX 5070 Ti (16 GB) hits the sweet spot — it's actually in the confirmed-working matrix (RTX 5070 at 12 GB passed). You'd run the `faster` backend comfortably.

**Relevance to voiceCLI:** direct overlap — this could feed training data into a Style-Bert-VITS2 pipeline, or the `faster-qwen3-tts` backend could be worth benchmarking as an alternative inference path.