import re
import sys
import io
from bs4 import BeautifulSoup

# Ensure UTF-8 output on Windows console
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

def validate():
    file_path = "d:/Personal/AntiGravity/Affiliate Marketting/scripts/batch3_articles.js"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    if "window.CLEAR_TAP_ARTICLES_BATCH3 = [" not in content:
        print("FAIL: window.CLEAR_TAP_ARTICLES_BATCH3 export missing")
        return 1

    # Split by object pattern or extract IDs
    article_chunks = re.split(r'\n\s*\{\s*\n\s*id:\s*', content)[1:]
    print(f"Found {len(article_chunks)} raw article chunks.")

    if len(article_chunks) != 5:
        print(f"FAIL: Expected 5 article chunks, got {len(article_chunks)}")
        return 1

    expected_guides = [
        (11, "tankless-vs-tank-reverse-osmosis", "reverse-osmosis"),
        (12, "springwell-cf1-review", "system-guides"),
        (13, "best-whole-house-water-filters", "system-guides"),
        (14, "best-water-test-kits", "water-testing"),
        (15, "remineralization-reverse-osmosis-filter", "reverse-osmosis"),
    ]

    for idx, chunk in enumerate(article_chunks):
        # Extract id
        id_match = re.match(r'^(\d+),', chunk)
        assert id_match, f"Could not match id in chunk {idx}"
        art_id = int(id_match.group(1))

        # Extract slug
        slug_match = re.search(r'slug:\s*"([^"]+)",', chunk)
        assert slug_match, f"Could not match slug in chunk {idx}"
        slug = slug_match.group(1)

        # Extract title
        title_match = re.search(r'title:\s*"([^"]+)",', chunk)
        assert title_match, f"Could not match title in chunk {idx}"
        title = title_match.group(1)

        # Extract category
        cat_match = re.search(r'category:\s*"([^"]+)",', chunk)
        assert cat_match, f"Could not match category in chunk {idx}"
        cat = cat_match.group(1)

        # Extract tags
        tags_match = re.search(r'tags:\s*\[(.*?)\]', chunk, re.DOTALL)
        assert tags_match, f"Could not match tags in chunk {idx}"
        raw_tags = tags_match.group(1)
        tags = [t.strip().strip('"').strip("'") for t in raw_tags.split(",") if t.strip()]

        # Extract contentHtml
        html_match = re.search(r'contentHtml:\s*`([\s\S]*?)`\s*\}', chunk)
        assert html_match, f"Could not match contentHtml in chunk {idx}"
        html = html_match.group(1).strip()

        exp_id, exp_slug, exp_cat = expected_guides[idx]
        print(f"\n--- Validating Guide {art_id}: {slug} ---")

        assert art_id == exp_id, f"ID mismatch: got {art_id}, expected {exp_id}"
        assert slug == exp_slug, f"Slug mismatch: got {slug}, expected {exp_slug}"
        assert cat == exp_cat, f"Category mismatch: got {cat}, expected {exp_cat}"

        print(f"Title: {title}")
        print(f"Tags ({len(tags)}): {tags}")
        assert len(tags) >= 5, f"Expected >=5 tags, got {len(tags)}"

        char_count = len(html)
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        words = text.split()
        word_count = len(words)
        print(f"HTML Char Count: {char_count} (min 3500 required)")
        print(f"Word Count: {word_count} (min 500 required)")
        assert char_count >= 3500, f"Guide {art_id} char count {char_count} < 3500"
        assert word_count >= 500, f"Guide {art_id} word count {word_count} < 500"

        # Check DOM elements
        badge = soup.find("div", class_=lambda c: c and "ctl-badge-pill" in c)
        assert badge is not None, f"Guide {art_id} missing .ctl-badge-pill"
        print(f"Badge: {badge.get_text().strip()}")

        h1 = soup.find("h1")
        assert h1 is not None, f"Guide {art_id} missing <h1>"
        print(f"H1: {h1.get_text().strip()}")

        # Spec box or card with spec grid
        spec_box = soup.find("div", class_=lambda c: c and ("ctl-spec-box" in c or "ctl-spec-grid" in c))
        assert spec_box is not None, f"Guide {art_id} missing .ctl-spec-box or .ctl-spec-grid"
        print(f"Spec Box/Grid found: {spec_box.get('class')}")

        # Table
        table_wrapper = soup.find("div", class_=lambda c: c and "ctl-table-wrapper" in c)
        assert table_wrapper is not None, f"Guide {art_id} missing .ctl-table-wrapper"
        table = table_wrapper.find("table", class_=lambda c: c and "ctl-table" in c)
        assert table is not None, f"Guide {art_id} missing table.ctl-table"
        rows = table.find_all("tr")
        print(f"Table found with {len(rows)} rows.")

        # FAQs
        faq_container = soup.find("div", class_=lambda c: c and "ctl-faq-container" in c)
        assert faq_container is not None, f"Guide {art_id} missing .ctl-faq-container"
        faq_items = faq_container.find_all("div", class_=lambda c: c and "ctl-faq-item" in c)
        print(f"FAQ Items: {len(faq_items)} (exactly 3-4 required)")
        assert 3 <= len(faq_items) <= 4, f"Guide {art_id} expected 3-4 FAQs, got {len(faq_items)}"

        # Author box
        author_box = soup.find("div", class_=lambda c: c and "ctl-author-box" in c)
        assert author_box is not None, f"Guide {art_id} missing .ctl-author-box"
        print(f"Author Box found: {author_box.get_text()[:40]}...")

        # Cross links
        cross_links = author_box.find_all("a")
        modal_links = [a for a in cross_links if "openArticleModal" in a.get("onclick", "")]
        print(f"Modal Cross-Links in author box: {len(modal_links)}")
        assert len(modal_links) >= 2, f"Guide {art_id} expected >=2 cross links in author box, got {len(modal_links)}"

    print("\n========================================================")
    print("ALL BATCH 3 GUIDES (11-15) STRICTLY VALIDATED AND PASSED!")
    print("========================================================")
    return 0

if __name__ == "__main__":
    sys.exit(validate())
