---
title: "just ran a security audit on 3 openclaw setups this week"
source: "https://x.com/johann_sath/status/2025286187116900831?s=46"
date: 2026-02-21
tags: ["security", "openclaw"]
platform: x
author: "@johann_sath"
summary: "An ex-Cisco engineer audited OpenClaw setups and found critical vulnerabilities including root execution and exposed API keys."
---
just ran a security audit on 3 openclaw setups this week

what i found on all 3:

→ running as root
→ no firewall (all ports open)
→ API keys in plain text on the host
→ no sandbox (agent has full system access)
→ no fail2ban (unlimited login attempts)
→ SSH on default port 22

your agent is as secure as you make it

the defaults ship with none of this

my full openclaw security guide below

by an ex-cisco engineer