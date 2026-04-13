# roxabi-intel Makefile
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

PROJECT_NAME ?= roxabi-intel
CF_PROJECT   ?= links-digest
INTEL_PORT   ?= 8082

-include .env
export CLOUDFLARE_ACCOUNT_ID
export CLOUDFLARE_API_TOKEN

SUPERVISOR_HUB  ?= $(HOME)/projects
HUB_SERVICES    := intel
-include $(SUPERVISOR_HUB)/hub.mk

.PHONY: digest digest-all build deploy open clean intel register help

# ── Digest ────────────────────────────────────────────────────────────────────

digest:
	uv run python digest.py --hours $(or $(H),24)

digest-all:
	uv run python digest.py --all

digest-%:
	@args=$*; \
	uv run python digest.py --$${args}

# ── Build ─────────────────────────────────────────────────────────────────────

INTEL_DIR ?= $(HOME)/.roxabi/intel

build:
	@echo "Building gallery..."
	@ls $(INTEL_DIR)/*.md 2>/dev/null | wc -l | xargs -I {} echo "Found {} MD files"
	@echo "Generating manifest.json + index.json..."
	@INTEL_DIR=$(INTEL_DIR) uv run python serve.py --build
	@echo "Syncing to public/..."
	@mkdir -p $(INTEL_DIR)/public/links
	@cp $(INTEL_DIR)/*.md $(INTEL_DIR)/public/links/ 2>/dev/null || true
	@cp $(INTEL_DIR)/manifest.json $(INTEL_DIR)/index.json $(INTEL_DIR)/public/links/
	@cp -r public/index.html public/css public/js public/favicon.svg public/favicon-32.png public/apple-touch-icon.png public/og-image.png $(INTEL_DIR)/public/
	@echo "Done."

# ── Deploy ────────────────────────────────────────────────────────────────────

deploy: build
	@echo "Deploying to Cloudflare Pages: $(CF_PROJECT)..."
	npx wrangler pages deploy $(INTEL_DIR)/public --project-name=$(CF_PROJECT) --branch=main --commit-dirty=true

# ── Dev ───────────────────────────────────────────────────────────────────────

open:
	xdg-open public/index.html 2>/dev/null || open public/index.html

# ── Clean ─────────────────────────────────────────────────────────────────────

clean:
	rm -rf $(INTEL_DIR)/*.md $(INTEL_DIR)/manifest.json $(INTEL_DIR)/public/*.md $(INTEL_DIR)/public/manifest.json .digest_state.json

# ── Supervisor service (hub-dispatched) ─────────────────────────────────────────
# Usage (from this dir or from ~/projects):
#   make intel start|stop|reload|status|logs|errlogs

intel:
	@$(HUB_SVC) roxabi-intel $(SVC_CMD)

# ── Registration ────────────────────────────────────────────────────────────────

register:
	@echo "Registering roxabi-intel with supervisor hub..."
	@$(HUB_GEN_MK) roxabi-intel "$(abspath .)" intel
	$(call hub-link-conf,roxabi-intel,supervisor/conf.d/roxabi-intel.conf)
	@mkdir -p "$(HOME)/.local/state/roxabi-intel/logs"
	$(hub_reread)
	@echo "Done."
