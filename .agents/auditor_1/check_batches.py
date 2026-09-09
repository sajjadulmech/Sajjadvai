import os
import sys

def check_batch_files_consistency():
    scripts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../scripts"))
    
    with open(os.path.join(scripts_dir, "articles-data.js"), "r", encoding="utf-8") as f:
        master_content = f.read()
        
    print(f"Master articles-data.js size: {len(master_content)} bytes")
    
    batch_files = ["batch1_articles.js", "batch2_articles.js", "batch3_articles.js", "batch4_articles.js"]
    total_batch_bytes = 0
    for bf in batch_files:
        p = os.path.join(scripts_dir, bf)
        if os.path.exists(p):
            sz = os.path.getsize(p)
            total_batch_bytes += sz
            print(f"  {bf}: {sz} bytes")
        else:
            print(f"  {bf}: NOT FOUND")
            
    print(f"Total batch bytes: {total_batch_bytes}")

if __name__ == "__main__":
    check_batch_files_consistency()
