"""
Comprehensive Deep Audit of All 20 ClearTapLab Guides
"""

import os
import sys
import json
import re
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
from tests.test_utils import load_articles_data

articles = load_articles_data()
print(f"Loaded {len(articles)} articles.")

audit_results = []
all_valid = True

for a in articles:
    aid = a["id"]
    slug = a["slug"]
    title = a["title"]
    cat = a["category"]
    cat_lbl = a["categoryLabel"]
    read_time = a["readTime"]
    badge_class = a["badgeClass"]
    excerpt = a["excerpt"]
    tags = a["tags"]
    html = a["contentHtml"]
    
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    words = re.findall(r'\b[\w\-\'\u00C0-\u017F]+\b', text)
    word_count = len(words)
    
    h1 = soup.find("h1")
    h1_text = h1.get_text(strip=True) if h1 else None
    
    badge = soup.find(class_=re.compile(r'ctl-badge-pill'))
    badge_text = badge.get_text(strip=True) if badge else None
    
    spec_boxes = soup.find_all(class_="ctl-spec-box")
    spec_box_count = len(spec_boxes)
    
    table_wrappers = soup.find_all(class_="ctl-table-wrapper")
    tables = soup.find_all("table", class_="ctl-table")
    table_count = len(tables)
    
    # Check table rows & cols
    table_valid = True
    for t in tables:
        rows = t.find_all("tr")
        headers = t.find_all("th")
        if len(rows) < 2 or len(headers) < 2:
            table_valid = False
            
    faq_section = soup.find(class_="ctl-faq-section")
    faq_items = soup.find_all(class_="ctl-faq-item")
    faq_count = len(faq_items)
    
    author_box = soup.find(class_="ctl-author-box")
    author_name = author_box.find("h4").get_text(strip=True) if (author_box and author_box.find("h4")) else None
    author_role = author_box.find(class_="ctl-author-role").get_text(strip=True) if (author_box and author_box.find(class_="ctl-author-role")) else None
    
    spa_links = [int(m) for m in re.findall(r'openArticleModal\((\d+)\)', html)]
    formula_boxes = soup.find_all(class_="ctl-formula-box")
    code_blocks = soup.find_all(class_="ctl-code-block")
    
    # Check for placeholder strings
    placeholders_found = []
    for pattern in [r'lorem\s+ipsum', r'\bTODO\b', r'\bTBD\b', r'coming\s+soon', r'under\s+construction', r'placeholder', r'\[insert', r'\[link']:
        matches = re.findall(pattern, html, re.IGNORECASE)
        if matches:
            placeholders_found.extend(matches)
            
    guide_status = {
        "id": aid,
        "slug": slug,
        "title": title,
        "category": cat,
        "categoryLabel": cat_lbl,
        "readTime": read_time,
        "badgeClass": badge_class,
        "wordCount": word_count,
        "tagCount": len(tags),
        "hasH1": bool(h1),
        "h1Text": h1_text,
        "hasBadge": bool(badge),
        "badgeText": badge_text,
        "specBoxCount": spec_box_count,
        "tableCount": table_count,
        "tableWrappersCount": len(table_wrappers),
        "tableValid": table_valid,
        "faqCount": faq_count,
        "hasFaqSection": bool(faq_section),
        "hasAuthorBox": bool(author_box),
        "authorName": author_name,
        "authorRole": author_role,
        "spaLinkCount": len(spa_links),
        "spaLinks": spa_links,
        "formulaBoxCount": len(formula_boxes),
        "codeBlockCount": len(code_blocks),
        "placeholders": placeholders_found,
        "passedAllChecks": (
            word_count >= 1000 and
            bool(h1) and
            bool(badge) and
            spec_box_count >= 1 and
            table_count >= 1 and
            len(table_wrappers) >= table_count and
            table_valid and
            faq_count >= 3 and
            bool(author_box) and
            len(spa_links) >= 1 and
            len(placeholders_found) == 0 and
            len(tags) >= 5
        )
    }
    
    if not guide_status["passedAllChecks"]:
        all_valid = False
        print(f"FAILED GUIDE {aid}: {guide_status}")
    else:
        print(f"Guide {aid:02d} [PASS] | {word_count} words | {table_count} tables | {spec_box_count} spec boxes | {faq_count} FAQs | {len(spa_links)} SPA links | Author: {author_name} ({author_role})")
        
    audit_results.append(guide_status)

print("\n" + "=" * 60)
print(f"ALL 20 GUIDES AUDIT RESULT: {'100% PASSED' if all_valid else 'FAILED'}")
print("=" * 60)

with open(".agents/victory_auditor_1/guides_deep_audit.json", "w", encoding="utf-8") as f:
    json.dump(audit_results, f, indent=2)
