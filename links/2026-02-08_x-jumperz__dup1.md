---
title: "so, a mini update to our discord agent swarm.."
source: "https://x.com/jumperz/status/2020605533711949919?s=46"
date: 2026-02-08
tags: ["Discord agent swarm", "Webhook identity", "Bot customization", "AI team coordination"]
platform: x
author: "@jumperz"
summary: "A Discord agent swarm uses webhooks to give each agent a unique identity, creating a realistic team feel without changing core functions."
---
so, a mini update to our discord agent swarm..

instead of one bot face every time, we added webhooks so each agent has its own identity.

functionally nothing changed. still the same isolated sessions, still different agents spawning and working in parallel etc.. 

but it changed everything about how it feels.

instead of 7 agents posting through one bot account, now each one appears as their own person with their own name and avatar. 

luna looks like luna. john looks like john.

each agent session spawns fresh but their visual identity stays consistent through a webhook mapping file that reloads on every restart.

the agents were already separate underneath tho .. the webhook just makes that separation visible.

once you set up your webhooks, do these too so you don't lose them when something updates or breaks:

-------

>create one discord webhook per agent channel
>save all webhook URLs to a JSON file
>lock that file (chmod 600) and gitignore it
>write a posting script that reads the file and sends with custom username + avatar
>add agent identity to your channel system prompts so it survives restarts
>keep the bot as fallback if webhooks ever break
>chunk messages over 2000 chars in your script
>back up the JSON file somewhere outside your project

-------

that's it, now you have an actual team with faces, not a bot with split personalities, which is super cool tbh because identity is what makes coordination feel real.