---
title: "sam-david/clawtalk-ios"
source: "https://github.com/sam-david/clawtalk-ios"
date: 2026-03-29
tags: ["ios", "voice-assistant", "openclaw", "speech-to-text", "whisperkit"]
platform: github
author: null
summary: "ClawTalk is a native iOS app for voice and text chat with OpenClaw agents, featuring on-device speech recognition via WhisperKit and multi-agent channel support."
---
# sam-david/clawtalk-ios

**URL:** https://github.com/sam-david/clawtalk-ios
**Description:** Native iOS app for talking to your OpenClaw agents by voice or text. On-device speech recognition, streaming responses, multi-agent channels.
**Language:** Swift
**Stars:** 27 | **Forks:** 3
**Topics:** ai, ios, llm, openclaw, self-hosted, speech-to-text, swift, voice-assistant, whisperkit
**Homepage:** https://clawtalkapp.com/
**Last updated:** 2026-04-04

## README (excerpt)

<p align="center">
  <img src="assets/app-icon.png" width="128" alt="ClawTalk" style="border-radius: 28px;">
</p>

<h1 align="center">ClawTalk</h1>

<p align="center">
  A native iOS app for voice and text chat with your <a href="https://github.com/openclaw/openclaw">OpenClaw</a> agents.
</p>

<p align="center">
  Push-to-talk or hands-free conversation mode with on-device speech recognition, streaming text responses with markdown rendering, text-to-speech output, image sending, and multi-agent channels — all over a secure HTTPS connection to your self-hosted OpenClaw gateway.
</p>

<p align="center">
  <img src="assets/screenshot-channels.png" width="230" alt="Channel list">
  <img src="assets/screenshot-chat1.png" width="230" alt="Chat conversation">
  <img src="assets/screenshot-tools.png" width="230" alt="Tools dashboard">
</p>

## Features

- **Voice input** — Push-to-talk or hands-free conversation mode with Voice Activity Detection
- **On-device speech-to-text** — WhisperKit runs entirely on your phone. Audio never leaves the device.
- **Streaming responses** — Text streams in real-time as your agent generates it
- **Text-to-speech** — Responses are spoken aloud. Choose from ElevenLabs, OpenAI, or Apple's built-in voice.
- **Image sending** — Attach up to 8 photos per message
- **Multi-agent channels** — Create channels for different OpenClaw agents
- **Markdown rendering** — Agent responses render with full markdown support
- **Token usage** — See input/output token counts per message (Open Responses API)
- **Dark mode** — Designed for dark mode with OpenClaw lobster branding
- **Security first** — All credentials in iOS Keychain, HTTPS enforced, on-device STT

## In Development

The following features are built on the ClawTalk side but waiting on upstream OpenClaw gateway support:

- **HTTP model selection** — Browse and switch models without WebSocket (needs `GET /v1/models` gateway endpoint)
- **Server-side session persistence** — Sessions appear in the gateway session list with SOUL.md injection and memory writes (needs gateway to persist HTTP/WS sessions)
- **File read in Tools dashboard** — Read files from the agent workspace via Tools (needs gateway to expose coding tools via `/tools/invoke`)
- **Accurate input token reporting** — Full input/output token breakdown (needs gateway fix for `input_tokens` in Open Responses API)
- **WebSocket model name & token usage** — Display model and token counts in WebSocket mode (needs gateway to include model/usage in chat events)
- **Memory & tools via WebSocket RPC** — Lower-latency tool access over the existing WebSocket connection (needs gateway RPC extensions)
- **Cron message viewing** — View output from scheduled agent cron jobs (needs gateway cron session support)

## Install

ClawTalk is available on the [App Store](https://apps.apple.com/app/clawtalk/id6760325621) for $2.99 (one-time purchase), or you can build it from source for free — see below.

## Requirements

- iOS 17.0+
- Xcode ...