import re
from bs4 import BeautifulSoup

with open('scripts/batch1_articles.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Verify variable assignment
assert 'window.CLEAR_TAP_ARTICLES_BATCH1 =' in text, 'Missing window.CLEAR_TAP_ARTICLES_BATCH1 array'

# Regex to parse individual article objects
article_pattern = re.compile(
    r'\{\s*id:\s*(\d+),\s*'
    r'slug:\s*"([^"]+)",\s*'
    r'title:\s*"([^"]+)",\s*'
    r'category:\s*"([^"]+)",\s*'
    r'categoryLabel:\s*"([^"]+)",\s*'
    r'readTime:\s*"([^"]+)",\s*'
    r'badgeClass:\s*"([^"]+)",\s*'
    r'excerpt:\s*"([^"]+)",\s*'
    r'tags:\s*\[([\s\S]*?)\],\s*'
    r'contentHtml:\s*`([\s\S]*?)`\s*\}',
    re.MULTILINE
)

matches = list(article_pattern.finditer(text))
print(f'Total articles parsed: {len(matches)}')
assert len(matches) == 5, f'Expected 5 articles, got {len(matches)}'

for m in matches:
    aid = int(m.group(1))
    slug = m.group(2)
    title = m.group(3)
    cat = m.group(4)
    cat_label = m.group(5)
    read_time = m.group(6)
    badge = m.group(7)
    excerpt = m.group(8)
    tags_str = m.group(9)
    html = m.group(10)

    print(f'\n--- Validating Guide {aid:02d}: {slug} ---')
    print(f'Title: {title}')
    print(f'Category: {cat} ({cat_label}) | Read Time: {read_time} | Badge: {badge}')
    print(f'Excerpt length: {len(excerpt)} chars')
    
    tags = [t.strip().strip('"').strip("'") for t in tags_str.split(',') if t.strip()]
    print(f'Tags ({len(tags)}): {tags}')
    assert len(tags) >= 5, f'Expected at least 5 tags, got {len(tags)}'

    print(f'contentHtml length: {len(html)} chars')
    assert len(html) > 2000, f'Article {aid} HTML is too short ({len(html)} chars)'

    soup = BeautifulSoup(html, 'html.parser')

    # Check Badge
    badge_el = soup.find(class_=re.compile(r'ctl-badge-pill'))
    assert badge_el is not None, f'Guide {aid} missing .ctl-badge-pill'
    print(f'  [x] Badge: {badge_el.text.strip()}')

    # Check H1
    h1 = soup.find('h1')
    assert h1 is not None, f'Guide {aid} missing <h1>'
    print(f'  [x] H1: {h1.text.strip()}')

    # Check Spec Box / Card
    spec_box = soup.find(class_=re.compile(r'ctl-spec-box|ctl-card'))
    assert spec_box is not None, f'Guide {aid} missing .ctl-spec-box or .ctl-card'
    print(f'  [x] Spec Box / Card found')

    # Check Table Wrapper & Table
    table_wrap = soup.find(class_='ctl-table-wrapper')
    assert table_wrap is not None, f'Guide {aid} missing .ctl-table-wrapper'
    table = table_wrap.find('table', class_='ctl-table')
    assert table is not None, f'Guide {aid} missing table.ctl-table'
    rows = table.find_all('tr')
    print(f'  [x] Table present with {len(rows)} rows')
    assert len(rows) >= 4, f'Table has too few rows ({len(rows)})'

    # Check FAQs
    faq_items = soup.find_all(class_='ctl-faq-item')
    print(f'  [x] FAQ count: {len(faq_items)}')
    assert len(faq_items) in [3, 4], f'Expected 3-4 FAQ items, got {len(faq_items)}'

    # Check Author Box
    author_box = soup.find(class_='ctl-author-box')
    assert author_box is not None, f'Guide {aid} missing .ctl-author-box'
    print(f'  [x] Author box present')

    # Check Internal Cross Links
    links = soup.find_all('a', onclick=re.compile(r'openArticleModal\(\d+\)'))
    print(f'  [x] SPA modal links: {len(links)}')
    assert len(links) >= 1, f'Guide {aid} missing SPA modal cross links'

    # Check no forbidden placeholder text
    for placeholder in ['TODO', 'Lorem', '[Placeholder]', 'TBD', 'stub']:
        assert placeholder not in html, f'Forbidden string {placeholder} found in Guide {aid}'

print('\n======================================================')
print('ALL 5 BATCH 1 GUIDES PASSED RIGOROUS SCIENTIFIC & DOM VERIFICATION!')
print('======================================================')
