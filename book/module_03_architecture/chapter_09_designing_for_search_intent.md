# Chapter 09: Designing for Search Intent: Commercial vs. Informational Gravity

---

## 1. What You Will Learn

* The psychological spectrum of search intent: Informational, Diagnostic, Comparative, and Transactional.
* How to prevent the "Intent Mismatch" penalty that causes high bounce rates and ranking demotions.
* The proper conversion architecture for each intent stage: when to use educational diagrams vs. comparison tables vs. direct CTA badges.
* How to use Gemini to classify keywords and predict the exact layout Google rewards for a target query.
* How to store and audit search intent classifications in an Antigravity JSON matrix.

---

## 2. Why This Matters

Most failed affiliate websites suffer from **Intent Mismatch**. 

When an operator wants to make money quickly, they often try to monetize every keyword aggressively. For example, when a homeowner searches for:
> *"Why does my well water smell like rotten eggs?"*

they are in an **anxious, diagnostic state**. They want to understand the chemistry of hydrogen sulfide gas and verify if their water is dangerous to drink. 

If they land on a low-quality affiliate page that starts with:
> *"Looking to buy a water filter? Click here for the Top 5 Best Filters on Amazon!"*

the reader bounces back to the search results in under 5 seconds. Google's ranking algorithms detect this immediate bounce (short dwell time) as a signal of user dissatisfaction, causing the page to lose rankings.

Conversely, when a user searches:
> *"Waterdrop G3P800 vs. iSpring RCC7AK"*

they have already diagnosed their problem, chosen reverse osmosis, and narrowed their choice down to two models. If they land on a page that provides 1,500 words on the history of municipal water treatment before showing a comparison, they will bounce just as quickly.

To rank and convert, the layout, tone, and monetization of the page must **match the exact search intent of the user**.

---

## 3. The Concept

### The 4 Stages of the Affiliate Intent Funnel

```
STAGE 1: INFORMATIONAL / DIAGNOSTIC
├── Query: "Why is my tap water cloudy?" / "Sulfur smell well water causes"
├── User State: Anxious, seeking explanation and safety guidance.
├── Optimal UX: Chemistry diagrams, diagnostic decision trees, water test advice.
├── Monetization: Low-friction links to water test kits ($30–$180); soft internal links.
└── Target Affiliate CTR: 1.0% – 2.5%

STAGE 2: TECHNOLOGICAL INVESTIGATION
├── Query: "Reverse osmosis vs. carbon filter" / "Ion exchange vs. TAC salt-free"
├── User State: Evaluating competing technical mechanisms.
├── Optimal UX: Scientific comparison tables, micron filtration cutoffs, operating costs.
├── Monetization: In-depth comparison tables linking to category buying guides.
└── Target Affiliate CTR: 3.0% – 6.0%

STAGE 3: COMMERCIAL ROUNDUP
├── Query: "Best reverse osmosis systems 2026" / "Best whole house filter for well water"
├── User State: Comparing specific branded systems; ready to make a decision.
├── Optimal UX: Filterable comparison matrix, "Best Overall" pick badges, spec boxes.
├── Monetization: High-contrast affiliate buttons, direct merchant checkout links.
└── Target Affiliate CTR: 6.0% – 12.0%

STAGE 4: TRANSACTIONAL / DIRECT ALTERNATIVES
├── Query: "Waterdrop G3P800 review & teardown" / "SpringWell CF1 discount"
├── User State: Final pre-purchase validation; checking warranty, noise, and dimensions.
├── Optimal UX: 5-year TCO breakdown, dimensional clearance specs, pros/cons.
├── Monetization: Prominent merchant pricing buttons, coupon code callouts.
└── Target Affiliate CTR: 10.0% – 20.0%
```

---

## 4. Step-by-Step Process: Keyword-to-Intent Mapping

```
Step 1: Gather 20 Target Keywords for Your Initial Content Cluster.
Step 2: Execute SERP Inspection to Observe Current Page-One Layouts.
   └── Does Google show video carousels, bulleted lists, comparison tables, or long guides?
Step 3: Run the Gemini Intent Classification Prompt.
Step 4: Assign Every Keyword an Intent Classification in data/intent_matrix.json.
Step 5: Bind Each Intent Type to a Specific Template Layout in Antigravity.
```

---

## 5. Real Example: ClearTapLab Intent Distribution

The **ClearTapLab** authority platform balances traffic acquisition and monetization by distributing its 20 initial cornerstone guides across all four intent stages:

* **Stage 1 (Informational / Diagnostic) — 6 Guides (30%):**
  * Guide 01: *How to Read Your Consumer Confidence Report (CCR)*
  * Guide 03: *Why Well Water Smells Like Rotten Eggs (Chemistry & Fixes)*
  * Guide 05: *Hard Water Sizing & GPG Scale Kinetics*
  * Guide 06: *Well Water Iron Chemistry: Ferrous vs. Ferric vs. Bacterial*
  * Guide 10: *How Much Water Does Reverse Osmosis Actually Waste?*
  * Guide 20: *Pressure Drop & Fluid Resistance: The Ergun Equation*
  * *Role:* Attract broad, high-volume organic search traffic, establish topical authority, and funnel readers to diagnostic test kits and commercial guides.
* **Stage 2 (Technological Investigation) — 6 Guides (30%):**
  * Guide 02: *Reverse Osmosis vs. Activated Carbon: Micron Cutoffs*
  * Guide 07: *Water Softeners vs. Salt-Free Conditioners: TAC Physics*
  * Guide 11: *Tankless vs. Tank Reverse Osmosis: The Engineering Reality*
  * Guide 15: *Remineralization Cartridges: Calcite vs. Corosex Dissolution*
  * Guide 18: *Sediment vs. Carbon Block: Mechanical Sieving Explained*
  * Guide 19: *Fluoride Removal: RO vs. Activated Alumina vs. Distillation*
  * *Role:* Guide buyers toward the correct filtration category using objective engineering comparisons.
* **Stage 3 (Commercial Roundups) — 5 Guides (25%):**
  * Guide 08: *Best Reverse Osmosis Systems (2026 Tested Audit)*
  * Guide 09: *PFAS & Forever Chemical Pitchers: Certified Reduction Audit*
  * Guide 13: *Best Whole-House Water Filters for Well Water (2026)*
  * Guide 14: *Best Mail-In Water Testing Kits (EPA Certified Lab Comparison)*
  * Guide 17: *Best Salt-Free Water Conditioners (DVGW W-512 Benchmark)*
  * *Role:* High-converting commercial hubs with structured comparison tables and pick badges.
* **Stage 4 (Deep Reviews & Teardowns) — 3 Guides (15%):**
  * Guide 04: *Waterdrop G3P800 Review: 800 GPD Engineering Teardown*
  * Guide 12: *SpringWell CF1 Whole House Filter Review: 10-Year TCO Audit*
  * Guide 16: *Water Softener Sizing Blueprint: Grain Capacity Equation*
  * *Role:* High-intent, high-ticket conversion pages that capture buyers immediately prior to checkout.

---

## 6. Gemini Workflow: Search Intent Classification Engine

Use Gemini to analyze your target keyword list and classify search intent along with recommended page elements.

```
+-------------------------------------------------------------------------+
| GEMINI PROMPT: SEARCH INTENT & LAYOUT ARCHITECT                         |
+-------------------------------------------------------------------------+
| Role: Senior Search Intent Strategist & UX Wireframe Architect          |
| Task: Classify a list of 10 keywords into intent categories and define   |
|       the mandatory UI components required to satisfy Google's SERP.   |
+-------------------------------------------------------------------------+
```

### Exact Prompt

```markdown
You are a senior search intent analyst and conversion UX architect.

Analyze the following list of 10 keywords for an affiliate authority site:
"""
[PASTE YOUR LIST OF 10 TARGET KEYWORDS HERE]
"""

For each keyword, provide a structured analysis:
1. Primary Intent Stage: Informational, Diagnostic, Comparative, Commercial Roundup, or Direct Transactional.
2. User Psychological State: What acute pain point, technical confusion, or buying doubt is the searcher trying to resolve?
3. Mandatory UI Components: Which structural components MUST be present on the page to satisfy user intent and rank on page one? (e.g., Diagnostic Flowchart, Spec Table, Pros/Cons Box, Pick Badge, Cost Calculator).
4. Affiliate Monetization Strategy: What is the appropriate CTA aggression level? (Soft contextual test kit link, category comparison table, or direct high-contrast buy button).
5. SERP Format Expectation: Does Google favor a definitive 50-word answer snippet, a structured data table, or an in-depth long-form guide?
```

### Expected Output

Gemini categorizes each query into its respective intent tier, maps user psychology, and defines the required layout elements (e.g., warning against aggressive product banners on diagnostic queries).

---

## 7. Antigravity Workflow: Building the Intent Matrix Database

Instruct Antigravity to create `data/intent_matrix.json` and a validation script `scripts/audit_intent_balance.py` to confirm your content portfolio maintains an effective ratio of informational to commercial content.

### Antigravity Steps

1. Open **Antigravity IDE**.
2. Create `data/intent_matrix.json`.
3. Create `scripts/audit_intent_balance.py` to check portfolio balance.

### Code Created by Antigravity

```python
#!/usr/bin/env python3
"""
scripts/audit_intent_balance.py - Content Portfolio Intent Auditor
ClearTapLab Engineering Standard
"""

import json
import os

MATRIX_FILE = os.path.join("data", "intent_matrix.json")

def load_matrix():
    if not os.path.exists(MATRIX_FILE):
        # Default 20-guide distribution
        sample_data = [
            {"id": "guide-01", "title": "How to Read Your CCR", "intent": "Diagnostic", "cta_style": "Soft Link"},
            {"id": "guide-02", "title": "RO vs. Carbon Filter", "intent": "Comparative", "cta_style": "Table Link"},
            {"id": "guide-03", "title": "Sulfur Smell in Well Water", "intent": "Diagnostic", "cta_style": "Test Kit Link"},
            {"id": "guide-04", "title": "Waterdrop G3P800 Review", "intent": "Transactional", "cta_style": "Buy Button"},
            {"id": "guide-08", "title": "Best RO Systems 2026", "intent": "Commercial", "cta_style": "Pick Badge"},
            {"id": "guide-12", "title": "SpringWell CF1 Review", "intent": "Transactional", "cta_style": "Buy Button"},
            {"id": "guide-13", "title": "Best Whole House Filters", "intent": "Commercial", "cta_style": "Pick Badge"}
        ]
        os.makedirs("data", exist_ok=True)
        with open(MATRIX_FILE, "w", encoding="utf-8") as f:
            json.dump(sample_data, f, indent=2)
        return sample_data

    with open(MATRIX_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def audit_intent():
    guides = load_matrix()
    counts = {}
    for g in guides:
        counts[g["intent"]] = counts.get(g["intent"], 0) + 1

    total = len(guides)
    print("\n# Content Portfolio Intent Balance Audit\n")
    print(f"Total Guides in Architecture: {total}\n")
    print("| Intent Category | Total Guides | Percentage of Portfolio | Recommended Ratio |")
    print("| :--- | :--- | :--- | :--- |")
    
    ratios = {
        "Diagnostic": "25% - 35%",
        "Comparative": "25% - 35%",
        "Commercial": "20% - 30%",
        "Transactional": "10% - 20%"
    }

    for category, count in counts.items():
        pct = (count / total) * 100.0
        rec = ratios.get(category, "N/A")
        print(f"| {category} | {count} | {pct:.1f}% | {rec} |")
    print("\n" + "="*60 + "\n")

if __name__ == "__main__":
    audit_intent()
```

---

## 8. Human Verification

Before writing an article, perform these three verification checks against the live search results:

1. **The Live SERP Layout Test:** Search your target keyword in an incognito window. Are the top 3 results comparison roundups, single reviews, or educational explainers? Your layout must match the dominant format Google is currently rewarding.
2. **The "Commercial Aggression" Sanity Check:** Read through your draft introduction. Does an affiliate button appear before the reader understands the basic problem or evaluation criteria? If yes, remove it. On informational content, affiliate links belong in contextual callouts or after diagnostic criteria are explained.
3. **The Mobile Dwell-Time Check:** Ensure that mobile readers landing on diagnostic guides immediately see a clear summary or visual diagnostic diagram without having to scroll past large promotional banners.

---

## 9. Common Mistakes

* **Treating Every Article as a "Best Of" List:** Publishing only "Best X" and "Best Y" articles. Without informational and comparative guides, a site lacks topical authority, looks like thin affiliate spam, and is vulnerable to core update penalties.
* **Aggressive Affiliate Hard-Selling on Diagnostic Queries:** Putting a glowing product endorsement with a "BUY NOW 50% OFF" button on an article explaining well water contamination chemistry.
* **Omitting Comparison Tables on Commercial Queries:** Writing 3,000 words reviewing 5 products without a side-by-side comparison table. Readers want to compare flow rates, prices, and certifications quickly.
* **Creating Cannibalizing URLs:** Publishing both *"Best Reverse Osmosis Systems"* and *"Top RO Filters"*. These target the same search intent and will compete against each other in search results, diluting your rankings.

---

## 10. Checklist

- [ ] Every keyword in my 20-page plan is mapped to a specific intent stage (Diagnostic, Comparative, Commercial, Transactional).
- [ ] My portfolio maintains a healthy balance: ~60% informational/comparative guides and ~40% commercial/transactional pages.
- [ ] Informational articles use soft contextual links and educational callouts rather than hard-sell buy buttons.
- [ ] Commercial and transactional articles feature structured comparison tables, spec boxes, and clear pick badges.
- [ ] No two planned URLs target the identical search intent.

---

## 11. Practical Exercise

1. Open your target list of 20 planned articles.
2. Classify each article into one of the 4 intent categories.
3. Run `python scripts/audit_intent_balance.py` in Antigravity to audit your intent balance.
4. If commercial articles exceed 50% of your total plan, add 3 diagnostic or technological comparison topics to strengthen your site's topical authority.
