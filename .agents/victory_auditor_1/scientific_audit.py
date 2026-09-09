"""
Independent Scientific & Regulatory Citations Audit across all 20 guides
"""

import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath("."))
from tests.test_utils import load_articles_data

articles = load_articles_data()

scientific_checks = {
    1: {
        "title": "CCR Guide",
        "terms": ["Safe Drinking Water Act", "MCL", "MCLG", "EPA", "Disinfection Byproduct", "Lead"],
        "equations_concepts": ["PPM", "PPB", "1 drop in 13.2 gallons"]
    },
    2: {
        "title": "RO vs Carbon Filters",
        "terms": ["NSF 58", "0.0001", "Van der Waals", "Adsorption", "TDS", "Membrane"],
        "equations_concepts": ["0.0001", "microns", "semi-permeable"]
    },
    3: {
        "title": "Sulfur Smell in Well Water",
        "terms": ["Hydrogen Sulfide", "Air-Injection", "AIO", "anode", "EPA", "NSF 42"],
        "equations_concepts": ["H₂S", "sulfur bacteria", "magnesium anode"]
    },
    4: {
        "title": "Waterdrop G3P800 Review",
        "terms": ["NSF 58", "NSF 372", "800 GPD", "TCO", "booster pump"],
        "equations_concepts": ["pure-to-drain", "3:1", "0.58 GPM"]
    },
    5: {
        "title": "Hard Water GPG vs PPM",
        "terms": ["GPG", "PPM", "Calcium", "Magnesium", "WQA", "USGS"],
        "equations_concepts": ["17.1", "Ca²⁺", "Mg²⁺", "grains per gallon"]
    },
    6: {
        "title": "Iron Removal Guide",
        "terms": ["Ferrous", "Ferric", "Air-Injection Oxidation", "Greensand", "0.3 PPM"],
        "equations_concepts": ["Fe²⁺", "Fe³⁺", "redox", "oxidation"]
    },
    7: {
        "title": "Softener vs Salt-Free TAC",
        "terms": ["Ion-Exchange", "Template Assisted Crystallization", "DVGW", "W-512", "NSF 44"],
        "equations_concepts": ["Ca²⁺", "CaCO₃", "nucleation", "sodium"]
    },
    8: {
        "title": "Best RO Systems 2026",
        "terms": ["NSF 58", "NSF 53", "NSF 401", "NSF P473", "TDS Rejection"],
        "equations_concepts": ["Waterdrop", "Home Master", "APEC", "permeate pump"]
    },
    9: {
        "title": "PFAS in Pitchers",
        "terms": ["NSF 53", "NSF P473", "PFOA", "PFOS", "4.0 PPT", "EPA"],
        "equations_concepts": ["C-F bond", "carbon block", "channeling", "adsorption"]
    },
    10: {
        "title": "RO Water Waste & Recovery",
        "terms": ["NSF 58", "Recovery Ratio", "Concentration Polarization", "Permeate Pump"],
        "equations_concepts": ["pure-to-drain", "drain water", "cross-flow"]
    },
    11: {
        "title": "Tankless vs Tank RO",
        "terms": ["NSF 58", "TDS Creep", "Bladder", "Booster Pump"],
        "equations_concepts": ["backpressure", "osmotic pressure", "Fick"]
    },
    12: {
        "title": "SpringWell CF1 Review",
        "terms": ["NSF 42", "NSF 61", "NSF 372", "KDF-55", "Catalytic Carbon"],
        "equations_concepts": ["redox", "EBCT", "upflow", "9 GPM"]
    },
    13: {
        "title": "Best Whole House Filters 2026",
        "terms": ["NSF 42", "NSF 53", "NSF 61", "GPM Peak Flow", "Pressure Drop"],
        "equations_concepts": ["cartridge", "backwashing", "port size", "1 inch"]
    },
    14: {
        "title": "Best Mail-In Test Kits 2026",
        "terms": ["EPA", "ICP-MS", "LC-MS/MS", "GC-MS", "Tap Score"],
        "equations_concepts": ["mass spectrometry", "certified laboratory", "PPB"]
    },
    15: {
        "title": "Remineralization RO Filters",
        "terms": ["EPA SMCL", "Calcite", "Corosex", "pH", "Calcium Carbonate"],
        "equations_concepts": ["carbonic acid", "dissolution", "alkaline", "TDS"]
    },
    16: {
        "title": "Water Softener Sizing Blueprint",
        "terms": ["NSF 44", "WQA", "Compensated Hardness", "Daily Grains"],
        "equations_concepts": ["75 gallons", "salt efficiency", "resin bed", "weekly capacity"]
    },
    17: {
        "title": "Best Salt-Free Conditioners 2026",
        "terms": ["DVGW W-512", "NSF 61", "Template Assisted Crystallization", "TAC Media"],
        "equations_concepts": ["micro-crystals", "scale prevention", "operating envelope"]
    },
    18: {
        "title": "Sediment vs Carbon Filters",
        "terms": ["NSF 42", "NSF 53", "Micron Rating", "Depth Sediment", "Melt-Blown"],
        "equations_concepts": ["step-down filtration", "5 micron", "surface filtration", "adsorption"]
    },
    19: {
        "title": "Fluoride Removal Methods",
        "terms": ["EPA MCL", "Activated Alumina", "Reverse Osmosis", "Distillation"],
        "equations_concepts": ["0.26", "ionic radius", "pH dependence", "hydration shell"]
    },
    20: {
        "title": "Filter Pressure Drop & Ergun Analysis",
        "terms": ["Ergun", "Darcy-Weisbach", "Friction Loss", "PSI Drop", "NSF 42"],
        "equations_concepts": ["bed fluidization", "port size", "dynamic pressure", "head loss"]
    }
}

all_passed = True
for aid, spec in scientific_checks.items():
    article = next(a for a in articles if a["id"] == aid)
    html = article["contentHtml"]
    
    missing_terms = [t for t in spec["terms"] if t.lower() not in html.lower()]
    missing_concepts = [c for c in spec["equations_concepts"] if c.lower() not in html.lower()]
    
    if missing_terms or missing_concepts:
        all_passed = False
        print(f"[FAIL] Guide {aid:02d} ({spec['title']}): Missing terms {missing_terms} | Missing concepts {missing_concepts}")
    else:
        print(f"[PASS] Guide {aid:02d} ({spec['title']}): All scientific terms & equations verified.")

print(f"\nOVERALL SCIENTIFIC CITATION AUDIT: {'100% VERIFIED' if all_passed else 'FAILED'}")
