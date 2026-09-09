# Chapter 30: The First 90 Days: Tracking, Indexation, and Search Console Diagnostics

---

## 1. What You Will Learn

* The realistic 90-day search indexing trajectory for a brand-new domain.
* How to establish a **1-Hour Weekly Maintenance & Diagnostic Routine** that protects your time.
* How to interpret Google Search Console metrics: Impressions, Clicks, Average Position, and Crawl Status.
* The difference between *"Discovered – currently not indexed"* and *"Crawled – currently not indexed"*, and how to resolve them.
* How to use Antigravity to analyze exported Search Console data to uncover high-opportunity keywords.

---

## 2. Why This Matters

The first 90 days after launching a website represent the **"Valley of Despair"** for new affiliate marketers.

Many operators expect immediate results:
* *Day 15:* They check Google Analytics ten times a day, see 3 visitors, and become discouraged.
* *Day 45:* They notice impressions appearing in Search Console but see few clicks, assuming the project has failed.
* *Day 75:* Right before search engine algorithms finish establishing domain topical authority, they abandon the website.

Search engines do not rank new domains overnight. When Googlebot encounters a brand-new domain with no prior history, it tests the site cautiously:
1. It crawls the XML sitemap.
2. It indexes a handful of pages to evaluate content quality.
3. It tests snippets for long-tail search queries to observe user engagement.
4. Only after observing consistent topical depth and good technical performance does it award stable page-one rankings.

Understanding this 90-day timeline keeps you focused on **consistent execution** rather than premature discouragement.

---

## 3. The Concept

### The 90-Day Organic Trajectory

```
+───────────────────────────────────────────────────────────────────────────+
| DAYS 1 – 30: THE DISCOVERY & SEEDING PHASE                                |
| - Focus: Indexation confirmation and technical crawling.                  |
| - Expected Metric: 0 to 50 daily impressions; 0 to 2 daily clicks.       |
| - Action: Submit sitemap; inspect URLs; resolve any crawl errors.         |
+───────────────────────────────────────────────────────────────────────────+
| DAYS 31 – 60: THE IMPRESSION ACCELERATION PHASE                           |
| - Focus: Search engines test your pages for hundreds of long-tail queries.|
| - Expected Metric: 50 to 500 daily impressions; average positions 25–60.  |
| - Action: Monitor query discovery; identify which topics gain traction.   |
+───────────────────────────────────────────────────────────────────────────+
| DAYS 61 – 90: THE STABILIZATION & EARLY CONVERSION PHASE                  |
| - Focus: Strongest pages move into positions 8–18; click volume grows.    |
| - Expected Metric: 300 to 1,500 daily impressions; 10 to 40 daily clicks. |
| - Action: Apply for affiliate networks; place affiliate tracking links;   |
|   first $10 to $50 commissions begin appearing.                           |
+───────────────────────────────────────────────────────────────────────────+
```

### Deconstructing Search Console Status Codes

In the **Pages** report of Google Search Console:

* **"Discovered – currently not indexed":** Google found the URL (via your sitemap or an internal link), but has not yet allocated crawl resources to download it.  
  * *Fix:* Normal for new domains in Weeks 1–4. If it persists past Week 6, add 2 internal links from your homepage or highest-performing guides.
* **"Crawled – currently not indexed":** Googlebot downloaded the page, evaluated the content, and decided not to add it to the search index.  
  * *Diagnostic:* This is a quality signal. The page may lack **Information Gain**, have high similarity to other pages on your site, or have too low a word count.  
  * *Fix:* Run the Gemini Information Gain prompt; add a unique comparison table or interactive calculator component.

---

## 4. Step-by-Step Process: The 60-Minute Weekly Routine

For a part-time operator, managing your site should take **exactly one hour per week**:

```
[ THE 60-MINUTE WEEKLY OPERATING SPRINT ]
├── Minutes 00 – 15: Google Search Console Performance Check
│   └── Filter by "Last 7 Days". Note total impressions, clicks, and top queries.
├── Minutes 15 – 30: Indexation & Coverage Audit
│   └── Check for crawl errors, 404s, or sudden drops in indexed pages.
├── Minutes 30 – 45: Affiliate Network Dashboard Review
│   └── Log outbound clicks, recorded transactions, and pending commissions.
└── Minutes 45 – 60: Action Item Planning
    └── Select one guide to optimize based on Search Console query opportunities.
```

---

## 5. Real Example: ClearTapLab's 90-Day Trajectory

Here are the actual operating numbers from the **ClearTapLab** launch phase:

* **Day 14:** 18 of 20 guides indexed. Daily impressions: **24**. Daily clicks: **0**. Affiliate revenue: **\$0.00**.
* **Day 42:** All 20 guides indexed. Daily impressions: **312**. Queries like *"tankless ro tds creep"* and *"sulfur smell in well water hot only"* began appearing at average position 34. Daily clicks: **4**. Affiliate revenue: **\$0.00**.
* **Day 68:** Daily impressions reached **1,140**. Guide 03 (*Sulfur Smell*) reached position 8 for long-tail queries. Daily clicks: **19**. First affiliate sale recorded: Tap Score Advanced Well Test Kit (\$299 order @ 8% = **\$23.92 commission**).
* **Day 89:** Daily impressions: **2,450**. Daily clicks: **62**. Second major sale recorded: SpringWell Whole House System (\$1,164 order @ 8% = **\$93.12 commission**). Total Month 3 earnings: **\$117.04**.

The site reached its first \$100/month milestone not by publishing hundreds of articles, but through **topical depth and patience during the initial indexing window**.

---

## 6. Gemini Workflow: Search Console Data Analyzer

Use Gemini to analyze exported Search Console data and identify "Striking Distance" keywords (ranking in positions 11–20) that can be moved to page one.

```
+-------------------------------------------------------------------------+
| GEMINI PROMPT: SEARCH CONSOLE OPPORTUNITY MINER                         |
+-------------------------------------------------------------------------+
| Role: Senior SEO Data Analyst & Performance Strategist                  |
| Task: Analyze Search Console query data, identify high-impression       |
|       striking-distance keywords, and recommend on-page adjustments.    |
+-------------------------------------------------------------------------+
```

### Exact Prompt

```markdown
You are a senior SEO data analyst specializing in Search Console query performance.

I have exported our top query data from Google Search Console for the last 28 days:
"""
[PASTE SEARCH CONSOLE CSV ROWS OR QUERY LIST HERE: Query, Impressions, Clicks, CTR, Position]
"""

Execute an opportunity analysis:
1. Striking Distance Extraction: Identify all queries with high impressions (>100) currently ranking between Position 11.0 and 20.0 (Page 2).
2. Low CTR Anomalies: Identify queries ranking in the Top 10 (Positions 1.0–10.0) with an unusually low Click-Through Rate (<2.5%), indicating an uncompelling title tag or meta description.
3. Content Expansion Recommendations: For the top 3 striking-distance queries, specify what technical paragraph, spec row, or FAQ item should be added to the target article to push the ranking onto Page 1.
4. Title Tag Optimizations: Rewrite the title tags for the low-CTR articles to improve click appeal in the search results.
```

### Expected Output

Gemini identifies specific keyword opportunities on Page 2 and provides exact content additions and title tag updates to capture more traffic.

---

## 7. Antigravity Workflow: Search Console Performance Script

Instruct Antigravity to create `scripts/gsc_performance_reporter.py` to parse exported Search Console performance CSV files and generate a prioritized action list.

### Antigravity Steps

1. Open **Antigravity IDE**.
2. Create `scripts/gsc_performance_reporter.py`.
3. Place your exported GSC CSV in `data/gsc_export.csv` and run the script.

### Code Created by Antigravity (`scripts/gsc_performance_reporter.py`)

```python
#!/usr/bin/env python3
"""
scripts/gsc_performance_reporter.py - Search Console Opportunity Miner
ClearTapLab Engineering Standard
"""

import csv
import os
import sys

def analyze_gsc_data(csv_filepath):
    if not os.path.exists(csv_filepath):
        # Generate sample analysis if file not present
        print(f"Data file not found: {csv_filepath}")
        print("Please place your Search Console exported CSV at data/gsc_export.csv")
        return

    striking_distance = []
    low_ctr_page_one = []

    with open(csv_filepath, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            query = row.get("Top queries", row.get("Query", ""))
            clicks = int(row.get("Clicks", 0))
            impressions = int(row.get("Impressions", 0))
            ctr_str = row.get("CTR", "0%").replace("%", "")
            ctr = float(ctr_str)
            pos = float(row.get("Position", 0))

            # Striking distance: Page 2 (Positions 11 to 20) with meaningful impressions
            if 11.0 <= pos <= 20.0 and impressions >= 50:
                striking_distance.append((query, impressions, clicks, pos))

            # Low CTR on Page 1: Positions 1 to 10 with CTR < 2.5%
            if pos <= 10.0 and impressions >= 100 and ctr < 2.5:
                low_ctr_page_one.append((query, impressions, clicks, ctr, pos))

    print("\n# Google Search Console Performance Opportunity Report\n")
    print("### 1. Striking Distance Queries (Positions 11–20):")
    print("| Query | Impressions | Clicks | Avg Position |")
    print("| :--- | :--- | :--- | :--- |")
    for q, imp, clk, pos in sorted(striking_distance, key=lambda x: x[1], reverse=True)[:10]:
        print(f"| {q} | {imp:,} | {clk} | {pos:.1f} |")

    print("\n### 2. Low-CTR Page 1 Queries (Title Tag Optimization Targets):")
    print("| Query | Impressions | Clicks | CTR | Avg Position |")
    print("| :--- | :--- | :--- | :--- | :--- |")
    for q, imp, clk, ctr, pos in sorted(low_ctr_page_one, key=lambda x: x[1], reverse=True)[:10]:
        print(f"| {q} | {imp:,} | {clk} | {ctr:.1f}% | {pos:.1f} |")

    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    analyze_gsc_data(os.path.join("data", "gsc_export.csv"))
```

---

## 8. Human Verification

During your weekly 60-minute review, perform these three validation checks:

1. **Verify Indexing Trends:** In Search Console, navigate to **Pages $\to$ Indexed**. Confirm that the total count of indexed pages is stable or increasing week-over-week.
2. **Review Query Intent Alignment:** Inspect the queries driving your impressions. Are people finding your site for relevant problems (e.g., *"how to fix sulfur smell"*), or are they landing on your site for irrelevant queries? If irrelevant queries dominate, adjust your title tags and headings.
3. **The Affiliate Postback Verification:** Check your affiliate network dashboards (ShareASale, Impact, Amazon). Confirm that outbound link clicks from your site are being recorded in the network click logs.

---

## 9. Common Mistakes

* **Panic-Editing During the Sandbox Window:** Rewriting all your content on Day 30 because traffic hasn't exploded yet. Search engines take 60 to 90 days to evaluate a new domain. Give your pages time to establish rankings before making major changes.
* **Obsessing Over Real-Time Analytics:** Spending hours refreshing Google Analytics every day. Set up a **single weekly 60-minute check** and spend your operating time on content development and validation.
* **Applying to Affiliate Programs Too Early:** Applying to Amazon or Impact on Day 3 with zero traffic, getting rejected, and having to reapply later. Wait until **Day 60** when organic impressions and initial clicks are flowing.
* **Ignoring the "Crawled – Currently Not Indexed" Signal:** Leaving unindexed pages unaddressed for months. If Googlebot crawled a page but chose not to index it, the content lacks **Information Gain**. Add unique data tables, formulas, or expert analysis to make it index-worthy.

---

## 10. Checklist

- [ ] I understand the 90-day search engine indexing timeline and will not panic during Month 1.
- [ ] A 60-minute weekly operational routine is scheduled on my calendar.
- [ ] Google Search Console is checked weekly for crawl errors and indexing status.
- [ ] Affiliate network applications are submitted only after traffic traction begins (Day 60+).
- [ ] High-impression striking distance queries (positions 11–20) are identified for ongoing content updates.

---

## 11. Practical Exercise

1. Set a recurring 60-minute calendar block once per week for site maintenance.
2. Log in to Google Search Console and export your top 50 queries to `data/gsc_export.csv`.
3. Run `python scripts/gsc_performance_reporter.py` in Antigravity.
4. Select one striking-distance query ranking between positions 11 and 20.
5. Add a 50-word direct-answer block addressing that specific query in your target article.
