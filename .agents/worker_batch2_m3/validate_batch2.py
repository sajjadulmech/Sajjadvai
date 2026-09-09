import re
import sys
from bs4 import BeautifulSoup

def main():
    with open('scripts/batch2_articles.js', 'r', encoding='utf-8') as f:
        js_content = f.read()

    # Verify assignment
    if 'window.CLEAR_TAP_ARTICLES_BATCH2 = [' not in js_content:
        print("ERROR: Missing window.CLEAR_TAP_ARTICLES_BATCH2 assignment")
        sys.exit(1)

    # Let's parse articles using regex for each article block
    # Split by object pattern
    id_matches = list(re.finditer(r'id:\s*(\d+),', js_content))
    print(f"Found {len(id_matches)} article IDs")
    if len(id_matches) != 5:
        print(f"ERROR: Expected 5 article IDs, found {len(id_matches)}")
        sys.exit(1)

    articles = []
    for i in range(len(id_matches)):
        start = id_matches[i].start()
        end = id_matches[i+1].start() if i+1 < len(id_matches) else js_content.rfind('];')
        block = js_content[start:end]
        
        aid = int(id_matches[i].group(1))
        slug = re.search(r'slug:\s*"([^"]+)"', block).group(1)
        title = re.search(r'title:\s*"([^"]+)"', block).group(1)
        category = re.search(r'category:\s*"([^"]+)"', block).group(1)
        category_label = re.search(r'categoryLabel:\s*"([^"]+)"', block).group(1)
        read_time = re.search(r'readTime:\s*"([^"]+)"', block).group(1)
        badge_class = re.search(r'badgeClass:\s*"([^"]+)"', block).group(1)
        excerpt = re.search(r'excerpt:\s*"([^"]+)"', block).group(1)
        
        tags_match = re.search(r'tags:\s*\[([\s\S]*?)\]', block)
        tags = [t.strip().strip('"') for t in tags_match.group(1).split(',') if t.strip()]
        
        html_match = re.search(r'contentHtml:\s*`([\s\S]*?)`', block)
        html = html_match.group(1)
        
        articles.append({
            'id': aid,
            'slug': slug,
            'title': title,
            'category': category,
            'categoryLabel': category_label,
            'readTime': read_time,
            'badgeClass': badge_class,
            'excerpt': excerpt,
            'tags': tags,
            'html': html
        })

    for a in articles:
        aid = a['id']
        title = a['title']
        slug = a['slug']
        category = a['category']
        cat_label = a['categoryLabel']
        read_time = a['readTime']
        badge = a['badgeClass']
        excerpt = a['excerpt']
        tags = a['tags']
        html = a['html']
        
        print(f"\n=== Article {aid}: {title} ===")
        print(f"  Slug: {slug}")
        print(f"  Category: {category} ({cat_label})")
        print(f"  Read Time: {read_time}")
        print(f"  Badge Class: {badge}")
        print(f"  Excerpt: {excerpt[:80]}...")
        print(f"  Tags ({len(tags)}): {tags}")
        print(f"  HTML length: {len(html)} chars, words: {len(html.split())}")
        
        assert aid in [6, 7, 8, 9, 10], f"Invalid ID {aid}"
        assert len(tags) >= 6, f"Expected >= 6 tags, got {len(tags)}"
        assert len(html) > 4000, f"HTML content too short: {len(html)} chars"
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        
        # Check elements
        badges = soup.select('.ctl-badge-pill')
        h1s = soup.select('h1')
        tables = soup.select('.ctl-table-wrapper table.ctl-table')
        spec_boxes = soup.select('.ctl-spec-box, .ctl-spec-grid, .ctl-card')
        faqs = soup.select('.ctl-faq-item')
        faq_questions = soup.select('.ctl-faq-question')
        faq_answers = soup.select('.ctl-faq-answer')
        authors = soup.select('.ctl-author-box')
        links = soup.select('a[onclick*="openArticleModal"]')
        
        print(f"  Badges: {len(badges)}, H1: {len(h1s)}, Tables: {len(tables)}, Spec/Grid/Cards: {len(spec_boxes)}, FAQs: {len(faqs)}, Author: {len(authors)}, Modal Links: {len(links)}")
        
        assert len(badges) >= 1, 'Missing badge pill'
        assert len(h1s) == 1, 'Expected exactly 1 H1'
        assert len(tables) >= 1, 'Missing comparison table'
        assert len(spec_boxes) >= 1, 'Missing spec box or card'
        assert len(faqs) == 4, f'Expected exactly 4 FAQ items, got {len(faqs)}'
        assert len(faq_questions) == 4, f'Expected 4 FAQ questions, got {len(faq_questions)}'
        assert len(faq_answers) == 4, f'Expected 4 FAQ answers, got {len(faq_answers)}'
        assert len(authors) == 1, 'Missing author box'
        assert len(links) >= 2, f'Expected at least 2 cross-links, got {len(links)}'

    print("\n=======================================================")
    print(">>> SUCCESS: ALL BATCH 2 VERIFICATIONS PASSED 100%! <<<")
    print("=======================================================")

if __name__ == '__main__':
    main()
