# ClearTapLab Technical SEO & Schema Configuration Manual

> **Document Type:** Technical SEO Setup, XML Sitemaps, Schema Mapping & Indexing Protocols  
> **Brand:** ClearTapLab (`ClearTapLab.com`)  
> **Recommended SEO Plugin:** Rank Math SEO (Free) or Yoast SEO (Free)  
> **Target Audience:** Solo Founder / Non-Developer / Lead SEO Architect  

---

## 1. Technical SEO Overview

Search engine optimization for ClearTapLab is built on three technical pillars:
1. **Clean Crawlability:** An optimized `robots.txt` and segmented `sitemap_index.xml` ensure Googlebot and Bingbot index only high-value pages without wasting crawl budget on duplicate archives.
2. **Semantic Schema Markup:** Structured JSON-LD signals to Google's Knowledge Graph that ClearTapLab is an authoritative organization founded by a verified mechanical engineer.
3. **Index Hygiene:** Elimination of thin content, tag archives, attachment pages, and pagination duplicate issues.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               TECHNICAL SEO ARCHITECTURE OVERVIEW                                │
├──────────────────────────┬─────────────────────────────────────┬─────────────────────────────────┤
│ Component                │ Target Configuration                │ Strategic Outcome               │
├──────────────────────────┼─────────────────────────────────────┼─────────────────────────────────┤
│ Permalinks               │ `/%postname%/` (Strip Category Base)│ Clean, evergreen URLs           │
│ XML Sitemaps             │ `/sitemap_index.xml`                │ Instant indexing of new posts   │
│ Robots.txt               │ Custom Crawl Budget Optimization    │ Block admin/search crawl waste  │
│ Breadcrumbs              │ `Home > Category > Title` (JSON-LD) │ Rich snippet search display     │
│ Organization Schema      │ Brand + Founder (Person) Schema     │ Knowledge Graph & E-E-A-T trust │
│ Article & Review Schema  │ TechArticle & Product Review Schema │ Enhanced CTR in Google SERPs    │
└──────────────────────────┴─────────────────────────────────────┴─────────────────────────────────┘
```

---

## 2. Step 1: Rank Math SEO General Settings Setup

1. In WordPress Admin, go to **Plugins ➔ Add New Plugin**.
2. Search for **Rank Math SEO** (Free by Rank Math).
3. Click **Install**, then **Activate**.
4. Skip the automated wizard (or choose *Advanced*) and navigate to: **Rank Math ➔ General Settings**:

### 2.1 Links Settings
* **Strip Category Base:** Set to **ON** *(Optional: transforms `cleartaplab.com/category/water-problems/` to clean `cleartaplab.com/water-problems/`)*.
* **Redirect Attachments:** Set to **ON** ➔ **Redirect to Homepage** *(Prevents Google from indexing empty WordPress media attachment pages)*.
* **Nofollow External Links:** Set to **OFF** *(We manage affiliate link `rel="nofollow noopener"` attributes manually on commercial links)*.
* **Open External Links in New Tab:** Set to **ON**.

### 2.2 Breadcrumbs Settings
* Navigate to: **Rank Math ➔ General Settings ➔ Breadcrumbs**.
* **Enable Breadcrumbs function:** Set to **ON**.
* **Separator Character:** `›` or `/`
* **Show Homepage Link:** Set to **ON** (Homepage Label: `Home`).
* **Show Category in Breadcrumbs:** Set to **ON**.
* **Show Article Title in Breadcrumbs:** Set to **ON**.

---

## 3. Step 2: XML Sitemap Architecture

Navigate to: **Rank Math ➔ Sitemap Settings**:

### 3.1 General Sitemap Settings
* **Sitemap URL:** Verified at `https://cleartaplab.com/sitemap_index.xml`
* **Links per Sitemap:** Set to `200`
* **Images in Sitemaps:** Set to **Include Images**
* **Include Featured Images:** Set to **ON**

### 3.2 Post Types in Sitemap
* **Posts:** Set to **Include in Sitemap** (Sitemap Priority: `0.8`, Frequency: `Weekly`).
* **Pages:** Set to **Include in Sitemap** (Sitemap Priority: `0.6`).
* **Media / Attachments:** Set to **Do NOT Include**.

### 3.3 Taxonomies in Sitemap
* **Categories:** Set to **Include in Sitemap** (Sitemap Priority: `0.7`).
* **Tags:** Set to **Do NOT Include** *(Prevents thin content tag cannibalization)*.

---

## 4. Step 3: Robots.txt Setup

ClearTapLab uses a production-tuned `robots.txt` that preserves full crawl budget for articles and categories while allowing search engines to render all CSS, JS, and WebP media assets.

1. Open [`robots.txt`](file:///d:/Personal/AntiGravity/Affiliate%20Marketting/robots.txt).
2. In WordPress, navigate to: **Rank Math ➔ General Settings ➔ Edit robots.txt** (or upload the file directly to your site root via SFTP / cPanel).
3. Paste the following configuration:

```text
User-agent: *
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php
Disallow: /wp-includes/
Allow: /wp-includes/js/
Allow: /wp-includes/css/
Allow: /wp-includes/images/
Disallow: /*?s=*
Disallow: /*?*filter=*
Disallow: /trackback/
Disallow: /feed/
Disallow: /comments/feed/

# Allow full rendering of stylesheets and scripts
Allow: /*.css$
Allow: /*.js$
Allow: /*.webp$
Allow: /*.png$
Allow: /*.jpg$
Allow: /*.svg$

# Master XML Sitemap Reference
Sitemap: https://cleartaplab.com/sitemap_index.xml
```
4. Click **Save Changes**.

---

## 5. Step 4: Structured Data & Schema Mapping

Rank Math outputs structured JSON-LD data to help Google interpret who we are and what we publish.

### 5.1 Organization & Knowledge Graph Setup
Navigate to: **Rank Math ➔ Titles & Meta ➔ Local SEO / Knowledge Graph**:
* **Type:** Organization
* **Organization Name:** `ClearTapLab`
* **Alternate Name:** `ClearTapLab Water Quality Research`
* **Website URL:** `https://cleartaplab.com`
* **Logo:** Upload `cleartaplab-engineering-logo.svg` or `.png` (`600x60px` or square)
* **Email:** `contact@cleartaplab.com`

---

### 5.2 Global Post Type Schema Defaults
Navigate to: **Rank Math ➔ Titles & Meta ➔ Posts**:
* **Schema Type:** `Article`
* **Article Type:** `TechArticle` or `BlogPosting`
* **Headline:** `%post_title%`
* **Description:** `%post_excerpt%`

---

### 5.3 JSON-LD Author & Organization Schema Reference

Below is the structured data blueprint automatically generated for ClearTapLab:

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Organization",
      "@id": "https://cleartaplab.com/#organization",
      "name": "ClearTapLab",
      "url": "https://cleartaplab.com",
      "logo": {
        "@type": "ImageObject",
        "@id": "https://cleartaplab.com/#logo",
        "url": "https://cleartaplab.com/wp-content/uploads/cleartaplab-engineering-logo.png",
        "caption": "ClearTapLab"
      },
      "description": "Independent engineering-based home water quality education and diagnostics platform."
    },
    {
      "@type": "Person",
      "@id": "https://cleartaplab.com/#founder",
      "name": "ClearTapLab Lead Engineer",
      "jobTitle": "Mechanical Engineer & Water Filtration Researcher",
      "worksFor": {
        "@id": "https://cleartaplab.com/#organization"
      },
      "description": "Mechanical engineer specializing in residential fluid mechanics, membrane flux kinetics, and NSF/ANSI testing audits."
    }
  ]
}
```

---

## 6. Step 5: Google Search Console & Bing Webmaster Setup

### 6.1 Google Search Console Verification
1. Go to [Google Search Console](https://search.google.com/search-console).
2. Add a new **Domain Property**: `cleartaplab.com`.
3. Copy the **DNS TXT record** provided by Google.
4. Add the TXT record in your domain registrar DNS settings (Namecheap / Cloudflare / Hostinger).
5. Once verified, go to **Sitemaps** in the left menu.
6. Enter `sitemap_index.xml` and click **Submit**.

### 6.2 Bing Webmaster Tools Integration
1. Go to [Bing Webmaster Tools](https://www.bing.com/webmasters).
2. Click **Import from Google Search Console** (automatically syncs verified ownership and sitemaps in 1 click).

---

## 7. Step 6: Content SEO Workflow for Every New Article

Before hitting "Publish" on any article, verify these 8 on-page SEO factors in Rank Math:

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 ON-PAGE ARTICLE SEO CHECKLIST                                    │
├────┬────────────────────────────┬────────────────────────────────────────────────────────────────┤
│ #  │ Check Item                 │ Execution Standard                                             │
├────┼────────────────────────────┼────────────────────────────────────────────────────────────────┤
│ 01 │ Focus Keyword              │ Set single target query (e.g., `fix rotten egg sulfur water`)  │
│ 02 │ Title Tag (H1)             │ Contains keyword near beginning; under 60 characters           │
│ 03 │ Meta Description           │ Includes keyword + diagnostic hook; under 155 characters       │
│ 04 │ URL Slug                   │ Short, lowercase, hyphenated (`/fix-rotten-egg-sulfur-water/`) │
│ 05 │ Heading Structure          │ Single H1; H2s for main sections; H3s for subsections          │
│ 06 │ Internal Links             │ 3–6 contextual links (1 up-funnel to science, 2 down to guides)│
│ 07 │ External Authority Sources │ 1–2 links to EPA.gov, CDC.gov, or NSF.org databases            │
│ 08 │ Image Alt Text             │ All WebP images include descriptive, keyword-natural alt text  │
└────┴────────────────────────────┴────────────────────────────────────────────────────────────────┘
```

---

## 8. Phase 5 Verification Checklist

Verify these 6 final technical SEO milestones:

```
[ ] 1. Rank Math SEO installed and configured.
[ ] 2. Category base stripped and attachment pages redirected.
[ ] 3. XML Sitemap active at /sitemap_index.xml (posts, pages, categories included; tags excluded).
[ ] 4. robots.txt deployed and verified.
[ ] 5. Breadcrumbs active with JSON-LD markup.
[ ] 6. Google Search Console verified and sitemap_index.xml submitted.
```

---

## Next Step: Proceeding to Phase 6

With the Technical SEO and Schema foundation established, we are ready to move directly into:
* **Phase 6: Content System & Article Publishing Production** (Drafting our first batch of cornerstone educational and product teardown articles).
