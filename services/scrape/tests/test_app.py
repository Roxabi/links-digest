"""Scrape FastAPI app smoke (factory contract)."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest
from httpx import ASGITransport, AsyncClient

from intel_scrape.app import build_app


@pytest.mark.asyncio
async def test_ready_and_health() -> None:
    app = build_app()
    transport = ASGITransport(app=app)
    with patch("intel_scrape.app.engine_ready", return_value=True):
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/health")
            assert r.status_code == 200
            r2 = await client.get("/ready")
            assert r2.status_code == 200
            assert r2.json().get("ready") is True


@pytest.mark.asyncio
async def test_ready_false_when_engine_down() -> None:
    app = build_app()
    transport = ASGITransport(app=app)
    with patch("intel_scrape.app.engine_ready", return_value=False):
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.get("/ready")
            assert r.status_code == 503
            assert r.json().get("ready") is False


@pytest.mark.asyncio
async def test_scrape_ssrf_http() -> None:
    app = build_app()
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        r = await client.post("/scrape", json={"url": "http://example.com"})
        assert r.status_code == 400
        assert r.json()["reason"] == "ssrf"


@pytest.mark.asyncio
async def test_scrape_success_mocked() -> None:
    app = build_app()
    transport = ASGITransport(app=app)
    with patch(
        "intel_scrape.app.scrape_to_text",
        new=AsyncMock(return_value="Example Domain text"),
    ):
        async with AsyncClient(transport=transport, base_url="http://test") as client:
            r = await client.post(
                "/scrape",
                json={"url": "https://example.com", "timeout_s": 10},
            )
    assert r.status_code == 200
    body = r.json()
    assert body["success"] is True
    assert "Example" in body["text"]


@pytest.mark.asyncio
async def test_bearer_required_when_token_set() -> None:
    app = build_app(token="secret-token")
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        r = await client.post("/scrape", json={"url": "https://example.com"})
        assert r.status_code == 401
        # health stays open
        assert (await client.get("/health")).status_code == 200
