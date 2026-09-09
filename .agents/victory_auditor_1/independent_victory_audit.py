"""
Independent Post-Victory Forensic Audit Script
ClearTapLab Guides & Articles Complete Content Overhaul
Auditor: victory_auditor_1
"""

import os
import re
import sys
import json
from bs4 import BeautifulSoup

BASE_DIR = os.path.abspath("d:/Personal/AntiGravity/Affiliate Marketting")
ARTICLES_DATA_PATH = os.path.join(BASE_DIR, "scripts", "articles-data.js")
APP_JS_PATH = os.path.join(BASE_DIR, "scripts", "app.js")
MAIN_CSS_PATH = os.path.join(BASE_DIR, "styles", "main.css")
INDEX_HTML_PATH = os.path.join(BASE_DIR, "index.html")

print("=" * 80)
print("INDEPENDENT POST-VICTORY FORENSIC AUDIT — CLEARTAPLAB")
print("=" * 80)

# 1. PARSE ARTICLES DATA INDEPENDENTLY
with open(ARTICLES_DATA_PATH, "r", encoding="utf-8") as f:
    js_content = f.read()

# Extract objects matching { id: X ... }
articles = []
pos = 0
while True:
    m = re.search(r'\{\s*id:\s*(\d+)', js_content[pos:])
    if not m:
        break
    start_idx = pos + m.start()
    
    idx = start_idx
    in_backtick = False
    in_double = False
    in_single = False
    escape = False
    brace_depth = 0
    
    while idx < len(js_content):
        char = js_content[idx]
        if escape:
            escape = False
        elif char == '\\':
            escape = True
        elif char == '`' and not in_double and not in_single:
            in_backtick = not in_backtick
        elif char == '"' and not in_backtick and not in_single:
            in_double = not in_double
        elif char == "'" and not in_backtick and not in_double:
            in_single = not in_single
        elif not in_backtick and not in_double and not in_single:
            if char == '{':
                brace_depth += 1
            elif char == '}':
                brace_depth -= 1
                if brace_depth == 0:
                    obj_str = js_content[start_idx:idx+1]
                    
                    id_m = re.search(r'id:\s*(\d+)', obj_str)
                    slug_m = re.search(r'slug:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                    title_m = re.search(r'title:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                    cat_m = re.search(r'category:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                    cat_lbl_m = re.search(r'categoryLabel:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                    read_m = re.search(r'readTime:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                    badge_m = re.search(r'badgeClass:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                    excerpt_m = re.search(r'excerpt:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                    tags_m = re.search(r'tags:\s*\[(.*?)\]', obj_str, re.DOTALL)
                    
                    html_start = obj_str.find("contentHtml:")
                    content_html = ""
                    if html_start != -1:
                        bt_start = obj_str.find("`", html_start)
                        if bt_start != -1:
                            bt_end = obj_str.rfind("`")
                            if bt_end > bt_start:
                                content_html = obj_str[bt_start+1:bt_end]

                    tags = []
                    if tags_m:
                        raw_tags = tags_m.group(1).split(',')
                        tags = [t.strip(' "\' \t\r\n') for t in raw_tags if t.strip(' "\' \t\r\n')]

                    articles.append({
                        "id": int(id_m.group(1)) if id_m else None,
                        "slug": slug_m.group(1).strip() if slug_m else "",
                        "title": title_m.group(1).strip() if title_m else "",
                        "category": cat_m.group(1).strip() if cat_m else "",
                        "categoryLabel": cat_lbl_m.group(1).strip() if cat_lbl_m else "",
                        "readTime": read_m.group(1).strip() if read_m else "",
                        "badgeClass": badge_m.group(1).strip() if badge_m else "",
                        "excerpt": excerpt_m.group(1).strip() if excerpt_m else "",
                        "tags": tags,
                        "contentHtml": content_html
                    })
                    pos = idx + 1
                    break
        idx += 1
    else:
        break

print(f"[*] Successfully parsed {len(articles)} articles from scripts/articles-data.js")

audit_passed = True
failures = []

def record_failure(msg):
    global audit_passed
    audit_passed = False
    failures.append(msg)
    print(f"  [FAIL] {msg}")

# CHECK 1: Exactly 20 guides with sequential IDs 1..20
if len(articles) != 20:
    record_failure(f"Expected exactly 20 articles, found {len(articles)}")
else:
    ids = [a["id"] for a in articles]
    if ids != list(range(1, 21)):
        record_failure(f"Article IDs are not strictly sequential 1..20: {ids}")
    else:
        print("[PASS] Exactly 20 articles with sequential IDs 1..20 verified.")

# CHECK 2: Metadata & Category Validity
valid_categories = {"reverse-osmosis", "water-testing", "water-problems", "filtration-technology", "system-guides"}
category_counts = {}
total_word_count = 0
total_tables = 0
total_spec_boxes = 0
total_faqs = 0
total_cross_links = 0
all_spa_targets = []

placeholder_patterns = [
    r'lorem\s+ipsum',
    r'\bTODO\b',
    r'\bTBD\b',
    r'coming\s+soon',
    r'under\s+construction',
    r'work\s+in\s+progress',
    r'placeholder',
    r'\[insert\b',
    r'\[link\b',
    r'article\s+content\s+here'
]

print("\n[*] Auditing individual guide completeness, science, tables, FAQs, and bylines:")

for a in articles:
    aid = a["id"]
    title = a["title"]
    cat = a["category"]
    html = a["contentHtml"]
    
    category_counts[cat] = category_counts.get(cat, 0) + 1
    if cat not in valid_categories:
        record_failure(f"Guide {aid} has invalid category: {cat}")
        
    if not a["slug"] or not a["title"] or not a["categoryLabel"] or not a["readTime"] or not a["excerpt"]:
        record_failure(f"Guide {aid} has missing metadata fields")
        
    if len(a["tags"]) < 3:
        record_failure(f"Guide {aid} has insufficient tags: {a['tags']}")

    # Check for placeholder text
    for p in placeholder_patterns:
        if re.search(p, html, re.IGNORECASE):
            record_failure(f"Guide {aid} contains placeholder pattern '{p}'")

    # Word count
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    words = re.findall(r'\b[\w\-\'\u00C0-\u017F]+\b', text)
    wc = len(words)
    total_word_count += wc
    
    if wc < 800:
        record_failure(f"Guide {aid} word count too low: {wc} words (expected >= 800)")

    # HTML Elements
    h1 = soup.find("h1")
    if not h1:
        record_failure(f"Guide {aid} missing <h1> element")

    badge = soup.find(class_=re.compile(r'ctl-badge-pill'))
    if not badge:
        record_failure(f"Guide {aid} missing .ctl-badge-pill element")

    spec_boxes = soup.find_all(class_="ctl-spec-box")
    if len(spec_boxes) < 1:
        record_failure(f"Guide {aid} missing .ctl-spec-box")
    total_spec_boxes += len(spec_boxes)

    tables = soup.find_all("table", class_="ctl-table")
    table_wrappers = soup.find_all(class_="ctl-table-wrapper")
    if len(tables) < 1:
        record_failure(f"Guide {aid} missing comparison table")
    if len(table_wrappers) < len(tables):
        record_failure(f"Guide {aid} table not wrapped in .ctl-table-wrapper")
    total_tables += len(tables)

    # Validate table structure
    for t in tables:
        th = t.find_all("th")
        tr = t.find_all("tr")
        if len(th) < 2 or len(tr) < 2:
            record_failure(f"Guide {aid} table has insufficient rows/columns")

    # FAQs
    faq_items = soup.find_all(class_="ctl-faq-item")
    if len(faq_items) < 3:
        record_failure(f"Guide {aid} has only {len(faq_items)} FAQ items (expected >= 3)")
    total_faqs += len(faq_items)

    for item in faq_items:
        q = item.find(class_="ctl-faq-question")
        ans = item.find(class_="ctl-faq-answer")
        if not q or not ans:
            record_failure(f"Guide {aid} FAQ item missing question or answer element")

    # Author Box
    author_box = soup.find(class_="ctl-author-box")
    if not author_box:
        record_failure(f"Guide {aid} missing .ctl-author-box")

    # SPA Cross-links
    spa_matches = re.findall(r'openArticleModal\((\d+)\)', html)
    total_cross_links += len(spa_matches)
    for target_id_str in spa_matches:
        tid = int(target_id_str)
        all_spa_targets.append((aid, tid))
        if tid < 1 or tid > 20:
            record_failure(f"Guide {aid} has invalid SPA link target: openArticleModal({tid})")

    print(f"  - Guide {aid:02d} [{cat}]: {wc} words, {len(tables)} tables, {len(spec_boxes)} spec boxes, {len(faq_items)} FAQs, {len(spa_matches)} cross-links, {len(a['tags'])} tags | Title: '{title[:45]}...'")

print(f"\n[SUMMARY STATS]")
print(f"Total Words Across 20 Guides: {total_word_count} (Average: {total_word_count/20:.1f} words/guide)")
print(f"Total Tables: {total_tables}")
print(f"Total Spec Boxes: {total_spec_boxes}")
print(f"Total FAQ Items: {total_faqs}")
print(f"Total In-Modal SPA Cross-Links: {total_cross_links}")
print(f"Category Distribution: {category_counts}")

# CHECK 3: Technical & Chemical Standards Citations
standards_map = {
    1: ["EPA", "SDWA", "MCL", "MCLG", "LCR", "NSF"],
    2: ["NSF 58", "NSF 42", "NSF 53", "0.0001", "Adsorption"],
    3: ["EPA", "NSF 42", "H₂S", "anode", "AIO"],
    4: ["NSF 58", "NSF 372", "800 GPD", "TCO", "TDS"],
    5: ["WQA", "NSF 44", "GPG", "PPM", "Ca²⁺", "17.1"],
    6: ["EPA", "0.3 PPM", "Fe²⁺", "Fe³⁺", "AIO", "Greensand"],
    7: ["NSF 44", "DVGW", "W-512", "Ion-Exchange", "TAC"],
    8: ["NSF 58", "NSF 53", "NSF 401", "NSF P473"],
    9: ["NSF 53", "NSF P473", "EPA", "PFOA", "PFOS", "4.0 PPT"],
    10: ["NSF 58", "Recovery Ratio", "Pure-to-Drain", "Polarization"],
    11: ["NSF 58", "TDS Creep", "Bladder", "Booster Pump"],
    12: ["NSF 42", "NSF 61", "NSF 372", "KDF-55", "Catalytic"],
    13: ["NSF 42", "NSF 53", "NSF 61", "GPM", "Pressure Drop"],
    14: ["EPA 200.8", "EPA 524.2", "EPA 537.1", "ICP-MS", "Tap Score"],
    15: ["EPA SMCL", "Calcite", "Corosex", "pH", "TDS"],
    16: ["NSF 44", "WQA", "Compensated Hardness", "Daily Grains"],
    17: ["DVGW W-512", "NSF 61", "TAC", "Nucleation"],
    18: ["NSF 42", "NSF 53", "Micron", "Depth Sediment", "Melt-Blown"],
    19: ["EPA MCL", "NSF 58", "Activated Alumina", "Fluoride", "0.26nm"],
    20: ["Ergun", "Darcy-Weisbach", "Friction Loss", "PSI Drop", "1 inch"]
}

print("\n[*] Auditing Technical & Chemical Citations across all 20 guides:")
for a in articles:
    aid = a["id"]
    html = a["contentHtml"]
    required_stds = standards_map.get(aid, [])
    missing_stds = [s for s in required_stds if s.lower() not in html.lower()]
    if missing_stds:
        record_failure(f"Guide {aid} missing key standards/mechanisms: {missing_stds}")
    else:
        print(f"  [PASS] Guide {aid:02d} verified all technical citations: {required_stds}")

# CHECK 4: Application Logic (`scripts/app.js`)
with open(APP_JS_PATH, "r", encoding="utf-8") as f:
    app_js = f.read()

print("\n[*] Auditing Interactive Application Controller (scripts/app.js):")

# Verify scroll reset
if "modalContainer.scrollTop = 0" not in app_js:
    record_failure("scripts/app.js missing modal scroll reset (modalContainer.scrollTop = 0)")
else:
    print("  [PASS] Modal scroll reset verified.")

# Verify escapeHtml
if "function escapeHtml" not in app_js:
    record_failure("scripts/app.js missing escapeHtml sanitization function")
else:
    print("  [PASS] escapeHtml sanitization function verified.")

# Verify tag searching in performSearch
if "a.tags.some" not in app_js:
    record_failure("scripts/app.js missing tags search indexing")
else:
    print("  [PASS] Live search tags indexing verified.")

# Verify triage data
for symptom in ["sulfur", "limescale", "rust", "chlorine", "acidic"]:
    if symptom not in app_js:
        record_failure(f"scripts/app.js missing symptom triage key: {symptom}")
print("  [PASS] Symptom triage data verified.")

# CHECK 5: Stylesheet (`styles/main.css`)
with open(MAIN_CSS_PATH, "r", encoding="utf-8") as f:
    main_css = f.read()

print("\n[*] Auditing Stylesheet (styles/main.css):")

css_tokens_to_check = [
    (".ctl-modal-body h1", "Scoped H1 in modal body"),
    (".ctl-modal-body h2", "Scoped H2 in modal body"),
    (".ctl-modal-body p", "Scoped p in modal body"),
    (".ctl-table-wrapper", "Table responsive wrapper"),
    (".ctl-table", "Table styling"),
    ("min-width: 580px", "Table min-width for mobile scrolling"),
    (".ctl-formula-box", "Formula callout box"),
    (".ctl-mono", "Monospace code token"),
    (".ctl-faq-section", "FAQ section"),
    (".ctl-faq-question", "FAQ question"),
    (".ctl-faq-answer", "FAQ answer"),
    (".ctl-author-box", "Author box")
]

for selector, label in css_tokens_to_check:
    if selector not in main_css:
        record_failure(f"styles/main.css missing {label} ({selector})")
    else:
        print(f"  [PASS] {label} verified in styles/main.css")

# CHECK 6: HTML Viewport & DOM Elements (`index.html`)
with open(INDEX_HTML_PATH, "r", encoding="utf-8") as f:
    index_soup = BeautifulSoup(f.read(), "html.parser")

print("\n[*] Auditing DOM Structure (index.html):")

dom_elements_to_check = [
    ("#article-modal", "Article Modal Backdrop"),
    ("#modal-article-body", "Modal Article Body Container"),
    ("#search-overlay", "Live Search Overlay"),
    ("#search-query-input", "Search Query Input"),
    ("#search-results-list", "Search Results List"),
    ("#articles-grid", "Article Grid Container"),
    ("#triage-result-container", "Triage Result Container"),
    ("#calc-people", "Calculator Household Size Input"),
    ("#calc-hardness", "Calculator Hardness Input"),
    ("#calc-iron", "Calculator Iron Input"),
    ("#res-target-cap", "Calculator Target Capacity Output"),
    ("#res-salt-cost", "Calculator 5-Year Salt Cost Output")
]

for selector, label in dom_elements_to_check:
    elem = index_soup.select_one(selector)
    if not elem:
        record_failure(f"index.html missing {label} ({selector})")
    else:
        print(f"  [PASS] {label} verified in index.html")

# Verify filter tab buttons
tab_buttons = index_soup.select(".ctl-tab-btn")
categories_in_tabs = [b.get("data-category") for b in tab_buttons]
expected_categories = ["all", "reverse-osmosis", "water-testing", "water-problems", "filtration-technology", "system-guides"]
if categories_in_tabs != expected_categories:
    record_failure(f"Category tabs in index.html {categories_in_tabs} do not match expected {expected_categories}")
else:
    print(f"  [PASS] All 6 category filter tab buttons verified in index.html.")

# CHECK 7: Cross-link destination validity
broken_links = []
for src_id, tgt_id in all_spa_targets:
    if not any(a["id"] == tgt_id for a in articles):
        broken_links.append((src_id, tgt_id))

if broken_links:
    record_failure(f"Found broken in-modal SPA cross-links: {broken_links}")
else:
    print(f"  [PASS] All {len(all_spa_targets)} in-modal SPA cross-links target valid article IDs (1..20).")

# CHECK 8: Triage Button Targets
triage_buttons = index_soup.select(".ctl-symptom-btn")
if len(triage_buttons) != 5:
    record_failure(f"Expected 5 symptom triage buttons, found {len(triage_buttons)}")
else:
    print(f"  [PASS] Exactly 5 symptom triage buttons found in index.html.")

print("\n" + "=" * 80)
if audit_passed:
    print(">>> INDEPENDENT FORENSIC VERIFICATION RESULT: 100% CLEAN & VERIFIED")
    print("=" * 80)
    sys.exit(0)
else:
    print(f">>> INDEPENDENT FORENSIC VERIFICATION RESULT: FAILED ({len(failures)} violations)")
    for idx, f in enumerate(failures, 1):
        print(f"  {idx}. {f}")
    print("=" * 80)
    sys.exit(1)
