# links-digest Makefile
#
# Usage:
#   make digest          # Scan last 24h
#   make digest H=72     # Scan last 72 hours
#   make digest D=7      # Scan last 7 days
#   make digest-all      # Scan entire history
#   make build           # Build index + validate
#   make deploy          # Deploy to Cloudflare Pages
#   make open            # Open gallery in browser
#   make start           # Start local server on port 8082
#   make stop            # Stop local server
#   make status          # Check server status

PROJECT_NAME ?= links-digest
CF_PROJECT   ?= links-digest
CF_ACCOUNT   ?= b5e90be971920ce406f7b679c4f1cd33
LINKS_PORT   ?= 8082

SUPERVISOR_HUB  ?= /home/mickael/projects
-include $(SUPERVISOR_HUB)/hub.mk

.PHONY: digest digest-all build deploy open clean start stop reload status logs errlogs

# ── Digest ────────────────────────────────────────────────────────────────────

digest:
	uv run python digest.py --hours $(or $(H),24)

digest-all:
	uv run python digest.py --all

digest-%:
	@args=$*; \
	uv run python digest.py --$${args}

# ── Build ─────────────────────────────────────────────────────────────────────

build:
	@echo "Building gallery..."
	@ls links/*.md 2>/dev/null | wc -l | xargs -I {} echo "Found {} MD files"
	@echo "Syncing to public/links/..."
	@mkdir -p public/links && cp links/*.md public/links/ 2>/dev/null || true
	@echo "Generating manifest.json..."
	@cd links && ls -1 *.md 2>/dev/null | jq -Rs 'split("\n") | map(select(length > 0))' > manifest.json
	@cp links/manifest.json public/links/
	@echo "Done."

# ── Deploy ────────────────────────────────────────────────────────────────────

deploy: build
	@echo "Deploying to Cloudflare Pages: $(CF_PROJECT)..."
	CLOUDFLARE_ACCOUNT_ID=$(CF_ACCOUNT) npx wrangler pages deploy public --project-name=$(CF_PROJECT) --branch=main --commit-dirty=true

# ── Dev ───────────────────────────────────────────────────────────────────────

open:
	xdg-open public/index.html 2>/dev/null || open public/index.html

# ── Clean ─────────────────────────────────────────────────────────────────────

clean:
	rm -rf links/*.md links/manifest.json public/links/*.md public/links/manifest.json .digest_state.json

# ── Server ──────────────────────────────────────────────────────────────────────

start:
	$(HUB_SVC) links-digest start

stop:
	$(HUB_SVC) links-digest stop

reload:
	$(HUB_SVC) links-digest reload

status:
	$(HUB_SVC) links-digest status

logs:
	$(HUB_SVC) links-digest logs

errlogs:
	$(HUB_SVC) links-digest errlogs
