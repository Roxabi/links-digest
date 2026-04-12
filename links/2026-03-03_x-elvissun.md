---
title: "zoe was burning 24M+ opus tokens/day monitoring agents that weren't running."
source: "https://x.com/elvissun/status/2028671336219107687?s=46"
date: 2026-03-03
tags: ["opus tokens", "token reduction", "event-driven stack", "monitoring agents"]
platform: x
author: "@elvissun"
summary: "The author reduced Zoe's daily Opus token consumption by 95% by replacing a cron job with a two-layer event-driven monitoring system."
---
zoe was burning 24M+ opus tokens/day monitoring agents that weren't running.

replaced her cron with a 2-layer system:
- bash pre-check, zero tokens when idle
- webhook fires opus only when needed.

~95% token reduction and more reliable output. details below.

(set up a cron to watch this performance, if it works well I'll double down on this event driven stack, seems like the future)