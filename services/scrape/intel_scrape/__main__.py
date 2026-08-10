"""CLI: python -m intel_scrape serve."""

from __future__ import annotations

import argparse
import logging

import uvicorn

from intel_scrape.app import build_app


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="intel_scrape", description="intel-scrape HTTP service")
    sub = parser.add_subparsers(dest="cmd", required=True)

    serve = sub.add_parser("serve", help="Start HTTP scrape service")
    serve.add_argument("--host", default="0.0.0.0", help="Bind host")
    serve.add_argument("--port", type=int, default=8455, help="Bind port")
    serve.add_argument("--log-level", default="info", help="uvicorn log level")

    args = parser.parse_args(argv)
    if args.cmd == "serve":
        logging.basicConfig(level=logging.INFO)
        uvicorn.run(build_app(), host=args.host, port=args.port, log_level=args.log_level)


if __name__ == "__main__":
    main()
