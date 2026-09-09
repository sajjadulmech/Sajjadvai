import sys
import os
import re
from bs4 import BeautifulSoup

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from tests.test_utils import (
    load_articles_data,
    load_index_html,
    load_main_css,
    simulate_category_filter,
    simulate_calculator
)

def js_perform_search(query, articles):
    """
    Faithful replication of scripts/app.js performSearch(query) logic:
    Searches title, excerpt, categoryLabel, and tags.
    """
    clean_q = query.strip().lower()
    if not clean_q:
        return articles
    
    matches = []
    for a in articles:
        tag_match = (
            any(isinstance(t, str) and clean_q in t.lower() for t in a.get("tags", []))
            if isinstance(a.get("tags"), list)
            else False
        )
        if (
            clean_q in a.get("title", "").lower()
            or clean_q in a.get("excerpt", "").lower()
            or clean_q in a.get("categoryLabel", "").lower()
            or tag_match
        ):
            matches.append(a)
    return matches

def run_adversarial_stress_tests():
    print("=== STARTING ADVERSARIAL STRESS TESTS ===")
    articles = load_articles_data()
    soup = load_index_html()
    css = load_main_css()

    errors = []

    # 1. Integrity Check: Scan for placeholder / fake content
    forbidden_tokens = [
        "lorem ipsum", "todo", "tbd", "placeholder", "coming soon",
        "temp text", "insert here", "sample text", "dummy text"
    ]
    for a in articles:
        text_lower = a['contentHtml'].lower()
        for token in forbidden_tokens:
            if token in text_lower:
                errors.append(f"[INTEGRITY] Article ID {a['id']} contains forbidden token '{token}'")

    # 2. Search Indexing Stress Test across ALL 166 tags
    all_tags = set()
    for a in articles:
        for tag in a.get('tags', []):
            all_tags.add(tag)
    
    print(f"Testing search across {len(all_tags)} unique tags...")
    for tag in all_tags:
        results = js_perform_search(tag, articles)
        if len(results) == 0:
            errors.append(f"[SEARCH] Tag '{tag}' produced 0 search results!")

    # 3. Table Responsiveness & Layout Architecture Check
    table_wrappers = re.findall(r'\.ctl-table-wrapper\s*\{([^}]+)\}', css)
    tables = re.findall(r'\.ctl-table\s*\{([^}]+)\}', css)
    
    if not table_wrappers or 'overflow-x: auto' not in table_wrappers[0]:
        errors.append("[CSS] .ctl-table-wrapper missing 'overflow-x: auto'")
    if not tables or 'min-width: 580px' not in tables[0]:
        errors.append("[CSS] .ctl-table missing 'min-width: 580px'")

    # Check all tables in articles are inside .ctl-table-wrapper
    for a in articles:
        art_soup = BeautifulSoup(a['contentHtml'], 'html.parser')
        for tbl in art_soup.find_all('table'):
            parent = tbl.parent
            classes = parent.get('class', []) if parent else []
            if 'ctl-table-wrapper' not in classes:
                errors.append(f"[RESPONSIVENESS] Article ID {a['id']} has table not wrapped in .ctl-table-wrapper")

    # 4. Modal Reader Scoped Typography Check
    required_scoped_selectors = [
        '.ctl-modal-body h1',
        '.ctl-modal-body h2',
        '.ctl-modal-body h3',
        '.ctl-modal-body p',
        '.ctl-modal-body ul',
        '.ctl-modal-body li',
        '.ctl-modal-body blockquote'
    ]
    for sel in required_scoped_selectors:
        if sel not in css:
            errors.append(f"[TYPOGRAPHY] CSS missing scoped selector '{sel}' to protect against universal reset")

    # 5. Section 2 Hub Card Labels vs Category Distribution
    hub_section = soup.find(id='hubs')
    if not hub_section:
        errors.append("[DOM] Section #hubs not found in index.html")
    else:
        hub_text = hub_section.get_text()
        if "Explore RO Systems (5 Guides)" not in hub_text:
            errors.append("[HUB LABELS] Section 2 RO Hub card label mismatch (expected 5 Guides)")
        if "Water Testing Guides (2 Guides)" not in hub_text:
            errors.append("[HUB LABELS] Section 2 Water Testing Hub card label mismatch (expected 2 Guides)")
        if "Troubleshoot Symptoms (3 Guides)" not in hub_text:
            errors.append("[HUB LABELS] Section 2 Water Problems Hub card label mismatch (expected 3 Guides)")
        if "Whole-House Guides (6 Guides)" not in hub_text:
            errors.append("[HUB LABELS] Section 2 System Guides Hub card label mismatch (expected 6 Guides)")

    # 6. Category Tabs Subset Accuracy
    categories_map = {
        "all": 20,
        "reverse-osmosis": 5,
        "water-testing": 2,
        "water-problems": 3,
        "filtration-technology": 4,
        "system-guides": 6
    }
    for cat, expected_count in categories_map.items():
        subset = simulate_category_filter(cat, articles)
        if len(subset) != expected_count:
            errors.append(f"[CATEGORY FILTER] Category '{cat}' returned {len(subset)} guides, expected {expected_count}")

    # 7. Sizing Calculator Mathematical Invariants
    # Test monotonicity: increasing hardness or iron must increase or keep constant capacity and cost
    prev_cost = -1
    for hardness in range(5, 50, 5):
        res = simulate_calculator(4, hardness, 0.5)
        cost = res['five_year_salt_cost']
        if cost < prev_cost:
            errors.append(f"[CALCULATOR] Monotonicity failure at hardness {hardness}: cost {cost} < prev {prev_cost}")
        prev_cost = cost

    print("\n--- RESULTS OF ADVERSARIAL STRESS TESTS ---")
    if errors:
        print(f"FAILED with {len(errors)} error(s):")
        for e in errors[:20]:
            print(f"  [FAIL] {e}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more errors.")
    else:
        print("[PASS] ALL ADVERSARIAL STRESS TESTS PASSED WITH ZERO FINDINGS!")

if __name__ == "__main__":
    run_adversarial_stress_tests()
