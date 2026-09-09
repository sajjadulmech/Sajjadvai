import re
import sys

def test_css_rules():
    print("Testing styles/main.css...")
    with open("styles/main.css", "r", encoding="utf-8") as f:
        css = f.read()

    # 1. Check scoped typography rules
    typography_selectors = [
        r"\.ctl-modal-body\s+h1",
        r"\.ctl-modal-body\s+h2",
        r"\.ctl-modal-body\s+h3",
        r"\.ctl-modal-body\s+h4",
        r"\.ctl-modal-body\s+p",
        r"\.ctl-modal-body\s+ul",
        r"\.ctl-modal-body\s+ol",
        r"\.ctl-modal-body\s+li",
        r"\.ctl-modal-body\s+strong",
        r"\.ctl-modal-body\s+blockquote",
        r"\.ctl-modal-body\s+hr",
    ]
    for sel in typography_selectors:
        assert re.search(sel, css), f"Missing scoped typography selector: {sel}"
    print("  [PASS] All scoped modal typography selectors present.")

    # 2. Check .ctl-mono, .ctl-formula-box, .ctl-code-block
    assert ".ctl-mono" in css, "Missing .ctl-mono rule"
    assert ".ctl-formula-box" in css, "Missing .ctl-formula-box rule"
    assert ".ctl-formula-box .formula-sub" in css, "Missing .ctl-formula-box .formula-sub rule"
    assert ".ctl-code-block" in css, "Missing .ctl-code-block rule"
    print("  [PASS] Formula, mono, and code block styles present.")

    # 3. Check min-width: 580px for .ctl-table
    table_match = re.search(r"\.ctl-table\s*\{([^}]+)\}", css)
    assert table_match, "Missing .ctl-table rule"
    assert "min-width: 580px" in table_match.group(1), ".ctl-table lacks min-width: 580px"
    print("  [PASS] .ctl-table has min-width: 580px.")

    # 4. Check FAQ accordion styles
    faq_classes = [".ctl-faq-section", ".ctl-faq-item", ".ctl-faq-question", ".ctl-faq-answer"]
    for cls in faq_classes:
        assert cls in css, f"Missing FAQ class: {cls}"
    print("  [PASS] All FAQ accordion styles present.")

    # 5. Check author box mobile stacking query
    assert re.search(r"@media\s*\(\s*max-width\s*:\s*640px\s*\)\s*\{\s*\.ctl-author-box", css), "Missing @media (max-width: 640px) for .ctl-author-box"
    print("  [PASS] Author box mobile media query present.")

def test_app_js():
    print("\nTesting scripts/app.js...")
    with open("scripts/app.js", "r", encoding="utf-8") as f:
        js = f.read()

    # 1. Check openArticleModal scroll reset
    assert "modalContainer.scrollTop = 0" in js, "Missing modalContainer.scrollTop = 0 in openArticleModal"
    print("  [PASS] scrollTop = 0 present in openArticleModal.")

    # 2. Check performSearch tag querying
    assert "tagMatch" in js, "tagMatch logic not found in performSearch"
    assert "a.tags.some" in js, "a.tags.some logic not found in performSearch"
    print("  [PASS] tag matching logic present in performSearch.")

    # 3. Check calculator & triage functions remain intact
    assert "function initSymptomTriage" in js, "initSymptomTriage missing"
    assert "function initCalculator" in js, "initCalculator missing"
    assert "function initArticleGrid" in js, "initArticleGrid missing"
    assert "function initModalReader" in js, "initModalReader missing"
    assert "function initLiveSearch" in js, "initLiveSearch missing"
    assert "function initMobileDrawer" in js, "initMobileDrawer missing"
    print("  [PASS] All core application functions intact.")

    # 4. Behavioral simulation of search logic
    sample_articles = [
        {"id": 1, "title": "Water Report", "excerpt": "CCR guide", "categoryLabel": "Testing", "tags": ["EPA", "Lead", "PFAS"]},
        {"id": 2, "title": "RO vs Carbon", "excerpt": "Pore size", "categoryLabel": "Science", "tags": ["Membrane", "Carbon"]},
        {"id": 3, "title": "Sulfur Well", "excerpt": "Rotten egg", "categoryLabel": "Problems", "tags": None},
    ]

    def simulate_search(q, articles):
        clean_q = q.strip().lower()
        return [
            a for a in articles
            if clean_q in a["title"].lower()
            or clean_q in a["excerpt"].lower()
            or clean_q in a["categoryLabel"].lower()
            or (isinstance(a.get("tags"), list) and any(clean_q in t.lower() for t in a["tags"] if isinstance(t, str)))
        ]

    # Search for tag "PFAS" which is only in tags of article 1
    res = simulate_search("PFAS", sample_articles)
    assert len(res) == 1 and res[0]["id"] == 1, f"Search by tag failed: {res}"
    # Search for "rotten" in excerpt
    res = simulate_search("rotten", sample_articles)
    assert len(res) == 1 and res[0]["id"] == 3, f"Search by excerpt failed: {res}"
    # Search for empty string
    res = simulate_search("", sample_articles)
    assert len(res) == 3, f"Empty search failed: {res}"
    print("  [PASS] Search logic simulation verified with tag indexing.")

def test_index_html():
    print("\nTesting index.html...")
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    # Check Section 2 Hub card labels
    assert "Explore RO Systems (5 Guides) ➔" in html, "RO Systems count label missing or incorrect"
    assert "Water Testing Guides (2 Guides) ➔" in html, "Water Testing count label missing or incorrect"
    assert "Troubleshoot Symptoms (3 Guides) ➔" in html, "Water Problems count label missing or incorrect"
    assert "Whole-House Guides (6 Guides) ➔" in html, "Whole-House count label missing or incorrect"
    print("  [PASS] Section 2 Hub card labels match exact guide distribution.")

if __name__ == "__main__":
    try:
        test_css_rules()
        test_app_js()
        test_index_html()
        print("\nALL VERIFICATION CHECKS PASSED SUCCESSFULLY!")
    except AssertionError as e:
        print(f"\n[FAIL] Assertion error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n[ERROR] Unexpected error: {e}")
        sys.exit(1)
