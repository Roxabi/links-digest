# intel-scrape — web-intel (Playwright + trafilatura) behind factory scrape HTTP API
# Build context: repo root (roxabi-intel)
#   podman build -f services/scrape/Dockerfile -t ghcr.io/roxabi/intel-scrape:local .
#
# Image contract:
#   POST /scrape  GET /ready  GET /health  — port 8455
#   optional SCRAPE_TOKEN / FACTORY_SCRAPE_TOKEN

FROM python:3.12-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PLAYWRIGHT_BROWSERS_PATH=/ms-playwright \
    WEB_INTEL_SCRIPTS_PATH=/app/web-intel/scripts \
    # /app/web-intel hosts vendored roxabi_sdk (fetchers PLUGIN_ROOT path)
    PYTHONPATH=/app/service:/app/web-intel

# Non-root uid matches factory Quadlet UserNS keep-id 1500
RUN groupadd -g 1500 scrape && useradd -u 1500 -g 1500 -m -s /bin/bash scrape \
    && mkdir -p /ms-playwright /tmp/playwright \
    && chown -R scrape:scrape /ms-playwright /tmp/playwright

WORKDIR /app

# Service package
COPY services/scrape/pyproject.toml /app/service/pyproject.toml
COPY services/scrape/intel_scrape /app/service/intel_scrape

# web-intel engine
COPY plugins/web-intel /app/web-intel

# Install Python deps + Chromium system libs + browser
RUN pip install --upgrade pip \
    && pip install /app/service \
    && pip install \
        "trafilatura>=1.8" \
        "playwright>=1.40" \
        "playwright-stealth>=2.0.2" \
        "requests>=2.31" \
        "httpx>=0.27" \
        "filelock>=3.13" \
    && playwright install-deps chromium \
    && playwright install chromium \
    && chown -R scrape:scrape /ms-playwright /app /home/scrape

USER scrape
WORKDIR /app
EXPOSE 8455

HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
    CMD python -c "import urllib.request,sys; r=urllib.request.urlopen('http://127.0.0.1:8455/ready',timeout=3); sys.exit(0 if r.status==200 else 1)"

CMD ["python", "-m", "intel_scrape", "serve", "--host", "0.0.0.0", "--port", "8455"]
