#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit


STATIC_SCOPE = (
    "Static checks only: this result does not prove mobile usability, visible text, "
    "working interactions, received analytics events, or a successful production deployment."
)


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
        self.document_text = []
        self.inline_css = []
        self._excluded_text_tags = []
        self._in_style = False
        self._script_type = None
        self._script_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"head", "title", "script", "style", "template"}:
            self._excluded_text_tags.append(tag)
        if tag == "style":
            self._in_style = True
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
        if (attrs.get("data-track") or "").strip():
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
        if self._in_style:
            self.inline_css.append(data)
        if not self._excluded_text_tags:
            self.document_text.append(data)

    def handle_endtag(self, tag):
        if tag in self._excluded_text_tags:
            self._excluded_text_tags.remove(tag)
        if tag == "style":
            self._in_style = False
        if tag == "title":
            self._in_title = False
        if tag == "script":
            if self._script_type == "application/ld+json":
                self.json_ld_blocks.append("".join(self._script_text).strip())
            self._script_type = None
            self._script_text = []


def read_optional(path: str | None) -> str:
    return Path(path).read_text(encoding="utf-8") if path else ""


def add_failure(failures: list[str], condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)


def css_rule_text(css: str) -> str:
    """Mask comments and strings so their contents cannot impersonate CSS rules."""
    return re.sub(r'/\*.*?(?:\*/|$)|"(?:\\.|[^"\\])*"|\'(?:\\.|[^\'\\])*\'', " ", css, flags=re.DOTALL)


def is_placeholder_link(href: str) -> bool:
    return href == "#" or bool(re.fullmatch(r"javascript\s*:\s*void\s*\(\s*0\s*\)\s*;?", href, re.IGNORECASE))


def product_destination(href: str) -> str | None:
    """Count product destinations once, including their query/fragment variants."""
    try:
        url = urlsplit(href)
    except ValueError:
        return None
    if url.scheme.lower() not in {"", "http", "https"} or "/products/" not in url.path:
        return None
    if not url.path.split("/products/", 1)[1].strip("/"):
        return None
    return urlunsplit((url.scheme.lower(), url.netloc.lower(), url.path.rstrip("/"), "", ""))


def main() -> int:
    parser = argparse.ArgumentParser(description="Run generic static checks for a local ecommerce page.", epilog=STATIC_SCOPE)
    parser.add_argument("html", help="Path to the HTML file to inspect.")
    parser.add_argument("--css", help="Optional CSS file to inspect.")
    parser.add_argument("--js", help="Optional JS file to inspect.")
    parser.add_argument("--required-id", action="append", default=[], help="Required element id. Repeat as needed.")
    parser.add_argument("--required-text", action="append", default=[], help="Required document text, excluding comments, head, scripts, styles and templates. Repeat as needed.")
    parser.add_argument("--forbidden-text", action="append", default=[], help="Forbidden or unverified claim. Repeat as needed.")
    parser.add_argument("--min-product-links", type=int, default=0, help="Minimum unique /products/ destinations, ignoring query strings and fragments.")
    parser.add_argument("--require-tracking", action="store_true", help="Require at least one nonempty data-track attribute; does not verify event delivery.")
    parser.add_argument("--require-mobile-css", action="store_true", help="Require a max-width media query in supplied or inline CSS; does not verify mobile usability.")
    parser.add_argument("--forbid-placeholder-links", action="store_true", help="Fail on href='#' or javascript:void(0), including whitespace and a trailing semicolon.")
    args = parser.parse_args()

    html = Path(args.html).read_text(encoding="utf-8")
    css = read_optional(args.css)
    js = read_optional(args.js)
    combined = "\n".join([html, css, js])

    site = SiteParser()
    site.feed(html)
    site.close()
    document_text = re.sub(r"\s+", " ", "".join(site.document_text)).strip()
    failures = []

    add_failure(failures, bool(site.title.strip()), "Missing <title>.")
    add_failure(failures, bool((site.meta.get("description") or "").strip()), "Missing or empty meta description.")
    add_failure(failures, bool((site.meta.get("viewport") or "").strip()), "Missing or empty viewport meta content.")
    add_failure(failures, sum(1 for tag, _ in site.headings if tag == "h1") == 1, "Expected exactly one H1.")

    for image in site.images:
        add_failure(failures, bool(image.get("src") or image.get("srcset")), f"Image missing source: {image}")
        alt = image.get("alt")
        decorative = (image.get("role") or "").lower() in {"none", "presentation"} or (image.get("aria-hidden") or "").lower() == "true"
        add_failure(failures, alt is not None and (bool(alt.strip()) or decorative), f"Image missing alt text (empty alt requires explicit decorative markup): {image}")

    for link in site.links:
        href = (link.get("href") or "").strip()
        add_failure(failures, bool(href), f"Link missing href: {link}")
        if args.forbid_placeholder_links:
            add_failure(failures, not is_placeholder_link(href), f"Placeholder link remains: {link}")

    for block in site.json_ld_blocks:
        try:
            json.loads(block)
        except json.JSONDecodeError as exc:
            failures.append(f"Invalid JSON-LD: {exc}")

    for required_id in args.required_id:
        add_failure(failures, required_id in site.ids, f"Missing required id: {required_id}")

    for text in args.required_text:
        add_failure(failures, re.sub(r"\s+", " ", text).strip() in document_text, f"Missing required text: {text}")

    for text in args.forbidden_text:
        add_failure(failures, text not in combined, f"Forbidden or unverified text present: {text}")

    product_links = {destination for link in site.links if (destination := product_destination((link.get("href") or "").strip()))}
    add_failure(
        failures,
        len(product_links) >= args.min_product_links,
        f"Expected at least {args.min_product_links} unique product destinations, found {len(product_links)}.",
    )

    if args.require_tracking:
        add_failure(failures, bool(site.data_tracks), "Missing nonempty data-track attributes.")

    if args.require_mobile_css:
        rules = css_rule_text("\n".join([css, *site.inline_css]))
        add_failure(failures, bool(re.search(r"@media\b[^{;]*\(\s*max-width\s*:\s*[^)]+\)", rules, re.IGNORECASE)), "Missing max-width mobile media query.")

    if failures:
        print("FAIL")
        for failure in failures:
            print(f"- {failure}")
        print(STATIC_SCOPE)
        return 1

    print("PASS")
    print(f"Images checked: {len(site.images)}")
    print(f"Links checked: {len(site.links)}")
    print(f"Unique product destinations checked: {len(product_links)}")
    print(f"Tracking hooks checked: {len(site.data_tracks)}")
    print(f"JSON-LD blocks checked: {len(site.json_ld_blocks)}")
    print(STATIC_SCOPE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
