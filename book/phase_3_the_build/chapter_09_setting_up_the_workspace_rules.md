# Chapter 09: Setting Up the Workspace: Rules and Progressive Disclosure

If you open an AI coding tool and type:

> *"Build me an affiliate marketing website for water filters."*

you will get a disaster.

The AI will enthusiastically generate a sprawling, fragile project:
* It will install React, Next.js, and 450 megabytes of `node_modules`.
* It will pull in external CSS frameworks (Bootstrap or Tailwind via CDN) that slow down mobile load times.
* It will write generic placeholder articles with fabricated reviews.
* It will forget FTC disclosures, leave off `rel="sponsored"` tags, and create broken mobile layouts.

Why does this happen? Because LLMs are non-deterministic pattern generators. Unless you give the model **strict boundaries and architectural rules**, it defaults to whatever modern web boilerplate it was trained on.

In this chapter, you will learn how to configure **Google Antigravity** so it behaves not like an erratic chatbot, but like a disciplined, senior software engineer working under your direct supervision.

You will see how to use **Workspace Rules** (`.agents/rules/AGENTS.md`) and **Planning Mode** to keep your technical asset clean, fast, and compliant.

---

## How Google Antigravity Thinks

Unlike traditional autocomplete extensions or basic chat interfaces, Google Antigravity operates as an **autonomous agentic assistant**. 

When Antigravity runs inside your project, it follows a structured lifecycle:

```
[ USER REQUEST ]
       │
       ▼
[ STEP 1: READ WORKSPACE RULES (.agents/rules/AGENTS.md) ]
  - Loads project constraints, coding standards, and compliance rules.
       │
       ▼
[ STEP 2: INSPECT FILE SYSTEM & DISCOVER SKILLS ]
  - Reads existing files, checks dependencies, scans repository state.
       │
       ▼
[ STEP 3: ENTER PLANNING MODE (If task requires structural changes) ]
  - Creates implementation_plan.md.
  - Outlines exact files to create, modify, or delete.
  - STOPS AND WAITS FOR YOUR HUMAN APPROVAL.
       │
       ▼ (You review and click "Approve" or type "proceed")
[ STEP 4: AUTONOMOUS EXECUTION ]
  - Writes code, edits files, executes terminal verification tests.
       │
       ▼
[ STEP 5: VERIFICATION & WALKTHROUGH ]
  - Runs automated test runner (tests/run_e2e_tests.py).
  - Reports completed results in walkthrough.md.
```

Notice the most critical step in that sequence: **Step 3 (Planning Mode)**. 

Antigravity does not blindly edit your production code behind your back. For any major structural task, it creates an `implementation_plan.md` artifact, lays out the architectural changes, and **waits for your explicit approval**. You remain the project director at all times.

---

## The Secret Weapon: `.agents/rules/AGENTS.md`

To ensure Antigravity never violates your architectural standards, you place an instructions file in your repository:

```
[YOUR PROJECT ROOT]
└── .agents/
    └── rules/
        └── AGENTS.md
```

Whenever Antigravity starts an interaction, it reads `AGENTS.md` first. Any rule defined in this file takes precedence over generic training data.

Here is the exact `AGENTS.md` configuration we created for **ClearTapLab**:

```markdown
# ClearTapLab: Project Engineering & Compliance Rules

## 1. Technical Stack Constraints
- PURE STATIC ARCHITECTURE: Use only semantic HTML5, modern CSS3, and Vanilla JavaScript (ES6+).
- ZERO EXTERNAL DEPENDENCIES: No npm packages, no node_modules, no frontend frameworks (React/Vue), and no external CSS/JS CDNs. All styles and scripts must be self-contained in local files.
- PERFORMANCE TARGET: 100/100 Core Web Vitals. Sub-second LCP, zero CLS, and sub-50ms INP on mobile.

## 2. Affiliate Compliance & Legal Standards (FTC 16 CFR Part 255)
- OUTBOUND LINK SECURITY: Every outbound affiliate link MUST include:
  target="_blank" rel="sponsored nofollow noopener"
- MANDATORY DISCLOSURE: Every page containing commercial recommendations must feature the standard ClearTapLab above-the-fold disclosure box before the first affiliate link.
- NO PRICING FABRICATION: Never hard-code static prices that violate merchant operating agreements. Use "Check Current Price" or dynamic pricing indicators.

## 3. UI/UX Design System
- CSS CUSTOM PROPERTIES: All colors, typography scales, and spacing must use variables defined in `styles/main.css`.
- MOBILE TOUCH TARGETS: All buttons, navigation links, and interactive calculator controls must maintain a minimum touch target of 44x44 pixels.
- RESPONSIVE TABLES: All comparison tables must be wrapped in `.ctl-table-wrapper` with horizontal scrolling (`overflow-x: auto`) to prevent mobile layout breaking.

## 4. Editorial Integrity (Strict Non-Fabrication)
- Never claim personal laboratory testing or unboxing.
- Base all technical evaluations on certified third-party standards (NSF/ANSI, WQA, EPA) and verified manufacturer engineering specifications.

## 5. Verification Before Completion
- Never report a technical task as complete without executing `python tests/run_e2e_tests.py` and verifying 100% test passes.
```

---

## Why These Rules Transform the Output

Look at what happens when you establish these rules before writing a single line of code:

| Without Rules | With `AGENTS.md` Rules |
| :--- | :--- |
| AI imports external Google Fonts that add 300ms of DNS lookup lag. | AI uses clean system font stacks (`-apple-system, BlinkMacSystemFont, "Segoe UI"`) that load in 0ms. |
| AI creates basic links (`<a href="...">`) that violate FTC and Google search guidelines. | AI automatically adds `target="_blank" rel="sponsored nofollow noopener"` to every commercial link. |
| AI writes complex build steps requiring Node.js. | AI outputs clean, zero-dependency HTML files ready for instant deployment to Cloudflare Pages. |
| AI claims *"In our lab tests, we ran 500 gallons..."* (a legal liability). | AI writes *"According to NSF 58 test data, the 0.0001-micron membrane reduces lead by 99.3%..."* (accurate, truthful, compliant). |

---

## How to Set Up Your Own Project in 5 Minutes

Here is the exact terminal procedure to scaffold your new workspace:

```bash
# 1. Create your project directory
mkdir my-affiliate-site
cd my-affiliate-site

# 2. Create the rules directory
mkdir -p .agents/rules

# 3. Create your project folders
mkdir styles scripts images data tests
```

Then, copy the `AGENTS.md` template above into `.agents/rules/AGENTS.md`.

Once that file exists, you can direct Antigravity with high-level business instructions, confident that every file it creates will adhere to your technical and legal standards.

---

## What I Would Do Right Now

* **Never skip the rules file.** Spending 10 minutes writing an `AGENTS.md` file saves you 15 hours of correcting formatting mistakes and fixing non-compliant links later.
* **Keep your stack pure static.** Resist the urge to add "just one little framework." The simplicity of plain HTML, CSS, and JavaScript is your greatest operational superpower as a solo creator.
* **Use Planning Mode for everything.** When you ask Antigravity to build or modify a feature, always review its proposed plan in `implementation_plan.md` before giving the green light.

In the next chapter, we are going to direct Antigravity to build the entire **ClearTapLab** website foundation in an afternoon.
