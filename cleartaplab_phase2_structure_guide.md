# ClearTapLab Phase 2: Authority Pages & Structure Setup Guide (Refined)

> **Phase 2 Implementation Manual**  
> **Brand:** ClearTapLab (`ClearTapLab.com`)  
> **Target Scope:** 6 Core Authority, Trust & Legal Pages + Author Profile Foundation  
> **Target Architecture:** WordPress Core + Kadence Theme + Kadence Blocks (Free)  
> **Target Audience:** Solo Founder / Non-Developer / Engineering Lead  

---

## 1. Phase 2 Scope & E-E-A-T Strategy

Phase 2 establishes the **authority, trust, transparency, and legal foundation** for ClearTapLab. 

By clearly articulating our engineering auditing methodology, distinguishing our work from a physical laboratory, disclaiming bespoke consulting, and establishing a consistent author profile, we build an unassailable foundation for Google's E-E-A-T evaluations.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                PHASE 2 PAGE & ARCHITECTURE MATRIX                                │
├──────┬────────────────────────┬──────────────────────────┬───────────────────────────────────────┤
│ #    │ Page Title             │ Target URL Slug          │ Primary Function & Guardrail          │
├──────┼────────────────────────┼──────────────────────────┼───────────────────────────────────────┤
│ 1    │ About ClearTapLab      │ `/about/`                │ Engineering mission & lab distinction │
│ 2    │ Editorial Policy       │ `/editorial-policy/`     │ 4-stage audit method (no physical lab)│
│ 3    │ Author Profile/Bylines │ `/author/lead-engineer/` │ Standardized author credentials & schema│
│ 4    │ Contact Us             │ `/contact/`              │ Inquiries (no bespoke consulting)     │
│ 5    │ Affiliate Disclosure   │ `/affiliate-disclosure/` │ Adaptable FTC commercial compliance   │
│ 6    │ Privacy Policy         │ `/privacy-policy/`       │ Adaptable GDPR/CCPA data & cookie policy│
│ 7    │ Terms of Service       │ `/terms/`                │ Educational & DIY liability disclaimer│
└──────┴────────────────────────┴──────────────────────────┴───────────────────────────────────────┘
```

---

## 2. Step-by-Step Page Creation in WordPress

For each page, follow this straightforward sequence in WordPress Admin:

1. Navigate to: **Pages ➔ Add New Page**.
2. Enter the **Page Title** and verify the **URL Slug**.
3. In the top-right **Kadence Page Settings** panel:
   * **Page Title:** Set to **Disable / Hide**.
   * **Page Layout:** Set to **Unboxed** or **Normal**.
   * **Content Style:** Set to **Narrow Container** (`780px` max reading width).
   * **Sidebar:** Set to **No Sidebar**.
4. Open [`cleartaplab_main_pages_content.md`](file:///d:/Personal/AntiGravity/Affiliate%20Marketting/cleartaplab_main_pages_content.md), copy the corresponding section, and paste it into the block editor.
5. **Customize Placeholders:** Replace any bracketed tags (e.g., `[Insert Contact Email]`, `[Insert Entity Name]`) with your actual business details.
6. Click **Publish**.

---

## 3. Setting Up the WordPress Author Profile & Bylines

To ensure every published article carries strong author attribution:

### 3.1 Configure WordPress User Profile
1. In WordPress Admin, go to: **Users ➔ Profile** (or *Edit Profile* on your admin account).
2. **Display Name publicly as:** Select `ClearTapLab Editorial Team` or your preferred author name.
3. **Biographical Info:** Paste the standardized bio:
   > *"ClearTapLab provides independent engineering analysis of residential water filtration technology, public water data (CCRs), and international testing standards (NSF/ANSI). Content is authored and fact-checked strictly for educational purposes."*
4. **Profile Picture:** Upload your author headshot via Gravatar or use the Kadence author avatar upload.
5. Click **Update Profile**.

### 3.2 Standard Byline Block in Article Publishing
When drafting articles in Gutenberg:
* Add the **Top Byline Block** right beneath the H1 headline.
* Add the **Author Bio Box** (`.ctl-author-box`) at the end of the article before the footer.

---

## 4. Menu & Navigation Architecture Setup

Link your new authority and legal pages into the global navigation:

### 4.1 Primary Header Navigation Menu
Go to: **Appearance ➔ Menus ➔ Primary Navigation**:
1. **Water Problems** (`/category/water-problems/`)
2. **Water Testing** (`/category/water-testing/`)
3. **Reverse Osmosis** (`/category/reverse-osmosis/`)
4. **Filtration Science** (`/category/filtration-technology/`)
5. **System Guides** (`/category/system-guides/`)
6. **About Us** (`/about/`)

*Header Action CTA Button:* **"Find Your Solution"** ➔ Links to `/water-problems/`.

---

### 4.2 Footer Architecture (4 Columns + Disclaimer)
Go to: **Appearance ➔ Customize ➔ Footer**:

* **Column 1 (Brand & Mission):** ClearTapLab summary with honest positioning.
* **Column 2 (System Guides):** Links to RO, Whole-House, Softeners, and Testing hubs.
* **Column 3 (Diagnostics):** Links to Water Problems and CCR interpretation guides.
* **Column 4 (Trust & Legal):**
  * [About the Lab](/about/)
  * [Editorial & Auditing Policy](/editorial-policy/)
  * [Affiliate Disclosure](/affiliate-disclosure/)
  * [Privacy Policy](/privacy-policy/)
  * [Terms of Service](/terms/)
  * [Contact Us](/contact/)

---

## 5. Phase 2 Quality Verification Checklist

Before proceeding to Phase 3, verify these 6 quality checks:

```
[ ] 1. All 6 authority/legal pages published with clean slugs (/about/, /editorial-policy/, /contact/, /affiliate-disclosure/, /privacy-policy/, /terms/).
[ ] 2. All pages configured with Kadence Narrow Container (780px) and No Sidebar.
[ ] 3. Bracketed placeholders customized for your specific email, entity name, and analytics tools.
[ ] 4. Clear distinction made between engineering data auditing and a physical laboratory across all pages.
[ ] 5. Explicit disclaimer active stating no professional engineering consulting or licensed plumbing contractor services are offered.
[ ] 6. Author profile configured in WordPress Users for consistent article bylines.
```

---

## Next Step

With all authority, legal, and author profiles established with pristine integrity guardrails, we are ready to proceed to:
* **Phase 3: Homepage Build** (Reviewing and assembling the 6-section homepage).
