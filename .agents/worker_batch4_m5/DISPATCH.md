## 2026-08-17T11:10:07Z
You are the Batch 4 Articles Specialist for the ClearTapLab Guides & Articles overhaul.

Workspace Directory: d:/Personal/AntiGravity/Affiliate Marketting
Agent Directory: d:/Personal/AntiGravity/Affiliate Marketting/.agents/worker_batch4_m5
Original Request: d:/Personal/AntiGravity/Affiliate Marketting/ORIGINAL_REQUEST.md
Batch 4 Source Markdown: d:/Personal/AntiGravity/Affiliate Marketting/cleartaplab_batch4_cornerstone_articles.md
Articles Survey Report: d:/Personal/AntiGravity/Affiliate Marketting/.agents/teamwork_preview_explorer_survey_1/survey_articles_report.md
Standards Survey Report: d:/Personal/AntiGravity/Affiliate Marketting/.agents/teamwork_preview_explorer_survey_3/survey_standards_and_testing_report.md
Project Spec: d:/Personal/AntiGravity/Affiliate Marketting/PROJECT.md

MANDATORY FIRST STEP: Read ORIGINAL_REQUEST.md and the source markdown file `cleartaplab_batch4_cornerstone_articles.md`.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

EXCLUSIVE FILE OWNERSHIP:
You own and will create:
- `scripts/batch4_articles.js`

YOUR MISSION:
Author complete, production-grade, long-form JavaScript object definitions with full HTML content for **Guides 16 through 20**:
- Guide 16: `how-to-size-water-softener` (System Guides)
- Guide 17: `best-salt-free-water-conditioners` (System Guides)
- Guide 18: `sediment-vs-carbon-filters` (Filtration Science)
- Guide 19: `fluoride-removal-water` (Filtration Science)
- Guide 20: `whole-house-filter-water-pressure` (System Guides)

STRUCTURAL REQUIREMENTS FOR EACH GUIDE:
1. Badge: `<div class="ctl-badge-pill [badgeClass]" style="margin-bottom: 15px;">[Badge Name]</div>`
2. Title: `<h1 style="font-family: var(--ctl-font-heading); font-size: 2rem; color: var(--ctl-navy); margin-bottom: 16px; line-height: 1.25;">[Title]</h1>`
3. Problem overview & first-principles scientific explanation.
4. Technical comparison table wrapped in `<div class="ctl-table-wrapper"><table class="ctl-table">...</table></div>`.
5. Engineering spec box `<div class="ctl-spec-box [info|warning]">...</div>` or `<div class="ctl-card"><div class="ctl-spec-grid">...</div></div>`.
6. Practical testing, troubleshooting, or sizing methodologies.
7. Formulas / chemical reactions formatted cleanly with `<sub>`, `<sup>`, `.ctl-mono`, or `.ctl-formula-box`. (Ensure Guide 20 includes the Ergun Equation for porous media!).
8. Exactly 3 to 4 comprehensive FAQ items with thorough technical answers.
9. Author / Editorial Byline `<div class="ctl-author-box">...</div>`.
10. SPA internal cross-links formatted as `<a href="javascript:void(0)" onclick="openArticleModal(ID)">Title</a>`.
11. Add a rich `tags: [...]` array of relevant technical keywords.

Output the array as:
`window.CLEAR_TAP_ARTICLES_BATCH4 = [ ... 5 guide objects ... ];` in `scripts/batch4_articles.js`.

Write handoff.md in your agent directory and notify parent when done.
