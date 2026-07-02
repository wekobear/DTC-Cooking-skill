#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path


class SiteParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.title = ""
        self._in_title = False
        self.meta = {}
        self.ids = set()
        self.images = []
        self.links = []
        self.buttons = []
        self.data_tracks = []
        self.json_ld_blocks = []
        self.headings = []
        self._script_type = None
        self._script_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self._in_title = True
        if tag == "meta":
            key = attrs.get("name") or attrs.get("property")
            if key:
                self.meta[key.lower()] = attrs.get("content", "")
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "img":
            self.images.append(attrs)
        if tag == "a":
            self.links.append(attrs)
        if tag == "button":
            self.buttons.append(attrs)
        if "data-track" in attrs:
            self.data_tracks.append(attrs["data-track"])
        if re.fullmatch(r"h[1-6]", tag):
            self.headings.append((tag, attrs))
        if tag == "script":
            self._script_type = attrs.get("type")
            self._script_text = []

    def handle_data(self, data):
        if self._in_title:
            self.title += data
        if self._script_type == "application/ld+json":
            self._script_text.append(data)

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag == "script" and self._script_type == "application/ld+json":
            self.json_ld_blocks.append("".join(self._script_text).strip())
            self._script_type = None
            self._script_text = []


def read_optional(path: str | None) -> str:
    return Path(path).read_text(encoding="utf-8") if path else ""


def add_failure(failures: list[str], condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run generic static checks for a local ecommerce page.")
    parser.add_argument("html", help="Path to the HTML file to inspect.")
    parser.add_argument("--css", help="Optional CSS file to inspect.")
    parser.add_argument("--js", help="Optional JS file to inspect.")
    parser.add_argument("--required-id", action="append", default=[], help="Required element id. Repeat as needed.")
    parser.add_argument("--required-text", action="append", default=[], help="Required text. Repeat as needed.")
    parser.add_argument("--forbidden-text", action="append", default=[], help="Forbidden or unverified claim. Repeat as needed.")
    parser.add_argument("--min-product-links", type=int, default=0, help="Minimum links whose href contains /products/.")
    parser.add_argument("--require-tracking", action="store_true", help="Require at least one data-track attribute.")
    parser.add_argument("--require-mobile-css", action="store_true", help="Require an @media max-width rule in CSS.")
    parser.add_argument("--forbid-placeholder-links", action="store_true", help="Fail on href='#' or javascript:void(0).")
    args = parser.parse_args()

    html = Path(args.html).read_text(encoding="utf-8")
    css = read_optional(args.css)
    js = read_optional(args.js)
    combined = "\n".join([html, css, js])

    site = SiteParser()
    site.feed(html)
    failures = []

    add_failure(failures, bool(site.title.strip()), "Missing <title>.")
    add_failure(failures, bool(site.meta.get("description")), "Missing meta description.")
    add_failure(failures, site.meta.get("viewport") is not None, "Missing viewport meta tag.")
    add_failure(failures, sum(1 for tag, _ in site.headings if tag == "h1") == 1, "Expected exactly one H1.")

    for image in site.images:
        add_failure(failures, bool(image.get("src") or image.get("srcset")), f"Image missing source: {image}")
        add_failure(failures, bool(image.get("alt")), f"Image missing alt text: {image}")

    for link in site.links:
        href = link.get("href", "")
        add_failure(failures, bool(href), f"Link missing href: {link}")
        if args.forbid_placeholder_links:
            add_failure(failures, href not in {"#", "javascript:void(0)"}, f"Placeholder link remains: {link}")

    for block in site.json_ld_blocks:
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            failures.append(f"Invalid JSON-LD: {exc}")

    for required_id in args.required_id:
        add_failure(failures, required_id in site.ids, f"Missing required id: {required_id}")

    for text in args.required_text:
        add_failure(failures, text in combined, f"Missing required text: {text}")

    for text in args.forbidden_text:
        add_failure(failures, text not in combined, f"Forbidden or unverified text present: {text}")

    product_links = [link for link in site.links if "/products/" in link.get("href", "")]
    add_failure(
        failures,
        len(product_links) >= args.min_product_links,
        f"Expected at least {args.min_product_links} product links, found {len(product_links)}.",
    )

    if args.require_tracking:
        add_failure(failures, bool(site.data_tracks), "Missing data-track attributes.")

    if args.require_mobile_css:
        add_failure(failures, bool(re.search(r"@media[^{]+max-width", css)), "Missing max-width mobile media query.")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("PASS")
    print(f"Images checked: {len(site.images)}")
    print(f"Links checked: {len(site.links)}")
    print(f"Product links checked: {len(product_links)}")
    print(f"Tracking hooks checked: {len(site.data_tracks)}")
    print(f"JSON-LD blocks checked: {len(site.json_ld_blocks)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
