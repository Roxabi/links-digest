---
title: "Cocoon-AI/architecture-diagram-generator"
source: "https://github.com/Cocoon-AI/architecture-diagram-generator"
date: 2026-04-11
tags: []
platform: github
author: null
summary: "Generate beautiful dark-themed system architecture diagrams as standalone HTML/SVG files. Works as a Claude AI skill."
---
# Cocoon-AI/architecture-diagram-generator

**URL:** https://github.com/Cocoon-AI/architecture-diagram-generator
**Description:** Generate beautiful dark-themed system architecture diagrams as standalone HTML/SVG files. Works as a Claude AI skill.
**Language:** HTML
**Stars:** 89 | **Forks:** 6
**License:** MIT License
**Last updated:** 2025-12-22

## README (excerpt)

# Architecture Diagram Generator

**Need an architecture diagram? Get AI to build you one.**

Use [Claude.ai](https://claude.ai) with this special skill to generate professional architecture diagrams in seconds. Describe your system, and Claude creates a beautiful, dark-themed diagram as a standalone HTML file you can open in any browser.

- **No design skills needed** — just describe your architecture in plain English
- **Iterate quickly** — ask Claude to add components, change layouts, or update styles
- **Share easily** — output is a single HTML file, no special software required

![Version](https://img.shields.io/badge/version-1.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Claude](https://img.shields.io/badge/Claude-Skill-orange)

## 🚀 Quick Start (3 Steps)

### Step 1: Install the Skill

> ⚠️ Requires Claude Pro, Max, Team, or Enterprise plan

1. Download [`architecture-diagram.zip`](architecture-diagram.zip)
2. Go to [claude.ai](https://claude.ai) → **Settings** → **Capabilities** → **Skills**
3. Click **+ Add** and upload the zip file
4. Toggle the skill on

📚 Need help? See the [full installation guide](#-installation) below.

### Step 2: Get Text that Describes Your Architecture

You just need a text description of your system. Pick whichever works for you:

**Option A: Have AI analyze your codebase**

Open your code in Cursor, Claude Code, Windsurf, or ChatGPT and ask:

```
Analyze this codebase and describe the architecture. Include all major
components, how they connect, what technologies they use, and any cloud
services or integrations. Format as a list for an architecture diagram.
```

**Option B: Write it yourself**

Just list your components and how they connect:

```
- React frontend talking to a Node.js API
- PostgreSQL database
- Redis for caching
- Hosted on AWS with CloudFront CDN
```

**Option C: Ask for a typical architecture**

Don't have a specific system? Ask Claude for a starting point:

```
What's a typical architecture for a SaaS application?
```

### Step 3: Generate Your Diagram by Asking Claude to Use the Skill 

Take the output from Step 2 and paste it into [Claude](https://claude.ai) (with the Architecture Diagram Generator skill installed):

```
Use your architecture diagram skill to create an architecture diagram from this description:

[PASTE YOUR ARCHITECTURE DESCRIPTION HERE]
```

That's it! Claude will generate a beautiful HTML file you can open in any browser.

Then!  You can iterate simply by using chat.   Ask Claude:  Please update XYZ to see your diagram update in real time.  You can ask Claude to fix any issues you have with the diagram as well.  

---

### Example Prompts for Common Scenarios

**For a web app:**

```
Create an architecture diagram for a web application with:
- React frontend
- Node.js/Express API
- PostgreSQL database
- Redis cache
- JWT authentication
```

**For AWS serverless:**

```
Create an architecture diagram showing:
- CloudFront CDN
- API Gateway
- Lam...