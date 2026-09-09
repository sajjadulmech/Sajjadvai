# E2E Test Infra: ClearTapLab Guides & Articles Overhaul

## Test Philosophy
- Opaque-box, requirement-driven verification derived directly from `ORIGINAL_REQUEST.md`.
- Zero dependency on external network services: automated Python 3.14 test suite using `BeautifulSoup4`, `lxml`, and headless browser verification.
- Methodology: Category-Partition + Boundary Value Analysis + Pairwise Combinatorial + Real-World Workload Testing.

---

## Feature Inventory & Test Coverage

| # | Feature | Source (Requirement) | Tier 1 Tests | Tier 2 Tests | Tier 3 Tests | Tier 4 Tests |
|---|---------|---------------------|:------------:|:------------:|:------------:|:------------:|
| 1 | Guide 01 (CCR Water Quality Report) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 2 | Guide 02 (RO vs Carbon Filters) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 3 | Guide 03 (Sulfur Smell in Well Water) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 4 | Guide 04 (Waterdrop G3P800 Review) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 5 | Guide 05 (Hard Water GPG vs PPM) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 6 | Guide 06 (Iron Removal Well Water) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 7 | Guide 07 (Softener vs Salt-Free TAC) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 8 | Guide 08 (Best RO Systems 2026) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 9 | Guide 09 (PFAS Pitcher Filters) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 10 | Guide 10 (RO Water Waste & Ratios) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 11 | Guide 11 (Tankless vs Tank RO) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 12 | Guide 12 (SpringWell CF1 Review) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 13 | Guide 13 (Best Whole House Filters) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 14 | Guide 14 (Best Water Test Kits) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 15 | Guide 15 (Remineralization RO) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 16 | Guide 16 (How to Size Softener) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 17 | Guide 17 (Best Salt-Free Conditioners)| ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 18 | Guide 18 (Sediment vs Carbon Filters) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 19 | Guide 19 (Fluoride Removal Methods) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 20 | Guide 20 (Water Pressure & Ergun) | ORIGINAL_REQUEST §R1, §R2 | ≥5 | ≥5 | ✓ | ✓ |
| 21 | Modal Reader Interactive Lifecycle | ORIGINAL_REQUEST §R3 | ≥5 | ≥5 | ✓ | ✓ |
| 22 | Category Filtering Mechanism | ORIGINAL_REQUEST §R3 | ≥5 | ≥5 | ✓ | ✓ |
| 23 | Live Search Engine & Tag Indexing | ORIGINAL_REQUEST §R3 | ≥5 | ≥5 | ✓ | ✓ |

---

## Test Architecture

### Test Runner & Invocation
- Runner command: `python tests/run_e2e_tests.py`
- Pass/Fail Semantics:
  - Exit code `0` on 100% test pass
  - Non-zero exit code on any test failure
  - Detailed assertion failure reports with line numbers and expected vs actual values

### Directory Layout
```
tests/
├── run_e2e_tests.py             # Main test suite aggregator & CLI entry point
├── test_tier1_features.py       # Tier 1: Feature coverage (Structural, HTML, Spec, Table, FAQ completeness)
├── test_tier2_boundaries.py     # Tier 2: Boundary & corner cases (empty search, regex injection, mobile layout)
├── test_tier3_cross_feature.py  # Tier 3: Pairwise combinations (filter + search, modal navigation, byline)
└── test_tier4_user_scenarios.py # Tier 4: Realistic user journey workflows (RO research, hard water sizing)
```

---

## Coverage Thresholds

- **Tier 1 (Feature Coverage)**: ≥5 test cases per feature (23 features × 5 = ≥115 tests).
- **Tier 2 (Boundary & Corner Cases)**: ≥5 test cases per feature area (≥115 tests).
- **Tier 3 (Cross-Feature Combinations)**: ≥23 pairwise interaction tests.
- **Tier 4 (Real-World Application Scenarios)**: ≥12 comprehensive multi-step user scenarios.
- **Total Minimum Test Count Target**: ≥265 automated test cases.
