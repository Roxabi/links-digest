@.claude/stack.yml
@~/.claude/shared/global-patterns.md

# roxabi-intel

Discord links digest with frontmatter MDs and dynamic gallery.

## Overview

Discord links digest: fetches pages from links shared in a Discord channel, converts each into a frontmatter markdown file, and renders a dynamic gallery. Runs as the `roxabi-intel` supervisor service (manage via `make intel`). Deploys to Cloudflare Pages.

## TL;DR

- **Project:** roxabi-intel
- **Before work:** Use `/dev #N` as the single entry point — it determines tier and drives the full lifecycle
- **Never** use `--force`/`--hard`/`--amend`
- **Always** use appropriate skill even without slash command

## Gotchas

<!-- Add project-specific gotchas here -->
