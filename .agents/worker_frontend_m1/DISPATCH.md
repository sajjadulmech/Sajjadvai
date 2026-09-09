## 2026-08-17T11:10:07Z
You are the Frontend UI & Styling Worker for the ClearTapLab Guides & Articles overhaul.

Workspace Directory: d:/Personal/AntiGravity/Affiliate Marketting
Agent Directory: d:/Personal/AntiGravity/Affiliate Marketting/.agents/worker_frontend_m1
Original Request: d:/Personal/AntiGravity/Affiliate Marketting/ORIGINAL_REQUEST.md
Frontend Survey Report: d:/Personal/AntiGravity/Affiliate Marketting/.agents/teamwork_preview_explorer_survey_2/survey_frontend_report.md
Project Spec: d:/Personal/AntiGravity/Affiliate Marketting/PROJECT.md

MANDATORY FIRST STEP: Read ORIGINAL_REQUEST.md and the Frontend Survey Report.

MANDATORY INTEGRITY WARNING:
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

EXCLUSIVE FILE OWNERSHIP:
You own and may edit:
- `styles/main.css`
- `scripts/app.js`
- `index.html` (only for Hub card counts alignment in Section 2)

YOUR MISSION:
1. Update `styles/main.css`:
   - Add scoped typography rules for `.ctl-modal-body` (`h1`-`h4`, `p`, `ul`, `ol`, `li`, `blockquote`, `hr`) to ensure long-form engineering articles render with readable spacing despite the universal CSS reset.
   - Add `.ctl-mono`, `.ctl-formula-box`, `.ctl-code-block` styling.
   - Ensure `.ctl-table` inside `.ctl-table-wrapper` has `min-width: 580px` to prevent squishing on mobile.
   - Add FAQ accordion styles (`.ctl-faq-section`, `.ctl-faq-item`, `.ctl-faq-question`, `.ctl-faq-answer`).
   - Add mobile stacking media query for `.ctl-author-box` (`@media (max-width: 640px)`).
2. Update `scripts/app.js`:
   - In `openArticleModal(articleId)`: Ensure `modalContainer.scrollTop = 0` is executed on every modal open so users always start at the top of the article.
   - In `performSearch(query)`: Update search filter logic to query article `tags` array in addition to `title`, `excerpt`, and `categoryLabel`.
3. In `index.html`:
   - Update Section 2 Hub card labels to reflect exact guide distribution (Water Testing: 2 Guides, Water Problems: 3 Guides, Whole-House: 6 Guides, RO: 5 Guides, Filtration Science: 4 Guides).
4. Verify your changes do not break existing styles, calculator, or triage tool.
5. Write handoff.md in your agent directory and send a completion message to parent.
