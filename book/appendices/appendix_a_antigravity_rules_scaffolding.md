# Appendix A: Master Antigravity Project Scaffolding & Rules

This appendix provides the complete file tree and configuration templates to scaffold an Antigravity-powered affiliate platform from scratch.

---

## 1. Directory Tree Architecture

```
my-affiliate-platform/
├── .agents/
│   └── rules/
│       └── AGENTS.md            # Primary agent instruction set & constraints
├── _headers                     # Cloudflare Pages edge HTTP security headers
├── index.html                   # Core application shell, category filters, and reader
├── styles/
│   └── main.css                 # Zero-dependency design tokens & responsive components
├── scripts/
│   ├── app.js                   # Client-side UI controller & interactive calculator
│   └── articles-data.js         # Master structured content repository
├── images/                      # Optimized local WebP illustrations and diagrams
├── tests/
│   └── run_e2e_tests.py         # Automated Python quality & link verification test runner
└── sitemap.xml                  # Search engine XML index
```

---

## 2. Production `.agents/rules/AGENTS.md` Template

Copy and paste this into `.agents/rules/AGENTS.md`:

```markdown
# Autonomous Engineering & Legal Compliance Standards

## 1. Architectural Constraints
- PURE STATIC STACK: Semantic HTML5, native CSS3 variables, and Vanilla JavaScript (ES6+).
- ZERO EXTERNAL DEPENDENCIES: No npm build steps, no node_modules, no frontend frameworks (React, Vue), and no external CSS/JS CDNs. All assets must be stored locally.
- PERFORMANCE MANDATE: Target 100/100 Core Web Vitals. Sub-second LCP, zero CLS, and sub-50ms INP on mobile devices.

## 2. Affiliate Compliance & Link Hygiene (FTC 16 CFR Part 255)
- MANDATORY LINK TAGS: Every outbound affiliate hyperlink MUST include:
  target="_blank" rel="sponsored nofollow noopener"
- ABOVE-THE-FOLD DISCLOSURE: Every guide containing commercial recommendations must feature the standard `.ctl-disclosure` component before the first commercial link.
- NO PRICING FABRICATION: Never hard-code static prices that violate merchant terms. Use "Check Current Price" or dynamic indicators.

## 3. UI/UX & Responsive Design Rules
- CSS TOKENS: Colors, font scales, and spacing must use variables in `styles/main.css`.
- MOBILE TOUCH ERGONOMICS: All clickable elements (buttons, nav tabs, slider thumbs) must have a minimum touch target of 44x44px.
- TABLE WRAPPERS: All comparison tables must be contained in `.ctl-table-wrapper` with horizontal scroll (`overflow-x: auto`) to prevent mobile viewport clipping.

## 4. Editorial Integrity (Strict Non-Fabrication)
- Never claim personal unboxing, hands-on lab testing, or personal ownership.
- Base all technical teardowns on verified third-party certified standards (NSF/ANSI, WQA, EPA) and manufacturer engineering schematics.

## 5. Automated Verification Gate
- Always run `python tests/run_e2e_tests.py` before marking any coding or content task complete.
```
