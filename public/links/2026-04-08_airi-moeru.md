---
title: "AIRI — Self-hosted AI Virtual Character Platform"
source: "https://github.com/moeru-ai/airi"
date: 2026-04-08
tags: ['AI agent', 'voice', 'virtual character', 'multimodal', 'WebGPU']
platform: github
author: null
---

# AIRI — Self-hosted AI Virtual Character Platform

**Source:** https://github.com/moeru-ai/airi
**Date:** 2026-04-08

---

--|
| Framework | Vue.js, TypeScript |
| Web | WebGPU, WebAudio, Web Workers, WebAssembly, WebSocket |
| Native Acceleration | NVIDIA CUDA, Apple Metal (via HuggingFace candle) |
| Build | pnpm monorepo, Turbo, Vite |
| Desktop | Electron-based ("Stage Tamagotchi") |
| Mobile | Capacitor ("Stage Pocket") |
| ORM | Drizzle with DuckDB WASM driver |

## Architecture

The project uses a modular "organ" metaphor:

```
UI → StageUI → Stage → Core

Brain  → LLM integration, game-playing agents, memory
Ears   → Audio input, speech recognition
Mouth  → Voice synthesis (ElevenLabs supported)
Body   → VRM/Live2D avatar rendering and animation
```

## Supported Platforms

- **Web:** Browser version at airi.moeru.ai (PWA supported)
- **Desktop:** Windows, macOS (native installers available)
- **Mobile:** iOS/Android via Capacitor
- **Package Managers:** Windows Scoop bucket, Nix flakes

## LLM Providers (via xsai)

Extensive support including: OpenAI/Azure OpenAI, Anthropic Claude, Google Gemini, xAI, DeepSeek, Qwen, Mistral, Groq, Ollama, vLLM, SGLang, OpenRouter, Together.ai, Fireworks.ai, and many Chinese providers (Zhipu, SiliconFlow, Stepfun, Baichuan, Minimax, Moonshot, ModelScope, Tencent Cloud).

## Voice Pipeline

"Unspeech" provides "Universal endpoint proxy server for audio/transcriptions and audio/speech, like LiteLLM but for any ASR and TTS."

Pipeline: **VAD (Voice Activity Detection) + STT (Speech-to-Text) + LLM + TTS (Text-to-Speech)**