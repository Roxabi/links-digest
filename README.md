# links-digest

Discord links digest with frontmatter MDs and dynamic gallery.

## Structure

```
links-digest/
├── digest.py           # Fetch Discord + scrape URLs → MDs
├── config.toml         # Channel ID, time window
├── templates/
│   └── link.md.j2      # Jinja2 template with frontmatter
├── links/              # YYYY-MM-DD_slug.md files
│   └── manifest.json
├── public/             # Deploy root (CF Pages)
│   ├── index.html      # Dynamic gallery
│   ├── css/gallery.css
│   └── js/gallery.js
└── Makefile
```

## Usage

```bash
# Scan last 24 hours (default)
make digest

# Scan last 72 hours
make digest H=72

# Scan last 7 days
make digest D=7

# Scan entire channel history (first run)
make digest-all

# Build manifest.json
make build

# Deploy to Cloudflare Pages
make deploy
```

## Frontmatter format

```yaml
---
title: VoiceDesignCloner
source: https://github.com/reinehonoka/Voice-Design-Cloner
date: 2026-04-10
tags: [TTS, voice-cloning, Qwen3]
platform: github
author: null
---

# VoiceDesignCloner

Content...
```

## Requirements

- Python 3.11+
- Discord bot token stored in Lyra CredentialStore (`discord_bot_token`)
- `web-intel` plugin for scraping

## Cloudflare Pages setup

1. Create project: `npx wrangler pages project create links-digest`
2. Deploy: `make deploy`
3. Set output directory: `public`
