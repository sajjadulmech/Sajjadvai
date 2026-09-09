"""
Deep Technical & Scientific Review Script for ClearTapLab Guides (01-20)
Analyzes scientific mechanisms, chemical equations, mathematical formulations,
NSF/ANSI standards, EPA regulations, and structure.
"""

import os
import re
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from bs4 import BeautifulSoup
from tests.test_utils import load_articles_data

articles = load_articles_data()

print(f"Total articles loaded: {len(articles)}")
print("=" * 80)

for a in articles:
    aid = a["id"]
    title = a["title"]
    cat = a["category"]
    cat_label = a.get("categoryLabel", "")
    raw_html = a.get("contentHtml", "")
    soup = BeautifulSoup(raw_html, "html.parser")
    text = soup.get_text(" ", strip=True)
    words = len(re.findall(r"\b\w+\b", text))
    
    # Structural Elements
    h1 = [h.get_text().strip() for h in soup.find_all("h1")]
    h2s = [h.get_text().strip() for h in soup.find_all("h2")]
    h3s = [h.get_text().strip() for h in soup.find_all("h3")]
    badge_pills = [b.get_text().strip() for b in soup.find_all(class_=re.compile(r"ctl-badge-pill"))]
    spec_boxes = soup.find_all(class_=re.compile(r"ctl-spec-box"))
    tables = soup.find_all(class_=re.compile(r"ctl-table-wrapper"))
    author_boxes = soup.find_all(class_=re.compile(r"ctl-author-box"))
    
    # FAQs
    faq_questions = []
    # Check details/summary or h3/h4 with ? or bold questions
    for el in soup.find_all(["summary", "h3", "h4", "strong", "p"]):
        qtext = el.get_text().strip()
        if "?" in qtext and len(qtext) > 15 and len(qtext) < 150:
            if qtext not in faq_questions:
                faq_questions.append(qtext)
                
    # Search for scientific standards
    standards = set(re.findall(
        r"(?:NSF(?:/ANSI)?\s*(?:42|53|58|44|401|P473|61|372)|EPA\b|SDWA\b|MCLG?\b|SMCL\b|LCR\b|DVGW(?:\s*W-512)?|WQA\b|USGS\b|ISO\s*\d+|IPC\b|UPC\b|WHO\b)",
        text,
        re.IGNORECASE
    ))
    
    # Search for key chemical formulas and engineering terms
    chem_math = set(re.findall(
        r"(?:Fe²⁺|Fe³⁺|H₂S|Ca²⁺|Mg²⁺|CaCO₃|HCO₃⁻|SO₄²⁻|NO₃⁻|Na⁺|Cl⁻|O₂|KMnO₄|Cl₂|HOCl|OCl⁻|KDF-55|KDF-85|Al₂O₃|PFOS|PFOA|PFHxS|PFNA|HFPO-DA|GenX|Ergun|Darcy[- ]Weisbach|Van\s*[\'\"]?t\s*Hoff|ΔP|GPG|PPM|PPB|PPT|GPD|GPM|PSI|TDS|TAC|EBCT|TCO|ICP-MS|LC-MS/MS|GC-MS|microns?|angstroms?|osmotic\s*pressure|flux\s*rate|permeate|brine|rejection\s*rate)",
        text,
        re.IGNORECASE
    ))
    
    # Code blocks or formulas
    code_blocks = [c.get_text().strip() for c in soup.find_all(["code", "pre"])]
    
    print(f"GUIDE {aid:02d}: {title}")
    print(f"  Category: {cat} ({cat_label}) | Word Count: {words}")
    print(f"  H1: {h1}")
    print(f"  Badge: {badge_pills}")
    print(f"  H2 Count: {len(h2s)} | Sections: {h2s[:3]}...")
    print(f"  Spec Boxes: {len(spec_boxes)} | Tables: {len(tables)} | Author Boxes: {len(author_boxes)}")
    print(f"  FAQ Count: {len(faq_questions)}")
    for i, q in enumerate(faq_questions[:4], 1):
        print(f"    FAQ {i}: {q}")
    print(f"  Standards Detected: {sorted(list(standards))}")
    print(f"  Chem / Engineering Entities ({len(chem_math)}): {sorted(list(chem_math))[:10]}...")
    print(f"  Code / Formula Snippets ({len(code_blocks)}): {code_blocks[:3]}")
    print("-" * 80)
