"""
Inspect how chemical formulas and standards are represented in HTML
"""
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
from tests.test_utils import load_articles_data

articles = load_articles_data()

for a in articles:
    aid = a["id"]
    title = a["title"]
    html = a["contentHtml"]
    print(f"\n--- Guide {aid:02d}: {title} ---")
    
    # Check for chemical formulas & math
    chems = re.findall(r'(?:Fe\S+|Ca\S+|Mg\S+|H2S|H₂S|SO4\S+|CaCO3\S+|CO2\S+|PFAS|PFOA|PFOS|TTHM|HAA5|Darcy|Ergun|Bernoulli|EBCT|GPG|PPM|PPB|PPT|MCL|MCLG|NSF\s*\d+|ANSI\s*\d+|DVGW|WQA|EPA)', html, re.IGNORECASE)
    print(f"Sample Chemical/Standard/Physics Tokens ({len(chems)} found): {set(chems[:20])}")
