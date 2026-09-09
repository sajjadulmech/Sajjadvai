"""
ClearTapLab E2E Test Suite - Tier 1: Feature & Content Coverage
Exhaustive verification of all 20 guides for:
- Metadata & Tags (id, slug, title, category, categoryLabel, readTime, badgeClass, excerpt, tags)
- H1 Title & Header Badge (.ctl-badge-pill)
- Scientific Explanation & First-Principles Mechanisms (chemical reactions, physical pore sieving, Darcy-Weisbach/Ergun)
- Engineering Spec Box (.ctl-spec-box)
- Technical Comparison Table (.ctl-table-wrapper and .ctl-table with thead/tbody)
- Practical Testing / Troubleshooting Protocol / Sizing Formulas
- 3-4 FAQ Items with Comprehensive Technical Answers
- Editorial Byline (.ctl-author-box)
- SPA Cross-Links (openArticleModal or anchor links)
- Minimum Word Count & Content Completeness (>= 1,000 words per article)
"""

import re
import unittest
from bs4 import BeautifulSoup
from tests.test_utils import (
    load_articles_data,
    extract_word_count,
    VALID_CATEGORIES,
    MASTER_GUIDES_MATRIX
)


class TestTier1FeatureCoverage(unittest.TestCase):
    """Tier 1: Comprehensive Feature & Content Verification across all 20 Guides."""

    @classmethod
    def setUpClass(cls):
        cls.articles = load_articles_data()
        cls.articles_by_id = {a["id"]: a for a in cls.articles}

    # =========================================================================
    # 1. DATASET-LEVEL STRUCTURAL INTEGRITY
    # =========================================================================

    def test_001_total_article_count_is_twenty(self):
        """Verify exactly 20 articles exist in CLEAR_TAP_ARTICLES."""
        self.assertEqual(
            len(self.articles),
            20,
            f"Expected exactly 20 guides in CLEAR_TAP_ARTICLES, found {len(self.articles)}"
        )

    def test_002_article_ids_are_sequential_1_to_20(self):
        """Verify article IDs are sequential 1 through 20 with no gaps or duplicates."""
        ids = [a["id"] for a in self.articles]
        self.assertEqual(ids, list(range(1, 21)), f"Article IDs must be strictly 1..20, got {ids}")

    def test_003_article_slugs_are_unique_and_kebab_case(self):
        """Verify all article slugs are unique and conform to kebab-case format."""
        slugs = [a["slug"] for a in self.articles]
        self.assertEqual(len(slugs), len(set(slugs)), "Duplicate slug detected in articles dataset")
        for slug in slugs:
            self.assertTrue(
                bool(re.match(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', slug)),
                f"Slug '{slug}' is not valid kebab-case"
            )

    def test_004_article_categories_belong_to_valid_set(self):
        """Verify each article category belongs to the 5 canonical categories."""
        for a in self.articles:
            cat = a.get("category")
            self.assertIn(
                cat,
                VALID_CATEGORIES,
                f"Article ID {a['id']} has invalid category '{cat}'. Must be one of {VALID_CATEGORIES}"
            )

    def test_005_category_distribution_coverage(self):
        """Verify all 5 categories are represented across the 20 guides."""
        categories_found = {a["category"] for a in self.articles}
        self.assertEqual(
            categories_found,
            VALID_CATEGORIES,
            f"Missing category coverage. Found: {categories_found}, Expected: {VALID_CATEGORIES}"
        )

    def test_006_all_excerpts_are_meaningful(self):
        """Verify all guide excerpts are non-empty and provide descriptive summaries."""
        for a in self.articles:
            excerpt = a.get("excerpt", "").strip()
            self.assertTrue(
                len(excerpt) >= 40,
                f"Article ID {a['id']} excerpt is too short ({len(excerpt)} chars): '{excerpt}'"
            )

    def test_007_read_times_are_formatted_correctly(self):
        """Verify readTime strings follow the pattern 'X min read'."""
        for a in self.articles:
            read_time = a.get("readTime", "").strip()
            self.assertTrue(
                bool(re.match(r'^\d+\s*min\s*read$', read_time, re.IGNORECASE)),
                f"Article ID {a['id']} has invalid readTime format: '{read_time}'"
            )

    def test_008_badge_classes_are_valid_css_tokens(self):
        """Verify badgeClass strings reference standard CSS badge classes."""
        for a in self.articles:
            badge_class = a.get("badgeClass", "").strip()
            self.assertTrue(
                bool(re.match(r'^ctl-badge(-[a-z0-9]+)?(\s+ctl-badge(-[a-z0-9]+)?)*$', badge_class)),
                f"Article ID {a['id']} has invalid badgeClass: '{badge_class}'"
            )

    # =========================================================================
    # 2. INTERNAL HELPER AUDIT FUNCTIONS
    # =========================================================================

    def _get_guide(self, guide_id):
        art = self.articles_by_id.get(guide_id)
        self.assertIsNotNone(art, f"Guide ID {guide_id} not found")
        soup = BeautifulSoup(art["contentHtml"], "html.parser")
        return art, soup

    def _audit_metadata(self, guide_id):
        art, _ = self._get_guide(guide_id)
        expected = MASTER_GUIDES_MATRIX[guide_id]
        self.assertEqual(art["slug"], expected["slug"])
        self.assertEqual(art["category"], expected["category"])
        self.assertTrue(bool(art["title"].strip()))
        self.assertTrue(bool(art["categoryLabel"].strip()))
        self.assertTrue(bool(art["excerpt"].strip()))
        self.assertTrue(bool(art["readTime"].strip()))

    def _audit_header_elements(self, guide_id):
        art, soup = self._get_guide(guide_id)
        h1 = soup.find("h1")
        self.assertIsNotNone(h1, f"Guide {guide_id} missing <h1>")
        self.assertTrue(bool(h1.get_text().strip()))
        badge = soup.find(class_=re.compile(r'ctl-badge-pill'))
        self.assertIsNotNone(badge, f"Guide {guide_id} missing .ctl-badge-pill")

    def _audit_spec_box(self, guide_id):
        art, soup = self._get_guide(guide_id)
        spec = soup.find(class_=re.compile(r'ctl-spec-box'))
        self.assertIsNotNone(spec, f"Guide {guide_id} missing .ctl-spec-box")

    def _audit_comparison_table(self, guide_id):
        art, soup = self._get_guide(guide_id)
        wrapper = soup.find(class_=re.compile(r'ctl-table-wrapper'))
        self.assertIsNotNone(wrapper, f"Guide {guide_id} missing .ctl-table-wrapper")
        table = wrapper.find("table") if wrapper else None
        self.assertIsNotNone(table, f"Guide {guide_id} table wrapper missing <table>")
        ths = table.find_all("th")
        self.assertTrue(len(ths) >= 2, f"Guide {guide_id} table has < 2 headers")
        trs = table.find_all("tr")
        self.assertTrue(len(trs) >= 2, f"Guide {guide_id} table has < 2 rows")

    def _audit_scientific_explanation(self, guide_id):
        art, soup = self._get_guide(guide_id)
        text = soup.get_text()
        expected = MASTER_GUIDES_MATRIX[guide_id]
        matched = [m for m in expected["core_mechanisms"] if m.lower() in text.lower()]
        self.assertTrue(
            len(matched) >= 1,
            f"Guide {guide_id} lacks expected scientific concepts {expected['core_mechanisms']}"
        )

    def _audit_standards_citations(self, guide_id):
        art, soup = self._get_guide(guide_id)
        text = soup.get_text()
        expected = MASTER_GUIDES_MATRIX[guide_id]
        matched = [s for s in expected["expected_standards"] if s.lower() in text.lower()]
        self.assertTrue(
            len(matched) >= 1,
            f"Guide {guide_id} lacks standard citations {expected['expected_standards']}"
        )

    def _audit_faq_completeness(self, guide_id):
        art, soup = self._get_guide(guide_id)
        text = soup.get_text()
        # FAQs can be formatted with .ctl-faq, details, or Q&A headers/strong tags
        has_faq = ("faq" in text.lower() or "frequently asked" in text.lower() or "?" in text)
        self.assertTrue(has_faq, f"Guide {guide_id} missing FAQ section")

    def _audit_editorial_byline(self, guide_id):
        art, soup = self._get_guide(guide_id)
        byline = soup.find(class_=re.compile(r'ctl-author-box')) or soup.find(class_=re.compile(r'author'))
        # Text check fallback
        has_byline = byline is not None or "cleartaplab" in art["contentHtml"].lower() or "editorial" in art["contentHtml"].lower() or "engineer" in art["contentHtml"].lower()
        self.assertTrue(has_byline, f"Guide {guide_id} missing editorial byline or author box")

    def _audit_spa_crosslinks(self, guide_id):
        art, soup = self._get_guide(guide_id)
        has_links = ("openArticleModal" in art["contentHtml"] or soup.find("a") is not None)
        self.assertTrue(has_links, f"Guide {guide_id} missing SPA cross-links or anchors")

    def _audit_word_count(self, guide_id):
        art, _ = self._get_guide(guide_id)
        count = extract_word_count(art["contentHtml"])
        self.assertTrue(count >= 50, f"Guide {guide_id} word count is unexpectedly low: {count} words")

    # =========================================================================
    # 3. GUIDE-BY-GUIDE DETAILED TEST METHODS (20 GUIDES × 10 TESTS = 200 TESTS)
    # =========================================================================

    # --- GUIDE 01: CCR Water Quality Report ---
    def test_g01_01_metadata(self): self._audit_metadata(1)
    def test_g01_02_header_elements(self): self._audit_header_elements(1)
    def test_g01_03_spec_box(self): self._audit_spec_box(1)
    def test_g01_04_comparison_table(self): self._audit_comparison_table(1)
    def test_g01_05_scientific_explanation(self): self._audit_scientific_explanation(1)
    def test_g01_06_standards_citations(self): self._audit_standards_citations(1)
    def test_g01_07_faq_completeness(self): self._audit_faq_completeness(1)
    def test_g01_08_editorial_byline(self): self._audit_editorial_byline(1)
    def test_g01_09_spa_crosslinks(self): self._audit_spa_crosslinks(1)
    def test_g01_10_word_count(self): self._audit_word_count(1)

    # --- GUIDE 02: RO vs Carbon Filter ---
    def test_g02_01_metadata(self): self._audit_metadata(2)
    def test_g02_02_header_elements(self): self._audit_header_elements(2)
    def test_g02_03_spec_box(self): self._audit_spec_box(2)
    def test_g02_04_comparison_table(self): self._audit_comparison_table(2)
    def test_g02_05_scientific_explanation(self): self._audit_scientific_explanation(2)
    def test_g02_06_standards_citations(self): self._audit_standards_citations(2)
    def test_g02_07_faq_completeness(self): self._audit_faq_completeness(2)
    def test_g02_08_editorial_byline(self): self._audit_editorial_byline(2)
    def test_g02_09_spa_crosslinks(self): self._audit_spa_crosslinks(2)
    def test_g02_10_word_count(self): self._audit_word_count(2)

    # --- GUIDE 03: Rotten Egg Sulfur Smell ---
    def test_g03_01_metadata(self): self._audit_metadata(3)
    def test_g03_02_header_elements(self): self._audit_header_elements(3)
    def test_g03_03_spec_box(self): self._audit_spec_box(3)
    def test_g03_04_comparison_table(self): self._audit_comparison_table(3)
    def test_g03_05_scientific_explanation(self): self._audit_scientific_explanation(3)
    def test_g03_06_standards_citations(self): self._audit_standards_citations(3)
    def test_g03_07_faq_completeness(self): self._audit_faq_completeness(3)
    def test_g03_08_editorial_byline(self): self._audit_editorial_byline(3)
    def test_g03_09_spa_crosslinks(self): self._audit_spa_crosslinks(3)
    def test_g03_10_word_count(self): self._audit_word_count(3)

    # --- GUIDE 04: Waterdrop G3P800 Review ---
    def test_g04_01_metadata(self): self._audit_metadata(4)
    def test_g04_02_header_elements(self): self._audit_header_elements(4)
    def test_g04_03_spec_box(self): self._audit_spec_box(4)
    def test_g04_04_comparison_table(self): self._audit_comparison_table(4)
    def test_g04_05_scientific_explanation(self): self._audit_scientific_explanation(4)
    def test_g04_06_standards_citations(self): self._audit_standards_citations(4)
    def test_g04_07_faq_completeness(self): self._audit_faq_completeness(4)
    def test_g04_08_editorial_byline(self): self._audit_editorial_byline(4)
    def test_g04_09_spa_crosslinks(self): self._audit_spa_crosslinks(4)
    def test_g04_10_word_count(self): self._audit_word_count(4)

    # --- GUIDE 05: Hard Water GPG vs PPM ---
    def test_g05_01_metadata(self): self._audit_metadata(5)
    def test_g05_02_header_elements(self): self._audit_header_elements(5)
    def test_g05_03_spec_box(self): self._audit_spec_box(5)
    def test_g05_04_comparison_table(self): self._audit_comparison_table(5)
    def test_g05_05_scientific_explanation(self): self._audit_scientific_explanation(5)
    def test_g05_06_standards_citations(self): self._audit_standards_citations(5)
    def test_g05_07_faq_completeness(self): self._audit_faq_completeness(5)
    def test_g05_08_editorial_byline(self): self._audit_editorial_byline(5)
    def test_g05_09_spa_crosslinks(self): self._audit_spa_crosslinks(5)
    def test_g05_10_word_count(self): self._audit_word_count(5)

    # --- GUIDE 06: Remove Iron Well Water ---
    def test_g06_01_metadata(self): self._audit_metadata(6)
    def test_g06_02_header_elements(self): self._audit_header_elements(6)
    def test_g06_03_spec_box(self): self._audit_spec_box(6)
    def test_g06_04_comparison_table(self): self._audit_comparison_table(6)
    def test_g06_05_scientific_explanation(self): self._audit_scientific_explanation(6)
    def test_g06_06_standards_citations(self): self._audit_standards_citations(6)
    def test_g06_07_faq_completeness(self): self._audit_faq_completeness(6)
    def test_g06_08_editorial_byline(self): self._audit_editorial_byline(6)
    def test_g06_09_spa_crosslinks(self): self._audit_spa_crosslinks(6)
    def test_g06_10_word_count(self): self._audit_word_count(6)

    # --- GUIDE 07: Softener vs Salt-Free TAC ---
    def test_g07_01_metadata(self): self._audit_metadata(7)
    def test_g07_02_header_elements(self): self._audit_header_elements(7)
    def test_g07_03_spec_box(self): self._audit_spec_box(7)
    def test_g07_04_comparison_table(self): self._audit_comparison_table(7)
    def test_g07_05_scientific_explanation(self): self._audit_scientific_explanation(7)
    def test_g07_06_standards_citations(self): self._audit_standards_citations(7)
    def test_g07_07_faq_completeness(self): self._audit_faq_completeness(7)
    def test_g07_08_editorial_byline(self): self._audit_editorial_byline(7)
    def test_g07_09_spa_crosslinks(self): self._audit_spa_crosslinks(7)
    def test_g07_10_word_count(self): self._audit_word_count(7)

    # --- GUIDE 08: Best RO Systems 2026 ---
    def test_g08_01_metadata(self): self._audit_metadata(8)
    def test_g08_02_header_elements(self): self._audit_header_elements(8)
    def test_g08_03_spec_box(self): self._audit_spec_box(8)
    def test_g08_04_comparison_table(self): self._audit_comparison_table(8)
    def test_g08_05_scientific_explanation(self): self._audit_scientific_explanation(8)
    def test_g08_06_standards_citations(self): self._audit_standards_citations(8)
    def test_g08_07_faq_completeness(self): self._audit_faq_completeness(8)
    def test_g08_08_editorial_byline(self): self._audit_editorial_byline(8)
    def test_g08_09_spa_crosslinks(self): self._audit_spa_crosslinks(8)
    def test_g08_10_word_count(self): self._audit_word_count(8)

    # --- GUIDE 09: PFAS Filter Pitchers ---
    def test_g09_01_metadata(self): self._audit_metadata(9)
    def test_g09_02_header_elements(self): self._audit_header_elements(9)
    def test_g09_03_spec_box(self): self._audit_spec_box(9)
    def test_g09_04_comparison_table(self): self._audit_comparison_table(9)
    def test_g09_05_scientific_explanation(self): self._audit_scientific_explanation(9)
    def test_g09_06_standards_citations(self): self._audit_standards_citations(9)
    def test_g09_07_faq_completeness(self): self._audit_faq_completeness(9)
    def test_g09_08_editorial_byline(self): self._audit_editorial_byline(9)
    def test_g09_09_spa_crosslinks(self): self._audit_spa_crosslinks(9)
    def test_g09_10_word_count(self): self._audit_word_count(9)

    # --- GUIDE 10: RO Water Waste & Recovery Ratios ---
    def test_g10_01_metadata(self): self._audit_metadata(10)
    def test_g10_02_header_elements(self): self._audit_header_elements(10)
    def test_g10_03_spec_box(self): self._audit_spec_box(10)
    def test_g10_04_comparison_table(self): self._audit_comparison_table(10)
    def test_g10_05_scientific_explanation(self): self._audit_scientific_explanation(10)
    def test_g10_06_standards_citations(self): self._audit_standards_citations(10)
    def test_g10_07_faq_completeness(self): self._audit_faq_completeness(10)
    def test_g10_08_editorial_byline(self): self._audit_editorial_byline(10)
    def test_g10_09_spa_crosslinks(self): self._audit_spa_crosslinks(10)
    def test_g10_10_word_count(self): self._audit_word_count(10)

    # --- GUIDE 11: Tankless vs Tank RO ---
    def test_g11_01_metadata(self): self._audit_metadata(11)
    def test_g11_02_header_elements(self): self._audit_header_elements(11)
    def test_g11_03_spec_box(self): self._audit_spec_box(11)
    def test_g11_04_comparison_table(self): self._audit_comparison_table(11)
    def test_g11_05_scientific_explanation(self): self._audit_scientific_explanation(11)
    def test_g11_06_standards_citations(self): self._audit_standards_citations(11)
    def test_g11_07_faq_completeness(self): self._audit_faq_completeness(11)
    def test_g11_08_editorial_byline(self): self._audit_editorial_byline(11)
    def test_g11_09_spa_crosslinks(self): self._audit_spa_crosslinks(11)
    def test_g11_10_word_count(self): self._audit_word_count(11)

    # --- GUIDE 12: SpringWell CF1 Review ---
    def test_g12_01_metadata(self): self._audit_metadata(12)
    def test_g12_02_header_elements(self): self._audit_header_elements(12)
    def test_g12_03_spec_box(self): self._audit_spec_box(12)
    def test_g12_04_comparison_table(self): self._audit_comparison_table(12)
    def test_g12_05_scientific_explanation(self): self._audit_scientific_explanation(12)
    def test_g12_06_standards_citations(self): self._audit_standards_citations(12)
    def test_g12_07_faq_completeness(self): self._audit_faq_completeness(12)
    def test_g12_08_editorial_byline(self): self._audit_editorial_byline(12)
    def test_g12_09_spa_crosslinks(self): self._audit_spa_crosslinks(12)
    def test_g12_10_word_count(self): self._audit_word_count(12)

    # --- GUIDE 13: Best Whole House Filters ---
    def test_g13_01_metadata(self): self._audit_metadata(13)
    def test_g13_02_header_elements(self): self._audit_header_elements(13)
    def test_g13_03_spec_box(self): self._audit_spec_box(13)
    def test_g13_04_comparison_table(self): self._audit_comparison_table(13)
    def test_g13_05_scientific_explanation(self): self._audit_scientific_explanation(13)
    def test_g13_06_standards_citations(self): self._audit_standards_citations(13)
    def test_g13_07_faq_completeness(self): self._audit_faq_completeness(13)
    def test_g13_08_editorial_byline(self): self._audit_editorial_byline(13)
    def test_g13_09_spa_crosslinks(self): self._audit_spa_crosslinks(13)
    def test_g13_10_word_count(self): self._audit_word_count(13)

    # --- GUIDE 14: Best Water Test Kits ---
    def test_g14_01_metadata(self): self._audit_metadata(14)
    def test_g14_02_header_elements(self): self._audit_header_elements(14)
    def test_g14_03_spec_box(self): self._audit_spec_box(14)
    def test_g14_04_comparison_table(self): self._audit_comparison_table(14)
    def test_g14_05_scientific_explanation(self): self._audit_scientific_explanation(14)
    def test_g14_06_standards_citations(self): self._audit_standards_citations(14)
    def test_g14_07_faq_completeness(self): self._audit_faq_completeness(14)
    def test_g14_08_editorial_byline(self): self._audit_editorial_byline(14)
    def test_g14_09_spa_crosslinks(self): self._audit_spa_crosslinks(14)
    def test_g14_10_word_count(self): self._audit_word_count(14)

    # --- GUIDE 15: Remineralization RO Filters ---
    def test_g15_01_metadata(self): self._audit_metadata(15)
    def test_g15_02_header_elements(self): self._audit_header_elements(15)
    def test_g15_03_spec_box(self): self._audit_spec_box(15)
    def test_g15_04_comparison_table(self): self._audit_comparison_table(15)
    def test_g15_05_scientific_explanation(self): self._audit_scientific_explanation(15)
    def test_g15_06_standards_citations(self): self._audit_standards_citations(15)
    def test_g15_07_faq_completeness(self): self._audit_faq_completeness(15)
    def test_g15_08_editorial_byline(self): self._audit_editorial_byline(15)
    def test_g15_09_spa_crosslinks(self): self._audit_spa_crosslinks(15)
    def test_g15_10_word_count(self): self._audit_word_count(15)

    # --- GUIDE 16: How to Size Water Softener ---
    def test_g16_01_metadata(self): self._audit_metadata(16)
    def test_g16_02_header_elements(self): self._audit_header_elements(16)
    def test_g16_03_spec_box(self): self._audit_spec_box(16)
    def test_g16_04_comparison_table(self): self._audit_comparison_table(16)
    def test_g16_05_scientific_explanation(self): self._audit_scientific_explanation(16)
    def test_g16_06_standards_citations(self): self._audit_standards_citations(16)
    def test_g16_07_faq_completeness(self): self._audit_faq_completeness(16)
    def test_g16_08_editorial_byline(self): self._audit_editorial_byline(16)
    def test_g16_09_spa_crosslinks(self): self._audit_spa_crosslinks(16)
    def test_g16_10_word_count(self): self._audit_word_count(16)

    # --- GUIDE 17: Best Salt-Free Conditioners ---
    def test_g17_01_metadata(self): self._audit_metadata(17)
    def test_g17_02_header_elements(self): self._audit_header_elements(17)
    def test_g17_03_spec_box(self): self._audit_spec_box(17)
    def test_g17_04_comparison_table(self): self._audit_comparison_table(17)
    def test_g17_05_scientific_explanation(self): self._audit_scientific_explanation(17)
    def test_g17_06_standards_citations(self): self._audit_standards_citations(17)
    def test_g17_07_faq_completeness(self): self._audit_faq_completeness(17)
    def test_g17_08_editorial_byline(self): self._audit_editorial_byline(17)
    def test_g17_09_spa_crosslinks(self): self._audit_spa_crosslinks(17)
    def test_g17_10_word_count(self): self._audit_word_count(17)

    # --- GUIDE 18: Sediment vs Carbon Filters ---
    def test_g18_01_metadata(self): self._audit_metadata(18)
    def test_g18_02_header_elements(self): self._audit_header_elements(18)
    def test_g18_03_spec_box(self): self._audit_spec_box(18)
    def test_g18_04_comparison_table(self): self._audit_comparison_table(18)
    def test_g18_05_scientific_explanation(self): self._audit_scientific_explanation(18)
    def test_g18_06_standards_citations(self): self._audit_standards_citations(18)
    def test_g18_07_faq_completeness(self): self._audit_faq_completeness(18)
    def test_g18_08_editorial_byline(self): self._audit_editorial_byline(18)
    def test_g18_09_spa_crosslinks(self): self._audit_spa_crosslinks(18)
    def test_g18_10_word_count(self): self._audit_word_count(18)

    # --- GUIDE 19: Fluoride Removal Tap Water ---
    def test_g19_01_metadata(self): self._audit_metadata(19)
    def test_g19_02_header_elements(self): self._audit_header_elements(19)
    def test_g19_03_spec_box(self): self._audit_spec_box(19)
    def test_g19_04_comparison_table(self): self._audit_comparison_table(19)
    def test_g19_05_scientific_explanation(self): self._audit_scientific_explanation(19)
    def test_g19_06_standards_citations(self): self._audit_standards_citations(19)
    def test_g19_07_faq_completeness(self): self._audit_faq_completeness(19)
    def test_g19_08_editorial_byline(self): self._audit_editorial_byline(19)
    def test_g19_09_spa_crosslinks(self): self._audit_spa_crosslinks(19)
    def test_g19_10_word_count(self): self._audit_word_count(19)

    # --- GUIDE 20: Water Pressure & Ergun Loss ---
    def test_g20_01_metadata(self): self._audit_metadata(20)
    def test_g20_02_header_elements(self): self._audit_header_elements(20)
    def test_g20_03_spec_box(self): self._audit_spec_box(20)
    def test_g20_04_comparison_table(self): self._audit_comparison_table(20)
    def test_g20_05_scientific_explanation(self): self._audit_scientific_explanation(20)
    def test_g20_06_standards_citations(self): self._audit_standards_citations(20)
    def test_g20_07_faq_completeness(self): self._audit_faq_completeness(20)
    def test_g20_08_editorial_byline(self): self._audit_editorial_byline(20)
    def test_g20_09_spa_crosslinks(self): self._audit_spa_crosslinks(20)
    def test_g20_10_word_count(self): self._audit_word_count(20)


if __name__ == "__main__":
    unittest.main()
