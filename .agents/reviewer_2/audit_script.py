import sys
import os
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from tests.test_utils import load_articles_data, load_index_html
from bs4 import BeautifulSoup
from collections import Counter

articles = load_articles_data()
print(f"Total articles: {len(articles)}")

cat_counts = Counter(a['category'] for a in articles)
for cat, count in sorted(cat_counts.items()):
    print(f"Category {cat}: {count} guides")

print("\n--- Detailed Per-Article Breakdown ---")
for a in articles:
    soup = BeautifulSoup(a['contentHtml'], 'html.parser')
    tables = soup.find_all('table')
    wrappers = soup.find_all(class_='ctl-table-wrapper')
    spec_boxes = soup.find_all(class_='ctl-spec-box')
    faqs = soup.find_all('details')
    if not faqs:
        faqs = soup.find_all(class_='ctl-faq-item')
    authors = soup.find_all(class_='ctl-author-box')
    words = len(soup.get_text().split())
    
    # Check table wrapping
    unwrapped_tables = 0
    for t in tables:
        parent = t.parent
        if not parent or 'ctl-table-wrapper' not in parent.get('class', []):
            unwrapped_tables += 1
            
    print(f"ID {a['id']:02d}: {a['category']:22s} | Words: {words:4d} | Tables: {len(tables)} (Unwrapped: {unwrapped_tables}) | Specs: {len(spec_boxes)} | FAQs: {len(faqs)} | Authors: {len(authors)} | Tags: {len(a['tags'])}")

print("\n--- Category Listing ---")
for cat in sorted(cat_counts.keys()):
    cat_articles = [a for a in articles if a['category'] == cat]
    ids = [a['id'] for a in cat_articles]
    titles = [f"ID {a['id']}: {a['title']}" for a in cat_articles]
    print(f"\n[{cat}] ({len(cat_articles)} guides): IDs {ids}")
    for t in titles:
        print(f"  - {t}")
