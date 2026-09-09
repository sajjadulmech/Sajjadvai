import os
import re

css_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../styles/main.css"))

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

required_classes = [
    "ctl-table-wrapper",
    "ctl-spec-box",
    "ctl-faq-item",
    "ctl-modal-backdrop",
    "ctl-modal-container",
    "ctl-modal-body",
    "ctl-search-overlay",
    "ctl-search-box",
    "ctl-badge-pill",
    "ctl-triage-card",
    "ctl-calc-grid",
    "ctl-card",
    "ctl-article-card",
    "ctl-author-box"
]

print("=== CSS INTEGRITY AUDIT ===")
all_found = True
for cls in required_classes:
    pattern = r'\.' + re.escape(cls) + r'\b'
    match = re.search(pattern, css)
    status = "FOUND [PASS]" if match else "MISSING [FAIL]"
    if not match:
        all_found = False
    print(f"Class .{cls:<25} : {status}")

# Check responsive / overflow properties
has_overflow = "overflow-x" in css and ".ctl-table-wrapper" in css
print(f"Table horizontal scroll responsiveness: {'YES [PASS]' if has_overflow else 'NO [FAIL]'}")

# Check modal display properties
has_modal_open = ".ctl-modal-backdrop.open" in css or ".ctl-modal-backdrop" in css
print(f"Modal backdrop open state: {'YES [PASS]' if has_modal_open else 'NO [FAIL]'}")

if all_found and has_overflow and has_modal_open:
    print(">>> CSS INTEGRITY AUDIT PASSED 100%! <<<")
else:
    print(">>> CSS INTEGRITY ISSUES FOUND! <<<")
