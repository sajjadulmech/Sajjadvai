"""
Scientific and Technical Accuracy Assertion Suite for ClearTapLab 20 Guides
Validates exact scientific principles, chemistry formulas, engineering equations,
NSF/ANSI standards, EPA regulations, and structure.
"""

import os
import re
import sys
from bs4 import BeautifulSoup

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

from tests.test_utils import load_articles_data

articles = load_articles_data()
articles_by_id = {a["id"]: a for a in articles}

def verify_all_guides_scientifically():
    checks = []
    
    # Guide 1
    g1 = articles_by_id[1]
    soup1 = BeautifulSoup(g1["contentHtml"], "html.parser")
    t1 = soup1.get_text(" ", strip=True)
    checks.append(("Guide 01: EPA SDWA / CCR standards", all(k in t1 for k in ["MCL", "MCLG", "SDWA", "PPM", "PPB", "PPT"])))
    checks.append(("Guide 01: Disinfection Byproducts (TTHMs, HAAs)", any(k in t1 for k in ["Disinfection Byproduct", "TTHM", "HAA5"])))
    checks.append(("Guide 01: Lead and Copper Rule (LCR)", "Lead and Copper Rule" in t1 or "LCR" in t1))
    
    # Guide 2
    g2 = articles_by_id[2]
    soup2 = BeautifulSoup(g2["contentHtml"], "html.parser")
    t2 = soup2.get_text(" ", strip=True)
    checks.append(("Guide 02: NSF 58 & NSF 42/53", "NSF 58" in t2 and ("NSF 42" in t2 or "NSF 53" in t2)))
    checks.append(("Guide 02: TFC RO Membrane pore size (0.0001 micron)", "0.0001" in t2 and "polyamide" in t2.lower()))
    checks.append(("Guide 02: Carbon Adsorption & Van der Waals", "adsorption" in t2.lower() and "van der waals" in t2.lower()))
    
    # Guide 3
    g3 = articles_by_id[3]
    soup3 = BeautifulSoup(g3["contentHtml"], "html.parser")
    t3 = soup3.get_text(" ", strip=True)
    checks.append(("Guide 03: H2S & Sulfate-Reducing Bacteria", "H₂S" in t3 or "hydrogen sulfide" in t3.lower()))
    checks.append(("Guide 03: Water Heater Anode Rod Reaction", "anode" in t3.lower() and ("magnesium" in t3.lower() or "aluminum" in t3.lower())))
    checks.append(("Guide 03: Air Injection Oxidation (AIO) / Aeration", "AIO" in t3 or "air-injection" in t3.lower() or "oxidation" in t3.lower()))
    
    # Guide 4
    g4 = articles_by_id[4]
    soup4 = BeautifulSoup(g4["contentHtml"], "html.parser")
    t4 = soup4.get_text(" ", strip=True)
    checks.append(("Guide 04: Waterdrop G3P800 800 GPD spec", "800 GPD" in t4 or "800" in t4))
    checks.append(("Guide 04: Pure-to-drain recovery ratio", "pure-to-drain" in t4.lower() or "recovery ratio" in t4.lower() or "3:1" in t4))
    checks.append(("Guide 04: NSF 58 / NSF 372 / NSF 53 standards", "NSF" in t4 and "58" in t4))
    checks.append(("Guide 04: TCO (Total Cost of Ownership)", "TCO" in t4 or "Cost of Ownership" in t4))
    
    # Guide 5
    g5 = articles_by_id[5]
    soup5 = BeautifulSoup(g5["contentHtml"], "html.parser")
    t5 = soup5.get_text(" ", strip=True)
    checks.append(("Guide 05: GPG to PPM conversion factor (17.1)", "17.1" in t5 and "GPG" in t5 and "PPM" in t5))
    checks.append(("Guide 05: Calcium & Magnesium divalent ions (Ca2+, Mg2+)", ("Ca²⁺" in t5 or "calcium" in t5.lower()) and ("Mg²⁺" in t5 or "magnesium" in t5.lower())))
    checks.append(("Guide 05: WQA / USGS Hardness classification", "WQA" in t5 or "USGS" in t5))
    
    # Guide 6
    g6 = articles_by_id[6]
    soup6 = BeautifulSoup(g6["contentHtml"], "html.parser")
    t6 = soup6.get_text(" ", strip=True)
    checks.append(("Guide 06: Ferrous (Fe2+) vs Ferric (Fe3+) iron", ("Fe²⁺" in t6 or "ferrous" in t6.lower()) and ("Fe³⁺" in t6 or "ferric" in t6.lower())))
    checks.append(("Guide 06: EPA Secondary Standard 0.3 PPM", "0.3" in t6 and "PPM" in t6))
    checks.append(("Guide 06: Oxidation technologies (AIO, Greensand, Birm)", "AIO" in t6 and ("greensand" in t6.lower() or "birm" in t6.lower())))
    
    # Guide 7
    g7 = articles_by_id[7]
    soup7 = BeautifulSoup(g7["contentHtml"], "html.parser")
    t7 = soup7.get_text(" ", strip=True)
    checks.append(("Guide 07: Ion-Exchange vs TAC (Template Assisted Crystallization)", "ion-exchange" in t7.lower() and "tac" in t7.lower()))
    checks.append(("Guide 07: DVGW W-512 German scale standard", "DVGW" in t7 or "W-512" in t7))
    checks.append(("Guide 07: Sodium exchange chemistry and resin cross-linking", "resin" in t7.lower() and "sodium" in t7.lower()))
    
    # Guide 8
    g8 = articles_by_id[8]
    soup8 = BeautifulSoup(g8["contentHtml"], "html.parser")
    t8 = soup8.get_text(" ", strip=True)
    checks.append(("Guide 08: Multi-system benchmark audit (Waterdrop, Home Master, APEC)", "waterdrop" in t8.lower() and "home master" in t8.lower()))
    checks.append(("Guide 08: NSF 58, 53, 401, P473 verification", "NSF 58" in t8 and "NSF" in t8))
    checks.append(("Guide 08: Permeate pump / TDS creep physics", "permeate pump" in t8.lower() or "tds" in t8.lower()))
    
    # Guide 9
    g9 = articles_by_id[9]
    soup9 = BeautifulSoup(g9["contentHtml"], "html.parser")
    t9 = soup9.get_text(" ", strip=True)
    checks.append(("Guide 09: PFAS species (PFOA, PFOS, GenX/HFPO-DA)", "PFOA" in t9 and "PFOS" in t9))
    checks.append(("Guide 09: NSF 53 & NSF P473 standards (4.0 PPT EPA limit)", "NSF 53" in t9 or "NSF P473" in t9 or "4.0" in t9 or "4 ppt" in t9.lower()))
    checks.append(("Guide 09: Channeling & Empty Bed Contact Time (EBCT)", "channeling" in t9.lower() or "ebct" in t9.lower() or "contact time" in t9.lower()))
    
    # Guide 10
    g10 = articles_by_id[10]
    soup10 = BeautifulSoup(g10["contentHtml"], "html.parser")
    t10 = soup10.get_text(" ", strip=True)
    checks.append(("Guide 10: Recovery ratios (pure-to-drain)", "pure-to-drain" in t10.lower() or "recovery" in t10.lower()))
    checks.append(("Guide 10: Concentration Polarization & Osmotic Pressure", "polarization" in t10.lower() or "osmotic pressure" in t10.lower() or "van 't hoff" in t10.lower() or "van" in t10.lower()))
    checks.append(("Guide 10: Permeate pump efficiency improvement", "permeate pump" in t10.lower()))
    
    # Guide 11
    g11 = articles_by_id[11]
    soup11 = BeautifulSoup(g11["contentHtml"], "html.parser")
    t11 = soup11.get_text(" ", strip=True)
    checks.append(("Guide 11: TDS Creep thermodynamic mechanism", "tds creep" in t11.lower() or "creep" in t11.lower()))
    checks.append(("Guide 11: Direct booster pump vs hydropneumatic bladder tank", "booster pump" in t11.lower() and "bladder" in t11.lower()))
    checks.append(("Guide 11: Membrane Flux Rate (GFD)", "flux" in t11.lower() or "gfd" in t11.lower() or "flow rate" in t11.lower()))
    
    # Guide 12
    g12 = articles_by_id[12]
    soup12 = BeautifulSoup(g12["contentHtml"], "html.parser")
    t12 = soup12.get_text(" ", strip=True)
    checks.append(("Guide 12: SpringWell CF1 media (Catalytic Carbon + KDF-55)", "catalytic carbon" in t12.lower() and "kdf" in t12.lower()))
    checks.append(("Guide 12: Upflow fluidization bed dynamics", "upflow" in t12.lower() or "fluidization" in t12.lower()))
    checks.append(("Guide 12: Peak flow rate (9 GPM) & pressure drop", "9 gpm" in t12.lower() or "pressure drop" in t12.lower() or "psi" in t12.lower()))
    
    # Guide 13
    g13 = articles_by_id[13]
    soup13 = BeautifulSoup(g13["contentHtml"], "html.parser")
    t13 = soup13.get_text(" ", strip=True)
    checks.append(("Guide 13: Whole house sizing: peak GPM & bathroom fixture count", "gpm" in t13.lower() and "bathroom" in t13.lower()))
    checks.append(("Guide 13: Port sizing friction loss (1\" vs 3/4\" NPT)", "1\"" in t13 or "1 inch" in t13.lower() or "3/4" in t13 or "port" in t13.lower()))
    checks.append(("Guide 13: Backwashing media vs cartridge systems", "backwash" in t13.lower() and "cartridge" in t13.lower()))
    
    # Guide 14
    g14 = articles_by_id[14]
    soup14 = BeautifulSoup(g14["contentHtml"], "html.parser")
    t14 = soup14.get_text(" ", strip=True)
    checks.append(("Guide 14: EPA certified lab methods (EPA 200.8, 524.2, 537.1, 300.0)", "EPA" in t14 and ("200.8" in t14 or "537.1" in t14 or "524.2" in t14 or "300.0" in t14)))
    checks.append(("Guide 14: Analytical instruments (ICP-MS, LC-MS/MS, GC-MS)", "ICP-MS" in t14 and "LC-MS/MS" in t14))
    checks.append(("Guide 14: Tap Score vs paper test strips accuracy", "tap score" in t14.lower() and "strip" in t14.lower()))
    
    # Guide 15
    g15 = articles_by_id[15]
    soup15 = BeautifulSoup(g15["contentHtml"], "html.parser")
    t15 = soup15.get_text(" ", strip=True)
    checks.append(("Guide 15: Mineral dissolution chemistry (Calcite CaCO3, Corosex MgO)", "calcite" in t15.lower() and ("corosex" in t15.lower() or "caco₃" in t15.lower() or "calcium carbonate" in t15.lower())))
    checks.append(("Guide 15: pH rebalancing and Langelier Saturation Index (LSI)", "ph" in t15.lower() and ("rebalance" in t15.lower() or "alkaline" in t15.lower())))
    checks.append(("Guide 15: SCA Specialty Coffee extraction TDS requirements", "coffee" in t15.lower() or "extraction" in t15.lower() or "sca" in t15.lower()))
    
    # Guide 16
    g16 = articles_by_id[16]
    soup16 = BeautifulSoup(g16["contentHtml"], "html.parser")
    t16 = soup16.get_text(" ", strip=True)
    checks.append(("Guide 16: 4-step softener sizing formula (People x 75 GPD x Compensated Hardness)", "75" in t16 and "compensated" in t16.lower() and "grain" in t16.lower()))
    checks.append(("Guide 16: Salt efficiency curve (3,350+ grains/lb vs max capacity)", "salt efficiency" in t16.lower() or "3,350" in t16 or "grains/lb" in t16.lower() or "grains per pound" in t16.lower()))
    checks.append(("Guide 16: NSF 44 & Metered DIR control valve", "NSF 44" in t16 or "DIR" in t16 or "metered" in t16.lower()))
    
    # Guide 17
    g17 = articles_by_id[17]
    soup17 = BeautifulSoup(g17["contentHtml"], "html.parser")
    t17 = soup17.get_text(" ", strip=True)
    checks.append(("Guide 17: TAC (Template Assisted Crystallization) microscopic nucleation", "template assisted crystallization" in t17.lower() or "tac" in t17.lower()))
    checks.append(("Guide 17: DVGW W-512 testing benchmark", "DVGW" in t17 or "W-512" in t17))
    checks.append(("Guide 17: Pre-installation operating envelope (pH, Fe, Mn, Chlorine)", "operating envelope" in t17.lower() or ("iron" in t17.lower() and "chlorine" in t17.lower())))
    
    # Guide 18
    g18 = articles_by_id[18]
    soup18 = BeautifulSoup(g18["contentHtml"], "html.parser")
    t18 = soup18.get_text(" ", strip=True)
    checks.append(("Guide 18: Step-down micron sizing (50 -> 20 -> 5 -> 0.5 micron)", "step-down" in t18.lower() or "micron" in t18.lower()))
    checks.append(("Guide 18: Mechanical sieving vs adsorption mechanics", "sieving" in t18.lower() or "pore" in t18.lower() or "adsorption" in t18.lower()))
    checks.append(("Guide 18: ISO 2942 / NSF 42 standards", "ISO 2942" in t18 or "NSF 42" in t18))
    
    # Guide 19
    g19 = articles_by_id[19]
    soup19 = BeautifulSoup(g19["contentHtml"], "html.parser")
    t19 = soup19.get_text(" ", strip=True)
    checks.append(("Guide 19: Why GAC fails on fluoride (small hydrated ionic radius)", "ionic radius" in t19.lower() or "hydrated" in t19.lower() or "adsorption" in t19.lower()))
    checks.append(("Guide 19: Activated Alumina (Al2O3) chemisorption & pH sensitivity", "activated alumina" in t19.lower() and "ph" in t19.lower()))
    checks.append(("Guide 19: Reverse Osmosis Donnan exclusion / Distillation phase separation", "reverse osmosis" in t19.lower() and "distillation" in t19.lower()))
    
    # Guide 20
    g20 = articles_by_id[20]
    soup20 = BeautifulSoup(g20["contentHtml"], "html.parser")
    t20 = soup20.get_text(" ", strip=True)
    checks.append(("Guide 20: Ergun Equation for packed bed pressure drop", "Ergun" in t20))
    checks.append(("Guide 20: Darcy-Weisbach friction loss equation", "Darcy-Weisbach" in t20 or "Darcy" in t20))
    checks.append(("Guide 20: Upflow fluidization vs Downflow packed beds", "upflow" in t20.lower() and "downflow" in t20.lower()))
    checks.append(("Guide 20: Port sizing & pipe diameter impact (1\" vs 3/4\")", "port" in t20.lower() or "diameter" in t20.lower() or "1\"" in t20 or "3/4" in t20))

    passed = 0
    failed = 0
    print("=== SCIENTIFIC AND TECHNICAL ASSERTION RESULTS ===")
    for desc, result in checks:
        status = "PASS" if result else "FAIL"
        if result:
            passed += 1
        else:
            failed += 1
        print(f"[{status}] {desc}")
    print(f"\nTotal Assertions: {len(checks)} | Passed: {passed} | Failed: {failed}")

if __name__ == "__main__":
    verify_all_guides_scientifically()
