# camofox-browser — Anti-Detection Headless Browser Server for AI Agents

**Source:** https://github.com/jo-inc/camofox-browser
**Date:** 2026-04-09
**Tags:** browser automation, anti-detection, AI agents, headless browser, Playwright alternative

---

**camofox-browser** is an open-source REST API server that wraps [Camoufox](https://camoufox.com) — a Firefox fork that patches fingerprint spoofing at the C++ level — making it viable for AI agents to browse sites that normally block headless browsers.

**Why it's different from Playwright/Puppeteer:**
- Fingerprint spoofing happens at the C++ layer (`hardwareConcurrency`, WebGL, AudioContext, WebRTC) — no JS shims that are themselves detectable
- Passes Cloudflare, Google, and most commercial bot detection

**Key features:**
| Feature | Detail |
|---|---|
| Element refs | Stable `e1`/`e2`/`e3` IDs for reliable clicking |
| Token-efficient snapshots | Accessibility tree instead of raw HTML — ~90% smaller |
| Session isolation | Per-user cookies/storage |
| Cookie import | Netscape-format files for authenticated sessions |
| Proxy + GeoIP | Residential proxy routing with auto locale/timezone |
| Search macros | `@google_search`, `@youtube_search`, `@amazon_search`, `@reddit_subreddit` + 10 more |
| YouTube transcripts | Via `yt-dlp`, no API key |
| Low idle footprint | ~40 MB when idle — fits alongside your stack |

**Quick start:**
```bash
git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
# → http://localhost:9377
```

**Relevance to your stack:** Could slot in nicely alongside Lyra for agent web browsing tasks — lightweight enough to run on `roxabituwer` alongside your existing daemons.
