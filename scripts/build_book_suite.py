#!/usr/bin/env python3
"""
scripts/build_book_suite.py
Compiles all 32 chapters into:
1. book/THE_COMPLETE_BOOK.md (Single master Markdown manuscript)
2. book/THE_COMPLETE_BOOK.html (Single-file printable HTML book with PDF styles)
3. book_reader.html (Interactive, zero-dependency offline web reader app)
"""

import os
import json
import re
import markdown

BOOK_DIR = "book"
MODULE_ORDER = [
    ("phase_1_battlefield", "Phase 1: The Reality Check & The Battlefield"),
    ("phase_2_products_intent", "Phase 2: Products, Competitors, and Intent"),
    ("phase_3_the_build", "Phase 3: The Build (Gemini as Brain, Antigravity as Hands)"),
    ("phase_4_content_engine", "Phase 4: The Content Engine (High E-E-A-T Without Fabrication)"),
    ("phase_5_launch_survival", "Phase 5: Launch, Survival, and The First Dollar"),
    ("phase_6_the_fork", "Phase 6: The Fork in the Road"),
    ("appendices", "Appendices: The Technical Reference Desk")
]

def load_chapters():
    chapters = []
    chapter_num = 1
    
    for mod_folder, mod_title in MODULE_ORDER:
        folder_path = os.path.join(BOOK_DIR, mod_folder)
        if not os.path.exists(folder_path):
            continue
        
        files = sorted([f for f in os.listdir(folder_path) if f.endswith(".md")])
        for f in files:
            full_path = os.path.join(folder_path, f)
            with open(full_path, "r", encoding="utf-8") as file:
                raw_content = file.read()
            
            # Extract chapter title from first line
            title_match = re.search(r"^#\s+(.+)$", raw_content, re.MULTILINE)
            title = title_match.group(1) if title_match else f"Chapter {chapter_num}"
            
            # Convert to HTML
            html_content = markdown.markdown(
                raw_content,
                extensions=["extra", "tables", "codehilite", "toc"]
            )
            
            chapters.append({
                "number": chapter_num,
                "module_id": mod_folder,
                "module_title": mod_title,
                "filename": f,
                "title": title,
                "markdown": raw_content,
                "html": html_content
            })
            chapter_num += 1
            
    return chapters

def build_complete_markdown(chapters):
    print("Building book/THE_COMPLETE_BOOK.md...")
    lines = [
        "# The AI-Powered Affiliate Operating System",
        "## A Part-Time Engineer’s Manual for Building, Launching, and Monetizing High-Trust Websites with Google Gemini and Google Antigravity\n",
        "**Author:** Antigravity Engineering & Strategy Press  ",
        "**Edition:** Production Release 1.0 (2026)  ",
        "**Target Milestone:** $0 \\to \\$50 \\to \\$100/\\text{month}$ and beyond  ",
        "**Case Study:** *ClearTapLab* (Residential Water Chemistry & Filtration Authority Platform)\n",
        "---\n",
        "## Table of Contents\n"
    ]
    
    # Table of contents
    current_mod = ""
    for ch in chapters:
        if ch["module_title"] != current_mod:
            current_mod = ch["module_title"]
            lines.append(f"\n### {current_mod}\n")
        lines.append(f"* [{ch['title']}](#{slugify(ch['title'])})")
        
    lines.append("\n---\n")
    
    # Body
    for ch in chapters:
        lines.append(f"\n<div id=\"{slugify(ch['title'])}\"></div>\n")
        lines.append(ch["markdown"])
        lines.append("\n\n---\n")
        
    out_path = os.path.join(BOOK_DIR, "THE_COMPLETE_BOOK.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[OK] Saved: {out_path} ({len(lines)} lines)")

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")

def build_interactive_reader(chapters):
    print("Building book_reader.html...")
    
    # Prepare JSON data for client-side app
    chapters_json = json.dumps([{
        "id": f"ch-{ch['number']}",
        "num": ch["number"],
        "modTitle": ch["module_title"],
        "title": ch["title"],
        "html": ch["html"]
    } for ch in chapters])
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The AI-Powered Affiliate Operating System — Interactive Reader</title>
  <style>
    :root {{
      --bg: #f8fafc;
      --surface: #ffffff;
      --sidebar-bg: #0f172a;
      --sidebar-text: #94a3b8;
      --sidebar-active: #38bdf8;
      --text: #334155;
      --heading: #0f172a;
      --border: #e2e8f0;
      --primary: #0284c7;
      --code-bg: #1e293b;
      --code-text: #f8fafc;
      --table-th: #f1f5f9;
      --font-size: 17px;
    }}
    body.dark {{
      --bg: #0b0f17;
      --surface: #111827;
      --sidebar-bg: #030712;
      --sidebar-text: #9ca3af;
      --sidebar-active: #38bdf8;
      --text: #cbd5e1;
      --heading: #f8fafc;
      --border: #1f2937;
      --primary: #38bdf8;
      --code-bg: #030712;
      --code-text: #e2e8f0;
      --table-th: #1f2937;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      font-size: var(--font-size);
      line-height: 1.7;
      display: flex;
      height: 100vh;
      overflow: hidden;
    }}
    /* SIDEBAR */
    #sidebar {{
      width: 340px;
      min-width: 340px;
      background-color: var(--sidebar-bg);
      color: var(--sidebar-text);
      display: flex;
      flex-direction: column;
      border-right: 1px solid var(--border);
      transition: all 0.2s ease;
      z-index: 100;
    }}
    .sidebar-header {{
      padding: 1.25rem 1.5rem;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }}
    .sidebar-title {{
      font-size: 0.95rem;
      font-weight: 700;
      color: #f8fafc;
      letter-spacing: 0.03em;
      text-transform: uppercase;
    }}
    .sidebar-subtitle {{
      font-size: 0.75rem;
      color: #64748b;
      margin-top: 0.25rem;
    }}
    .search-box {{
      padding: 0.75rem 1.25rem;
      border-bottom: 1px solid rgba(255,255,255,0.08);
    }}
    .search-input {{
      width: 100%;
      padding: 0.5rem 0.75rem;
      background: rgba(255,255,255,0.06);
      border: 1px solid rgba(255,255,255,0.12);
      border-radius: 6px;
      color: #f8fafc;
      font-size: 0.85rem;
      outline: none;
    }}
    .search-input:focus {{
      border-color: var(--sidebar-active);
    }}
    .nav-list {{
      flex: 1;
      overflow-y: auto;
      padding: 1rem 0;
      list-style: none;
    }}
    .nav-module-title {{
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      color: #64748b;
      padding: 0.75rem 1.5rem 0.25rem;
      letter-spacing: 0.05em;
    }}
    .nav-item {{
      padding: 0.5rem 1.5rem;
      font-size: 0.85rem;
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 0.5rem;
      color: var(--sidebar-text);
      transition: background 0.15s ease, color 0.15s ease;
      line-height: 1.4;
      border-left: 3px solid transparent;
    }}
    .nav-item:hover {{
      background: rgba(255,255,255,0.04);
      color: #f8fafc;
    }}
    .nav-item.active {{
      background: rgba(56, 189, 248, 0.1);
      color: var(--sidebar-active);
      border-left-color: var(--sidebar-active);
      font-weight: 600;
    }}
    .nav-item-num {{
      font-size: 0.75rem;
      opacity: 0.6;
      font-mono: monospace;
      margin-top: 1px;
    }}
    /* MAIN CONTENT */
    #main {{
      flex: 1;
      display: flex;
      flex-direction: column;
      overflow: hidden;
      background-color: var(--bg);
    }}
    /* TOP CONTROLS */
    .topbar {{
      height: 56px;
      background-color: var(--surface);
      border-bottom: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 2rem;
    }}
    .topbar-left {{
      display: flex;
      align-items: center;
      gap: 1rem;
    }}
    .sidebar-toggle-btn {{
      background: none;
      border: none;
      cursor: pointer;
      color: var(--text);
      font-size: 1.25rem;
      display: flex;
      align-items: center;
    }}
    .chapter-indicator {{
      font-size: 0.85rem;
      color: #64748b;
      font-weight: 500;
    }}
    .topbar-right {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}
    .btn-ctrl {{
      background: var(--bg);
      border: 1px solid var(--border);
      border-radius: 6px;
      padding: 0.35rem 0.65rem;
      font-size: 0.8rem;
      cursor: pointer;
      color: var(--text);
      font-weight: 500;
      transition: all 0.15s ease;
    }}
    .btn-ctrl:hover {{
      background: var(--border);
    }}
    /* CONTENT AREA */
    #reader-pane {{
      flex: 1;
      overflow-y: auto;
      padding: 2.5rem 3rem 5rem 3rem;
      scroll-behavior: smooth;
    }}
    .article-container {{
      max-width: 820px;
      margin: 0 auto;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 3rem 3.5rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.03);
    }}
    /* TYPOGRAPHY */
    h1 {{
      font-size: 1.85rem;
      font-weight: 800;
      color: var(--heading);
      margin-bottom: 1.5rem;
      line-height: 1.3;
      border-bottom: 2px solid var(--border);
      padding-bottom: 0.75rem;
    }}
    h2 {{
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--heading);
      margin: 2.25rem 0 1rem;
      border-bottom: 1px solid var(--border);
      padding-bottom: 0.4rem;
    }}
    h3 {{
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--heading);
      margin: 1.5rem 0 0.75rem;
    }}
    p {{
      margin-bottom: 1.2rem;
    }}
    ul, ol {{
      margin: 0.75rem 0 1.25rem 1.75rem;
    }}
    li {{
      margin-bottom: 0.4rem;
    }}
    blockquote {{
      border-left: 4px solid var(--primary);
      padding: 0.75rem 1.25rem;
      background: rgba(2, 132, 199, 0.05);
      border-radius: 0 6px 6px 0;
      margin: 1.25rem 0;
      font-style: italic;
    }}
    /* CODE BLOCKS */
    pre {{
      background-color: var(--code-bg);
      color: var(--code-text);
      padding: 1.25rem;
      border-radius: 6px;
      overflow-x: auto;
      margin: 1.25rem 0;
      font-family: ui-monospace, Menlo, Consolas, monospace;
      font-size: 0.88rem;
      line-height: 1.5;
    }}
    code {{
      font-family: ui-monospace, Menlo, Consolas, monospace;
      font-size: 0.9em;
      background: rgba(0,0,0,0.06);
      padding: 0.15rem 0.35rem;
      border-radius: 4px;
    }}
    body.dark code {{
      background: rgba(255,255,255,0.08);
    }}
    pre code {{
      background: transparent;
      padding: 0;
    }}
    /* TABLES */
    table {{
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      font-size: 0.9rem;
    }}
    th, td {{
      padding: 0.75rem 1rem;
      border: 1px solid var(--border);
      text-align: left;
    }}
    th {{
      background-color: var(--table-th);
      color: var(--heading);
      font-weight: 600;
    }}
    tr:nth-child(even) {{
      background-color: rgba(0,0,0,0.015);
    }}
    /* CALLOUT BOXES */
    .ctl-disclosure, aside {{
      background: rgba(2, 132, 199, 0.06);
      border-left: 4px solid var(--primary);
      padding: 1rem 1.25rem;
      border-radius: 4px;
      margin: 1.5rem 0;
      font-size: 0.9rem;
    }}
    /* NAV BUTTONS */
    .chapter-nav {{
      display: flex;
      justify-content: space-between;
      margin-top: 3rem;
      padding-top: 2rem;
      border-top: 1px solid var(--border);
    }}
    .nav-prev-btn, .nav-next-btn {{
      padding: 0.65rem 1.25rem;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 6px;
      color: var(--primary);
      font-weight: 600;
      cursor: pointer;
      font-size: 0.9rem;
      transition: all 0.15s ease;
    }}
    .nav-prev-btn:hover, .nav-next-btn:hover {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }}
    @media (max-width: 900px) {{
      #sidebar {{
        position: fixed;
        left: -340px;
        top: 0;
        bottom: 0;
      }}
      #sidebar.open {{
        left: 0;
      }}
      .article-container {{
        padding: 1.75rem;
      }}
      #reader-pane {{
        padding: 1rem;
      }}
    }}
  </style>
</head>
<body>

  <!-- SIDEBAR -->
  <aside id="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-title">AI Affiliate OS</div>
      <div class="sidebar-subtitle">32-Chapter Operating Manual</div>
    </div>
    <div class="search-box">
      <input type="text" id="search-input" class="search-input" placeholder="Search chapters...">
    </div>
    <ul id="nav-list" class="nav-list"></ul>
  </aside>

  <!-- MAIN VIEWPORT -->
  <main id="main">
    <header class="topbar">
      <div class="topbar-left">
        <button id="toggle-sidebar" class="sidebar-toggle-btn" title="Toggle Sidebar">☰</button>
        <span id="chapter-indicator" class="chapter-indicator">Module 1 · Chapter 1</span>
      </div>
      <div class="topbar-right">
        <button id="btn-font-down" class="btn-ctrl" title="Smaller Font">A−</button>
        <button id="btn-font-up" class="btn-ctrl" title="Larger Font">A+</button>
        <button id="btn-theme" class="btn-ctrl" title="Toggle Dark/Light Mode">🌙 Dark</button>
        <button id="btn-print" class="btn-ctrl" title="Print to PDF" onclick="window.print()">🖨️ PDF</button>
      </div>
    </header>

    <div id="reader-pane">
      <div class="article-container">
        <div id="article-body"></div>
        <div class="chapter-nav">
          <button id="btn-prev" class="nav-prev-btn">&larr; Previous</button>
          <button id="btn-next" class="nav-next-btn">Next &rarr;</button>
        </div>
      </div>
    </div>
  </main>

  <script>
    const CHAPTERS = {chapters_json};
    let currentIndex = 0;
    let currentFontSize = 17;

    const sidebar = document.getElementById("sidebar");
    const navList = document.getElementById("nav-list");
    const articleBody = document.getElementById("article-body");
    const chapterIndicator = document.getElementById("chapter-indicator");
    const readerPane = document.getElementById("reader-pane");
    const btnPrev = document.getElementById("btn-prev");
    const btnNext = document.getElementById("btn-next");
    const searchInput = document.getElementById("search-input");
    const btnTheme = document.getElementById("btn-theme");

    function renderNav(filter = "") {{
      navList.innerHTML = "";
      let lastMod = "";

      CHAPTERS.forEach((ch, idx) => {{
        if (filter && !ch.title.toLowerCase().includes(filter.toLowerCase()) && !ch.html.toLowerCase().includes(filter.toLowerCase())) {{
          return;
        }}

        if (ch.modTitle !== lastMod) {{
          lastMod = ch.modTitle;
          const modEl = document.createElement("li");
          modEl.className = "nav-module-title";
          modEl.textContent = ch.modTitle;
          navList.appendChild(modEl);
        }}

        const li = document.createElement("li");
        li.className = `nav-item ${{idx === currentIndex ? "active" : ""}}`;
        li.innerHTML = `<span class="nav-item-num">${{ch.num.toString().padStart(2, "0")}}</span><span>${{ch.title.replace(/^Chapter \\d+:\\s*/, "")}}</span>`;
        li.onclick = () => loadChapter(idx);
        navList.appendChild(li);
      }});
    }}

    function loadChapter(index) {{
      if (index < 0 || index >= CHAPTERS.length) return;
      currentIndex = index;
      const ch = CHAPTERS[currentIndex];
      
      articleBody.innerHTML = ch.html;
      chapterIndicator.textContent = `${{ch.modTitle}} · Chapter ${{ch.num}}`;
      readerPane.scrollTop = 0;

      // Update active sidebar state
      document.querySelectorAll(".nav-item").forEach((el, i) => {{
        el.classList.toggle("active", i === currentIndex);
      }});

      // Update prev/next buttons
      btnPrev.style.visibility = currentIndex > 0 ? "visible" : "hidden";
      btnNext.style.visibility = currentIndex < CHAPTERS.length - 1 ? "visible" : "hidden";

      if (currentIndex > 0) {{
        btnPrev.textContent = `← Ch ${{CHAPTERS[currentIndex - 1].num}}`;
      }}
      if (currentIndex < CHAPTERS.length - 1) {{
        btnNext.textContent = `Ch ${{CHAPTERS[currentIndex + 1].num}} →`;
      }}

      // Close mobile sidebar if open
      if (window.innerWidth < 900) {{
        sidebar.classList.remove("open");
      }}
    }}

    btnPrev.onclick = () => loadChapter(currentIndex - 1);
    btnNext.onclick = () => loadChapter(currentIndex + 1);

    document.getElementById("toggle-sidebar").onclick = () => {{
      sidebar.classList.toggle("open");
    }};

    document.getElementById("btn-font-up").onclick = () => {{
      if (currentFontSize < 24) {{
        currentFontSize += 1;
        document.documentElement.style.setProperty("--font-size", `${{currentFontSize}}px`);
      }}
    }};

    document.getElementById("btn-font-down").onclick = () => {{
      if (currentFontSize > 13) {{
        currentFontSize -= 1;
        document.documentElement.style.setProperty("--font-size", `${{currentFontSize}}px`);
      }}
    }};

    btnTheme.onclick = () => {{
      document.body.classList.toggle("dark");
      const isDark = document.body.classList.contains("dark");
      btnTheme.textContent = isDark ? "☀️ Light" : "🌙 Dark";
      localStorage.setItem("reader-theme", isDark ? "dark" : "light");
    }};

    searchInput.addEventListener("input", (e) => {{
      renderNav(e.target.value);
    }});

    // Restore saved theme
    if (localStorage.getItem("reader-theme") === "dark") {{
      document.body.classList.add("dark");
      btnTheme.textContent = "☀️ Light";
    }}

    // Initial load
    renderNav();
    loadChapter(0);
  </script>
</body>
</html>"""

    with open("book_reader.html", "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] Saved interactive reader: book_reader.html ({len(html)} bytes)")

def build_complete_html_book(chapters):
    print("Building book/THE_COMPLETE_BOOK.html...")
    
    body_parts = []
    body_parts.append("""<header style="text-align:center; padding: 4rem 1rem 3rem; border-bottom: 2px solid #0f172a; margin-bottom: 3rem;">
      <h1 style="font-size: 2.4rem; color: #0f172a; margin-bottom: 0.5rem;">The AI-Powered Affiliate Operating System</h1>
      <h2 style="font-size: 1.25rem; font-weight: 500; color: #475569; margin-bottom: 1.5rem;">A Part-Time Engineer’s Manual for Building, Launching, and Monetizing High-Trust Websites with Google Gemini and Google Antigravity</h2>
      <p style="font-size: 0.95rem; color: #64748b;">Production Release 1.0 (2026) · Complete 32-Chapter Edition</p>
    </header>""")
    
    # Master TOC
    body_parts.append("<div style='page-break-after: always;'><h2 style='border-bottom: 2px solid #0f172a; padding-bottom: 0.5rem;'>Table of Contents</h2><ul style='list-style:none; padding:0; margin:1.5rem 0;'>")
    for ch in chapters:
        ch_title_clean = re.sub(r"^Chapter \d+:\s*", "", ch["title"])
        mod_prefix = ch["module_title"].split(":")[0]
        body_parts.append(f"<li style='margin-bottom: 0.6rem;'><a href='#ch-{ch['number']}' style='color:#0284c7; text-decoration:none; font-weight:500;'>Chapter {ch['number']:02d}: {ch_title_clean}</a> <span style='color:#94a3b8; font-size:0.85em;'>({mod_prefix})</span></li>")
    body_parts.append("</ul></div>")

    for ch in chapters:
        body_parts.append(f"""
        <article id="ch-{ch['number']}" style="page-break-before: always; margin-top: 3rem; padding-top: 2rem;">
          <div style="font-size: 0.85rem; text-transform: uppercase; color: #0284c7; font-weight: 700; letter-spacing: 0.05em; margin-bottom: 0.5rem;">{ch['module_title']}</div>
          {ch['html']}
        </article>
        """)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>The AI-Powered Affiliate Operating System (Complete Edition)</title>
  <style>
    @media print {{
      @page {{ margin: 2cm; }}
      body {{ font-size: 11pt; line-height: 1.5; color: #000; }}
      h1, h2, h3 {{ page-break-after: avoid; }}
      table, pre, blockquote {{ page-break-inside: avoid; }}
      a {{ text-decoration: none; color: #000; }}
      .no-print {{ display: none; }}
    }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Georgia, serif;
      max-width: 860px;
      margin: 0 auto;
      padding: 2rem 1.5rem 6rem;
      color: #1e293b;
      line-height: 1.7;
      font-size: 17px;
      background: #ffffff;
    }}
    h1 {{ font-size: 2rem; color: #0f172a; margin-top: 2.5rem; margin-bottom: 1rem; }}
    h2 {{ font-size: 1.4rem; color: #0f172a; margin-top: 2rem; margin-bottom: 0.75rem; border-bottom: 1px solid #e2e8f0; padding-bottom: 0.3rem; }}
    h3 {{ font-size: 1.15rem; color: #0f172a; margin-top: 1.5rem; }}
    p {{ margin-bottom: 1.1rem; }}
    table {{ width: 100%; border-collapse: collapse; margin: 1.5rem 0; font-size: 0.9em; }}
    th, td {{ border: 1px solid #cbd5e1; padding: 0.6rem 0.8rem; text-align: left; }}
    th {{ background: #f8fafc; font-weight: 600; }}
    pre {{ background: #0f172a; color: #f8fafc; padding: 1.25rem; border-radius: 6px; overflow-x: auto; font-size: 0.85em; margin: 1.25rem 0; }}
    code {{ font-family: monospace; background: #f1f5f9; padding: 0.15rem 0.3rem; border-radius: 3px; font-size: 0.9em; }}
    pre code {{ background: transparent; padding: 0; color: inherit; }}
    blockquote {{ border-left: 4px solid #0284c7; padding-left: 1rem; margin: 1.25rem 0; color: #475569; }}
  </style>
</head>
<body>
  {"".join(body_parts)}
</body>
</html>"""

    out_path = os.path.join(BOOK_DIR, "THE_COMPLETE_BOOK.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"[OK] Saved: {out_path} ({len(full_html)} bytes)")

def main():
    chapters = load_chapters()
    print(f"Loaded {len(chapters)} chapters.")
    if len(chapters) == 0:
        print("Error: No chapters found.")
        return
        
    build_complete_markdown(chapters)
    build_interactive_reader(chapters)
    build_complete_html_book(chapters)
    
    # Mirror files to book and books directories
    import shutil
    os.makedirs("book", exist_ok=True)
    os.makedirs("books", exist_ok=True)
    shutil.copyfile("book_reader.html", "book/index.html")
    shutil.copyfile("book_reader.html", "books/index.html")
    shutil.copyfile("book/THE_COMPLETE_BOOK.html", "books/THE_COMPLETE_BOOK.html")
    print("[OK] Mirrored reader apps to book/index.html and books/index.html")
    
    print("\nAll formats built successfully!")

if __name__ == "__main__":
    main()
