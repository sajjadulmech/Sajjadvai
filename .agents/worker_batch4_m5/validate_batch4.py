import re
from bs4 import BeautifulSoup

def main():
    with open('scripts/batch4_articles.js', 'r', encoding='utf-8') as f:
        code = f.read()

    match = re.search(r'window\.CLEAR_TAP_ARTICLES_BATCH4\s*=\s*(\[[\s\S]*?\]);\s*(?:\n|//|if|$)', code)
    if not match:
        print('ERROR: Could not find window.CLEAR_TAP_ARTICLES_BATCH4 definition!')
        return 1

    print('Found batch 4 array declaration! Length of JS file:', len(code), 'bytes')

    items = re.findall(r'\{\s*id:\s*(\d+),[\s\S]*?contentHtml:\s*`([\s\S]*?)`\s*\}', code)
    print(f'Matched {len(items)} guides with contentHtml backticks')

    assert len(items) == 5, f'Expected exactly 5 guides, found {len(items)}'

    expected_ids = [16, 17, 18, 19, 20]
    actual_ids = [int(item[0]) for item in items]
    assert actual_ids == expected_ids, f'Expected IDs {expected_ids}, got {actual_ids}'

    for g_id_str, content_html in items:
        g_id = int(g_id_str)
        soup = BeautifulSoup(content_html, 'html.parser')
        text = soup.get_text()
        words = len(text.split())
        chars = len(content_html)
        
        h1 = soup.find('h1')
        badge = soup.find(class_='ctl-badge-pill')
        spec_box = soup.find(class_='ctl-spec-box') or soup.find(class_='ctl-card')
        table_wrapper = soup.find(class_='ctl-table-wrapper')
        table = soup.find('table', class_='ctl-table') if table_wrapper else None
        faqs = soup.find_all(class_='ctl-faq-item')
        author_box = soup.find(class_='ctl-author-box')
        links = soup.find_all('a')
        
        print(f'\n--- Guide {g_id} ---')
        print(f'  Chars: {chars}, Words: {words}')
        print(f'  H1: {h1.get_text().strip() if h1 else "MISSING"}')
        print(f'  Badge: {badge.get_text().strip() if badge else "MISSING"}')
        print(f'  Spec Box / Card: {"YES" if spec_box else "MISSING"}')
        print(f'  Table: {"YES" if table else "MISSING"}')
        print(f'  FAQ Count: {len(faqs)}')
        print(f'  Author Box: {"YES" if author_box else "MISSING"}')
        print(f'  Internal Links: {len(links)}')

        # Verification rules
        assert chars >= 3500, f'Guide {g_id} contentHtml too short: {chars} < 3500'
        assert words >= 500, f'Guide {g_id} word count too low: {words} < 500'
        assert h1 is not None, f'Guide {g_id} missing H1'
        assert badge is not None, f'Guide {g_id} missing badge'
        assert spec_box is not None, f'Guide {g_id} missing spec-box or card'
        assert table is not None, f'Guide {g_id} missing table'
        assert len(faqs) in (3, 4), f'Guide {g_id} FAQs must be 3 or 4, found {len(faqs)}'
        assert author_box is not None, f'Guide {g_id} missing author-box'
        assert len(links) > 0, f'Guide {g_id} missing internal links'

        # Special verification for Guide 20: Ergun Equation
        if g_id == 20:
            assert 'Ergun' in content_html, 'Guide 20 must mention Ergun equation'
            assert 'ΔP / L' in content_html or '&Delta;P / L' in content_html, 'Guide 20 must include Ergun equation formula'

    print('\n========================================')
    print('ALL 5 BATCH 4 GUIDES PASSED DOM & CONTENT ASSERTIONS!')
    print('========================================')
    return 0

if __name__ == '__main__':
    exit(main())
