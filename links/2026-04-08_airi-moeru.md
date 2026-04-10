---
title: "AIRI — Self-hosted AI Virtual Character Platform"
source: "https://github.com/moeru-ai/airi"
date: 2026-04-08
tags: ['AI agent', 'voice', 'virtual character', 'multimodal', 'WebGPU']
platform: github
author: null
summary: "AIRI is a self-hosted AI virtual character/waifu platform inspired by Neuro-sama, designed to create "cyber living beings" that can chat, play games, ..."
---

# AIRI — Self-hosted AI Virtual Character Platform

**Source:** https://github.com/moeru-ai/airi
**Date:** 2026-04-08

---

AIRI is a self-hosted AI virtual character/waifu platform inspired by Neuro-sama, designed to create "cyber living beings" that can chat, play games, and interact in real-time across web, desktop, and mobile platforms.

### Main Features
- **Real-time voice chat** with browser-based audio input and speech recognition
- **Game-playing agents**: Minecraft, Factorio, Kerbal Space Program (WIP: Helldivers 2)
- **Platform integrations**: Discord and Telegram chat
- **Avatar support**: VRM and Live2D models with animations (auto-blink, look-at, idle movements)
- **Memory system**: In-browser databases (DuckDB WASM, pglite) plus WIP "Memory Alaya"
- **Voice synthesis**: ElevenLabs integration
- **Multi-platform**: Web (PWA), desktop (Electron), mobile (Capacitor)

### Tech Stack
- **Core**: Vue.js, TypeScript, WebGPU, WebAudio, Web Workers, WebAssembly, WebSocket
- **Native acceleration**: NVIDIA CUDA, Apple Metal (via HuggingFace candle)
- **LLM gateway**: xsai library supporting 25+ providers (OpenAI, Claude, Gemini, DeepSeek, xAI, Ollama, vLLM, etc.)
- **Build tools**: pnpm monorepo, Turbo, Vite
- **Packaging**: Electron, Capacitor, Nix flakes

### Relevance for AI Agent/Voice Stack
AIRI is highly relevant as a reference implementation for:
1. **Unified LLM abstraction** via xsai (similar to LiteLLM but with broader provider support)
2. **Real-time voice pipeline**: VAD + STT + LLM + TTS chain
3. **Browser-based inference** using WebGPU and Transformers.js
4. **Game-playing agent architecture** (Mineflayer for Minecraft, RCON for Factorio)
5. **MCP (Model Context Protocol) launcher** for tool integration
6. **Unspeech** - universal endpoint proxy for ASR/TTS (like LiteLLM but for audio)