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

PROJECT_NAME ?= links-digest
CF_PROJECT   ?= links-digest

.PHONY: digest digest-all build deploy open clean

# ── Digest ────────────────────────────────────────────────────────────────────

digest:
	uv run python digest.py --hours $(or $(H),24)

digest-%:
	@args=$*; \
	case $$args in \
		all) uv run python digest.py --all ;; \
		*) uv run python digest.py --$${args} ;; \
	esac

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
	npx wrangler pages deploy public --project-name=$(CF_PROJECT) --branch=main

# ── Dev ───────────────────────────────────────────────────────────────────────

open:
	xdg-open public/index.html 2>/dev/null || open public/index.html

# ── Clean ─────────────────────────────────────────────────────────────────────

clean:
	rm -rf links/*.md links/manifest.json public/links/*.md public/links/manifest.json .digest_state.json
