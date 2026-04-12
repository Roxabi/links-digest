---
title: "PunithVT/ai-avatar-system"
source: "https://github.com/PunithVT/ai-avatar-system"
date: 2026-04-03
tags: ["ai-avatar", "voice-cloning", "lip-sync", "real-time-voice", "generative-ai"]
platform: github
author: null
summary: "AvatarAI is an open-source AI avatar platform that enables real-time conversations with any face using voice cloning, lip-sync video generation, and multi-LLM integrations."
---
# PunithVT/ai-avatar-system

**URL:** https://github.com/PunithVT/ai-avatar-system
**Description:** 🎭 Open-source AI avatar platform — upload a photo, clone a voice, talk to any face in real time. Lip-sync video, voice cloning, WebSocket streaming. Powered by Claude, Whisper & MuseTalk.
**Language:** Python
**Stars:** 14 | **Forks:** 3
**Topics:** ai-avatar, avatar-ai, claude-ai, digital-avatar, fastapi, generative-ai, lip-sync, nextjs, real-time-voice, sadtalker, speech-to-text, talking-avatar, text-to-speech, voice-agent, voice-cloning, websocket, whisper-ai, xtts-v2
**Last updated:** 2026-03-31

## README (excerpt)

<div align="center">

<h1>🎭 AvatarAI — Real-Time AI Avatar Platform</h1>

<p><strong>Upload a photo · Clone a voice · Talk to any face in real time</strong></p>

<p>
  <a href="https://github.com/PunithVT/ai-avatar-system/stargazers"><img src="https://img.shields.io/github/stars/PunithVT/ai-avatar-system?style=for-the-badge&color=7c3aed" alt="Stars"/></a>
  <a href="https://github.com/PunithVT/ai-avatar-system/forks"><img src="https://img.shields.io/github/forks/PunithVT/ai-avatar-system?style=for-the-badge&color=3b82f6" alt="Forks"/></a>
  <a href="https://github.com/PunithVT/ai-avatar-system/issues"><img src="https://img.shields.io/github/issues/PunithVT/ai-avatar-system?style=for-the-badge" alt="Issues"/></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge" alt="MIT License"/></a>
</p>

<p>
  <img src="https://img.shields.io/badge/Next.js-14-black?logo=next.js&style=flat-square" />
  <img src="https://img.shields.io/badge/FastAPI-0.109-009688?logo=fastapi&style=flat-square" />
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&style=flat-square" />
  <img src="https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript&style=flat-square" />
  <img src="https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&style=flat-square" />
  <img src="https://img.shields.io/badge/CUDA-11.8-76B900?logo=nvidia&style=flat-square" />
  <img src="https://img.shields.io/badge/PostgreSQL-15-336791?logo=postgresql&style=flat-square" />
  <img src="https://img.shields.io/badge/Redis-7-DC382D?logo=redis&style=flat-square" />
</p>

<p>
  <a href="#-quick-start">Quick Start</a> ·
  <a href="#-features">Features</a> ·
  <a href="#-architecture">Architecture</a> ·
  <a href="#-gpu--aws-deployment">GPU / AWS Deploy</a> ·
  <a href="#-api-reference">API</a> ·
  <a href="#-roadmap">Roadmap</a>
</p>

> **The most complete open-source AI talking avatar system.**
> Real-time lip-sync · Zero-shot voice cloning · Multi-LLM · Runs 100% locally or on AWS.

</div>

---

## 🎬 What is AvatarAI?

AvatarAI is an open-source, production-ready platform for building **photorealistic AI avatar conversations**. Upload any face photo, clone a voice from a 5-second audio clip, and have a real-time conversation — with **lip-sync video generated on every single response**.

```
[mic input]  →  Whisper STT  →  Claude / GPT-4  →  XTTS v2 TTS  →  MuseTalk lip-sync  →  [video]
                                 < 2–4 s first chunk on AWS GPU >
```

**What makes AvatarAI different:**
- 🎤 **Zero-shot voice cloning** — 5 seconds of audio is all you need (XTTS v2)
- 🎭 **Any face, any language** — upload a JPEG, pick from 18 languages, start talking
- ⚡ **Sentence-chunk streaming** — first video chunk plays while the rest is still being generated
- 😴 **Idle animation** — avatar breathes and glows while waiting, no blank screens
- 🔒 **100% local mode** — nothing leaves your machine
- 🔌 **Multi-LLM** — Claude, GPT-4, ...