## 2026-08-17T11:10:07Z
You are the E2E Test Suite Architect for the ClearTapLab Guides & Articles overhaul.

Workspace Directory: d:/Personal/AntiGravity/Affiliate Marketting
Agent Directory: d:/Personal/AntiGravity/Affiliate Marketting/.agents/test_writer_1
Original Request: d:/Personal/AntiGravity/Affiliate Marketting/ORIGINAL_REQUEST.md
Test Infra Plan: d:/Personal/AntiGravity/Affiliate Marketting/TEST_INFRA.md
Explorer 3 Report: d:/Personal/AntiGravity/Affiliate Marketting/.agents/teamwork_preview_explorer_survey_3/survey_standards_and_testing_report.md
Baseline Test: d:/Personal/AntiGravity/Affiliate Marketting/.agents/teamwork_preview_explorer_survey_3/test_clear_tap_lab.py

MANDATORY FIRST STEP: Read ORIGINAL_REQUEST.md, TEST_INFRA.md, and the Explorer 3 Survey Report.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

YOUR MISSION:
1. Create the complete, robust automated E2E test suite in the `tests/` directory:
   - `tests/run_e2e_tests.py`: CLI test runner executing all test tiers and reporting summary metrics.
   - `tests/test_tier1_features.py`: Tests all 20 guides for:
     * Valid metadata (`id`, `slug`, `title`, `category`, `readTime`, `badgeClass`, `excerpt`, `tags`)
     * Header badge and H1 title
     * Scientific explanation with first-principles mechanisms
     * Engineering spec box (`.ctl-spec-box`)
     * Technical comparison table (`.ctl-table-wrapper` and `.ctl-table`)
     * Practical testing / troubleshooting protocol / sizing formulas
     * 3-4 FAQ items with comprehensive technical answers
     * Editorial byline (`.ctl-author-box`)
     * SPA cross-links (`openArticleModal`)
     * Minimum word count (>= 1,000 words per article) and non-empty content.
   - `tests/test_tier2_boundaries.py`: Tests edge cases:
     * Search with empty query, special regex chars, whitespace, case-insensitivity
     * Category filtering with invalid/empty categories
     * Modal reader open/close state transitions, scroll reset logic
     * Table responsiveness (`min-width: 580px`) and long text wrapping
   - `tests/test_tier3_cross_feature.py`: Tests pairwise feature interactions:
     * Search + category filtering combination
     * In-modal cross-link clicks opening target article
     * Hub card button click navigating to filtered tab
   - `tests/test_tier4_user_scenarios.py`: Tests full user journeys:
     * Reverse osmosis comparison and sizing
     * Well water sulfur smell and iron diagnosis
     * Hard water GPG/PPM calculation and softener sizing
     * Water test kit lab comparison (ICP-MS)
2. Execute the test runner `python tests/run_e2e_tests.py` using run_command to verify it runs smoothly against the current workspace.
3. Once created and verified, generate `TEST_READY.md` at project root summarizing test runner invocation, tier breakdown, and test case counts.
4. Output handoff.md in your agent directory and send a completion message to parent.
