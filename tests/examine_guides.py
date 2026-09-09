"""
Detailed Content Auditor for ClearTapLab 20 Guides
"""
import os
import re
import sys
from bs4 import BeautifulSoup

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from tests.test_utils import load_articles_data

articles = load_articles_data()

for a in articles:
    gid = a["id"]
    title = a["title"]
    soup = BeautifulSoup(a["contentHtml"], "html.parser")
    text = soup.get_text(" ", strip=True)
    words = len(re.findall(r"\b\w+\b", text))
    
    h2s = [h.get_text().strip() for h in soup.find_all("h2")]
    spec_boxes = [sb.get_text(" ", strip=True) for sb in soup.find_all(class_=re.compile(r"ctl-spec-box"))]
    tables = soup.find_all(class_=re.compile(r"ctl-table-wrapper"))
    author_box = soup.find(class_=re.compile(r"ctl-author-box"))
    author_text = author_box.get_text(" ", strip=True) if author_box else "None"
    
    print(f"==================== GUIDE {gid:02d}: {title} ====================")
    print(f"Word Count: {words} | Category: {a['category']} | Slug: {a['slug']}")
    print("H2 Sections:")
    for h in h2s:
        print(f"  - {h}")
    print(f"Tables Found: {len(tables)}")
    for i, t in enumerate(tables, 1):
        tbl = t.find("table")
        if tbl:
            headers = [th.get_text().strip() for th in tbl.find_all("th")]
            rows = len(tbl.find_all("tr"))
            print(f"  Table {i}: Headers={headers} | Total Rows={rows}")
    print(f"Spec Boxes: {len(spec_boxes)}")
    for i, sb in enumerate(spec_boxes, 1):
        print(f"  Spec Box {i}: {sb[:150]}...")
    print(f"Author Box: {author_text[:120]}...")
    print()
