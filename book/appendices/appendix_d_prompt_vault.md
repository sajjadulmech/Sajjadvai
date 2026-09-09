# Appendix D: The Operator's Prompt Vault

A curated reference collection of the four primary strategic prompts used throughout the Gemini research and editorial pipeline.

---

## 1. The Niche Sceptic Prompt (Niche Inversion)

**When to use:** When you have 2–3 niche candidates and need an objective critique before committing time.

```markdown
You are a conservative business analyst evaluating physical product affiliate opportunities for a solo part-time operator (10 hours/week).

I want to find 5 unglamorous, technical micro-niches based on ACUTE HOME OR WORKSHOP PROBLEMS, NOT lifestyle hobbies.

Filter all candidates through these 5 mandatory constraints:
1. Acute Pain: The user is searching to solve a specific, frustrating, or urgent failure (e.g., odor, leaks, mechanical wear, contamination, regulatory compliance), NOT casually browsing a hobby.
2. High Payout Potential: The core solving equipment must retail between $200 and $1,200, with private affiliate programs paying 6% to 10% commission ($20 to $100 per sale).
3. Consumable Tail: The equipment must require regular replacement consumables (filters, cartridges, calibration fluid, wear parts) that can be linked to Amazon or direct merchants for recurring sales.
4. Independent Technical Standards: The products must be governed by published engineering standards (e.g., NSF, ANSI, UL, EPA, ISO) or manufacturer technical manuals, so we can evaluate specifications objectively without fabricating hands-on lab tests.
5. Search Vulnerability: Search results must NOT be completely dominated by mainstream lifestyle media (Wirecutter, Forbes). There should be room for a specialized technical reference site.

Provide 4 candidate micro-niches. For each candidate, specify the core problem, core product price, consumable parts, and why big lifestyle publishers ignore it.
```

---

## 2. The Information Gap Extractor (Competitor Research)

**When to use:** Before drafting any cornerstone guide. Paste summaries of the top 3 ranking Google results to extract their technical omissions.

```markdown
You are a senior investigative technical editor specializing in consumer mechanical appliances.

Here are the text summaries of the 3 top-ranking articles for the search query: [INSERT QUERY]:
"""
[PASTE COMPETITOR OUTLINES OR EXCERPTS HERE]
"""

Perform an Information Gain & Gap Audit:
1. Identify 4 critical technical questions that an educated homeowner would have before spending $800, but which NONE of these 3 competitor articles answered.
2. Search manufacturer technical manuals, NSF/ANSI Standard 58 performance listings, and plumbing installation guides to find the exact answers to those 4 missing questions.
3. Highlight any physical limitations, plumbing fitting constraints, water temperature limits, or recurring consumable costs that competitors ignored.
4. Output these findings as a structured "Information Gain Brief" that will form the core of our technical teardown.
```

---

## 3. The Forensic Teardown Drafter

**When to use:** To draft a product teardown using engineering manuals and certified test data without fake hands-on claims.

```markdown
You are a senior plumbing systems and materials engineer writing a forensic technical product teardown for ClearTapLab.com.

Product to Analyze: [INSERT PRODUCT, e.g., Waterdrop G3P800 Tankless Reverse Osmosis System]
Retail Price: [INSERT PRICE, e.g., $799]
Target Audience: Discerning homeowners researching under-sink water purification.

Strict Editorial Directives:
1. ABSOLUTE NON-FABRICATION: Never use first-person pronouns claiming personal unboxing, hands-on testing, or kitchen installation. Write from the perspective of an independent technical analyst evaluating public engineering documentation.
2. CITATION OF CERTIFIED STANDARDS: Cite official NSF/ANSI Standards (42, 53, 58, 372). Specify exact percentage reduction for lead, PFOA/PFAS, and TDS.
3. PHYSICAL & PLUMBING REALITIES: Detail cabinet clearance requirements, unswitched 110V electrical requirements, feed water pressure limits, and booster pump noise dynamics (dB).
4. THE "SO WHAT?" TEST: For every dry technical specification, explain its direct household consequence.
5. 5-YEAR TCO AUDIT: Include a detailed replacement schedule table breaking down composite filter and RO membrane costs over 60 months.
```

---

## 4. The Commission Negotiation Pitch

**When to use:** When your site generates 5+ sales per month with a merchant and you want to request a private commission tier increase.

```text
Subject: [YourDomain.com] Performance Review & Commission Tier Discussion

Hi [Affiliate Manager Name],

My name is [Your Name], publisher of [YourDomain.com]. Over the last 60 days, our technical guides have driven [Number, e.g., 8] qualified sales of your [Brand/System Name], with an exceptional 0% customer return rate.

Our platform focuses heavily on technical pre-purchase installation education (electrical requirements, plumbing clearance, certified NSF standards), which ensures our referred buyers are fully qualified and know exactly what they are purchasing.

We are currently planning an expansion into our next topic cluster ([e.g., Residential UV Disinfection & Whole House Systems]), where we intend to feature [Merchant Brand] as our primary recommendation.

Given our conversion performance and upcoming cluster expansion, would you be open to adjusting our baseline commission tier from 8.0% to 10.5%?

You can review our live platform and recent teardown of your equipment here:
[Link to your best-performing guide]

Thank you for your partnership,
[Your Name]
[YourDomain.com]
```
