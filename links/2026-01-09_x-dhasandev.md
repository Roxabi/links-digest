---
title: "How to Wrap the Claude CLI for Your Agentic Apps"
source: "https://x.com/dhasandev/status/2009529865511555506?s=46"
date: 2026-01-09
tags: ["Claude CLI wrapper", "agentic applications", "print mode usage", "API authentication", "JSON schema output"]
platform: x
author: "@dhasandev"
summary: "The article explains how to wrap Claude CLI's print mode for agentic apps using various input/output formats, tools configuration, and permission modes."
---
In today's article, I'll explain how to wrap the Claude CLI properly for your agentic apps.

Context

For those who don't know, you can no longer use your Claude subscription to use opencode and other third party apps. The reason for this can be found in their Agent SDK docs:

Unless previously approved, we do not allow third party developers to offer Claude.ai login or rate limits for their products, including agents built on the Claude Agent SDK. Please use the API key authentication methods described in this document instead.

Many harnesses/orchestrators like @opencode and @clawdbot have been slammed with this error as a result:

This means the oauth token generated in Claude Code via `/login` and `claude setup-token` no longer work outside of claude code. So, you have to pursue an alternative.

Wrapping the CLI

This all comes down to CC's "print" mode. It's run via `claude -p` or `claude --print` and it is a one-shot invocation of the CLI that takes a boatload of parameters. In this article, I'll outline the different flags you can use for various applications.

The State Machine

Claude CLI's print mode can be thought of as a state machine with multiple dimensions:

Input/Output Format Matrix

Gotchas

`--output-format stream-json` requires `--verbose` or you'll get an error.

`--input-format stream-json` requires `--output-format stream-json`. You can't mix stream input with text output.

Before we get into it: This is all derived from our implementation at trysquad.ai, where we're developing robust agent verification and coordination techniques to enable engineers to scale up from 5 parallel claudes to 500. Sign up for the waitlist now for early access! Experiments and findings available at:

https://gist.github.com/danialhasan/abbf1d7e721475717e5d07cee3244509

Basic Usage Patterns

Getting Data IN: Input Methods

There are 5 ways to feed a prompt into `claude -p`:

1. Command Line Argument (Most Common)

2. Stdin Pipe (Pipe content from another command:)

3. Stdin Redirect (Read from a file:)

Here-Doc (Multi-line Prompts, perfect for complex prompts with formatting)

5. Stream-JSON Input (Advanced, for programmatic, real-time input)

Note: Stream input REQUIRES stream output (bidirectional only).

Combining Input Methods

You can combine argument + stdin for context + instruction:

Getting Data OUT: Output Methods

There are 3 output formats controlled by `--output-format`:

1. Text Output (Default, human-readable, plain text)

2. JSON Output

Structured response with full metadata:

Returns:

Extract fields with jq:

3. Stream-JSON Output (Real-Time)

For live UI updates - requires `--verbose`:

Emits multiple JSON events (one per line):

Parse in real-time:

Or in Node.js:

Input/Output Combination Matrix

Structured Output with JSON Schema

This is the killer feature for data extraction apps:

Key Discovery #3: The response includes a `structured_output` field separate from the text `result`:

This is perfect for:

Data extraction pipelines

Form filling automation

API response formatting

Type-safe agentic outputs

Literally anything

Tool Configuration

You have quite a few options for tool configuration. By default it uses its native tools like Glob, Grep, Search, etc; but you can add custom tools,  remove all tools, or some combination of the two. You can get real granular with this.

Disable All Tools (Pure LLM)

For chat-only applications where you don't want file access or command execution:

Specific Tool Whitelist

Enable only the tools you need.

Pattern-Based Allow/Deny

Fine-grained control with patterns:

Permission Modes

This is critical for autonomous execution:

For CI/CD Pipelines

I'm supposed to put a warning here saying "be careful with bypassPermissions and only use it in a sandbox with no internet access!!" but honestly bro? Fuck it. Bypass the permissions; as long as you set the guardrails right Claude won't be able to do some crazy shit like delete your google drive. like antigravity did. Oh well!

There's also a convenience flag:

Session Management

Ephemeral Sessions (No Disk Storage)

For stateless microservices:

Fixed Session ID (Multi-Turn Conversations)

Maintain context across calls:

Custom System Prompts

Replace Entirely

Append to Default (Recommended)

Preserves Claude Code's capabilities while adding custom behavior:

Custom Agents

Define personas inline:

Model Selection

Basic Model Choice

Fallback for Reliability

Auto-fallback when primary model is overloaded:

Bidirectional Streaming (Advanced)

For real-time interactive applications:

The `--replay-user-messages` flag echoes user messages back with `"isReplay": true` for acknowledgment tracking.

Input format:

Putting It All Together

Production Agentic Wrapper

Chatbot Wrapper

Data Extraction Pipeline

Quick Reference

Gotchas

1. Stream-json requires --verbose - Won't work without it

2. Stream input requires stream output - Can't mix formats

3. MCP tools load regardless - Use `--strict-mcp-config` to disable

4. bypassPermissions must be used responsibly - set your guardrails!

5. JSON schema output is separate - Look for `structured_output` field

6. Context caching reduces cost - First run is expensive, subsequent runs cheaper as long as you don't blow up the KV cache at the start using a dynamic timestamp or something.

The Claude CLI's print mode is a powerful primitive for building agentic applications. By understanding the state machine of input/output formats, permission modes, and tool configurations, you can build everything from simple chatbots to fully autonomous coding agents.

The key insight is that `claude -p` isn't just a CLI wrapper - it's a full-featured agent runtime that happens to be accessible via command line. Use it wisely.

---

This is all derived from our implementation at trysquad.ai, where we're developing robust agent verification and coordination techniques to enable engineers to scale up from 5 parallel claudes to 500. Sign up for the waitlist now for early access!

Experiments and findings available at: https://gist.github.com/danialhasan/abbf1d7e721475717e5d07cee3244509

Claude Code version: 2.1.2 | Tested: 2026-01-08