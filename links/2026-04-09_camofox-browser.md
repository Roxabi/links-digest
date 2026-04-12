---
title: "jo-inc/camofox-browser"
source: "https://github.com/jo-inc/camofox-browser"
date: 2026-04-09
tags: ["browser-automation", "anti-detection", "ai-agents", "headless-browser", "web-scraping"]
platform: github
author: null
summary: "A headless browser automation server powered by Camoufox that enables AI agents to bypass bot detection and interact with web pages via a REST API."
---
# jo-inc/camofox-browser

**URL:** https://github.com/jo-inc/camofox-browser
**Description:** Headless browser automation server for AI agents to visit sites that are usually blocked
**Language:** JavaScript
**Stars:** 1904 | **Forks:** 178
**License:** MIT License
**Last updated:** 2026-04-06

## README (excerpt)

<div align="center">
  <img src="fox.png" alt="camofox-browser" width="200" />
  <h1>camofox-browser</h1>
  <p><strong>Anti-detection browser server for AI agents, powered by Camoufox</strong></p>
  <p>
    <a href="https://github.com/jo-inc/camofox-browser/actions"><img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build" /></a>
    <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-blue" alt="License" /></a>
    <a href="https://camoufox.com"><img src="https://img.shields.io/badge/engine-Camoufox-red" alt="Camoufox" /></a>
    <a href="https://hub.docker.com"><img src="https://img.shields.io/badge/docker-ready-blue" alt="Docker" /></a>
  </p>
  <p>
    Standing on the mighty shoulders of <a href="https://camoufox.com">Camoufox</a> - a Firefox fork with fingerprint spoofing at the C++ level.
    <br/><br/>
    The same engine behind <a href="https://askjo.ai?ref=camofox">Jo</a> — an AI assistant that doesn't need you to babysit it. Runs half on your Mac, half on a dedicated cloud machine that only you use. Available on macOS, Telegram, and WhatsApp. <a href="https://askjo.ai?ref=camofox">Try the beta free →</a>
  </p>
</div>

<br/>

```bash
git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
# → http://localhost:9377
```

---

## Why

AI agents need to browse the real web. Playwright gets blocked. Headless Chrome gets fingerprinted. Stealth plugins become the fingerprint.

Camoufox patches Firefox at the **C++ implementation level** - `navigator.hardwareConcurrency`, WebGL renderers, AudioContext, screen geometry, WebRTC - all spoofed before JavaScript ever sees them. No shims, no wrappers, no tells.

This project wraps that engine in a REST API built for agents: accessibility snapshots instead of bloated HTML, stable element refs for clicking, and search macros for common sites.

## Features

- **C++ Anti-Detection** - bypasses Google, Cloudflare, and most bot detection
- **Element Refs** - stable `e1`, `e2`, `e3` identifiers for reliable interaction
- **Token-Efficient** - accessibility snapshots are ~90% smaller than raw HTML
- **Runs on Anything** - lazy browser launch + idle shutdown keeps memory at ~40MB when idle. Designed to share a box with the rest of your stack — Raspberry Pi, $5 VPS, shared Railway infra.
- **Session Isolation** - separate cookies/storage per user
- **Cookie Import** - inject Netscape-format cookie files for authenticated browsing
- **Proxy + GeoIP** - route traffic through residential proxies with automatic locale/timezone
- **Structured Logging** - JSON log lines with request IDs for production observability
- **YouTube Transcripts** - extract captions from any YouTube video via yt-dlp, no API key needed
- **Search Macros** - `@google_search`, `@youtube_search`, `@amazon_search`, `@reddit_subreddit`, and 10 more
- **Snapshot Screenshots** - include a base64 PNG screenshot alongside the accessibility snap...