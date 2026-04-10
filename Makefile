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
	@ls public/links/*.md 2>/dev/null | wc -l | xargs -I {} echo "Found {} MD files"
	@echo "Generating manifest.json..."
	@cd public/links && ls -1 *.md 2>/dev/null | jq -Rs 'split("\n") | map(select(length > 0))' > manifest.json
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
	rm -rf public/links/*.md .digest_state.json
