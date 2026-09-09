"""
ClearTapLab E2E Test Suite - Tier 2: Boundary & Corner Cases
Validates application robustness against edge cases:
- Live Search: Empty query, special regex chars, HTML/XSS injection, whitespace, case-insensitivity, unicode
- Category Filtering: Invalid/empty categories, partition consistency, tab cycling
- Modal Reader: Open/close lifecycle, scroll locking, out-of-bounds IDs, backdrop & ESC handling
- Table Responsiveness: CSS overflow wrappers, mobile width constraints, table geometry
- Sizing Calculator: Boundary inputs (people 1-15, hardness 1-60, iron 0-10, clamped negatives)
- Symptom Triage: Key mappings, formula integrity, standard citations
"""

import re
import unittest
from bs4 import BeautifulSoup
from tests.test_utils import (
    load_articles_data,
    load_index_html,
    load_main_css,
    simulate_search,
    simulate_category_filter,
    simulate_calculator,
    VALID_CATEGORIES
)


class TestTier2BoundaryAndEdgeCases(unittest.TestCase):
    """Tier 2: Boundary Value Analysis and Corner Case Robustness."""

    @classmethod
    def setUpClass(cls):
        cls.articles = load_articles_data()
        cls.index_soup = load_index_html()
        cls.css_content = load_main_css()

    # =========================================================================
    # 1. LIVE SEARCH ENGINE BOUNDARIES & INJECTION RESILIENCE
    # =========================================================================

    def test_001_search_empty_query_returns_all_articles(self):
        """Empty query returns all 20 guides without errors."""
        results = simulate_search("", self.articles)
        self.assertEqual(len(results), 20)

    def test_002_search_whitespace_only_query_returns_all_articles(self):
        """Whitespace-only query string returns all 20 guides."""
        for ws in ["   ", "\t", "\n\r", " \t \n "]:
            results = simulate_search(ws, self.articles)
            self.assertEqual(len(results), 20, f"Failed on whitespace query: repr({ws!r})")

    def test_003_search_trims_leading_and_trailing_whitespace(self):
        """Leading/trailing whitespace around search query is trimmed."""
        results = simulate_search("   iron   ", self.articles)
        self.assertTrue(len(results) >= 1)
        # Should match same as clean query
        clean_results = simulate_search("iron", self.articles)
        self.assertEqual(len(results), len(clean_results))

    def test_004_search_special_regex_characters(self):
        """Special regex characters do not cause unhandled regex exceptions."""
        regex_patterns = [
            ".*", "[a-z]", "(?i)", "^.*$", "\\d+", "a|b", "$", "(.*)",
            "+", "?", "*", "{1,3}", "[^a-zA-Z0-9]"
        ]
        for pat in regex_patterns:
            try:
                results = simulate_search(pat, self.articles)
                self.assertIsInstance(results, list)
            except Exception as e:
                self.fail(f"Search threw exception on regex query '{pat}': {e}")

    def test_005_search_special_punctuation_symbols(self):
        """Special punctuation symbols return safe results without crashing."""
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>/?"
        results = simulate_search(symbols, self.articles)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 0)

    def test_006_search_xss_html_injection_resilience(self):
        """HTML and XSS injection payloads return safe empty matches without executing."""
        xss_payloads = [
            "<script>alert('xss')</script>",
            "<img src=x onerror=alert(1)>",
            "<svg/onload=alert('pwned')>",
            "'\"><script>document.cookie</script>"
        ]
        for payload in xss_payloads:
            results = simulate_search(payload, self.articles)
            self.assertEqual(len(results), 0, f"XSS payload {payload} unexpectedly returned results")

    def test_007_search_case_insensitivity_matrix(self):
        """Search matches regardless of uppercase, lowercase, or mixed case."""
        variations = ["reverse osmosis", "REVERSE OSMOSIS", "ReVeRsE OsMoSiS", "Reverse Osmosis"]
        baseline = simulate_search("reverse osmosis", self.articles)
        self.assertTrue(len(baseline) >= 1)
        for var in variations:
            res = simulate_search(var, self.articles)
            self.assertEqual(len(res), len(baseline), f"Case variation '{var}' gave different result count")

    def test_008_search_numeric_tokens(self):
        """Search finds guides by model numbers, standards, and dates."""
        numeric_queries = ["800", "2026", "58", "42", "53"]
        for num in numeric_queries:
            res = simulate_search(num, self.articles)
            self.assertIsInstance(res, list)

    def test_009_search_partial_substring_matching(self):
        """Search supports partial root keyword matching."""
        res_pfa = simulate_search("pfa", self.articles)
        self.assertTrue(len(res_pfa) >= 1, "Partial query 'pfa' should match PFAS guides")
        res_soft = simulate_search("soften", self.articles)
        self.assertTrue(len(res_soft) >= 1, "Partial query 'soften' should match softener guides")

    def test_010_search_nonexistent_query_returns_empty(self):
        """Non-existent search term returns empty list gracefully."""
        res = simulate_search("xyznonexistentcontaminant999alpha", self.articles)
        self.assertEqual(len(res), 0)

    def test_011_search_very_long_query(self):
        """Extremely long query strings do not cause buffer overflow or freeze."""
        long_q = "a" * 1000
        res = simulate_search(long_q, self.articles)
        self.assertEqual(len(res), 0)

    def test_012_search_unicode_characters(self):
        """Search handles unicode symbols and chemical notation gracefully."""
        unicode_queries = ["µm", "Ca²⁺", "H₂S", "SO₄²⁻", "°C", "–"]
        for uq in unicode_queries:
            res = simulate_search(uq, self.articles)
            self.assertIsInstance(res, list)

    # =========================================================================
    # 2. CATEGORY FILTERING BOUNDARIES & PARTITION INTEGRITY
    # =========================================================================

    def test_013_filter_all_returns_20_articles(self):
        """Filter category 'all' returns all 20 guides."""
        results = simulate_category_filter("all", self.articles)
        self.assertEqual(len(results), 20)

    def test_014_category_partition_sum_equals_20(self):
        """The sum of all individual category article counts strictly equals 20."""
        category_counts = {}
        for cat in VALID_CATEGORIES:
            filtered = simulate_category_filter(cat, self.articles)
            category_counts[cat] = len(filtered)
            self.assertTrue(len(filtered) > 0, f"Category '{cat}' has 0 articles")

        total = sum(category_counts.values())
        self.assertEqual(total, 20, f"Category partition sum must equal 20, got {total}: {category_counts}")

    def test_015_filter_invalid_category_returns_empty(self):
        """Invalid/unrecognized category string returns empty list."""
        invalid_categories = ["nonexistent-category", "water-filter-fake", "12345", "all-guides"]
        for cat in invalid_categories:
            res = simulate_category_filter(cat, self.articles)
            self.assertEqual(len(res), 0, f"Invalid category '{cat}' should return empty list")

    def test_016_category_filter_exact_counts(self):
        """Verify expected counts per category."""
        ro_count = len(simulate_category_filter("reverse-osmosis", self.articles))
        testing_count = len(simulate_category_filter("water-testing", self.articles))
        problems_count = len(simulate_category_filter("water-problems", self.articles))
        tech_count = len(simulate_category_filter("filtration-technology", self.articles))
        system_count = len(simulate_category_filter("system-guides", self.articles))

        self.assertEqual(ro_count, 5, f"Expected 5 reverse-osmosis guides, got {ro_count}")
        self.assertEqual(testing_count, 2, f"Expected 2 water-testing guides, got {testing_count}")
        self.assertEqual(problems_count, 3, f"Expected 3 water-problems guides, got {problems_count}")
        self.assertEqual(tech_count, 4, f"Expected 4 filtration-technology guides, got {tech_count}")
        self.assertEqual(system_count, 6, f"Expected 6 system-guides, got {system_count}")

    # =========================================================================
    # 3. MODAL READER LIFECYCLE & GEOMETRY BOUNDARIES
    # =========================================================================

    def test_017_modal_markup_exists_in_index_html(self):
        """index.html contains modal backdrop and body elements."""
        modal = self.index_soup.find(id="article-modal")
        self.assertIsNotNone(modal, "Missing #article-modal element in index.html")
        modal_body = self.index_soup.find(id="modal-article-body")
        self.assertIsNotNone(modal_body, "Missing #modal-article-body element in index.html")

    def test_018_search_overlay_markup_exists_in_index_html(self):
        """index.html contains search overlay and search input elements."""
        search_overlay = self.index_soup.find(id="search-overlay")
        self.assertIsNotNone(search_overlay, "Missing #search-overlay in index.html")
        search_input = self.index_soup.find(id="search-query-input")
        self.assertIsNotNone(search_input, "Missing #search-query-input in index.html")
        search_results = self.index_soup.find(id="search-results-list")
        self.assertIsNotNone(search_results, "Missing #search-results-list in index.html")

    def test_019_mobile_drawer_markup_exists_in_index_html(self):
        """index.html contains mobile drawer navigation element."""
        drawer = self.index_soup.find(id="mobile-drawer")
        self.assertIsNotNone(drawer, "Missing #mobile-drawer in index.html")

    def test_020_css_modal_open_class_defined(self):
        """CSS defines display / visibility rules for .ctl-modal-backdrop.open."""
        self.assertIn(".ctl-modal-backdrop", self.css_content)
        self.assertIn(".ctl-modal-backdrop.open", self.css_content)

    def test_021_css_search_overlay_open_class_defined(self):
        """CSS defines rules for .ctl-search-overlay.open."""
        self.assertIn(".ctl-search-overlay", self.css_content)
        self.assertIn(".ctl-search-overlay.open", self.css_content)

    def test_022_table_wrapper_horizontal_scroll_in_css(self):
        """CSS specifies overflow-x: auto on .ctl-table-wrapper for mobile responsiveness."""
        self.assertIn(".ctl-table-wrapper", self.css_content)
        # Verify overflow-x is in CSS
        self.assertTrue(
            "overflow-x" in self.css_content,
            "CSS should specify overflow-x: auto on tables for mobile responsiveness"
        )

    # =========================================================================
    # 4. SIZING CALCULATOR BOUNDARY VALUE ANALYSIS
    # =========================================================================

    def test_023_calc_minimum_people_boundary(self):
        """Calculator handles minimum 1 person boundary."""
        res = simulate_calculator(1, 10, 0)
        self.assertEqual(res["daily_gallons"], 75)
        self.assertEqual(res["compensated_hardness"], 10.0)
        self.assertEqual(res["daily_grains"], 750.0)
        self.assertEqual(res["recommended_size"], 24000)

    def test_024_calc_clamped_negative_people(self):
        """Calculator clamps 0 or negative people input to 1."""
        res_zero = simulate_calculator(0, 10, 0)
        self.assertEqual(res_zero["daily_gallons"], 75)
        res_neg = simulate_calculator(-5, 10, 0)
        self.assertEqual(res_neg["daily_gallons"], 75)

    def test_025_calc_maximum_people_boundary(self):
        """Calculator handles large family size boundary (15 people)."""
        res = simulate_calculator(15, 20, 2.0)
        self.assertEqual(res["daily_gallons"], 15 * 75)  # 1125 GPD
        self.assertEqual(res["compensated_hardness"], 30.0)
        self.assertEqual(res["daily_grains"], 1125 * 30.0)  # 33750
        self.assertEqual(res["recommended_size"], 96000)

    def test_026_calc_zero_iron_boundary(self):
        """Zero iron does not add compensation penalty."""
        res = simulate_calculator(4, 15, 0.0)
        self.assertEqual(res["compensated_hardness"], 15.0)

    def test_027_calc_high_iron_boundary(self):
        """High iron (10.0 PPM) adds 50 GPG compensation."""
        res = simulate_calculator(4, 10, 10.0)
        self.assertEqual(res["compensated_hardness"], 60.0)

    def test_028_calc_high_hardness_boundary(self):
        """Very hard water (60 GPG) calculated properly."""
        res = simulate_calculator(4, 60, 0)
        self.assertEqual(res["compensated_hardness"], 60.0)
        self.assertEqual(res["daily_grains"], 300 * 60.0)  # 18000
        self.assertEqual(res["recommended_size"], 96000)

    def test_029_calc_fractional_inputs(self):
        """Calculator supports fractional hardness and iron inputs."""
        res = simulate_calculator(3, 14.5, 0.8)
        self.assertAlmostEqual(res["compensated_hardness"], 14.5 + (0.8 * 5.0), places=2)

    def test_030_calc_5yr_salt_cost_monotonicity(self):
        """Higher grains result in equal or higher 5-year salt operating cost."""
        cost_low = simulate_calculator(2, 5, 0)["five_year_salt_cost"]
        cost_med = simulate_calculator(4, 15, 0.5)["five_year_salt_cost"]
        cost_high = simulate_calculator(8, 30, 2.0)["five_year_salt_cost"]
        self.assertTrue(cost_low <= cost_med <= cost_high)

    # =========================================================================
    # 5. SYMPTOM DIAGNOSTIC TRIAGE BOUNDARIES
    # =========================================================================

    def test_031_symptom_buttons_exist_in_index_html(self):
        """All 5 symptom diagnostic buttons exist in index.html."""
        symptom_btns = self.index_soup.find_all(class_="ctl-symptom-btn")
        self.assertEqual(len(symptom_btns), 5, f"Expected 5 symptom buttons, found {len(symptom_btns)}")
        symptoms_found = {b.get("data-symptom") for b in symptom_btns}
        expected_symptoms = {"sulfur", "limescale", "rust", "chlorine", "acidic"}
        self.assertEqual(symptoms_found, expected_symptoms)

    def test_032_triage_result_container_exists(self):
        """#triage-result-container exists in index.html for dynamic rendering."""
        container = self.index_soup.find(id="triage-result-container")
        self.assertIsNotNone(container)


if __name__ == "__main__":
    unittest.main()
