# intel-scrape

HTTP scrape service owned by **roxabi-intel**. Engine = **web-intel** (Playwright + trafilatura).

Factory is a **client only** (`HttpScrapeProvider` + Quadlet pin) — see [roxabi-factory#2338](https://github.com/Roxabi/roxabi-factory/issues/2338).

## Contract

```
POST /scrape  { "url", "timeout_s"? } → { "success", "text"?, "url"?, "error"?, "reason"? }
GET  /ready   → 200 { "ready": true } | 503
GET  /health  → 200 { "status": "ok" }
Optional: Authorization: Bearer <SCRAPE_TOKEN|FACTORY_SCRAPE_TOKEN>
```

- **HTTPS only** at the service boundary (SSRF dual-check, fail-closed DNS).
- Port **8455** (factory default).

## Local run

```bash
# from repo root
cd services/scrape
uv venv && source .venv/bin/activate
uv pip install -e ".[dev]"
# web-intel deps (trafilatura + playwright)
cd ../../plugins/web-intel && uv sync --extra scraper --extra twitter
uv run playwright install chromium
cd ../../services/scrape
export WEB_INTEL_SCRIPTS_PATH=$PWD/../../plugins/web-intel/scripts
export PYTHONPATH=$PWD
python -m intel_scrape serve --port 8455
```

Smoke:

```bash
curl -sS http://127.0.0.1:8455/ready
curl -sS -X POST http://127.0.0.1:8455/scrape \
  -H 'content-type: application/json' \
  -d '{"url":"https://example.com","timeout_s":30}'
```

## Image

```bash
# build from repo root
podman build -f services/scrape/Dockerfile -t ghcr.io/roxabi/intel-scrape:local .
podman run --rm -p 8455:8455 ghcr.io/roxabi/intel-scrape:local
```

Published: `ghcr.io/roxabi/intel-scrape:staging` (and `:sha-<git>`).

## Factory pin

Quadlet unit `factory-scrape` points at this image; hub uses `FACTORY_SCRAPE_URL=http://factory-scrape:8455`.
