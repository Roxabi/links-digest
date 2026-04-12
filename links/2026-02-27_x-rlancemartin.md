---
title: "Give Claude a computer"
source: "https://x.com/rlancemartin/status/2027450018513490419?s=46"
date: 2026-02-27
tags: ["programmatic tool calling", "context window optimization", "Claude AI capabilities", "computer use agents"]
platform: x
author: "@RLanceMartin"
summary: "Programmatic tool calling lets Claude write code to orchestrate tools directly, improving efficiency by keeping intermediate data out of the context window."
---
TL;DR – Programmatic tool calling (PTC) is an interesting capability in Claude Opus/Sonnet 4.6. Instead of making tool calls that each round-trip through Claude's context, Claude writes code that can orchestrate tool calls directly inside a container. Intermediate tool results return to the code, not Claude’s context window. This reduces token usage and improves performance on multi-step tasks like search. Opus 4.6 with PTC recently scored #1 on LMArena’s search benchmark. See our docs to learn more about PTC and our new web search tool that uses PTC by default.

Computer use is one of Claude’s most central capabilities. Just giving Claude a bash tool opens up a broad action space and leads to a common question: is bash all you need? And how to decide what other tools to give an agent?

Actions are how Claude interacts with the world. Tools are a way to declaratively specify the actions that Claude can take. The API lets you add tools by giving Claude a tool name, description, and input arguments.

If Claude wants to call a tool, it will respond with a JSON object of tool arguments to run. A tool handler (e.g., MCP server, code you write, etc) runs the tool and passes back context. If you run this in a loop, you have an agent. For example, the bash tool produced bash commands by generating a JSON object with the command. It is passed to a bash tool handler to execute:

When to use tools

Claude with a bash tool running in a loop is a computer-use agent. This is central to Claude Code. But Claude Code doesn’t just use bash. It uses tools as a control surface around certain actions. See @trq212's breakdown on these points. Promoting an action to a tool can make sense in a few cases:

UX:  @trq212 talks about the AskUserQuestion tool. This examples shows that tools are useful in cases where specific actions need to be caught and rendered to the user in a particular way.

Guardrails. Some actions need guardrails. For example, a file edit tool can run a staleness check to verify that the file hasn't changed since the model last read it.

Concurrency control. Sometimes it's useful to group actions by concurrency safety (e.g., read-only tools can run in parallel).

Observability. It can be useful to isolate specific actions for logging (e.g., measuring latency or token usage).

Autonomy. You may want to group actions by autonomy-level. If the harness can undo an action, it can approve the action more freely.

The problem with tools

Tools trade-off control with composability. Consider three actions as tool calls. The context from each tool call is returned back to Claude. Each round trip costs latency, serializes the tool result into context (e.g., it will pass thousands of rows even if the next step only needs five), and introduces a reasoning step. The composition tax grows with the number of actions.

Programmatic tool calling

Claude is developing a capability that unites the composability of code with the control surface of tools. Claude can perform programmatic tool calling (PTC, see docs here): you can define tools, as usual. But rather than calling them individually, Claude can compose them as functions and run them in a code execution container. The output of each function returns to the container rather than to Claude’s context window.

When the code calls a tool (e.g., await web_search(query)) the container pauses. The call crosses the sandbox boundary as a typed tool-use event. It is fulfilled just as if the model directly called the tool (e.g., via a handler, an MCP server etc). But the result returns to the running code, not to Claude's context window. The code processes it following the control flow that Claude specified (e.g., calls another tool, filters the data, accumulates results). Only the final output reaches Claude.

With Opus 4.6, we’ve seen gains in token efficiency and performance on non-coding evals (e.g., BrowseComp and DeepsearchQA for web search) with PTC. For example, rather than pulling 50 raw search results into context for Claude to reason over, the code can parse, filter, and cross-reference results programmatically. This keeps what's relevant and discards the rest (e.g., dynamic filtering). Across BrowseComp and DeepsearchQA, it improved accuracy by an average of 11% while using 24% fewer input tokens. Opus 4.6 with PTC is currently #1 in LMarena’s Search Arena.

With these gains in mind, PTC is now built-into to the web search tool on the API to boost performance and save token when using search:

PTC is a way to get the benefit of code execution (e.g., composability) while preserving the control surface of tools: tool implementations run on your side of the sandbox, not inside it. The tool handlers still sit in the middle of every call as a control surface, able to inspect, reject, log, or queue for human approval. But it allows Claude to fluently orchestrate actions in code.