#!/usr/bin/env python3
"""
Roxabi Intel — Fetch Discord links → scrape → generate frontmatter MDs

Usage:
    uv run python digest.py              # Scan last 24h (default)
    uv run python digest.py --hours 72   # Scan last 72 hours
    uv run python digest.py --days 7     # Scan last 7 days
    uv run python digest.py --all        # Scan entire channel history
"""

import argparse
import json
import re
import subprocess
import sys
import tomllib
from datetime import datetime, timedelta, timezone
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

# ── Paths ─────────────────────────────────────────────────────────────────────

PROJECT_ROOT = Path(__file__).parent
CONFIG_PATH = PROJECT_ROOT / "config.toml"
TEMPLATE_DIR = PROJECT_ROOT / "templates"
INTEL_DIR = Path.home() / ".roxabi" / "intel"
STATE_FILE = PROJECT_ROOT / ".digest_state.json"

# ── Config ────────────────────────────────────────────────────────────────────


def load_config() -> dict:
    with open(CONFIG_PATH, "rb") as f:
        return tomllib.load(f)


# ── State tracking ────────────────────────────────────────────────────────────


def load_state() -> dict:
    if STATE_FILE.exists():
        with open(STATE_FILE) as f:
            return json.load(f)
    return {"last_scan": None, "scanned_ids": []}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w") as f:
        json.dump(state, f, indent=2)


# ── Discord ───────────────────────────────────────────────────────────────────


def get_discord_token() -> str:
    """Get Discord bot token from Lyra's CredentialStore."""
    import asyncio

    lyra_dir = Path.home() / ".lyra"

    # Check if Lyra's credential store exists
    keyring_path = lyra_dir / "keyring.key"
    db_path = lyra_dir / "config.db"

    if not keyring_path.exists() or not db_path.exists():
        print("ERROR: Lyra credential store not found")
        print("Run 'lyra bot add' to store Discord token first")
        sys.exit(1)

    # Import Lyra's credential store
    try:
        from lyra.core.stores.credential_store import CredentialStore, LyraKeyring
    except ImportError:
        print("ERROR: lyra package not installed")
        print("Install it or set DISCORD_TOKEN env var")
        sys.exit(1)

    async def _get_token() -> str | None:
        keyring = LyraKeyring.load_or_create(keyring_path)
        store = CredentialStore(db_path=db_path, keyring=keyring)
        await store.connect()
        try:
            # Try 'lyra' bot first, then any discord bot
            token = await store.get("discord", "lyra")
            if not token:
                # List all discord bots and use the first one
                rows = await store.list_all()
                discord_bots = [r for r in rows if r.platform == "discord"]
                if discord_bots:
                    token = await store.get("discord", discord_bots[0].bot_id)
            return token
        finally:
            await store.close()

    token = asyncio.run(_get_token())
    if not token:
        print("ERROR: No Discord bot token found in Lyra credential store")
        print("Run: lyra bot add --platform discord --bot-id lyra")
        sys.exit(1)
    return token


def fetch_discord_messages(
    channel_id: str, token: str, after: datetime | None = None, limit: int = 1000
) -> list[dict]:
    """Fetch messages from Discord channel using bot API."""
    import discord
    from discord.ext import commands

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    messages = []

    @bot.event
    async def on_ready():
        nonlocal messages
        channel = bot.get_channel(int(channel_id))
        if not channel:
            print(f"ERROR: Channel {channel_id} not found")
            await bot.close()
            return

        # Only text channels have name and history
        if not isinstance(channel, discord.TextChannel):
            print(f"ERROR: Channel {channel_id} is not a text channel")
            await bot.close()
            return

        print(f"Fetching messages from #{channel.name}...")

        # Convert after to snowflake if provided
        after_snowflake = None
        if after:
            # Discord epoch: 2015-01-01
            discord_epoch = datetime(2015, 1, 1, tzinfo=timezone.utc)
            snowflake_time = (after - discord_epoch).total_seconds() * 1000
            after_id = int(snowflake_time) << 22
            after_snowflake = discord.Object(after_id)

        async for msg in channel.history(limit=limit, after=after_snowflake):
            if msg.content:  # Skip empty messages
                messages.append(
                    {
                        "id": str(msg.id),
                        "content": msg.content,
                        "author": str(msg.author),
                        "timestamp": msg.created_at.isoformat(),
                        "jump_url": msg.jump_url,
                    }
                )

        print(f"Fetched {len(messages)} messages")
        await bot.close()

    bot.run(token)
    return messages


# ── URL extraction ────────────────────────────────────────────────────────────


def extract_urls(messages: list[dict]) -> list[dict]:
    """Extract URLs from messages with metadata."""
    url_pattern = r"https?://[^\s<>\[\]\"']+"
    results = []

    for msg in messages:
        urls = re.findall(url_pattern, msg["content"])
        for url in urls:
            # Clean URL (remove trailing punctuation)
            url = url.rstrip(".,;!?)")

            # Skip common non-content URLs
            if any(
                skip in url.lower()
                for skip in ["/tenor.com/", "/giphy.com/", "discord.com/channels/"]
            ):
                continue

            results.append(
                {
                    "url": url,
                    "message_id": msg["id"],
                    "author": msg["author"],
                    "timestamp": msg["timestamp"],
                    "jump_url": msg["jump_url"],
                }
            )

    # Dedupe by URL
    seen = set()
    unique = []
    for item in results:
        if item["url"] not in seen:
            seen.add(item["url"])
            unique.append(item)

    return unique


# ── Scraping ──────────────────────────────────────────────────────────────────


def find_web_intel() -> Path | None:
    """Find web-intel plugin root.

    Prefers the git-tracked source under ~/projects/roxabi-plugins so local
    fixes take effect immediately without waiting for a marketplace plugin
    refresh. Falls back to the marketplace cache, then a legacy standalone
    checkout.
    """
    candidates = [
        # Live source of truth — changes to enricher.py / fetchers apply here.
        Path.home() / "projects" / "roxabi-plugins" / "plugins" / "web-intel",
        # Marketplace plugin cache (may lag behind git by days).
        Path.home()
        / ".claude"
        / "plugins"
        / "cache"
        / "roxabi-marketplace"
        / "web-intel"
        / "0.1.0",
        Path.home() / "projects" / "web-intel",
    ]
    for p in candidates:
        if (p / "scripts" / "scraper.py").exists():
            return p
    return None


def scrape_url(url: str, web_intel_root: Path) -> dict | None:
    """Scrape URL using web-intel scraper."""
    try:
        result = subprocess.run(
            ["uv", "run", "python", "scripts/scraper.py", url],
            cwd=web_intel_root,
            capture_output=True,
            text=True,
            timeout=60,
            env={
                **dict(__import__("os").environ),
                "SSL_CERT_FILE": "/etc/ssl/certs/ca-certificates.crt",
            },
        )

        if result.returncode != 0:
            print(f"  Scrape failed for {url}: {result.stderr[:100]}")
            return None

        return json.loads(result.stdout)

    except subprocess.TimeoutExpired:
        print(f"  Timeout scraping {url}")
        return None
    except json.JSONDecodeError as e:
        print(f"  JSON parse error for {url}: {e}")
        return None


# Signals that an enrichment result has bled in reasoning text or prompt
# fragments — we discard the whole enrichment when these appear rather than
# letting salvaged bullet-list garbage reach the MD frontmatter.
_ENRICH_BLEED_TAG_CHARS = set("`()?*[]{}")
_ENRICH_BLEED_RE = re.compile(
    r"\b(draft|encapsulat|one sentence|keywords\?|refinement|let me|"
    r"thinking|revised)\b",
    re.IGNORECASE,
)


def validate_enrichment(enriched: dict) -> tuple[bool, str]:
    """Return (ok, reason) — reject garbage enrichment output.

    Defence-in-depth after the enricher's own validator. If this returns
    False, the caller should treat the enrichment as empty and fall back
    to the scraper-provided description.
    """
    tags = enriched.get("tags", []) or []
    summary = (enriched.get("summary") or "").strip()

    for t in tags:
        if not isinstance(t, str) or not t.strip():
            return False, f"non-string or empty tag: {t!r}"
        if any(ch in t for ch in _ENRICH_BLEED_TAG_CHARS):
            return False, f"tag has markdown bleed chars: {t!r}"
        if _ENRICH_BLEED_RE.search(t):
            return False, f"tag echoes prompt vocabulary: {t!r}"
        if len(t) > 40 or len(t.split()) > 5:
            return False, f"tag too long or phrase-like: {t!r}"

    if summary:
        if summary.startswith(("*", "-", "`", "#", ">")):
            return False, f"summary starts with markdown: {summary[:40]!r}"
        if _ENRICH_BLEED_RE.search(summary):
            return False, f"summary echoes prompt vocabulary: {summary[:60]!r}"

    return True, "ok"


def enrich_content(data: dict, web_intel_root: Path) -> dict:
    """Enrich scraped content with LLM-extracted tags and summary."""
    empty = {"tags": [], "summary": "", "key_points": []}
    try:
        # Pass scraped data to enricher via stdin
        input_json = json.dumps(data)
        result = subprocess.run(
            ["uv", "run", "python", "scripts/enricher.py"],
            cwd=web_intel_root,
            input=input_json,
            capture_output=True,
            text=True,
            timeout=60,
        )

        if result.returncode != 0:
            print(f"  Enrichment failed: {result.stderr[:80]}")
            return empty

        enriched = json.loads(result.stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError) as e:
        print(f"  Enrichment error: {e}")
        return empty

    ok, reason = validate_enrichment(enriched)
    if not ok:
        print(f"  Enrichment rejected by validator: {reason}")
        return empty
    return enriched


# ── Platform detection ────────────────────────────────────────────────────────


def detect_platform(url: str) -> str:
    """Detect platform from URL."""
    url_lower = url.lower()
    # gist.github.com must be checked BEFORE github.com (substring match)
    if "gist.github.com" in url_lower:
        return "gist"
    elif "github.com" in url_lower:
        return "github"
    elif "x.com" in url_lower or "twitter.com" in url_lower:
        return "x"
    elif "youtube.com" in url_lower or "youtu.be" in url_lower:
        return "youtube"
    elif "reddit.com" in url_lower:
        return "reddit"
    else:
        return "web"


# ── MD generation ─────────────────────────────────────────────────────────────


def generate_slug(url: str, date: str) -> str:
    """Generate filename slug from URL and date."""
    # Try to extract meaningful name from URL
    platform = detect_platform(url)

    if platform == "github":
        # Extract repo name. Strip query (?tab=readme-ov-file) / fragment
        # suffixes before returning — a `?` in the filename is valid on
        # Linux but breaks URL escaping in the gallery and looks broken.
        match = re.search(r"github\.com/[^/]+/([^/?#]+)", url)
        if match:
            return match.group(1).lower()
    elif platform == "gist":
        match = re.search(r"gist\.github\.com/([^/]+)/", url)
        if match:
            return f"gist-{match.group(1).lower()}"
    elif platform == "x":
        # Extract author
        match = re.search(r"x\.com/([^/]+)/status/", url)
        if match:
            return f"x-{match.group(1).lower()}"
    elif platform == "reddit":
        match = re.search(r"reddit\.com/r/[^/]+/comments/[^/]+/([^/]+)", url)
        if match:
            return match.group(1).lower().rstrip("/")

    # Fallback: hash
    import hashlib

    url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
    return f"link-{url_hash}"


def render_md(data: dict, template) -> str:
    """Render MD from template."""
    return template.render(**data)


def synthesize_tweet_title(text: str, author: str | None) -> str:
    """Build a meaningful title from a tweet body when none is provided."""
    if text:
        first = next((line.strip() for line in text.splitlines() if line.strip()), "")
        if first:
            if len(first) > 80:
                first = first[:77].rstrip() + "..."
            return first
    return f"@{author} on X" if author else "X post"


# ── Main ──────────────────────────────────────────────────────────────────────


def parse_args():
    parser = argparse.ArgumentParser(description="Generate links digest from Discord")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--hours", type=int, help="Scan last N hours")
    group.add_argument("--days", type=int, help="Scan last N days")
    group.add_argument("--all", action="store_true", help="Scan entire channel history")
    return parser.parse_args()


def main():
    args = parse_args()

    # Load config
    config = load_config()
    channel_id = config["discord"]["channel_id"]

    # Determine time window
    if args.all:
        after = None
        print("Scanning entire channel history...")
    elif args.days:
        after = datetime.now(timezone.utc) - timedelta(days=args.days)
        print(f"Scanning last {args.days} days (since {after.isoformat()})...")
    elif args.hours:
        after = datetime.now(timezone.utc) - timedelta(hours=args.hours)
        print(f"Scanning last {args.hours} hours (since {after.isoformat()})...")
    else:
        hours = config["scan"]["default_hours"]
        after = datetime.now(timezone.utc) - timedelta(hours=hours)
        print(f"Scanning last {hours} hours (since {after.isoformat()})...")

    # Get Discord token
    token = get_discord_token()

    # Fetch messages
    messages = fetch_discord_messages(channel_id, token, after=after)

    if not messages:
        print("No messages found")
        return

    # Extract URLs
    urls = extract_urls(messages)
    print(f"Found {len(urls)} unique URLs")

    if not urls:
        print("No URLs to process")
        return

    # Find web-intel
    web_intel = find_web_intel()
    if not web_intel:
        print("ERROR: web-intel plugin not found. Install: claude plugin install web-intel")
        sys.exit(1)

    print(f"Using web-intel at {web_intel}")

    # Setup Jinja
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    # Override `tojson` filter so frontmatter gets raw UTF-8 + raw
    # apostrophes instead of \uXXXX escapes. Jinja's default `tojson`
    # uses htmlsafe_json_dumps which escapes both non-ASCII *and*
    # HTML-special chars ('<>&\'"') regardless of ensure_ascii — that's
    # wrong for YAML frontmatter (never embedded in HTML attributes).
    # YAML 1.2 accepts both escaped and raw forms; the gallery's
    # JSON.parse fallback still decodes legacy escaped files cleanly.
    env.filters["tojson"] = lambda obj: json.dumps(obj, ensure_ascii=False)
    template = env.get_template("link.md.j2")

    # Ensure output dir
    INTEL_DIR.mkdir(parents=True, exist_ok=True)

    # Process URLs
    results = []
    for i, item in enumerate(urls, 1):
        url = item["url"]
        print(f"[{i}/{len(urls)}] Scraping {url}...")

        scraped = scrape_url(url, web_intel)

        if scraped and scraped.get("success"):
            data = scraped.get("data", {})
            content_type = scraped.get("content_type", "web")
            date = item["timestamp"][:10]
            slug = generate_slug(url, date)

            # Enrich with LLM
            print(f"  Enriching {slug}...")
            enriched = enrich_content(data, web_intel)

            # Per-content-type extraction.
            # web-intel's `data.text` is a French LLM-prompt blob
            # ("Auteur: ... Type: ... Titre: ... Contenu: ...") meant for the
            # enricher. Render the clean field for the markdown body instead.
            if content_type == "twitter":
                content = data.get("raw_text") or ""
                author = data.get("author") or data.get("username")
                # Regular tweets have no title field — synthesize from body.
                title = data.get("title") or synthesize_tweet_title(content, author)
            elif content_type == "gist":
                content = data.get("content") or ""
                author = data.get("owner")
                title = data.get("title") or "Untitled Gist"
            else:
                content = data.get("text") or ""
                author = data.get("author") or data.get("username")
                title = data.get("title") or "Untitled"

            md_data = {
                "title": title,
                "source": url,
                "date": date,
                "tags": enriched.get("tags", []) if enriched.get("tags") else [],
                "platform": detect_platform(url),
                "author": author,
                "summary": enriched.get("summary")
                or data.get("description")
                or data.get("excerpt")
                or "",
                "content": content,
            }

            # Write MD
            md_content = render_md(md_data, template)
            filename = f"{date}_{slug}.md"
            filepath = INTEL_DIR / filename

            with open(filepath, "w") as f:
                f.write(md_content)

            print(f"  → {filename}")
            results.append({"file": filename, **md_data})

        else:
            # Create placeholder for failed scrapes (e.g., X posts)
            date = item["timestamp"][:10]
            platform = detect_platform(url)

            if platform == "x":
                # Extract username
                match = re.search(r"x\.com/([^/]+)/status/", url)
                author = f"@{match.group(1)}" if match else None
            elif platform == "gist":
                match = re.search(r"gist\.github\.com/([^/]+)/", url)
                author = match.group(1) if match else None
            else:
                author = None

            slug = generate_slug(url, date)
            filename = f"{date}_{slug}.md"
            filepath = INTEL_DIR / filename

            md_data = {
                "title": f"Link — {platform.title()}",
                "source": url,
                "date": date,
                "tags": [platform],
                "platform": platform,
                "author": author,
                "summary": f"Content from {url}. See source for details.",
                "content": None,
            }

            md_content = render_md(md_data, template)
            with open(filepath, "w") as f:
                f.write(md_content)

            print(f"  → {filename} (placeholder)")
            results.append({"file": filename, **md_data})

    # Update state
    state = load_state()
    state["last_scan"] = datetime.now(timezone.utc).isoformat()
    save_state(state)

    print(f"\nDone! Generated {len(results)} MD files in {INTEL_DIR}")


if __name__ == "__main__":
    main()
