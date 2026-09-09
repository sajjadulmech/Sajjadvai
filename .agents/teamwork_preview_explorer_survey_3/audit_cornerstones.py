import glob
import re
import os

batch_files = sorted(glob.glob('cleartaplab_batch*.md'))

for batch_file in batch_files:
    print('========================================')
    print('FILE:', batch_file)
    with open(batch_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    parts = re.split(r'\n# Article (\d+):', text)
    for i in range(1, len(parts), 2):
        art_id = parts[i]
        art_content = parts[i+1]
        
        title_m = re.search(r'# ([^\n]+)', art_content)
        title = title_m.group(1) if title_m else 'No title'
        
        slug_m = re.search(r'<!-- SLUG:\s*([^\s>]+)\s*-->', art_content)
        slug = slug_m.group(1) if slug_m else 'No slug'
        
        cat_m = re.search(r'<!-- CATEGORY:\s*([^\s>]+)\s*-->', art_content)
        cat = cat_m.group(1) if cat_m else 'No cat'
        
        spec_boxes = len(re.findall(r'ctl-spec-box', art_content))
        tables = len(re.findall(r'ctl-table', art_content))
        faq_matches = re.findall(r'### (?:Q\d+:|FAQ|\d+\. )|#### (?:Q\d+:|FAQ)|<details\b', art_content)
        words = len(art_content.split())
        
        # Standards references
        nsf_refs = re.findall(r'(?:NSF(?:/ANSI)?(?:\s*(?:42|53|58|401|55|44|372|60|61|P473|P231|P477|50))?|P473|P231|P477)', art_content)
        epa_refs = re.findall(r'(?:EPA|MCLG?|SMCL|SDWA|LCRI|NPDWR|NSDWR|MRDL)', art_content)
        
        print(f"Article {art_id.rjust(2)} | Slug: {slug.ljust(35)} | Words: {words:5d} | Tables: {tables} | SpecBoxes: {spec_boxes} | FAQs: {len(faq_matches)}")
        print(f"   Title: {title}")
        print(f"   NSF hits ({len(nsf_refs)}): {list(set(nsf_refs))[:8]}")
        print(f"   EPA hits ({len(epa_refs)}): {list(set(epa_refs))[:8]}")
