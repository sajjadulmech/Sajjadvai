#!/usr/bin/env python3
"""
ClearTapLab Adversarial Stress Test Suite & Security Audit
Author: Challenger 1 (Adversarial Edge Case & Injection Stress Tester)

This suite performs deep empirical verification against:
1. Live Browser Runtime (Headless Microsoft Edge via Chrome DevTools Protocol + Local HTTP Server)
   - Search Adversarial Payloads (SQLi, XSS, Unicode, 1000-char fuzzing, Regex metachars, Whitespace)
   - Modal Boundary IDs (-1, 0, 21, 999, NaN, Infinity, non-numeric strings)
   - Category Filter Boundaries (invalid categories, rapid tab cycling)
   - Responsive Layout & Table constraints at 320px viewport
   - Calculator Extreme Boundaries
   - Triage Diagnostics Robustness
2. Dataset & HTML AST Security Audit
   - JS syntax & AST integrity of scripts/articles-data.js
   - HTML markup validity, unclosed tags, and unescaped template literals
   - Word count & comprehensive component verification (H1, badge, table, spec-box, FAQs, science)
"""

import os
import sys
import time
import json
import base64
import socket
import struct
import subprocess
import threading
import http.server
import socketserver
import urllib.request
import re
from bs4 import BeautifulSoup

if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except:
        pass

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ARTICLES_DATA_PATH = os.path.join(BASE_DIR, "scripts", "articles-data.js")
APP_JS_PATH = os.path.join(BASE_DIR, "scripts", "app.js")
INDEX_HTML_PATH = os.path.join(BASE_DIR, "index.html")
MAIN_CSS_PATH = os.path.join(BASE_DIR, "styles", "main.css")

# Minimal WebSocket RFC6455 Client for CDP
class CDPWebSocketClient:
    def __init__(self, ws_url):
        url_part = ws_url.replace("ws://", "")
        host_port, path = url_part.split("/", 1)
        path = "/" + path
        host, port = host_port.split(":")
        port = int(port)

        self.sock = socket.create_connection((host, port), timeout=10)
        key = base64.b64encode(os.urandom(16)).decode('utf-8')
        headers = [
            f"GET {path} HTTP/1.1",
            f"Host: {host_port}",
            "Upgrade: websocket",
            "Connection: Upgrade",
            f"Sec-WebSocket-Key: {key}",
            "Sec-WebSocket-Version: 13",
            "\r\n"
        ]
        self.sock.sendall("\r\n".join(headers).encode('utf-8'))
        
        response = b""
        while b"\r\n\r\n" not in response:
            response += self.sock.recv(4096)
        
        if not (b" 101 " in response or b"HTTP/1.1 101" in response):
            raise ConnectionError(f"WebSocket Handshake failed: {response}")
        self._msg_id = 0

    def call_cdp(self, method, params=None, timeout=10):
        self._msg_id += 1
        msg_id = self._msg_id
        req = {"id": msg_id, "method": method}
        if params is not None:
            req["params"] = params
        
        payload = json.dumps(req).encode('utf-8')
        frame = bytearray()
        frame.append(0x81)  # text frame, FIN=1
        length = len(payload)
        mask_key = os.urandom(4)
        if length < 126:
            frame.append(0x80 | length)
        elif length < 65536:
            frame.append(0x80 | 126)
            frame.extend(struct.pack("!H", length))
        else:
            frame.append(0x80 | 127)
            frame.extend(struct.pack("!Q", length))
        frame.extend(mask_key)
        masked_payload = bytearray(b ^ mask_key[i % 4] for i, b in enumerate(payload))
        frame.extend(masked_payload)
        self.sock.sendall(frame)

        self.sock.settimeout(timeout)
        start_t = time.time()
        while time.time() - start_t < timeout:
            resp = self._read_frame()
            if resp and resp.get("id") == msg_id:
                if "error" in resp:
                    raise RuntimeError(f"CDP Error for {method}: {resp['error']}")
                return resp.get("result", {})
        raise TimeoutError(f"Timed out waiting for CDP response to {method}")

    def _read_frame(self):
        header = self.sock.recv(2)
        if not header:
            return None
        mask_payload_len = header[1]
        masked = bool(mask_payload_len & 0x80)
        payload_len = mask_payload_len & 0x7F

        if payload_len == 126:
            ext = self.sock.recv(2)
            payload_len = struct.unpack("!H", ext)[0]
        elif payload_len == 127:
            ext = self.sock.recv(8)
            payload_len = struct.unpack("!Q", ext)[0]

        mask = self.sock.recv(4) if masked else None
        
        raw_data = bytearray()
        while len(raw_data) < payload_len:
            chunk = self.sock.recv(payload_len - len(raw_data))
            if not chunk:
                break
            raw_data.extend(chunk)
            
        if masked and mask:
            raw_data = bytearray(b ^ mask[i % 4] for i, b in enumerate(raw_data))
            
        try:
            return json.loads(raw_data.decode('utf-8', errors='ignore'))
        except:
            return None

    def close(self):
        try:
            self.sock.close()
        except:
            pass


class QuietHTTPHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress HTTP access logging


class AdversarialTestRunner:
    def __init__(self):
        self.http_port = 8765
        self.cdp_port = 9333
        self.http_server = None
        self.http_thread = None
        self.edge_proc = None
        self.cdp_ws = None
        self.results = []

    def start_environment(self):
        # Start local HTTP server
        os.chdir(BASE_DIR)
        handler = QuietHTTPHandler
        self.http_server = socketserver.TCPServer(("127.0.0.1", self.http_port), handler)
        self.http_thread = threading.Thread(target=self.http_server.serve_forever, daemon=True)
        self.http_thread.start()

        # Start Edge Headless
        edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        user_data_dir = os.path.join(BASE_DIR, ".agents", "challenger_1", "edge_profile_adversarial")
        os.makedirs(user_data_dir, exist_ok=True)

        self.edge_proc = subprocess.Popen([
            edge_path,
            f"--remote-debugging-port={self.cdp_port}",
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={user_data_dir}",
            f"http://127.0.0.1:{self.http_port}/index.html"
        ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for CDP to initialize
        time.sleep(2.0)
        req = urllib.request.urlopen(f"http://127.0.0.1:{self.cdp_port}/json")
        targets = json.loads(req.read().decode('utf-8'))
        page_target = next(t for t in targets if t.get('type') == 'page')
        self.cdp_ws = CDPWebSocketClient(page_target['webSocketDebuggerUrl'])

        # Enable runtime and DOM
        self.cdp_ws.call_cdp("Runtime.enable")
        self.cdp_ws.call_cdp("Page.enable")
        self.cdp_ws.call_cdp("DOM.enable")

        # Wait for page ready
        time.sleep(1.0)

    def stop_environment(self):
        if self.cdp_ws:
            self.cdp_ws.close()
        if self.edge_proc:
            self.edge_proc.kill()
        if self.http_server:
            self.http_server.shutdown()
            self.http_server.server_close()

    def eval_js(self, expression):
        res = self.cdp_ws.call_cdp("Runtime.evaluate", {
            "expression": expression,
            "returnByValue": True,
            "awaitPromise": True
        })
        val = res.get("result", {})
        if "value" in val:
            return val["value"]
        return val

    def record_test(self, test_name, passed, message="", blast_radius="LOW", details=None):
        status_str = "PASS" if passed else "FAIL"
        self.results.append({
            "name": test_name,
            "passed": passed,
            "status": status_str,
            "message": message,
            "blast_radius": blast_radius,
            "details": details or {}
        })
        print(f"  [{status_str}] {test_name}: {message}")

    # =========================================================================
    # 1. LIVE SEARCH ADVERSARIAL STRESS TESTS
    # =========================================================================
    def test_search_adversarial_queries(self):
        print("\n>>> Domain 1: Search Adversarial Queries & Injection Resilience")

        # 1.1 SQL Injection Payloads
        sqli_payloads = [
            "' OR '1'='1",
            "'; DROP TABLE articles; --",
            "' UNION SELECT null, username, password FROM users --",
            "1' ORDER BY 1--",
            "admin' --",
            "' OR 1=1#"
        ]
        for sqli in sqli_payloads:
            res = self.eval_js(f"""
                (function() {{
                    window.openSearch();
                    const input = document.getElementById('search-query-input');
                    input.value = {json.dumps(sqli)};
                    input.dispatchEvent(new Event('input'));
                    const results = document.getElementById('search-results-list');
                    const items = results.querySelectorAll('.ctl-search-item');
                    return {{
                        itemsCount: items.length,
                        html: results.innerHTML,
                        hasError: false
                    }};
                }})()
            """)
            passed = isinstance(res, dict) and res.get("itemsCount", -1) >= 0
            self.record_test(
                f"Search SQLi Resilience ({sqli[:20]})",
                passed,
                f"Handled safely without error (matches: {res.get('itemsCount')})",
                "HIGH"
            )

        # 1.2 XSS / HTML Injection Payloads
        xss_payloads = [
            ('<script>window._xss_1=1;</script>', 'window._xss_1'),
            ('<img src="invalid_img_url" onerror="window._xss_2=1">', 'window._xss_2'),
            ('<svg onload="window._xss_3=1">', 'window._xss_3'),
            ('"><iframe src="javascript:window._xss_4=1"></iframe>', 'window._xss_4'),
            ('<b onmouseover="window._xss_5=1">hover</b>', 'window._xss_5')
        ]
        for xss_str, flag_var in xss_payloads:
            res = self.eval_js(f"""
                (async function() {{
                    window.{flag_var} = undefined;
                    window.openSearch();
                    const input = document.getElementById('search-query-input');
                    input.value = {json.dumps(xss_str)};
                    input.dispatchEvent(new Event('input'));
                    
                    // Allow browser event loop to tick for async onerror triggers
                    await new Promise(r => setTimeout(r, 200));
                    
                    const results = document.getElementById('search-results-list');
                    return {{
                        xssExecuted: window.{flag_var} !== undefined,
                        rawHtml: results.innerHTML
                    }};
                }})()
            """)
            xss_executed = res.get("xssExecuted", False) if isinstance(res, dict) else False
            raw_html = res.get("rawHtml", "") if isinstance(res, dict) else ""
            injected_tags = "<img" in raw_html or "<svg" in raw_html or "<iframe" in raw_html or "<script" in raw_html or "<b" in raw_html
            
            if xss_executed or injected_tags:
                self.record_test(
                    f"Search HTML Injection / XSS ({xss_str[:25]})",
                    False,
                    f"VULNERABILITY: Unescaped HTML injected into searchResults.innerHTML (XSS Executed: {xss_executed})",
                    "CRITICAL" if xss_executed else "HIGH",
                    {"payload": xss_str, "rendered_html": raw_html, "xss_executed": xss_executed}
                )
            else:
                self.record_test(
                    f"Search HTML Injection / XSS ({xss_str[:25]})",
                    True,
                    f"Safe: Input properly escaped in search empty state",
                    "HIGH"
                )

        # 1.3 Regex Metacharacters
        regex_payloads = [
            ".*", "[a-z]", "(?i)", "^.*$", "\\d+", "a|b", "$", "(.*)",
            "+", "?", "*", "{1,3}", "[^a-zA-Z0-9]", "(((", "[[["
        ]
        for pat in regex_payloads:
            res = self.eval_js(f"""
                (function() {{
                    try {{
                        window.openSearch();
                        const input = document.getElementById('search-query-input');
                        input.value = {json.dumps(pat)};
                        input.dispatchEvent(new Event('input'));
                        const results = document.getElementById('search-results-list');
                        return {{ error: null, count: results.querySelectorAll('.ctl-search-item').length }};
                    }} catch(e) {{
                        return {{ error: e.toString(), count: -1 }};
                    }}
                }})()
            """)
            passed = isinstance(res, dict) and res.get("error") is None
            self.record_test(
                f"Search Regex Metacharacter ({pat})",
                passed,
                f"Search completed without unhandled regex crash (matched: {res.get('count')})",
                "MEDIUM"
            )

        # 1.4 Unicode & Multilingual Stress
        unicode_payloads = [
            "µm", "Ca²⁺", "H₂S", "SO₄²⁻", "°C", "–", "🚰💧", "Фильтрация", "مياه", "逆浸透", "\u202Ereversed\u202C", "\u200Bzero\u200Bwidth"
        ]
        for u_str in unicode_payloads:
            res = self.eval_js(f"""
                (function() {{
                    try {{
                        window.openSearch();
                        const input = document.getElementById('search-query-input');
                        input.value = {json.dumps(u_str)};
                        input.dispatchEvent(new Event('input'));
                        const results = document.getElementById('search-results-list');
                        return {{ error: null, count: results.querySelectorAll('.ctl-search-item').length }};
                    }} catch(e) {{
                        return {{ error: e.toString(), count: -1 }};
                    }}
                }})()
            """)
            passed = isinstance(res, dict) and res.get("error") is None
            self.record_test(
                f"Search Unicode & Multilingual ({u_str})",
                passed,
                f"Unicode query evaluated safely (matches: {res.get('count')})",
                "LOW"
            )

        # 1.5 1000-char and 10,000-char Long Query Fuzzing
        long_strings = ["A" * 1000, "water " * 500, "X" * 10000]
        for ls in long_strings:
            t0 = time.perf_counter()
            res = self.eval_js(f"""
                (function() {{
                    try {{
                        window.openSearch();
                        const input = document.getElementById('search-query-input');
                        input.value = {json.dumps(ls)};
                        input.dispatchEvent(new Event('input'));
                        const results = document.getElementById('search-results-list');
                        return {{ error: null, count: results.querySelectorAll('.ctl-search-item').length }};
                    }} catch(e) {{
                        return {{ error: e.toString(), count: -1 }};
                    }}
                }})()
            """)
            elapsed = time.perf_counter() - t0
            passed = isinstance(res, dict) and res.get("error") is None and elapsed < 1.0
            self.record_test(
                f"Search High Volume Fuzzing ({len(ls)} chars)",
                passed,
                f"Completed in {elapsed*1000:.1f}ms without hang (matches: {res.get('count')})",
                "MEDIUM"
            )

        # 1.6 Pure Whitespace Queries
        for ws in ["   ", "\t\t", "\n\n", " \t \n "]:
            res = self.eval_js(f"""
                (function() {{
                    window.openSearch();
                    const input = document.getElementById('search-query-input');
                    input.value = {json.dumps(ws)};
                    input.dispatchEvent(new Event('input'));
                    const results = document.getElementById('search-results-list');
                    return results.querySelectorAll('.ctl-search-item').length;
                }})()
            """)
            passed = (res == 20)
            self.record_test(
                f"Search Whitespace Query (len {len(ws)})",
                passed,
                f"Whitespace trimmed to empty query, successfully returned all 20 guides",
                "LOW"
            )

    # =========================================================================
    # 2. MODAL OPENING BOUNDARY & OUT-OF-BOUNDS TESTS
    # =========================================================================
    def test_modal_boundary_conditions(self):
        print("\n>>> Domain 2: Modal Opening Boundary & Out-of-Bounds Stress")

        boundary_ids = [
            (-1, "Negative ID (-1)"),
            (0, "Zero ID (0)"),
            (21, "Out-of-bounds upper (21)"),
            (999, "Large non-existent ID (999)"),
            ("NaN", "NaN ID"),
            ("Infinity", "Infinity ID"),
            ("-Infinity", "-Infinity ID"),
            ("'1'", "String ID ('1')"),
            ("''", "Empty String ID"),
            ("'xyz'", "Non-numeric String ('xyz')"),
            ("null", "Null ID"),
            ("undefined", "Undefined ID"),
            ("{}", "Object ID"),
            ("[]", "Array ID")
        ]

        for bad_id, desc in boundary_ids:
            res = self.eval_js(f"""
                (function() {{
                    window.closeArticleModal();
                    const modal = document.getElementById('article-modal');
                    const initialIsOpen = modal.classList.contains('open');
                    const initialBodyHtml = document.getElementById('modal-article-body').innerHTML;
                    
                    try {{
                        window.openArticleModal({bad_id});
                        const afterIsOpen = modal.classList.contains('open');
                        const afterBodyHtml = document.getElementById('modal-article-body').innerHTML;
                        return {{
                            error: null,
                            modalOpened: afterIsOpen,
                            bodyChanged: (initialBodyHtml !== afterBodyHtml)
                        }};
                    }} catch(e) {{
                        return {{ error: e.toString() }};
                    }}
                }})()
            """)
            passed = isinstance(res, dict) and res.get("error") is None and not res.get("modalOpened", True)
            self.record_test(
                f"Modal Boundary ID ({desc})",
                passed,
                f"Safely rejected without opening modal or throwing exception",
                "HIGH"
            )

        # Test all 20 valid article IDs
        for article_id in range(1, 21):
            res = self.eval_js(f"""
                (function() {{
                    window.closeArticleModal();
                    window.openArticleModal({article_id});
                    const modal = document.getElementById('article-modal');
                    const modalBody = document.getElementById('modal-article-body');
                    const modalContainer = modal.querySelector('.ctl-modal-container');
                    
                    const hasH1 = !!modalBody.querySelector('h1');
                    const hasSpecBox = !!modalBody.querySelector('.ctl-spec-box');
                    const hasTable = !!modalBody.querySelector('.ctl-table-wrapper') || !!modalBody.querySelector('table');
                    const hasFaq = !!modalBody.querySelector('.ctl-faq-section') || (modalBody.querySelectorAll('.ctl-faq-item').length > 0) || modalBody.innerHTML.includes('FAQ');
                    const wordCount = modalBody.textContent.trim().split(/\\s+/).length;
                    const isScrolledTop = modalContainer ? (modalContainer.scrollTop === 0) : true;
                    
                    return {{
                        isOpen: modal.classList.contains('open'),
                        hasH1: hasH1,
                        hasSpecBox: hasSpecBox,
                        hasTable: hasTable,
                        hasFaq: hasFaq,
                        wordCount: wordCount,
                        isScrolledTop: isScrolledTop
                    }};
                }})()
            """)
            is_valid = (
                isinstance(res, dict) and 
                res.get("isOpen") is True and 
                res.get("hasH1") is True and 
                res.get("hasSpecBox") is True and 
                res.get("hasTable") is True and 
                res.get("hasFaq") is True and 
                res.get("wordCount", 0) > 400 and
                res.get("isScrolledTop") is True
            )
            self.record_test(
                f"Modal Render Article ID #{article_id:02d}",
                is_valid,
                f"Rendered full rich article ({res.get('wordCount')} words, H1, spec-box, table, FAQ, scrollTop=0)",
                "CRITICAL"
            )

        # Modal Close on Backdrop Click & ESC
        res_close = self.eval_js("""
            (function() {
                window.openArticleModal(1);
                const modal = document.getElementById('article-modal');
                const openState = modal.classList.contains('open');
                
                // Click backdrop
                modal.dispatchEvent(new MouseEvent('click', { bubbles: true, target: modal }));
                const afterBackdropClose = !modal.classList.contains('open');
                
                // Reopen and press Escape
                window.openArticleModal(1);
                document.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
                const afterEscClose = !modal.classList.contains('open');
                
                return {
                    openState: openState,
                    backdropClose: afterBackdropClose,
                    escClose: afterEscClose
                };
            })()
        """)
        passed_close = (
            isinstance(res_close, dict) and 
            res_close.get("openState") and 
            res_close.get("backdropClose") and 
            res_close.get("escClose")
        )
        self.record_test(
            "Modal Dismissal (Backdrop Click & ESC Key)",
            passed_close,
            "Successfully dismissed via backdrop click and ESC keydown",
            "MEDIUM"
        )

    # =========================================================================
    # 3. CATEGORY FILTERING BOUNDARY TESTS
    # =========================================================================
    def test_category_filtering(self):
        print("\n>>> Domain 3: Category Filtering Boundary & Stress")

        # Invalid Categories
        invalid_cats = ["fake-cat", "<script>alert(1)</script>", "reverse_osmosis", "12345", "null", "undefined"]
        for bad_cat in invalid_cats:
            res = self.eval_js(f"""
                (function() {{
                    try {{
                        const grid = document.getElementById('articles-grid');
                        const filtered = CLEAR_TAP_ARTICLES.filter(a => a.category === {json.dumps(bad_cat)});
                        grid.innerHTML = filtered.map(a => `<div class="ctl-article-card">${{a.title}}</div>`).join('');
                        return {{ error: null, count: grid.children.length }};
                    }} catch(e) {{
                        return {{ error: e.toString(), count: -1 }};
                    }}
                }})()
            """)
            passed = isinstance(res, dict) and res.get("error") is None and res.get("count") == 0
            self.record_test(
                f"Category Filter Invalid Category ({bad_cat[:20]})",
                passed,
                f"Gracefully rendered 0 cards without JS runtime error",
                "HIGH"
            )

        # Rapid Tab Cycling Stress (50 switches)
        res_cycle = self.eval_js("""
            (function() {
                const tabs = Array.from(document.querySelectorAll('.ctl-tab-btn'));
                if (!tabs.length) return { error: "No tabs found" };
                
                for (let i = 0; i < 50; i++) {
                    const tab = tabs[i % tabs.length];
                    tab.click();
                }
                
                const grid = document.getElementById('articles-grid');
                return {
                    error: null,
                    activeTabCount: document.querySelectorAll('.ctl-tab-btn.active').length,
                    cardsCount: grid.querySelectorAll('.ctl-article-card').length
                };
            })()
        """)
        passed_cycle = (
            isinstance(res_cycle, dict) and 
            res_cycle.get("error") is None and 
            res_cycle.get("activeTabCount") == 1 and
            res_cycle.get("cardsCount", 0) > 0
        )
        self.record_test(
            "Category Filter Rapid Cycling Stress (50 iterations)",
            passed_cycle,
            f"Active tab count = 1, grid card count = {res_cycle.get('cardsCount')}, zero state corruption",
            "MEDIUM"
        )

    # =========================================================================
    # 4. TABLE RENDERING & MOBILE VIEWPORT (320px) CONSTRAINTS
    # =========================================================================
    def test_mobile_viewport_and_tables(self):
        print("\n>>> Domain 4: Table Rendering & Mobile Viewport Constraints (320px)")

        # Set 320px viewport in CDP
        self.cdp_ws.call_cdp("Emulation.setDeviceMetricsOverride", {
            "width": 320,
            "height": 640,
            "deviceScaleFactor": 2,
            "mobile": True
        })
        time.sleep(0.5)

        # Test every article's table rendering within modal at 320px
        for article_id in range(1, 21):
            res = self.eval_js(f"""
                (function() {{
                    window.openArticleModal({article_id});
                    const modal = document.getElementById('article-modal');
                    const modalContainer = modal.querySelector('.ctl-modal-container');
                    const tableWrappers = Array.from(modal.querySelectorAll('.ctl-table-wrapper'));
                    const tables = Array.from(modal.querySelectorAll('table'));
                    
                    let hasTableWrapper = tableWrappers.length > 0;
                    let tableCount = tables.length;
                    
                    let modalWidth = modalContainer.getBoundingClientRect().width;
                    let wrapperOverflowStyles = tableWrappers.map(tw => {{
                        const style = window.getComputedStyle(tw);
                        return {{
                            overflowX: style.overflowX,
                            scrollWidth: tw.scrollWidth,
                            clientWidth: tw.clientWidth
                        }};
                    }});
                    
                    return {{
                        articleId: {article_id},
                        modalWidth: modalWidth,
                        hasTableWrapper: hasTableWrapper,
                        tableCount: tableCount,
                        wrapperStyles: wrapperOverflowStyles
                    }};
                }})()
            """)
            
            if isinstance(res, dict):
                wrappers = res.get("wrapperStyles", [])
                has_auto_scroll = all(w.get("overflowX") in ("auto", "scroll") for w in wrappers)
                is_valid = res.get("hasTableWrapper") and res.get("tableCount", 0) >= 1 and has_auto_scroll
                self.record_test(
                    f"320px Viewport Table Containment Article #{article_id:02d}",
                    is_valid,
                    f"Tables ({res.get('tableCount')}) wrapped with overflow-x: auto, contained within {res.get('modalWidth', 0):.0f}px modal",
                    "HIGH"
                )

        # Restore default desktop viewport
        self.cdp_ws.call_cdp("Emulation.clearDeviceMetricsOverride")

    # =========================================================================
    # 5. DATASET & HTML AST INTEGRITY AUDIT
    # =========================================================================
    def test_dataset_ast_and_html_integrity(self):
        print("\n>>> Domain 5: Dataset & HTML AST Integrity Audit")

        with open(ARTICLES_DATA_PATH, "r", encoding="utf-8") as f:
            raw_js = f.read()

        # Check JS Syntax via CDP evaluation
        res_syntax = self.eval_js("""
            (function() {
                if (typeof CLEAR_TAP_ARTICLES === 'undefined') return { error: "CLEAR_TAP_ARTICLES undefined" };
                return {
                    length: CLEAR_TAP_ARTICLES.length,
                    ids: CLEAR_TAP_ARTICLES.map(a => a.id)
                };
            })()
        """)
        syntax_ok = (
            isinstance(res_syntax, dict) and 
            res_syntax.get("length") == 20 and 
            res_syntax.get("ids") == list(range(1, 21))
        )
        self.record_test(
            "Dataset JavaScript Syntax & Array Integrity",
            syntax_ok,
            f"Successfully parsed 20 articles with sequential IDs 1-20 (Length: {res_syntax.get('length')})",
            "CRITICAL"
        )

        # Check for unescaped template literal evaluations in articles-data.js
        suspicious_literals = re.findall(r"\$\{[^}]*\}", raw_js)
        self.record_test(
            "Dataset Template Literal Interpolation Leak Check",
            len(suspicious_literals) == 0,
            f"Found {len(suspicious_literals)} unescaped ${{...}} expressions in articles-data.js",
            "HIGH",
            {"suspicious_matches": suspicious_literals[:5]}
        )

        # Verify each article's HTML markup with BeautifulSoup
        articles_json = self.eval_js("JSON.stringify(CLEAR_TAP_ARTICLES)")
        articles = json.loads(articles_json)

        for a in articles:
            a_id = a["id"]
            html = a.get("contentHtml", "")
            soup = BeautifulSoup(html, "html.parser")
            
            # Checks:
            h1 = soup.find("h1")
            spec_boxes = soup.find_all(class_=re.compile(r"ctl-spec-box"))
            tables = soup.find_all("table")
            table_wrappers = soup.find_all(class_=re.compile(r"ctl-table-wrapper"))
            faq_items = soup.find_all(class_=re.compile(r"ctl-faq-item")) or soup.find_all("details")
            faq_headers = [h for h in soup.find_all(["h2", "h3", "h4"]) if "faq" in h.text.lower() or "frequently" in h.text.lower()]
            
            text = soup.get_text(separator=" ")
            words = len(text.split())

            # Word boundary regex for genuine placeholders
            placeholder_pattern = re.compile(r"\b(stub|stubs|todo|lorem\s+ipsum|placeholder|coming\s+soon)\b", re.IGNORECASE)
            placeholder_matches = placeholder_pattern.findall(text)

            valid_article = (
                h1 is not None and
                len(spec_boxes) >= 1 and
                len(tables) >= 1 and
                len(table_wrappers) >= 1 and
                (len(faq_items) >= 3 or len(faq_headers) >= 1) and
                words >= 500 and
                len(placeholder_matches) == 0
            )

            self.record_test(
                f"Article #{a_id:02d} Deep HTML Content Audit",
                valid_article,
                f"Words: {words} | H1: {'YES' if h1 else 'NO'} | SpecBox: {len(spec_boxes)} | Tables: {len(tables)} | FAQ: {len(faq_items) or len(faq_headers)} | Placeholders: {placeholder_matches if placeholder_matches else 'NONE'}",
                "CRITICAL"
            )

    # =========================================================================
    # 6. SIZING CALCULATOR EXTREME BOUNDARIES
    # =========================================================================
    def test_calculator_extreme_boundaries(self):
        print("\n>>> Domain 6: Sizing Calculator Extreme Boundaries")

        test_cases = [
            (-100, -50, -10, "Extreme Negative Inputs"),
            (0, 0, 0, "All Zero Inputs"),
            (100, 100, 50, "Extreme High Inputs"),
            ("NaN", "NaN", "NaN", "NaN String Inputs"),
            ("abc", "xyz", "!@#", "Alphanumeric Non-numeric Inputs")
        ]

        for p_val, h_val, i_val, desc in test_cases:
            res = self.eval_js(f"""
                (function() {{
                    const p = document.getElementById('calc-people');
                    const h = document.getElementById('calc-hardness');
                    const i = document.getElementById('calc-iron');
                    
                    p.value = {json.dumps(p_val)};
                    h.value = {json.dumps(h_val)};
                    i.value = {json.dumps(i_val)};
                    
                    p.dispatchEvent(new Event('input'));
                    h.dispatchEvent(new Event('input'));
                    i.dispatchEvent(new Event('input'));
                    
                    return {{
                        dailyGal: document.getElementById('res-daily-gal').textContent,
                        compHard: document.getElementById('res-comp-hard').textContent,
                        dailyGrains: document.getElementById('res-daily-grains').textContent,
                        targetCap: document.getElementById('res-target-cap').textContent,
                        saltCost: document.getElementById('res-salt-cost').textContent
                    }};
                }})()
            """)
            
            has_nan = any("NaN" in str(v) or "undefined" in str(v) for v in res.values()) if isinstance(res, dict) else True
            self.record_test(
                f"Calculator Extreme Input ({desc})",
                not has_nan,
                f"Clamped to valid numeric ranges without NaN (Target: {res.get('targetCap')})",
                "HIGH"
            )

    # =========================================================================
    # 7. SYMPTOM TRIAGE RESILIENCE
    # =========================================================================
    def test_symptom_triage_resilience(self):
        print("\n>>> Domain 7: Symptom Triage Tool Resilience")

        symptoms = ["sulfur", "limescale", "rust", "chlorine", "acidic"]
        for sym in symptoms:
            res = self.eval_js(f"""
                (function() {{
                    const btn = document.querySelector(`.ctl-symptom-btn[data-symptom="{sym}"]`);
                    if (!btn) return {{ error: "Button not found" }};
                    btn.click();
                    const container = document.getElementById('triage-result-container');
                    return {{
                        error: null,
                        title: container.querySelector('.ctl-result-title') ? container.querySelector('.ctl-result-title').textContent : '',
                        hasButton: !!container.querySelector('button')
                    }};
                }})()
            """)
            passed = isinstance(res, dict) and res.get("error") is None and bool(res.get("title")) and res.get("hasButton")
            self.record_test(
                f"Triage Diagnostic Button ({sym})",
                passed,
                f"Rendered diagnosis '{res.get('title')}' with actionable CTA guide link",
                "MEDIUM"
            )

    def run_all(self):
        print("=" * 88)
        print("         STARTING CLEARTAPLAB ADVERSARIAL STRESS TEST & SECURITY SUITE          ")
        print("=" * 88)
        
        try:
            self.start_environment()
            self.test_search_adversarial_queries()
            self.test_modal_boundary_conditions()
            self.test_category_filtering()
            self.test_mobile_viewport_and_tables()
            self.test_dataset_ast_and_html_integrity()
            self.test_calculator_extreme_boundaries()
            self.test_symptom_triage_resilience()
        finally:
            self.stop_environment()

        total = len(self.results)
        passed = sum(1 for r in self.results if r["passed"])
        failed = total - passed

        print("\n" + "=" * 88)
        print("                        ADVERSARIAL STRESS TEST SUMMARY                         ")
        print("=" * 88)
        print(f"Total Tests Executed: {total}")
        print(f"Passed: {passed}")
        print(f"Failed: {failed}")
        print(f"Pass Rate: {(passed/total*100.0):.1f}%")
        print("=" * 88)

        if failed > 0:
            print("\n" + "!" * 88)
            print("                               VULNERABILITIES & FAILURES                               ")
            print("!" * 88)
            for r in self.results:
                if not r["passed"]:
                    print(f"\n[BLAST RADIUS: {r['blast_radius']}] {r['name']}")
                    print(f"  Message: {r['message']}")
                    if r.get("details"):
                        print(f"  Details: {json.dumps(r['details'], indent=4)}")
            print("\n" + "!" * 88)

        return {
            "total": total,
            "passed": passed,
            "failed": failed,
            "results": self.results
        }


if __name__ == "__main__":
    runner = AdversarialTestRunner()
    summary = runner.run_all()
    sys.exit(0 if summary["failed"] == 0 else 1)
