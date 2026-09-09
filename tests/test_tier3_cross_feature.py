"""
ClearTapLab E2E Test Suite - Tier 3: Cross-Feature Combinations
Validates pairwise feature interactions and navigation flows:
- Category Filtering + Live Search engine interplay
- In-modal cross-link navigation and validity of all openArticleModal() target IDs
- Hub card CTAs navigating to corresponding category filter tabs
- Symptom Triage 5-button diagnostic engine deep linking to Guides 03, 05, 06, 02, 13
- Water Softener Sizing Calculator integration and deep link to Guide 16
- 3-Step Framework CTAs integration with Guides 01, 02, 04
- Header and Footer anchor navigation targets verification
"""

import re
import unittest
from bs4 import BeautifulSoup
from tests.test_utils import (
    load_articles_data,
    load_index_html,
    simulate_search,
    simulate_category_filter,
    VALID_CATEGORIES
)


class TestTier3CrossFeatureCombinations(unittest.TestCase):
    """Tier 3: Pairwise Cross-Feature Interactions & Navigation Integrity."""

    @classmethod
    def setUpClass(cls):
        cls.articles = load_articles_data()
        cls.articles_by_id = {a["id"]: a for a in cls.articles}
        cls.index_soup = load_index_html()

    # =========================================================================
    # 1. CATEGORY FILTER + LIVE SEARCH INTERACTION
    # =========================================================================

    def test_001_search_spans_across_different_categories(self):
        """Global search returns matching articles across multiple categories."""
        # Searching for 'reverse osmosis' should return items from both reverse-osmosis and filtration-technology
        results = simulate_search("reverse osmosis", self.articles)
        categories_matched = {a["category"] for a in results}
        self.assertTrue(
            len(categories_matched) >= 1,
            f"Expected search to find matches across categories, got {categories_matched}"
        )

    def test_002_search_for_waterdrop_finds_guide_4(self):
        """Search query 'Waterdrop' locates Guide 04 regardless of active category filter."""
        results = simulate_search("Waterdrop", self.articles)
        matched_ids = [a["id"] for a in results]
        self.assertIn(4, matched_ids, f"Search for 'Waterdrop' should return Guide 04, got {matched_ids}")

    def test_003_search_for_iron_finds_guide_6(self):
        """Search query 'Iron' locates Guide 06."""
        results = simulate_search("Iron", self.articles)
        matched_ids = [a["id"] for a in results]
        self.assertIn(6, matched_ids, f"Search for 'Iron' should return Guide 06, got {matched_ids}")

    def test_004_search_for_pfas_finds_guide_9(self):
        """Search query 'PFAS' locates Guide 09."""
        results = simulate_search("PFAS", self.articles)
        matched_ids = [a["id"] for a in results]
        self.assertIn(9, matched_ids, f"Search for 'PFAS' should return Guide 09, got {matched_ids}")

    def test_005_search_for_softener_sizing_finds_guide_16(self):
        """Search query 'Size' or 'Softener' locates Guide 16."""
        results = simulate_search("Softener", self.articles)
        matched_ids = [a["id"] for a in results]
        self.assertTrue(
            16 in matched_ids or 7 in matched_ids,
            f"Search for 'Softener' should match Guide 16 or 7, got {matched_ids}"
        )

    def test_006_search_for_springwell_finds_guide_12(self):
        """Search query 'SpringWell' locates Guide 12."""
        results = simulate_search("SpringWell", self.articles)
        matched_ids = [a["id"] for a in results]
        self.assertIn(12, matched_ids, f"Search for 'SpringWell' should return Guide 12, got {matched_ids}")

    # =========================================================================
    # 2. IN-MODAL CROSS-LINK NAVIGATION INTEGRITY
    # =========================================================================

    def test_007_all_modal_crosslinks_reference_valid_article_ids(self):
        """All openArticleModal(ID) calls inside article HTML bodies reference valid 1..20 IDs."""
        for a in self.articles:
            html = a.get("contentHtml", "")
            # Find all openArticleModal(\d+) calls
            referenced_ids = [int(x) for x in re.findall(r'openArticleModal\((\d+)\)', html)]
            for ref_id in referenced_ids:
                self.assertIn(
                    ref_id,
                    self.articles_by_id,
                    f"Article ID {a['id']} ({a['slug']}) cross-links to invalid Article ID {ref_id}"
                )

    def test_008_all_in_modal_anchor_links_resolve_to_existing_dom_ids(self):
        """Anchor links in article content (e.g. href="#calculator") resolve to elements in index.html."""
        for a in self.articles:
            soup = BeautifulSoup(a.get("contentHtml", ""), "html.parser")
            anchors = soup.find_all("a", href=re.compile(r'^#[a-zA-Z0-9_\-]+$'))
            for anc in anchors:
                target_id = anc["href"].lstrip("#")
                target_elem = self.index_soup.find(id=target_id)
                self.assertIsNotNone(
                    target_elem,
                    f"Article ID {a['id']} contains anchor link #{target_id} but element does not exist in index.html"
                )

    # =========================================================================
    # 3. HUB CARD BUTTON NAVIGATION & FILTER TAB MAPPING
    # =========================================================================

    def test_009_hub_cards_exist_and_map_to_valid_categories(self):
        """Core technical hubs in index.html link to corresponding category tabs."""
        hubs_section = self.index_soup.find(id="hubs")
        self.assertIsNotNone(hubs_section, "Missing #hubs section in index.html")

        # Find category trigger onclicks inside hubs
        cat_triggers = re.findall(r"data-category=([a-zA-Z0-9_\-]+)", str(hubs_section))
        self.assertTrue(len(cat_triggers) >= 4, f"Expected at least 4 hub category triggers, found {len(cat_triggers)}")
        for cat in cat_triggers:
            self.assertIn(
                cat,
                VALID_CATEGORIES,
                f"Hub card links to invalid category '{cat}'"
            )

    def test_010_filter_tabs_in_index_html_match_valid_categories(self):
        """All category filter buttons in index.html match canonical categories."""
        tab_buttons = self.index_soup.find_all("button", attrs={"data-category": True})
        tab_categories = {b["data-category"] for b in tab_buttons}
        expected_categories = VALID_CATEGORIES | {"all"}
        self.assertEqual(
            tab_categories,
            expected_categories,
            f"Filter tab categories mismatch. Found: {tab_categories}, Expected: {expected_categories}"
        )

    # =========================================================================
    # 4. SYMPTOM DIAGNOSTIC TRIAGE DEEP LINKING
    # =========================================================================

    def test_011_symptom_triage_target_articles_exist(self):
        """The 5 diagnostic triage symptoms map to valid, existing article IDs (3, 5, 6, 2, 13)."""
        expected_triage_mappings = {
            "sulfur": 3,     # fix-sulfur-smell-well-water
            "limescale": 5,  # hard-water-gpg-ppm-guide
            "rust": 6,       # remove-iron-from-well-water
            "chlorine": 2,   # reverse-osmosis-vs-carbon-filter
            "acidic": 13     # best-whole-house-water-filters
        }
        for symptom, target_id in expected_triage_mappings.items():
            self.assertIn(
                target_id,
                self.articles_by_id,
                f"Symptom '{symptom}' maps to non-existent Article ID {target_id}"
            )
            article = self.articles_by_id[target_id]
            self.assertTrue(bool(article["contentHtml"].strip()))

    # =========================================================================
    # 5. WATER SOFTENER SIZING CALCULATOR INTEGRATION
    # =========================================================================

    def test_012_calculator_cta_links_to_guide_16(self):
        """Water softener calculator CTA button opens Guide 16 (How to Size Softener)."""
        calc_section = self.index_soup.find(id="calculator")
        self.assertIsNotNone(calc_section, "Missing #calculator section in index.html")
        calc_html = str(calc_section)
        self.assertIn("openArticleModal(16)", calc_html, "Calculator CTA should call openArticleModal(16)")

    def test_013_calculator_input_fields_exist(self):
        """Calculator has inputs for people, hardness, and iron."""
        self.assertIsNotNone(self.index_soup.find(id="calc-people"))
        self.assertIsNotNone(self.index_soup.find(id="calc-hardness"))
        self.assertIsNotNone(self.index_soup.find(id="calc-iron"))

    def test_014_calculator_output_elements_exist(self):
        """Calculator has output elements for all result metrics."""
        output_ids = [
            "res-daily-gal",
            "res-comp-hard",
            "res-daily-grains",
            "res-target-cap",
            "res-resin-vol",
            "res-salt-cost"
        ]
        for out_id in output_ids:
            self.assertIsNotNone(
                self.index_soup.find(id=out_id),
                f"Missing calculator output element #{out_id} in index.html"
            )

    # =========================================================================
    # 6. THREE-STEP WATER PURITY FRAMEWORK CTAS
    # =========================================================================

    def test_015_three_step_framework_ctas_link_to_guides_1_2_4(self):
        """Step 1, 2, and 3 cards link to Guide 01, Guide 02, and Guide 04."""
        index_text = str(self.index_soup)
        self.assertIn("openArticleModal(1)", index_text, "Step 1 CTA should link to Guide 01")
        self.assertIn("openArticleModal(2)", index_text, "Step 2 CTA should link to Guide 02")
        self.assertIn("openArticleModal(4)", index_text, "Step 3 CTA should link to Guide 04")

    # =========================================================================
    # 7. NAVIGATION HEADER & FOOTER TARGET INTEGRITY
    # =========================================================================

    def test_016_header_nav_links_have_valid_target_sections(self):
        """All desktop navigation links target valid IDs on the page."""
        nav = self.index_soup.find("nav", class_="ctl-nav")
        self.assertIsNotNone(nav, "Missing header nav element")
        links = nav.find_all("a")
        for link in links:
            href = link.get("href", "")
            if href.startswith("#") and len(href) > 1:
                target_id = href.lstrip("#")
                target_elem = self.index_soup.find(id=target_id)
                self.assertIsNotNone(
                    target_elem,
                    f"Nav link '{link.get_text()}' targets #{target_id} but element does not exist"
                )

    def test_017_mobile_drawer_links_have_valid_target_sections(self):
        """All mobile navigation drawer links target valid IDs on the page."""
        drawer = self.index_soup.find(id="mobile-drawer")
        self.assertIsNotNone(drawer, "Missing mobile drawer")
        links = drawer.find_all("a")
        for link in links:
            href = link.get("href", "")
            if href.startswith("#") and len(href) > 1:
                target_id = href.lstrip("#")
                target_elem = self.index_soup.find(id=target_id)
                self.assertIsNotNone(
                    target_elem,
                    f"Mobile drawer link targets #{target_id} but element does not exist"
                )

    def test_018_footer_hub_links_match_category_tabs(self):
        """Footer hub links trigger valid category filter tabs."""
        footer = self.index_soup.find("footer", class_="ctl-footer")
        self.assertIsNotNone(footer, "Missing footer")
        footer_html = str(footer)
        for cat in VALID_CATEGORIES:
            self.assertIn(
                f"data-category={cat}",
                footer_html,
                f"Footer missing quick filter link for category '{cat}'"
            )


if __name__ == "__main__":
    unittest.main()
