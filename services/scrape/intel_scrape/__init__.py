"""intel-scrape — HTTP scrape service (web-intel engine).

Contract matches factory HttpScrapeProvider (#2327 / factory#2338):
  POST /scrape  {url, timeout_s?} → {success, text?, url?, error?, reason?}
  GET  /ready   → 200 {ready: true} | 503
  GET  /health  → 200 process up
"""

__version__ = "0.1.0"
