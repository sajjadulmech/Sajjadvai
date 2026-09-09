## 2026-08-17T11:14:18Z
You are the Master Dataset Integration Worker for the ClearTapLab Guides & Articles overhaul.

Workspace Directory: d:/Personal/AntiGravity/Affiliate Marketting
Agent Directory: d:/Personal/AntiGravity/Affiliate Marketting/.agents/worker_integration
Original Request: d:/Personal/AntiGravity/Affiliate Marketting/ORIGINAL_REQUEST.md
Batch 1 File: d:/Personal/AntiGravity/Affiliate Marketting/scripts/batch1_articles.js
Batch 2 File: d:/Personal/AntiGravity/Affiliate Marketting/scripts/batch2_articles.js
Batch 3 File: d:/Personal/AntiGravity/Affiliate Marketting/scripts/batch3_articles.js
Batch 4 File: d:/Personal/AntiGravity/Affiliate Marketting/scripts/batch4_articles.js
Target Master File: d:/Personal/AntiGravity/Affiliate Marketting/scripts/articles-data.js
Test Runner: d:/Personal/AntiGravity/Affiliate Marketting/tests/run_e2e_tests.py

MANDATORY FIRST STEP: Read ORIGINAL_REQUEST.md.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

EXCLUSIVE FILE OWNERSHIP:
You own:
- `scripts/articles-data.js`

YOUR MISSION:
1. Merge and assemble all 20 guides from:
   - `scripts/batch1_articles.js` (Guides 01–05)
   - `scripts/batch2_articles.js` (Guides 06–10)
   - `scripts/batch3_articles.js` (Guides 11–15)
   - `scripts/batch4_articles.js` (Guides 16–20)
   into the master dataset file `scripts/articles-data.js`.
2. Ensure `scripts/articles-data.js` defines:
   ```javascript
   // ClearTapLab Guides & Articles - Master Production Dataset (Guides 01-20)
   const CLEAR_TAP_ARTICLES = [
     // ... all 20 guide objects in exact ID order 1..20 ...
   ];
   ```
   Ensure clean ES6+ JavaScript syntax, no dangling syntax errors, valid backtick template strings for `contentHtml`, and complete preservation of all rich HTML content, tags, formulas, tables, spec boxes, FAQs, bylines, and SPA cross-links.
3. Run the automated E2E test suite:
   `python tests/run_e2e_tests.py --verbose`
   Verify that all 277 test cases pass with exit code `0`.
4. If any tests fail, inspect the failure output and resolve the issue in `scripts/articles-data.js`.
5. Write a detailed handoff.md in `.agents/worker_integration/handoff.md` documenting test results and verification metrics, and notify parent when done.
