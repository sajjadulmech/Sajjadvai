import sys
import os
import re

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from tests.test_utils import load_articles_data

articles = load_articles_data()
print(f"Total articles loaded: {len(articles)}")
for a in articles:
    links = re.findall(r'openArticleModal\(\s*(\d+)\s*\)', a['contentHtml'])
    print(f"Guide {a['id']:02d} ({a['slug']}): links={links}")
