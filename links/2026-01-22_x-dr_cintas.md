---
title: "How to Run Claude Code Locally (100% Free & Fully Private)"
source: "https://x.com/dr_cintas/status/2014380662300533180"
date: 2026-01-22
tags: ["local AI setup", "Claude Code installation", "Ollama configuration", "privacy-focused development"]
platform: x
author: "@dr_cintas"
summary: "This tutorial explains how to configure Claude Code to run locally using Ollama for a free and private coding experience."
---
In this tutorial, you'll learn how to run Claude Code entirely on your own machine using local open-source models. This setup lets the AI read files, edit code, and run commands without sending any data to the cloud, no API costs, no tracking, and complete privacy.

🧰 Who is This For

Developers who want a private, offline AI coding agent

Power users who want Claude Code capabilities

Open-source fans experimenting with local LLMs

Anyone who wants an AI that can actually edit files and run terminal commands

Note: You can receive practical AI tutorials like this every morning in my free newsletter.

STEP 1: Choose Your Local “Brain” (Ollama)

Before running Claude Code, you need a local engine that can host AI models and support tool or function calling. Ollama handles this part.

Start by downloading and installing Ollama. Once installed, it runs quietly in the background on both Mac and Windows.

Next, you need to download a coding-focused model. There are a lot of open-source models you can choose from, and it also depends how powerful your machine is. My recommendation:

For high performance systems, pull a larger model like:
qwen3-coder:30b

If you’re on a lower-RAM machine, smaller options like:
gemma:2b or qwen2.5-coder:7b work well.

Once you pick one, open your terminal and download one by typing:

STEP 2: Install Claude Code

Now it’s time to install the Claude Code agent itself. This is what turns the model into an active coding assistant. Open your terminal and run the install command for your system.

On Mac or Linux, run: curl -fsSL https://claude.ai/install.sh | bash

On Windows, run: irm https://claude.ai/install.ps1 | iex

Once the installation finishes, verify everything worked by typing:

If you were previously logged into an Anthropic account, you may need to log out so Claude can switch to local mode.

STEP 3: Point Claude to Your Local Machine

This is the most important step. By default, Claude expects to talk to Anthropic’s servers. Here, you explicitly redirect it to your local Ollama instance.

First, tell Claude where Ollama is running by setting the base URL:

export ANTHROPIC_BASE_URL="http://localhost:11434"

Next, Claude still expects an API key, so you give it a dummy value:

export ANTHROPIC_AUTH_TOKEN="ollama"

Finally, you can also opt out of both telemetry and survey by setting:

export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1:

STEP 4: Launch Claude and Run a Real Test

Now you’re ready to use Claude Code for actual work.

Navigate to any project folder in your terminal and launch Claude with your selected model. For example:

claude --model qwen2.5-coder:7b

You should then see your local model pop up:

Once it’s running, try your prompt, For example:
“Add a hello world website”

You’ll see Claude read your files, modify the code, and execute terminal commands live, entirely on your machine.

No API calls. No cloud processing. Zero cost. Just a fully local AI coding agent working directly inside your project.