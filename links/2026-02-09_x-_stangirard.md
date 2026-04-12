---
title: "I reverse-engineered Claude Code's binary."
source: "https://x.com/_stangirard/status/2020979746931085772?s=46"
date: 2026-02-09
tags: ["claude-code", "reverse-engineering", "websocket", "remote-access"]
platform: x
author: "@_StanGirard"
summary: "Stan Girard reverse-engineered Claude Code to enable remote access via a hidden WebSocket feature."
---
I reverse-engineered Claude Code's binary.

Found a flag they hid from --help.

--sdk-url

Enable it and the terminal disappears. The CLI becomes a WebSocket client.

We built a server to catch the connection. Added a React UI on top.

Now I run Claude Code from my browser. From my phone. From anywhere.

Same $200/month subscription. Zero extra API costs.

bunx the-vibe-companion

http://github.com/The-Vibe-Company/companion