---
title: "camofox-browser — Anti-Detection Headless Browser Server for AI Agents"
source: "https://github.com/jo-inc/camofox-browser"
date: 2026-04-09
tags: ['browser automation', 'anti-detection', 'AI agents', 'headless browser']
platform: github
author: null
---

# camofox-browser — Anti-Detection Headless Browser Server for AI Agents

**Source:** https://github.com/jo-inc/camofox-browser
**Date:** 2026-04-09

---

-|
| Element refs | Stable `e1`/`e2`/`e3` IDs for reliable clicking |
| Token-efficient snapshots | Accessibility tree instead of raw HTML — ~90% smaller |
| Session isolation | Per-user cookies/storage |
| Cookie import | Netscape-format files for authenticated sessions |
| Proxy + GeoIP | Residential proxy routing with auto locale/timezone |
| Search macros | `@google_search`, `@youtube_search`, `@amazon_search` + 10 more |
| YouTube transcripts | Via `yt-dlp`, no API key |
| Low idle footprint | ~40 MB when idle |

## Tech Stack

- **Engine:** Camoufox (Firefox fork)
- **Runtime:** Node.js with REST API (default port 9377)
- **Deployment:** Docker, Fly.io, Railway

## Quick Start

```bash
git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
# → http://localhost:9377
```