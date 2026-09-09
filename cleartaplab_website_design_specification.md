# ClearTapLab Website Design & UI/UX Architectural Blueprint

**Document Type:** Full Website UI/UX Design Specification, Wireframes, Design Tokens & WordPress Implementation  
**Brand:** ClearTapLab (`ClearTapLab.com`)  
**Niche:** Residential Water Diagnostics, Filtration Engineering & System Benchmarks  
**Design Reference:** Modular Visual Hierarchy & Card Flow (Inspired by OutdoorGrillHub Pattern)  
**Date:** August 2026  

---

## Executive Design Summary

ClearTapLab's digital design translates complex residential water chemistry, fluid dynamics, and NSF/ANSI testing standards into an intuitive, high-converting, and visually stunning consumer experience. 

Inspired by the structured, card-based, multi-stage layout of modern authority portals, ClearTapLab adopts a **"Consumer Reports Lab Meets Dyson"** aesthetic: surgical lab cleanliness, crystalline aquatic hues, exploded component callouts, and frictionless problem-to-solution diagnostic routing.

```
+----------------------------------------------------------------------------------------------------+
|                                    CLEARTAPLAB DESIGN FOUNDATION                                   |
+------------------------------------+------------------------------------+--------------------------+
| Visual Language                    | Brand Tone                         | Core Conversion Engine   |
+------------------------------------+------------------------------------+--------------------------+
| Crisp Lab White (#FFFFFF)          | First-Principles Physics           | Interactive Diagnostic   |
| Deep Marine Navy (#0B192C)         | NSF/ANSI Scientific Rigor          | Problem -> Solution Map  |
| Pure Aqua Accent (#0284C7)         | Transparent TCO & Filter Math      | Lab Benchmark Reviews    |
| Soft 20px Rounded Elevation Cards  | No Snake-Oil / Zero Sales Fluff    | Sizing & Flow Calculators|
+------------------------------------+------------------------------------+--------------------------+
```

---

## 1. Brand Identity & Visual Positioning Verdict

```
+----------------------------------------------------------------------------------------------------+
|                                     BRAND ARCHETYPE EVALUATION                                     |
+---------------------+-------------------------------+----------------------------------------------+
| Archetype           | Strengths                     | Weaknesses & Pitfalls                        |
+---------------------+-------------------------------+----------------------------------------------+
| A) Wirecutter Style | High general consumer trust;  | Visually sterile; lacks specialized technical|
|    (Generic Review) | familiar editorial layout.    | depth; feels like an affiliate blog.         |
+---------------------+-------------------------------+----------------------------------------------+
| B) Science Journal  | Maximum academic credibility; | Too dense and intimidating for everyday      |
|    (e.g., Lab Pubs) | rigorous citation standards.  | homeowners; severely lowers buying intent.   |
+---------------------+-------------------------------+----------------------------------------------+
| C) Engineering OEM  | Sleek, premium, high-tech;    | Can appear biased or like a single product   |
|    (e.g., Dyson)    | visual schematics & diagrams. | manufacturer rather than an unbiased lab.    |
+---------------------+-------------------------------+----------------------------------------------+
```

### 🏆 The Strategic Sweet Spot: **"The Accessible Engineering Authority"**
* **The Editorial Rigor (Wirecutter):** Jargon-free recommendations, "Our Top Pick" badges, clear trade-offs, and transparent annual replacement cost calculations.
* **The Scientific Credibility (Science Magazine):** First-principles testing, spectrometer benchmark charts, micron cutoff scales, and certified NSF/ANSI standards audits.
* **The Visual Sophistication (Premium Engineering Brand):** Exploded component vectors, clean isometric schematics, fluid aquatic gradients, and soft-elevation modular cards.

---

## 2. Global Design System & CSS Tokens

### 2.1 Color Palette & Semantic Usage

```
+----------------------------------------------------------------------------------------------------+
|                                    COLOR TOKEN ARCHITECTURE                                        |
+----------------------+-----------+-------------------+---------------------------------------------+
| Token Name           | Hex Code  | HSL Equivalent    | Semantic Usage                              |
+----------------------+-----------+-------------------+---------------------------------------------+
| `--ctl-navy`         | `#0B192C` | `hsl(215, 60%, 11%)` | Primary Headings, Dark Cards, Footer Surface|
| `--ctl-navy-light`   | `#1E293B` | `hsl(215, 33%, 17%)` | Secondary Dark Cards, High-Contrast Borders |
| `--ctl-aqua`         | `#0284C7` | `hsl(201, 96%, 39%)` | Primary Action CTAs, Active Filter Pills    |
| `--ctl-aqua-hover`   | `#0369A1` | `hsl(201, 96%, 32%)` | CTA Hover State                             |
| `--ctl-aqua-light`   | `#E0F2FE` | `hsl(204, 94%, 94%)` | Category Pill Badges, Soft Highlights       |
| `--ctl-teal`         | `#0D9488` | `hsl(175, 84%, 32%)` | NSF Certified Indicators, Verified Badges   |
| `--ctl-teal-light`   | `#CCFBF1` | `hsl(167, 85%, 89%)` | Solution Success Badges                     |
| `--ctl-coral-alert`  | `#EA580C` | `hsl(21, 90%, 48%)`  | Contaminant Warnings (PFAS, Lead, Hardness) |
| `--ctl-coral-light`  | `#FFEDD5` | `hsl(34, 100%, 92%)` | Problem Badge Backgrounds                   |
| `--ctl-bg-ice`       | `#F8FAFC` | `hsl(210, 40%, 98%)` | Page Body, Alternating Section Backgrounds  |
| `--ctl-surface-white`| `#FFFFFF` | `hsl(0, 0%, 100%)`   | High-Elevation Feature Cards & Modals       |
| `--ctl-text-main`    | `#0F172A` | `hsl(222, 47%, 11%)` | Primary Reading Text                        |
| `--ctl-text-muted`   | `#475569` | `hsl(215, 19%, 35%)` | Secondary Subtitles, Spec Descriptions      |
+----------------------+-----------+-------------------+---------------------------------------------+
```

### 2.2 Typography System

* **Primary Headline Typeface:** `Plus Jakarta Sans` *(Google Fonts, Weights: 700, 800)*  
  * *Characteristics:* Crisp, geometric, authoritative, modern.
* **Body / Editorial Typeface:** `Inter` *(Google Fonts, Weights: 400, 500, 600)*  
  * *Characteristics:* Highly readable across long-form diagnostic guides and dense comparison tables.
* **Technical Spec & Data Typeface:** `JetBrains Mono` or `Space Mono` *(Weights: 600)*  
  * *Characteristics:* Used for micron ratings (`0.0001 μm`), flow metrics (`0.8 GPM`), and TDS readings (`18 PPM`).

### 2.3 Ready-to-Use CSS Design Tokens

```css
/* ==========================================================================
   ClearTapLab Global Design Tokens (WordPress / Custom CSS)
   ========================================================================== */

:root {
  /* Brand Colors */
  --ctl-navy: #0B192C;
  --ctl-navy-light: #1E293B;
  --ctl-aqua: #0284C7;
  --ctl-aqua-hover: #0369A1;
  --ctl-aqua-light: #E0F2FE;
  --ctl-teal: #0D9488;
  --ctl-teal-light: #CCFBF1;
  --ctl-coral: #EA580C;
  --ctl-coral-light: #FFEDD5;
  --ctl-bg-ice: #F8FAFC;
  --ctl-surface-white: #FFFFFF;
  --ctl-border-light: #E2E8F0;
  --ctl-text-main: #0F172A;
  --ctl-text-muted: #475569;

  /* Typography */
  --ctl-font-head: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
  --ctl-font-body: 'Inter', system-ui, -apple-system, sans-serif;
  --ctl-font-mono: 'JetBrains Mono', monospace;

  /* Geometry & Shadows */
  --ctl-radius-sm: 8px;
  --ctl-radius-md: 14px;
  --ctl-radius-card: 20px;
  --ctl-radius-pill: 9999px;
  --ctl-shadow-card: 0 10px 30px -5px rgba(11, 25, 44, 0.05), 0 4px 6px -2px rgba(11, 25, 44, 0.02);
  --ctl-shadow-hover: 0 20px 35px -5px rgba(2, 132, 199, 0.12);
  --ctl-transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
}

/* Base Body Setup */
body {
  font-family: var(--ctl-font-body);
  color: var(--ctl-text-main);
  background-color: var(--ctl-bg-ice);
  line-height: 1.6;
  -webkit-font-smoothing: antialiased;
}

/* Category & Section Pill Badges */
.ctl-badge-pill {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 16px;
  background-color: var(--ctl-aqua-light);
  color: var(--ctl-aqua);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-radius: var(--ctl-radius-pill);
  margin-bottom: 14px;
}

/* Section Title Group */
.ctl-section-header {
  text-align: center;
  max-width: 680px;
  margin: 0 auto 48px auto;
}

.ctl-section-header h2 {
  font-family: var(--ctl-font-head);
  font-size: clamp(28px, 4vw, 38px);
  font-weight: 800;
  color: var(--ctl-navy);
  letter-spacing: -0.02em;
  line-height: 1.2;
  margin-bottom: 12px;
}

.ctl-section-header p {
  font-size: 16px;
  color: var(--ctl-text-muted);
}

/* Modular Rounded Feature Card */
.ctl-feature-card {
  background: var(--ctl-surface-white);
  border-radius: var(--ctl-radius-card);
  padding: 32px 24px;
  box-shadow: var(--ctl-shadow-card);
  border: 1px solid var(--ctl-border-light);
  transition: var(--ctl-transition);
}

.ctl-feature-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--ctl-shadow-hover);
  border-color: rgba(2, 132, 199, 0.3);
}

/* Primary Pill Button */
.ctl-btn-primary {
  background-color: var(--ctl-aqua);
  color: #FFFFFF;
  padding: 14px 28px;
  font-weight: 700;
  font-size: 15px;
  border-radius: var(--ctl-radius-pill);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: var(--ctl-transition);
}

.ctl-btn-primary:hover {
  background-color: var(--ctl-aqua-hover);
  transform: translateY(-2px);
  box-shadow: 0 8px 20px -4px rgba(2, 132, 199, 0.4);
}

/* Outlined Pill Button */
.ctl-btn-outline {
  background-color: transparent;
  color: var(--ctl-navy);
  border: 1.5px solid var(--ctl-navy);
  padding: 12.5px 26px;
  font-weight: 700;
  font-size: 15px;
  border-radius: var(--ctl-radius-pill);
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: var(--ctl-transition);
}

.ctl-btn-outline:hover {
  background-color: var(--ctl-navy);
  color: #FFFFFF;
  transform: translateY(-2px);
}
```

---

## 3. Detailed Homepage Section Architecture

The homepage is organized into a seamless, high-engagement sequence inspired by the reference layout.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   CLEARTAPLAB HOMEPAGE FLOW                                      │
├────┬─────────────────────────────┬──────────────────────────────────────────────────────────────┤
│ #  │ Section                     │ Purpose & Functionality                                      │
├────┼─────────────────────────────┼──────────────────────────────────────────────────────────────┤
│ 01 │ Hero Section                │ Value proposition + Exploded Under-Sink RO interactive vector│
│ 02 │ Core Solution Hub           │ 6 Core Filtration Categories (2x3 Rounded Soft Grid)         │
│ 03 │ Interactive Problem Selector│ Filter Pills: Well, City, PFAS, Scale, Renters, Budget       │
│ 04 │ 4-Step Diagnostic Pipeline  │ Step-by-Step Roadmap from Water Test to Perfect Glass        │
│ 05 │ Common Problems & Fixes     │ 6 Troubleshooting Cards: Sulfur, Scale, Rust, Chlorine...    │
│ 06 │ Lab-Tested Benchmark Picks  │ 5-Column System Showcase with "View Lab Verdict" links       │
│ 07 │ Problem-to-Solution Matrix  │ Visual 2-Column Matching: [Contaminant Box] ➔ [Filter Tech] │
│ 08 │ Authority Pillar Tiles      │ 4 Deep-Colored Accent Cards (NSF Standards, TCO, Physics)    │
│ 09 │ Trust & Testing Methodology │ Lab Verification Bar with 4 Credibility Checkmarks           │
│ 10 │ High-Converting CTA Banner  │ Full-width Deep Ocean Gradient Card: Custom Diagnostic Plan  │
│ 11 │ Footer & Legal Disclosures  │ Comprehensive E-E-A-T disclaimers & full IA navigation       │
└────┴─────────────────────────────┴──────────────────────────────────────────────────────────────┘
```

---

### Section 01: Hero Header & Interactive System Diagram

```
+----------------------------------------------------------------------------------------------------+
| [ 🔬 RESIDENTIAL WATER FILTRATION LAB ]                                                            |
|                                                                                                    |
| Test Accurately. Choose Smarter. Drink Pure.                  [ Interactive System Diagram ]       |
|                                                                 +------------------------------+   |
| Independent water diagnostics, NSF-certified system            | [📍 5μ Sediment Barrier]     |   |
| testing, and engineering breakdowns to help you                 | [📍 Catalytic Carbon Block]  |   |
| eliminate contaminants without the sales pitch.                 | [📍 0.0001μm RO Membrane]    |   |
|                                                                 | [📍 Ca/Mg Remineralizer]     |   |
| [ Start Water Diagnostic ➔ ]   [ Browse Lab Reviews ]           +------------------------------+   |
+----------------------------------------------------------------------------------------------------+
```

* **Section Tagline Pill:** `🔬 RESIDENTIAL WATER FILTRATION LAB`
* **Main Headline:** **Test Accurately.** Choose Smarter. **Drink Pure.**
* **Lead Paragraph:** *"Independent water diagnostics, NSF-certified system testing, and engineering breakdowns to help you eliminate contaminants without the high-pressure sales pitch."*
* **CTAs:**
  * Primary: `[Start Water Diagnostic ➔] (Solid Aqua Pill)`
  * Secondary: `[Browse Lab Reviews] (Outlined Slate Pill)`
* **Right-Side Visual:** Isometric 3D rendering or exploded vector of an **Under-Sink Multi-Stage Reverse Osmosis System** with 4 interactive pointer pins that highlight real-time specs when clicked or hovered:
  * **Pin 1:** *5-Micron Sediment Barrier* — Captures rust, sand, and pipe silt.
  * **Pin 2:** *Catalytic Carbon Block* — Eradicates chlorine, chloramine, and PFAS.
  * **Pin 3:** *0.0001 μm Thin-Film Membrane* — Rejects 99.8% of TDS, arsenic, and heavy metals.
  * **Pin 4:** *Remineralization Post-Filter* — Restores calcium and magnesium for optimal pH (7.4–8.0).

---

### Section 02: "Everything You Need" Core Category Cards (2×3 Grid)

* **Section Tagline Pill:** `💧 COMPLETE WATER COVERAGE`
* **Section Title:** **Everything You Need For Pristine Home Water**
* **Section Subtitle:** *Engineered filtration guides categorized by water source, household size, and budget.*

```
+------------------------------------+------------------------------------+--------------------------+
| [🧪 Icon]                          | [🚰 Icon]                          | [🧼 Icon]                |
| Reverse Osmosis (RO)               | Whole-House Filtration             | Water Softeners & Scale  |
| Point-of-use under-sink & benchtop | POE systems delivering filtered    | Ion-exchange and TAC     |
| systems for pure drinking water.   | water to every home fixture.       | solutions for hard scale.|
+------------------------------------+------------------------------------+--------------------------+
| [🏡 Icon]                          | [☀️ Icon]                          | [🧫 Icon]                |
| Well Water Treatment               | UV Disinfection Purifiers          | Home Water Test Kits     |
| Iron, sulfur, manganese, and air-  | Chemical-free 254nm ultraviolet    | EPA-certified mail-in lab|
| injection oxidation guides.        | sterilization for bacteria/cysts.  | kits and instant strips. |
+------------------------------------+------------------------------------+--------------------------+
```

---

### Section 03: Interactive Quick-Filter Pills

* **Section Tagline Pill:** `🔍 TARGETED SOLUTIONS`
* **Section Title:** **A Better System Starts With Your Exact Water Type**
* **Section Subtitle:** *Select your specific water profile to filter our lab tests and recommendations:*

```
[ All Guides ]  [ Well Water ]  [ City Tap Water ]  [ PFAS & Lead ]  [ Hard Water Scale ]  [ Renters & Apartments ]  [ Under $300 ]
```

---

### Section 04: The 4-Step Water Purity Diagnostic Roadmap

A horizontal milestone timeline displaying a step-by-step path to clean water:

```
( 01 ) ──────────────────> ( 02 ) ──────────────────> ( 03 ) ──────────────────> ( 04 )
Test Your Water           Identify Contaminants     Match Filter Tech         Install & Validate
City CCR lookup or        Pinpoint exact PPM of     Select RO, Catalytic      Step-by-step DIY guide
mail-in EPA lab kit       hardness, PFAS, or lead   Carbon, or Ion-Exchange   and TDS/flow verification
```

---

### Section 05: Common Water Problems & Engineering Fixes (Troubleshooting 6-Grid)

* **Section Tagline Pill:** `🛠️ WATER QUALITY TROUBLESHOOTING`
* **Section Title:** **Common Tap Water Problems & How To Solve Them**

```
+------------------------------------+------------------------------------+--------------------------+
| [⚠️ Icon: Coral]                   | [⚠️ Icon: Coral]                   | [⚠️ Icon: Coral]         |
| Rotten Egg (Sulfur) Smell          | White Chalky Limescale             | Rust & Orange Staining   |
| Cause: Hydrogen sulfide gas.       | Cause: Dissolved Ca/Mg carbonate.  | Cause: Ferrous iron.     |
| Fix: Air-injection oxidation.      | Fix: Salt-based or TAC softener.   | Fix: Greensand / KDF-85. |
+------------------------------------+------------------------------------+--------------------------+
| [⚠️ Icon: Coral]                   | [⚠️ Icon: Coral]                   | [⚠️ Icon: Coral]         |
| Bleach / Pool Chemical Taste       | Low Flow Pressure Across Home      | Boil Water Alert / E.Coli|
| Cause: Chlorine & chloramine.      | Cause: Clogged 5μ pre-filters.     | Cause: Microbial path.   |
| Fix: Catalytic carbon block.       | Fix: High-flow backwashing rig.    | Fix: 254nm UV Chamber.   |
+------------------------------------+------------------------------------+--------------------------+
```

---

### Section 06: Lab-Tested Top Benchmarks (5-Column Gear Showcase)

* **Section Tagline Pill:** `⭐ LAB BENCHMARK PICKS`
* **Section Title:** **Top-Tested Water Treatment Systems of 2026**

```
+----------------+----------------+----------------+----------------+----------------+
| [RO System]    | [Whole House]  | [Softener]     | [Test Kit]     | [Pitcher]      |
| Waterdrop G3   | SpringWell CF1 | Kind Water     | Tap Score Lab  | Clearly Filter |
| 800 GPD / Tank | 1,000,000 Gal  | Salt-Free TAC  | 109 Parameters | Removes PFAS   |
| [View Verdict] | [View Verdict] | [View Verdict] | [View Verdict] | [View Verdict] |
+----------------+----------------+----------------+----------------+----------------+
```

---

### Section 07: Problem-to-Solution Matching Matrix

Replicating the side-by-side comparison box from the reference layout:

```
+----------------------------------------------+-----+---------------------------------------------+
| Water Contaminant / Symptom                  | ➔   | Verified Filtration Solution                |
+----------------------------------------------+-----+---------------------------------------------+
| [🚨 High PFAS "Forever Chemicals"]           | ➔   | [✅ 0.0001 μm RO or Catalytic Carbon GAC]    |
| [🚨 Limescale on Dishwashers & Kettles]      | ➔   | [✅ Ion-Exchange Salt Softener or TAC]      |
| [🚨 Black / Orange Well Water Staining]      | ➔   | [✅ Air-Injection Iron & Manganese Filter]  |
| [🚨 Lead Leaching from Old Copper Pipes]     | ➔   | [✅ NSF 53 Certified Solid Carbon Block]    |
| [🚨 Coliform or Microbial Well Risk]         | ➔   | [✅ 30 mJ/cm² Ultraviolet (UV) Chamber]     |
| [🚨 Dry, Itchy Skin & Damaged Hair]          | ➔   | [✅ KDF-55 Whole-House Dechlorinator]       |
+----------------------------------------------+-----+---------------------------------------------+
```

---

### Section 08: The 4 Authority Pillar Cards (Deep Accent Tiles)

* **Section Tagline Pill:** `🛡️ ENGINEERING PRINCIPLES`
* **Section Title:** **Water Filtration Grounded in Physics, Not Sales Hype**

```
+--------------------------+--------------------------+--------------------------+--------------------------+
| [ NAVY BLUE TILE ]       | [ AQUATIC CYAN TILE ]    | [ BIO-TEAL TILE ]        | [ WARM AMBER TILE ]      |
| NSF/ANSI Standard Rigor  | First-Principles Physics | Lifetime Ownership Math  | Zero Sponsored Verdicts  |
| Audited against NSF 42,  | Verified GPM flow rates, | Transparent calculation  | 100% independent lab     |
| 53, 58, 401 & 372 specs. | PSI drops & drain ratios.| of annual filter costs.  | benchmarking & reviews.  |
+--------------------------+--------------------------+--------------------------+--------------------------+
```

---

### Section 09: Testing Methodology & Trust Bar

* **Background:** Soft Ice Slate (`#F1F5F9`)
* **Section Title:** **Rigorous Diagnostics For Real Homeowners.**
* **4 Checkmark Value Props:**
  * ✅ *Spectrometer & Digital TDS Meter Benchmarking*
  * ✅ *Real-World GPM Flow Rate & Pressure Drop Validation*
  * ✅ *Standardized NSF/ANSI Certification Audit*
  * ✅ *Step-by-Step DIY Installation & Pipe Sizing Math*

---

### Section 10: High-Converting Hero Footer CTA

* **Card Design:** Full-width rounded card with a deep ocean gradient (`#0B192C` to `#0284C7`).
* **Headline:** **Get Clear on What’s in Your Tap Water.**
* **Subtitle:** *Take our 60-second diagnostic quiz to get a customized, engineering-backed water filtration plan.*
* **Buttons:**
  * `[Find Your Filter System (Quiz)] (Solid White Pill)`
  * `[Read Water Test Kit Guide] (Transparent White Outlined Pill)`

---

## 4. Header & Navigation Architecture

```
+----------------------------------------------------------------------------------------------------+
| [💧 ClearTapLab]   Water Diagnostics ▾  System Types ▾  Lab Reviews  Test Kits  Plumbing DIY       |
|                                                                           [ Diagnostic Quiz ➔ ]    |
+----------------------------------------------------------------------------------------------------+
```

### 4.1 Primary Header Links
1. **Water Diagnostics (Dropdown Mega-Menu):**
   * *Well Water Quality Guide* (Iron, Sulfur, Coliform)
   * *City Tap Water & CCR Lookup* (Chloramine, Fluoride)
   * *Hard Water & Scale Removal* (Grains Per Gallon Math)
   * *PFAS, Lead & Microplastics Guide*
2. **System Types (Dropdown Mega-Menu):**
   * *Reverse Osmosis Systems* (Under-Sink & Countertop)
   * *Whole House Filtration* (POE Carbon & Sediment)
   * *Water Softeners & Descalers* (Salt-based vs. TAC)
   * *UV Disinfection Units* (Well water sterilization)
   * *Filter Pitchers & Faucet Attachments*
3. **Lab Reviews (Direct Link):** Comprehensive tear-downs, flow tests, and annual cost comparisons.
4. **Water Test Kits (Direct Link):** EPA mail-in laboratory kits vs. instant colorimetric test strips.
5. **Plumbing DIY (Direct Link):** Pipe sizing charts, bypass valve setup, and filter change schedules.
6. **Header CTA Button:** `[Diagnostic Quiz ➔]` (Solid Aqua Pill).

---

## 5. WordPress Theme Implementation & Technical Stack

To maintain **95+ Google PageSpeed Core Web Vitals (LCP < 1.2s, INP < 50ms)**, the entire website must be built using native WordPress Block Architecture without bloated page builders.

```
+----------------------------------------------------------------------------------------------------+
|                                    WORDPRESS TECHNOLOGY STACK                                      |
+----------------------+------------------------------------------+----------------------------------+
| Layer                | Tool / Plugin                            | Purpose                          |
+----------------------+------------------------------------------+----------------------------------+
| Core Theme           | Kadence Theme (or GeneratePress)         | Ultra-clean DOM, zero jQuery     |
| Block System         | Kadence Blocks (or Spectra / Gutenberg)  | Fast, responsive modular layouts |
| Custom Post Types    | ACF Pro (Advanced Custom Fields)         | Structured review & spec data    |
| Dynamic Templating   | Kadence Elements (Theme Hook Builder)    | Reusable review templates & CTAs |
| Table Engine         | TablePress Pro or Ninja Tables           | Responsive comparison tables     |
| SEO & Schema         | Rank Math SEO Pro                        | Review, Product & FAQ Schema     |
| Caching & Speed      | WP Rocket + Cloudflare APO               | Sub-second page load times       |
+----------------------+------------------------------------------+----------------------------------+
```

### 5.1 ACF Custom Post Type Schema: `water_review`

```php
/**
 * Register Custom Post Type: Water System Reviews
 */
function ctl_register_review_cpt() {
    $labels = array(
        'name'          => 'System Reviews',
        'singular_name' => 'System Review',
        'menu_name'     => 'Lab Reviews',
        'add_new_item'  => 'Add New Water System Review',
    );
    $args = array(
        'labels'        => $labels,
        'public'        => true,
        'has_archive'   => true,
        'rewrite'       => array('slug' => 'reviews'),
        'supports'      => array('title', 'editor', 'thumbnail', 'excerpt'),
        'menu_icon'     => 'dashicons-filter',
        'show_in_rest'  => true,
    );
    register_post_type('water_review', $args);
}
add_action('init', 'ctl_register_review_cpt');
```

#### Custom Field Definitions (ACF Pro)
* `field_micron_rating`: Text (e.g., `0.0001 μm` or `5.0 μm`)
* `field_flow_rate_gpm`: Number / Text (e.g., `0.8 GPM` / `15.0 GPM`)
* `field_nsf_certifications`: Checkbox (`NSF 42`, `NSF 53`, `NSF 58`, `NSF 401`, `NSF 372`)
* `field_annual_filter_cost`: Number (e.g., `$85`)
* `field_waste_water_ratio`: Text (e.g., `1:1 Pure to Drain` or `Zero Waste`)
* `field_hardness_capacity`: Text (e.g., `48,000 Grains`)
* `field_affiliate_buy_link`: URL (Cloaked outbound redirection link)

---

## 6. High-Converting Affiliate Conversion Modules

### 6.1 The "Lab Verdict" Review Box (Kadence Element Pattern)

```
+----------------------------------------------------------------------------------------------------+
| 🔬 CLEARTAPLAB VERDICT: Waterdrop G3P800 Reverse Osmosis System                                   |
+----------------------------------------------------------------------------------------------------+
| Rating: ★★★★★ (9.4 / 10) | Category: Best Tankless Under-Sink RO | Price: $799                      |
|                                                                                                    |
| SPECIFICATIONS AT A GLANCE:                                                                        |
| • Micron Rating: 0.0001 μm          • NSF Certifications: NSF 58, NSF 372 (Lead-Free)             |
| • Pure-to-Drain Ratio: 3:1 (Eco)    • Annual Filter Cost: $85 / year                               |
| • Measured Flow Rate: 0.82 GPM      • TDS Reduction: 94.8% Measured in Lab                         |
|                                                                                                    |
| PROS                                              CONS                                             |
| [+] Tankless design saves 70% under-sink space   [-] Requires an active 110V power outlet          |
| [+] Smart faucet displays real-time output TDS   [-] Remineralizer cartridge must be bought extra  |
| [+] Fast 3-second twist-and-pull filter change                                                     |
|                                                                                                    |
| [ Check Price on Waterdrop Direct ]    [ Check Price on Amazon ]                                   |
+----------------------------------------------------------------------------------------------------+
```

---

## 7. Execution & Launch Checklist

1. **Theme Installation:** Install Kadence Theme Pro + Kadence Blocks Pro.
2. **Global CSS Setup:** Drop the custom CSS tokens into `wp-admin > Appearance > Additional CSS`.
3. **Typography Configuration:** Set `Plus Jakarta Sans` for H1–H4, `Inter` for body copy, and `JetBrains Mono` for data badges.
4. **Homepage Block Assembly:** Build the 10 homepage sections using native container/row blocks matching the exact padding (`clamp(48px, 6vw, 96px)`) and 20px card border radii.
5. **ACF Configuration:** Import the custom fields for `System Reviews` and setup the Kadence Elements single template for reviews.
6. **Diagnostic Quiz Setup:** Implement an interactive 4-question quiz using Fluent Forms or Gravity Forms routing users to their tailored filter category.
