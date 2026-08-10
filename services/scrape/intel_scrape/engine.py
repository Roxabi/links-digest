"""Run web-intel scrape_content and map to factory text contract."""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Any

from intel_scrape.ssrf import SsrfRejected, assert_url_safe

log = logging.getLogger(__name__)

_MAX_TEXT = 32_000  # align with factory hub ScrapingProcessor

# web-intel scripts live next to the service in the image / monorepo layout.
_DEFAULT_WEB_INTEL_SCRIPTS = (
    Path(__file__).resolve().parents[3] / "plugins" / "web-intel" / "scripts"
)


def _ensure_web_intel_path() -> Path:
    """Put web-intel scripts on sys.path; honour WEB_INTEL_SCRIPTS_PATH override."""
    import os

    raw = os.environ.get("WEB_INTEL_SCRIPTS_PATH", "").strip()
    scripts = Path(raw) if raw else _DEFAULT_WEB_INTEL_SCRIPTS
    if not scripts.is_dir():
        raise RuntimeError(f"web-intel scripts not found: {scripts}")
    s = str(scripts)
    if s not in sys.path:
        sys.path.insert(0, s)
    return scripts


def _text_from_result(result: dict[str, Any]) -> str:
    """Extract main text from scrape_content result."""
    data = result.get("data")
    if isinstance(data, dict):
        text = data.get("text") or ""
        if text:
            return str(text)
    # Some fetchers put text at top level on success
    text = result.get("text") or ""
    return str(text) if text else ""


async def scrape_to_text(url: str, *, timeout: float = 30.0) -> str:
    """SSRF-check *url*, run web-intel, return plain text (capped).

    Raises:
        SsrfRejected — policy violation
        TimeoutError — scrape exceeded timeout
        ValueError — empty extract / engine error with message
        RuntimeError — web-intel unavailable
    """
    import asyncio

    safe = await assert_url_safe(url)
    _ensure_web_intel_path()

    try:
        from scraper import scrape_content  # type: ignore[import-not-found]
    except ImportError as exc:
        raise RuntimeError("web-intel scraper import failed") from exc

    def _run() -> dict[str, Any]:
        return scrape_content(safe)

    try:
        result = await asyncio.wait_for(asyncio.to_thread(_run), timeout=timeout)
    except TimeoutError as exc:
        raise TimeoutError("timeout") from exc

    if not result.get("success"):
        err = str(result.get("error") or "scrape_failed")
        # Surface SSRF-like messages from web-intel as ssrf
        low = err.lower()
        if "ssrf" in low or "priv" in low or "interne" in low or "private" in low:
            raise SsrfRejected("private_ip")
        raise ValueError(err)

    text = _text_from_result(result).strip()
    text = text[:_MAX_TEXT]
    if not text:
        raise ValueError("empty_extract")
    return text


def engine_ready() -> bool:
    """True if web-intel + critical deps import cleanly."""
    try:
        _ensure_web_intel_path()
        import importlib

        importlib.import_module("scraper")
        importlib.import_module("trafilatura")
    except Exception as exc:  # noqa: BLE001 — readiness probe
        log.warning("engine ready fail: %s", exc)
        return False
    return True
