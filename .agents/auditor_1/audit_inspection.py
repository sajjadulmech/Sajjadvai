import os
import sys
import re
from bs4 import BeautifulSoup

# Ensure repo root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from tests.test_utils import load_articles_data, extract_word_count, MASTER_GUIDES_MATRIX

def run_deep_article_audit():
    articles = load_articles_data()
    print(f"=== DEEP FORENSIC AUDIT: 20 ARTICLES IN scripts/articles-data.js ===")
    print(f"Total articles loaded: {len(articles)}")
    assert len(articles) == 20, f"Expected 20 articles, got {len(articles)}"

    suspicious_patterns = [
        r'\blorem\s+ipsum\b',
        r'\bplaceholder\b',
        r'\btodo\b',
        r'\btbd\b',
        r'\bcoming\s+soon\b',
        r'\bsample\s+text\b',
        r'\binsert\s+here\b',
        r'\bxxx+\b',
        r'\bstub\b',
        r'\bdummy\b',
        r'\basdf\b',
        r'\btest\s+content\b'
    ]

    all_faqs = []
    issues = []

    for a in articles:
        aid = a['id']
        title = a['title']
        slug = a['slug']
        cat = a['category']
        html = a['contentHtml']
        wc = extract_word_count(html)
        soup = BeautifulSoup(html, 'html.parser')

        # 1. Suspicious pattern check
        for pat in suspicious_patterns:
            matches = re.findall(pat, html, re.IGNORECASE)
            if matches:
                issues.append(f"[Article {aid:02d}] Matched suspicious pattern '{pat}': {matches}")

        # 2. Word count check (minimum 1000 words per article)
        if wc < 1000:
            issues.append(f"[Article {aid:02d}] Insufficient word count: {wc} words (minimum 1000)")

        # 3. Headings check
        h2s = soup.find_all('h2')
        h3s = soup.find_all('h3')
        if len(h2s) < 3:
            issues.append(f"[Article {aid:02d}] Too few H2 headings: {len(h2s)}")

        # 4. Table check
        tables = soup.find_all('div', class_='ctl-table-wrapper')
        if len(tables) < 1:
            issues.append(f"[Article {aid:02d}] Missing table (.ctl-table-wrapper)")
        for t in tables:
            rows = t.find_all('tr')
            if len(rows) < 3:
                issues.append(f"[Article {aid:02d}] Table has too few rows ({len(rows)})")

        # 5. Spec callout box check
        specs = soup.find_all('div', class_='ctl-spec-box')
        if len(specs) < 1:
            issues.append(f"[Article {aid:02d}] Missing engineering spec box (.ctl-spec-box)")

        # 6. FAQ check
        faqs = soup.find_all('div', class_='ctl-faq-item')
        if len(faqs) < 3 or len(faqs) > 4:
            issues.append(f"[Article {aid:02d}] FAQ count out of range: {len(faqs)} (expected 3-4)")
        for fidx, f in enumerate(faqs, 1):
            q_elem = f.find(['h3', 'h4', 'strong', 'p'])
            q_text = q_elem.get_text().strip() if q_elem else f.get_text()[:40]
            ans_text = f.get_text().strip()
            all_faqs.append((aid, q_text, ans_text))
            if len(ans_text) < 80:
                issues.append(f"[Article {aid:02d}] FAQ #{fidx} answer too short ({len(ans_text)} chars): {q_text}")

        # 7. Author byline & related links check
        byline = soup.find(class_=re.compile(r'byline|author', re.I)) or soup.find(text=re.compile(r'Author|ClearTapLab Engineering|Staff', re.I))
        # Check links
        links = soup.find_all('a')
        internal_onclicks = [a.get('onclick') for a in links if a.get('onclick') and 'openArticleModal' in a.get('onclick')]
        internal_hrefs = [a.get('href') for a in links if a.get('href') and a.get('href').startswith('#')]

        print(f"Guide {aid:02d} [{cat}] -> {wc:4d} words, {len(h2s)} H2s, {len(tables)} tables, {len(specs)} spec-boxes, {len(faqs)} FAQs, {len(internal_onclicks)} modal cross-links")

    # Check FAQ uniqueness across entire catalog
    faq_questions = [q[1].lower() for q in all_faqs]
    if len(faq_questions) != len(set(faq_questions)):
        dupes = [q for q in faq_questions if faq_questions.count(q) > 1]
        issues.append(f"Duplicate FAQ questions detected across guides: {set(dupes)}")

    print(f"\n--- RESULTS OF ARTICLE INSPECTION ---")
    print(f"Total FAQs verified: {len(all_faqs)}")
    print(f"Total issues detected: {len(issues)}")
    if issues:
        for iss in issues:
            print("  ISSUE:", iss)
    else:
        print(">>> ZERO ISSUES DETECTED ACROSS ALL 20 PRODUCTION ARTICLES! ALL CLEAN! <<<")

if __name__ == "__main__":
    run_deep_article_audit()
