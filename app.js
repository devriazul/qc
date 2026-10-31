// QCLab Multi-Page & Tiered Catalog Application Logic

document.addEventListener('DOMContentLoaded', () => {
  console.log('QCLab Tiered Catalog Logic Initializing...');
  
  const data = window.QCLAB_DATA || {};
  const categories = data.categories || [];
  
  const searchInput = document.getElementById('search_input');
  const searchResultsDropdown = document.getElementById('search_results_dropdown');
  const catalogDashboardSearch = document.getElementById('catalog_dashboard_search');
  
  // Setup Search Input Listeners
  if (searchInput) {
    searchInput.addEventListener('input', (e) => {
      const query = e.target.value.trim().toLowerCase();
      handleLiveSearchDropdown(categories, query);
    });
  }

  // Dashboard Search on catalog.html
  if (catalogDashboardSearch) {
    catalogDashboardSearch.addEventListener('input', (e) => {
      const query = e.target.value.trim().toLowerCase();
      renderCurrentCatalogView(categories, query);
    });
  }

  // Close search dropdown on click outside
  document.addEventListener('click', (e) => {
    if (searchResultsDropdown && !searchInput.contains(e.target) && !searchResultsDropdown.contains(e.target)) {
      searchResultsDropdown.classList.remove('active');
    }
  });

  // Page Specific Inits
  const path = window.location.pathname.toLowerCase();

  // Catalog Dashboard Page Init
  if (path.includes('catalog.html') || document.getElementById('catalog-grid')) {
    window.catalogTier = 1; // Tier 1: Main Categories, Tier 2: Sub-Categories, Tier 3: Products
    window.selectedMainCategory = null;
    window.selectedSubCategory = null;
    renderCatalogDashboardPills(categories);
    renderCurrentCatalogView(categories, '');
  }

  // Subpage specific rendering based on current HTML file
  if (path.includes('aggregates.html')) {
    renderSubPageGrid(categories, 'Aggregates', 'all');
  } else if (path.includes('bitumen-asphalt.html')) {
    renderSubPageGrid(categories, 'Bitumen & Asphalt', 'all');
  } else if (path.includes('building-materials.html')) {
    renderSubPageGrid(categories, 'Building Materials', 'all');
  } else if (path.includes('ndt-testing.html')) {
    renderSubPageGrid(categories, 'NDT Testing', 'all');
  } else if (path.includes('soil-testing.html')) {
    renderSubPageGrid(categories, 'Soil', 'all');
  } else if (path.includes('petrochemical.html')) {
    renderSubPageGrid(categories, 'Petrochemical Testing', 'all');
  } else if (path.includes('environmental.html')) {
    renderSubPageGrid(categories, 'Environmental', 'all');
  }

  setupModals();
});

// Category Icons & Images Map
const CAT_ICONS = {
  'Aggregates': '🏗️', 'Bitumen & Asphalt': '🛣️', 'Asphalt Binder': '🛢️', 'Building Materials': '🏢',
  'NDT Testing': '🔍', 'General Lab': '🔬', 'Geoscience': '🌍',
  'Petrochemical Testing': '⛽', 'Soil': '🧪', 'Soil Mechanics': '🧱', 'Material Testing': '⚙️',
  'Monitoring': '📊', 'Environmental': '🍃', 'Geotextile Testing': '🧶'
};

const CAT_IMAGES = {
  'Aggregates': 'assets/soil_asphalt_lab.jpg',
  'Bitumen & Asphalt': 'assets/soil_asphalt_lab.jpg',
  'Asphalt Binder': 'assets/soil_asphalt_lab.jpg',
  'Building Materials': 'assets/civil_testing.jpg',
  'NDT Testing': 'assets/ndt_calibration.jpg',
  'General Lab': 'assets/civil_testing.jpg',
  'Geoscience': 'assets/mega_bridge_project.jpg',
  'Petrochemical Testing': 'assets/soil_asphalt_lab.jpg',
  'Soil': 'assets/soil_asphalt_lab.jpg',
  'Soil Mechanics': 'assets/soil_asphalt_lab.jpg',
  'Material Testing': 'assets/civil_testing.jpg',
  'Monitoring': 'assets/hero_banner.jpg',
  'Environmental': 'assets/civil_testing.jpg',
  'Geotextile Testing': 'assets/mega_bridge_project.jpg'
};

function getCategoryImg(catName, index = 0) {
  if (CAT_IMAGES[catName]) return CAT_IMAGES[catName];
  const scrapedImgs = [
    'assets/images/img_0.jpg', 'assets/images/img_1.jpg', 'assets/images/img_2.jpg',
    'assets/images/img_3.jpg', 'assets/images/img_4.jpg', 'assets/images/img_5.jpg',
    'assets/images/img_6.jpg', 'assets/images/img_7.jpg', 'assets/images/img_8.jpg',
    'assets/images/img_9.jpg', 'assets/images/img_10.jpg', 'assets/images/img_11.jpg'
  ];
  return scrapedImgs[index % scrapedImgs.length];
}

// Render Catalog Dashboard Pills with Category and Sub-category counts
function renderCatalogDashboardPills(categories) {
  const container = document.getElementById('catalog_pills_container');
  if (!container) return;

  container.innerHTML = '';

  // All Categories pill
  const allBtn = document.createElement('button');
  allBtn.className = 'catalog-pill-btn active';
  allBtn.id = 'pill-all-cats';
  allBtn.innerHTML = `🌟 All Main Categories <span class="catalog-pill-count">${categories.length}</span>`;
  allBtn.onclick = () => {
    document.querySelectorAll('.catalog-pill-btn').forEach(b => b.classList.remove('active'));
    allBtn.classList.add('active');
    setCatalogTier(1, null, null);
  };
  container.appendChild(allBtn);

  categories.forEach((cat, idx) => {
    const btn = document.createElement('button');
    btn.className = 'catalog-pill-btn';
    btn.id = `pill-cat-${idx}`;
    const icon = CAT_ICONS[cat.category] || '🧪';
    const subCount = cat.groups ? cat.groups.length : 0;
    btn.innerHTML = `${icon} ${cat.category} <span class="catalog-pill-count">${subCount} Subs</span>`;
    btn.onclick = () => {
      document.querySelectorAll('.catalog-pill-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      setCatalogTier(2, cat.category, null);
    };
    container.appendChild(btn);
  });
}

// Master View Router for Catalog Page (Tier 1: Main Categories, Tier 2: Sub-Categories, Tier 3: Products)
window.setCatalogTier = function(tier, mainCatName = null, subCatName = null) {
  window.catalogTier = tier;
  window.selectedMainCategory = mainCatName;
  window.selectedSubCategory = subCatName;

  // Sync Pill Highlight
  const categories = (window.QCLAB_DATA && window.QCLAB_DATA.categories) ? window.QCLAB_DATA.categories : [];
  const pills = document.querySelectorAll('.catalog-pill-btn');
  pills.forEach(p => p.classList.remove('active'));

  if (tier === 1 || !mainCatName) {
    const allPill = document.getElementById('pill-all-cats');
    if (allPill) allPill.classList.add('active');
  } else if (mainCatName) {
    const catIndex = categories.findIndex(c => c.category === mainCatName);
    if (catIndex !== -1) {
      const targetPill = document.getElementById(`pill-cat-${catIndex}`);
      if (targetPill) targetPill.classList.add('active');
    }
  }

  const searchQuery = document.getElementById('catalog_dashboard_search') ? document.getElementById('catalog_dashboard_search').value.trim().toLowerCase() : '';
  renderCurrentCatalogView(categories, searchQuery);
};

// Render Current View based on Tier
function renderCurrentCatalogView(categories, searchQuery) {
  const catalogGrid = document.getElementById('catalog-grid');
  const catalogCount = document.getElementById('catalog-count');
  if (!catalogGrid) return;

  catalogGrid.innerHTML = '';

  // -------------------------------------------------------------
  // TIER 1: Main Category Cards View
  // -------------------------------------------------------------
  if (window.catalogTier === 1 && !searchQuery) {
    if (catalogCount) {
      catalogCount.innerHTML = `
        <div class="tier-breadcrumb">
          <span>📂 Browsing ${categories.length} Main Testing Divisions</span>
        </div>
      `;
    }

    categories.forEach((cat, idx) => {
      let totalProducts = 0;
      (cat.groups || []).forEach(g => totalProducts += (g.items ? g.items.length : 0));

      const card = document.createElement('div');
      card.className = 'main-cat-card';

      let subCatPreviewHtml = '';
      (cat.groups || []).slice(0, 4).forEach(g => {
        const childCnt = g.items ? g.items.length : 0;
        subCatPreviewHtml += `<li><strong>${g.group}</strong> <span style="font-size: 0.78rem; background: #e0f2fe; color: #0056b3; padding: 1px 8px; border-radius: 10px; margin-left: 4px;">${childCnt} items</span></li>`;
      });
      if (cat.groups && cat.groups.length > 4) {
        subCatPreviewHtml += `<li style="font-weight: 700; color: var(--primary-color);">+ ${cat.groups.length - 4} more sub-categories</li>`;
      }

      const icon = CAT_ICONS[cat.category] || '🧪';
      const catImg = cat.image ? cat.image : getCategoryImg(cat.category, idx);

      card.innerHTML = `
        <div>
          <div style="height: 140px; margin: -20px -20px 15px -20px; overflow: hidden; border-radius: 12px 12px 0 0; background: #f8fafc;">
            <img src="${catImg}" alt="${cat.category}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.src='assets/civil_testing.jpg'">
          </div>
          <div class="main-cat-header-row">
            <span class="main-cat-icon">${icon}</span>
            <span class="subcat-count-tag">🏷️ ${cat.groups ? cat.groups.length : 0} Sub-Categories</span>
          </div>
          <h3 class="main-cat-title">${cat.category}</h3>
          <div style="font-size: 0.85rem; color: #64748b; font-weight: 600;">Accredited Testing & Products: <strong style="color: #0056b3;">${totalProducts} Items</strong></div>
          <ul class="subcat-preview-list">
            ${subCatPreviewHtml}
          </ul>
        </div>
        <button class="main-cat-action-btn" onclick="setCatalogTier(2, '${escapeHtml(cat.category)}', null)">
          Browse ${cat.groups ? cat.groups.length : 0} Sub-Categories →
        </button>
      `;

      catalogGrid.appendChild(card);
    });
    return;
  }

  // -------------------------------------------------------------
  // TIER 2: Sub-Category Cards View under Selected Main Category
  // -------------------------------------------------------------
  if (window.catalogTier === 2 && !searchQuery) {
    const mainCat = categories.find(c => c.category === window.selectedMainCategory);
    if (!mainCat) { setCatalogTier(1); return; }

    const groups = mainCat.groups || [];

    if (catalogCount) {
      catalogCount.innerHTML = `
        <div class="tier-breadcrumb">
          <a href="javascript:void(0)" onclick="setCatalogTier(1)">Main Categories</a>
          <span>/</span>
          <span>${mainCat.category} (${groups.length} Sub-Categories)</span>
        </div>
      `;
    }

    groups.forEach((group, idx) => {
      const childCount = group.items ? group.items.length : 0;
      const card = document.createElement('div');
      card.className = 'sub-cat-card';

      let itemsPreview = '';
      if (group.items && group.items.length > 0) {
        group.items.slice(0, 4).forEach(it => {
          itemsPreview += `<li style="font-size: 0.88rem; color: #475569; padding: 4px 0;">✔️ ${it.title}</li>`;
        });
      } else {
        itemsPreview = `<li style="font-style: italic; color: #94a3b8; font-size: 0.85rem;">Standard testing & calibration available</li>`;
      }

      const groupImg = group.image ? group.image : (mainCat.image || getCategoryImg(mainCat.category, idx));

      card.innerHTML = `
        <div>
          <div style="height: 120px; margin: -20px -20px 12px -20px; overflow: hidden; border-radius: 12px 12px 0 0; background: #f8fafc;">
            <img src="${groupImg}" alt="${group.group}" style="width: 100%; height: 100%; object-fit: cover;" onerror="this.src='assets/civil_testing.jpg'">
          </div>
          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; flex-wrap: wrap; gap: 8px;">
            <span class="card-cat-badge">${mainCat.category}</span>
            <span style="font-size: 0.8rem; background: #e0f2fe; color: #0056b3; padding: 4px 12px; border-radius: 12px; font-weight: 700; border: 1px solid #bae6fd;">
              📦 ${childCount} Products & Tests
            </span>
          </div>
          <h3 class="card-title" style="font-size: 1.25rem;">${group.group}</h3>
          <ul style="list-style: none; margin: 12px 0 20px; border-top: 1px solid #f1f5f9; padding-top: 10px;">
            ${itemsPreview}
          </ul>
        </div>
        <button class="card-action-btn" onclick="setCatalogTier(3, '${escapeHtml(mainCat.category)}', '${escapeHtml(group.group)}')">
          View Products & Standards (${childCount}) →
        </button>
      `;

      catalogGrid.appendChild(card);
    });
    return;
  }

  // -------------------------------------------------------------
  // TIER 3: Individual Products / Standards Page View
  // -------------------------------------------------------------
  if (window.catalogTier === 3 && !searchQuery) {
    const mainCat = categories.find(c => c.category === window.selectedMainCategory);
    const subCatGroup = mainCat ? (mainCat.groups || []).find(g => g.group === window.selectedSubCategory) : null;
    
    if (!mainCat || !subCatGroup) {
      setCatalogTier(1);
      return;
    }

    const items = subCatGroup.items || [];
    
    if (catalogCount) {
      catalogCount.innerHTML = `
        <div class="tier-breadcrumb">
          <a href="javascript:void(0)" onclick="setCatalogTier(1)">Categories</a>
          <span>/</span>
          <a href="javascript:void(0)" onclick="setCatalogTier(2, '${escapeHtml(mainCat.category)}')">${mainCat.category}</a>
          <span>/</span>
          <span>${subCatGroup.group} (${items.length} Products & Standards)</span>
        </div>
      `;
    }

    if (items.length > 0) {
      items.forEach((item, idx) => {
        const card = document.createElement('div');
        card.className = 'card-item product-card';
        const productImg = item.image ? item.image : getCategoryImg(mainCat.category, idx);
        
        let specsHtml = '';
        if (item.specs && item.specs.length > 0) {
          item.specs.slice(0, 3).forEach(sp => {
            specsHtml += `<li>✔ ${sp}</li>`;
          });
        } else {
          specsHtml = `
            <li>✔ ISO/IEC 17025 Compliant Test Procedure</li>
            <li>✔ Rapid Field Sampling & Laboratory Analysis</li>
            <li>✔ Official Accredited Test Certificate Report</li>
          `;
        }

        const childGroupLabel = item.child_group ? `<div class="product-subcat-label">📁 ${item.child_group}</div>` : `<div class="product-subcat-label">📁 ${subCatGroup.group}</div>`;
        
        card.innerHTML = `
          <div>
            <div class="card-img-wrapper" style="height: 180px; overflow: hidden; display: flex; align-items: center; justify-content: center; background: #ffffff;">
              <img src="${productImg}" alt="${item.title}" style="max-height: 100%; object-fit: contain; width: 100%;" onerror="this.src='assets/logo.png'">
              <span class="product-card-badge-top">ISO 17025 ACCREDITED</span>
            </div>
            <div class="product-card-meta">
              <span class="card-cat-badge">${mainCat.category}</span>
              <span class="product-std-code">Standard #${idx + 1}</span>
            </div>
            ${childGroupLabel}
            <h3 class="card-title" style="font-size: 1.15rem; color: #0f172a; margin-bottom: 10px; line-height: 1.4;">${item.title}</h3>
            <ul class="product-features-list">
              ${specsHtml}
            </ul>
          </div>
          <button class="card-action-btn" onclick="openProductDetailModal('${escapeHtml(item.title)}', '${escapeHtml(mainCat.category)} - ${escapeHtml(subCatGroup.group)}', '${productImg}', ${JSON.stringify(item.specs || []).replace(/"/g, '&quot;')}, ${JSON.stringify(item.gallery || []).replace(/"/g, '&quot;')})">
            Request Price Quote & Specs →
          </button>
        `;
        
        catalogGrid.appendChild(card);
      });
    } else {
      const card = document.createElement('div');
      card.className = 'card-item product-card';
      const productImg = subCatGroup.image ? subCatGroup.image : getCategoryImg(mainCat.category, 0);
      card.innerHTML = `
        <div>
          <div class="card-img-wrapper">
            <img src="${productImg}" alt="${subCatGroup.group}">
            <span class="product-card-badge-top">ISO 17025 ACCREDITED</span>
          </div>
          <div class="product-card-meta">
            <span class="card-cat-badge">${mainCat.category}</span>
          </div>
          <div class="product-subcat-label">📁 ${subCatGroup.group}</div>
          <h3 class="card-title">${subCatGroup.group}</h3>
          <ul class="product-features-list">
            <li>✔ ISO/IEC 17025 Accredited Calibration & Testing</li>
            <li>✔ Traceable National & International Standards</li>
          </ul>
        </div>
        <button class="card-action-btn" onclick="openDetailModal('${escapeHtml(subCatGroup.group)}', '${escapeHtml(mainCat.category)}', [])">
          Request Inquiry & Quote →
        </button>
      `;
      catalogGrid.appendChild(card);
    }
    return;
  }

  // -------------------------------------------------------------
  // Live Search Query Mode
  // -------------------------------------------------------------
  let totalProductsFound = 0;
  if (catalogCount) {
    catalogCount.innerHTML = `<div class="tier-breadcrumb"><span>🔍 Search Results for "${escapeHtml(searchQuery)}"</span></div>`;
  }

  categories.forEach((cat, cIdx) => {
    (cat.groups || []).forEach((group, gIdx) => {
      const titleMatch = group.group.toLowerCase().includes(searchQuery);
      const itemsMatch = (group.items || []).some(item => item.title.toLowerCase().includes(searchQuery));

      if (!titleMatch && !itemsMatch) return;

      totalProductsFound++;

      const card = document.createElement('div');
      card.className = 'card-item product-card';
      const searchImg = group.image ? group.image : getCategoryImg(cat.category, gIdx);

      let itemsListHtml = '';
      if (group.items && group.items.length > 0) {
        group.items.slice(0, 5).forEach(it => {
          itemsListHtml += `<li>✔ ${it.title}</li>`;
        });
      } else {
        itemsListHtml = `<li>✔ Standard testing & equipment calibration available</li>`;
      }

      card.innerHTML = `
        <div>
          <div class="card-img-wrapper" style="height: 160px; overflow: hidden; background: #ffffff;">
            <img src="${searchImg}" alt="${group.group}" style="width: 100%; height: 100%; object-fit: contain;" onerror="this.src='assets/logo.png'">
            <span class="product-card-badge-top">ISO 17025 ACCREDITED</span>
          </div>
          <div class="product-card-meta">
            <span class="card-cat-badge">${cat.category}</span>
            <span class="product-std-code">${group.items.length} Standard Products</span>
          </div>
          <h3 class="card-title" style="font-size: 1.2rem; margin-bottom: 10px;">${group.group}</h3>
          <ul class="product-features-list">
            ${itemsListHtml}
          </ul>
        </div>
        <button class="card-action-btn" onclick="setCatalogTier(3, '${escapeHtml(cat.category)}', '${escapeHtml(group.group)}')">
          View All ${group.items.length} Products & Standards →
        </button>
      `;

      catalogGrid.appendChild(card);
    });
  });

  if (totalProductsFound === 0) {
    catalogGrid.innerHTML = `
      <div style="grid-column: 1 / -1; text-align: center; padding: 60px 20px; background: #ffffff; border-radius: var(--radius-md); box-shadow: var(--card-shadow); border: 1px solid var(--card-border);">
        <div style="font-size: 3rem; margin-bottom: 10px;">🔍</div>
        <h3 style="font-size: 1.3rem; color: var(--text-dark);">No matching products or standards found</h3>
        <p style="color: #64748b; margin-top: 8px;">Try searching for a different keyword or resetting your filters.</p>
        <button class="btn-primary" style="margin-top: 15px;" onclick="resetCatalogFilters()">Reset All Filters</button>
      </div>
    `;
  }
}

// Subpage Grid Render Logic
function renderSubPageGrid(categories, targetCatName, subGroupFilter) {
  const container = document.getElementById('subpage-grid');
  if (!container) return;

  container.innerHTML = '';
  const targetCat = categories.find(c => c.category.toLowerCase() === targetCatName.toLowerCase());
  
  if (!targetCat || !targetCat.groups) {
    container.innerHTML = '<p>No test data found for this category.</p>';
    return;
  }

  // Populate Sidebar Badges
  const sidebarLinks = document.querySelectorAll('.sidebar-menu li');
  if (sidebarLinks.length > 0 && subGroupFilter === 'all') {
    const sidebarUl = document.querySelector('.sidebar-menu');
    if (sidebarUl) {
      let sidebarHtml = `<li><a href="#" class="active" onclick="filterSubCat('${escapeHtml(targetCat.category)}', 'all')">All ${escapeHtml(targetCat.category)} Tests <span class="sidebar-count">${targetCat.groups.length}</span></a></li>`;
      targetCat.groups.forEach(g => {
        const childCount = g.items ? g.items.length : 0;
        sidebarHtml += `<li><a href="#" onclick="filterSubCat('${escapeHtml(targetCat.category)}', '${escapeHtml(g.group)}')">${g.group} <span class="sidebar-count">${childCount}</span></a></li>`;
      });
      sidebarUl.innerHTML = sidebarHtml;
    }
  }

  let count = 0;
  targetCat.groups.forEach(group => {
    if (subGroupFilter !== 'all' && group.group !== subGroupFilter) return;

    count++;
    const groupCard = document.createElement('div');
    groupCard.className = 'group-section-card';

    const childItems = group.items || [];
    let childCardsHtml = '';

    if (childItems.length > 0) {
      childItems.forEach(child => {
        const itemImg = child.image ? child.image : 'assets/logo.png';
        childCardsHtml += `
          <div class="child-item-card" style="display: flex; gap: 12px; align-items: center;">
            <div style="width: 60px; height: 60px; flex-shrink: 0; background: #fff; border-radius: 6px; overflow: hidden; border: 1px solid #e2e8f0; display: flex; align-items: center; justify-content: center;">
              <img src="${itemImg}" alt="${child.title}" style="max-height: 100%; max-width: 100%; object-fit: contain;" onerror="this.src='assets/logo.png'">
            </div>
            <div style="flex: 1;">
              <div class="child-item-title">${child.title}</div>
              <div class="child-item-action" onclick="openProductDetailModal('${escapeHtml(child.title)}', '${escapeHtml(targetCat.category)} - ${escapeHtml(group.group)}', '${itemImg}', ${JSON.stringify(child.specs || []).replace(/"/g, '&quot;')}, ${JSON.stringify(child.gallery || []).replace(/"/g, '&quot;')})">
                View Standards & Quote →
              </div>
            </div>
          </div>
        `;
      });
    } else {
      childCardsHtml = `
        <div class="child-item-card" style="grid-column: 1 / -1;">
          <div class="child-item-title">Standard Laboratory Testing & Calibration</div>
          <p style="font-size: 0.85rem; color: #64748b; margin-top: 4px;">ISO 17025 accredited apparatus calibration and field inspection available for ${group.group}.</p>
          <div class="child-item-action" onclick="openDetailModal('${escapeHtml(group.group)}', '${escapeHtml(targetCat.category)}', [])">
            Request Inquiry →
          </div>
        </div>
      `;
    }

    groupCard.innerHTML = `
      <div class="group-header">
        <div class="group-title-text">
          <span>📁</span>
          <span>${group.group}</span>
        </div>
        <span class="group-count-badge">${childItems.length} Products & Tests</span>
      </div>
      <div class="child-items-grid">
        ${childCardsHtml}
      </div>
    `;

    container.appendChild(groupCard);
  });
}

// Sidebar Subgroup Filter Click Handler
window.filterSubCat = function(mainCatName, subGroupName) {
  const links = document.querySelectorAll('.sidebar-menu a');
  links.forEach(l => l.classList.remove('active'));
  if (event && event.currentTarget) {
    event.currentTarget.classList.add('active');
  }

  renderSubPageGrid(window.QCLAB_DATA.categories, mainCatName, subGroupName);
};

// Reset Catalog Dashboard Filters
window.resetCatalogFilters = function() {
  const searchInput = document.getElementById('catalog_dashboard_search');
  if (searchInput) searchInput.value = '';
  setCatalogTier(1, null, null);
};

// Live Search Dropdown Across All Pages
function handleLiveSearchDropdown(categories, query) {
  const dropdown = document.getElementById('search_results_dropdown');
  if (!dropdown) return;

  if (query.length < 2) {
    dropdown.classList.remove('active');
    return;
  }

  dropdown.innerHTML = '';
  let count = 0;

  categories.forEach(cat => {
    (cat.groups || []).forEach(group => {
      const matchItems = (group.items || []).filter(i => i.title.toLowerCase().includes(query));
      if (group.group.toLowerCase().includes(query) || matchItems.length > 0) {
        if (count >= 6) return;
        count++;

        const item = document.createElement('div');
        item.className = 'search-result-item';
        item.innerHTML = `
          <div class="search-result-title">${group.group}</div>
          <div class="search-result-cat">${cat.category} • ${group.items ? group.items.length : 0} Products / Standards</div>
        `;
        item.onclick = () => {
          dropdown.classList.remove('active');
          window.location.href = `catalog.html`;
        };
        dropdown.appendChild(item);
      }
    });
  });

  if (count > 0) {
    dropdown.classList.add('active');
  } else {
    dropdown.classList.remove('active');
  }
}

// Modal Setup
function setupModals() {
  const quoteModal = document.getElementById('quote_modal');
  const detailModal = document.getElementById('detail_modal');

  window.openQuoteModal = function() {
    if (quoteModal) quoteModal.classList.add('active');
  };

  window.closeQuoteModal = function() {
    if (quoteModal) quoteModal.classList.remove('active');
  };

  window.closeDetailModal = function() {
    if (detailModal) detailModal.classList.remove('active');
  };
}

// Rich Product Detail Modal
window.openProductDetailModal = function(title, cat, image, specs, gallery) {
  const detailModal = document.getElementById('detail_modal');
  const titleEl = document.getElementById('detail_modal_title');
  const bodyEl = document.getElementById('detail_modal_body');

  if (!detailModal || !titleEl || !bodyEl) return;

  titleEl.innerText = title;
  
  let specsList = '';
  if (specs && specs.length > 0) {
    specs.forEach(sp => {
      specsList += `<li style="padding: 6px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.9rem; color: #334155;">✔ ${sp}</li>`;
    });
  } else {
    specsList = `<li style="padding: 8px 0; color: #64748b;">Comprehensive testing procedures and ISO 17025 compliant calibration available for this apparatus.</li>`;
  }

  let galleryHtml = '';
  if (gallery && gallery.length > 0) {
    galleryHtml = `
      <div style="display: flex; gap: 8px; margin-top: 10px; overflow-x: auto; padding-bottom: 6px;">
        ${gallery.map(img => `<img src="${img}" style="width: 60px; height: 60px; object-fit: contain; border: 1px solid #e2e8f0; border-radius: 6px; padding: 2px; background: #fff;" onerror="this.style.display='none'">`).join('')}
      </div>
    `;
  }

  bodyEl.innerHTML = `
    <div style="display: flex; gap: 20px; flex-wrap: wrap; margin-bottom: 15px;">
      <div style="width: 140px; height: 140px; background: #ffffff; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
        <img src="${image}" alt="${title}" style="max-width: 100%; max-height: 100%; object-fit: contain;" onerror="this.src='assets/logo.png'">
      </div>
      <div style="flex: 1; min-width: 200px;">
        <span class="card-cat-badge" style="display: inline-block; margin-bottom: 8px;">${cat}</span>
        <div style="font-size: 0.85rem; color: #16a34a; font-weight: 700; margin-bottom: 6px;">● Available for Official Sourcing & Calibration</div>
        <div style="font-size: 0.85rem; color: #64748b;">Certified to international ASTM, BS, EN, and ISO testing benchmarks.</div>
        ${galleryHtml}
      </div>
    </div>
    <h4 style="margin-bottom: 8px; color: var(--primary-color); font-size: 1rem;">Accredited Specifications & Test Standards:</h4>
    <ul style="list-style: none; margin-bottom: 20px; max-height: 220px; overflow-y: auto;">
      ${specsList}
    </ul>
    <button class="btn-primary" style="width: 100%; justify-content: center;" onclick="closeDetailModal(); openQuoteModal();">
      Request Official Price Quote & Datasheet →
    </button>
  `;

  detailModal.classList.add('active');
};

// Generic Detail Modal
window.openDetailModal = function(title, cat, items) {
  const detailModal = document.getElementById('detail_modal');
  const titleEl = document.getElementById('detail_modal_title');
  const bodyEl = document.getElementById('detail_modal_body');

  if (!detailModal || !titleEl || !bodyEl) return;

  titleEl.innerText = title;
  
  let listItems = '';
  if (items && items.length > 0) {
    items.forEach(it => {
      listItems += `<li style="padding: 8px 0; border-bottom: 1px solid #f1f5f9; font-size: 0.95rem;">✔️ <strong>${it.title}</strong></li>`;
    });
  } else {
    listItems = `<li style="padding: 10px 0; color: #64748b;">Comprehensive testing and ISO 17025 compliant calibration available for ${title}.</li>`;
  }

  bodyEl.innerHTML = `
    <div style="margin-bottom: 15px;">
      <span class="card-cat-badge">${cat}</span>
    </div>
    <h4 style="margin-bottom: 10px; color: var(--primary-color);">Accredited Test Specifications:</h4>
    <ul style="list-style: none; margin-bottom: 20px; max-height: 260px; overflow-y: auto;">
      ${listItems}
    </ul>
    <button class="btn-primary" style="width: 100%; justify-content: center;" onclick="closeDetailModal(); openQuoteModal();">
      Request Official Price Quote →
    </button>
  `;

  detailModal.classList.add('active');
};

window.submitQuoteForm = function(event) {
  event.preventDefault();
  alert('Thank you! Your testing & quotation request has been submitted successfully to QC Lab Solution.');
  closeQuoteModal();
};

function escapeHtml(str) {
  return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
