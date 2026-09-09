# Comprehensive Audit & Cornerstone Content Analysis Report
**ClearTapLab Guides & Articles Overhaul**

- **Agent:** Explorer 1 (Articles Data & Cornerstone Content Specialist)
- **Date / Timestamp:** 2026-08-17T11:06:01Z
- **Workspace Directory:** `d:/Personal/AntiGravity/Affiliate Marketting`
- **Audit Target Files:**
  - `scripts/articles-data.js` (Current runtime master dataset)
  - `cleartaplab_batch1_cornerstone_articles.md` (Batch 1: Guides 01–05)
  - `cleartaplab_batch2_cornerstone_articles.md` (Batch 2: Guides 06–10)
  - `cleartaplab_batch3_cornerstone_articles.md` (Batch 3: Guides 11–15)
  - `cleartaplab_batch4_cornerstone_articles.md` (Batch 4: Guides 16–20)
  - Supporting: `index.html`, `scripts/app.js`, `styles/main.css`, `cleartaplab_global_styles.css`, `cleartaplab_seo_content_architecture.md`, `cleartaplab_content_hub_pages.md`

---

## Executive Summary

An exhaustive audit of `scripts/articles-data.js` against the 4 cornerstone Markdown files reveals that **all 20 guides currently in `scripts/articles-data.js` exist only as placeholder stubs or truncated summaries**. 

- **Guides 01–04:** Contain truncated introductory stubs (15 to 49 lines of HTML) missing deep-dive mechanisms, sub-sections, full comparison tables, author bylines, and complete FAQ suites.
- **Guides 05–20:** Contain single-paragraph placeholder stubs (~7 lines of HTML each), completely lacking tables, spec boxes, formulas, troubleshooting protocols, and FAQs.
- **Source Cornerstone Coverage:** Four production-grade Markdown files (`cleartaplab_batch1_cornerstone_articles.md` through `cleartaplab_batch4_cornerstone_articles.md`) contain 20 complete long-form articles (~153,500 total bytes of technical content) with rigorous first-principles engineering explanations, tables, chemical/physical formulas, and spec ratings.
- **Content Gap Analysis:** While the cornerstone Markdown files provide extensive content, several articles lack explicit 3–4 item FAQ sections (Guides 4, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 have either 0 or only 2 FAQs in source Markdown). These must be authored during conversion to satisfy the R2 acceptance criteria.
- **SPA Cross-Linking Requirement:** Internal cross-links within `contentHtml` currently use external URL slugs (e.g. `/reverse-osmosis-vs-carbon-filter/`). In the single-page application modal reader (`index.html`), these must be converted to modal-triggering Javascript actions (e.g. `<a href="javascript:void(0)" onclick="openArticleModal(2)">`) to ensure seamless in-modal navigation without breaking the application state.

---

## 1. Complete 20-Guide Status Matrix

The table below catalogs every guide across `scripts/articles-data.js`, comparing metadata, current HTML status in the codebase, and source Markdown availability.

| ID | Slug | Category | Category Label | Read Time | Badge Class | Current `contentHtml` Status | Cornerstone Source File & Lines |
|:---|:---|:---|:---|:---|:---|:---|:---|
| **01** | `how-to-read-water-quality-report` | `water-testing` | Water Testing | 8 min read | `ctl-badge-teal` | **Truncated Stub** (49 lines; missing Sec 3 & 4, FAQs, Byline) | `batch1` (lines 10–158) |
| **02** | `reverse-osmosis-vs-carbon-filter` | `filtration-technology` | Filtration Science | 10 min read | `ctl-badge-pill` | **Truncated Stub** (20 lines; 1 table only, missing deep dives) | `batch1` (lines 159–345) |
| **03** | `fix-sulfur-smell-well-water` | `water-problems` | Water Problems | 9 min read | `ctl-badge-warning` | **Truncated Stub** (15 lines; summary box only, missing chemistry) | `batch1` (lines 346–483) |
| **04** | `waterdrop-g3p800-review` | `reverse-osmosis` | Reverse Osmosis | 12 min read | `ctl-badge-pill` | **Truncated Stub** (15 lines; verdict card only, missing TCO table) | `batch1` (lines 484–630) |
| **05** | `hard-water-gpg-ppm-guide` | `water-problems` | Water Problems | 8 min read | `ctl-badge-warning` | **Single-Paragraph Stub** (7 lines; missing formulas & tables) | `batch1` (lines 632–798) |
| **06** | `remove-iron-from-well-water` | `water-problems` | Water Problems | 11 min read | `ctl-badge-warning` | **Single-Paragraph Stub** (7 lines; missing 4 forms & AIO) | `batch2` (lines 10–170) |
| **07** | `water-softener-vs-salt-free` | `system-guides` | System Guides | 10 min read | `ctl-badge-dark` | **Single-Paragraph Stub** (7 lines; missing TAC physics) | `batch2` (lines 171–347) |
| **08** | `best-reverse-osmosis-systems` | `reverse-osmosis` | Reverse Osmosis | 14 min read | `ctl-badge-pill` | **Single-Paragraph Stub** (7 lines; missing benchmark tables) | `batch2` (lines 349–494) |
| **09** | `filter-pitchers-pfas-removal` | `filtration-technology` | Filtration Science | 9 min read | `ctl-badge-pill` | **Single-Paragraph Stub** (7 lines; missing C-F bond & tests) | `batch2` (lines 496–629) |
| **10** | `reverse-osmosis-water-waste` | `reverse-osmosis` | Reverse Osmosis | 8 min read | `ctl-badge-pill` | **Single-Paragraph Stub** (7 lines; missing recovery ratio tables) | `batch2` (lines 631–767) |
| **11** | `tankless-vs-tank-reverse-osmosis` | `reverse-osmosis` | Reverse Osmosis | 10 min read | `ctl-badge-pill` | **Single-Paragraph Stub** (7 lines; missing booster pump math) | `batch3` (lines 10–172) |
| **12** | `springwell-cf1-review` | `system-guides` | System Guides | 11 min read | `ctl-badge-dark` | **Single-Paragraph Stub** (7 lines; missing 4-stage breakdown) | `batch3` (lines 174–333) |
| **13** | `best-whole-house-water-filters` | `system-guides` | System Guides | 13 min read | `ctl-badge-dark` | **Single-Paragraph Stub** (7 lines; missing GPM sizing formula) | `batch3` (lines 335–456) |
| **14** | `best-water-test-kits` | `water-testing` | Water Testing | 9 min read | `ctl-badge-teal` | **Single-Paragraph Stub** (7 lines; missing ICP-MS lab comparisons) | `batch3` (lines 458–573) |
| **15** | `remineralization-reverse-osmosis-filter` | `reverse-osmosis` | Reverse Osmosis | 8 min read | `ctl-badge-pill` | **Single-Paragraph Stub** (7 lines; missing carbonic acid kinetics) | `batch3` (lines 575–667) |
| **16** | `how-to-size-water-softener` | `system-guides` | System Guides | 10 min read | `ctl-badge-dark` | **Single-Paragraph Stub** (7 lines; missing master sizing matrix) | `batch4` (lines 10–155) |
| **17** | `best-salt-free-water-conditioners` | `system-guides` | System Guides | 11 min read | `ctl-badge-dark` | **Single-Paragraph Stub** (7 lines; missing DVGW W-512 data) | `batch4` (lines 157–280) |
| **18** | `sediment-vs-carbon-filters` | `filtration-technology` | Filtration Science | 8 min read | `ctl-badge-pill` | **Single-Paragraph Stub** (7 lines; missing step-down micron rules) | `batch4` (lines 282–400) |
| **19** | `fluoride-removal-water` | `filtration-technology` | Filtration Science | 9 min read | `ctl-badge-pill` | **Single-Paragraph Stub** (7 lines; missing 3 proven methods) | `batch4` (lines 402–509) |
| **20** | `whole-house-filter-water-pressure` | `system-guides` | System Guides | 10 min read | `ctl-badge-dark` | **Single-Paragraph Stub** (7 lines; missing Ergun equation & Delta P) | `batch4` (lines 511–622) |

---

## 2. Detailed Audit of Required Components (Guides 01–20)

Every production engineering article must fulfill all 10 core structural requirements set forth in `ORIGINAL_REQUEST.md`. Below is the guide-by-guide audit of component readiness:

```
Component Key:
[H] Header Badge & H1 Title
[S] Scientific Overview & First-Principles Mechanisms
[T] Technical Comparison Table (.ctl-table-wrapper)
[B] Engineering Specification Callout Box (.ctl-spec-box)
[M] Practical Testing & Troubleshooting Methodologies
[F] Formulas / Chemical Equations / Lifetime TCO Sizing
[Q] 3–4 Comprehensive FAQ Items with Technical Answers
[E] Editorial Author Byline (.ctl-author-box)
[L] Related Internal Guide Links (SPA modal triggers)
```

### Batch 1: Guides 01–05 Audit

#### Guide 01: How to Read Your City CCR Water Quality Report: An Engineer’s Guide
- **Slug:** `how-to-read-water-quality-report` | **Category:** `water-testing`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Diagnostic Engineering Guide", H1: "How to Read Your City CCR Water Quality Report: An Engineer’s Guide"
  - `[S]` **Ready in MD:** SDWA regulatory limits vs. biological safety; municipal treatment scale constraints; distribution line leaching.
  - `[T]` **Ready in MD:** 4 Contaminant Categories Table (Lead/Copper, TTHMs/HAAs, PFAS, Nitrates) with MCL, ideal target, and mechanical fix.
  - `[B]` **Ready in MD:** Executive Summary Box (MCL, MCLG, Action Levels, PPM vs PPB).
  - `[M]` **Ready in MD:** Disinfectant Residual Audit (Free Chlorine vs. Chloramines); 3 Common Homeowner CCR Mistakes.
  - `[F]` **Ready in MD:** PPM vs PPB conversion ($1\text{ mg/L}$, $1\ \mu\text{g/L}$, $1\text{ ng/L}$); Hardness calculation formula ($\text{PPM} \div 17.1 = \text{GPG}$).
  - `[Q]` **Needs Expansion:** Source MD has 3 FAQs (Where to find CCR, Private well applicability, Lead leaching sampling). Add 1 extra FAQ: *"What is the difference between Primary and Secondary EPA standards?"*
  - `[E]` **Ready in MD:** Author box for ClearTapLab Engineering Team.
  - `[L]` **Action Required:** Link to `openArticleModal(2)` (RO vs Carbon) and `openArticleModal(14)` (Mail-in test kits).

#### Guide 02: Reverse Osmosis vs. Carbon Filters: The Physics Explained
- **Slug:** `reverse-osmosis-vs-carbon-filter` | **Category:** `filtration-technology`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Filtration Science Deep-Dive", H1: "Reverse Osmosis vs. Carbon Filters: The Physics Explained"
  - `[S]` **Ready in MD:** Van der Waals adsorption in carbon lattices ($900^\circ\text{C}$ steam activation) vs. cross-flow polyamide membrane flux (0.0001 µm pores).
  - `[T]` **Ready in MD:** Side-by-side engineering metric table (Pore cutoff, TDS reduction, Lead, PFAS, Flow rate, Wastewater, 5-Yr Cost).
  - `[B]` **Ready in MD:** 10-Second Engineering Distinction Callout Box.
  - `[M]` **Ready in MD:** Multi-stage sequential placement (why carbon pre-filter is required before RO membrane).
  - `[F]` **Ready in MD:** Molecular size comparison ($H_2O$ 0.00028 µm vs RO pore 0.0001 µm); 5-Year Operating Cost calculations ($250 vs $750–$1,200).
  - `[Q]` **Needs Expansion:** Source MD has 2 FAQs (Mineral removal, Fluoride removal). Add 2 extra FAQs: *"Does a carbon filter reduce water pressure?"* and *"Can a carbon filter remove microplastics?"*
  - `[E]` **Ready in MD:** Author box for Mechanical Engineers & Fluid Dynamics Specialists.
  - `[L]` **Action Required:** Link to `openArticleModal(4)` (G3P800 review), `openArticleModal(10)` (RO water waste), and `openArticleModal(18)` (Sediment vs Carbon).

#### Guide 03: How to Fix Rotten Egg Sulfur Smell in Well Water
- **Slug:** `fix-sulfur-smell-well-water` | **Category:** `water-problems`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Problem-Solving Guide", H1: "How to Fix Rotten Egg Sulfur Smell in Well Water: An Engineer’s Guide"
  - `[S]` **Ready in MD:** Hydrogen sulfide ($H_2S$) generation via Sulfur-Reducing Bacteria (SRB) in aquifers and galvanic anode rod reactions in hot water tanks.
  - `[T]` **Ready in MD:** 4 Treatment Technologies Table (AIO, Catalytic Carbon, Chemical Feed, Powered Anode Rod) with Max PPM, consumables, maintenance, cost.
  - `[B]` **Ready in MD:** 60-Second Hot vs. Cold Water Isolation Diagnostic Callout Box.
  - `[M]` **Ready in MD:** AIO aeration physics (4-step sequence) and 3 costly mistakes (softener resin fouling, standard carbon saturation, pH sensitivity).
  - `[F]` **Ready in MD:** Chemical redox reactions: $\text{Organic Matter} + SO_4^{2-} \xrightarrow{\text{SRB}} S^{2-} + H_2O + CO_2 \xrightarrow{H^+} H_2S\uparrow$ and $2H_2S + O_2 \longrightarrow 2S^0\downarrow + 2H_2O$.
  - `[Q]` **Needs Expansion:** Source MD has 2 FAQs (Health risk, Testing methodology). Add 2 extra FAQs: *"Why did my water softener fail to remove the sulfur smell?"* and *"Will shock chlorination permanently fix sulfur in a well?"*
  - `[E]` **Ready in MD:** Author box for Groundwater Chemistry Specialists.
  - `[L]` **Action Required:** Link to `openArticleModal(6)` (Iron removal), `openArticleModal(14)` (Mail-in test kits), and `openArticleModal(13)` (Whole-house filters).

#### Guide 04: Waterdrop G3P800 Engineering Review: 6-Month Benchmark Audit
- **Slug:** `waterdrop-g3p800-review` | **Category:** `reverse-osmosis`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "In-Depth Engineering Review", H1: "Waterdrop G3P800 Engineering Review: 6-Month Benchmark Audit"
  - `[S]` **Ready in MD:** High-flow 800 GPD composite membrane physics, DC booster pump dynamics, Fick's first law of diffusion (TDS creep mechanism).
  - `[T]` **Ready in MD:** Manufacturer Claim vs. Measured Benchmark Table; 5-Year Lifetime TCO Table ($1,189 total / $0.65/day).
  - `[B]` **Ready in MD:** ClearTapLab Verdict Card with `.ctl-spec-grid` (0.55 GPM, 2.4:1 ratio, 58 dB noise, NSF 58/372/42).
  - `[M]` **Ready in MD:** Morning TDS flush protocol; Filter replacement twist-and-pull audit; Noise level isolation testing.
  - `[F]` **Ready in MD:** Real-world flow rate math (0.55 GPM = 6.5 sec per 8 oz); 5-Year TCO line items.
  - `[Q]` **Needs Authoring:** Source MD lacks FAQs. Author 4 technical FAQs:
    1. *"How do you resolve the initial morning TDS creep on the G3P800?"*
    2. *"Can the Waterdrop G3P800 be connected to a refrigerator ice maker?"*
    3. *"What happens to water dispensing during a power outage?"*
    4. *"How does the automated 20-second membrane flush cycle work?"*
  - `[E]` **Needs Addition:** Embed `.ctl-author-box` with Editorial Team credentials.
  - `[L]` **Action Required:** Link to `openArticleModal(11)` (Tankless vs Tank) and `openArticleModal(10)` (RO Water Waste).

#### Guide 05: What Is Hard Water? GPG vs. PPM Calculation & Sizing Guide
- **Slug:** `hard-water-gpg-ppm-guide` | **Category:** `water-problems`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Engineering Sizing Calculator", H1: "What Is Hard Water? GPG vs. PPM Calculation & Sizing Guide"
  - `[S]` **Ready in MD:** Multivalent dissolved metallic cations ($Ca^{2+}, Mg^{2+}$); Thermal decomposition of calcium bicarbonate into insoluble scale ($CaCO_3$); 24% thermal energy transfer loss.
  - `[T]` **Ready in MD:** Water Quality Association (WQA) Hardness Scale Table; Household Grain Sizing Reference Matrix.
  - `[B]` **Ready in MD:** Master Hardness Conversion Formula Box ($1\text{ GPG} = 17.118\text{ PPM}$).
  - `[M]` **Ready in MD:** 4-Step Sizing Procedure (Daily usage, Compensated hardness with iron, Daily grains, 7-day regeneration cadence).
  - `[F]` **Ready in MD:** Scale formation reaction: $Ca(HCO_3)_2 \xrightarrow{\Delta} CaCO_3\downarrow + H_2O + CO_2$; Compensated hardness formula.
  - `[Q]` **Needs Expansion:** Source MD has 2 FAQs (Hair/skin effects, Sodium content). Add 2 extra FAQs: *"What is the difference between temporary and permanent hardness?"* and *"Why can't a handheld TDS meter measure water hardness accurately?"*
  - `[E]` **Ready in MD:** Author box for Water Treatment Sizing Specialists.
  - `[L]` **Action Required:** Link to `openArticleModal(16)` (Water softener sizing) and `openArticleModal(7)` (Softener vs Salt-free).

---

### Batch 2: Guides 06–10 Audit

#### Guide 06: How to Remove Iron from Well Water: The Complete Engineer’s Guide
- **Slug:** `remove-iron-from-well-water` | **Category:** `water-problems`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Problem-Solving Diagnostic Guide", H1: "How to Remove Iron from Well Water: The Complete Engineer’s Guide"
  - `[S]` **Ready in MD:** Redox chemistry of 4 iron species (Ferrous $Fe^{2+}$, Ferric $Fe^{3+}$, Bacterial slime, Colloidal/chelated tannins); pH dependency (> 6.8).
  - `[T]` **Ready in MD:** The 4 Chemical Forms of Iron Matrix; Treatment Systems Comparison Table (AIO, Greensand Plus, Chlorine/Peroxide, Softener).
  - `[B]` **Ready in MD:** Executive Summary Warning Box (EPA 0.3 PPM limit, standard filter pore bypass).
  - `[M]` **Ready in MD:** Air-Injection Oxidation (AIO) aeration mechanics; Well pump GPM backwash verification; 3 installation pitfalls.
  - `[F]` **Ready in MD:** Iron oxidation redox formula: $4Fe^{2+} + O_2 + 10H_2O \longrightarrow 4Fe(OH)_3\downarrow + 8H^+$.
  - `[Q]` **Needs Expansion:** Source MD has 2 FAQs (RO for iron, Testing for iron). Add 2 extra FAQs: *"Will a water softener resin bed be damaged by ferrous iron?"* and *"How do you treat iron bacteria in a well casing?"*
  - `[E]` **Ready in MD:** Author box for Groundwater Chemistry Specialists.
  - `[L]` **Action Required:** Link to `openArticleModal(3)` (Sulfur smell), `openArticleModal(14)` (Mail-in test kits), and `openArticleModal(13)` (Whole house filters).

#### Guide 07: Water Softeners vs. Salt-Free TAC Conditioners: Which Do You Actually Need?
- **Slug:** `water-softener-vs-salt-free` | **Category:** `system-guides`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "System Sizing & Comparison", H1: "Water Softeners vs. Salt-Free TAC Conditioners: Which Do You Actually Need?"
  - `[S]` **Ready in MD:** Polystyrene cation-exchange resin kinetics vs. Template Assisted Crystallization (TAC) nucleation kinetics and crystal morphology modification.
  - `[T]` **Ready in MD:** Head-to-Head Comparison Table (Mechanism, Hardness Removal, Scale Prevention %, Consumables, Wastewater, Electricity, Cost).
  - `[B]` **Ready in MD:** 10-Second Engineering Distinction Callout Box.
  - `[M]` **Ready in MD:** TAC chemical boundaries audit (Iron < 0.3 PPM, Manganese < 0.05 PPM, Copper < 1.3 PPM, H2S = 0 PPM).
  - `[F]` **Ready in MD:** TAC nucleation reaction: $Ca^{2+} + 2HCO_3^- \xrightarrow{\text{TAC}} CaCO_3\text{ (Micro-Crystal)} + H_2O + CO_2$.
  - `[Q]` **Needs Authoring:** Source MD lacks explicit FAQs. Author 4 technical FAQs:
    1. *"Does a salt-free TAC conditioner make water feel slippery like a water softener?"*
    2. *"Can TAC technology protect tankless water heater warranty requirements?"*
    3. *"Will a salt-free conditioner remove existing limescale buildup in older pipes?"*
    4. *"What happens if water containing dissolved iron passes through a TAC system?"*
  - `[E]` **Ready in MD:** Author box for Mechanical Engineering Editorial Team.
  - `[L]` **Action Required:** Link to `openArticleModal(16)` (Softener sizing) and `openArticleModal(17)` (Best salt-free conditioners).

#### Guide 08: Best Reverse Osmosis Systems of 2026: An Engineer’s Benchmark Audit
- **Slug:** `best-reverse-osmosis-systems` | **Category:** `reverse-osmosis`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Buyer's Engineering Guide", H1: "Best Reverse Osmosis Systems of 2026: An Engineer’s Benchmark Audit"
  - `[S]` **Ready in MD:** 5 Evaluation benchmarks: Flow rate (GPM), Pure-to-drain recovery, NSF certification registry audits (NSF 58, 53, 372, 401, P473), membrane longevity, 5-yr TCO.
  - `[T]` **Ready in MD:** System Comparison Benchmark Table (Waterdrop G3P800, Home Master TMAFC, APEC ROES-50, AquaTru Countertop).
  - `[B]` **Ready in MD:** ClearTapLab 2026 Benchmark Verdict Card.
  - `[M]` **Ready in MD:** Decision Tree Framework (Under-sink 110V power, tank volume space, zero-plumbing countertop).
  - `[F]` **Ready in MD:** 5-Year Operating TCO estimates ($540 to $1,189); Recovery ratio calculations (1:3 to 4:1).
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"Which NSF certification guarantees the removal of PFAS forever chemicals?"*
    2. *"How often should under-sink pre-filters be replaced compared to the RO membrane?"*
    3. *"Can an under-sink RO system supply sufficient pressure for a refrigerator dispenser?"*
    4. *"Is a tankless RO system more prone to bacterial growth than a tank system?"*
  - `[E]` **Needs Addition:** Author box for Water Treatment Research Team.
  - `[L]` **Action Required:** Link to `openArticleModal(4)` (G3P800 review), `openArticleModal(11)` (Tankless vs Tank), and `openArticleModal(15)` (Remineralization).

#### Guide 09: Do Water Filter Pitchers Remove PFAS Forever Chemicals? NSF 53 & P473 Tested
- **Slug:** `filter-pitchers-pfas-removal` | **Category:** `filtration-technology`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Contaminant Investigation", H1: "Do Water Filter Pitchers Remove PFAS Forever Chemicals? NSF 53 & P473 Tested"
  - `[S]` **Ready in MD:** Carbon-Fluorine bond chemistry ($485\text{ kJ/mol}$ bond energy); Loose GAC water channeling vs. solid extruded catalytic carbon blocks.
  - `[T]` **Ready in MD:** Certified Pitcher Comparison Table (Clearly Filtered, ZeroWater, Epic Pure, Brita Standard, Brita Elite) with NSF standards, tested PFAS reduction %, filter lifespan.
  - `[B]` **Ready in MD:** Executive Takeaway Warning Box (Standard GAC < 30% vs. Extruded Block 98%+).
  - `[M]` **Ready in MD:** 3 Critical Pitcher Pitfalls (Water channeling, short-chain PFAS mobility like GenX/PFBS, high cost-per-gallon economics).
  - `[F]` **Ready in MD:** EPA 4.0 PPT regulatory limit; Cost-per-gallon analysis ($0.25–$0.45/gal pitcher vs $0.06/gal RO).
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"Does boiling tap water remove PFAS forever chemicals?"*
    2. *"Why does the standard Brita white pitcher filter fail to remove PFAS?"*
    3. *"How does ZeroWater achieve 99% PFAS reduction while reducing TDS to 0?"*
    4. *"How do short-chain PFAS compounds differ from legacy PFOA/PFOS during filtration?"*
  - `[E]` **Ready in MD:** Author box for Environmental Chemistry Researchers.
  - `[L]` **Action Required:** Link to `openArticleModal(2)` (RO vs Carbon) and `openArticleModal(14)` (Mail-in test kits).

#### Guide 10: How Much Water Does Reverse Osmosis Waste? Recovery Ratios Explained
- **Slug:** `reverse-osmosis-water-waste` | **Category:** `reverse-osmosis`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Membrane Physics & Efficiency", H1: "How Much Water Does Reverse Osmosis Waste? Recovery Ratios Explained"
  - `[S]` **Ready in MD:** Dead-end filtration vs. Cross-flow membrane separation; Concentration polarization physics; Polyamide pore flux kinetics.
  - `[T]` **Ready in MD:** Pure-to-Drain Efficiency Matrix across 4 architectures (Traditional Tank, Tank + Permeate Pump, Modern Tankless, High-Efficiency G3P800).
  - `[B]` **Ready in MD:** Executive Summary Callout Box (Why RO requires a brine sweep; real utility cost calculation).
  - `[M]` **Ready in MD:** DC booster pumps vs. non-electric permeate pump retrofits; 3 strategies to repurpose brine concentrate.
  - `[F]` **Ready in MD:** Annual wastewater volume and utility bill calculation ($2.50 to $5.00/yr based on 2,190 gallons).
  - `[Q]` **Needs Expansion:** Source MD has 2 FAQs (Brine on garden plants, Low feed pressure impact). Add 2 extra FAQs: *"Can you install a permeate pump on any standard RO system?"* and *"What is the difference between recovery ratio and rejection rate?"*
  - `[E]` **Ready in MD:** Author box for Fluid Dynamics Specialists.
  - `[L]` **Action Required:** Link to `openArticleModal(4)` (G3P800 review) and `openArticleModal(11)` (Tankless vs Tank).

---

### Batch 3: Guides 11–15 Audit

#### Guide 11: Tankless vs. Tank Reverse Osmosis Systems: An Engineer’s Breakdown
- **Slug:** `tankless-vs-tank-reverse-osmosis` | **Category:** `reverse-osmosis`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "System Architecture Comparison", H1: "Tankless vs. Tank Reverse Osmosis Systems: An Engineer’s Breakdown"
  - `[S]` **Ready in MD:** Net driving pressure ($\Delta P$) dynamics; Storage bladder backpressure ($5\rightarrow 35\text{ PSI}$); Fick's first law of diffusion (TDS Creep).
  - `[T]` **Ready in MD:** Head-to-Head Architecture Table; 5-Year Lifetime TCO Table ($415 vs $1,201).
  - `[B]` **Ready in MD:** 10-Second Engineering Distinction Callout Box.
  - `[M]` **Ready in MD:** Morning TDS purge protocol; Under-sink space allocation (0.6 sq ft vs 2.0 sq ft); Electrical outlet requirement.
  - `[F]` **Ready in MD:** TCO math ($0.23/day vs $0.66/day); Pure-to-drain wastewater ratios (1:4 vs 2.5:1).
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"How loud is the internal booster pump on a tankless RO system?"*
    2. *"Can a tankless RO system supply a refrigerator water dispenser and ice maker?"*
    3. *"Why does water flow from a tank RO system slow down as the tank empties?"*
    4. *"Do tankless RO systems have a higher risk of membrane fouling?"*
  - `[E]` **Ready in MD:** Author box for Membrane Physics Research Team.
  - `[L]` **Action Required:** Link to `openArticleModal(4)` (G3P800 review) and `openArticleModal(8)` (Best RO systems).

#### Guide 12: SpringWell CF1 Whole-House Water Filter Review: An Engineer’s 1-Year Benchmark
- **Slug:** `springwell-cf1-review` | **Category:** `system-guides`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "System Benchmark Review", H1: "SpringWell CF1 Whole-House Water Filter Review: An Engineer’s 1-Year Benchmark"
  - `[S]` **Ready in MD:** 4-Stage sequential upflow architecture (5µm sediment, KDF-55 redox alloy, Catalytic coconut carbon, sub-micron post-filter); Empty Bed Contact Time (EBCT).
  - `[T]` **Ready in MD:** Performance Benchmark Table (Free Chlorine, Chloramines, Lead/Heavy metals, Flow Rate, $\Delta P$ Pressure Drop); 10-Year TCO Table ($1,550 total / $0.42/day).
  - `[B]` **Ready in MD:** ClearTapLab Benchmark Verdict Card with `.ctl-spec-grid` (9.0 GPM, 1,000,000 gal, < 2.5 PSI $\Delta P$).
  - `[M]` **Ready in MD:** Upflow fluidization inspection; Pre-filter differential pressure monitoring; Long-term disinfectant breakthrough testing.
  - `[F]` **Ready in MD:** 1,000,000 gallon capacity timeline; 10-Year replacement economics.
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"Does the SpringWell CF1 soften hard water or remove limescale?"*
    2. *"How often do you need to replace the central KDF and carbon tank media?"*
    3. *"Can the SpringWell CF1 be installed on private well water?"*
    4. *"Will installing the SpringWell CF1 cause a noticeable drop in shower pressure?"*
  - `[E]` **Needs Addition:** Author box for Whole-House Engineering Research Team.
  - `[L]` **Action Required:** Link to `openArticleModal(13)` (Best whole-house filters) and `openArticleModal(20)` (Pressure drop analysis).

#### Guide 13: Best Whole-House Water Filters of 2026: Sizing & Sieve Analysis
- **Slug:** `best-whole-house-water-filters` | **Category:** `system-guides`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Buyer's Sizing Blueprint", H1: "Best Whole-House Water Filters of 2026: Sizing & Sieve Analysis"
  - `[S]` **Ready in MD:** Peak simultaneous fixture demand; Empty Bed Contact Time (EBCT); Cartridge systems vs. Central upflow media tanks.
  - `[T]` **Ready in MD:** System Comparison Table (SpringWell CF1, Express Water 3-Stage, SpringWell WS1 AIO, Aquasana Rhino).
  - `[B]` **Ready in MD:** ClearTapLab 2026 Whole-House Benchmark Verdict Card.
  - `[M]` **Ready in MD:** Peak Household GPM Sizing Calculation (Fixture load calculation + 25% safety reserve).
  - `[F]` **Ready in MD:** Peak Flow Demand Formula: $(\text{Showers} \times 2.5) + (\text{Kitchen} \times 2.0) \times 1.25 = \text{Target GPM}$; 10-Year TCO calculations ($1,550 to $2,100).
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"Does a whole-house water filter eliminate the need for an under-sink RO system?"*
    2. *"What port diameter should I choose for my whole-house filter (3/4" vs 1")?"*
    3. *"Can a whole-house carbon filter remove fluoride or dissolved minerals?"*
    4. *"What is the maintenance difference between Big Blue cartridges and central media tanks?"*
  - `[E]` **Needs Addition:** Author box for Plumbing Systems Engineering Team.
  - `[L]` **Action Required:** Link to `openArticleModal(12)` (SpringWell CF1), `openArticleModal(18)` (Sediment vs Carbon), and `openArticleModal(20)` (Pressure drop).

#### Guide 14: Best Mail-In Water Test Kits of 2026: EPA Lab Accuracy Compared
- **Slug:** `best-water-test-kits` | **Category:** `water-testing`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Diagnostic Lab Comparison", H1: "Best Mail-In Water Test Kits of 2026: EPA Lab Accuracy Compared"
  - `[S]` **Ready in MD:** Inductively Coupled Plasma Mass Spectrometry (ICP-MS, 0.001 PPB precision); Gas Chromatography-Mass Spectrometry (GC-MS); Certified microbial incubation.
  - `[T]` **Ready in MD:** Test Kit Comparison Table (Tap Score Advanced City, Tap Score Essential Well, NTL WaterCheck Deluxe, Varify 17-in-1 Strips).
  - `[B]` **Ready in MD:** ClearTapLab 2026 Water Test Kit Benchmark Verdict Card.
  - `[M]` **Ready in MD:** Homeowner testing cadence guidelines (Annual private well testing, home acquisition, taste/odor shifts, pipe main repairs).
  - `[F]` **Ready in MD:** Parts-Per-Billion ($1\ \mu\text{g/L}$) vs. Parts-Per-Trillion ($1\text{ ng/L}$) analytical limits.
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"How do I properly collect a 'first-draw' water sample for lead testing?"*
    2. *"Why can't inexpensive paper test strips detect lead or PFAS?"*
    3. *"How long does it take to receive results from an EPA mail-in water laboratory?"*
    4. *"How often should private well owners test their water supply?"*
  - `[E]` **Ready in MD:** Author box for Environmental Analysis & Diagnostics Team.
  - `[L]` **Action Required:** Link to `openArticleModal(1)` (CCR guide) and `openArticleModal(3)` (Sulfur smell).

#### Guide 15: Remineralization RO Filters: Do You Need an Alkaline Post-Filter?
- **Slug:** `remineralization-reverse-osmosis-filter` | **Category:** `reverse-osmosis`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Water Chemistry & Health", H1: "Remineralization RO Filters: Do You Need an Alkaline Post-Filter?"
  - `[S]` **Ready in MD:** Loss of bicarbonate buffering capacity; Atmospheric $CO_2$ absorption forming weak carbonic acid ($H_2CO_3$, pH 6.0–6.5); Calcite ($CaCO_3$) and Corosex ($MgO$) dissolution chemistry.
  - `[T]` **Needs Structuring in HTML:** Create a comparison table of Remineralization Media (Calcite, Corosex, Maifan Stone, Bio-Ceramics) across pH range, TDS addition (PPM), lifespan, and target application.
  - `[B]` **Ready in MD:** Executive Summary Callout Box (Why RO water is slightly acidic).
  - `[M]` **Ready in MD:** Specialty Coffee Association (SCA) extraction parameters; Copper pipe corrosion prevention (pH > 7.5).
  - `[F]` **Ready in MD:** Carbonic acid equilibrium formula: $H_2O + CO_2 \rightleftharpoons H_2CO_3 \rightleftharpoons H^+ + HCO_3^-$; SCA TDS target (75–150 PPM).
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"Does drinking slightly acidic RO water leach minerals from bones or teeth?"*
    2. *"How often do remineralization post-filter cartridges need to be replaced?"*
    3. *"Will an alkaline remineralization filter add limescale back into a tea kettle?"*
    4. *"Can you add a remineralization filter to an existing reverse osmosis system?"*
  - `[E]` **Ready in MD:** Author box for Water Chemistry Research Team.
  - `[L]` **Action Required:** Link to `openArticleModal(2)` (RO vs Carbon) and `openArticleModal(8)` (Best RO systems).

---

### Batch 4: Guides 16–20 Audit

#### Guide 16: How to Size a Water Softener: The Step-by-Step Engineering Formula
- **Slug:** `how-to-size-water-softener` | **Category:** `system-guides`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Engineering Sizing Blueprint", H1: "How to Size a Water Softener: The Step-by-Step Engineering Formula"
  - `[S]` **Ready in MD:** Cation resin volume ($cu\ ft$) regeneration kinetics; Undersizing water/salt waste vs. Oversizing resin channeling and bacterial growth.
  - `[T]` **Ready in MD:** Master Household Sizing Reference Matrix (1–2, 3–4, 5–6, 7+ people across Moderate, Hard, Very Hard, Severe Well hardness).
  - `[B]` **Ready in MD:** Master Sizing Equation at a Glance Callout Box.
  - `[M]` **Ready in MD:** 4-Step Sizing Procedure; Control valve port diameter sizing (3/4", 1", 1.25" NPT); 3 costly sizing pitfalls.
  - `[F]` **Ready in MD:** Master Equation: $(\text{People} \times 75\text{ GPD} \times \text{Compensated Hardness GPG} \times 7\text{ Days}) \times 1.25$; Iron compensation formula.
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"What is the difference between nominal grain rating and operational salt efficiency?"*
    2. *"How much salt should a properly sized 48,000 grain water softener consume per month?"*
    3. *"What is a metered Demand-Initiated Regeneration (DIR) valve?"*
    4. *"Do I need a dual-tank alternating water softener for a residential home?"*
  - `[E]` **Ready in MD:** Author box for Sizing & Thermodynamics Team.
  - `[L]` **Action Required:** Link to `#calculator` and `openArticleModal(5)` (Hard water guide).

#### Guide 17: Best Salt-Free Water Conditioners of 2026: TAC Scale Prevention Benchmark
- **Slug:** `best-salt-free-water-conditioners` | **Category:** `system-guides`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Buyer's Engineering Guide", H1: "Best Salt-Free Water Conditioners of 2026: TAC Scale Prevention Benchmark"
  - `[S]` **Ready in MD:** Template Assisted Crystallization (TAC) nucleation mechanics; DVGW W-512 testing certification; Ineffective magnetic/electronic descaler physics.
  - `[T]` **Ready in MD:** System Comparison Table (SpringWell FS1, Kind Water E-2000, Aquasana SimplySoft, SoftPro Salt-Free).
  - `[B]` **Ready in MD:** ClearTapLab 2026 Salt-Free Conditioner Verdict Card.
  - `[M]` **Ready in MD:** Water Chemistry Pre-Purchase Audit (Iron < 0.3 PPM, Manganese < 0.05 PPM, Copper < 1.3 PPM, H2S = 0 PPM).
  - `[F]` **Ready in MD:** TAC reaction equation: $Ca^{2+} + 2HCO_3^- \xrightarrow{\text{TAC}} CaCO_3 + H_2O + CO_2$; 5-Year TCO estimates ($1,100 to $1,850).
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"Can a salt-free TAC conditioner protect a tankless water heater warranty?"*
    2. *"Why do magnetic and electronic wire-wrap descalers fail independent testing?"*
    3. *"Can I install a salt-free TAC conditioner on well water with high iron?"*
    4. *"How do you test if a salt-free conditioner is working if a hardness test still shows hard water?"*
  - `[E]` **Needs Addition:** Author box for Water Treatment Research Team.
  - `[L]` **Action Required:** Link to `openArticleModal(7)` (Softener vs Salt-free) and `openArticleModal(16)` (Softener sizing).

#### Guide 18: Sediment vs. Carbon Filters: Micron Ratings & Placement Sequence Explained
- **Slug:** `sediment-vs-carbon-filters` | **Category:** `filtration-technology`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Plumbing Physics Fundamentals", H1: "Sediment vs. Carbon Filters: Micron Ratings & Placement Sequence Explained"
  - `[S]` **Ready in MD:** Mechanical sieving (size exclusion) vs. Chemical adsorption (Van der Waals forces); Pore blinding and carbon exhaustion kinetics when sequence is inverted.
  - `[T]` **Ready in MD:** Side-by-Side Comparison Table (Primary function, Pore size range, Effect on dissolved minerals, $\Delta P$, Lifespan, Cost).
  - `[B]` **Ready in MD:** The Golden Rule of Filter Placement Sequence Callout Box.
  - `[M]` **Ready in MD:** Step-Down Micron Sizing Strategy (Stage 1: 20–50µm, Stage 2: 5µm, Stage 3: 0.5–5µm extruded block).
  - `[F]` **Ready in MD:** Step-down micron rating sequence; Pressure loss thresholds ($\Delta P < 1\text{ PSI}$ vs $1–3\text{ PSI}$).
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"Can you wash and reuse sediment filter cartridges?"*
    2. *"What happens if you accidentally install a carbon filter before a sediment filter?"*
    3. *"What is the difference between melt-blown spun and pleated polyester sediment filters?"*
    4. *"How do you know when an extruded carbon block filter is fully exhausted?"*
  - `[E]` **Ready in MD:** Author box for Fluid Filtration Research Team.
  - `[L]` **Action Required:** Link to `openArticleModal(2)` (RO vs Carbon) and `openArticleModal(20)` (Pressure drop).

#### Guide 19: Fluoride Removal Methods for Tap Water: RO vs. Activated Alumina vs. Distillation
- **Slug:** `fluoride-removal-water` | **Category:** `filtration-technology`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Contaminant Elimination", H1: "Fluoride Removal Methods for Tap Water: RO vs. Activated Alumina vs. Distillation"
  - `[S]` **Ready in MD:** Microscopic ionic dimensions of fluoride ion ($F^-$: 0.00026 µm / 0.26 nm) vs. activated carbon pores (0.5–5.0 µm); Why standard carbon pitchers fail completely.
  - `[T]` **Ready in MD:** Head-to-Head Comparison Table (RO vs. Activated Alumina vs. Thermal Distiller across Rejection %, Flow Rate, pH Sensitivity, Cost).
  - `[B]` **Ready in MD:** Executive Summary Callout Box (The 3 Proven Methods Compared).
  - `[M]` **Ready in MD:** Activated Alumina strict pH boundary (requires pH < 7.5); Engineering decision protocol.
  - `[F]` **Ready in MD:** Municipal target concentration ($0.7\text{ PPM}$); Fluoride ion diameter comparison.
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"Do standard refrigerator water filters or shower filters remove fluoride?"*
    2. *"Does boiling municipal tap water remove fluoride?"*
    3. *"Is activated alumina filter media safe, or will it leach aluminum into drinking water?"*
    4. *"Why does reverse osmosis achieve 90%+ fluoride rejection despite the small ion size?"*
  - `[E]` **Ready in MD:** Author box for Drinking Water Diagnostics Team.
  - `[L]` **Action Required:** Link to `openArticleModal(2)` (RO vs Carbon) and `openArticleModal(8)` (Best RO systems).

#### Guide 20: Do Whole-House Water Filters Reduce Water Pressure? Friction Loss & Head Loss Analysis
- **Slug:** `whole-house-filter-water-pressure` | **Category:** `system-guides`
- **Component Audit:**
  - `[H]` **Ready:** Badge: "Fluid Mechanics Analysis", H1: "Do Whole-House Water Filters Reduce Water Pressure? Friction Loss & Head Loss Analysis"
  - `[S]` **Ready in MD:** Static pressure vs. Dynamic operating flow pressure; Fluid resistance in porous media; Quadratic velocity relationship ($v_0^2$).
  - `[T]` **Ready in MD:** 4 Primary Causes of Pressure Drop Table (Undersized port, Clogged pre-filter, Overly tight micron, Undersized tank) with $\Delta P$ and Prevention Rule.
  - `[B]` **Ready in MD:** Static Pressure vs. Dynamic Flow Pressure Callout Box.
  - `[M]` **Ready in MD:** Dual pressure gauge differential monitoring ($\Delta P = 10–12\text{ PSI}$ filter swap trigger); 4 Engineering Rules to maintain 60 PSI.
  - `[F]` **Ready in MD:** The Ergun Equation for porous media: $\frac{\Delta P}{L} = \frac{150 \mu (1-\epsilon)^2}{\epsilon^3 d_p^2} v_0 + \frac{1.75 \rho (1-\epsilon)}{\epsilon^3 d_p} v_0^2$.
  - `[Q]` **Needs Authoring:** Author 4 technical FAQs:
    1. *"What is considered normal dynamic water pressure for a residential home?"*
    2. *"Will installing a residential booster pump solve filter head loss?"*
    3. *"Why do pleated sediment filters maintain higher flow rates than spun-polypropylene filters?"*
    4. *"How much pressure drop does a central backwashing media tank cause?"*
  - `[E]` **Ready in MD:** Author box for Fluid Dynamics Engineering Team.
  - `[L]` **Action Required:** Link to `openArticleModal(12)` (SpringWell CF1) and `openArticleModal(13)` (Best whole-house filters).

---

## 3. Formatting Conventions, HTML Architecture & Data Structure

### 3.1 JavaScript Data Structure in `scripts/articles-data.js`
Each article must be declared as a Javascript object inside `CLEAR_TAP_ARTICLES`:

```javascript
const CLEAR_TAP_ARTICLES = [
  {
    id: 1, // Unique Integer 1..20
    slug: "how-to-read-water-quality-report", // Clean SEO Slug matching MD
    title: "How to Read Your City CCR Water Quality Report: An Engineer’s Guide", // Exact Title
    category: "water-testing", // Filter category identifier
    categoryLabel: "Water Testing", // Display Label
    readTime: "8 min read", // Estimated read time
    badgeClass: "ctl-badge-teal", // ctl-badge-teal | ctl-badge-pill | ctl-badge-warning | ctl-badge-dark
    excerpt: "Decode EPA Maximum Contaminant Levels (MCLs), PPM vs PPB units, and unregulated disinfection byproducts in your annual municipal water report.",
    contentHtml: `
      <!-- Rich HTML Content Body Here -->
    `
  },
  // ... Guides 2 to 20
];
```

### 3.2 HTML Hierarchy & CSS Classes

1. **Header Badge:**
   ```html
   <div class="ctl-badge-pill ctl-badge-teal" style="margin-bottom: 15px;">Diagnostic Engineering Guide</div>
   ```
2. **H1 Title:**
   ```html
   <h1 style="font-family: var(--ctl-font-heading); font-size: 2rem; color: var(--ctl-navy); margin-bottom: 16px; line-height: 1.25;">How to Read Your City CCR Water Quality Report: An Engineer’s Guide</h1>
   ```
3. **Introductory Summary:**
   ```html
   <p style="color: var(--ctl-text-main); font-size: 1.05rem; line-height: 1.68; margin-bottom: 20px;">Every July, municipal water utilities...</p>
   ```
4. **Specification Callout Boxes (`.ctl-spec-box`):**
   - Default Teal/Success: `<div class="ctl-spec-box">...</div>`
   - Info/Blue: `<div class="ctl-spec-box info">...</div>`
   - Warning/Orange: `<div class="ctl-spec-box warning">...</div>`
5. **Responsive Technical Comparison Tables:**
   ```html
   <div class="ctl-table-wrapper">
     <table class="ctl-table">
       <thead>
         <tr><th>Header 1</th><th>Header 2</th><th>Header 3</th></tr>
       </thead>
       <tbody>
         <tr><td><strong>Row Label</strong></td><td>Data Value</td><td>Data Value</td></tr>
       </tbody>
     </table>
   </div>
   ```
6. **Chemical / Physical Formulas & Math Callouts:**
   ```html
   <div style="background: var(--ctl-bg-ice); border: 1.5px solid var(--ctl-border); border-radius: var(--ctl-radius-sm); padding: 14px 18px; margin: 18px 0; font-family: var(--ctl-font-mono); font-size: 0.95rem; font-weight: 700; color: var(--ctl-navy);">
     Ca(HCO₃)₂ ──► CaCO₃↓ (Solid Limescale) + H₂O + CO₂↑
   </div>
   ```
7. **System Benchmark Spec Grids (`.ctl-spec-grid`):**
   ```html
   <div class="ctl-card" style="margin: 24px 0;">
     <h3 style="color: var(--ctl-navy); margin-bottom: 10px;">ClearTapLab Engineering Verdict: 4.8 / 5.0</h3>
     <p style="color: var(--ctl-text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">The G3P800 delivers audited 0.55 GPM flow...</p>
     <div class="ctl-spec-grid">
       <div class="ctl-spec-item"><div class="label">Tested Flow Rate</div><div class="value">0.55 GPM</div></div>
       <div class="ctl-spec-item"><div class="label">Pure-to-Drain</div><div class="value">2.4 : 1</div></div>
       <div class="ctl-spec-item"><div class="label">Measured Noise</div><div class="value">58 dB</div></div>
       <div class="ctl-spec-item"><div class="label">5-Yr TCO</div><div class="value">~$1,189</div></div>
     </div>
   </div>
   ```
8. **Frequently Asked Questions Suite:**
   ```html
   <div class="ctl-faq-container" style="margin-top: 36px; border-top: 2px solid var(--ctl-border); padding-top: 24px;">
     <h2 style="font-family: var(--ctl-font-heading); font-size: 1.4rem; color: var(--ctl-navy); margin-bottom: 18px;">Frequently Asked Questions</h2>
     
     <div class="ctl-faq-item" style="margin-bottom: 20px;">
       <h4 style="font-size: 1.05rem; color: var(--ctl-navy); margin-bottom: 6px;">Q: Where can I find my local city water report?</h4>
       <p style="color: var(--ctl-text-muted); font-size: 0.95rem; line-height: 1.6; margin: 0;">Municipal water utilities are legally required to post their CCR by July 1st each year...</p>
     </div>
     <!-- 3 to 4 items total -->
   </div>
   ```
9. **Author / Editorial Byline Box:**
   ```html
   <div class="ctl-author-box">
     <div style="font-size: 2.5rem; flex-shrink: 0;">👨‍🔬</div>
     <div class="ctl-author-meta">
       <h4>Written by ClearTapLab Technical Editorial Team</h4>
       <div class="ctl-author-role">Mechanical Engineering &amp; Water Quality Diagnostics</div>
       <p>Providing independent analysis of water chemistry, fluid mechanics, and third-party NSF/ANSI standards.</p>
     </div>
   </div>
   ```
10. **Interactive Single-Page Modal Internal Links:**
    ```html
    <a href="javascript:void(0)" onclick="openArticleModal(4)">Waterdrop G3P800 Review</a>
    ```

---

## 4. Batch Conversion & Implementation Roadmap

To execute the complete overhaul without regressions, implementation should follow a 4-batch pipeline:

### Batch 1: Conversion of Guides 01–05
- **Focus:** Foundational diagnostics, basic filtration science, first benchmark review, and water hardness sizing.
- **Conversion Scope:**
  - Expand Guide 01 (`how-to-read-water-quality-report`): Add Disinfectants section, 3 Mistakes, 4 FAQs, Byline.
  - Expand Guide 02 (`reverse-osmosis-vs-carbon-filter`): Add full Carbon & RO physics, sequential filtering, 4 FAQs, Byline.
  - Expand Guide 03 (`fix-sulfur-smell-well-water`): Add SRB/anode chemistry, AIO mechanism, 4 FAQs, Byline.
  - Expand Guide 04 (`waterdrop-g3p800-review`): Add spec audit table, 5-year TCO table, 4 technical FAQs, Byline.
  - Expand Guide 05 (`hard-water-gpg-ppm-guide`): Add WQA scale table, 4-step sizing formula, 4 FAQs, Byline.

### Batch 2: Conversion of Guides 06–10
- **Focus:** Groundwater iron chemistry, softener vs. TAC scale prevention, flagship RO roundup, PFAS pitcher investigation, and RO wastewater recovery physics.
- **Conversion Scope:**
  - Build Guide 06 (`remove-iron-from-well-water`): 4 iron forms matrix, redox equations, AIO deep dive, 4 FAQs, Byline.
  - Build Guide 07 (`water-softener-vs-salt-free`): Ion exchange vs TAC nucleation physics, comparison table, 4 FAQs, Byline.
  - Build Guide 08 (`best-reverse-osmosis-systems`): System benchmark table, individual product reviews, decision tree, 4 FAQs, Byline.
  - Build Guide 09 (`filter-pitchers-pfas-removal`): Carbon-fluorine bond chemistry, certified pitcher table, channeling pitfalls, 4 FAQs, Byline.
  - Build Guide 10 (`reverse-osmosis-water-waste`): Cross-flow kinetics, pure-to-drain efficiency table, booster pump physics, 4 FAQs, Byline.

### Batch 3: Conversion of Guides 11–15
- **Focus:** System architectures, POE whole-house filter benchmarks, mail-in laboratory testing kits, and RO remineralization chemistry.
- **Conversion Scope:**
  - Build Guide 11 (`tankless-vs-tank-reverse-osmosis`): Fluid mechanics of booster pumps vs tank backpressure, TDS creep math, 5-yr TCO, 4 FAQs, Byline.
  - Build Guide 12 (`springwell-cf1-review`): 4-stage upflow schematic, measured flow & pressure drop table, 10-yr TCO, 4 FAQs, Byline.
  - Build Guide 13 (`best-whole-house-water-filters`): Peak GPM fixture calculation, comparison table, cartridge vs media tank trade-offs, 4 FAQs, Byline.
  - Build Guide 14 (`best-water-test-kits`): ICP-MS and GC-MS lab testing breakdown, test kit comparison table, testing cadence, 4 FAQs, Byline.
  - Build Guide 15 (`remineralization-reverse-osmosis-filter`): Carbonic acid equilibrium, calcite/corosex dissolution, SCA coffee extraction parameters, 4 FAQs, Byline.

### Batch 4: Conversion of Guides 16–20
- **Focus:** Water softener master sizing, TAC salt-free conditioner roundup, sediment step-down micron sequence, fluoride removal chemistry, and whole-house pressure loss fluid dynamics.
- **Conversion Scope:**
  - Build Guide 16 (`how-to-size-water-softener`): 4-step sizing formula, master household sizing matrix, valve port sizing, 4 FAQs, Byline.
  - Build Guide 17 (`best-salt-free-water-conditioners`): DVGW W-512 TAC scale benchmark table, pre-purchase water chemistry audit, 4 FAQs, Byline.
  - Build Guide 18 (`sediment-vs-carbon-filters`): Sieving vs adsorption physics, step-down micron sizing (50µm -> 5µm -> 0.5µm), comparison table, 4 FAQs, Byline.
  - Build Guide 19 (`fluoride-removal-water`): Fluoride ionic radius (0.00026 µm), 3 proven removal methods table, activated alumina pH bounds, 4 FAQs, Byline.
  - Build Guide 20 (`whole-house-filter-water-pressure`): Ergun equation for porous media, 4 causes of pressure loss table, 4 engineering rules to maintain 60 PSI, 4 FAQs, Byline.

---

## 5. Verification & Test Plan

1. **Syntax & Data Integrity Validation:**
   - Run Node.js execution on `scripts/articles-data.js` to ensure zero syntax errors, valid array length (`CLEAR_TAP_ARTICLES.length === 20`), and correct property types.
2. **DOM & Modal Rendering Verification:**
   - Verify that calling `openArticleModal(id)` for every ID from 1 through 20 populates `#modal-article-body` with non-empty, rich HTML containing H1 headings, tables, spec callouts, formulas, FAQs, and author boxes.
3. **Category Filtering & Live Search Verification:**
   - Verify that selecting category tabs (`reverse-osmosis`, `water-testing`, `water-problems`, `filtration-technology`, `system-guides`) correctly renders all corresponding cards without truncation.
   - Verify that live search queries for keywords (e.g. "PFAS", "Iron", "Sulfur", "Ergun", "G3P800") return accurate filtered matches and open full articles in the modal.
4. **Layout & Accessibility Verification:**
   - Confirm responsive behavior on mobile viewports (< 600px) with horizontal scroll containers on `.ctl-table-wrapper`.
   - Ensure escape key and backdrop click close the modal and restore background scrolling (`document.body.style.overflow = ''`).
