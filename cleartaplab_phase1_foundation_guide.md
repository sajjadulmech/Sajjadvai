# ClearTapLab Phase 1: WordPress Foundation & Setup Manual

> **Phase 1 Master Manual (Updated & Refined)**  
> **Brand:** ClearTapLab (`ClearTapLab.com`)  
> **Positioning:** Engineering-Based Home Water Quality Education & Diagnostics Platform  
> **Target Architecture:** WordPress.org Core + Kadence Theme (Free) + Gutenberg (Kadence Blocks Free) + Rank Math SEO (Free)  
> **Target Audience:** Solo Founder / Non-Developer / Engineering Lead  

---

## 1. Foundation Principles

Before publishing content or building page layouts, we establish the technical foundation for ClearTapLab. This setup is built on four core principles:

1. **Lightweight & Maintainable:** 100% native WordPress blocks and free Kadence Theme settings. No Elementor, no heavy page builders, no jQuery, and zero custom PHP hacks.
2. **Real-World Core Web Vitals:** We optimize for real user experience—fast Largest Contentful Paint (LCP), instant Interaction to Next Paint (INP), and zero Cumulative Layout Shift (CLS)—rather than chasing synthetic PageSpeed benchmarks at the expense of functionality.
3. **Local Font Privacy & Performance:** We serve Google Fonts locally directly from the WordPress host, eliminating render-blocking third-party font requests.
4. **Structural SEO from Day 1:** Clean URL slugs, logical category hierarchies, breadcrumb schema, and standardized article templates.

---

## 2. Step 1: WordPress Core Configuration

Log in to your WordPress dashboard (`yourdomain.com/wp-admin`) and configure these foundational settings:

### 2.1 Permalinks (SEO Foundation)
* Navigate to: **Settings ➔ Permalinks**
* Under *Common Settings*, select **Post name** (`https://cleartaplab.com/%postname%/`)
* Click **Save Changes**.
* *Why:* Short, clean URLs without dates or numbers rank higher and remain evergreen.

### 2.2 Site Identity & Timezone
* Navigate to: **Settings ➔ General**
* **Site Title:** `ClearTapLab`
* **Tagline:** `Engineering-Grade Home Water Diagnostics`
* **WordPress Address & Site Address:** `https://cleartaplab.com` *(Verify `https` SSL is active)*
* **Timezone:** Select your local city or UTC offset (e.g., `New York` or `UTC-5`).
* **Date Format:** `F j, Y` (e.g., *August 17, 2026*)
* Click **Save Changes**.

### 2.3 Discussion & Comment Hygiene
* Navigate to: **Settings ➔ Discussion**
* ❌ *Uncheck:* "Attempt to notify any blogs linked to from the post"
* ❌ *Uncheck:* "Allow link notifications from other blogs (pingbacks and trackbacks)"
* ✅ *Check:* "Comment author must fill out name and email"
* ✅ *Check:* "Comment must be manually approved"
* Click **Save Changes**.

---

## 3. Step 2: Kadence Theme Manual Configuration (Field-by-Field)

> [!TIP]
> **Manual Customizer Priority:** To avoid any plugin incompatibilities or JSON import version mismatches, follow this exact manual customizer walkthrough. It takes less than 5 minutes.

### 3.1 Install Kadence Theme
1. In WordPress Admin, go to **Appearance ➔ Themes ➔ Add New Theme**.
2. Search for **Kadence**.
3. Click **Install**, then click **Activate**.

---

### 3.2 Configure Global Colors (Palette Slots 1 to 9)
1. Go to: **Appearance ➔ Customize ➔ Colors & Fonts ➔ Colors**.
2. Click on the **Global Palette** bar. Set each of the 9 color slots to the following hex values:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                   GLOBAL COLOR PALETTE SLOTS                                     │
├──────┬───────────┬───────────────────────────┬───────────────────────────────────────────────────┤
│ Slot │ Hex Code  │ Name / Semantic Role      │ Where Kadence Applies It                          │
├──────┼───────────┼───────────────────────────┼───────────────────────────────────────────────────┤
│ 1    │ #0084D1   │ Primary Accent (Aqua/Cyan)│ Primary buttons, active links, filter tags        │
│ 2    │ #006EB3   │ Dark Blue (Hover State)   │ Button hover states, active link hover            │
│ 3    │ #0D2040   │ Deep Navy                 │ Headings H1–H6, dark section cards, footer bg     │
│ 4    │ #0D2040   │ Main Reading Text         │ Standard paragraph body text                      │
│ 5    │ #526E88   │ Muted Blue-Slate          │ Subtitles, captions, technical spec labels        │
│ 6    │ #E1EDF5   │ Structural Gray-Blue      │ Card borders, table dividers, input borders       │
│ 7    │ #E0F2FE   │ Soft Aqua Background      │ Badge backgrounds, code snippets, highlight boxes │
│ 8    │ #FFFFFF   │ Surface Pure White        │ Card containers, white reading surfaces           │
│ 9    │ #F4FAFD   │ Soft Ice-Blue Page Bg     │ Global background behind all pages and articles   │
└──────┴───────────┴───────────────────────────┴───────────────────────────────────────────────────┘
```

3. **Page Backgrounds:**
   * **Site Background:** Select **Palette 9** (`#F4FAFD`).
   * **Content Background:** Select **Palette 8** (`#FFFFFF`).
4. Click **Publish**.

---

### 3.3 Configure Typography & Local Font Hosting
1. Go to: **Appearance ➔ Customize ➔ Colors & Fonts ➔ Typography**.
2. **Base Font (Body Copy):**
   * **Font Family:** `Inter`
   * **Font Weight:** `400 (Regular)`
   * **Font Size:** `16px` | **Line Height:** `1.65`
   * **Color:** Select **Palette 4** (`#0F172A`).
3. **Headings Font (H1–H6):**
   * **Font Family:** `Plus Jakarta Sans`
   * **Font Weight:** `700 (Bold)`
   * **Letter Spacing:** `-0.025em`
   * **Color:** Select **Palette 3** (`#0B192C`).
4. **Specific Heading Sizes:**
   * **H1:** `44px` (Desktop) / `28px` (Mobile) | Weight `800` | Line Height `1.15` | Letter Spacing `-0.035em`
   * **H2:** `32px` (Desktop) / `22px` (Mobile) | Weight `800` | Line Height `1.25` | Letter Spacing `-0.03em`
   * **H3:** `24px` (Desktop) / `18px` (Mobile) | Weight `700` | Line Height `1.3`
   * **H4:** `20px` (Desktop) / `16px` (Mobile) | Weight `700` | Line Height `1.35`
5. **Local Font Hosting & Performance:**
   * Go to: **Appearance ➔ Customize ➔ General ➔ Performance**.
   * ✅ **Enable "Load Google Fonts Locally"** — *This causes Kadence to download the font files to your own hosting server on first save, eliminating external render-blocking calls to Google and complying with privacy standards.*
   * ✅ **Enable "Preload Local Fonts"** — *Ensures the browser fetches body and heading fonts instantly, eliminating layout shift (CLS).*
6. Click **Publish**.

---

### 3.4 Configure Global Buttons
1. Go to: **Appearance ➔ Customize ➔ Colors & Fonts ➔ Buttons**.
2. **Primary Button:**
   * **Text Color:** `#FFFFFF` (White)
   * **Background Color:** Select **Palette 1** (`#0284C7`)
   * **Hover Text Color:** `#FFFFFF`
   * **Hover Background Color:** Select **Palette 2** (`#0369A1`)
   * **Border Radius:** `8px`
   * **Font Family:** `Plus Jakarta Sans` | Weight: `700` | Size: `16px`
   * **Padding:** `12px` top/bottom, `24px` left/right.
3. Click **Publish**.

---

### 3.5 Configure Layout & Max Widths
1. Go to: **Appearance ➔ Customize ➔ General ➔ Layout**.
2. **Content Max Width:** Set to `1200px`.
3. **Single Post Layout:**
   * Go to: **Appearance ➔ Customize ➔ Posts/Pages Layout ➔ Single Post Layout**.
   * Set Container Layout to **Unboxed** or **Normal**.
   * Set Content Style to **Narrow** (`780px` max reading width) for optimal editorial legibility.
4. Click **Publish**.

---

## 4. Step 3: Global Custom CSS (Lightweight Components)

We use a minimal, modular CSS stylesheet that defines our design tokens and custom component classes without overriding Kadence core blocks.

1. Open [`cleartaplab_global_styles.css`](file:///d:/Personal/AntiGravity/Affiliate%20Marketting/cleartaplab_global_styles.css).
2. Copy the entire contents.
3. In WordPress Admin, navigate to: **Appearance ➔ Customize ➔ Additional CSS**.
4. Paste the code into the box.
5. Click **Publish**.

### Available Reusable Component Classes:
* `.ctl-badge-pill` — Aqua pill for categories and tags.
* `.ctl-badge-teal` — Teal pill for NSF/ANSI certified products.
* `.ctl-badge-warning` — Orange pill for contaminant alerts (Lead, PFAS, Hardness).
* `.ctl-card` — 20px rounded white card with subtle elevation.
* `.ctl-card-dark` — Deep Navy container for highlighted sections.
* `.ctl-symptom-card` — Problem card for water troubleshooting.
* `.ctl-step-card` — 3-step diagnostic framework box.
* `.ctl-spec-box` — Engineering spec callout box with accent left border.
* `.ctl-spec-grid` — Responsive grid for technical specs (GPM, TDS, Micron).
* `.ctl-table` / `.ctl-table-wrapper` — Clean, zebra-striped, responsive comparison table.
* `.ctl-author-box` — High-trust E-E-A-T author bio container.

---

## 5. Step 4: Kadence Blocks Free Configuration

1. In WordPress Admin, go to **Plugins ➔ Add New Plugin**.
2. Search for **Kadence Blocks** (Free by Kadence WP).
3. Click **Install**, then click **Activate**.
4. Go to **Kadence ➔ Settings ➔ Blocks**:
   * **Row Layout:** Default container max width set to `1200px`.
   * **Advanced Heading:** Default typography set to `Inherit from Theme`.
   * **Advanced Button:** Default border-radius set to `8px`.

---

## 6. Step 5: SEO Taxonomy Setup

Refer to the complete [cleartaplab_seo_content_architecture.md](file:///d:/Personal/AntiGravity/Affiliate%20Marketting/cleartaplab_seo_content_architecture.md) for full SEO definitions.

Navigate to: **Posts ➔ Categories** and create the 5 primary categories:

1. **Water Problems** (`water-problems`)
   * *Description:* Diagnose tap and well water symptoms, from sulfur odors and rust stains to limescale buildup and chlorine taste.
2. **Water Testing** (`water-testing`)
   * *Description:* Interpret municipal Consumer Confidence Reports (CCRs) and choose certified EPA mail-in lab test kits.
3. **Reverse Osmosis** (`reverse-osmosis`)
   * *Description:* Unbiased engineering breakdowns, efficiency ratios, and benchmark evaluations for under-sink and countertop RO systems.
4. **Filtration Technology** (`filtration-technology`)
   * *Description:* First-principles explanations of water treatment physics, media types, micron ratings, and NSF/ANSI certification standards.
5. **System Guides** (`system-guides`)
   * *Description:* Comprehensive sizing guides, installation breakdowns, and lifetime cost calculations for residential water treatment.

---

## 7. Step 6: Real-World Core Web Vitals Optimization

Rather than breaking site functionality to achieve artificial 100/100 scores, configure these practical optimizations:

### 7.1 Caching & Server Compression
* Install **LiteSpeed Cache** (on LiteSpeed hosting) or **WP Super Cache** / **W3 Total Cache** (on Apache/Nginx).
* Enable **Page Caching** and **Browser Caching**.
* Ensure **Gzip** or **Brotli** compression is active on your host.

### 7.2 Image Optimization
* Install **Converter for Media** or **ShortPixel** (Free).
* Enable automatic conversion of uploaded JPGs/PNGs to **WebP**.
* Set maximum image upload dimensions to `1600px` wide.
* Always supply width and height attributes (WordPress block editor does this natively) to eliminate layout shift (CLS).

### 7.3 Font & CSS Delivery
* With Kadence's **"Load Google Fonts Locally"** enabled, font files are cached on your domain with `font-display: swap`, ensuring instant text rendering on mobile networks.

---

## 8. Phase 1 Verification Checklist

Verify each of the following 8 items before proceeding to Phase 2:

```
[ ] 1. Permalinks set to /%postname%/ (Settings > Permalinks).
[ ] 2. Kadence 9-color palette configured with exact hex values (#0B192C, #0284C7, #F8FAFC).
[ ] 3. Typography set to Plus Jakarta Sans (Headings) and Inter (Body).
[ ] 4. "Load Google Fonts Locally" and "Preload Local Fonts" enabled in Kadence Performance.
[ ] 5. cleartaplab_global_styles.css pasted into Appearance > Customize > Additional CSS.
[ ] 6. 5 primary SEO categories created with clean slugs and descriptions.
[ ] 7. Kadence Blocks (Free) installed and activated.
[ ] 8. SEO Content Architecture document reviewed for article publishing standards.
```

---

## Next Step

With the foundation verified and the SEO content architecture locked in, we are ready to proceed to:
* **Phase 2: Website Structure & Main Authority Pages** (Homepage, About the Engineer, Editorial & Testing Policy, Contact, Affiliate Disclosure, Privacy Policy, Terms of Service).
