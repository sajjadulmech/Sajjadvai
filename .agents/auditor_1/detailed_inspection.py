import os
import sys
import re
from bs4 import BeautifulSoup

# Ensure utf-8 output encoding for Windows terminal
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from tests.test_utils import load_articles_data

articles = {a['id']: a for a in load_articles_data()}

def inspect_article_content(aid, title):
    art = articles[aid]
    soup = BeautifulSoup(art['contentHtml'], 'html.parser')
    print(f"\n=======================================================")
    print(f"GUIDE {aid:02d}: {art['title']}")
    print(f"=======================================================")
    print("Category:", art['category'])
    print("Excerpt:", art['excerpt'])
    print("Tags:", art['tags'])
    
    # Print all H2 headings
    h2s = [h.get_text().strip() for h in soup.find_all('h2')]
    print(f"H2 Headings ({len(h2s)}):", h2s)
    
    # Print spec boxes
    specs = [s.get_text().strip() for s in soup.find_all('div', class_='ctl-spec-box')]
    print("Spec boxes count:", len(specs))
    for idx, s in enumerate(specs, 1):
        print(f"  Spec #{idx}:", s[:150].replace('\n', ' '))
        
    # Print tables summary
    tables = soup.find_all('div', class_='ctl-table-wrapper')
    print("Tables count:", len(tables))
    for idx, t in enumerate(tables, 1):
        headers = [th.get_text().strip() for th in t.find_all('th')]
        rows = t.find_all('tr')
        print(f"  Table #{idx} Headers ({len(headers)} cols, {len(rows)} rows):", headers)
        
    # Print FAQs
    faqs = soup.find_all('div', class_='ctl-faq-item')
    print("FAQs count:", len(faqs))
    for idx, f in enumerate(faqs, 1):
        q = f.find(['h3', 'h4', 'strong', 'p'])
        q_text = q.get_text().strip() if q else "No title"
        print(f"  FAQ #{idx} Question:", q_text)

for aid in range(1, 21):
    inspect_article_content(aid, articles[aid]['title'])
