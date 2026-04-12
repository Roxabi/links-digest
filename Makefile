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

SUPERVISOR_HUB  ?= $(HOME)/projects
HUB_SERVICES    := links
-include $(SUPERVISOR_HUB)/hub.mk

.PHONY: digest digest-all build deploy open clean links register help

# ── Digest ────────────────────────────────────────────────────────────────────

digest:
	uv run python digest.py --hours $(or $(H),24)

digest-all:
	uv run python digest.py --all

digest-%:
	@args=$*; \
	uv run python digest.py --$${args}

# ── Build ─────────────────────────────────────────────────────────────────────

LINKS_DIR ?= $(HOME)/roxabi/links

build:
	@echo "Building gallery..."
	@ls $(LINKS_DIR)/*.md 2>/dev/null | wc -l | xargs -I {} echo "Found {} MD files"
	@echo "Generating manifest.json + index.json..."
	@LINKS_DIR=$(LINKS_DIR) uv run python serve.py --build
	@echo "Syncing to public/..."
	@mkdir -p $(LINKS_DIR)/public
	@cp $(LINKS_DIR)/*.md $(LINKS_DIR)/public/ 2>/dev/null || true
	@cp $(LINKS_DIR)/manifest.json $(LINKS_DIR)/index.json $(LINKS_DIR)/public/
	@cp -r public/index.html public/css public/js $(LINKS_DIR)/public/
	@echo "Done."

# ── Deploy ────────────────────────────────────────────────────────────────────

deploy: build
	@echo "Deploying to Cloudflare Pages: $(CF_PROJECT)..."
	CLOUDFLARE_ACCOUNT_ID=$(CF_ACCOUNT) npx wrangler pages deploy $(LINKS_DIR)/public --project-name=$(CF_PROJECT) --branch=main --commit-dirty=true

# ── Dev ───────────────────────────────────────────────────────────────────────

open:
	xdg-open public/index.html 2>/dev/null || open public/index.html

# ── Clean ─────────────────────────────────────────────────────────────────────

clean:
	rm -rf $(LINKS_DIR)/*.md $(LINKS_DIR)/manifest.json $(LINKS_DIR)/public/*.md $(LINKS_DIR)/public/manifest.json .digest_state.json

# ── Supervisor service (hub-dispatched) ─────────────────────────────────────────
# Usage (from this dir or from ~/projects):
#   make links start|stop|reload|status|logs|errlogs
#
# Hub target `links` dispatches to supervisor program `links-digest`
# (program name kept for historical continuity / conf file naming).

links:
	@$(HUB_SVC) links-digest $(SVC_CMD)

# ── Registration ────────────────────────────────────────────────────────────────

register:
	@echo "Registering links-digest with supervisor hub..."
	@$(HUB_GEN_MK) links-digest "$(abspath .)" links
	$(call hub-link-conf,links-digest,supervisor/conf.d/links-digest.conf)
	@mkdir -p "$(HOME)/.local/state/links-digest/logs"
	$(hub_reread)
	@echo "Done."
