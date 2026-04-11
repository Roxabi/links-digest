#!/usr/bin/env python3
"""serve.py — serve links-digest with live-reload.

- Regenerates manifest.json on startup and whenever MD files change
- Watches for MD file changes every 2s
- Pushes SSE events to connected browsers on change

Usage:
  LINKS_DIR=~/projects/links-digest python3 serve.py
  LINKS_DIR=~/projects/links-digest LINKS_PORT=8082 python3 serve.py
"""

import glob as globmod
import http.server
import json
import os
import re
import threading
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DIR = Path(os.environ.get("LINKS_DIR", SCRIPT_DIR))
PORT = int(os.environ.get("LINKS_PORT", 8082))

# ── Manifest generation ───────────────────────────────────────────────────────


def parse_md(filepath: Path) -> dict | None:
    """Parse MD file and extract frontmatter."""
    try:
        text = filepath.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return None

    # Parse frontmatter
    match = re.match(r"^---\s*\n([\s\S]*?)\n---\s*\n", text)
    if not match:
        return None

    yaml_block = match.group(1)
    data = {}

    # Simple YAML parser
    for line in yaml_block.split("\n"):
        arr_match = re.match(r"^(\w+):\s*\[(.+)\]$", line)
        str_match = re.match(r"^(\w+):\s*\"(.+)\"$", line)
        plain_match = re.match(r"^(\w+):\s*(.+)$", line)

        if arr_match:
            data[arr_match[1]] = [s.strip().strip("\"'") for s in arr_match[2].split(",")]
        elif str_match:
            data[str_match[1]] = str_match[2]
        elif plain_match:
            val = plain_match[2]
            if val == "null":
                val = None
            elif val == "true":
                val = True
            elif val == "false":
                val = False
            data[plain_match[1]] = val

    return {
        "f": filepath.name,
        "t": data.get("title", filepath.stem),
        "s": data.get("source", ""),
        "d": data.get("date", "2026-01-01"),
        "tags": data.get("tags", []),
        "p": data.get("platform", "web"),
        "a": data.get("author"),
        "sum": data.get("summary", ""),
    }


def gen_manifest() -> list[dict]:
    """Generate manifest.json from MD files."""
    entries = []
    for match in sorted(globmod.glob(str(DIR / "links" / "*.md"))):
        fp = Path(match)
        entry = parse_md(fp)
        if entry:
            entries.append(entry)

    out = DIR / "links" / "manifest.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n")
    return entries


# ── File watcher ───────────────────────────────────────────────────────────────

sse_clients: list = []
sse_lock = threading.Lock()


def snapshot() -> dict:
    """Return {relative_path: (mtime, size)} for all .md files."""
    snap = {}
    for match in globmod.glob(str(DIR / "links" / "*.md")):
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
            changed_list = ", ".join(sorted(delta))
            print(f"[watcher] manifest updated — {len(entries)} links (changed: {changed_list})")

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
            fp = DIR / "links" / rel_path
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
    # Initial manifest generation
    entries = gen_manifest()
    print(f"manifest.json — {len(entries)} links")

    # Start file watcher
    t = threading.Thread(target=watcher_loop, daemon=True)
    t.start()

    # Start HTTP server
    server = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Serving links-digest at http://localhost:{PORT}")
    print("Watching for changes every 2s...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
