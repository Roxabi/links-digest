---
title: "The 5-Minute Setup That Gives AI Agents Full Access to Google Workspace - A Must Have for OpenClaw "
source: "https://x.com/misbahsy/status/2029628752456786109?s=46"
date: 2026-03-05
tags: ["Google Workspace CLI", "AI agent tools", "OpenClaw support", "Google Discovery Service"]
platform: x
author: "@MisbahSy"
summary: "Google engineers released gws, a CLI tool providing AI agents with dynamic, direct access to all Google Workspace APIs via structured JSON."
---
Google engineers just quietly released something that the AI agent community is super excited about.

It's called gws (Google Workspace CLI), and it's a single command-line tool that gives AI agents direct access to Gmail, Google Drive, Calendar, Sheets, Docs, Slides, Chat, Tasks, Meet, Forms, Keep, Classroom, Admin, and basically every Google Workspace API that exists. All through structured JSON output. All agent-ready out of the box.

And here's the part that really caught my eye: it ships with 100+ agent skills and has native OpenClaw support built right into the README.

Let's break down why this matters and how you can start using it today.

What Is gws and Why Should You Care?

For non-technical wizards, `gws` is a command-line tool that lets AI agents directly control your Google Workspace apps. Think of it like giving your AI agent superpowers to manage your email, calendar, files, and more.

And for the techies (skip to the next section if you're not one), `gws` is a CLI built in Rust that wraps every Google Workspace API into clean, composable commands. But the clever part is how it actually works. Here's the problem most developer tools run into: they ship a fixed list of commands, and every time Google adds something new, someone has to manually update the tool, cut a new release, and hope everyone upgrades. It's a maintenance treadmill that never ends. Most Google Workspace wrappers you've seen are already out of date by the time you install them.

gws solves this in a fundamentally different way. Instead of hardcoding commands, it talks directly to something called the Google Discovery Service. Think of this as Google's own live catalog of every single action available across all their Workspace apps. Every API, every method, every parameter. Google maintains this catalog themselves, and it's always current.

When you run gws, the first thing it does is pull this live catalog, and then it builds its entire command structure on the fly from whatever Google says is available right now. So if Google ships a new Sheets feature at 2pm today, your CLI already supports it at 2:01pm. No update. No new version. No waiting for a maintainer to catch up. The tool literally cannot fall behind because it's reading from the source of truth every time. This is a design philosophy more tools should adopt. Don't maintain a copy of someone else's API surface. Just read it live and build from it.

Now, why does this matter for agents specifically? Because every single response comes back as structured JSON. Not HTML. Not formatted text. Not something your agent has to squint at and try to parse. Clean, predictable, machine-readable data that an AI agent can immediately reason about and act on. That's the difference between an agent that kind of works and one that works reliably.

Getting Started: Your First 5 Minutes

If you want to try this right now, here's the quickest path below. Just make sure you have the gcloud CLI installed first, if not it's a simple brew install --cask gcloud-cli on macOS.

That's it. Three commands and you're talking to Google Workspace from your terminal.

These are the screens you'll probably see right after gws auth setup:

Cool thing is you can start with one account and later on add multiple accounts (work, personal, etc) and your agent can use them based on the context.

Next is the GCP project setup. You can either create a new project or use an existing one. And the all of that is done via the CLI itself. How cool is that?

Then you enable the APIs you need. Again, all via the CLI. OMG I'm in love!

Some of you might hit this manual OAuth client setup. Don't worry, it's straightforward.

Right after this you're all set with the setup. Now you can login with gws auth login and give your agent the right ammo to work with.

If you have a separate email for your agent, just YOLO it and give it Full Access!

And in case you are logging in with your personal/work email, give it Limited Access to begin with. You can always change it later.

And that's it! You're all set.

Now let's look at how to plug this into your agent setup.

100+ Agent Skills, Right Out of the Box

This is where things get really interesting for the OpenClaw and Claude Code communities.

The repo ships with over 100 SKILL.md files organized into four categories. If you're not familiar with the SKILL.md format, it's the emerging standard for giving AI agents structured, composable capabilities. Think of skills like apps but for agent knowledge and tool access.

Here's how the skills are organized:

Service Skills (25+)

One skill per Google Workspace API. These are your building blocks:

gws-drive for managing files, folders, and shared drives

gws-gmail for sending, reading, and managing email

gws-calendar for managing calendars and events

gws-sheets for reading and writing spreadsheets

gws-docs for reading and writing Google Docs

gws-slides for presentations

gws-tasks for task lists

gws-chat for Google Chat spaces and messages

gws-people for contacts and profiles

gws-admin for managing users, groups, and devices

gws-classroom for classes, rosters, and coursework

gws-forms for Google Forms

gws-keep for Google Keep notes

gws-meet for conference management

gws-vault for eDiscovery

gws-apps-script for managing Apps Script projects

And there are more covering Cloud Identity, Alert Center, Group Settings, Licensing, Reseller, and even Model Armor for safety filtering.

Persona Skills (10 Pre-Built Agent Roles)

This is the part that really stands out. Google created 10 ready-to-use persona bundles that define complete agent roles:

Executive Assistant - manages schedules, inbox, and communications

Project Manager - coordinates projects, tracks tasks, schedules meetings

HR Coordinator - handles onboarding, announcements, employee communications

Sales Ops - manages sales workflows, tracks deals, schedules calls

IT Admin - administers users, monitors security, configures Workspace

Content Creator - creates, organizes, and distributes content

Customer Support - manages tickets, responds to issues, handles escalation

Event Coordinator - plans events, manages invitations, handles logistics

Team Lead - runs standups, coordinates tasks, manages team communication

Researcher - organizes research, manages references, handles collaboration

Each persona bundles together the right service skills, helper commands, and workflow patterns for that specific role. You don't have to figure out which combination of Gmail + Calendar + Drive + Sheets skills your agent needs. Just give it the persona and it knows what to do.

Helper Skills

These are shortcut commands for the most common operations. Things like gws-drive-upload for quick file uploads, gws-gmail-send for sending emails, and gws-modelarmor-sanitize-prompt for cleaning up prompts before they hit your agent.

Recipe Skills (50 Curated Workflows)

Multi-step task sequences with real commands baked in. Examples include auditing externally shared Drive files, sending personalized emails from Sheets data, and other common productivity automations. These are the "copy-paste and go" workflows that save hours of prompt engineering.

How to Use This With OpenClaw

Google literally included OpenClaw setup instructions in the README. This isn't a community hack or a workaround. It's built-in, first-class support.

Here's how to get started:

Option 1: Symlink All Skills (Recommended for Development)

This keeps everything in sync with the repo. When Google updates the skills, you get the updates automatically.

Option 2: Copy Specific Skills

Option 3: Use the Skills CLI

The gws-shared skill is especially smart here. It includes an install block that auto-installs the CLI via npm if gws isn't already on your PATH. So your OpenClaw agent can bootstrap itself. It checks for the tool, installs it if needed, and starts working. No manual setup required.

How to Use This With Claude Code

If you're a Claude Code user (and honestly, this is where I've been spending most of my time lately), there are a couple of approaches to bring gws into your workflow.

Approach 1: Direct CLI Access

Claude Code can execute shell commands. Once you have gws installed and authenticated, Claude Code can call it directly:

The structured JSON output means Claude Code can parse the results, reason about them, and take follow-up actions without any custom tooling.

Approach 2: MCP Server

This is the more powerful approach. gws includes a built-in MCP (Model Context Protocol) server that exposes Workspace APIs as structured tools:

You can configure this in your MCP client settings:

This works with Claude Desktop, VS Code, Gemini CLI, and any MCP-compatible client. Each service adds roughly 10 to 80 tools, so keep the list focused on what you actually need to stay under tool limits.

Approach 3: Add Skills to Your Project

If you're working on a Claude Code project and want it to understand Google Workspace operations, you can add the relevant SKILL.md files to your project context. This gives Claude Code the procedural knowledge to construct the right gws commands for any task you throw at it.

Model Armor: Built-In Agent Safety

Here's something that doesn't get enough attention. The repo includes integration with Google Cloud Model Armor for response sanitization.

What does that mean in practice? When your agent reads data from Gmail or Drive, that data could contain prompt injection attacks. Someone could craft an email specifically designed to manipulate your agent's behavior. Model Armor scans API responses before they reach your agent and filters out potentially malicious content.

You can run it in warn mode (flags suspicious content but still returns it) or block mode (strips it out entirely). This is especially important when agents are operating autonomously on email and document content they've never seen before.

For context, Cisco's AI security team found that 26% of the 31,000+ skills on ClawHub contain vulnerabilities, and SecurityScorecard reported that 63% of exposed OpenClaw instances are misconfigured. Agent security isn't a theoretical problem. It's happening right now. Having safety filtering built into the data pipeline is a smart move from Google.

Why This Tool Matters

Well, here's a taste of all the cool things your agent can do with gws:

Gmail: Search, read, send, and organize email

Calendar: View your schedule, create and update events

Drive: Upload, download, organize, and share files

Sheets: Read, write, and create spreadsheets

Docs: Create and write documents

Chat, Meet, Forms, and more

Notice the pattern. Every action is one line. And the + helper commands (like +send, +upload, +agenda, +triage, +read, +append, +write) handle all the messy encoding and formatting that would normally take 10 lines of boilerplate. Your agent doesn't need to know about RFC 2822 email formatting or base64 encoding. It just says what it wants to do and gws handles the rest.

What's Next

This architecture is solid, the skill coverage is impressive, and the fact that they built OpenClaw compatibility from day one tells you a lot about where they think the agent ecosystem is headed.

We'll be diving deeper into specific use cases in upcoming articles. The persona skills alone deserve their own deep dive, and there are 50 recipe workflows worth exploring in detail. If you're building on OpenClaw, Claude Code, or any agent platform, this is one of those tools you'll want to have in your toolkit.

The agent economy is getting its infrastructure. And it's happening faster than most people realize.

Have questions or want to share what you're building with gws? Drop a comment below. Also, check out what we're building at Clawable.ai.