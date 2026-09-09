# Original User Request

## 2026-08-17T11:05:21Z

Audit and complete the entire Guides and Articles section of the ClearTapLab website, replacing all stub and summary content with comprehensive, first-principles engineering articles across all 20 guides.

Working directory: d:/Personal/AntiGravity/Affiliate Marketting
Integrity mode: development

## Requirements

### R1. Complete Website & Content Audit
- Audit all 20 guide cards and articles across the ClearTapLab platform (index.html, scripts/articles-data.js, and batch markdown files).
- Identify any truncated articles, placeholder text, missing tables, missing mathematical formulas, or broken cross-links.

### R2. Author & Integrate Production Engineering Articles (Guides 01–20)
- Populate every guide in scripts/articles-data.js with full-length, production-grade HTML content matching the caliber of the cornerstone Markdown files (cleartaplab_batch1_cornerstone_articles.md, cleartaplab_batch2_cornerstone_articles.md, cleartaplab_batch3_cornerstone_articles.md, cleartaplab_batch4_cornerstone_articles.md).
- Each guide must include:
  - Header badge and clear H1 title
  - Problem overview and first-principles scientific explanation
  - Technical comparison table (.ctl-table-wrapper)
  - Engineering specification callout box (.ctl-spec-box)
  - Practical testing and troubleshooting methodology
  - Lifetime Total Cost of Ownership (TCO) or sizing formulas where applicable
  - 3–4 comprehensive FAQ items with technical answers
  - Editorial author byline and related internal guide links

### R3. Interactive Web Application Verification
- Ensure the interactive modal reader (#article-modal) in index.html renders full-length rich content seamlessly for every single card (Guides 01 through 20).
- Verify that filtering by category (reverse-osmosis, water-testing, water-problems, filtration-technology, system-guides) and live search displays all 20 complete articles without truncation or layout shifts.
- Maintain existing styling tokens, colors, responsive geometry, and accessibility standards.

### R4. Final Audit & Verification Report
- Provide a full validation report verifying that all 20 articles contain complete long-form content with zero placeholder stubs remaining.

## Acceptance Criteria

### Content Completeness
- [ ] All 20 guides in scripts/articles-data.js contain full HTML bodies (comprising introductory science, deep-dive mechanisms, spec callouts, tables, and FAQs).
- [ ] No guide card in index.html or modal reader opens to a single-paragraph summary or placeholder stub.
- [ ] Technical accuracy verified against NSF/ANSI standards (42, 53, 58, 401, P473) and EPA water quality guidelines.

### UI & Interaction Quality
- [ ] Modal reader renders smoothly with formatted typography, tables, and spec boxes for every article ID (1–20).
- [ ] Live search queries correctly index and open full articles.
- [ ] Category tabs filter to the correct subset of complete guides.
