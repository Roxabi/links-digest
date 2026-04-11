---
title: "Claude Lets You Run Your Computer From Your Phone "
source: "https://x.com/tomcrawshaw01/status/2034254381995139403"
date: 2026-03-18
tags: ["Anthropic", "Claude", "Mobile", "Remote Control", "Productivity"]
platform: x
author: "@tomcrawshaw01"
summary: "Anthropic introduced Dispatch and Remote Control, new features that enable users to assign tasks and manage active Claude Code sessions on their desktops remotely via their mobile phones."
---
Two new Anthropic features just removed the one thing holding AI back: you had to be at your computer to use it.

In 2026, Every Time I Wanted Claude to Do Something Real, I Had to Be at My Computer to Do It

In 2026, I've been using Claude seriously for months, and the bottleneck has always been the same.

The tasks worth doing (pulling data from local files, running Claude Code against a real codebase, working with apps already configured on my desktop) all required me to be sitting at it.

Claude on my phone was fine for quick questions. For anything real, I had to wait.

The specific friction was this: I'd Wispr Flow an idea into Claude Code on my phone, ask it to map out a plan, and Claude would do exactly that. A full breakdown, ready to run.

But I couldn't execute any of it until I was back at my desk. I had the plan. I just couldn't start it.

That's what makes this week's announcements different.

Anthropic Didn't Make Claude Better on Mobile. They Made Your Desktop Do the Work Instead.

Instead of improving Claude on your phone, Anthropic shipped two features that split Claude into two layers.

Your phone is the interface. Your desktop is the engine.

The work still happens on your computer. You just no longer need to be sitting at it to get things started.

Dispatch Lets You Assign Tasks From Your Phone and Come Back to Finished Work

The first is Dispatch, which lives inside Cowork.

You assign a task from your phone, and Claude gets to work on your desktop with access to your real local files and everything you've already connected in Cowork. When it finishes, you get the result as a message.

Ask it to pull data from a local spreadsheet and compile a summary, or tell it to search your Slack and email and draft a briefing from what it finds.

You don't set anything up separately for mobile. Everything you've already configured in Cowork is available from your phone.

Remote Control Lets You Continue an Active Claude Code Session From Anywhere

The second feature is built for Claude Code.

Start a session at your desk, get halfway through something, and Remote Control lets you pick it up from your phone. The session keeps running on your machine the entire time.

Your filesystem, MCP servers, tools, and project configuration all stay exactly where they are. Nothing moves to the cloud.

The conversation stays in sync across every connected device, so you can send messages from your terminal, your browser, and your phone interchangeably.

If your laptop sleeps or your network drops, the session reconnects automatically when your machine comes back online.

The Two Features Work Differently, But the Shift Is the Same

Dispatch runs on a single continuous thread — Claude retains context from every previous task you've assigned.

Remote Control syncs a running Claude Code session, where all connected surfaces share the same live conversation.

One caveat for both: your desktop needs to be on and Claude needs to be running.

Before: map a plan on your phone, wait until you're back at your desk, open Claude, execute it yourself.

Now: continue that session from wherever you are, send the next message, come back to the output.

The gap between idea and finished work used to require you in the middle of it.

Your Desktop Is the Engine Now. You Just Don't Have to Sit at It to Run It.

Your desktop hasn't changed, and neither has Cowork or Claude Code.

What's changed is that your phone can now act as the interface for all of it. The compute still runs on your machine. You just access it from wherever you are.

Setting Up Dispatch

Download the latest Claude Desktop and update Claude on your phone.

Open Cowork on either device, click Dispatch in the left panel, and follow the setup steps.

Dispatch is rolling out to Max plans today and Pro plans tomorrow.

Setting Up Remote Control

Navigate to your project directory and run claude remote-control in your terminal.

Press spacebar to show a QR code, scan it with the Claude mobile app, and your phone is connected to that session.

From inside an existing Claude Code session, /remote-control does the same thing without leaving your terminal.

Remote Control is available on all plans and requires Claude Code v2.1.51 or later — check yours with claude --version.

I've watched a lot of AI updates ship. Most change what Claude knows or how it reasons. This one changes where it works, and that's a different kind of upgrade.

30 Day Claude Code Challenge

I'm running a 30-Day Claude Code Challenge starting April 1st. 20 spots.

You don't watch videos and hope something sticks. You build inside Claude Code from day one, and by the end you have a working script, a deployed web app with a real URL, and a live agent running on a schedule.

It runs across three phases. Investigate (identify the highest-value thing to build), Build (process real data end to end), Ship (deploy something you can show a client or a hiring manager).

Four live group calls run alongside it where we build together and unblock anything stuck.

If you're interested DM me and I'll send you the link to the doc.