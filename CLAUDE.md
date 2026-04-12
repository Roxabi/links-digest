@.claude/stack.yml
@~/.claude/shared/global-patterns.md

# roxabi-intel

Discord links digest with frontmatter MDs and dynamic gallery.

## Overview

Add project overview here.

## TL;DR

- **Project:** roxabi-intel
- **Before work:** Use `/dev #N` as the single entry point — it determines tier (S / F-lite / F-full) and drives the full lifecycle
- **Always** `AskUserQuestion` for choices — never plain-text questions
- **Never** use `--force`/`--hard`/`--amend`
- **Always** use appropriate skill even without slash command

### 1. Git

Format: `<type>(<scope>): <desc>` + `Co-Authored-By: Claude <model> <noreply@anthropic.com>`
Types: feat|fix|refactor|docs|style|test|chore|ci|perf
Never force/hard/amend. Hook fail → fix + NEW commit.

## Gotchas

<!-- Add project-specific gotchas here -->
