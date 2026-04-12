---
title: "nicobailon/pi-interactive-shell"
source: "https://github.com/nicobailon/pi-interactive-shell"
date: 2026-04-12
tags: []
platform: github
author: null
summary: "Pi coding agent extension that allows Pi to autonomously control interactive CLIs in an observable overlay. Full PTY emulation, no  tmux, token efficient. User can take over anytime."
---
# nicobailon/pi-interactive-shell

**URL:** https://github.com/nicobailon/pi-interactive-shell
**Description:** Pi coding agent extension that allows Pi to autonomously control interactive CLIs in an observable overlay. Full PTY emulation, no  tmux, token efficient. User can take over anytime.
**Language:** TypeScript
**Stars:** 373 | **Forks:** 26
**Last updated:** 2026-04-12

## README (excerpt)

<p>
  <img src="banner.png" alt="pi-interactive-shell" width="1100">
</p>

# Pi Interactive Shell

An extension for [Pi coding agent](https://github.com/badlogic/pi-mono/) that lets Pi autonomously run interactive CLIs in an observable TUI overlay. Pi controls the subprocess while you watch - take over anytime.

https://github.com/user-attachments/assets/76f56ecd-fc12-4d92-a01e-e6ae9ba65ff4

```typescript
interactive_shell({ command: 'vim config.yaml' })
```

Important: the `interactive_shell({...})` snippets in this README are tool calls made by Pi (or extension/prompt authors). End users do not type these directly into chat. As a user, ask Pi to run something (for example: "run this in dispatch mode") or use `/spawn`, `/attach`, and `/dismiss` commands.

## Why

Some tasks need interactive CLIs - editors, REPLs, database shells, long-running processes. Pi can launch them in an overlay where:

- **User watches** - See exactly what's happening in real-time
- **User takes over** - Type anything to gain control
- **Agent monitors** - Query status, send input, decide when done

Works with any CLI: `vim`, `htop`, `psql`, `ssh`, `docker logs -f`, `npm run dev`, `git rebase -i`, etc.

## Install

```bash
pi install npm:pi-interactive-shell
```

The `interactive-shell` skill is automatically symlinked to `~/.pi/agent/skills/interactive-shell/`.

**Requires:** Node.js. PTY support uses `zigpty` prebuilt binaries (no `node-gyp` toolchain required on supported platforms).

## Modes

| Mode | Agent waits? | How output reaches agent | Best for |
|---|---|---|---|
| **Interactive** (default) | Yes — blocks until exit | Tool return value | Editors, REPLs, SSH — when you need the result now |
| **Hands-free** | No | Poll with `sessionId` | Dev servers, builds — when you want to watch progress and send follow-up commands |
| **Dispatch** | No | Notification on completion via `triggerTurn` | Delegating tasks to subagents — fire and forget |
| **Monitor** | No | Notification on structured monitor trigger events | Watchers, logs, tests, and state checks — wake only when something specific happens |

**Interactive** — The overlay opens, user controls the session, agent waits for it to close. Use for editors (`vim`), database shells (`psql`), or any task where the agent needs the final result immediately.

**Hands-free** — The overlay opens but returns immediately. The agent polls periodically with `sessionId` to check status and get new output. Good for long-running builds or dev servers where you want to react mid-flight (send input, check logs, kill when ready).

**Dispatch** — Returns immediately. No polling. The agent gets woken up via `triggerTurn` only when the session completes (natural exit, timeout, quiet detection, or user kill). The notification includes a tail of the output. This is the default for delegating work to subagents. Add `background: true` to skip the overlay entirely.

**Monitor** — Returns immediately. No polling, no completion notification....