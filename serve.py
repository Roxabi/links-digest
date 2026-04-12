#!/usr/bin/env python3
"""serve.py — serve roxabi-intel with live-reload.

- Regenerates manifest.json on startup and whenever MD files change
- Watches for MD file changes every 2s
- Pushes SSE events to connected browsers on change

Usage:
  INTEL_DIR=~/roxabi/intel python3 serve.py
  INTEL_DIR=~/roxabi/intel INTEL_PORT=8082 python3 serve.py
"""

import glob as globmod
import http.server
import json
import locale
import os
import re
import threading
import time
from pathlib import Path

# Match GNU `ls` default collation so our output is byte-identical to
# `make build` (which uses `ls -1 *.md | jq ...`). Without this, Python's
# codepoint sort places `_` before letters while `ls` collates it after,
# causing spurious manifest diffs after every serve.py watcher tick.
locale.setlocale(locale.LC_ALL, "")

SCRIPT_DIR = Path(__file__).resolve().parent
DIR = Path(os.environ.get("INTEL_DIR", str(Path.home() / "roxabi" / "intel")))
PORT = int(os.environ.get("INTEL_PORT", 8082))

# ── Manifest generation ───────────────────────────────────────────────────────


def gen_manifest() -> list[str]:
    """Generate manifest.json — plain list of filenames.

    Kept for backwards-compatibility with existing tooling and as the
    fallback path in gallery.js when index.json is unavailable.
    """
    entries = sorted(
        (Path(match).name for match in globmod.glob(str(DIR / "*.md"))),
        key=locale.strxfrm,
    )

    out = DIR / "manifest.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")
    return entries


# ── Index generation (lazy-load pivot) ────────────────────────────────────────

_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_FM_LINE_RE = re.compile(r"^(\w+):\s*(.*)$", re.MULTILINE)
_INDEX_FIELDS = ("title", "source", "date", "tags", "platform", "author", "summary")


def _parse_frontmatter(text: str) -> dict | None:
    """Parse the frontmatter block of a links/*.md file.

    The template writes every non-bare field via Jinja's `tojson` filter
    (with ensure_ascii=False), so quoted strings and arrays are valid
    JSON. Bare scalars (date, platform, `null`) are stored as-is.
    """
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    result: dict = {}
    for line_m in _FM_LINE_RE.finditer(m.group(1)):
        key = line_m.group(1)
        raw = line_m.group(2).strip()
        if raw == "null" or raw == "":
            result[key] = None
        elif raw.startswith('"') or raw.startswith("["):
            try:
                result[key] = json.loads(raw)
            except json.JSONDecodeError:
                result[key] = raw
        else:
            result[key] = raw
    return result


def gen_index() -> int:
    """Generate index.json — one row of frontmatter per link.

    Shipped to the browser so gallery.js can render every card from a
    single HTTP request instead of fetching N individual .md files.
    Full markdown content stays in the per-file .md and is loaded
    lazily on modal open.
    """
    entries: list[dict] = []
    for match in sorted(
        globmod.glob(str(DIR / "*.md")),
        key=lambda p: locale.strxfrm(Path(p).name),
    ):
        path = Path(match)
        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue
        fm = _parse_frontmatter(text)
        if not fm:
            continue
        entry: dict = {"file": path.name}
        for field in _INDEX_FIELDS:
            entry[field] = fm.get(field)
        entries.append(entry)

    out = DIR / "index.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")
    return len(entries)


# ── File watcher ───────────────────────────────────────────────────────────────

sse_clients: list = []
sse_lock = threading.Lock()


def snapshot() -> dict:
    """Return {relative_path: (mtime, size)} for all .md files."""
    snap = {}
    for match in globmod.glob(str(DIR / "*.md")):
        fp = Path(match)
        try:
            st = fp.stat()
            snap[fp.name] = (st.st_mtime, st.st_size)
        except OSError:
            snap[fp.name] = (0, 0)
    return snap


def watcher_loop():
    prev = snapshot()
    while True:
        time.sleep(2)
        curr = snapshot()
        if curr != prev:
            added = set(curr) - set(prev)
            removed = set(prev) - set(curr)
            changed = {k for k in set(curr) & set(prev) if curr[k] != prev[k]}
            delta = added | removed | changed
            prev = curr

            entries = gen_manifest()
            gen_index()
            changed_list = ", ".join(sorted(delta))
            print(f"[watcher] index updated — {len(entries)} links (changed: {changed_list})")

            # Notify SSE clients
            msg = f"data: {json.dumps({'type': 'reload', 'changed': sorted(delta)})}\n\n"
            with sse_lock:
                dead = []
                for wf in sse_clients:
                    try:
                        wf.write(msg.encode())
                        wf.flush()
                    except Exception:
                        dead.append(wf)
                for wf in dead:
                    sse_clients.remove(wf)


# ── HTTP handler ───────────────────────────────────────────────────────────────

FAVICON_SVG = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">'
    b'<rect width="32" height="32" rx="6" fill="#f59e0b"/>'
    b'<path d="M8 10h16v2H8zm0 5h12v2H8zm0 5h14v2H8z" fill="#fff" opacity=".9"/>'
    b"</svg>"
)


class Handler(http.server.SimpleHTTPRequestHandler):
    _NO_CACHE_EXTS = (".html", ".htm", ".css", ".js", ".mjs", ".json")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(DIR / "public"), **kwargs)

    def end_headers(self):
        path = self.path.split("?")[0].split("#")[0].lower()
        if path == "/" or path.endswith(self._NO_CACHE_EXTS):
            self.send_header("Cache-Control", "no-cache, must-revalidate")
        super().end_headers()

    def do_GET(self):
        # Serve index.html from public/
        if self.path in ("/", "/index.html"):
            index = DIR / "public" / "index.html"
            body = index.read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return

        if self.path == "/favicon.ico":
            self.send_response(200)
            self.send_header("Content-Type", "image/svg+xml")
            self.send_header("Content-Length", str(len(FAVICON_SVG)))
            self.send_header("Cache-Control", "public, max-age=86400")
            self.end_headers()
            self.wfile.write(FAVICON_SVG)
            return

        if self.path == "/api/events":
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.send_header("Cache-Control", "no-cache")
            self.send_header("Connection", "keep-alive")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(b": connected\n\n")
            self.wfile.flush()
            with sse_lock:
                sse_clients.append(self.wfile)
            try:
                while True:
                    time.sleep(30)
                    self.wfile.write(b": ping\n\n")
                    self.wfile.flush()
            except Exception:
                pass
            finally:
                with sse_lock:
                    if self.wfile in sse_clients:
                        sse_clients.remove(self.wfile)
            return

        # Serve links/ directory
        if self.path.startswith("/links/"):
            # Redirect to local links directory
            rel_path = self.path[7:]  # strip /links/
            fp = DIR / rel_path
            if fp.exists():
                body = fp.read_bytes()
                ct = "text/markdown" if rel_path.endswith(".md") else "application/octet-stream"
                self.send_response(200)
                self.send_header("Content-Type", ct)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)
                return
            else:
                self.send_error(404, "Not found")
                return

        super().do_GET()

    def log_message(self, format, *args):
        if "/api/events" in (str(args[0]) if args else ""):
            return
        super().log_message(format, *args)


# ── Main ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    # Initial manifest + index generation
    entries = gen_manifest()
    count = gen_index()
    print(f"manifest.json + index.json — {count} links")

    # --build flag: generate manifest + index and exit (used by `make build`).
    if "--build" in sys.argv:
        sys.exit(0)

    # Start file watcher
    t = threading.Thread(target=watcher_loop, daemon=True)
    t.start()

    # Start HTTP server
    server = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Serving roxabi-intel at http://localhost:{PORT}")
    print("Watching for changes every 2s...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
