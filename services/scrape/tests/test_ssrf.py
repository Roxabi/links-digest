"""SSRF policy unit tests."""

from __future__ import annotations

import ipaddress

import pytest

from intel_scrape.ssrf import (
    SsrfRejected,
    assert_url_safe,
    ip_is_blocked,
    require_https_url,
)


def test_https_only() -> None:
    with pytest.raises(SsrfRejected) as ei:
        require_https_url("http://example.com")
    assert ei.value.reason == "https_only"


def test_https_ok() -> None:
    assert require_https_url("https://example.com/path") == "https://example.com/path"


def test_private_literal_ip() -> None:
    assert ip_is_blocked(ipaddress.ip_address("127.0.0.1"))
    assert ip_is_blocked(ipaddress.ip_address("10.0.0.1"))
    assert ip_is_blocked(ipaddress.ip_address("192.168.1.1"))
    assert ip_is_blocked(ipaddress.ip_address("100.64.0.1"))  # Tailscale CGNAT


@pytest.mark.asyncio
async def test_assert_private_literal() -> None:
    with pytest.raises(SsrfRejected) as ei:
        await assert_url_safe("https://127.0.0.1/")
    assert ei.value.reason == "private_ip"
