# ClearTapLab Phase 3: Homepage Build & Assembly Manual (Refined)

> **Phase 3 Implementation Manual**  
> **Brand:** ClearTapLab (`ClearTapLab.com`)  
> **Target Scope:** 6-Section Gutenberg Homepage Assembly & SEO Metadata  
> **Target Architecture:** WordPress Core + Kadence Theme + Kadence Blocks (Free) + Rank Math SEO  
> **Target Audience:** Solo Founder / Non-Developer / Lead Content Architect  

---

## 1. Homepage Architecture Overview

The ClearTapLab homepage is designed as an **authoritative, frictionless diagnostic router**. It prioritizes our three primary content pillars:
1. **Reverse Osmosis (RO):** Core commercial and technical drinking water hub.
2. **Water Testing & Reports:** High-trust municipal CCR and private well diagnostic hub.
3. **Water Problem Troubleshooting:** High-urgency symptom resolution hub (sulfur, limescale, rust).

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 HOMEPAGE 6-SECTION WIREFRAME                                     │
├────┬────────────────────────────┬────────────────────────────────────────────────────────────────┤
│ #  │ Section Name               │ Key Function & Priority Focus                                  │
├────┼────────────────────────────┼────────────────────────────────────────────────────────────────┤
│ 01 │ Hero Section               │ Core value prop, dual CTAs (Problems / RO), independent trust  │
│ 02 │ Core System Hubs           │ Prioritized: (1) RO, (2) Testing, (3) Problems, (4) Whole-Home │
│ 03 │ Water Problem Diagnostics  │ Symptom cards: Sulfur smell, Limescale, Rust, Chlorine taste   │
│ 04 │ 3-Step Purity Framework    │ Decision tree: (1) Test Tap ➔ (2) Match Tech ➔ (3) Lifetime TCO│
│ 05 │ Featured Engineering Guides│ 4 Flagship posts (RO review, CCR report, Sulfur fix, RO vs CB) │
│ 06 │ About & Editorial Trust    │ Engineering background, certification analysis, zero hype      │
└────┴────────────────────────────┴────────────────────────────────────────────────────────────────┘
```

---

## 2. Step 1: Configure Homepage SEO Metadata

In the WordPress block editor on the `Home` page, scroll to the **Rank Math SEO** meta box and configure these exact metadata values:

* **SEO Title:** `ClearTapLab | Engineering-Based Home Water Quality Education & Filtration Analysis`
* **Meta Description:** `Understand your home water problems with first-principles engineering. Objective analysis of Reverse Osmosis systems, water testing reports, and filtration specifications.`
* **Canonical URL:** `https://cleartaplab.com/`
* **Social / Open Graph (Facebook/Twitter tab):**
  * **OG Title:** `ClearTapLab: Understand Your Water. Choose the Right Solution.`
  * **OG Description:** `Engineering-based home water quality education, Reverse Osmosis reviews, water testing diagnostics, and filtration technology analysis without sales pressure.`
  * **OG Image:** Upload `cleartaplab-og-home.webp` (`1200x630px`).

---

## 3. Step 2: Page Setup & Static Front Page

### 3.1 Kadence Page Settings
1. Navigate to: **Pages ➔ Add New Page** (or edit existing `Home`).
2. In the top-right **Kadence Page Settings** panel:
   * **Page Title:** Set to **Disable / Hide**.
   * **Page Layout:** Set to **Unboxed / Full Width**.
   * **Content Style:** Set to **Unboxed**.
   * **Sidebar:** Set to **No Sidebar**.
   * **Content Padding:** Set to **Disabled / None** (row layouts manage padding).
3. Click **Publish / Update**.

### 3.2 Set Static Front Page
1. Go to: **Settings ➔ Reading**.
2. Under *Your homepage displays*, select **A static page**.
3. Set **Homepage:** Select `Home`.
4. Click **Save Changes**.

---

## 4. Step 3: Block Assembly & Real Image Sourcing Guidelines

Open the `Home` page in the block editor and insert the markup from [`cleartaplab_homepage_content.md`](file:///d:/Personal/AntiGravity/Affiliate%20Marketting/cleartaplab_homepage_content.md):

### Image Sourcing Guidelines per Section (No AI Images):

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                HOMEPAGE IMAGE SOURCING MATRIX                                    │
├──────┬────────────────────────┬───────────────────────────────┬──────────────────────────────────┤
│ Sect │ Target Image           │ Approved Real Source          │ Target File Name                 │
├──────┼────────────────────────┼───────────────────────────────┼──────────────────────────────────┤
│ 01   │ Hero Background/Header │ Editorial tap water pouring   │ `residential-tap-water-hero.webp`│
│ 02   │ Card 1: RO Hub         │ Manufacturer under-sink render│ `reverse-osmosis-under-sink.webp`│
│ 02   │ Card 2: Water Testing  │ EPA test kit & report photo   │ `home-water-testing-kit-ccr.webp`│
│ 02   │ Card 3: Water Problems │ Real limescale plumbing photo │ `hard-water-limescale-pipe.webp` │
│ 02   │ Card 4: Whole-House    │ Real whole-house filter setup │ `whole-house-filtration-hub.webp`│
│ 03   │ Symptom Troubleshooting│ Closeups of real fixtures     │ `sulfur-water-heater-anode.webp` │
│ 05   │ Featured Guides        │ Product photos / 2D diagrams  │ `waterdrop-g3p800-installed.webp`│
└──────┴────────────────────────┴───────────────────────────────┴──────────────────────────────────┘
```

---

## 5. Phase 3 Verification Checklist

Verify these 6 criteria before moving to Phase 4:

```
[ ] 1. Homepage SEO title, meta description, and Open Graph tags configured in Rank Math.
[ ] 2. Category hierarchy prioritizes Reverse Osmosis, Water Testing, and Water Problems.
[ ] 3. All copy uses accurate terminology ("NSF/ANSI certification analysis" - zero claims of conducting lab audits).
[ ] 4. All images follow real sourcing guidelines (zero AI-generated visuals).
[ ] 5. Page displays fluidly across mobile (< 480px), tablet (768px), and desktop (1200px+).
[ ] 6. Static front page active in Settings > Reading.
```

---

## Next Step: Proceeding to Phase 4

With the Homepage completed and verified, we are ready to proceed to:
* **Phase 4: SEO Content Hub Pages & Category Taxonomy Setup** (Building out the 5 category archive hub templates and launching the first article templates).
