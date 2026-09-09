# ClearTapLab: 90-Day MVP Execution Playbook (Zero to Launch)

**Platform:** ClearTapLab (`ClearTapLab.com`)  
**Mission:** The Independent, Engineering-Backed Water Quality & Technology Hub  
**Founder Constraint:** Solo Founder, Mechanical Engineer, 10 hours/week, beginner in web building  
**Date:** August 2026  

---

## Executive Summary: The 90-Day Goal

By **Day 90**, ClearTapLab will be a live, lightning-fast, technically rigorous authority site featuring:
* **25 deeply researched, engineering-backed articles** covering Reverse Osmosis & Drinking Water.
* A complete **E-E-A-T trust infrastructure** (Methodology page, Author bio, Testing protocol).
* Full **Google Search Console & GA4 indexing** with zero technical debt.
* **3 approved high-intent affiliate merchant accounts** (Tap Score, Waterdrop, Amazon backup).
* A baseline of organic keyword impressions growing consistently in Google Search Console.

```
THE 90-DAY LAUNCH PHASES
┌───────────────────────┬───────────────────────┬───────────────────────┐
│ WEEKS 1–3: SETUP      │ WEEKS 4–8: SEEDING    │ WEEKS 9–12: AUTHORITY │
│ • Fast Host & Theme   │ • 12 Core RO Articles │ • 13 Problem Guides   │
│ • E-E-A-T Pages       │ • Internal Linking    │ • Seed Affiliate Apps │
│ • GSC / Analytics     │ • Technical Diagrams  │ • GSC Performance Rev │
└───────────────────────┴───────────────────────┴───────────────────────┘
```

---

## 1. Technology Stack: Lightweight, Fast & Beginner-Proof

Avoid complex website builders (Elementor, Divi) that bloat code and destroy Google Core Web Vitals (LCP/INP). Use a clean, ultra-fast block-based WordPress setup.

```
+---------------------------------------------------------------------------------------------------+
| Recommended Technology Stack                                                                      |
+---------------------+-------------------------------+---------------------------------------------+
| Component           | Recommended Tool              | Cost / Notes                                |
+---------------------+-------------------------------+---------------------------------------------+
| **Domain**          | Namecheap or Cloudflare Reg.  | ~$10 – $14 / year (`ClearTapLab.com`)       |
| **Hosting**         | Hostinger Cloud or Cloudways  | ~$10 – $14 / mo (High speed, built-in SSL)  |
| **CMS**             | WordPress.org (Self-hosted)   | Free / Open Source                          |
| **Theme**           | GeneratePress Premium / Kadence| ~$59 / year (Cleanest code, 100% Core Web   |
|                     |                               | Vitals score out of the box)                |
| **Page Building**   | GenerateBlocks / Kadence Blk  | Free (Uses native WordPress Gutenberg)      |
+---------------------+-------------------------------+---------------------------------------------+
```

### The 7 Essential Plugins (Keep Total Plugins Under 10)
1. **Rank Math SEO (Free):** Handles on-page SEO, XML sitemaps, breadcrumbs, and Schema markup.
2. **LiteSpeed Cache / WP Rocket:** Caching, CSS minification, and instant page loading.
3. **TablePress / Kadence Tables:** For clean, responsive comparison tables and spec sheets.
4. **Pretty Links / ThirstyAffiliates (Free):** Cloaks and tracks outbound affiliate links (e.g., `cleartaplab.com/recommends/waterdrop-g3`).
5. **Instant Indexing (Rank Math + IndexNow):** Automatically notifies Google & Bing of newly published posts.
6. **Fluent Forms (Free):** Lightweight contact form for inquiries and feedback.
7. **Wordfence / Cloudflare Turnstile:** Security and spam prevention.

---

## 2. WordPress Site Structure & URL Taxonomy

Set your permalinks immediately before publishing any post:  
**Settings $\rightarrow$ Permalinks $\rightarrow$ Select `Post name` (`/%postname%/`)**.

```
CLEARTAPLAB ARCHITECTURE
├── /about/                  (Founder Bio: Mechanical Engineer, Testing philosophy)
├── /testing-methodology/    (TDS meters, pressure test gauges, NSF/EPA cross-referencing)
├── /ro-systems/             (Reverse Osmosis physics, tankless, countertop, remineralization)
├── /water-testing/          (TDS, mail-in lab tests, DIY strips, city CCR report reading)
├── /troubleshooting/        (Low water pressure, strange tastes, leaking air gaps, noise)
└── /reviews/                (Phase 2 Commercial Hub: Tested systems & shootouts)
```

---

## 3. Mandatory Trust (E-E-A-T) Pages: Build in Week 2

Google raters check these pages to verify you are a real expert and not an anonymous AI content farm:

### Page 1: `About Us & The Engineer Behind ClearTapLab` (`/about/`)
* **Photo:** Professional headshot of yourself.
* **Credentials:** State your mechanical/process engineering degree, background in fluid mechanics, and practical experience with valves, piping, and manufacturing tolerances.
* **The Mission:** *"ClearTapLab was founded to bring objective engineering rigor to residential water treatment—translating confusing water chemistry and fluid dynamics into actionable, unbiased advice for homeowners."*

### Page 2: `Our Testing & Research Methodology` (`/testing-methodology/`)
* Explain your benchmark tools: Calibrated digital TDS meters, inline pressure gauges, flow rate measurement cups, and official NSF/ANSI Standard (42, 53, 58) verification against public EPA and WQA databases.

### Page 3: Legal Disclosures (`/affiliate-disclosure/`, `/privacy-policy/`)
* Clear, prominent statement: *"ClearTapLab participates in select affiliate programs. If you purchase through our links, we may earn a commission at no additional cost to you. We only recommend systems that meet our engineering standards."*

---

## 4. The 10-Hour/Week Article Workflow (AI-Assisted, Human-Engineered)

As a solo founder working 10 hours a week, you will produce **2 high-quality articles every 10–12 days (~6–8 articles per month)**.

```
THE 10-HOUR PRODUCTION SYSTEM
┌─────────────────────────────────────────────────────────────────┐
│ 1. Keyword & Intent Blueprinting (1.0 hr)                       │
│    • Target 1 primary keyword + 3-4 long-tail questions (GSC/PPA│
├─────────────────────────────────────────────────────────────────┤
│ 2. Engineering Outline & Calculations (1.5 hrs)                 │
│    • Define the physics: PSI loss, GPM, micron size, drain ratio│
├─────────────────────────────────────────────────────────────────┤
│ 3. AI First-Draft Prompting (1.0 hr)                            │
│    • Prompt Claude / ChatGPT with strict engineering parameters │
├─────────────────────────────────────────────────────────────────┤
│ 4. Heavy Technical Editing & Fact-Checking (3.5 hrs)            │
│    • Remove generic AI fluff; inject real numbers, specs, & formulas│
├─────────────────────────────────────────────────────────────────┤
│ 5. Diagrams, Tables & Formatting (1.5 hrs)                      │
│    • Build custom comparison table, callout boxes, schematic    │
├─────────────────────────────────────────────────────────────────┤
│ 6. On-Page SEO, Linking & Publishing (1.5 hrs)                  │
│    • Meta title, URL slug, Schema FAQ, internal links (2 in, 2 out)│
└─────────────────────────────────────────────────────────────────┘
```

### The Exact AI Prompting Template for Engineering Articles

```markdown
Role: You are an expert mechanical engineer and residential water treatment specialist writing for ClearTapLab.com.
Topic: [Insert Topic, e.g., Tankless vs Tank Reverse Osmosis: Water Flow & Efficiency]
Audience: Homeowners who want clear, technically sound explanations without marketing jargon.

Strict Guidelines:
1. Do not use generic filler words ("In today's fast-paced world", "Look no further", "It is important to remember").
2. Explain the physical mechanics: line pressure (PSI), flow rates (GPM), wastewater drain ratios, and semi-permeable membrane physics.
3. Include a comparison table highlighting: Flow Rate, Footprint, Wastewater Ratio, Maintenance Cost, and Electrical Requirements.
4. Include a step-by-step diagnostic checklist for troubleshooting low pressure.
5. Reference NSF/ANSI Standard 58 testing criteria.
```

---

## 5. The First 25 Articles: The 90-Day Content Roadmap

```
+----------------------------------------------------------------------------------------------------+
| 90-Day Publishing Schedule (Target: 25 Articles)                                                   |
+---------+--------------------+-------------------------------------------+-------------------------+
| Weeks   | Category Focus     | Article Titles / Topics                   | Target Search Intent    |
+---------+--------------------+-------------------------------------------+-------------------------+
| **Wk 3**| Core RO Science    | 1. How Reverse Osmosis Works (Physics)    | Informational Pillar    |
|         |                    | 2. Tank vs Tankless RO Systems Compared   | Commercial Comparison   |
+---------+--------------------+-------------------------------------------+-------------------------+
| **Wk 4**| RO Efficiency      | 3. RO Drain Ratios ($1:1$ vs $4:1$ Math)  | Engineering Education   |
|         |                    | 4. Do You Need Remineralization Post-RO?  | Health & Chemistry      |
+---------+--------------------+-------------------------------------------+-------------------------+
| **Wk 5**| Operating Physics  | 5. How Temperature Changes RO Output (GPD)| Technical / E-E-A-T     |
|         |                    | 6. Feedwater Pressure: Why RO Needs 45 PSI| Plumbing Diagnostic     |
+---------+--------------------+-------------------------------------------+-------------------------+
| **Wk 6**| Under-Sink Config  | 7. Under-Sink vs Countertop RO Systems    | Buyer Guide             |
|         |                    | 8. Ultrafiltration (UF) vs Reverse Osmosis| Comparative Guide       |
+---------+--------------------+-------------------------------------------+-------------------------+
| **Wk 7**| Membrane Lifespan  | 9. How Long Do RO Membranes Really Last?  | Maintenance Guide       |
|         |                    | 10. NSF Standard 58 Decoded for Homeowners| Standards / Authority   |
+---------+--------------------+-------------------------------------------+-------------------------+
| **Wk 8**| Troubleshooting    | 11. Low Flow from RO Faucet (5 Step Fix)  | Problem-Solving Snippet |
|         |                    | 12. Connect RO System to Refrigerator Ice | DIY Plumbing Tutorial   |
+---------+--------------------+-------------------------------------------+-------------------------+
| **Wk 9**| Diagnostics        | 13. Why Water Runs Constantly Down Drain  | Problem-Solving Snippet |
|         |                    | 14. Install RO Without Drilling a Hole    | DIY Rental Friendly     |
+---------+--------------------+-------------------------------------------+-------------------------+
| **Wk 10**| Mechanics Fixes   | 15. Fix Gurgling Air Gap Faucet on RO     | Plumbing Diagnostic     |
|         |                    | 16. Auto Shut-Off Valve (ASOV) Failure Fix| Hardware Troubleshooting|
+---------+--------------------+-------------------------------------------+-------------------------+
| **Wk 11**| Testing & Quality | 17. Adjust Air Pressure in RO Holding Tank| Maintenance Tutorial    |
|         |                    | 18. Why Does Filtered RO Water Taste Sour?| Taste / Chemistry Fix   |
|         |                    | 19. How to Sanitize an Under-Sink RO Unit | Maintenance Checklist   |
+---------+--------------------+-------------------------------------------+-------------------------+
| **Wk 12**| Commercial Seeds  | 20. Do RO Booster Pumps Actually Save Water?| Engineering Hardware  |
|         |                    | 21. What a TDS Meter Measures (and Misses)| Water Testing Authority |
|         |                    | 22. Best Home Water Test Kits (Lab vs DIY)| High-Intent Affiliate   |
|         |                    | 23. Best RO Remineralization Filters 2026 | High-Intent Affiliate   |
|         |                    | 24. Waterdrop G3P800 vs APEC ROES-50 Shootout| Core Buyer Comparison|
|         |                    | 25. Best Countertop RO Systems for Renters| High-Intent Affiliate   |
+---------+--------------------+-------------------------------------------+-------------------------+
```

---

## 6. On-Page SEO Checklist (Apply to Every Single Article)

```
ON-PAGE SEO EXECUTION GATE
[ ] Target Keyword in H1 Title (preferably near the front)
[ ] Target Keyword in First 100 Words of Intro
[ ] Clean, Short URL Slug (e.g., `/tankless-vs-tank-ro/`, NOT `/2026/08/best-tankless-vs-tank/`)
[ ] H2 Subheadings include natural semantic variations (LSI keywords)
[ ] At least ONE custom HTML/Gutenberg comparison table
[ ] At least TWO internal links pointing to relevant sibling articles on your site
[ ] At least ONE outbound link to an authoritative source (EPA.gov, NSF.org, or CDC.gov)
[ ] Custom Meta Description (145–155 characters with clear click-benefit)
[ ] Schema FAQ markup added to Rank Math for 3 common questions
```

---

## 7. Monetization Setup: The 90-Day Execution Gate

Do **NOT** apply for affiliate programs on Day 1. If you apply with zero content, networks will reject your application.

```
THE AFFILIATE ROLLOUT GATEWAY
┌─────────────────────────────────────────────────────────────┐
│ WEEKS 1–9: PURE CONTENT CREATION                            │
│ • No affiliate links, no banner ads, no popups.             │
│ • Build organic indexing and clean site structure.          │
├─────────────────────────────────────────────────────────────┤
│ WEEKS 10–12: APPLY TO SEED AFFILIATE NETWORKS               │
│ • 1. ShareASale / Awin: Apply for SimpleLab (Tap Score)     │
│      (10% on $150–$300 certified mail-in lab tests)         │
│ • 2. Waterdrop Direct Affiliate Program (8%–12% on RO units)│
│ • 3. Amazon Associates (Backup for fittings, TDS meters)    │
├─────────────────────────────────────────────────────────────┤
│ DAY 90+: INSERT CLOAKED AFFILIATE LINKS                     │
│ • Use Pretty Links (`/recommends/product-name/`)            │
│ • Add rel="sponsored nofollow" tags automatically           │
└─────────────────────────────────────────────────────────────┘
```

---

## 8. Week-by-Week 90-Day Execution Checklist

```
+---------------------------------------------------------------------------------------------------+
| Week-by-Week Action Items                                                                         |
+----------+----------------------------------------------------------------------------------------+
| Week     | Specific Action Items (10 Hours per Week)                                              |
+----------+----------------------------------------------------------------------------------------+
| **Wk 1** | Register domain (`ClearTapLab.com`), set up hosting, install WordPress + GeneratePress.|
|          | Configure clean permalinks, SSL certificate, and install Rank Math SEO.                |
+----------+----------------------------------------------------------------------------------------+
| **Wk 2** | Design minimal logo (Canva), write `/about/` (Engineer Bio), `/testing-methodology/`,  |
|          | and Legal Disclosures. Set up Google Search Console & Google Analytics 4.              |
+----------+----------------------------------------------------------------------------------------+
| **Wk 3** | Write & publish Articles 1 & 2 (RO Physics & Tank vs Tankless). Submit sitemap to GSC. |
+----------+----------------------------------------------------------------------------------------+
| **Wk 4** | Write & publish Articles 3 & 4 (Drain Ratios & Remineralization).                      |
+----------+----------------------------------------------------------------------------------------+
| **Wk 5** | Write & publish Articles 5 & 6 (Temperature effects & Feedwater PSI requirements).    |
+----------+----------------------------------------------------------------------------------------+
| **Wk 6** | Write & publish Articles 7 & 8 (Under-sink vs Countertop & UF vs RO).                  |
+----------+----------------------------------------------------------------------------------------+
| **Wk 7** | Write & publish Articles 9 & 10 (Membrane lifespan & NSF Standard 58 decoded).        |
+----------+----------------------------------------------------------------------------------------+
| **Wk 8** | Write & publish Articles 11 & 12 (Low flow troubleshooting & Refrigerator ice kit).   |
+----------+----------------------------------------------------------------------------------------+
| **Wk 9** | Write & publish Articles 13 & 14 (Constant drain flow & No-drill rental install).      |
+----------+----------------------------------------------------------------------------------------+
| **Wk 10**| Write & publish Articles 15 & 16. Apply for **SimpleLab / Tap Score** affiliate account.|
+----------+----------------------------------------------------------------------------------------+
| **Wk 11**| Write & publish Articles 17, 18 & 19. Apply for **Waterdrop** affiliate program.       |
+----------+----------------------------------------------------------------------------------------+
| **Wk 12**| Write & publish Articles 20–25. Apply for **Amazon Associates**. Insert cloaked CTAs.  |
|          | Perform Month 3 GSC indexing and keyword impression audit.                             |
+----------+----------------------------------------------------------------------------------------+
```

---

## 90-Day MVP Success Metrics

On Day 90, log into Google Search Console and verify:
1. **Total Indexed Pages:** 25 content articles + 3 trust pages = **28 URLs indexed**.
2. **Total Impressions:** 500 – 3,000 monthly impressions starting to climb across long-tail queries.
3. **Core Web Vitals:** 95+ Mobile / 100 Desktop PageSpeed scores.
4. **Active Affiliate Accounts:** Tap Score and Waterdrop approved and integrated into your first 5 commercial guides.

You are now in full position to scale into **Month 4–12 (Topical Expansion & First Cashflow)**.
