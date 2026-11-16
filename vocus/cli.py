"""CLI entry point for vocus."""

import argparse
import sys

from .window import run


def _read_html(args) -> str:
    if args.html:
        with open(args.html, "r", encoding="utf-8") as f:
            return f.read()
    # stdin
    if not sys.stdin.isatty():
        return sys.stdin.read()
    # no input: empty frame
    return ""


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        prog="vocus", description="Tiny native HTML viewer (GTK3 + WebKit2GTK)."
    )
    parser.add_argument("--html", metavar="PATH", help="HTML file to display")
    parser.add_argument("--title", default="vocus", help="window title")
    args = parser.parse_args(argv)

    html = _read_html(args)
    run(html, title=args.title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())