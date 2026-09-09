# Chapter 12: Antigravity Setup: Rules, Skills, and Workspace Configuration

---

## 1. What You Will Learn

* The core architecture of Google Antigravity: Context engine, planning mode, and file system permissions.
* How to configure `.agents/rules/` (`AGENTS.md` / `GEMINI.md`) to establish firm boundaries for code style, affiliate compliance, and editorial standards.
* The mechanics of **Progressive Disclosure Skills**: equipping Antigravity with specialized workflows without overwhelming the context window.
* How to use Antigravity's **Planning Mode** (`implementation_plan.md` and `walkthrough.md`) to audit changes before any file is modified.
* How to configure terminal sandboxing and security permissions for reliable local execution.

---

## 2. Why This Matters

When working with an autonomous AI coding assistant, vague instructions lead to drift:
* The agent may introduce unnecessary dependencies (like heavy npm packages, jQuery, or CSS frameworks) that slow down your site.
* The agent may forget to add `rel="sponsored nofollow"` to affiliate links.
* The agent may overwrite your design system tokens with inconsistent inline styling.
* The agent may invent files in non-standard directories.

Google Antigravity addresses this problem through **Contextual Rules and Progressive Disclosure**. By configuring your workspace with a persistent `AGENTS.md` file and specialized skills, you establish an operating framework that governs every tool call, code generation, and file edit. 

The agent operates not as an unpredictable conversationalist, but as a disciplined pair programmer adhering strictly to your engineering specifications.

---

## 3. The Concept

### The Antigravity Customization Architecture

```
+───────────────────────────────────────────────────────────────────────────+
| ANTIGRAVITY ENGINE ARCHITECTURE                                           |
+───────────────────────────────────────────────────────────────────────────+
  │
  ├── 1. ALWAYS-ON RULES (.agents/rules/AGENTS.md)
  │      └── Automatically injected into every agent turn.
  │      └── Enforces coding style, performance thresholds, and disclosures.
  │
  ├── 2. PROGRESSIVE DISCLOSURE SKILLS (skills/<skill-name>/SKILL.md)
  │      └── Injects only name and description until triggered.
  │      └── Loads full multi-step execution SOP only when needed.
  │
  ├── 3. PLANNING MODE (implementation_plan.md)
  │      └── Triggered for multi-file edits or complex refactors.
  │      └── Details proposed changes, diffs, and verification steps.
  │      └── User Review Gate: Agent pauses until you explicitly approve.
  │
  └── 4. VERIFICATION HARNESS (walkthrough.md & tests/)
         └── Terminal execution runs Python/DOM unit tests.
         └── Agent documents results, diffs, and verification status.
```

### Key Antigravity Settings

In Antigravity's settings configuration:
* **Tool Execution Policy:** Controls how terminal commands are executed. Set to `always-proceed` for trusted local scripts (like Python test runners) or `request-review` for package installations.
* **Terminal Sandboxing:** Isolates command execution to protect system directories outside your workspace.
* **Workspace Boundaries:** Restricts file reads and writes strictly to your project root folder (`allow-workspace-only`).

---

## 4. Step-by-Step Process: Hardening the Workspace

```
Step 1: Create the .agents/rules/ Directory at the Root of Your Project.
Step 2: Author AGENTS.md with Strict Architectural and Compliance Constraints.
Step 3: Define Custom Skills in skills/ for Specialized Multi-Step Tasks.
Step 4: Verify Planning Mode Behavior by Triggering a Multi-File Task.
Step 5: Execute a Verification Test via the Terminal to Confirm Permissions.
```

---

## 5. Real Example: ClearTapLab's AGENTS.md

The **ClearTapLab** codebase is protected by the following production `AGENTS.md` file located in `.agents/rules/`:

```markdown
# ClearTapLab Agent Engineering Rules

## 1. Zero External Dependencies
- Use vanilla ES6+ JavaScript, semantic HTML5, and vanilla CSS3 design tokens.
- Never install or reference external CSS/JS CDNs (no Tailwind CDN, Bootstrap, React, or jQuery).
- All icons must be inline SVGs.

## 2. Affiliate Compliance & Link Hygiene
- Every outbound merchant link must have: `target="_blank" rel="sponsored nofollow noopener"`.
- Every guide must include the `.ctl-disclosure` component immediately beneath the article header.
- Never cloak, shorten, or redirect Amazon affiliate links through local scripts.

## 3. Responsive Layout Standards
- Mobile viewports (down to 320px) must never trigger horizontal scrolling.
- All comparison tables must be wrapped in `<div class="ctl-table-wrapper">` with `min-width: 580px`.
- Interactive sliders and inputs must have minimum touch targets of 44x44px.

## 4. Verification Protocol
- Never mark a feature complete without running `python tests/run_e2e_tests.py`.
- If an automated test fails, diagnose and fix the root cause; never bypass or delete test assertions.
```

Whenever Antigravity opens, edits, or generates code in the ClearTapLab repository, these constraints are enforced automatically.

---

## 6. Gemini Workflow: AGENTS.md Rule Generator

Use Gemini to generate a customized `AGENTS.md` rule file tailored to your specific micro-niche and design system.

```
+-------------------------------------------------------------------------+
| GEMINI PROMPT: AGENTS.MD RULE ARCHITECT                                 |
+-------------------------------------------------------------------------+
| Role: Principal Systems Architect & AI Safety Engineer                 |
| Task: Generate a comprehensive, unambiguous AGENTS.md rules file to     |
|       govern Google Antigravity during affiliate site development.      |
+-------------------------------------------------------------------------+
```

### Exact Prompt

```markdown
You are a principal systems architect and AI safety engineer.

I am building a high-trust, zero-maintenance affiliate website using Google Antigravity.
- Niche: [INSERT NICHE, e.g., Residential Water Filtration]
- Stack: Vanilla HTML5, Vanilla CSS3 (custom properties/tokens), Vanilla ES6+ JavaScript. Zero external frameworks.
- Primary Monetization: Direct Specialty Affiliate Programs + Amazon Associates.

Generate a comprehensive, unambiguous .agents/rules/AGENTS.md file that enforces:
1. Technical Architecture Standards: Zero third-party dependencies, accessible semantic markup, modular CSS tokens, fast loading speeds.
2. Affiliate Legal Compliance: Mandatory above-the-fold disclosures, strict `rel="sponsored nofollow noopener"` link tagging, prohibition of deceptive cloaking.
3. Editorial Integrity: Strict ban on AI hallucinations of firsthand physical testing; requirements for citing verified certifications (NSF/ANSI, EPA, UL).
4. Responsive UX Constraints: Mandatory table wrappers for mobile horizontal scrolling, minimum 44px touch targets.
5. Verification Protocol: Mandatory execution of local Python test runners before marking tasks done.
```

### Expected Output

Gemini generates a structured, production-ready `AGENTS.md` file ready to be saved into your project's `.agents/rules/` directory.

---

## 7. Antigravity Workflow: Workspace Verification & Rule Injection

Instruct Antigravity to create `.agents/rules/AGENTS.md` and verify that its context engine correctly enforces the rules.

### Antigravity Steps

1. Open **Antigravity IDE**.
2. Propose creating `.agents/rules/AGENTS.md`.
3. Test rule adherence by asking Antigravity to generate a sample affiliate link component.

### Exact Antigravity Prompt

```markdown
Write the file .agents/rules/AGENTS.md using our high-trust engineering specification.

Then, to verify rule enforcement:
Generate a sample product recommendation callout card in HTML and CSS for a $799 Waterdrop G3P800 RO system with an outbound affiliate button.

Verify that:
1. The affiliate button strictly includes rel="sponsored nofollow noopener".
2. The markup uses our .ctl- CSS naming convention and design tokens.
3. No external CSS frameworks or scripts are imported.
```

### Code Generated by Antigravity

```html
<!-- Verified Rule-Compliant Product Card Component -->
<div class="ctl-product-card">
  <div class="ctl-product-badge">Top Pick: Tankless Reverse Osmosis</div>
  <h3 class="ctl-product-title">Waterdrop G3P800</h3>
  <div class="ctl-product-specs">
    <span class="ctl-spec-pill">800 GPD Flow</span>
    <span class="ctl-spec-pill">3:1 Pure-to-Drain</span>
    <span class="ctl-spec-pill">NSF 58 Certified</span>
  </div>
  <p class="ctl-product-desc">
    High-efficiency under-sink tankless RO system featuring an internal booster pump, digital TDS monitoring faucet, and 0.0001-micron filtration cutoff.
  </p>
  <div class="ctl-product-pricing">
    <span class="ctl-price-retail">$799.00</span>
    <a href="https://shareasale.com/r.cfm?b=12345&u=67890&m=11111" 
       target="_blank" 
       rel="sponsored nofollow noopener" 
       class="ctl-btn ctl-btn-primary">
      Check Live Price on Waterdrop &rarr;
    </a>
  </div>
</div>
```

---

## 8. Human Verification

Verify your Antigravity environment with these three checks:

1. **Rule Discovery Confirmation:** In the Antigravity Chat panel, type `@rules`. Confirm that `AGENTS.md` appears in the list of recognized project rules.
2. **Planning Mode Test:** Ask Antigravity to perform a task touching multiple files (e.g., *"Add a new category filter tab and update the article count"*). Verify that Antigravity enters Planning Mode, displays `implementation_plan.md`, and **waits for your approval** before writing files.
3. **Terminal Execution Safety:** Run a benign command via Antigravity (e.g., `python -c "print('Antigravity connected')"`). Confirm that the command executes cleanly in your project environment.

---

## 9. Common Mistakes

* **Leaving the Rules File Empty:** Relying on memory or informal prompt reminders instead of a formal `AGENTS.md`. Without a rules file, the agent will inevitably introduce conflicting styles and code bloat.
* **Auto-Approving Complex Plans:** Clicking "Proceed" on implementation plans without reading the proposed file changes. Take 30 seconds to review file diffs in Planning Mode.
* **Allowing External Frameworks:** Letting the agent install heavy frameworks (e.g., adding React or Tailwind via npm for a simple 20-guide static site). This creates unnecessary build steps and maintenance overhead.
* **Scattering Rules Across Many Files:** Creating 15 micro-rule files that contradict each other. Consolidate your core coding, styling, and compliance rules into one clean, well-organized `AGENTS.md`.

---

## 10. Checklist

- [ ] `.agents/rules/AGENTS.md` is present at the root of my project.
- [ ] Coding rules mandate zero external dependencies and semantic HTML5/CSS3.
- [ ] Compliance rules strictly enforce `rel="sponsored nofollow noopener"` and above-the-fold disclosures.
- [ ] Antigravity's Planning Mode is active and pausing for approval on multi-file changes.
- [ ] Terminal execution is verified and functioning cleanly.

---

## 11. Practical Exercise

1. Create the directory `.agents/rules/` in your project if it does not already exist.
2. Populate `.agents/rules/AGENTS.md` with your site’s coding and compliance standards.
3. Open Antigravity, trigger a small test prompt, and verify that the agent references your rules in its thought process.
4. Verify that all generated links include `rel="sponsored nofollow noopener"`.
