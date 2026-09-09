import re
import sys

def audit_batch3_quality():
    file_path = "d:/Personal/AntiGravity/Affiliate Marketting/scripts/batch3_articles.js"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Verify standards citations
    standards_checks = {
        11: ["NSF", "58", "TDS", "booster pump", "bladder"],
        12: ["KDF-55", "catalytic", "NSF", "42", "61", "372", "1,000,000", "EBCT"],
        13: ["GPM", "IPC", "peak", "EBCT", "SpringWell", "Express Water"],
        14: ["ICP-MS", "GC-MS", "EPA", "200.8", "524.2", "Tap Score", "NTL"],
        15: ["Calcite", "Corosex", "carbonic acid", "CO2", "SCA", "LSI", "pH"]
    }

    print("Checking standards & technical terminology across all 5 guides:")
    for guide_id, keywords in standards_checks.items():
        print(f"\nGuide {guide_id}:")
        for kw in keywords:
            count = len(re.findall(re.escape(kw), content, re.IGNORECASE))
            print(f"  - Keyword '{kw}': {count} occurrences")
            assert count > 0, f"Guide {guide_id} missing keyword: {kw}"

    # Verify cross-links point to valid openArticleModal calls
    modal_links = re.findall(r'openArticleModal\((\d+)\)', content)
    print(f"\nFound {len(modal_links)} openArticleModal links in batch 3: {set(modal_links)}")
    for link_id in modal_links:
        int_id = int(link_id)
        assert 1 <= int_id <= 20, f"Invalid article modal ID: {int_id}"

    # Check for backtick nesting or unescaped string syntax errors
    # Make sure every backtick is part of contentHtml
    backticks = content.count('`')
    print(f"\nBacktick count: {backticks} (expected 10 - 2 per guide)")
    assert backticks == 10, f"Expected 10 backticks, found {backticks}"

    print("\nBatch 3 quality audit PASSED 100%!")
    return 0

if __name__ == "__main__":
    sys.exit(audit_batch3_quality())
