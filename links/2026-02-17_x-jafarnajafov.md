---
title: "Holy shit... someone just built the \"Ollama for voice\" and it's completely op..."
source: "https://x.com/jafarnajafov/status/2023684728252178546?s=46"
date: 2026-02-17
tags: ["voice cloning software", "open source tool", "local text-to-speech", "Qwen3-TTS model"]
platform: x
author: "@JafarNajafov"
summary: "Voicebox is a free open-source tool for local voice cloning using Qwen3-TTS, offering an alternative to paid cloud services."
---
Holy shit... someone just built the "Ollama for voice" and it's completely opensource.

It's called Voicebox and it clones any voice from a few seconds of audio.

No cloud. No subscription. No voice data ever leaving your machine.

The model behind it is Qwen3-TTS from Alibaba.

Near-perfect voice cloning from just a short audio sample.

Natural prosody, emotion, and cadence not the robotic TTS you're used to.

Multi-language support. English, Chinese, and more coming.

But the app itself is where it gets insane.

Think of it as a full DAW for voice:

→ Clone voices with one click
→ Arrange multi-speaker dialogues on a timeline
→ Trim and split clips inline
→ Record system audio directly
→ Auto-transcribe everything with Whisper

This isn't a demo. It's a production tool.

The tech stack is elite:

→ Tauri (Rust) instead of Electron 10x smaller, native speed
→ FastAPI backend with auto-generated OpenAPI docs
→ Full REST API for building your own voice-powered apps
→ SQLite for local-first storage
→ Voice prompt caching for instant regeneration

Zero Python install required from the user.

Here's the wildest part:

ElevenLabs charges $5-$99/month for voice cloning behind their cloud.

Voicebox does the same thing for $0. Forever. On your hardware.

Your voice data never touches a server.

MIT Licensed. macOS + Windows available now.

Link in the comment.