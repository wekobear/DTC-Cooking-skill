"""Exercise the public CLI against representative false-positive regressions."""

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "static_site_audit.py"


class StaticAuditTests(unittest.TestCase):
    def audit(self, body="", *args, css="", js="", viewport="width=device-width, initial-scale=1"):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            html = (
                '<!doctype html><html><head><title>Store</title>'
                '<meta name="description" content="Product page">'
                f'<meta name="viewport" content="{viewport}">'
                f'</head><body><h1>Products</h1>{body}</body></html>'
            )
            (root / "index.html").write_text(html, encoding="utf-8")
            (root / "styles.css").write_text(css, encoding="utf-8")
            (root / "app.js").write_text(js, encoding="utf-8")
            return subprocess.run(
                [sys.executable, str(SCRIPT), str(root / "index.html"),
                 "--css", str(root / "styles.css"), "--js", str(root / "app.js"), *args],
                text=True, capture_output=True, check=False,
            )

    def test_comments_and_source_code_cannot_satisfy_page_checks(self):
        result = self.audit(
            '<!-- Free returns <button data-track="buy">Buy</button> -->'
            '<script>const offer = "Free returns";</script>'
            '<template>Free returns</template>',
            "--required-text", "Free returns", "--require-tracking", "--require-mobile-css",
            css='/* @media (max-width: 700px) {} */ .label::after { content: "@media (max-width: 700px) {} Free returns"; }',
            js='// Free returns\nconst message = "Free returns";',
        )
        self.assertEqual(result.returncode, 1, result.stderr)
        for failure in ("Missing required text", "Missing nonempty data-track", "Missing max-width mobile media query"):
            self.assertIn(failure, result.stdout)

    def test_placeholder_link_variants_fail(self):
        for href in ("#", "javascript:void(0)", "javascript:void(0);", " JavaScript: void ( 0 ) ; "):
            with self.subTest(href=href):
                result = self.audit(f'<a href="{href}">Buy</a>', "--forbid-placeholder-links")
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn("Placeholder link remains", result.stdout)

    def test_empty_viewport_and_empty_tracking_fail(self):
        result = self.audit('<button data-track="   ">Buy</button>', "--require-tracking", viewport=" ")
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("Missing or empty viewport", result.stdout)
        self.assertIn("Missing nonempty data-track", result.stdout)

    def test_repeated_product_and_variant_links_count_once(self):
        result = self.audit(
            '<a href="/products/chair">Chair</a>'
            '<a href="/products/chair">Buy chair</a>'
            '<a href="/products/chair?variant=blue#details">Blue chair</a>'
            '<a href="/products/chair/">Chair details</a>'
            '<a href="javascript:/products/desk">Invalid product</a>',
            "--min-product-links", "2",
        )
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("unique product destinations, found 1", result.stdout)

    def test_explicit_decorative_images_allow_empty_alt(self):
        result = self.audit(
            '<img src="divider.svg" alt="" role="presentation">'
            '<img src="shape.svg" alt="" role="none">'
            '<img src="pattern.svg" alt="" aria-hidden="true">'
            '<img src="chair.jpg" alt="Blue chair">'
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_informative_images_and_missing_alt_still_fail(self):
        for image in ('<img src="chair.jpg" alt="">', '<img src="divider.svg" role="presentation">'):
            with self.subTest(image=image):
                result = self.audit(image)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertIn("Image missing alt text", result.stdout)

    def test_real_markup_passes_with_explicit_runtime_limit(self):
        result = self.audit(
            '<p>Free <strong>returns</strong> &amp; shipping</p>'
            '<a href="/products/chair">Chair</a><a href="/products/desk">Desk</a>'
            '<button id="buy" data-track="buy">Buy</button>'
            '<style>@media (max-width: 700px) { body { width: 100%; } }</style>',
            "--required-id", "buy", "--required-text", "Free returns & shipping",
            "--min-product-links", "2", "--require-tracking", "--require-mobile-css",
            "--forbid-placeholder-links",
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(result.stdout.startswith("PASS\n"))
        for limit in ("Static checks only", "mobile usability", "received analytics events", "production deployment"):
            self.assertIn(limit, result.stdout)

    def test_existing_json_and_claim_checks_still_fail(self):
        result = self.audit('<script type="application/ld+json">{bad}</script><p>Guaranteed outcome</p>',
                            "--forbidden-text", "Guaranteed outcome")
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("Invalid JSON-LD", result.stdout)
        self.assertIn("Forbidden or unverified text", result.stdout)
        self.assertIn("Static checks only", result.stdout)


if __name__ == "__main__":
    unittest.main()
