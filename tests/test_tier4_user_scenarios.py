"""
ClearTapLab E2E Test Suite - Tier 4: Real-World User Scenarios
Validates complete multi-step end-to-end user journeys:
- Scenario 1: Reverse Osmosis Research, Review & Sizing Workflow (Guides 02, 04, 08, 10, 11, 15)
- Scenario 2: Well Water Emergency Sulfur & Iron Diagnostic Workflow (Triage + Guides 03, 06, 14)
- Scenario 3: Hard Water Calculation & Water Softener Sizing Workflow (Guide 05 + Calculator + Guides 16, 07, 17)
- Scenario 4: Municipal CCR Water Quality Report & Lab Test Workflow (Guides 01, 09, 14, 12, 13)
"""

import unittest
from bs4 import BeautifulSoup
from tests.test_utils import (
    load_articles_data,
    load_index_html,
    simulate_search,
    simulate_category_filter,
    simulate_calculator
)


class TestTier4RealWorldScenarios(unittest.TestCase):
    """Tier 4: Comprehensive Multi-Step User Journeys."""

    @classmethod
    def setUpClass(cls):
        cls.articles = load_articles_data()
        cls.articles_by_id = {a["id"]: a for a in cls.articles}
        cls.index_soup = load_index_html()

    # =========================================================================
    # SCENARIO 1: REVERSE OSMOSIS RESEARCH & SIZING JOURNEY
    # =========================================================================

    def test_scenario_01_step_1_ro_hub_and_science_lookup(self):
        """Scenario 1.1: User investigates RO science in Guide 02."""
        art2 = self.articles_by_id.get(2)
        self.assertIsNotNone(art2)
        self.assertEqual(art2["slug"], "reverse-osmosis-vs-carbon-filter")
        soup = BeautifulSoup(art2["contentHtml"], "html.parser")
        text = soup.get_text()
        self.assertTrue("0.0001" in text or "Micron" in text)
        self.assertIn("Reverse Osmosis", text)

    def test_scenario_01_step_2_ro_product_review_lookup(self):
        """Scenario 1.2: User audits Waterdrop G3P800 in Guide 04."""
        art4 = self.articles_by_id.get(4)
        self.assertIsNotNone(art4)
        self.assertEqual(art4["slug"], "waterdrop-g3p800-review")
        self.assertEqual(art4["category"], "reverse-osmosis")

    def test_scenario_01_step_3_ro_roundup_benchmark(self):
        """Scenario 1.3: User reviews multi-system comparison in Guide 08."""
        art8 = self.articles_by_id.get(8)
        self.assertIsNotNone(art8)
        self.assertEqual(art8["slug"], "best-reverse-osmosis-systems")

    def test_scenario_01_step_4_ro_water_waste_analysis(self):
        """Scenario 1.4: User evaluates pure-to-drain recovery ratios in Guide 10."""
        art10 = self.articles_by_id.get(10)
        self.assertIsNotNone(art10)
        self.assertEqual(art10["slug"], "reverse-osmosis-water-waste")

    def test_scenario_01_step_5_tankless_vs_tank_evaluation(self):
        """Scenario 1.5: User breaks down tankless vs tanked RO in Guide 11."""
        art11 = self.articles_by_id.get(11)
        self.assertIsNotNone(art11)
        self.assertEqual(art11["slug"], "tankless-vs-tank-reverse-osmosis")

    def test_scenario_01_step_6_remineralization_evaluation(self):
        """Scenario 1.6: User evaluates alkaline remineralization in Guide 15."""
        art15 = self.articles_by_id.get(15)
        self.assertIsNotNone(art15)
        self.assertEqual(art15["slug"], "remineralization-reverse-osmosis-filter")

    # =========================================================================
    # SCENARIO 2: WELL WATER SULFUR SMELL & IRON DIAGNOSTIC JOURNEY
    # =========================================================================

    def test_scenario_02_step_1_sulfur_symptom_triage_interaction(self):
        """Scenario 2.1: User clicks sulfur symptom button in Triage."""
        btn_sulfur = self.index_soup.find("button", attrs={"data-symptom": "sulfur"})
        self.assertIsNotNone(btn_sulfur, "Sulfur triage button missing")

    def test_scenario_02_step_2_sulfur_guide_isolation_protocol(self):
        """Scenario 2.2: User opens Guide 03 for hot vs cold sulfur isolation."""
        art3 = self.articles_by_id.get(3)
        self.assertIsNotNone(art3)
        self.assertEqual(art3["slug"], "fix-sulfur-smell-well-water")
        soup = BeautifulSoup(art3["contentHtml"], "html.parser")
        text = soup.get_text()
        self.assertTrue("anode" in text.lower() or "isolation" in text.lower() or "sulfur" in text.lower())

    def test_scenario_02_step_3_iron_symptom_triage_and_guide(self):
        """Scenario 2.3: User identifies orange rust staining and opens Guide 06."""
        btn_rust = self.index_soup.find("button", attrs={"data-symptom": "rust"})
        self.assertIsNotNone(btn_rust, "Rust triage button missing")
        art6 = self.articles_by_id.get(6)
        self.assertIsNotNone(art6)
        self.assertEqual(art6["slug"], "remove-iron-from-well-water")

    def test_scenario_02_step_4_lab_test_kit_selection_for_well_water(self):
        """Scenario 2.4: User evaluates EPA certified mail-in well test kits in Guide 14."""
        art14 = self.articles_by_id.get(14)
        self.assertIsNotNone(art14)
        self.assertEqual(art14["slug"], "best-water-test-kits")

    # =========================================================================
    # SCENARIO 3: HARD WATER GPG/PPM CALCULATION & SOFTENER SIZING JOURNEY
    # =========================================================================

    def test_scenario_03_step_1_hardness_science_and_conversion(self):
        """Scenario 3.1: User learns GPG vs PPM conversion in Guide 05."""
        art5 = self.articles_by_id.get(5)
        self.assertIsNotNone(art5)
        self.assertEqual(art5["slug"], "hard-water-gpg-ppm-guide")

    def test_scenario_03_step_2_calculator_household_sizing_execution(self):
        """Scenario 3.2: User enters 4 people, 15 GPG hardness, 0.5 PPM iron into calculator."""
        res = simulate_calculator(people=4, hardness_gpg=15.0, iron_ppm=0.5)
        # Expected:
        # dailyGallons = 4 * 75 = 300
        # compHardness = 15 + (0.5 * 5) = 17.5 GPG
        # dailyGrains = 300 * 17.5 = 5250
        # rawWeekly = 5250 * 7 * 1.25 = 45937.5 -> rounded up to 48,000 Grains (1.5 cu ft)
        self.assertEqual(res["daily_gallons"], 300)
        self.assertEqual(res["compensated_hardness"], 17.5)
        self.assertEqual(res["daily_grains"], 5250.0)
        self.assertEqual(res["recommended_size"], 48000)
        self.assertEqual(res["cu_ft"], 1.5)

    def test_scenario_03_step_3_softener_sizing_engineering_blueprint(self):
        """Scenario 3.3: User opens Guide 16 to verify engineering sizing blueprint."""
        art16 = self.articles_by_id.get(16)
        self.assertIsNotNone(art16)
        self.assertEqual(art16["slug"], "how-to-size-water-softener")

    def test_scenario_03_step_4_softener_vs_salt_free_tradeoff(self):
        """Scenario 3.4: User compares ion-exchange vs salt-free TAC in Guide 07."""
        art7 = self.articles_by_id.get(7)
        self.assertIsNotNone(art7)
        self.assertEqual(art7["slug"], "water-softener-vs-salt-free")

    def test_scenario_03_step_5_salt_free_conditioners_benchmark(self):
        """Scenario 3.5: User reviews top TAC conditioners in Guide 17."""
        art17 = self.articles_by_id.get(17)
        self.assertIsNotNone(art17)
        self.assertEqual(art17["slug"], "best-salt-free-water-conditioners")

    # =========================================================================
    # SCENARIO 4: MUNICIPAL CCR REPORT & PFAS LAB TESTING JOURNEY
    # =========================================================================

    def test_scenario_04_step_1_ccr_report_interpretation(self):
        """Scenario 4.1: User reads municipal CCR guide (Guide 01)."""
        art1 = self.articles_by_id.get(1)
        self.assertIsNotNone(art1)
        self.assertEqual(art1["slug"], "how-to-read-water-quality-report")

    def test_scenario_04_step_2_pfas_pitcher_investigation(self):
        """Scenario 4.2: User audits pitcher filter PFAS capabilities in Guide 09."""
        art9 = self.articles_by_id.get(9)
        self.assertIsNotNone(art9)
        self.assertEqual(art9["slug"], "filter-pitchers-pfas-removal")

    def test_scenario_04_step_3_mail_in_water_test_kit_selection(self):
        """Scenario 4.3: User selects EPA certified mail-in laboratory test kit in Guide 14."""
        art14 = self.articles_by_id.get(14)
        self.assertIsNotNone(art14)
        self.assertEqual(art14["slug"], "best-water-test-kits")

    def test_scenario_04_step_4_whole_house_filtration_evaluation(self):
        """Scenario 4.4: User evaluates whole house point-of-entry solutions in Guides 12 & 13."""
        art12 = self.articles_by_id.get(12)
        art13 = self.articles_by_id.get(13)
        self.assertIsNotNone(art12)
        self.assertIsNotNone(art13)
        self.assertEqual(art12["slug"], "springwell-cf1-review")
        self.assertEqual(art13["slug"], "best-whole-house-water-filters")


if __name__ == "__main__":
    unittest.main()
