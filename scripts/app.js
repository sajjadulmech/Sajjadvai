/**
 * ClearTapLab Web Application Main Logic
 * Interactive Tools: Symptom Triage, Softener Sizing Calculator, Live Search & Article Reader
 * Strictly Enforced: Zero Hardcoded Inline Styles, Pure CSS Classes, Pure Flexbox
 */

document.addEventListener('DOMContentLoaded', () => {
  initSymptomTriage();
  initCalculator();
  initArticleGrid();
  initLiveSearch();
  initModalReader();
  initMobileDrawer();
  initCategoryTriggers();
});

/* ==========================================================================
   1. Interactive Symptom Diagnostic Triage Tool
   ========================================================================== */
const SYMPTOM_DATA = {
  sulfur: {
    title: "Rotten Egg / Sulfur Odor",
    cause: "Dissolved Hydrogen Sulfide gas (H2S) from groundwater sulfur bacteria or water heater sacrificial magnesium anode rods.",
    epa: "Secondary Aesthetic Guideline: < 0.05 PPM (Odor detectable at 0.0005 PPM)",
    fix: "Air-Injection Oxidation (AIO) or Powered Titanium Anode Rod",
    articleId: 3,
    pillClass: "badge-warning",
    formula: "H2S + 2O2 ---> SO4(2-) + 2H(+)"
  },
  limescale: {
    title: "White Chalky Limescale & Fixture Crust",
    cause: "High concentration of dissolved Calcium (Ca2+) and Magnesium (Mg2+) carbonates exceeding 7 GPG (~120 PPM).",
    epa: "No Health Limit; Plumbing Threshold > 7 GPG causes pipe scale & heater burnout",
    fix: "Ion-Exchange Water Softener or Salt-Free TAC Water Conditioner",
    articleId: 5,
    pillClass: "badge-warning",
    formula: "Ca(2+) + 2HCO3(-) ---> CaCO3(v) + H2O + CO2"
  },
  scale: {
    title: "White Chalky Limescale & Fixture Crust",
    cause: "High concentration of dissolved Calcium (Ca2+) and Magnesium (Mg2+) carbonates exceeding 7 GPG (~120 PPM).",
    epa: "No Health Limit; Plumbing Threshold > 7 GPG causes pipe scale & heater burnout",
    fix: "Ion-Exchange Water Softener or Salt-Free TAC Water Conditioner",
    articleId: 5,
    pillClass: "badge-warning",
    formula: "Ca(2+) + 2HCO3(-) ---> CaCO3(v) + H2O + CO2"
  },
  rust: {
    title: "Orange / Red Stains & Metallic Aftertaste",
    cause: "Dissolved clear-water ferrous iron (Fe2+) or precipitated red-water ferric iron (Fe3+) exceeding 0.3 PPM.",
    epa: "EPA: Secondary Standard is 0.3 PPM (mg/L)",
    fix: "Air-Injection Oxidation (AIO) + 5um Depth Sediment Filter",
    articleId: 6,
    pillClass: "badge-warning",
    formula: "4Fe(2+) + O2 + 10H2O ---> 4Fe(OH)3(v) + 8H(+)"
  },
  iron: {
    title: "Orange / Red Stains & Metallic Aftertaste",
    cause: "Dissolved clear-water ferrous iron (Fe2+) or precipitated red-water ferric iron (Fe3+) exceeding 0.3 PPM.",
    epa: "EPA: Secondary Standard is 0.3 PPM (mg/L)",
    fix: "Air-Injection Oxidation (AIO) + 5um Depth Sediment Filter",
    articleId: 6,
    pillClass: "badge-warning",
    formula: "4Fe(2+) + O2 + 10H2O ---> 4Fe(OH)3(v) + 8H(+)"
  },
  chlorine: {
    title: "Bleach / Chlorine Chemical Taste & Odor",
    cause: "Municipal disinfection residuals: Free Chlorine or Chloramines (chlorine + ammonia) and DBPs.",
    epa: "EPA Maximum Residual Disinfectant Level (MRDL): 4.0 PPM",
    fix: "Multi-Stage Catalytic Carbon Block or Under-Sink RO System",
    articleId: 2,
    pillClass: "badge-pill",
    formula: "NH2Cl + C* ---> NH3 + C*O + Cl(-)"
  },
  acidic: {
    title: "Blue-Green Copper Stains & Pinhole Pipe Leaks",
    cause: "Corrosive acidic water (pH < 6.5) dissolving internal copper plumbing pipes and brass fittings.",
    epa: "EPA Secondary Guideline: pH 6.5 - 8.5 (Ideal: 7.2 - 7.8)",
    fix: "Calcite / Corosex Acid Neutralizing Media Tank",
    articleId: 13,
    pillClass: "badge-warning",
    formula: "CaCO3 + 2H(+) ---> Ca(2+) + H2O + CO2"
  }
};

function initSymptomTriage() {
  const buttons = document.querySelectorAll('.ctl-symptom-btn');
  const resultCard = document.getElementById('triage-result-container');
  if (!buttons.length || !resultCard) return;

  function renderSymptom(key) {
    const data = SYMPTOM_DATA[key];
    if (!data) return;

    resultCard.innerHTML = `
      <div class="ctl-triage-result">
        <div class="ctl-triage-left">
          <div class="badge-pill ${data.pillClass}">
            <span class="bullet-dot"></span>
            <span>Diagnosed Mechanism</span>
          </div>
          <div class="ctl-result-title">${data.title}</div>
          <p class="ctl-triage-cause">
            <strong>Likely Cause:</strong> ${data.cause}
          </p>
          <div class="ctl-reaction-box">
            <strong>Reaction:</strong> ${data.formula}
          </div>
          <div class="ctl-triage-std">
            <strong>Standard:</strong> ${data.epa}
          </div>
        </div>
        <div class="ctl-triage-right">
          <div class="ctl-spec-box">
            <h4 class="ctl-spec-heading">Proven Engineering Solution:</h4>
            <p class="ctl-spec-solution">${data.fix}</p>
          </div>
          <button class="button-primary button-sm" onclick="openArticleModal(${data.articleId})">
            Read Complete Engineering Diagnostic Guide &rarr;
          </button>
        </div>
      </div>
    `;
  }

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const symptomKey = btn.getAttribute('data-symptom');
      renderSymptom(symptomKey);
    });
  });

  renderSymptom('limescale');
}

/* ==========================================================================
   2. Interactive Water Softener & RO Sizing Calculator
   ========================================================================== */
function initCalculator() {
  const peopleInput = document.getElementById('calc-people');
  const hardnessInput = document.getElementById('calc-hardness');
  const ironInput = document.getElementById('calc-iron');

  if (!peopleInput || !hardnessInput || !ironInput) return;

  function calculate() {
    const people = Math.max(1, parseInt(peopleInput.value) || 4);
    const hardnessGpg = Math.max(1, parseFloat(hardnessInput.value) || 10);
    const ironPpm = Math.max(0, parseFloat(ironInput.value) || 0);

    // Step 1: Daily Household Water Demand
    const dailyGallons = people * 75;

    // Step 2: Compensated Hardness
    const compensatedHardness = hardnessGpg + (ironPpm * 5);

    // Step 3: Daily Grains to remove
    const dailyGrains = dailyGallons * compensatedHardness;

    // Step 4: Weekly Grain Requirement (7 days) + 25% Reserve
    const rawWeeklyCapacity = dailyGrains * 7 * 1.25;

    // Standard tank sizing round-up
    let recommendedSize = 32000;
    let cuFt = 1.0;
    if (rawWeeklyCapacity <= 24000) { recommendedSize = 24000; cuFt = 0.75; }
    else if (rawWeeklyCapacity <= 32000) { recommendedSize = 32000; cuFt = 1.0; }
    else if (rawWeeklyCapacity <= 40000) { recommendedSize = 40000; cuFt = 1.25; }
    else if (rawWeeklyCapacity <= 48000) { recommendedSize = 48000; cuFt = 1.5; }
    else if (rawWeeklyCapacity <= 64000) { recommendedSize = 64000; cuFt = 2.0; }
    else if (rawWeeklyCapacity <= 80000) { recommendedSize = 80000; cuFt = 2.5; }
    else { recommendedSize = 96000; cuFt = 3.0; }

    // Update DOM elements
    const elDailyGal = document.getElementById('res-daily-gal');
    const elCompHard = document.getElementById('res-comp-hard');
    const elDailyGrains = document.getElementById('res-daily-grains');
    const elGrainReq = document.getElementById('res-grain-req');
    const elGrains = document.getElementById('res-grains');
    const elCuft = document.getElementById('res-cuft');
    const elTargetCap = document.getElementById('res-target-cap');
    const elResinVol = document.getElementById('res-resin-vol');
    const elSalt = document.getElementById('res-salt');
    const elCost = document.getElementById('res-cost');
    const elSaltCost = document.getElementById('res-salt-cost');

    if (elDailyGal) elDailyGal.textContent = `${dailyGallons.toLocaleString()} GPD`;
    if (elCompHard) elCompHard.textContent = `${compensatedHardness.toFixed(1)} GPG`;
    if (elDailyGrains) elDailyGrains.textContent = `${Math.round(dailyGrains).toLocaleString()} Grains`;
    if (elGrainReq) elGrainReq.textContent = `${Math.round(dailyGrains).toLocaleString()} Grains`;
    if (elGrains) elGrains.textContent = `${recommendedSize.toLocaleString()} Grains`;
    if (elCuft) elCuft.textContent = `${cuFt.toFixed(2)} Cu. Ft. Resin`;
    if (elTargetCap) elTargetCap.textContent = `${recommendedSize.toLocaleString()} Grains`;
    if (elResinVol) elResinVol.textContent = `${cuFt} Cu Ft Resin Bed`;

    // Salt Usage & Cost Calculation
    const annualSaltBags = Math.round((dailyGrains * 365) / (2000 * 40)) + 6;
    const annualSaltCost = annualSaltBags * 8;
    const fiveYearSaltCost = annualSaltCost * 5;

    if (elSalt) elSalt.textContent = `${annualSaltBags * 40} lbs (~ ${annualSaltBags} bags)`;
    if (elCost) elCost.textContent = `$${annualSaltCost} - $${annualSaltCost + 20} / year`;
    if (elSaltCost) elSaltCost.textContent = `~$${fiveYearSaltCost} ($${(fiveYearSaltCost / (5 * 365)).toFixed(2)}/day)`;
  }

  [peopleInput, hardnessInput, ironInput].forEach(input => {
    input.addEventListener('input', calculate);
  });

  calculate();
}

/* ==========================================================================
   3. Dynamic Article Grid & Category Filter Tabs
   ========================================================================== */
function initArticleGrid() {
  const gridContainer = document.getElementById('articles-grid');
  const tabs = document.querySelectorAll('.ctl-tab-btn');
  if (!gridContainer || typeof CLEAR_TAP_ARTICLES === 'undefined') return;

  window.renderCategoryArticles = function(filterCategory = 'all') {
    const filtered = filterCategory === 'all' 
      ? CLEAR_TAP_ARTICLES 
      : CLEAR_TAP_ARTICLES.filter(a => a.category === filterCategory);

    gridContainer.innerHTML = filtered.map(a => `
      <div class="ctl-article-card">
        <div>
          <div class="ctl-article-meta-top">
            <span class="badge-pill ${a.badgeClass}">
              <span class="bullet-dot"></span>
              <span>${a.categoryLabel}</span>
            </span>
            <span class="ctl-read-time">${a.readTime}</span>
          </div>
          <h3 class="ctl-article-title">${a.title}</h3>
          <p class="ctl-article-snippet">${a.excerpt}</p>
        </div>
        <button class="button-outline button-sm" onclick="openArticleModal(${a.id})">
          Read Complete Guide &rarr;
        </button>
      </div>
    `).join('');
  };

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      const cat = tab.getAttribute('data-category');
      renderCategoryArticles(cat);
    });
  });

  renderCategoryArticles('all');
}

function initCategoryTriggers() {
  const triggers = document.querySelectorAll('[data-category]');
  triggers.forEach(trig => {
    if (trig.classList.contains('ctl-tab-btn')) return;
    trig.addEventListener('click', () => {
      const cat = trig.getAttribute('data-category');
      const tab = document.querySelector(`.ctl-tab-btn[data-category="${cat}"]`);
      if (tab) {
        document.querySelectorAll('.ctl-tab-btn').forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        if (window.renderCategoryArticles) {
          window.renderCategoryArticles(cat);
        }
      }
    });
  });
}

/* ==========================================================================
   4. Modal Article Reader
   ========================================================================== */
function initModalReader() {
  window.openArticleModal = function(articleId) {
    if (typeof CLEAR_TAP_ARTICLES === 'undefined') return;
    const article = CLEAR_TAP_ARTICLES.find(a => a.id === articleId);
    if (!article) return;

    const modal = document.getElementById('article-modal');
    const modalBody = document.getElementById('modal-article-body');
    const modalContainer = modal ? modal.querySelector('.ctl-modal-container') : null;

    if (modalBody) {
      modalBody.innerHTML = article.contentHtml;
    }
    if (modalContainer) {
      modalContainer.scrollTop = 0;
    }
    if (modal) {
      modal.classList.add('open');
      modal.setAttribute('aria-hidden', 'false');
      modal.scrollIntoView({ behavior: 'smooth' });
    }
  };

  window.closeArticleModal = function() {
    const modal = document.getElementById('article-modal');
    if (modal) {
      modal.classList.remove('open');
      modal.setAttribute('aria-hidden', 'true');
    }
  };

  const closeBtn = document.getElementById('modal-close-btn');
  if (closeBtn) {
    closeBtn.addEventListener('click', closeArticleModal);
  }

  const modalBackdrop = document.getElementById('article-modal');
  if (modalBackdrop) {
    modalBackdrop.addEventListener('click', (e) => {
      if (e.target === modalBackdrop) {
        closeArticleModal();
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeArticleModal();
      closeSearch();
      closeMobileDrawer();
    }
  });
}

/* ==========================================================================
   5. Live Instant Search Overlay
   ========================================================================== */
function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

function initLiveSearch() {
  const searchOverlay = document.getElementById('search-overlay');
  const searchInput = document.getElementById('search-query-input');
  const searchResults = document.getElementById('search-results-list');
  const searchBtn = document.getElementById('search-btn');
  const searchCloseBtn = document.getElementById('search-close-btn');

  window.openSearch = function() {
    if (searchOverlay && searchInput) {
      searchOverlay.classList.add('open');
      searchOverlay.setAttribute('aria-hidden', 'false');
      searchInput.focus();
      searchOverlay.scrollIntoView({ behavior: 'smooth' });
      performSearch('');
    }
  };

  window.closeSearch = function() {
    if (searchOverlay) {
      searchOverlay.classList.remove('open');
      searchOverlay.setAttribute('aria-hidden', 'true');
    }
  };

  if (searchBtn) {
    searchBtn.addEventListener('click', openSearch);
  }

  if (searchCloseBtn) {
    searchCloseBtn.addEventListener('click', closeSearch);
  }

  function performSearch(query) {
    if (!searchResults || typeof CLEAR_TAP_ARTICLES === 'undefined') return;
    const cleanQ = query.trim().toLowerCase();

    const matches = CLEAR_TAP_ARTICLES.filter(a => {
      const tagMatch = Array.isArray(a.tags) 
        ? a.tags.some(t => typeof t === 'string' && t.toLowerCase().includes(cleanQ)) 
        : false;
      return a.title.toLowerCase().includes(cleanQ) || 
             a.excerpt.toLowerCase().includes(cleanQ) || 
             a.slug.toLowerCase().includes(cleanQ) || 
             a.categoryLabel.toLowerCase().includes(cleanQ) || 
             tagMatch;
    });

    if (matches.length === 0) {
      searchResults.innerHTML = `
        <div class="ctl-search-empty">
          No technical guides found matching "<strong>${escapeHtml(query)}</strong>".
        </div>
      `;
    } else {
      searchResults.innerHTML = matches.map(a => `
        <div class="ctl-search-item" onclick="closeSearch(); openArticleModal(${a.id});">
          <div class="ctl-search-item-meta">
            <span class="badge-pill ${a.badgeClass}">
              <span class="bullet-dot"></span>
              <span>${a.categoryLabel}</span>
            </span>
            <span class="ctl-read-time">${a.readTime}</span>
          </div>
          <h4>${a.title}</h4>
          <p>${a.excerpt}</p>
        </div>
      `).join('');
    }
  }

  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      performSearch(e.target.value);
    });
  }

  if (searchOverlay) {
    searchOverlay.addEventListener('click', (e) => {
      if (e.target === searchOverlay) {
        closeSearch();
      }
    });
  }
}

/* ==========================================================================
   6. Mobile Menu Drawer
   ========================================================================== */
function initMobileDrawer() {
  const drawer = document.getElementById('mobile-drawer');
  const menuBtn = document.getElementById('menu-btn');
  const closeBtn = document.getElementById('drawer-close-btn');
  const drawerLinks = document.querySelectorAll('.drawer-link');

  window.openMobileDrawer = function() {
    if (drawer) {
      drawer.classList.add('open');
      drawer.setAttribute('aria-hidden', 'false');
      drawer.scrollIntoView({ behavior: 'smooth' });
    }
  };

  window.closeMobileDrawer = function() {
    if (drawer) {
      drawer.classList.remove('open');
      drawer.setAttribute('aria-hidden', 'true');
    }
  };

  if (menuBtn) {
    menuBtn.addEventListener('click', openMobileDrawer);
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', closeMobileDrawer);
  }

  drawerLinks.forEach(lnk => {
    lnk.addEventListener('click', closeMobileDrawer);
  });
}
