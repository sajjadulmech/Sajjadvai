"""
ClearTapLab E2E Test Suite - Shared Utilities & Data Parsers
Provides robust parsing of scripts/articles-data.js, index.html, styles/main.css,
and simulated business logic for search, category filtering, triage, and calculator.
"""

import os
import re
import json
from bs4 import BeautifulSoup

# Resolve workspace directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
STYLES_DIR = os.path.join(BASE_DIR, "styles")
INDEX_HTML_PATH = os.path.join(BASE_DIR, "index.html")
ARTICLES_DATA_PATH = os.path.join(SCRIPTS_DIR, "articles-data.js")
MAIN_CSS_PATH = os.path.join(STYLES_DIR, "main.css")

# Canonical Categories
VALID_CATEGORIES = {
    "reverse-osmosis",
    "water-testing",
    "water-problems",
    "filtration-technology",
    "system-guides"
}

# Master Standards & Scientific Matrix for all 20 guides
MASTER_GUIDES_MATRIX = {
    1: {
        "slug": "how-to-read-water-quality-report",
        "title": "How to Read Your City CCR Water Quality Report: An Engineer’s Guide",
        "category": "water-testing",
        "categoryLabel": "Water Testing",
        "expected_standards": ["EPA", "SDWA", "MCL", "MCLG", "LCR", "NSF"],
        "core_mechanisms": ["PPM", "PPB", "PPT", "Disinfection Byproduct", "Lead", "1 drop in 13.2 gallons"],
        "min_faq_count": 3
    },
    2: {
        "slug": "reverse-osmosis-vs-carbon-filter",
        "title": "Reverse Osmosis vs. Carbon Filters: The Physics Explained",
        "category": "filtration-technology",
        "categoryLabel": "Filtration Science",
        "expected_standards": ["NSF 58", "NSF 42", "NSF 53"],
        "core_mechanisms": ["0.0001", "Adsorption", "Van der Waals", "Membrane", "TDS"],
        "min_faq_count": 3
    },
    3: {
        "slug": "fix-sulfur-smell-well-water",
        "title": "How to Fix Rotten Egg Sulfur Smell in Well Water",
        "category": "water-problems",
        "categoryLabel": "Water Problems",
        "expected_standards": ["EPA", "NSF 42", "0.05"],
        "core_mechanisms": ["H₂S", "Hydrogen Sulfide", "anode", "Air-Injection", "AIO"],
        "min_faq_count": 3
    },
    4: {
        "slug": "waterdrop-g3p800-review",
        "title": "Waterdrop G3P800 Engineering Review: 6-Month Benchmark Audit",
        "category": "reverse-osmosis",
        "categoryLabel": "Reverse Osmosis",
        "expected_standards": ["NSF 58", "NSF 372", "NSF 53"],
        "core_mechanisms": ["800 GPD", "TCO", "Recovery", "pure-to-drain", "TDS"],
        "min_faq_count": 3
    },
    5: {
        "slug": "hard-water-gpg-ppm-guide",
        "title": "What Is Hard Water? GPG vs. PPM Calculation & Sizing Guide",
        "category": "water-problems",
        "categoryLabel": "Water Problems",
        "expected_standards": ["WQA", "NSF 44", "USGS", "17.1"],
        "core_mechanisms": ["GPG", "PPM", "Calcium", "Magnesium", "Ca²⁺", "Scale"],
        "min_faq_count": 3
    },
    6: {
        "slug": "remove-iron-from-well-water",
        "title": "How to Remove Iron from Well Water: The Complete Engineer’s Guide",
        "category": "water-problems",
        "categoryLabel": "Water Problems",
        "expected_standards": ["EPA", "0.3 PPM", "NSF 42", "NSF 44"],
        "core_mechanisms": ["Ferrous", "Ferric", "Fe²⁺", "Fe³⁺", "Oxidation", "AIO", "Greensand"],
        "min_faq_count": 3
    },
    7: {
        "slug": "water-softener-vs-salt-free",
        "title": "Water Softeners vs. Salt-Free TAC Conditioners: Which Do You Actually Need?",
        "category": "system-guides",
        "categoryLabel": "System Sizing & Guides",
        "expected_standards": ["NSF 44", "DVGW", "W-512", "NSF 372"],
        "core_mechanisms": ["Ion-Exchange", "TAC", "Template Assisted Crystallization", "Resin", "Sodium"],
        "min_faq_count": 3
    },
    8: {
        "slug": "best-reverse-osmosis-systems",
        "title": "Best Reverse Osmosis Systems of 2026: An Engineer’s Benchmark Audit",
        "category": "reverse-osmosis",
        "categoryLabel": "Reverse Osmosis",
        "expected_standards": ["NSF 58", "NSF 53", "NSF 401", "NSF P473"],
        "core_mechanisms": ["Waterdrop", "Home Master", "APEC", "TDS Rejection", "Permeate Pump"],
        "min_faq_count": 3
    },
    9: {
        "slug": "filter-pitchers-pfas-removal",
        "title": "Do Water Filter Pitchers Remove PFAS Forever Chemicals? NSF 53 & P473 Tested",
        "category": "filtration-technology",
        "categoryLabel": "Filtration Science",
        "expected_standards": ["NSF 53", "NSF P473", "EPA", "4.0 PPT", "PFOA", "PFOS"],
        "core_mechanisms": ["GAC", "Carbon Block", "Channeling", "Adsorption", "Forever Chemicals"],
        "min_faq_count": 3
    },
    10: {
        "slug": "reverse-osmosis-water-waste",
        "title": "How Much Water Does Reverse Osmosis Waste? Recovery Ratios Explained",
        "category": "reverse-osmosis",
        "categoryLabel": "Reverse Osmosis",
        "expected_standards": ["NSF 58", "EPA WaterSense"],
        "core_mechanisms": ["Recovery Ratio", "Pure-to-Drain", "Concentration Polarization", "Permeate Pump", "Drain Water"],
        "min_faq_count": 3
    },
    11: {
        "slug": "tankless-vs-tank-reverse-osmosis",
        "title": "Tankless vs. Tank Reverse Osmosis Systems: An Engineer’s Breakdown",
        "category": "reverse-osmosis",
        "categoryLabel": "Reverse Osmosis",
        "expected_standards": ["NSF 58", "NSF 372"],
        "core_mechanisms": ["TDS Creep", "Bladder Tank", "Booster Pump", "Flow Rate", "Membrane Flux"],
        "min_faq_count": 3
    },
    12: {
        "slug": "springwell-cf1-review",
        "title": "SpringWell CF1 Whole-House Water Filter Review: An Engineer’s 1-Year Benchmark",
        "category": "system-guides",
        "categoryLabel": "System Sizing & Guides",
        "expected_standards": ["NSF 42", "NSF 61", "NSF 372"],
        "core_mechanisms": ["KDF-55", "Catalytic Carbon", "Sediment", "GPM", "Pressure Drop", "Upflow"],
        "min_faq_count": 3
    },
    13: {
        "slug": "best-whole-house-water-filters",
        "title": "Best Whole-House Water Filters of 2026: Sizing & Sieve Analysis",
        "category": "system-guides",
        "categoryLabel": "System Sizing & Guides",
        "expected_standards": ["NSF 42", "NSF 53", "NSF 61"],
        "core_mechanisms": ["GPM Peak Flow", "Port Size", "Backwashing Media", "Cartridge", "Pressure Drop"],
        "min_faq_count": 3
    },
    14: {
        "slug": "best-water-test-kits",
        "title": "Best Mail-In Water Test Kits of 2026: EPA Lab Accuracy Compared",
        "category": "water-testing",
        "categoryLabel": "Water Testing",
        "expected_standards": ["EPA 200.8", "EPA 524.2", "EPA 537.1", "EPA 300.0"],
        "core_mechanisms": ["ICP-MS", "LC-MS/MS", "GC-MS", "Tap Score", "Test Strips", "PPB"],
        "min_faq_count": 3
    },
    15: {
        "slug": "remineralization-reverse-osmosis-filter",
        "title": "Remineralization RO Filters: Do You Need an Alkaline Post-Filter?",
        "category": "reverse-osmosis",
        "categoryLabel": "Reverse Osmosis",
        "expected_standards": ["EPA SMCL", "SCA", "pH 6.5"],
        "core_mechanisms": ["Calcite", "Corosex", "Calcium Carbonate", "pH Rebalancing", "Coffee Extraction", "TDS"],
        "min_faq_count": 3
    },
    16: {
        "slug": "how-to-size-water-softener",
        "title": "How to Size a Water Softener: The Step-by-Step Engineering Formula",
        "category": "system-guides",
        "categoryLabel": "System Sizing & Guides",
        "expected_standards": ["NSF 44", "WQA S-100", "3,350 grains"],
        "core_mechanisms": ["Compensated Hardness", "Daily Grains", "Weekly Capacity", "Resin Bed", "Salt Efficiency"],
        "min_faq_count": 3
    },
    17: {
        "slug": "best-salt-free-water-conditioners",
        "title": "Best Salt-Free Water Conditioners of 2026: TAC Scale Prevention Benchmark",
        "category": "system-guides",
        "categoryLabel": "System Sizing & Guides",
        "expected_standards": ["DVGW W-512", "NSF 61", "NSF 372"],
        "core_mechanisms": ["TAC Media", "Scale Prevention", "Nucleation", "Operating Envelope", "Chlorine Limit"],
        "min_faq_count": 3
    },
    18: {
        "slug": "sediment-vs-carbon-filters",
        "title": "Sediment vs. Carbon Filters: Micron Ratings & Placement Sequence Explained",
        "category": "filtration-technology",
        "categoryLabel": "Filtration Science",
        "expected_standards": ["NSF 42", "NSF 53", "ISO 2942"],
        "core_mechanisms": ["Micron Rating", "Depth Sediment", "Melt-Blown", "Pleated", "Step-Down Filtration"],
        "min_faq_count": 3
    },
    19: {
        "slug": "fluoride-removal-water",
        "title": "Fluoride Removal Methods for Tap Water: RO vs. Activated Alumina vs. Distillation",
        "category": "filtration-technology",
        "categoryLabel": "Filtration Science",
        "expected_standards": ["EPA MCL 4.0", "EPA SMCL 2.0", "NSF 58", "NSF 53"],
        "core_mechanisms": ["Activated Alumina", "Reverse Osmosis", "Distillation", "Ionic Radius", "pH Dependence"],
        "min_faq_count": 3
    },
    20: {
        "slug": "whole-house-filter-water-pressure",
        "title": "Do Whole-House Water Filters Reduce Water Pressure? Friction Loss & Head Loss Analysis",
        "category": "system-guides",
        "categoryLabel": "System Sizing & Guides",
        "expected_standards": ["IPC", "UPC", "NSF 42", "NSF 61"],
        "core_mechanisms": ["Ergun Equation", "Darcy-Weisbach", "Friction Loss", "PSI Drop", "Port Size 1 inch", "Bed Fluidization"],
        "min_faq_count": 3
    }
}


def load_articles_data(file_path=None):
    """
    Robustly parses scripts/articles-data.js into a list of Python dicts.
    Handles JavaScript template literals (`...`), unquoted keys, nested quotes,
    and HTML content blocks with complete accuracy.
    """
    path = file_path or ARTICLES_DATA_PATH
    if not os.path.exists(path):
        raise FileNotFoundError(f"Articles data file not found at: {path}")

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    articles = []
    pos = 0
    while True:
        m = re.search(r'\{\s*id:\s*(\d+)', content[pos:])
        if not m:
            break
        start_idx = pos + m.start()
        
        # State machine to find the matching closing brace
        idx = start_idx
        in_backtick = False
        in_double = False
        in_single = False
        escape = False
        brace_depth = 0
        
        while idx < len(content):
            char = content[idx]
            if escape:
                escape = False
            elif char == '\\':
                escape = True
            elif char == '`' and not in_double and not in_single:
                in_backtick = not in_backtick
            elif char == '"' and not in_backtick and not in_single:
                in_double = not in_double
            elif char == "'" and not in_backtick and not in_double:
                in_single = not in_single
            elif not in_backtick and not in_double and not in_single:
                if char == '{':
                    brace_depth += 1
                elif char == '}':
                    brace_depth -= 1
                    if brace_depth == 0:
                        obj_str = content[start_idx:idx+1]
                        
                        # Extract fields
                        id_m = re.search(r'id:\s*(\d+)', obj_str)
                        slug_m = re.search(r'slug:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                        title_m = re.search(r'title:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                        cat_m = re.search(r'category:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                        cat_lbl_m = re.search(r'categoryLabel:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                        read_m = re.search(r'readTime:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                        badge_m = re.search(r'badgeClass:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                        excerpt_m = re.search(r'excerpt:\s*["\'`]([^"\r\n\'`]+)["\'`]', obj_str)
                        tags_m = re.search(r'tags:\s*\[(.*?)\]', obj_str, re.DOTALL)
                        
                        # Extract contentHtml inside backticks
                        # Match contentHtml: `...`
                        html_start = obj_str.find("contentHtml:")
                        content_html = ""
                        if html_start != -1:
                            bt_start = obj_str.find("`", html_start)
                            if bt_start != -1:
                                bt_end = obj_str.rfind("`")
                                if bt_end > bt_start:
                                    content_html = obj_str[bt_start+1:bt_end]

                        tags = []
                        if tags_m:
                            raw_tags = tags_m.group(1).split(',')
                            tags = [t.strip(' "\' \t\r\n') for t in raw_tags if t.strip(' "\' \t\r\n')]

                        articles.append({
                            "id": int(id_m.group(1)) if id_m else None,
                            "slug": slug_m.group(1).strip() if slug_m else "",
                            "title": title_m.group(1).strip() if title_m else "",
                            "category": cat_m.group(1).strip() if cat_m else "",
                            "categoryLabel": cat_lbl_m.group(1).strip() if cat_lbl_m else "",
                            "readTime": read_m.group(1).strip() if read_m else "",
                            "badgeClass": badge_m.group(1).strip() if badge_m else "",
                            "excerpt": excerpt_m.group(1).strip() if excerpt_m else "",
                            "tags": tags,
                            "contentHtml": content_html
                        })
                        pos = idx + 1
                        break
            idx += 1
        else:
            break

    return articles


def load_index_html(file_path=None):
    """Loads index.html and returns a BeautifulSoup DOM tree."""
    path = file_path or INDEX_HTML_PATH
    if not os.path.exists(path):
        raise FileNotFoundError(f"index.html not found at: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return BeautifulSoup(f.read(), "html.parser")


def load_main_css(file_path=None):
    """Loads styles/main.css content."""
    path = file_path or MAIN_CSS_PATH
    if not os.path.exists(path):
        raise FileNotFoundError(f"styles/main.css not found at: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def simulate_search(query, articles):
    """
    Simulates the JavaScript performSearch(query) logic from scripts/app.js.
    """
    clean_q = query.strip().lower()
    if not clean_q:
        return articles
    
    return [
        a for a in articles
        if clean_q in a.get("title", "").lower()
        or clean_q in a.get("excerpt", "").lower()
        or clean_q in a.get("categoryLabel", "").lower()
    ]


def simulate_category_filter(category, articles):
    """
    Simulates the JavaScript category filter logic from scripts/app.js.
    """
    if category == "all":
        return articles
    return [a for a in articles if a.get("category") == category]


def simulate_calculator(people, hardness_gpg, iron_ppm):
    """
    Simulates the JavaScript calculate() logic from scripts/app.js.
    Returns calculated values matching UI outputs.
    """
    people_val = max(1, int(people))
    hardness_val = max(1.0, float(hardness_gpg))
    iron_val = max(0.0, float(iron_ppm))

    daily_gallons = people_val * 75
    compensated_hardness = hardness_val + (iron_val * 5.0)
    daily_grains = daily_gallons * compensated_hardness
    raw_weekly_capacity = daily_grains * 7 * 1.25

    if raw_weekly_capacity <= 24000:
        recommended_size = 24000
        cu_ft = 0.75
    elif raw_weekly_capacity <= 32000:
        recommended_size = 32000
        cu_ft = 1.0
    elif raw_weekly_capacity <= 40000:
        recommended_size = 40000
        cu_ft = 1.25
    elif raw_weekly_capacity <= 48000:
        recommended_size = 48000
        cu_ft = 1.5
    elif raw_weekly_capacity <= 64000:
        recommended_size = 64000
        cu_ft = 2.0
    elif raw_weekly_capacity <= 80000:
        recommended_size = 80000
        cu_ft = 2.5
    else:
        recommended_size = 96000
        cu_ft = 3.0

    annual_salt_bags = round((daily_grains * 365) / (2000 * 40)) + 6
    five_year_salt_cost = annual_salt_bags * 8 * 5

    return {
        "daily_gallons": daily_gallons,
        "compensated_hardness": compensated_hardness,
        "daily_grains": daily_grains,
        "raw_weekly_capacity": raw_weekly_capacity,
        "recommended_size": recommended_size,
        "cu_ft": cu_ft,
        "five_year_salt_cost": five_year_salt_cost
    }


def extract_word_count(html_content):
    """
    Extracts visible text from HTML and returns the clean word count.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text(separator=" ", strip=True)
    words = re.findall(r'\b[\w\-\'\u00C0-\u017F]+\b', text)
    return len(words)
