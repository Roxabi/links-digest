---
title: "Chiti (My bot) started getting \"short-term memory loss\".."
source: "https://x.com/code_rams/status/2023514892297531863?s=46"
date: 2026-02-16
tags: ["memory management", "rate limiting", "embeddings", "bot development", "debugging"]
platform: x
author: "@code_rams"
summary: "The author describes how upgrading their bot's memory system caused model failures due to frequent embedding operations that hit rate limits, and shares their solution of reducing refresh frequency."
---
Chiti (My bot) started getting "short-term memory loss".. 
so I upgraded his memory 
and accidentally crashed every model.

I already had QMD + Qdrant.

After each session Chiti 
-> compact + flush, 
->write a daily memory file, 
->and read it back next time. 

Still felt like something was missing.

So I went full nerd:  
- backed everything up to GitHub
- added Rowboat for a beautiful visual "memory graph"

That’s when the chaos started.

Everything looked fine… 

then suddenly
- all models started failing
- gateway screaming “already running” on port 18789
- OpenClaw: “All models failed”

Root cause (simple): 
I re-indexed Chiti’s brain every 30 minutes.

The culprit:
qmd update → qmd embed -f → qmd status (every 30m)
i
-f = force rebuild embeddings 
→ burns quota fast
→ providers hit rate limits 
→ cooldown cascade.

Bonus comedy: 
gateway + macOS LaunchAgent started fighting → duplicate processes on same port.

Fix:
• slowed QMD refresh to every 6h (daily for now)
• removed -f (force only weekly/manual)
• disabled unsupported fallbacks
• gateway in ONE mode only

Takeaway: 
Agent memory = remembering + indexing.
Treat indexing like backups, not heartbeats.

Embedding jobs are silent quota killers. 
Set limits.

Holding Rowboat for now, suggest your favorite lightweight memory visualization tool? 

Any suggestions to improve chiti's memory?

Im happy to try it out. 
Preferring open source.