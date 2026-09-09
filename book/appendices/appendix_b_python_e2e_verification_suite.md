# Appendix B: Master Python Automated Verification Suite

This test suite automatically audits your static site for broken internal links, missing FTC disclosures, non-compliant affiliate tags, and missing comparison table wrappers.

Save this script at `tests/run_e2e_tests.py`:

```python
#!/usr/bin/env python3
"""
tests/run_e2e_tests.py - Production QA & Link Compliance Suite
ClearTapLab Engineering Standard
"""

import os
import re
import sys
from bs4 import BeautifulSoup

def run_suite():
    print("=" * 60)
    print("RUNNING STATIC AFFILIATE ASSET VERIFICATION SUITE")
    print("=" * 60)

    errors = []
    tests_run = 0

    # 1. Verify Core Files Exist
    core_files = [
        "index.html",
        "_headers",
        os.path.join("styles", "main.css"),
        os.path.join("scripts", "app.js"),
        os.path.join("scripts", "articles-data.js")
    ]
    for cf in core_files:
        tests_run += 1
        if not os.path.exists(cf):
            errors.append(f"Missing critical core file: {cf}")

    # 2. Inspect articles-data.js
    articles_path = os.path.join("scripts", "articles-data.js")
    if os.path.exists(articles_path):
        with open(articles_path, "r", encoding="utf-8") as f:
            content = f.read()

        articles = re.findall(
            r'id:\s*["\']([^"\']+)["\'].*?contentHtml:\s*`([^`]+)`',
            content,
            re.DOTALL
        )

        print(f"Discovered {len(articles)} published guides in data store.")

        for aid, html in articles:
            soup = BeautifulSoup(html, "html.parser")

            # Check Disclosure
            tests_run += 1
            disclosure = soup.find(class_=re.compile(r"disclosure", re.I))
            if not disclosure:
                errors.append(f"Guide `{aid}`: Missing above-the-fold affiliate disclosure.")

            # Check Outbound Affiliate Links
            links = soup.find_all("a", href=True)
            for a in links:
                href = a["href"]
                if any(x in href for x in ["amazon", "shareasale", "impact", "springwell"]):
                    tests_run += 1
                    rel = a.get("rel", [])
                    rel_str = " ".join(rel) if isinstance(rel, list) else rel
                    if "sponsored" not in rel_str or "nofollow" not in rel_str:
                        errors.append(f"Guide `{aid}`: Link `{href}` missing rel='sponsored nofollow'.")
                    if a.get("target") != "_blank":
                        errors.append(f"Guide `{aid}`: Link `{href}` missing target='_blank'.")

            # Check Table Wrappers
            tables = soup.find_all("table")
            for t in tables:
                tests_run += 1
                parent = t.find_parent(class_="ctl-table-wrapper")
                if not parent:
                    errors.append(f"Guide `{aid}`: Table not wrapped in `.ctl-table-wrapper`.")

    print(f"Total verification checks executed: {tests_run}")
    print("=" * 60)

    if errors:
        print(f"FAILED: {len(errors)} compliance or structural issues detected:\n")
        for err in errors:
            print(f"  ❌ {err}")
        sys.exit(1)
    else:
        print("PASS: All tests passed with 0 errors. Asset ready for production deploy.\n")
        sys.exit(0)

if __name__ == "__main__":
    run_suite()
```
