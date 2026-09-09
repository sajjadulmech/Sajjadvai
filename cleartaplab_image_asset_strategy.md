# ClearTapLab Master Image Strategy & Media Asset Management

> **Document Type:** Media Asset Strategy, Sourcing Protocols, SEO Naming & Compression Blueprint  
> **Brand:** ClearTapLab (`ClearTapLab.com`)  
> **Core Policy:** Real Photography & Engineering Schematics Only — Zero AI-Generated Imagery  
> **Target Audience:** Content Creators, Site Editors, SEO Architects  

---

## 1. Executive Image Policy: The Authenticity Mandate

ClearTapLab builds trust through uncompromising scientific and visual authenticity. In an affiliate landscape cluttered with low-quality, AI-generated synthetic images of fake laboratories and fictitious lab technicians, ClearTapLab adheres to a strict standard:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   THE AUTHENTICITY GUARDRAIL                                     │
├─────────────────────────────────────────────┬────────────────────────────────────────────────────┤
│ ❌ PROHIBITED (Zero Tolerance)              │ ✅ APPROVED & ENCOURAGED                           │
├─────────────────────────────────────────────┼────────────────────────────────────────────────────┤
│ • AI-generated images (Midjourney, DALL-E)  │ • Official manufacturer product photos             │
│ • Fake "laboratory testing" stock photos    │ • Real under-sink & whole-house plumbing photos    │
│ • Synthetic human "experts" in lab coats    │ • Editorial stock photos (Unsplash, Pexels)        │
│ • Uncredited third-party blogger images     │ • Original 2D vector schematics & fluid diagrams   │
│ • Raw, uncompressed camera files (> 500 KB) │ • Public domain EPA, USGS, and NSF diagrams        │
└─────────────────────────────────────────────┴────────────────────────────────────────────────────┘
```

> [!IMPORTANT]
> **Placeholder Rule:** If a suitable real image of a specific product or plumbing setup is not immediately available, **do NOT generate an AI image**. Insert our standard **Editorial Placeholder Box** and schedule the asset for manual sourcing or direct photography.

---

## 2. Approved Image Sourcing Channels

### 2.1 Manufacturer Media Kits & Affiliate Asset Portals
For product teardowns, buyer's guides, and system comparisons:
* **Approved Brands:** SpringWell Water, Waterdrop, APEC Water Systems, Home Master, Clearly Filtered, Aquasana, Express Water, Pentair.
* **Where to Source:** Official brand affiliate portals (ShareASale, Impact, CJ Affiliate, Amazon Associates Media Creator) or manufacturer press/media resource kits.
* **Permitted Asset Types:** High-resolution product renders on pure white backgrounds, exploded cutaway diagrams, dimensions diagrams, and filter replacement photos.

### 2.2 Editorial Photography (Free Commercial Use)
For general water chemistry, tap water, home plumbing, well heads, and kitchen fixtures:
* **Primary Platforms:** **Unsplash** (`unsplash.com`), **Pexels** (`pexels.com`), and **Pixabay** (`pixabay.com`).
* **Search Terms to Use:** `kitchen sink faucet`, `glass of clean tap water`, `copper pipe plumbing`, `water pressure gauge`, `well water pump`, `limescale shower head`.
* **Selection Criteria:** Look for realistic, natural lighting and authentic residential settings. Avoid overly dramatic stock imagery.

### 2.3 Government & Public Domain Resources
For scientific charts, water cycles, aquifer diagrams, and water treatment science:
* **Sources:** **US Geological Survey (USGS)**, **Environmental Protection Agency (EPA)**, **Centers for Disease Control (CDC)**, and **Wikimedia Commons (Public Domain / CC-BY)**.

---

## 3. Image Sizing, Aspect Ratios & WebP Standards

To maintain **Google Core Web Vitals** performance (LCP < 1.2s, CLS = 0.00), all uploaded images must adhere to standard dimensions and compression targets:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               DIMENSION & COMPRESSION SPECIFICATIONS                             │
├──────────────────────┬───────────────┬──────────────┬────────────────┬───────────────────────────┤
│ Image Role           │ Max Width     │ Aspect Ratio │ Target Format  │ Max File Size Target      │
├──────────────────────┼───────────────┼──────────────┼────────────────┼───────────────────────────┤
│ Hero / Banner Image  │ 1200 px       │ 16 : 9       │ WebP           │ < 90 KB                   │
│ In-Article Feature   │ 800 px        │ 16 : 9 / 4:3 │ WebP           │ < 55 KB                   │
│ Product Card / Grid  │ 400 px        │ 1 : 1 (Sq)   │ WebP / PNG     │ < 30 KB                   │
│ Technical Diagram    │ 800 px        │ Flexible     │ WebP / SVG     │ < 45 KB                   │
│ Author Avatar Headshot│ 200 px       │ 1 : 1 (Sq)   │ WebP           │ < 20 KB                   │
└──────────────────────┴───────────────┴──────────────┴────────────────┴───────────────────────────┘
```

### 3.1 Compression Workflow:
1. **Resize:** Downscale original raw images to target dimensions using Squoosh (`squoosh.app`), TinyPNG, or Photoshop.
2. **Convert to WebP:** Convert at **80%–85% quality** (imperceptible visual difference, 40%–60% file size reduction vs JPG).
3. **Prevent Cumulative Layout Shift (CLS):** WordPress native Gutenberg blocks automatically insert explicit `width` and `height` attributes—never remove these attributes.

---

## 4. SEO File Naming Conventions

Search engines use image file names as a primary signal for image search rankings and topical relevance.

### 4.1 The Naming Formula:
```
[system-or-problem-type]-[brand-model-or-feature]-[specific-view-or-action].webp
```
* **Rules:** All lowercase, words separated strictly by hyphens (`-`), zero underscores (`_`), zero camera serial numbers (`IMG_48292.jpg`), zero generic names (`photo.jpg`).

---

## 5. Master Catalog of Pre-Defined Image File Names & Alt Text

Below is the definitive catalog of approved asset names for core pages, categories, and initial launch articles:

### 5.1 Site Branding & Core Pages

| Asset Role | SEO File Name | Optimized Alt Text |
| :--- | :--- | :--- |
| **Site Logo** | `cleartaplab-engineering-logo.svg` | ClearTapLab engineering water diagnostics logo |
| **Favicon** | `cleartaplab-favicon-icon.png` | ClearTapLab geometric water drop icon |
| **Founder Headshot** | `cleartaplab-founder-mechanical-engineer.webp` | ClearTapLab founder and mechanical engineer |
| **About Hero** | `residential-water-quality-engineering-analysis.webp` | Mechanical engineer reviewing residential water quality testing data |
| **Contact Hero** | `water-testing-sample-bottle-preparation.webp` | Clean water testing sample collection bottle for laboratory analysis |

---

### 5.2 Category Hub Banners

| Category | SEO File Name | Optimized Alt Text |
| :--- | :--- | :--- |
| **Water Problems** | `hard-water-limescale-and-rust-stains-plumbing.webp` | White limescale and orange rust stains on bathroom plumbing fixtures |
| **Water Testing** | `home-water-quality-test-kit-and-ccr-report.webp` | Certified EPA mail-in water test kit with municipal water quality report |
| **Reverse Osmosis** | `reverse-osmosis-under-sink-filter-system.webp` | Multi-stage under-sink reverse osmosis water filtration system installed |
| **Filtration Tech** | `activated-carbon-block-filter-cross-section.webp` | Exploded engineering cross-section of a 0.5 micron catalytic carbon block |
| **System Guides** | `whole-house-water-filtration-system-installation.webp` | Whole-house water filter and water softener installed on main copper water line |

---

### 5.3 Launch Articles (Initial 10 Articles)

| Article Target | SEO File Name | Optimized Alt Text |
| :--- | :--- | :--- |
| **01. City CCR Report** | `municipal-consumer-confidence-report-ccr-guide.webp` | Reading contaminant levels on an EPA municipal consumer confidence water report |
| **02. Well Water Testing** | `private-well-water-pressure-tank-and-testing.webp` | Private well water pressure tank with certified laboratory sample collection |
| **03. RO vs. Carbon** | `reverse-osmosis-membrane-vs-carbon-block-filter.webp` | Comparison of 0.0001 micron RO membrane pore size vs 0.5 micron carbon filter |
| **04. Hard Water GPG** | `hard-water-scale-buildup-copper-pipe-interior.webp` | Cross-section of copper water pipe clogged with calcium carbonate limescale |
| **05. Sulfur Rotten Egg** | `air-injection-oxidation-aio-sulfur-filter-tank.webp` | Air injection oxidation AIO filter tank installed to eliminate sulfur odor |
| **06. Iron Removal** | `ferrous-vs-ferric-iron-water-stains-sink.webp` | Orange rust staining in a porcelain sink caused by high dissolved iron in well water |
| **07. Softener vs. TAC** | `ion-exchange-water-softener-vs-tac-descaler.webp` | Traditional salt water softener brine tank alongside a salt-free TAC conditioner |
| **08. Best RO Systems** | `best-under-sink-reverse-osmosis-systems-comparison.webp` | Top rated under-sink reverse osmosis systems evaluated for flow rate and waste |
| **09. Waterdrop G3P800**| `waterdrop-g3p800-tankless-ro-under-sink-view.webp` | Waterdrop G3P800 tankless reverse osmosis system installed beneath kitchen sink |
| **10. PFAS Removal** | `pfas-forever-chemicals-water-filter-pitcher-test.webp` | Testing water filter pitcher for certified NSF 53 and P473 PFAS reduction |

---

## 6. The Alt Text Formulation Standard

Alt text serves two critical purposes: **screen reader accessibility** for visually impaired users and **context indexing** for search engines.

### 6.1 The 3-Part Alt Text Formula:
$$\text{Alt Text} = [\text{Specific Subject / Equipment}] + [\text{Key Physical Feature or Action}] + [\text{Context or Setting}]$$

* **Bad (Keyword Stuffing):** `alt="best water filter water filtration reverse osmosis buy cheap"`
* **Bad (Too Vague):** `alt="water filter"`
* **Good (ClearTapLab Standard):** `alt="Under-sink 5-stage reverse osmosis system with 0.0001 micron membrane installed with dedicated chrome faucet"`

---

## 7. The Reusable Editorial Placeholder Component

When drafting new articles where real photography is pending, editors must insert this clean, styled HTML placeholder. It maintains layout integrity and marks the asset clearly for future replacement:

```html
<!-- =========================================================================
     CLEARTAPLAB EDITORIAL ASSET PLACEHOLDER
     Use when a genuine product/installation image is pending sourcing.
     ========================================================================= -->
<div class="ctl-img-placeholder" style="background-color: #F1F5F9; border: 2px dashed #CBD5E1; border-radius: 14px; padding: 40px 20px; text-align: center; margin: 25px 0;">
  <div style="font-size: 2rem; margin-bottom: 8px;">📷</div>
  <div style="font-family: var(--ctl-font-head); font-weight: 700; color: #0B192C; font-size: 1rem; margin-bottom: 4px;">
    [EDITORIAL ASSET PENDING: Real Image Required]
  </div>
  <div style="font-size: 0.85rem; color: #64748B; font-family: var(--ctl-font-mono); margin-bottom: 8px;">
    Target Asset: waterdrop-g3p800-tankless-ro-under-sink-view.webp
  </div>
  <div style="font-size: 0.8rem; color: #94A3B8; max-width: 500px; margin: 0 auto;">
    Specification: High-resolution official manufacturer photo or real under-sink installation showing unit dimensions and power connection. <em>Do not replace with AI-generated visuals.</em>
  </div>
</div>
```

---

## 8. Phase 4 Quality Verification Checklist

Before publishing any media asset to the WordPress Media Library, verify these 5 criteria:

```
[ ] 1. Sourced strictly from approved real channels (Manufacturer kit, Unsplash, Pexels, or original diagram).
[ ] 2. Converted to WebP format at 80-85% quality.
[ ] 3. File size strictly under target threshold (< 90 KB for hero, < 55 KB for in-article).
[ ] 4. File name matches the SEO naming formula ([brand-system]-[model]-[view].webp).
[ ] 5. Explicit descriptive alt text added following the 3-part formula.
```
