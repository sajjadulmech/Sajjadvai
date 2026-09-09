# Appendix C: FTC Legal Disclosures & Compliance Guide

Under the Federal Trade Commission (FTC) Guides Concerning the Use of Endorsements and Testimonials in Advertising (16 CFR Part 255), commercial relationships between content creators and product merchants must be disclosed clearly and conspicuously.

---

## 1. The 3 Core Legal Principles

1. **Clear and Conspicuous:** Disclosures cannot be buried in fine print, hidden in low-contrast light gray text, or relegated solely to the site footer or a separate terms page.
2. **Above the Fold:** A reader must encounter the disclosure **before** they click any commercial recommendation or outbound affiliate link.
3. **Plain English:** Never use ambiguous jargon like "aff/collab" or "sponsored partners." State plainly that purchases made through links may result in a financial commission at no extra cost to the buyer.

---

## 2. Production HTML Disclosure Component

Place this component at the very beginning of every article's `contentHtml`:

```html
<!-- Production FTC Above-the-Fold Disclosure -->
<aside class="ctl-disclosure" aria-label="Affiliate Disclosure">
  <div class="ctl-disclosure-icon">ℹ️</div>
  <div class="ctl-disclosure-text">
    <strong>Editorial Transparency:</strong> ClearTapLab evaluates water treatment 
    systems through forensic engineering analysis of certified NSF/ANSI standards, 
    manufacturer installation manuals, and long-term failure logs. We do not accept 
    free review units. When you purchase equipment through our links, we may earn 
    an affiliate commission from our partners (such as SpringWell, Waterdrop, or Amazon) 
    at zero additional cost to you. This support funds our independent research.
  </div>
</aside>
```

---

## 3. CSS Component Styling (`styles/main.css`)

```css
.ctl-disclosure {
  display: flex;
  align-items: flex-start;
  gap: 0.875rem;
  background-color: #f0f9ff;
  border-left: 4px solid #0284c7;
  border-radius: 0 6px 6px 0;
  padding: 1rem 1.25rem;
  margin: 1.5rem 0 2rem 0;
  font-size: 0.875rem;
  line-height: 1.5;
  color: #334155;
}

.ctl-disclosure-icon {
  font-size: 1.15rem;
  flex-shrink: 0;
  margin-top: 1px;
}

.ctl-disclosure-text strong {
  color: #0f172a;
}
```
