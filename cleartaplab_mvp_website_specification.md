# ClearTapLab MVP Website Specification & Build Blueprint

**Document Type:** Complete MVP Technical & Design Specification  
**Brand:** ClearTapLab (`ClearTapLab.com`)  
**Positioning:** Engineering-Based Home Water Quality Education & Diagnostics Platform  
**Target Architecture:** WordPress Core + Free Kadence Theme + Native Gutenberg (Kadence Blocks Free)  
**Date:** August 2026  

---

## Executive Overview

This document serves as the complete, step-by-step master specification for building the **ClearTapLab MVP Website**. It is designed for a solo mechanical engineer with 10 hours/week, prioritizing:
1. **Zero Coding Complexity:** 100% built with standard WordPress blocks and native customizer settings.
2. **Maximum Speed & SEO:** Scores 98–100 on Google PageSpeed (zero jQuery, no page builders).
3. **Genuine E-E-A-T Authority:** Real engineering analysis and NSF/ANSI standard auditing without fake lab claims.
4. **Frictionless Conversion:** Clean problem-to-solution pathways built directly into standard blog posts and category hubs.

---

## 1. Complete Homepage Wireframe (ASCII Layout)

The homepage consists of **6 lean, high-trust sections** designed to orient the visitor, establish engineering credibility, and route them to specific solutions.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ HEADER                                                                                           │
│ [💧 ClearTapLab]        Water Diagnostics    System Guides    Water Testing    About   [Get Started]│
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ SECTION 1: HERO                                                                                  │
│                                                                                                  │
│   [ 🔬 ENGINEERING-GRADE WATER QUALITY & FILTRATION ]                                            │
│   Understand Your Water.                                                                         │
│   Choose the Right Solution.                                                                     │
│                                                                                                  │
│   Clear water diagnostics, NSF/ANSI standard audits, and first-principles filtration             │
│   engineering to help homeowners solve tap and well water issues without sales pressure.         │
│                                                                                                  │
│   [ 💧 Explore Water Diagnostics ]      [ ⚙️ Browse System Guides ]                              │
│                                                                                                  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ SECTION 2: 4 CORE SYSTEM HUBS (2x2 Grid)                                                         │
│                                                                                                  │
│   [ 🔬 Reverse Osmosis (RO) ]              [ 🏡 Whole-House Filtration ]                         │
│   Under-sink and countertop systems for    Point-of-entry sediment and carbon                    │
│   zero-TDS drinking water.                 systems protecting every tap.                         │
│                                                                                                  │
│   [ 🧼 Water Softeners & Scale ]           [ 🌲 Well Water Treatment ]                           │
│   Ion-exchange vs. salt-free descalers     Iron, manganese, sulfur, and air-                     │
│   for hard water minerals.                 injection filtration solutions.                       │
│                                                                                                  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ SECTION 3: COMMON WATER PROBLEMS (Troubleshooting Hub)                                           │
│   "Identify Your Water Symptom"                                                                  │
│                                                                                                  │
│   [ ⚠️ Rotten Egg Smell ] ➔ Hydrogen Sulfide Guide & Aeration Systems                            │
│   [ ⚠️ White Limescale ] ➔ Hard Water Testing & Descaler Sizing                                  │
│   [ ⚠️ Orange/Rust Stains ] ➔ Ferrous vs. Ferric Iron Removal Solutions                          │
│   [ ⚠️ Chlorine/Bleach Taste ] ➔ Catalytic Carbon & Chloramine Block Filtration                  │
│                                                                                                  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ SECTION 4: THE 3-STEP WATER PURITY FRAMEWORK                                                     │
│                                                                                                  │
│   [ 01: Test Your Tap ] ───────> [ 02: Match Technology ] ───────> [ 03: Calculate Lifetime TCO ]│
│   Never buy a filter blind.      Match contaminants to correct    Factor in filter replacement   │
│   Start with CCR or test kit.    physics (RO, carbon, ion-ex).    costs, flow rate, and waste.   │
│                                                                                                  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ SECTION 5: FEATURED TECHNICAL GUIDES (Latest 4 Posts Grid)                                       │
│                                                                                                  │
│   [ Post Card 1 ]             [ Post Card 2 ]             [ Post Card 3 ]                        │
│   How to Read Your City CCR   RO vs. Carbon Filters       Waterdrop G3P800 Teardown              │
│   Diagnostic Guide            Technical Comparison        Engineering Review                     │
│                                                                                                  │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ SECTION 6: ABOUT THE ENGINEER & EDITORIAL TRANSPARENCY                                           │
│                                                                                                  │
│   [ Headshot Image ]   "Hi, I'm [Name], a Mechanical Engineer."                                  │
│                        Why I founded ClearTapLab: to cut through the marketing fluff of the      │
│                        $12B water treatment industry with real physics and independent audits.   │
│                                                                                                  │
│                        • Independent Analysis  • NSF/ANSI Standard Audits  • Transparent Disclosures│
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ FOOTER                                                                                           │
│ ClearTapLab Bio | Core Categories | Important Guides | Legal & Affiliate Disclosures             │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Header & Navigation Structure

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ [💧 ClearTapLab]   Water Diagnostics ▾   System Guides ▾   Water Testing   About   [Get Started] │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Logo & Branding
* **Site Title:** `ClearTapLab`
* **Favicon / Icon:** A minimalist stylized geometric water drop paired with a clean filter grid icon.
* **Tagline (in metadata):** *Engineering-Grade Home Water Diagnostics*

### 2.2 Navigation Menu Items (Desktop & Mobile)
1. **Water Diagnostics (Dropdown):**
   * *Well Water Quality Guide* (`/diagnostics/well-water/`)
   * *City Water & CCR Lookup Guide* (`/diagnostics/city-water/`)
   * *Hard Water & Scale Diagnostics* (`/diagnostics/hard-water/`)
   * *PFAS & Lead Elimination Guide* (`/diagnostics/pfas-lead/`)
2. **System Guides (Dropdown):**
   * *Reverse Osmosis Systems* (`/systems/reverse-osmosis/`)
   * *Whole-House Filtration* (`/systems/whole-house/`)
   * *Water Softeners & Descalers* (`/systems/water-softeners/`)
   * *Water Filter Pitchers & Faucets* (`/systems/pitchers-faucets/`)
3. **Water Testing (Direct Link):**
   * `/water-testing/` *(Mail-In EPA Lab Kits vs. Home Test Strips)*
4. **About the Engineer (Direct Link):**
   * `/about/` *(Author background, mechanical engineering credentials, testing methodology)*
5. **Header CTA Button:**
   * Text: `Find Your System` or `Get Started`
   * Target: Smooth-scroll to Section 2 (Core Categories) or to `/diagnostics/`.

---

## 3. Footer Structure & E-E-A-T Architecture

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ COLUMN 1 (Brand & Mission) │ COLUMN 2 (System Guides)  │ COLUMN 3 (Diagnostics) │ COLUMN 4 (Legal)│
│ ClearTapLab                │ • Reverse Osmosis         │ • City Water CCRs      │ • About Author  │
│ Independent engineering    │ • Whole-House Systems     │ • Well Water Stains    │ • Editorial Pol.│
│ diagnostics & water purity │ • Water Softeners         │ • Hard Water Scale     │ • Affiliate Disc│
│ guides for homeowners.     │ • Water Test Kits         │ • PFAS & Lead Guides   │ • Privacy Policy│
├────────────────────────────┴───────────────────────────┴────────────────────────┴─────────────────┤
│ MANDATORY AFFILIATE & MEDICAL DISCLAIMER:                                                        │
│ ClearTapLab provides technical research, engineering assessments, and educational content. We do │
│ not provide medical advice. We participate in affiliate programs and may earn commissions on     │
│ qualifying purchases at no extra cost to you. All product evaluations are 100% independent.     │
│ © 2026 ClearTapLab. All rights reserved.                                                         │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Required Core Pages (Day 1 Launch)

```
+----------------------+--------------------+----------------------------------------------------------+
| Page Name            | URL Slug           | Core Purpose & Key Content                               |
+----------------------+--------------------+----------------------------------------------------------+
| Homepage             | `/`                | 6-Section Hub, Value Proposition, Navigation             |
| About & Methodology  | `/about/`          | Author Bio, Mechanical Engineering Background, Audits    |
| Editorial Policy     | `/editorial/`      | How we research, NSF/ANSI auditing standards, no sponsors|
| Contact Us           | `/contact/`        | Simple contact form for reader questions and corrections |
| Affiliate Disclosure | `/disclosure/`     | Full FTC-compliant affiliate disclosure                  |
| Privacy Policy       | `/privacy-policy/` | Standard GDPR / CCPA compliant legal policy              |
| Terms of Service     | `/terms/`          | Standard website terms and conditions                    |
+----------------------+--------------------+----------------------------------------------------------+
```

---

## 5. Category Architecture & URL Taxonomy

Keep the URL structure clean, flat, and scalable.

```
ClearTapLab URL Hierarchy
├── /diagnostics/                     [Category Hub: Water Quality & Problem Solving]
│   ├── /how-to-read-city-water-report/
│   ├── /fix-rotten-egg-sulfur-smell/
│   └── /how-to-remove-iron-well-water/
├── /systems/                         [Category Hub: Filtration Hardware & Teardowns]
│   ├── /best-reverse-osmosis-systems/
│   ├── /waterdrop-g3p800-review/
│   ├── /water-softener-vs-descaler/
│   └── /best-whole-house-water-filters/
└── /water-testing/                   [Category Hub: Lab Kits, Meters & DIY Tests]
    ├── /best-mail-in-water-test-kits/
    └── /tds-meters-explained/
```

### WordPress Permalinks Setting:
* Select: **Post name** (`https://cleartaplab.com/%postname%/`)
* *Why:* Cleanest for SEO, easiest to reorganize categories later without breaking 301 redirects.

---

## 6. Homepage Copywriting (Exact Copy for Kadence Blocks)

### Section 1: Hero
* **Pill Badge:** `🔬 ENGINEERING-GRADE WATER QUALITY GUIDES`
* **Main Headline:** **Understand Your Water. Choose the Right Solution.**
* **Subtitle:** *Independent water diagnostics, NSF/ANSI standard audits, and first-principles filtration engineering to help homeowners solve tap and well water issues without high-pressure sales pitches.*
* **Primary Button:** `[ 💧 Explore Water Diagnostics ]` ➔ Links to `#diagnostics` or `/diagnostics/`
* **Secondary Button:** `[ ⚙️ Browse System Guides ]` ➔ Links to `#systems` or `/systems/`

---

### Section 2: Core Water System Hubs (2×2 Grid)
* **Section Tagline:** `SYSTEM CATEGORIES`
* **Section Headline:** **Engineered Filtration for Every Water Source**
* **Section Subtitle:** *Select a system category to explore technical breakdowns, sizing formulas, and independent assessments.*

* **Card 1: Reverse Osmosis (RO)**
  * *Subtitle:* Point-of-use under-sink and countertop systems delivering ultra-pure drinking water with 95%+ TDS reduction.
  * *Action Link:* `Explore RO Guides ➔` (`/systems/reverse-osmosis/`)
* **Card 2: Whole-House Filtration**
  * *Subtitle:* Point-of-entry carbon block and multi-stage sediment systems engineered to protect your entire home plumbing.
  * *Action Link:* `Explore Whole-House Systems ➔` (`/systems/whole-house/`)
* **Card 3: Water Softeners & Descalers**
  * *Subtitle:* Ion-exchange and template-assisted crystallization (TAC) systems compared for hard water scale control.
  * *Action Link:* `Explore Softener Guides ➔` (`/systems/water-softeners/`)
* **Card 4: Well Water Treatment**
  * *Subtitle:* Air-injection oxidation, greensand, and sediment filtration guides for iron, manganese, and hydrogen sulfide.
  * *Action Link:* `Explore Well Water Guides ➔` (`/diagnostics/well-water/`)

---

### Section 3: Common Water Symptoms (Troubleshooting Hub)
* **Section Tagline:** `DIAGNOSTIC HUB`
* **Section Headline:** **Identify Your Water Symptom**
* **Section Subtitle:** *Match the physical warning signs in your home to the correct treatment technology:*

* **Symptom 1: Rotten Egg / Sulfur Odor**
  * *Cause:* Dissolved hydrogen sulfide gas or sulfur-reducing bacteria.
  * *Engineering Solution:* Air-injection oxidation or catalytic carbon.
  * *Link:* `Read the Sulfur Elimination Guide ➔`
* **Symptom 2: White Crust & Limescale**
  * *Cause:* High concentrations of dissolved calcium and magnesium carbonate.
  * *Engineering Solution:* Ion-exchange softening or salt-free TAC descaling.
  * *Link:* `Read the Hard Water & Scale Guide ➔`
* **Symptom 3: Orange, Red, or Rust Stains**
  * *Cause:* Dissolved ferrous (clear-water) or oxidized ferric (red-water) iron.
  * *Engineering Solution:* Air-injection greensand or dedicated iron filters.
  * *Link:* `Read the Iron Removal Guide ➔`
* **Symptom 4: Chemical Bleach / Chlorine Taste**
  * *Cause:* Municipal chlorine or chloramine disinfectant residuals.
  * *Engineering Solution:* High-capacity catalytic carbon block microfiltration.
  * *Link:* `Read the Chloramine Removal Guide ➔`

---

### Section 4: The 3-Step Water Purity Framework
* **Section Tagline:** `OUR METHODOLOGY`
* **Section Headline:** **Three Steps to Pure, Safe Water**
* **Section Subtitle:** *Don't buy a filtration system blind. Follow this engineering sequence:*

* **Step 01: Test Your Tap First**
  * *Description:* Review your municipal Consumer Confidence Report (CCR) or order an EPA-certified mail-in laboratory test before spending a dollar on hardware.
* **Step 02: Match the Technology to the Physics**
  * *Description:* Different contaminants require different physical separation methods. Use carbon for chlorine/PFAS, RO for dissolved minerals, and ion-exchange for scale.
* **Step 03: Calculate Lifetime Ownership Cost**
  * *Description:* Account for annual replacement filter costs, pure-to-drain water ratios, and flow rate drops (GPM) before committing to a system.

---

### Section 5: Featured Technical Guides
* **Section Tagline:** `LATEST RESEARCH`
* **Section Headline:** **Recent Technical Guides & System Teardowns**
* **Content:** Kadence Post Grid Block displaying the 4 latest articles with categories, estimated reading times, and publication dates.

---

### Section 6: About the Engineer & Editorial Transparency
* **Section Headline:** **Independent Analysis Grounded in Engineering**
* **Body Copy:**
  > *"Hi, I’m [Name], a Mechanical Engineer and the founder of ClearTapLab.*
  > 
  > *Most homeowners are caught between confusing water chemistry and aggressive door-to-door water treatment salesmen pushing overpriced, one-size-fits-all systems.*
  > 
  > *ClearTapLab was founded to bring clarity to home water treatment. We audit manufacturer specifications against international NSF/ANSI testing standards, calculate true fluid dynamics (flow rates and pressure drops), and provide transparent guidance so you only invest in what your water actually requires."*
* **3 Bullet Highlights:**
  * 🛡️ **100% Independent Evaluations:** No paid reviews or sponsored ratings.
  * 🔬 **NSF/ANSI Standard Audits:** We verify real certifications (NSF 42, 53, 58, 401).
  * 📊 **First-Principles Analysis:** Transparent total cost of ownership ($/gallon) calculations.

---

## 7. Design Component System (Kadence Blocks Standard)

Using only standard Kadence Blocks, configure these 5 reusable component patterns:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                REUSABLE COMPONENT PATTERNS                                       │
├────────────────────────────┬─────────────────────────────┬───────────────────────────────────────┤
│ Component                  │ Kadence Block Type          │ Styling Settings                      │
├────────────────────────────┼─────────────────────────────┼───────────────────────────────────────┤
│ 1. Section Pill Badge      │ Advanced Text Block         │ Background: #E0F2FE, Color: #0284C7,  │
│                            │                             │ Radius: 9999px, Font-size: 11px Bold  │
├────────────────────────────┼─────────────────────────────┼───────────────────────────────────────┤
│ 2. Feature / Category Card │ Section / Row Layout Block  │ Background: #FFFFFF, Border: #E2E8F0, │
│                            │                             │ Radius: 16px, Shadow: Subdued 04      │
├────────────────────────────┼─────────────────────────────┼───────────────────────────────────────┤
│ 3. Engineering Callout Box │ Info Box Block              │ Border-Left: 4px solid #0284C7,       │
│    ("Engineer's Note")     │                             │ Background: #F8FAFC, Radius: 8px      │
├────────────────────────────┼─────────────────────────────┼───────────────────────────────────────┤
│ 4. "Our Verdict" Box       │ Row Layout Block            │ Header: #0B192C, Body: #FFFFFF,       │
│    (Product Review Box)    │                             │ Radius: 16px, CTA: #0284C7 Pill Btn   │
├────────────────────────────┼─────────────────────────────┼───────────────────────────────────────┤
│ 5. Technical Spec Table    │ Native Table Block          │ Header Row: #0B192C with White Text,  │
│                            │                             │ Alternating Row Background: #F8FAFC   │
└────────────────────────────┴─────────────────────────────┴───────────────────────────────────────┘
```

### Component Example: The "Engineer's Assessment" Box (In-Article Callout)

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│ 🔬 ENGINEER'S TECHNICAL ASSESSMENT                                                               │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ While Brand X markets this filter as "tested to NSF standards," our audit shows it lacks         │
│ official NSF/ANSI 53 certification for lead removal. It is only certified under NSF 42 for       │
│ aesthetic chlorine taste. If your home has legacy copper pipes with lead solder, select an       │
│ independently certified solid block carbon or reverse osmosis unit instead.                     │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 8. Mobile Responsive Behavior & Breakpoints

Kadence automatically handles responsive scaling. Follow these exact settings:

* **Desktop (1024px+):**
  * 2×2 Grid for Core Categories.
  * 3 or 4-Column Grid for Featured Posts.
  * Horizontal 3-Step Framework timeline.
* **Tablet (768px – 1023px):**
  * 2-Column Grid for Categories and Posts.
  * Padding automatically scales from `64px` to `48px`.
* **Mobile (< 767px):**
  * Single Column (100% width) for all cards and categories.
  * 3-Step Framework stacks vertically with downward connecting arrows (`↓`).
  * Tables enable horizontal scrolling (`overflow-x: auto;`) with a visible *"Swipe to view specs"* prompt.
  * Touch target size: All buttons and links have a minimum height of **48px** for easy tapping.

---

## 9. Image & Illustration Recommendations

As a solo engineer, **never waste time making 3D renders or hiring expensive illustrators on Day 1**.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 IMAGE STRATEGY & GUIDELINES                                      │
├──────────────────────┬───────────────────────────────┬───────────────────────────────────────────┤
│ Image Type           │ Best Tool / Source            │ Rules & Guidelines                        │
├──────────────────────┼───────────────────────────────┼───────────────────────────────────────────┤
│ Author Headshot      │ Smartphone + Clean Background │ High-trust, professional, approachable    │
│ Technical Diagrams   │ Canva Free (Flowcharts)       │ Clean 2D flowcharts: Inlet ➔ Filter ➔ Tap │
│ Category Headers     │ Unsplash / Pexels (Free)      │ Modern clean plumbing, crystal-clear glass│
│ Product Images       │ Official Manufacturer Press   │ Clean white-background product shots      │
│ Spec Charts          │ Native HTML/CSS Tables        │ DO NOT use images for tables (bad for SEO)│
└──────────────────────┴───────────────────────────────┴───────────────────────────────────────────┘
```

---

## 10. Step-by-Step WordPress Build Steps (Weekend Setup)

Follow this chronological checklist to launch the MVP website in **under 4 hours**:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                WEEKEND BUILD CHECKLIST (4 HOURS)                                 │
├────┬──────────────────────────────────────┬──────────────────────────────────────────────────────┤
│ #  │ Action Step                          │ Estimated Time                                       │
├────┼──────────────────────────────────────┼──────────────────────────────────────────────────────┤
│ 01 │ Install WordPress on Hosting         │ 15 mins (1-click install via Hostinger/Cloudways)   │
│ 02 │ Install Kadence Theme & Kadence Blocks│ 10 mins (via wp-admin > Appearance > Themes)         │
│ 03 │ Configure Customizer Colors & Fonts  │ 20 mins (Navy #0B192C, Aqua #0284C7, Plus Jakarta)   │
│ 04 │ Set Permalinks to /%postname%/       │ 2 mins (wp-admin > Settings > Permalinks)            │
│ 05 │ Create Required Pages (About, Legal) │ 30 mins (Copy/paste text from Section 4)             │
│ 06 │ Build the 6-Section Homepage         │ 60 mins (Using native Kadence Section blocks)        │
│ 07 │ Setup Header Navigation & Footer     │ 25 mins (Menu builder + Customizer footer)           │
│ 08 │ Install Rank Math Free & UpdraftPlus │ 15 mins (Basic setup wizard + Google Drive backup)   │
│ 09 │ Connect Google Search Console        │ 15 mins (Verify domain & submit sitemap.xml)         │
│ 10 │ Publish Article #1                   │ 45 mins (Ready for live traffic!)                    │
└────┴──────────────────────────────────────┴──────────────────────────────────────────────────────┘
```

---

## Summary: Ready for Execution

With this specification:
* You have **zero custom code maintenance**.
* You have **zero paid plugin dependencies**.
* You have a **clean, high-authority brand aesthetic** that stands out from spammy affiliate review blogs.
* You can dedicate **100% of your 10 weekly hours** to writing and publishing the first 20 articles.
