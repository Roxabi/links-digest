---
title: "Claude Code Guide for Designers"
source: "https://x.com/felixleezd/status/2018728056249254377?s=46"
date: 2026-02-03
tags: ["claude-code", "ai-tools", "designers", "web-development", "coding-agent"]
platform: x
author: "@felixleezd"
summary: "A comprehensive guide teaching designers how to use Claude Code, an AI coding agent, to build and deploy web projects without traditional programming knowledge."
---
Claude Code is the highest leverage skill you can learn this year.

The future of design is here. I've written a full guide for this.

Story time...

I built my personal website, with an AI chat that answers questions about my work, in 48 hours. Three days later, I shipped a growth design tool.

I'm not a developer. I'm a designer. A year ago, I couldn't ship a single line of code without an engineer. Now I deploy products on weekends.

Same person, different tool (no more Figma, kinda)!

This is the complete guide to using Claude Code as a designer -> step by step, command by command.

What is Claude Code?

Claude Code is a coding agent. You give it instructions in plain English, and it writes code for you. You prompt: "Create a landing page with a hero section, three feature cards, and a footer." It executes.

Or something like. "Add an AI chat widget that answers questions about my portfolio." It executes. You don't need to understand syntax. You need to understand what you're building.

Imho, this is even better than Cursor or anything else out there (as of today).

> things I've built

⭐️ Project 1: Tetris game

Okay, this one is insane: I built a Tetris game using only Figma MCP connected to FigJam, then back to Claude Code. I did not even design or touch a single line of code.

No joke, this one blew me away (see my reaction at 7s). 😂

⭐️ Project 2: Growth design tool

An internal tool for analyzing metrics and suggesting design experiments. Database-backed. User authentication. AI-powered recommendations. 3 days. Working product. Live on the internet.

How insane, got over 500 users now!

Now, let's get you up to speed on these.

> step 1: install Claude Code

On Mac: Open Terminal (search "Terminal" in Spotlight) and run:

If you don't have npm, install Node.js first from https://nodejs.org

Verify installation: Type ->

Claude Code should launch. You'll see a text interface where you can start typing instructions.

(NEW) Alternatively, you can download the desktop mac app for Claude Code as per video shown below. You’ll need an Anthropic account (sign up at claude.ai if you don’t have one). The link to download is here.

> step 2: basic terminal commands

Claude Code runs in the terminal. Here's what you need to know:

That's it. You don't need anything more than this to get started.

> step 3: create your first project

Create a project folder (aka directory):

Now you're inside Claude Code, in your project folder.

Start with a plan ALWAYS (critical):

Adjust if needed:

Implement:

Implement this project according to plan.md. Start with the HTML structure, then add CSS styling.

Watch as files appear: index.html, styles.css, images/.

Preview locally: How do I preview this in my browser?

For a local server:

Open http://localhost:3000 in your browser.

> step 4: iterate through prompts

This is where designers have an advantage. You already know how to give feedback.

Styling:

Responsiveness:

Functionality:

Debugging: Each prompt → code change → refresh browser. The loop is fast.

> step 5: commit (aka save) to GitHub

Create a GitHub account: Go to https://github.com and sign up (free).

Create a repository: Click + → New repository

Name it (e.g., my-portfolio)

Keep it Public or Private

Don't initialize with README

Click Create repository

Copy the repository URL.

Connect and push:

In Claude Code:

Initialize git in this project and connect it to my GitHub repository: https://github.com/yourusername/my-portfolio.git

Or manually:

Create documentation:

Create a README.md that explains what this project is and how to run it locally.

Create a claude.md file that describes the project architecture and context for future sessions.

Your code is now saved and versioned.

> step 6: go live/deploy to Vercel

Create a Vercel account: Go to https://vercel.com and sign up with GitHub.

Option 1 Vercel dashboard:

Click Add New → Project

Import your GitHub repository

Click Deploy

Option 2 through Claude Code:

Deploy this project to Vercel.

Result: You get a live URL like my-portfolio-abc123.vercel.app NOTE: Your site is on the internet. Every future push to GitHub auto-deploys.

> step 7: add your custom domain

In Vercel:

Go to Settings → Domains

Add your domain (e.g., yourname.com)

Vercel shows DNS records to add

Update DNS at your domain provider:

Wait 5-30 minutes. Your site loads on your custom domain.

> step 8: build into a web app (advanced)

Static sites are steps 1-7. Now let's add users, data, and AI.

Research prompt:

I want to expand this portfolio into a web app with:
- Google sign-in authentication
- An AI chat widget that answers questions about my work
- A comment section where signed-in users can leave messages

Research the best approach and create an implementation-plan.md with:
1. Services needed (auth, database, AI)
2. Architecture overview
3. Security considerations
4. Step-by-step implementation phases

Set up environment variables:

Create a .env file for storing API keys. Also create a .gitignore that excludes .env from GitHub.

Your .env file:

🚨 Never commit this file.

> step 9: supabase (database + auth)

Create a project:

Go to https://supabase.com

Create new project

Go to Settings → API

Copy Project URL and anon key

Enable Google sign-in:

In Supabase: Authentication → Providers → Google → Enable

Go to https://console.cloud.google.com

Create project → APIs & Services → Credentials → Create OAuth Client ID

Copy Client ID back to Supabase

> step 10: add ai features with OpenAI

Get API key:

Go to https://platform.openai.com

Create an API key

Store securely in Supabase:

Go to Settings → Edge Functions → Add Secret

Name: OPENAI_API_KEY

Value: your key

This keeps the key server-side, never exposed to users.

Implementation prompt:

Implement the web app according to implementation-plan.md.

Use:
- Supabase for auth and database (credentials in .env)
- OpenAI for the chat feature (key stored in Supabase Edge Functions)
- Google sign-in only

Start with authentication, then add the AI chat, then the comment system.

Then redeploy!

quick ref: prompts by category

Planning:

Implementation:

Adding features:

Debugging (good to include screenshot of error):

And you're all set! 🎉

This article is based on my full Vibe-Coding course (if you'd like to support) ⭐️. It includes:

Installation walkthroughs (Mac + Windows)

Interface orientation

First project tutorial

GitHub + version control

Vercel deployment

Custom domains

Supabase + OpenAI integration

Bonus chapters on AI agents and Figma MCP (coming soon)

⭐️ Get the free guide: https://adplist.notion.site/cursor-for-designers or want to build production apps? 🏛️ Apply to join our community (AI designer school) as a founding member (full courses available): https://adplist.org/vibe-code-designers

Final Thought... I used to feel like half a builder. Like my ideas needed someone else to become real. Not anymore.

It's time to build, designers.

Thank you for reading.

🔖 Bookmark this to come back again

🔄 If you find this helpful, let's repost or forward it and share your thoughts. Because more designers can learn to build.