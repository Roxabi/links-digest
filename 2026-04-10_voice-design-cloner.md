# VoiceDesignCloner — Recording-Free TTS Training Data Generator via Qwen3-TTS GUI

**Source:** https://github.com/reinehonoka/Voice-Design-Cloner
**Date:** 2026-04-10
**Tags:** TTS, voice cloning, Qwen3, Style-Bert-VITS2, Python

---

A GUI tool that solves the hardest part of building a custom TTS model: **getting training data without recording anything yourself.**

**What it does:**
- **Voice Design** — Generate a voice from a text prompt (zero-shot, no mic needed)
- **Voice Gacha** — Re-roll until you like the result
- **Bulk corpus synthesis** — Feed it hundreds/thousands of sentences, outputs WAV at 44.1kHz
- **Preprocessing pipeline** — Resamples + generates `esd.list` ready for Style-Bert-VITS2 training

**Stack:**
- Backend → Qwen3-TTS (Apache 2.0), with optional `faster-qwen3-tts` for 6–10× speedup via CUDA Graph
- Frontend → Gradio
- Output target → Style-Bert-VITS2

**Hardware fit for your setup:**

| Req | Spec |
|---|---|
| GPU | NVIDIA CUDA |
| VRAM | 8 GB min — **16 GB recommended** |
| Python | 3.10–3.12 |

Your RTX 5070 Ti (16 GB) hits the sweet spot — it's actually in the confirmed-working matrix (RTX 5070 at 12 GB passed). You'd run the `faster` backend comfortably.

**Relevance to voiceCLI:** direct overlap — this could feed training data into a Style-Bert-VITS2 pipeline, or the `faster-qwen3-tts` backend could be worth benchmarking as an alternative inference path.
