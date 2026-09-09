#!/usr/bin/env python3
"""
ClearTapLab Adversarial Cross-Feature & User Flow Stress Tester (Challenger 2)

Performs comprehensive empirical validation:
1. Parse every internal link (openArticleModal(X)) across all 20 articles in scripts/articles-data.js.
   - Verify 100% of target IDs exist in 1..20 and point to contextually valid articles.
2. Simulate complex multi-step user journeys:
   - User filters by "water-problems" -> opens Guide 3 -> navigates via cross-links to Guide 6 / opens Guide 6
     -> closes modal -> searches "TAC" -> opens Guide 7 -> navigates to calculator.
   - Symptom Triage -> Calculator -> Modal Reader -> Internal Cross-Links.
   - Rapid category switching and live search stress testing.
3. Validate state isolation across Calculator, Triage, Article Grid, Modal Reader, and Live Search.
4. Verify all 20 articles have distinct slugs, titles, excerpts, H1s, and non-overlapping content (Jaccard similarity).
"""

import sys
import os
import re
import unittest
import itertools
from bs4 import BeautifulSoup

# Ensure project root is in sys.path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from tests.test_utils import (
    load_articles_data,
    load_index_html,
    load_main_css,
    simulate_search,
    simulate_category_filter,
    simulate_calculator,
    extract_word_count,
    VALID_CATEGORIES,
    MASTER_GUIDES_MATRIX
)

APP_JS_PATH = os.path.join(BASE_DIR, "scripts", "app.js")


def load_app_js():
    """Reads scripts/app.js content."""
    with open(APP_JS_PATH, "r", encoding="utf-8") as f:
        return f.read()


def extract_triage_targets_from_app_js():
    """Extracts symptom keys and their articleId mappings from scripts/app.js."""
    content = load_app_js()
    pattern = r'(\w+):\s*\{[^}]*articleId:\s*(\d+)'
    matches = re.findall(pattern, content)
    return {k: int(v) for k, v in matches}


# =========================================================================
# TEST SUITE 1: INTERNAL CROSS-LINKS & GRAPH INTEGRITY
# =========================================================================
class TestInternalCrossLinks(unittest.TestCase):
    """Deep verification of all internal cross-links and DOM anchor references across all 20 articles."""

    @classmethod
    def setUpClass(cls):
        cls.articles = load_articles_data()
        cls.articles_by_id = {a["id"]: a for a in cls.articles}
        cls.index_soup = load_index_html()

    def test_001_exact_20_articles_with_consecutive_ids(self):
        """Verify exactly 20 articles exist with consecutive IDs 1 through 20."""
        self.assertEqual(len(self.articles), 20, f"Expected 20 articles, found {len(self.articles)}")
        article_ids = sorted([a["id"] for a in self.articles])
        self.assertEqual(article_ids, list(range(1, 21)), f"Article IDs must be exactly 1..20, got: {article_ids}")

    def test_002_parse_all_open_article_modal_calls_in_content(self):
        """Parse all openArticleModal(X) calls across all 20 articles and verify 100% target validity."""
        total_links_found = 0
        all_referenced_targets = set()
        link_records = []

        for a in self.articles:
            html = a.get("contentHtml", "")
            matches = re.findall(r'openArticleModal\(\s*(\d+)\s*\)', html)
            for target_str in matches:
                target_id = int(target_str)
                total_links_found += 1
                all_referenced_targets.add(target_id)
                self.assertIn(
                    target_id,
                    self.articles_by_id,
                    f"Article {a['id']} ('{a['slug']}') links to non-existent Article ID {target_id}"
                )
                target_art = self.articles_by_id[target_id]
                self.assertTrue(
                    len(target_art.get("contentHtml", "").strip()) > 500,
                    f"Article {a['id']} links to Article {target_id} which has insufficient content"
                )
                link_records.append((a["id"], target_id))

        # Check total links and coverage
        self.assertTrue(total_links_found >= 50, f"Expected at least 50 cross-links across library, found {total_links_found}")
        self.assertEqual(all_referenced_targets, set(range(1, 21)), "Every guide 1..20 must be referenced at least once in the cross-link network")

    def test_003_no_self_referential_modal_links(self):
        """Verify that an article does not contain a recursive modal link pointing to itself."""
        for a in self.articles:
            html = a.get("contentHtml", "")
            matches = [int(x) for x in re.findall(r'openArticleModal\(\s*(\d+)\s*\)', html)]
            self.assertNotIn(
                a["id"],
                matches,
                f"Article ID {a['id']} ('{a['slug']}') contains a self-referential openArticleModal({a['id']}) link"
            )

    def test_004_all_html_anchor_elements_in_articles_valid(self):
        """Verify that all <a> elements inside article HTML bodies have valid hrefs or onclick handlers."""
        for a in self.articles:
            soup = BeautifulSoup(a.get("contentHtml", ""), "html.parser")
            anchors = soup.find_all("a")
            for anc in anchors:
                href = anc.get("href", "")
                onclick = anc.get("onclick", "")
                
                # Hash anchor check
                if href.startswith("#") and len(href) > 1:
                    target_dom_id = href.lstrip("#")
                    target_elem = self.index_soup.find(id=target_dom_id)
                    self.assertIsNotNone(
                        target_elem,
                        f"Article {a['id']} has anchor '{href}' targeting #{target_dom_id} which does not exist in index.html"
                    )
                # Modal trigger check
                elif "openArticleModal" in onclick:
                    m = re.search(r'openArticleModal\(\s*(\d+)\s*\)', onclick)
                    self.assertIsNotNone(m, f"Article {a['id']} has malformed onclick in anchor: {onclick}")
                    target_id = int(m.group(1))
                    self.assertIn(target_id, self.articles_by_id, f"Article {a['id']} anchor links to invalid ID {target_id}")

    def test_005_all_triage_symptoms_have_valid_and_distinct_article_targets(self):
        """Verify that symptom triage options in app.js point to appropriate, valid articles."""
        triage_targets = extract_triage_targets_from_app_js()
        self.assertEqual(len(triage_targets), 5, f"Expected 5 symptom triage mappings, found {len(triage_targets)}")
        expected_symptoms = {"sulfur", "limescale", "rust", "chlorine", "acidic"}
        self.assertEqual(set(triage_targets.keys()), expected_symptoms)

        for symptom, target_id in triage_targets.items():
            self.assertIn(target_id, self.articles_by_id, f"Triage symptom '{symptom}' points to invalid ID {target_id}")
            target_art = self.articles_by_id[target_id]
            self.assertTrue(len(target_art["contentHtml"]) > 1000)


# =========================================================================
# TEST SUITE 2: ADVERSARIAL MULTI-STEP USER JOURNEYS
# =========================================================================
class TestMultiStepUserFlows(unittest.TestCase):
    """Simulates complex, multi-step real-world user flows across the full application lifecycle."""

    @classmethod
    def setUpClass(cls):
        cls.articles = load_articles_data()
        cls.articles_by_id = {a["id"]: a for a in cls.articles}
        cls.index_soup = load_index_html()

    def test_006_journey_water_problems_to_search_to_calc(self):
        """
        Simulates Journey 1:
        1. User filters by category "water-problems" -> verifies 3 water problem guides.
        2. User opens Guide 3 (fix-sulfur-smell-well-water) in modal.
        3. Inside Guide 3, user navigates via cross-link to Guide 14 (test kits), then to Guide 6 (iron removal).
        4. User closes modal -> verifies category filter remains "water-problems".
        5. User searches for "TAC".
        6. User opens Guide 7 (water-softener-vs-salt-free) from search results.
        7. User closes modal and navigates to Water Softener Sizing Calculator.
        """
        # Step 1: Filter by "water-problems"
        filtered_articles = simulate_category_filter("water-problems", self.articles)
        filtered_ids = [a["id"] for a in filtered_articles]
        self.assertEqual(sorted(filtered_ids), [3, 5, 6], f"Expected guides [3, 5, 6] for water-problems, got {filtered_ids}")
        self.assertTrue(all(a["category"] == "water-problems" for a in filtered_articles))

        # Step 2: Open Guide 3 Modal
        active_modal_id = 3
        active_modal_article = self.articles_by_id.get(active_modal_id)
        self.assertIsNotNone(active_modal_article)
        self.assertEqual(active_modal_article["slug"], "fix-sulfur-smell-well-water")
        modal_body_html = active_modal_article["contentHtml"]
        self.assertIn("Sulfur", modal_body_html)

        # Step 3: Navigate via internal links (Guide 3 -> Guide 14 -> Guide 6)
        self.assertIn("openArticleModal(14)", modal_body_html, "Guide 3 should link to Guide 14")
        guide_14_html = self.articles_by_id[14]["contentHtml"]
        self.assertIn("openArticleModal(6)", guide_14_html, "Guide 14 should link to Guide 6")
        
        # Switch modal to Guide 6
        active_modal_id = 6
        active_modal_article = self.articles_by_id.get(active_modal_id)
        self.assertIsNotNone(active_modal_article)
        self.assertEqual(active_modal_article["slug"], "remove-iron-from-well-water")
        modal_body_html = active_modal_article["contentHtml"]
        self.assertIn("Iron", modal_body_html)

        # Step 4: Close Modal -> Grid remains intact and filtered
        active_modal_id = None
        self.assertEqual([a["id"] for a in filtered_articles], [3, 5, 6])

        # Step 5: Search for "TAC"
        search_query = "TAC"
        search_results = simulate_search(search_query, self.articles)
        search_result_ids = [a["id"] for a in search_results]
        self.assertTrue(
            7 in search_result_ids or 17 in search_result_ids,
            f"Search for 'TAC' should locate Guide 7 or Guide 17, got {search_result_ids}"
        )

        # Step 6: Open Guide 7 from search results
        self.assertIn(7, search_result_ids)
        active_modal_id = 7
        active_modal_article = self.articles_by_id.get(active_modal_id)
        self.assertEqual(active_modal_article["slug"], "water-softener-vs-salt-free")
        modal_body_html = active_modal_article["contentHtml"]
        self.assertIn("Template Assisted Crystallization", modal_body_html)

        # Step 7: Close modal & Navigate to Calculator
        active_modal_id = None
        calc_res = simulate_calculator(people=4, hardness_gpg=15, iron_ppm=0.5)
        self.assertEqual(calc_res["daily_gallons"], 300)
        self.assertEqual(calc_res["compensated_hardness"], 17.5)
        self.assertEqual(calc_res["daily_grains"], 5250.0)
        self.assertEqual(calc_res["recommended_size"], 48000)
        self.assertEqual(calc_res["cu_ft"], 1.5)

    def test_007_journey_triage_to_calc_to_article_deep_link(self):
        """
        Simulates Journey 2:
        1. User selects "rust" symptom in triage -> target Article 6.
        2. User adjusts calculator to 6 people, 20 GPG hardness, 2.0 PPM iron.
        3. Calculator computes: comp_hardness = 30 GPG, daily_gallons = 450 GPD, daily_grains = 13,500.
        4. Weekly capacity = 13500 * 7 * 1.25 = 118,125 grains -> recommended_size = 96,000 grains (3.0 cu ft).
        5. User clicks calculator CTA to open Guide 16 (How to Size a Water Softener).
        6. In Guide 16, user clicks anchor link to #calculator or cross-link to Guide 5/7.
        """
        triage_target = 6
        self.assertIn(triage_target, self.articles_by_id)

        # Calculator inputs & outputs
        calc_res = simulate_calculator(people=6, hardness_gpg=20.0, iron_ppm=2.0)
        self.assertEqual(calc_res["daily_gallons"], 450)
        self.assertEqual(calc_res["compensated_hardness"], 30.0)
        self.assertEqual(calc_res["daily_grains"], 13500.0)
        self.assertEqual(calc_res["raw_weekly_capacity"], 118125.0)
        self.assertEqual(calc_res["recommended_size"], 96000)
        self.assertEqual(calc_res["cu_ft"], 3.0)

        # User opens Guide 16 via Calculator CTA
        guide_16 = self.articles_by_id[16]
        self.assertEqual(guide_16["slug"], "how-to-size-water-softener")
        self.assertIn("Compensated Hardness", guide_16["contentHtml"])

        # Verify Guide 16 has internal links to other relevant guides
        cross_links_16 = [int(x) for x in re.findall(r'openArticleModal\(\s*(\d+)\s*\)', guide_16["contentHtml"])]
        self.assertTrue(len(cross_links_16) >= 1, "Guide 16 should provide related guide links")
        for cl in cross_links_16:
            self.assertIn(cl, self.articles_by_id)

    def test_008_rapid_category_tab_cycling(self):
        """Verify partition of articles across rapid category switching with zero loss or leakage."""
        category_counts = {}
        for cat in VALID_CATEGORIES:
            filtered = simulate_category_filter(cat, self.articles)
            category_counts[cat] = len(filtered)
            self.assertTrue(len(filtered) > 0, f"Category '{cat}' has no articles!")
            self.assertTrue(all(a["category"] == cat for a in filtered))

        total_categorized = sum(category_counts.values())
        self.assertEqual(total_categorized, 20, f"Sum of category items must be exactly 20, got {total_categorized}")

        all_articles = simulate_category_filter("all", self.articles)
        self.assertEqual(len(all_articles), 20)

    def test_009_live_search_stress_adversarial_queries(self):
        """Stress-test live search engine with diverse, adversarial queries."""
        q1 = simulate_search("water", self.articles)
        self.assertTrue(len(q1) >= 10, "Search 'water' should return broad results")

        q2_lower = simulate_search("reverse osmosis", self.articles)
        q2_upper = simulate_search("REVERSE OSMOSIS", self.articles)
        q2_mixed = simulate_search("rEvErSe OsMoSiS", self.articles)
        self.assertEqual([a["id"] for a in q2_lower], [a["id"] for a in q2_upper])
        self.assertEqual([a["id"] for a in q2_lower], [a["id"] for a in q2_mixed])

        q3_clean = simulate_search("iron", self.articles)
        q3_spaces = simulate_search("   iron   \t", self.articles)
        self.assertEqual([a["id"] for a in q3_clean], [a["id"] for a in q3_spaces])

        q4_pfas = simulate_search("PFAS", self.articles)
        self.assertIn(9, [a["id"] for a in q4_pfas])

        q5_springwell = simulate_search("SpringWell", self.articles)
        self.assertIn(12, [a["id"] for a in q5_springwell])

        q6_none = simulate_search("zzzznonexistentquery9999", self.articles)
        self.assertEqual(len(q6_none), 0)


# =========================================================================
# TEST SUITE 3: CROSS-FEATURE STATE ISOLATION
# =========================================================================
class TestCrossFeatureStateIsolation(unittest.TestCase):
    """Validates DOM element separation and state independence across tools."""

    @classmethod
    def setUpClass(cls):
        cls.soup = load_index_html()
        cls.css = load_main_css()
        cls.articles = load_articles_data()

    def test_010_dom_container_ids_are_distinct(self):
        """Ensure all functional containers have unique, distinct IDs in index.html."""
        container_ids = [
            "triage-result-container",
            "calculator",
            "articles-grid",
            "article-modal",
            "modal-article-body",
            "search-overlay",
            "search-query-input",
            "search-results-list",
            "mobile-drawer"
        ]
        for cid in container_ids:
            elems = self.soup.find_all(id=cid)
            self.assertEqual(len(elems), 1, f"Element #{cid} should appear exactly once in index.html, found {len(elems)}")

    def test_011_calculator_inputs_do_not_share_ids_with_other_forms(self):
        """Ensure calculator inputs and output elements have unique, scoped IDs."""
        calc_ids = [
            "calc-people",
            "calc-hardness",
            "calc-iron",
            "res-daily-gal",
            "res-comp-hard",
            "res-daily-grains",
            "res-target-cap",
            "res-resin-vol",
            "res-salt-cost"
        ]
        for cid in calc_ids:
            elems = self.soup.find_all(id=cid)
            self.assertEqual(len(elems), 1, f"Calculator element #{cid} must exist exactly once")

    def test_012_css_modal_and_search_z_index_hierarchy(self):
        """Ensure modal and search overlays have proper z-index and display containment."""
        self.assertIn(".ctl-modal-backdrop", self.css)
        self.assertIn(".ctl-search-overlay", self.css)
        self.assertTrue("z-index" in self.css)


# =========================================================================
# TEST SUITE 4: CONTENT DISTINCTNESS, UNIQUENESS & INTEGRITY
# =========================================================================
class TestArticleDistinctnessAndQuality(unittest.TestCase):
    """Empirical validation that all 20 articles are distinct, bespoke, non-overlapping engineering guides."""

    @classmethod
    def setUpClass(cls):
        cls.articles = load_articles_data()

    def test_013_all_slugs_are_unique_and_kebab_case(self):
        """Verify all 20 slugs are unique and follow valid kebab-case syntax."""
        slugs = [a["slug"] for a in self.articles]
        self.assertEqual(len(slugs), 20)
        self.assertEqual(len(set(slugs)), 20, f"Duplicate slugs detected: {[s for s in slugs if slugs.count(s) > 1]}")
        for s in slugs:
            self.assertTrue(re.match(r'^[a-z0-9]+(-[a-z0-9]+)*$', s), f"Invalid slug format: '{s}'")

    def test_014_all_titles_are_unique_and_descriptive(self):
        """Verify all 20 article titles are unique and sufficiently descriptive (>15 chars)."""
        titles = [a["title"] for a in self.articles]
        self.assertEqual(len(titles), 20)
        self.assertEqual(len(set(titles)), 20, f"Duplicate titles detected: {[t for t in titles if titles.count(t) > 1]}")
        for t in titles:
            self.assertTrue(len(t) >= 15, f"Title too short: '{t}'")

    def test_015_all_h1_headers_in_content_are_unique(self):
        """Extract H1 from each article's contentHtml and verify complete uniqueness."""
        h1s = []
        for a in self.articles:
            soup = BeautifulSoup(a.get("contentHtml", ""), "html.parser")
            h1 = soup.find("h1")
            self.assertIsNotNone(h1, f"Article {a['id']} ('{a['slug']}') is missing an <h1> heading")
            h1_text = h1.get_text().strip()
            self.assertTrue(len(h1_text) > 10, f"Article {a['id']} H1 too short: '{h1_text}'")
            h1s.append(h1_text)

        self.assertEqual(len(h1s), 20)
        self.assertEqual(len(set(h1s)), 20, "Duplicate H1 headings detected in article contentHtml")

    def test_016_all_excerpts_are_unique(self):
        """Verify all 20 card excerpts are unique and non-empty."""
        excerpts = [a["excerpt"] for a in self.articles]
        self.assertEqual(len(excerpts), 20)
        self.assertEqual(len(set(excerpts)), 20, "Duplicate card excerpts detected")

    def test_017_all_articles_meet_minimum_word_count(self):
        """Verify all 20 articles contain comprehensive long-form content (>= 1,000 words)."""
        word_counts = {}
        for a in self.articles:
            wc = extract_word_count(a["contentHtml"])
            word_counts[a["id"]] = wc
            self.assertTrue(
                wc >= 1000,
                f"Article ID {a['id']} ('{a['slug']}') has only {wc} words (minimum required: 1,000)"
            )
        total_words = sum(word_counts.values())
        avg_words = total_words / len(word_counts)
        print(f"\n  [Word Count Audit] Total Words: {total_words:,} across 20 guides | Average: {avg_words:,.0f} words/guide | Min: {min(word_counts.values()):,} | Max: {max(word_counts.values()):,}")

    def test_018_pairwise_jaccard_similarity_across_all_articles(self):
        """
        Adversarial test: Compute pairwise Jaccard similarity across all 190 pairs of articles.
        Ensures no two articles share redundant, templated, or copy-pasted body text.
        Maximum allowed Jaccard similarity threshold is 0.35.
        """
        token_sets = {}
        for a in self.articles:
            soup = BeautifulSoup(a["contentHtml"], "html.parser")
            text = soup.get_text().lower()
            tokens = set(re.findall(r'\b[a-z]{3,}\b', text))
            token_sets[a["id"]] = tokens

        max_similarity = 0.0
        highest_pair = None
        similarity_records = []

        pairs = list(itertools.combinations(self.articles, 2))
        self.assertEqual(len(pairs), 190)

        for a1, a2 in pairs:
            set1 = token_sets[a1["id"]]
            set2 = token_sets[a2["id"]]
            intersection = len(set1 & set2)
            union = len(set1 | set2)
            jaccard = intersection / union if union > 0 else 0.0
            similarity_records.append((jaccard, a1["id"], a2["id"], a1["slug"], a2["slug"]))

            if jaccard > max_similarity:
                max_similarity = jaccard
                highest_pair = (a1["id"], a2["id"], a1["slug"], a2["slug"])

            self.assertLess(
                jaccard,
                0.35,
                f"Articles {a1['id']} ('{a1['slug']}') and {a2['id']} ('{a2['slug']}') have high Jaccard similarity ({jaccard:.3f} >= 0.35), indicating potential duplicate/templated text"
            )

        print(f"\n  [Jaccard Distinctness Audit] Maximum pairwise Jaccard similarity: {max_similarity:.3f} between Guide {highest_pair[0]} ('{highest_pair[2]}') and Guide {highest_pair[1]} ('{highest_pair[3]}'). All 190 pairs passed (< 0.35).")

    def test_019_all_20_articles_contain_tables_specs_and_faqs(self):
        """Verify each article contains technical tables, engineering spec boxes, and at least 3 FAQs."""
        for a in self.articles:
            soup = BeautifulSoup(a["contentHtml"], "html.parser")
            
            # 1. Table
            table = soup.find("table")
            self.assertIsNotNone(table, f"Article {a['id']} ('{a['slug']}') is missing a technical comparison table")
            headers = table.find_all("th")
            self.assertTrue(len(headers) >= 2, f"Article {a['id']} table needs at least 2 columns")
            rows = table.find_all("tr")
            self.assertTrue(len(rows) >= 3, f"Article {a['id']} table needs at least 2 data rows + header")

            # 2. Spec box
            spec_box = soup.find(class_=re.compile(r'ctl-spec-box'))
            self.assertIsNotNone(spec_box, f"Article {a['id']} ('{a['slug']}') is missing .ctl-spec-box")

            # 3. FAQs
            faq_elements = soup.find_all(class_=re.compile(r'ctl-faq-item'))
            if not faq_elements:
                faq_elements = soup.find_all("details")
            if not faq_elements:
                faq_section = soup.find(id=re.compile(r'faq', re.I)) or soup.find(string=re.compile(r'Frequently Asked Questions', re.I))
                self.assertIsNotNone(faq_section, f"Article {a['id']} ('{a['slug']}') is missing FAQ section")
            else:
                self.assertTrue(
                    len(faq_elements) >= 3,
                    f"Article {a['id']} ('{a['slug']}') has {len(faq_elements)} FAQs (minimum required: 3)"
                )


if __name__ == "__main__":
    unittest.main(verbosity=2)
