import json
import os

# Load scraped data
with open('scraped_data.json', 'r', encoding='utf-8') as f:
    scraped_data = json.load(f)

HEADER_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | QCLAB Solution Bangladesh</title>
    <meta name="description" content="{desc}">
    <meta name="keywords" content="QCLAB, Testing Bangladesh, Calibration Services, Inspection Bangladesh, Testing Lab Bangladesh">
    
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="styles.css">
    
    <!-- Schema.org -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "TestingLaboratory",
      "name": "QCLAB Solution",
      "url": "https://qclab.com.bd",
      "logo": "https://qclab.com.bd/storage/logo/urfP0vVnKliQy2O0CFdRnZCPUgUe0bgaxtlOYYeQ.png",
      "description": "Premier Testing, Inspection, and Calibration laboratory in Bangladesh."
    }}
    </script>
</head>
<body>

    <!-- Top Info Bar -->
    <div class="top-bar">
        <div class="container">
            <div class="top-bar-info">
                <span>📍 Dhaka, Bangladesh</span>
                <span>📞 Hotline: +880 1700-000000</span>
                <span>✉️ Email: info@qclab.com.bd</span>
            </div>
            <div>
                <span class="badge-accredited">ISO/IEC 17025 ACCREDITED LAB</span>
            </div>
        </div>
    </div>

    <!-- Main Navigation Header -->
    <header class="main-header">
        <div class="header-container">
            <a href="index.html" class="logo-wrapper">
                <img src="assets/logo.png" alt="QC Lab Solution Bangladesh" title="QC Lab Solution">
            </a>

            <div class="search-container">
                <input type="text" id="search_input" class="search-input" placeholder="Search ASTM, keyword (e.g. Concrete)..." autocomplete="off">
                <button class="search-btn">🔍</button>
                <div id="search_results_dropdown" class="search-results-dropdown"></div>
            </div>

            <nav>
                <ul class="nav-menu">
                    <li class="nav-item"><a href="about.html" class="nav-link {active_about}">About Us</a></li>
                    <li class="nav-item mega-dropdown">
                        <a href="catalog.html" class="nav-link {active_catalog}">Categories ▾</a>
                        <div class="mega-menu-content">
                            <div class="mega-broad-grid">
                                <!-- Pillar 1: Civil & Construction Materials -->
                                <div class="mega-cat-block">
                                    <div>
                                        <a href="building-materials.html" class="mega-pillar-title">🏗️ Civil Materials & Concrete</a>
                                        <div class="mega-subgroup-title">🏢 Concrete & Cement Standards</div>
                                        <ul class="mega-child-list">
                                            <li><a href="building-materials.html">• Cement Physical & Chemical Testing</a></li>
                                            <li><a href="building-materials.html">• Concrete Cylindrical Compression (ASTM C39)</a></li>
                                            <li><a href="building-materials.html">• Hardened Concrete & Shotcrete Strength</a></li>
                                        </ul>
                                        <div class="mega-subgroup-title">⛏️ Aggregates & Rock Testing</div>
                                        <ul class="mega-child-list">
                                            <li><a href="aggregates.html">• Geometrical Assessment of Fines</a></li>
                                            <li><a href="aggregates.html">• Particle Shape, Sieve Shakers & Flakiness</a></li>
                                            <li><a href="aggregates.html">• Aggregate Crushing Value (ACV) & AIV</a></li>
                                        </ul>
                                    </div>
                                    <a href="building-materials.html" class="mega-view-all-link">Browse 12 Concrete & Aggregates Standards →</a>
                                </div>

                                <!-- Pillar 2: Bitumen, Asphalt & Soil -->
                                <div class="mega-cat-block">
                                    <div>
                                        <a href="bitumen-asphalt.html" class="mega-pillar-title">🛣️ Bitumen, Asphalt & Soil</a>
                                        <div class="mega-subgroup-title">🛣️ Bitumen & Asphalt Mix QC</div>
                                        <ul class="mega-child-list">
                                            <li><a href="bitumen-asphalt.html">• Automatic Binder Extraction & Solvent Recovery</a></li>
                                            <li><a href="bitumen-asphalt.html">• Gyratory Compaction & Wheel Tracking</a></li>
                                            <li><a href="bitumen-asphalt.html">• Marshall Stability & Dynamic AMPT Testers</a></li>
                                        </ul>
                                        <div class="mega-subgroup-title">🧪 Soil Mechanics & Geotechnical</div>
                                        <ul class="mega-child-list">
                                            <li><a href="soil-testing.html">• Soil-Field Core Boring & SPT Drilling</a></li>
                                            <li><a href="soil-testing.html">• Soil-Lab Compaction & Atterberg Limits</a></li>
                                            <li><a href="soil-testing.html">• Triaxial Shear & Soil Permeability</a></li>
                                        </ul>
                                    </div>
                                    <a href="bitumen-asphalt.html" class="mega-view-all-link">Browse 14 Pavement & Soil Standards →</a>
                                </div>

                                <!-- Pillar 3: NDT & Structural Inspection -->
                                <div class="mega-cat-block">
                                    <div>
                                        <a href="ndt-testing.html" class="mega-pillar-title">🔍 NDT & Structural Inspection</a>
                                        <div class="mega-subgroup-title">🔬 Civil & Mechanical NDT</div>
                                        <ul class="mega-child-list">
                                            <li><a href="ndt-testing.html">• Ultrasonic Pulse Velocity (UPV) Flaw Test</a></li>
                                            <li><a href="ndt-testing.html">• Rebar Locator & Cover Depth Scanner</a></li>
                                            <li><a href="ndt-testing.html">• Concrete Rebound Hammer Soundness</a></li>
                                        </ul>
                                        <div class="mega-subgroup-title">📊 Structural Health Monitoring</div>
                                        <ul class="mega-child-list">
                                            <li><a href="ndt-testing.html">• Dynamic Strain & Crack Propagation</a></li>
                                            <li><a href="ndt-testing.html">• Mechanical Flaw & Weld Radiography</a></li>
                                        </ul>
                                    </div>
                                    <a href="ndt-testing.html" class="mega-view-all-link">Explore NDT & Field Inspection →</a>
                                </div>

                                <!-- Pillar 4: Petrochemical, Environmental & Calibration -->
                                <div class="mega-cat-block">
                                    <div>
                                        <a href="petrochemical.html" class="mega-pillar-title">⛽ Petrochemical & Environment</a>
                                        <div class="mega-subgroup-title">⛽ Petrochemical & Fuel Lab</div>
                                        <ul class="mega-child-list">
                                            <li><a href="petrochemical.html">• Petroleum Products Distillation & Quality</a></li>
                                            <li><a href="petrochemical.html">• Transformer Oil Breakdown Voltage DGA</a></li>
                                        </ul>
                                        <div class="mega-subgroup-title">🍃 Environmental & Water QC</div>
                                        <ul class="mega-child-list">
                                            <li><a href="environmental.html">• Water Quality & Effluent Wastewater</a></li>
                                            <li><a href="environmental.html">• Air Quality Monitoring & Microbiology</a></li>
                                        </ul>
                                        <div class="mega-subgroup-title">🛠️ Calibration & Support</div>
                                        <ul class="mega-child-list">
                                            <li><a href="support.html">• ISO 17025 Equipment Calibration</a></li>
                                            <li><a href="support.html">• Lab Repairs, Parts & Rentals</a></li>
                                        </ul>
                                    </div>
                                    <a href="petrochemical.html" class="mega-view-all-link">Browse Petrochemical & Water Labs →</a>
                                </div>
                            </div>

                            <div class="mega-bottom-bar">
                                <div class="mega-bottom-text">
                                    <span>🏆 <strong>ISO/IEC 17025 Accredited Laboratory</strong> — Serving 11 Divisions, 85 Sub-Groups & 150+ Accredited Standard Methods</span>
                                </div>
                                <a href="catalog.html" class="btn-primary" style="padding: 6px 18px; font-size: 0.82rem;">Explore Master Catalog Dashboard →</a>
                            </div>
                        </div>
                    </li>
                    <li class="nav-item"><a href="industries.html" class="nav-link {active_industries}">Industries</a></li>
                    <li class="nav-item"><a href="services.html" class="nav-link {active_services}">Services</a></li>
                    <li class="nav-item"><a href="projects.html" class="nav-link {active_projects}">Projects</a></li>
                    <li class="nav-item"><a href="blog.html" class="nav-link {active_blog}">Blog</a></li>
                    <li class="nav-item"><a href="contact.html" class="nav-link {active_contact}">Contact</a></li>
                </ul>
            </nav>

            <div class="header-actions">
                <button class="btn-primary" onclick="openQuoteModal()">Get Quote →</button>
            </div>
        </div>
    </header>
"""

FOOTER_HTML = """
    <!-- Detail Specifications Modal -->
    <div id="detail_modal" class="modal-backdrop">
        <div class="modal-box">
            <button class="modal-close" onclick="closeDetailModal()">✕</button>
            <h3 id="detail_modal_title" class="modal-title">Standard Details</h3>
            <div id="detail_modal_body"></div>
        </div>
    </div>

    <!-- Quote Request Modal -->
    <div id="quote_modal" class="modal-backdrop">
        <div class="modal-box">
            <button class="modal-close" onclick="closeQuoteModal()">✕</button>
            <h3 class="modal-title">Request Quotation & Testing Service</h3>
            <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 20px;">Fill in your required testing category and project details to get an official estimate.</p>
            
            <form onsubmit="submitQuoteForm(event)">
                <div style="margin-bottom: 15px;">
                    <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Full Name *</label>
                    <input type="text" required placeholder="e.g. Engr. Tanvir Ahmed" style="width: 100%; padding: 10px 15px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: inherit;">
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                    <div>
                        <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Email Address *</label>
                        <input type="email" required placeholder="name@company.com" style="width: 100%; padding: 10px 15px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: inherit;">
                    </div>
                    <div>
                        <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Phone Number *</label>
                        <input type="tel" required placeholder="+880 17..." style="width: 100%; padding: 10px 15px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: inherit;">
                    </div>
                </div>
                <div style="margin-bottom: 15px;">
                    <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Testing Category Required</label>
                    <select style="width: 100%; padding: 10px 15px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: inherit;">
                        <option>Aggregates & Rock Testing</option>
                        <option>Bitumen & Asphalt Mix Analysis</option>
                        <option>Concrete & Cement Strength Testing</option>
                        <option>NDT Testing & Inspection</option>
                        <option>Soil Mechanics & Field Testing</option>
                        <option>General Laboratory Equipment & Calibration</option>
                        <option>Environmental & Water Quality Testing</option>
                    </select>
                </div>
                <div style="margin-bottom: 20px;">
                    <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Project / Sample Details</label>
                    <textarea rows="3" placeholder="Specify number of samples, required ASTM/BSTI standards, or project location..." style="width: 100%; padding: 10px 15px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: inherit;"></textarea>
                </div>
                <button type="submit" class="btn-primary" style="width: 100%; justify-content: center;">Submit Inquiry to QC Lab →</button>
            </form>
        </div>
    </div>

    <!-- Main Footer -->
    <footer class="main-footer">
        <div class="footer-container">
            <div>
                <img src="assets/logo.png" alt="QC Lab Logo" style="height: 40px; filter: brightness(0) invert(1); margin-bottom: 15px;">
                <p style="font-size: 0.9rem; line-height: 1.6; margin-bottom: 15px;">
                    QCLab Solution is Bangladesh's premier testing, inspection, and calibration lab dedicated to quality assurance and structural safety.
                </p>
                <div style="margin-bottom: 15px;">
                    <a href="https://drive.google.com/file/d/1W2AaoIhubkUgirOqMnIl7OIbGwe5ti9h/view?usp=sharing" target="_blank" class="footer-pdf-btn">📄 Download Portfolio PDF</a>
                </div>
                <div style="font-size: 0.88rem;">
                    📍 Dhaka, Bangladesh<br>
                    📞 Phone: +880 1700-000000<br>
                    ✉️ Email: info@qclab.com.bd
                </div>
            </div>

            <div>
                <h4>Testing Categories</h4>
                <ul class="footer-links">
                    <li><a href="aggregates.html">Aggregates Testing</a></li>
                    <li><a href="bitumen-asphalt.html">Bitumen & Asphalt</a></li>
                    <li><a href="building-materials.html">Building Materials</a></li>
                    <li><a href="ndt-testing.html">NDT Inspection</a></li>
                    <li><a href="soil-testing.html">Soil Mechanics</a></li>
                </ul>
            </div>

            <div>
                <h4>Company & Support</h4>
                <ul class="footer-links">
                    <li><a href="about.html">About Us</a></li>
                    <li><a href="industries.html">Industries We Serve</a></li>
                    <li><a href="services.html">Services</a></li>
                    <li><a href="projects.html">Projects</a></li>
                    <li><a href="blog.html">Technical Blog</a></li>
                    <li><a href="support.html">Repairs, Parts & Rentals</a></li>
                    <li><a href="support.html">Calibration & Training</a></li>
                    <li><a href="contact.html">Contact Us</a></li>
                </ul>
            </div>

            <div>
                <h4>Accreditation</h4>
                <p style="font-size: 0.85rem; line-height: 1.5; margin-bottom: 15px;">
                    ISO/IEC 17025 Compliant. Equipment calibrated to national and international traceable standards.
                </p>
                <div style="background: rgba(255,255,255,0.05); padding: 12px; border-radius: 8px; font-size: 0.8rem; border: 1px solid rgba(255,255,255,0.1);">
                    🏆 Trusted by leading engineering firms, government authorities, and contractors across Bangladesh.
                </div>
            </div>
        </div>

        <div class="footer-bottom">
            <p>Copyright © 2026 QCLab Solution. All Rights Reserved.</p>
        </div>
    </footer>

    <script src="assets/data.js"></script>
    <script src="app.js"></script>
</body>
</html>
"""

def make_page(filename, title, desc, content_html, active_nav='home'):
    active_flags = {
        'active_about': 'active' if active_nav == 'about' else '',
        'active_catalog': 'active' if active_nav == 'catalog' else '',
        'active_industries': 'active' if active_nav == 'industries' else '',
        'active_services': 'active' if active_nav == 'services' else '',
        'active_projects': 'active' if active_nav == 'projects' else '',
        'active_blog': 'active' if active_nav == 'blog' else '',
        'active_contact': 'active' if active_nav == 'contact' else '',
    }
    
    header = HEADER_HTML.format(title=title, desc=desc, **active_flags)
    full_html = header + content_html + FOOTER_HTML
    with open(filename, 'w', encoding='utf-8') as out:
        out.write(full_html)
    print(f"Generated {filename}")

# Homepage (index.html)
home_content = """
    <!-- 1. HERO SECTION -->
    <section class="hero-section">
        <div class="hero-bg-overlay"></div>
        <div class="hero-container">
            <div>
                <div class="hero-badge">⚡ ISO 17025 Accredited & BSTI Compliant Laboratory</div>
                <h1 class="hero-title">Testing, Inspection & Calibration Services in Bangladesh</h1>
                <p class="hero-subtitle">Ensuring structural integrity, quality compliance, and precision material testing for Bangladesh's leading construction and industrial projects.</p>
                <div style="display: flex; gap: 15px; flex-wrap: wrap;">
                    <a href="catalog.html" class="btn-primary">Browse All Categories →</a>
                    <button class="btn-outline" style="color: #fff; border-color: #fff;" onclick="openQuoteModal()">Request Quote</button>
                </div>

                <div class="hero-stats-row">
                    <div class="stat-box">
                        <div class="stat-number">500+</div>
                        <div class="stat-label">Standard Tests</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">100%</div>
                        <div class="stat-label">Accredited Precision</div>
                    </div>
                    <div class="stat-box">
                        <div class="stat-number">15+</div>
                        <div class="stat-label">Sectors Served</div>
                    </div>
                </div>
            </div>

            <div style="position: relative; text-align: center;">
                <img src="assets/hero_banner.jpg" alt="Modern QCLab Laboratory" style="width: 100%; border-radius: var(--radius-lg); box-shadow: 0 20px 50px rgba(0,0,0,0.4); border: 2px solid rgba(255,255,255,0.2);">
            </div>
        </div>
    </section>

    <!-- 2. ABOUT SECTION -->
    <section id="about_section" style="max-width: 1300px; margin: 70px auto; padding: 0 20px;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center; background: #ffffff; padding: 50px; border-radius: var(--radius-lg); box-shadow: var(--card-shadow); border: 1px solid var(--card-border);">
            <div>
                <span class="section-tag">About QCLAB Solution</span>
                <h2 style="font-size: 2.2rem; margin-top: 8px; margin-bottom: 20px; color: var(--text-dark);">Bangladesh's Trusted Quality Control & Testing Partner</h2>
                <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 15px;">
                    QCLAB Solution is a premier ISO/IEC 17025 compliant laboratory dedicated to material testing, civil engineering quality assurance, non-destructive inspection, and industrial instrument calibration.
                </p>
                <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 25px;">
                    Operating under international standards (ASTM, AASHTO, BS EN, and BSTI), we serve major government mega projects, commercial developers, and industrial manufacturing facilities across Bangladesh.
                </p>
                <div style="display: flex; gap: 15px;">
                    <a href="about.html" class="btn-primary">Learn More About Us →</a>
                </div>
            </div>
            <div>
                <img src="assets/civil_testing.jpg" alt="QCLab Testing Facility" style="width: 100%; border-radius: var(--radius-md); box-shadow: var(--card-shadow);">
            </div>
        </div>
    </section>

    <!-- 3. CATEGORIES SECTION -->
    <section class="category-overview-section">
        <div class="section-header">
            <span class="section-tag">Core Testing Categories</span>
            <h2 class="section-title">Specialized Testing & Product Menus</h2>
            <p style="color: var(--text-muted); margin-top: 8px;">Explore dedicated testing standard pages for each major engineering division.</p>
        </div>

        <div class="cat-overview-grid">
            <div class="cat-overview-card">
                <div>
                    <div class="cat-card-icon">🏗️</div>
                    <h3 class="cat-card-title">Aggregates & Rock</h3>
                    <p class="cat-card-desc">Geometrical properties, particle shape, density, ACV device, AIV test, and triaxial rock testing.</p>
                </div>
                <a href="aggregates.html" class="cat-card-link">Explore Aggregates →</a>
            </div>

            <div class="cat-overview-card">
                <div>
                    <div class="cat-card-icon">🛣️</div>
                    <h3 class="cat-card-title">Bitumen & Asphalt</h3>
                    <p class="cat-card-desc">Automatic binder extraction, gyratory compactors, wheel tracking, AMPT testers, Marshall stability.</p>
                </div>
                <a href="bitumen-asphalt.html" class="cat-card-link">Explore Bitumen & Asphalt →</a>
            </div>

            <div class="cat-overview-card">
                <div>
                    <div class="cat-card-icon">🏢</div>
                    <h3 class="cat-card-title">Building Materials</h3>
                    <p class="cat-card-desc">Cement physical & chemical testing, concrete compression, hardened concrete, shotcrete evaluation.</p>
                </div>
                <a href="building-materials.html" class="cat-card-link">Explore Building Materials →</a>
            </div>

            <div class="cat-overview-card">
                <div>
                    <div class="cat-card-icon">🔍</div>
                    <h3 class="cat-card-title">NDT Testing</h3>
                    <p class="cat-card-desc">Non-destructive evaluation, ultrasonic pulse velocity, rebound hammer, rebar scanning, flaw detection.</p>
                </div>
                <a href="ndt-testing.html" class="cat-card-link">Explore NDT Testing →</a>
            </div>

            <div class="cat-overview-card">
                <div>
                    <div class="cat-card-icon">🧪</div>
                    <h3 class="cat-card-title">Soil Mechanics</h3>
                    <p class="cat-card-desc">Soil-Field SPT, core drilling, Soil-Lab compaction, Atterberg limits, triaxial shear testing.</p>
                </div>
                <a href="soil-testing.html" class="cat-card-link">Explore Soil Mechanics →</a>
            </div>

            <div class="cat-overview-card">
                <div>
                    <div class="cat-card-icon">⛽</div>
                    <h3 class="cat-card-title">Petrochemical Testing</h3>
                    <p class="cat-card-desc">Petroleum product testing, transformer oil breakdown voltage, fuel quality, polymer analysis.</p>
                </div>
                <a href="petrochemical.html" class="cat-card-link">Explore Petrochemical →</a>
            </div>
        </div>

        <div style="text-align: center; margin-top: 40px;">
            <a href="catalog.html" class="btn-primary" style="padding: 14px 30px; font-size: 1rem;">View All Product & Test Categories →</a>
        </div>
    </section>

    <!-- 4. SERVICES SECTION -->
    <section class="features-section">
        <div class="section-header">
            <span class="section-tag">Engineering Solutions</span>
            <h2 class="section-title">Our Technical Services</h2>
        </div>

        <div class="features-grid">
            <div class="feature-card">
                <img src="assets/civil_testing.jpg" alt="Civil Engineering Testing" class="feature-img">
                <div class="feature-content">
                    <h3 class="feature-title">Civil Engineering Testing</h3>
                    <p class="feature-desc">Comprehensive quality control for mega infrastructure, roads, bridges, and commercial structures.</p>
                </div>
            </div>

            <div class="feature-card">
                <img src="assets/ndt_calibration.jpg" alt="NDT Inspection" class="feature-img">
                <div class="feature-content">
                    <h3 class="feature-title">Condition Monitoring & NDT</h3>
                    <p class="feature-desc">Advanced non-destructive inspection, flaw analysis, structural health monitoring, and precision calibration.</p>
                </div>
            </div>

            <div class="feature-card">
                <img src="assets/soil_asphalt_lab.jpg" alt="Equipment Calibration" class="feature-img">
                <div class="feature-content">
                    <h3 class="feature-title">Equipment Repair & Calibration</h3>
                    <p class="feature-desc">Certified calibration, verification, training, and maintenance for lab and field instruments.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- 5. PROJECTS SECTION -->
    <section style="max-width: 1300px; margin: 70px auto; padding: 0 20px;">
        <div class="section-header">
            <span class="section-tag">Proven Track Record</span>
            <h2 class="section-title">Key Projects Portfolio</h2>
            <p style="color: var(--text-muted); margin-top: 8px;">Explore major infrastructure and industrial testing engagements across Bangladesh.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px;">
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/mega_bridge_project.jpg" alt="Expressway Pavement QA" class="feature-img">
                <div style="padding: 25px;">
                    <span class="badge-accredited" style="background: #10b981;">ONGOING</span>
                    <h3 style="margin-top: 12px; font-size: 1.25rem;">Expressway & Pavement Quality Assurance</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 10px;">Bitumen mix composition analysis, gyratory compaction, and on-site core extraction for major highway expansion.</p>
                </div>
            </div>
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/ndt_calibration.jpg" alt="High-Rise NDT Evaluation" class="feature-img">
                <div style="padding: 25px;">
                    <span class="badge-accredited" style="background: #3b82f6;">COMPLETED</span>
                    <h3 style="margin-top: 12px; font-size: 1.25rem;">Commercial High-Rise NDT Evaluation</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 10px;">Ultrasonic flaw detection, rebar locator scanning, and concrete rebound hammer testing for structural verification.</p>
                </div>
            </div>
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/soil_asphalt_lab.jpg" alt="Power Plant Geotechnical Soil Survey" class="feature-img">
                <div style="padding: 25px;">
                    <span class="badge-accredited" style="background: #f59e0b;">UPCOMING</span>
                    <h3 style="margin-top: 12px; font-size: 1.25rem;">Power Plant Geotechnical Soil Survey</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 10px;">Deep soil boring SPT, triaxial shear testing, and foundation load capacity analysis.</p>
                </div>
            </div>
        </div>
        <div style="text-align: center; margin-top: 30px;">
            <a href="projects.html" class="btn-outline">View Complete Projects List →</a>
        </div>
    </section>

    <!-- 6. RECENT ARTICLES SECTION -->
    <section style="background: #f1f5f9; padding: 70px 20px;">
        <div style="max-width: 1300px; margin: 0 auto;">
            <div class="section-header">
                <span class="section-tag">Knowledge & Insights</span>
                <h2 class="section-title">Recent Technical Blog Articles</h2>
                <p style="color: var(--text-muted); margin-top: 8px;">Technical articles on ASTM standards, concrete durability, and NDT methodologies.</p>
            </div>

            <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px; margin-top: 40px;">
                <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                    <img src="assets/civil_testing.jpg" alt="Concrete Cylindrical Compression" class="feature-img">
                    <div style="padding: 25px;">
                        <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">ASTM C39 Standards</div>
                        <h3 style="font-size: 1.15rem; margin: 10px 0; font-weight: 700;">Understanding Concrete Cylindrical Compression Testing</h3>
                        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.6;">A deep dive into sample curing, capping methods, and load rate precision to ensure accurate compressive strength values.</p>
                        <a href="blog.html" style="display: inline-block; margin-top: 15px; font-weight: 700; color: var(--primary-color); font-size: 0.88rem;">Read Article →</a>
                    </div>
                </div>

                <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                    <img src="assets/ndt_calibration.jpg" alt="Ultrasonic Pulse Velocity" class="feature-img">
                    <div style="padding: 25px;">
                        <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">Non-Destructive Testing</div>
                        <h3 style="font-size: 1.15rem; margin: 10px 0; font-weight: 700;">Ultrasonic Pulse Velocity for Existing Concrete Structures</h3>
                        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.6;">How UPV testing identifies internal honeycombing, void cracks, and delamination without structural damage.</p>
                        <a href="blog.html" style="display: inline-block; margin-top: 15px; font-weight: 700; color: var(--primary-color); font-size: 0.88rem;">Read Article →</a>
                    </div>
                </div>

                <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                    <img src="assets/soil_asphalt_lab.jpg" alt="Gyratory Compaction vs Marshall" class="feature-img">
                    <div style="padding: 25px;">
                        <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">Asphalt Mix Design</div>
                        <h3 style="font-size: 1.15rem; margin: 10px 0; font-weight: 700;">Gyratory Compaction vs Marshall Stability in Bitumen QC</h3>
                        <p style="color: var(--text-muted); font-size: 0.88rem; line-height: 1.6;">Comparing volumetric property evaluation methods for heavy traffic pavement designs under AASHTO T312.</p>
                        <a href="blog.html" style="display: inline-block; margin-top: 15px; font-weight: 700; color: var(--primary-color); font-size: 0.88rem;">Read Article →</a>
                    </div>
                </div>
            </div>
            <div style="text-align: center; margin-top: 35px;">
                <a href="blog.html" class="btn-primary">Visit Full Blog & Insights Center →</a>
            </div>
        </div>
    </section>

    <!-- 7. CONTACT FORM SECTION -->
    <section id="contact_section" style="max-width: 1300px; margin: 70px auto; padding: 0 20px;">
        <div class="section-header">
            <span class="section-tag">Get In Touch</span>
            <h2 class="section-title">Request Quotation & Contact Us</h2>
            <p style="color: var(--text-muted); margin-top: 8px;">Fill in the form below or visit our main laboratory in Dhaka.</p>
        </div>

        <div style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 40px; margin-top: 30px;">
            <div style="background: #ffffff; padding: 40px; border-radius: var(--radius-lg); box-shadow: var(--card-shadow); border: 1px solid var(--card-border);">
                <h3 style="font-size: 1.4rem; margin-bottom: 20px; color: var(--primary-color);">Send Us an Inquiry</h3>
                <form onsubmit="submitQuoteForm(event)">
                    <div style="margin-bottom: 15px;">
                        <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Full Name *</label>
                        <input type="text" required placeholder="Engr. Tanvir Ahmed" style="width: 100%; padding: 12px 16px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: inherit;">
                    </div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 15px;">
                        <div>
                            <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Email Address *</label>
                            <input type="email" required placeholder="name@company.com" style="width: 100%; padding: 12px 16px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: inherit;">
                        </div>
                        <div>
                            <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Phone Number *</label>
                            <input type="tel" required placeholder="+880 17..." style="width: 100%; padding: 12px 16px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: inherit;">
                        </div>
                    </div>
                    <div style="margin-bottom: 15px;">
                        <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Testing Category Required</label>
                        <select style="width: 100%; padding: 12px 16px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: inherit;">
                            <option>Aggregates & Rock Testing</option>
                            <option>Bitumen & Asphalt Mix Analysis</option>
                            <option>Concrete & Cement Strength Testing</option>
                            <option>NDT Testing & Inspection</option>
                            <option>Soil Mechanics & Field Testing</option>
                            <option>General Laboratory Equipment & Calibration</option>
                            <option>Environmental & Water Quality Testing</option>
                        </select>
                    </div>
                    <div style="margin-bottom: 20px;">
                        <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Project / Sample Details</label>
                        <textarea rows="4" placeholder="Specify number of samples, required ASTM/BSTI standards, or project location..." style="width: 100%; padding: 12px 16px; border-radius: 8px; border: 1px solid #cbd5e1; font-family: inherit;"></textarea>
                    </div>
                    <button type="submit" class="btn-primary" style="width: 100%; justify-content: center; padding: 14px;">Submit Inquiry to QC Lab →</button>
                </form>
            </div>

            <div>
                <div style="background: #ffffff; padding: 35px; border-radius: var(--radius-lg); box-shadow: var(--card-shadow); border: 1px solid var(--card-border); margin-bottom: 25px;">
                    <h3 style="font-size: 1.3rem; margin-bottom: 15px; color: var(--primary-color);">Headquarters & Lab Office</h3>
                    <p style="font-size: 0.95rem; line-height: 1.9; color: var(--text-dark);">
                        📍 <strong>Location:</strong> Dhaka, Bangladesh<br>
                        📞 <strong>Hotline:</strong> +880 1700-000000<br>
                        ✉️ <strong>Email:</strong> info@qclab.com.bd<br>
                        ⏰ <strong>Laboratory Hours:</strong> Sat – Thu: 9:00 AM – 6:00 PM
                    </p>
                </div>

                <div style="background: linear-gradient(135deg, #0f2027, #203a43); color: #fff; padding: 30px; border-radius: var(--radius-lg);">
                    <h4 style="color: var(--accent-color); font-size: 1.1rem; margin-bottom: 10px;">Emergency On-Site Sampling</h4>
                    <p style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">Our field technical teams are equipped for 24/7 mobile sampling, SPT soil boring, and concrete slump/core extraction across Bangladesh.</p>
                </div>
            </div>
        </div>
    </section>
"""

# New dedicated blog.html page
blog_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Technical Blog & Insights</h1>
            <p class="page-banner-subtitle">Stay updated on ASTM standard testing methods, concrete durability, bitumen quality control, and NDT inspection.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <span>Blog</span></div>
        </div>
    </div>

    <section style="max-width: 1200px; margin: 60px auto; padding: 0 20px;">
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px;">
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/civil_testing.jpg" alt="Concrete Compression Testing" class="feature-img">
                <div style="padding: 25px;">
                    <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">ASTM C39 Standards</div>
                    <h3 style="font-size: 1.2rem; margin: 12px 0; font-weight: 700;">Understanding Concrete Cylindrical Compression Testing</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">A deep dive into sample curing, sulfur capping vs unbonded caps, and load rate precision under ASTM C39 to ensure accurate compressive strength values.</p>
                    <button class="btn-primary" style="margin-top: 20px; width: 100%; justify-content: center;" onclick="openDetailModal('Concrete Compression Testing Article', 'Blog', [])">Read Technical Article →</button>
                </div>
            </div>

            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/ndt_calibration.jpg" alt="Ultrasonic Pulse Velocity" class="feature-img">
                <div style="padding: 25px;">
                    <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">Non-Destructive Testing</div>
                    <h3 style="font-size: 1.2rem; margin: 12px 0; font-weight: 700;">Ultrasonic Pulse Velocity for Existing Concrete Structures</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">How UPV testing non-destructively identifies internal honeycombing, void cracks, and delamination in existing high-rise structures.</p>
                    <button class="btn-primary" style="margin-top: 20px; width: 100%; justify-content: center;" onclick="openDetailModal('Ultrasonic Pulse Velocity Article', 'Blog', [])">Read Technical Article →</button>
                </div>
            </div>

            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/soil_asphalt_lab.jpg" alt="Gyratory Compaction vs Marshall" class="feature-img">
                <div style="padding: 25px;">
                    <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">Asphalt Mix Design</div>
                    <h3 style="font-size: 1.2rem; margin: 12px 0; font-weight: 700;">Gyratory Compaction vs Marshall Stability in Bitumen QC</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">Comparing volumetric property evaluation methods for heavy traffic pavement designs under AASHTO T312 and ASTM D6926.</p>
                    <button class="btn-primary" style="margin-top: 20px; width: 100%; justify-content: center;" onclick="openDetailModal('Gyratory Compaction Article', 'Blog', [])">Read Technical Article →</button>
                </div>
            </div>
        </div>
    </section>
"""

# Redesigned Catalog Page Content
catalog_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Master Testing & Equipment Catalog</h1>
            <p class="page-banner-subtitle">Search and filter across all 11 testing divisions, ASTM standard methods, and calibration services.</p>
            <div class="breadcrumb">
                <a href="index.html">Home</a> <span>/</span> <span>Catalog</span>
            </div>
        </div>
    </div>

    <div class="catalog-dashboard">
        <div class="catalog-top-controls">
            <div class="catalog-search-row">
                <input type="text" id="catalog_dashboard_search" class="catalog-search-input" placeholder="Search by test method, ASTM standard code, or keyword (e.g. Concrete, Bitumen, Triaxial, Soil)...">
                <button class="btn-primary" onclick="resetCatalogFilters()">Reset Filters</button>
            </div>
            
            <div id="catalog_pills_container" class="catalog-pills-row">
                <!-- Filter Pills with counts via JS -->
            </div>
        </div>

        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 25px;">
            <div id="catalog-count" style="font-weight: 700; color: var(--text-dark); font-size: 1.1rem;">Loading standards...</div>
            <div style="font-size: 0.88rem; color: var(--text-muted);">Showing ISO/IEC 17025 Accredited Test Standards</div>
        </div>

        <div id="catalog-grid" class="catalog-grid"></div>
    </div>
"""

# Subpage Contents
agg_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Aggregates & Rock Testing</h1>
            <p class="page-banner-subtitle">Geometrical properties, mechanical testing, ACV, AIV, particle shape, and rock mechanics.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <a href="catalog.html">Categories</a> <span>/</span> <span>Aggregates</span></div>
        </div>
    </div>

    <div class="subpage-container">
        <div class="sidebar-box">
            <h3 class="sidebar-title">Aggregates Sub-Groups</h3>
            <ul class="sidebar-menu">
                <li><a href="#" class="active" onclick="filterSubCat('Aggregates', 'all')">All Aggregates Tests</a></li>
                <li><a href="#" onclick="filterSubCat('Aggregates', 'Geometrical Properties')">Geometrical Properties</a></li>
                <li><a href="#" onclick="filterSubCat('Aggregates', 'Mechanical and Physical Properties')">Mechanical & Physical</a></li>
                <li><a href="#" onclick="filterSubCat('Aggregates', 'Sample Grading')">Sample Grading</a></li>
                <li><a href="#" onclick="filterSubCat('Aggregates', 'Rock Testing')">Rock Testing</a></li>
            </ul>
        </div>
        <div>
            <div id="subpage-grid" class="subpage-grid"></div>
        </div>
    </div>
"""

bitumen_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Bitumen & Asphalt Testing</h1>
            <p class="page-banner-subtitle">Binder extraction, Gyratory compactors, Wheel Tracking, AMPT, Marshall stability, and pavement quality testing.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <a href="catalog.html">Categories</a> <span>/</span> <span>Bitumen & Asphalt</span></div>
        </div>
    </div>

    <div class="subpage-container">
        <div class="sidebar-box">
            <h3 class="sidebar-title">Asphalt Sub-Groups</h3>
            <ul class="sidebar-menu">
                <li><a href="#" class="active" onclick="filterSubCat('Bitumen & Asphalt', 'all')">All Asphalt Tests</a></li>
                <li><a href="#" onclick="filterSubCat('Bitumen & Asphalt', 'Asphalt Mix Composition Analysis')">Composition Analysis</a></li>
                <li><a href="#" onclick="filterSubCat('Bitumen & Asphalt', 'Asphalt Mix Sample Preparation')">Sample Preparation</a></li>
                <li><a href="#" onclick="filterSubCat('Bitumen & Asphalt', 'Dynamic Asphalt Mix Testing Systems')">Dynamic Testing Systems</a></li>
                <li><a href="#" onclick="filterSubCat('Bitumen & Asphalt', 'Gyratory Compaction & Wheel Tracking')">Gyratory & Wheel Tracking</a></li>
                <li><a href="#" onclick="filterSubCat('Bitumen & Asphalt', 'Marshall Stability, BMD and Indirect Tensile')">Marshall & BMD</a></li>
            </ul>
        </div>
        <div>
            <div id="subpage-grid" class="subpage-grid"></div>
        </div>
    </div>
"""

building_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Building Materials & Concrete</h1>
            <p class="page-banner-subtitle">Cement physical & chemical properties, concrete compression, hardened concrete, and shotcrete strength testing.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <a href="catalog.html">Categories</a> <span>/</span> <span>Building Materials</span></div>
        </div>
    </div>

    <div class="subpage-container">
        <div class="sidebar-box">
            <h3 class="sidebar-title">Sub-Categories</h3>
            <ul class="sidebar-menu">
                <li><a href="#" class="active" onclick="filterSubCat('Building Materials', 'all')">All Building Materials</a></li>
                <li><a href="#" onclick="filterSubCat('Building Materials', 'Cement Testing')">Cement Testing</a></li>
                <li><a href="#" onclick="filterSubCat('Building Materials', 'Concrete Testing')">Concrete Testing</a></li>
                <li><a href="#" onclick="filterSubCat('Building Materials', 'Determination of Strength')">Determination of Strength</a></li>
                <li><a href="#" onclick="filterSubCat('Building Materials', 'Hardened Concrete Testing')">Hardened Concrete</a></li>
            </ul>
        </div>
        <div>
            <div id="subpage-grid" class="subpage-grid"></div>
        </div>
    </div>
"""

ndt_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Non-Destructive Testing (NDT)</h1>
            <p class="page-banner-subtitle">Mechanical and Civil NDT, Ultrasonic pulse velocity, rebar locator, rebound hammer, and structural inspection.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <a href="catalog.html">Categories</a> <span>/</span> <span>NDT Testing</span></div>
        </div>
    </div>

    <div class="subpage-container">
        <div class="sidebar-box">
            <h3 class="sidebar-title">NDT Categories</h3>
            <ul class="sidebar-menu">
                <li><a href="#" class="active" onclick="filterSubCat('NDT Testing', 'all')">All NDT Testing</a></li>
                <li><a href="#" onclick="filterSubCat('NDT Testing', 'Mechanical NDT Testing')">Mechanical NDT</a></li>
                <li><a href="#" onclick="filterSubCat('NDT Testing', 'Civil NDT Testing')">Civil NDT</a></li>
            </ul>
        </div>
        <div>
            <div id="subpage-grid" class="subpage-grid"></div>
        </div>
    </div>
"""

soil_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Soil Mechanics & Geotechnical Testing</h1>
            <p class="page-banner-subtitle">Field SPT, core sampling, soil laboratory compaction, Atterberg limits, triaxial shear, and permeability testing.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <a href="catalog.html">Categories</a> <span>/</span> <span>Soil</span></div>
        </div>
    </div>

    <div class="subpage-container">
        <div class="sidebar-box">
            <h3 class="sidebar-title">Soil Divisions</h3>
            <ul class="sidebar-menu">
                <li><a href="#" class="active" onclick="filterSubCat('Soil', 'all')">All Soil Tests</a></li>
                <li><a href="#" onclick="filterSubCat('Soil', 'Soil-Field')">Soil-Field Testing</a></li>
                <li><a href="#" onclick="filterSubCat('Soil', 'Soil-Lab')">Soil-Lab Testing</a></li>
                <li><a href="#" onclick="filterSubCat('Soil', 'Soil Mechanics')">Soil Mechanics</a></li>
            </ul>
        </div>
        <div>
            <div id="subpage-grid" class="subpage-grid"></div>
        </div>
    </div>
"""

petro_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Petrochemical & Fuel Testing</h1>
            <p class="page-banner-subtitle">Petroleum products, transformer oil breakdown voltage, coal & coke, biofuel, and polymer testing laboratory.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <a href="catalog.html">Categories</a> <span>/</span> <span>Petrochemical</span></div>
        </div>
    </div>

    <div class="subpage-container">
        <div class="sidebar-box">
            <h3 class="sidebar-title">Petrochemical Laboratories</h3>
            <ul class="sidebar-menu">
                <li><a href="#" class="active" onclick="filterSubCat('Petrochemical Testing', 'all')">All Petrochemical Tests</a></li>
                <li><a href="#" onclick="filterSubCat('Petrochemical Testing', 'Petroleum Products Testing Laboratory')">Petroleum Products</a></li>
                <li><a href="#" onclick="filterSubCat('Petrochemical Testing', 'Transformer Oil Testing Laboratory')">Transformer Oil</a></li>
            </ul>
        </div>
        <div>
            <div id="subpage-grid" class="subpage-grid"></div>
        </div>
    </div>
"""

env_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Environmental & Water Quality Testing</h1>
            <p class="page-banner-subtitle">Water quality analysis, wastewater monitoring, air quality monitoring, and microbiology testing.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <a href="catalog.html">Categories</a> <span>/</span> <span>Environmental</span></div>
        </div>
    </div>

    <div class="subpage-container">
        <div class="sidebar-box">
            <h3 class="sidebar-title">Environmental Units</h3>
            <ul class="sidebar-menu">
                <li><a href="#" class="active" onclick="filterSubCat('Environmental', 'all')">All Environmental Tests</a></li>
                <li><a href="#" onclick="filterSubCat('Environmental', 'Water Quality Testing Laboratory')">Water Quality</a></li>
                <li><a href="#" onclick="filterSubCat('Environmental', 'Microbiology Laboratory')">Microbiology Lab</a></li>
            </ul>
        </div>
        <div>
            <div id="subpage-grid" class="subpage-grid"></div>
        </div>
    </div>
"""

about_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">About QCLAB Solution</h1>
            <p class="page-banner-subtitle">ISO/IEC 17025 Accredited Laboratory committed to structural safety, material precision, and standard compliance in Bangladesh.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <span>About Us</span></div>
        </div>
    </div>

    <section style="max-width: 1100px; margin: 60px auto; padding: 0 20px;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; align-items: center;">
            <div>
                <span class="section-tag">Who We Are</span>
                <h2 style="font-size: 2.2rem; margin-top: 10px; margin-bottom: 20px;">Leading Quality Assurance & Calibration Laboratory</h2>
                <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 15px;">
                    QCLAB Solution is a premier provider of Testing, Inspection, and Calibration services based in Bangladesh. We specialize in civil engineering materials, bitumen mixes, soil mechanics, NDT inspection, and industrial equipment calibration.
                </p>
                <p style="color: var(--text-muted); line-height: 1.8; margin-bottom: 25px;">
                    Our facilities are equipped with state-of-the-art testing machinery traceable to international standards (ASTM, AASHTO, BS EN, BSTI), providing reliable test reports accepted by government authorities, consultants, and contractors nationwide.
                </p>
                <button class="btn-primary" onclick="openQuoteModal()">Consult Our Engineers →</button>
            </div>
            <div>
                <img src="assets/hero_banner.jpg" alt="QCLab Team and Facility" style="width: 100%; border-radius: var(--radius-md); box-shadow: var(--card-shadow);">
            </div>
        </div>
    </section>
"""

services_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Services & Technical Capabilities</h1>
            <p class="page-banner-subtitle">Civil Engineering Testing, Condition Monitoring, Equipment Calibration, Rentals, and Consultancy.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <span>Services</span></div>
        </div>
    </div>

    <section style="max-width: 1300px; margin: 60px auto; padding: 0 20px;">
        <div class="features-grid">
            <div class="feature-card">
                <img src="assets/civil_testing.jpg" class="feature-img" alt="Civil Engineering">
                <div class="feature-content">
                    <h3 class="feature-title">Civil Engineering Testing</h3>
                    <p class="feature-desc">Comprehensive strength evaluation for concrete, steel rebars, cement, aggregates, and asphalt mixes.</p>
                </div>
            </div>
            <div class="feature-card">
                <img src="assets/ndt_calibration.jpg" class="feature-img" alt="NDT Testing">
                <div class="feature-content">
                    <h3 class="feature-title">Condition Monitoring & NDT</h3>
                    <p class="feature-desc">Ultrasonic testing, rebar scanning, rebound hammer, and structural flaw diagnosis on existing buildings & bridges.</p>
                </div>
            </div>
            <div class="feature-card">
                <img src="assets/soil_asphalt_lab.jpg" class="feature-img" alt="Calibration">
                <div class="feature-content">
                    <h3 class="feature-title">Instrument Calibration & Repair</h3>
                    <p class="feature-desc">ISO 17025 traceable calibration for pressure gauges, UTM load cells, balances, and field equipment.</p>
                </div>
            </div>
            <div class="feature-card">
                <img src="assets/mega_bridge_project.jpg" class="feature-img" alt="Field Boring & Geotechnical">
                <div class="feature-content">
                    <h3 class="feature-title">Geotechnical Field Boring & Survey</h3>
                    <p class="feature-desc">On-site SPT boring, core drilling, triaxial soil shear evaluation, and foundation load capacity analysis.</p>
                </div>
            </div>
            <div class="feature-card">
                <img src="assets/images/img_1.jpg" class="feature-img" alt="Petrochemical Environmental">
                <div class="feature-content">
                    <h3 class="feature-title">Petrochemical & Water Quality Analysis</h3>
                    <p class="feature-desc">Transformer oil breakdown voltage, fuel quality specs, industrial effluent wastewater, and air quality monitoring.</p>
                </div>
            </div>
            <div class="feature-card">
                <img src="assets/images/img_7.jpg" class="feature-img" alt="Equipment Rental & Training">
                <div class="feature-content">
                    <h3 class="feature-title">Equipment Rentals & Training</h3>
                    <p class="feature-desc">Field NDT instrument rentals, technician hands-on training, and ISO 17025 lab management consulting.</p>
                </div>
            </div>
        </div>
    </section>
"""

projects_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Projects Portfolio</h1>
            <p class="page-banner-subtitle">Upcoming, Ongoing, and Completed Infrastructure & Industrial Testing Projects in Bangladesh.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <span>Projects</span></div>
        </div>
    </div>

    <section style="max-width: 1200px; margin: 60px auto; padding: 0 20px;">
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 25px;">
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/mega_bridge_project.jpg" class="feature-img" alt="Expressway QC">
                <div style="padding: 25px;">
                    <span class="badge-accredited" style="background: #10b981;">ONGOING</span>
                    <h3 style="margin-top: 12px; font-size: 1.25rem;">Mega Expressway QC Testing</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 8px;">Bitumen mix design, compaction verification, and core sample extraction for highway construction.</p>
                </div>
            </div>
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/ndt_calibration.jpg" class="feature-img" alt="High-Rise NDT">
                <div style="padding: 25px;">
                    <span class="badge-accredited" style="background: #3b82f6;">COMPLETED</span>
                    <h3 style="margin-top: 12px; font-size: 1.25rem;">High-Rise Tower NDT Inspection</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 8px;">Ultrasonic pulse velocity and rebar scanning for structural health verification.</p>
                </div>
            </div>
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/soil_asphalt_lab.jpg" class="feature-img" alt="Power Plant Field Survey">
                <div style="padding: 25px;">
                    <span class="badge-accredited" style="background: #f59e0b;">UPCOMING</span>
                    <h3 style="margin-top: 12px; font-size: 1.25rem;">Power Plant Geotechnical Field Survey</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 8px;">Soil boring SPT, triaxial shear testing, and foundation load capacity analysis.</p>
                </div>
            </div>
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/images/img_12.jpg" class="feature-img" alt="Industrial Calibration">
                <div style="padding: 25px;">
                    <span class="badge-accredited" style="background: #3b82f6;">COMPLETED</span>
                    <h3 style="margin-top: 12px; font-size: 1.25rem;">Industrial Refinery Instrument Calibration</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 8px;">On-site ISO 17025 pressure gauge, UTM, and temperature sensor calibration.</p>
                </div>
            </div>
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/civil_testing.jpg" class="feature-img" alt="Bridge Monitoring">
                <div style="padding: 25px;">
                    <span class="badge-accredited" style="background: #10b981;">ONGOING</span>
                    <h3 style="margin-top: 12px; font-size: 1.25rem;">River Bridge Structural Health Monitoring</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 8px;">Dynamic strain gauge measurement, concrete crack monitoring, and vibration analysis.</p>
                </div>
            </div>
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/images/img_10.jpg" class="feature-img" alt="Port Harbor Foundation">
                <div style="padding: 25px;">
                    <span class="badge-accredited" style="background: #3b82f6;">COMPLETED</span>
                    <h3 style="margin-top: 12px; font-size: 1.25rem;">Port & Harbor Jetty Concrete QC</h3>
                    <p style="color: var(--text-muted); font-size: 0.9rem; margin-top: 8px;">Marine concrete durability testing, chloride ion penetration, and compressive strength evaluation.</p>
                </div>
            </div>
        </div>
    </section>
"""

support_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Technical Support & Rentals</h1>
            <p class="page-banner-subtitle">Equipment Repairs, Parts, Instrument Rental, Installation, Commissioning & Training.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <span>Support</span></div>
        </div>
    </div>

    <section style="max-width: 1100px; margin: 60px auto; padding: 0 20px;">
        <div class="cat-overview-grid" style="grid-template-columns: repeat(2, 1fr);">
            <div class="cat-overview-card">
                <div>
                    <div class="cat-card-icon">🛠️</div>
                    <h3 class="cat-card-title">Repairs, Parts & Rentals</h3>
                    <p class="cat-card-desc">Genuine spare parts, hydraulic repair for compression machines, and temporary field instrument rentals.</p>
                </div>
                <button class="btn-primary" onclick="openQuoteModal()">Request Support →</button>
            </div>
            <div class="cat-overview-card">
                <div>
                    <div class="cat-card-icon">🎓</div>
                    <h3 class="cat-card-title">Installation & Training</h3>
                    <p class="cat-card-desc">On-site equipment commissioning, technician training, and ISO 17025 laboratory quality system setup.</p>
                </div>
                <button class="btn-primary" onclick="openQuoteModal()">Book Training →</button>
            </div>
        </div>
    </section>
"""

contact_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Contact QCLAB Solution</h1>
            <p class="page-banner-subtitle">Get in touch with our engineering team for testing inquiries, price quotes, or lab visits.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <span>Contact</span></div>
        </div>
    </div>

    <section style="max-width: 1100px; margin: 60px auto; padding: 0 20px;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px;">
            <div style="background: #fff; padding: 35px; border-radius: var(--radius-md); box-shadow: var(--card-shadow);">
                <h3 style="font-size: 1.5rem; margin-bottom: 20px; color: var(--primary-color);">Send Us an Inquiry</h3>
                <form onsubmit="submitQuoteForm(event)">
                    <div style="margin-bottom: 15px;">
                        <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Full Name *</label>
                        <input type="text" required placeholder="Engr. Tanvir Ahmed" style="width: 100%; padding: 10px 15px; border-radius: 8px; border: 1px solid #cbd5e1;">
                    </div>
                    <div style="margin-bottom: 15px;">
                        <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Email Address *</label>
                        <input type="email" required placeholder="name@company.com" style="width: 100%; padding: 10px 15px; border-radius: 8px; border: 1px solid #cbd5e1;">
                    </div>
                    <div style="margin-bottom: 20px;">
                        <label style="display: block; font-weight: 600; font-size: 0.88rem; margin-bottom: 6px;">Message / Test Specification</label>
                        <textarea rows="4" placeholder="How can we help your project?" style="width: 100%; padding: 10px 15px; border-radius: 8px; border: 1px solid #cbd5e1;"></textarea>
                    </div>
                    <button type="submit" class="btn-primary" style="width: 100%; justify-content: center;">Send Message →</button>
                </form>
            </div>

            <div>
                <div style="background: #fff; padding: 35px; border-radius: var(--radius-md); box-shadow: var(--card-shadow); margin-bottom: 25px;">
                    <h3 style="font-size: 1.3rem; margin-bottom: 15px;">Laboratory Location & Contacts</h3>
                    <p style="font-size: 0.95rem; line-height: 1.8; color: var(--text-muted);">
                        📍 <strong>Address:</strong> Dhaka, Bangladesh<br>
                        📞 <strong>Hotline:</strong> +880 1700-000000<br>
                        ✉️ <strong>Email:</strong> info@qclab.com.bd<br>
                        ⏰ <strong>Working Hours:</strong> Saturday – Thursday: 9:00 AM – 6:00 PM
                    </p>
                </div>
            </div>
        </div>
    </section>
"""

# Industries Page Content
industries_content = """
    <div class="page-header-banner">
        <div class="page-banner-content">
            <h1 class="page-banner-title">Industries We Serve</h1>
            <p class="page-banner-subtitle">We deliver professional civil engineering, testing, inspection, and calibration solutions across diverse industries in Bangladesh.</p>
            <div class="breadcrumb"><a href="index.html">Home</a> <span>/</span> <span>Industries</span></div>
        </div>
    </div>

    <section style="max-width: 1300px; margin: 60px auto; padding: 0 20px;">
        <div style="background: #ffffff; padding: 45px; border-radius: var(--radius-lg); box-shadow: var(--card-shadow); border: 1px solid var(--card-border); margin-bottom: 50px;">
            <span class="section-tag">Cross-Sector Expertise</span>
            <h2 style="font-size: 2.2rem; margin-top: 8px; margin-bottom: 20px; color: var(--text-dark);">Comprehensive Solutions Across Infrastructure & Industrial Sectors</h2>
            <p style="color: var(--text-muted); font-size: 1.05rem; line-height: 1.8;">
                We deliver professional civil engineering and construction solutions across diverse industries. Our experience includes residential and commercial development, industrial facilities, infrastructure, transportation, government projects, and institutional buildings. We provide expertise in site development, structural works, roads, drainage, utilities, and project management. With a strong focus on quality, safety, sustainability, and cost efficiency, we help clients turn complex projects into successful, durable developments.
            </p>
        </div>

        <div class="section-header">
            <span class="section-tag">Industry Solutions Portfolio</span>
            <h2 class="section-title">Specialized Testing & Engineering Solutions</h2>
            <p style="color: var(--text-muted); margin-top: 8px;">Explore specialized technical services tailored for power, civil, industrial, and environmental sectors.</p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin-top: 40px;">
            <!-- Card 1: Power & Utility Grid Solutions -->
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/ndt_calibration.jpg" alt="Power & Substation Maintenance" class="feature-img">
                <div style="padding: 28px;">
                    <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">Power & Utilities</div>
                    <h3 style="font-size: 1.3rem; margin: 12px 0; font-weight: 700; color: var(--text-dark);">Substation & Electrical Diagnostics</h3>
                    <ul style="list-style: none; padding: 0; margin-bottom: 20px; font-size: 0.9rem; color: var(--text-muted); line-height: 1.8;">
                        <li>⚡ Integrated Testing & Calibration Solution</li>
                        <li>🔌 Switchgear Protection Testing Solution</li>
                        <li>🏗️ Substation Maintenance & Commissioning</li>
                        <li>⚡ Underground Cable Fault Testing & Diagnostics</li>
                        <li>📊 Partial Discharge (PD) Monitoring System</li>
                        <li>☀️ Solar Performance Testing Solution</li>
                    </ul>
                    <button class="btn-primary" style="width: 100%; justify-content: center;" onclick="openQuoteModal()">Request Utility Solution Quote →</button>
                </div>
            </div>

            <!-- Card 2: Infrastructure & Road Engineering -->
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/mega_bridge_project.jpg" alt="Subsurface Utility Mapping & Roads" class="feature-img">
                <div style="padding: 28px;">
                    <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">Infrastructure & Transportation</div>
                    <h3 style="font-size: 1.3rem; margin: 12px 0; font-weight: 700; color: var(--text-dark);">Subsurface & Pavement Solutions</h3>
                    <ul style="list-style: none; padding: 0; margin-bottom: 20px; font-size: 0.9rem; color: var(--text-muted); line-height: 1.8;">
                        <li>🗺️ Subsurface Utility Mapping Solution</li>
                        <li>🛣️ Road-Marking & Retroreflection Assessment</li>
                        <li>🌡️ Thermal Assessment</li>
                        <li>⚡ Lineman Safety Solutions</li>
                        <li>🔥 Combustible Gas Analysis Solution</li>
                    </ul>
                    <button class="btn-primary" style="width: 100%; justify-content: center;" onclick="openQuoteModal()">Request Infrastructure Solution Quote →</button>
                </div>
            </div>

            <!-- Card 3: Mechanical & Industrial Maintenance -->
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/civil_testing.jpg" alt="Mechanical & Preventive Maintenance" class="feature-img">
                <div style="padding: 28px;">
                    <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">Industrial & Mechanical</div>
                    <h3 style="font-size: 1.3rem; margin: 12px 0; font-weight: 700; color: var(--text-dark);">Preventive Maintenance & Inspection</h3>
                    <ul style="list-style: none; padding: 0; margin-bottom: 20px; font-size: 0.9rem; color: var(--text-muted); line-height: 1.8;">
                        <li>⚙️ Mechanical Preventive Maintenance</li>
                        <li>⚡ Electrical Preventive Maintenance</li>
                        <li>🔍 Composite Flaw Detection</li>
                        <li>🚗 Brake Disc Wear & Solid Tyre Inspection</li>
                        <li>🔨 Hardness Testing</li>
                    </ul>
                    <button class="btn-primary" style="width: 100%; justify-content: center;" onclick="openQuoteModal()">Request Maintenance Quote →</button>
                </div>
            </div>

            <!-- Card 4: Environmental & Geotechnical Observation -->
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/images/img_2.jpg" alt="Weather & Remote Sensing" class="feature-img">
                <div style="padding: 28px;">
                    <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">Environment & Remote Sensing</div>
                    <h3 style="font-size: 1.3rem; margin: 12px 0; font-weight: 700; color: var(--text-dark);">Weather & Earth Observation</h3>
                    <ul style="list-style: none; padding: 0; margin-bottom: 20px; font-size: 0.9rem; color: var(--text-muted); line-height: 1.8;">
                        <li>🌤️ Automatic Weather Station</li>
                        <li>📡 Remote Sensing & Observation System</li>
                        <li>🌲 Forestry Management</li>
                        <li>💧 Water & Environmental Quality Analysis</li>
                    </ul>
                    <button class="btn-primary" style="width: 100%; justify-content: center;" onclick="openQuoteModal()">Request Environmental Quote →</button>
                </div>
            </div>

            <!-- Card 5: AR/VR & Automated Simulators -->
            <div class="feature-card" style="background: #ffffff; overflow: hidden;">
                <img src="assets/soil_asphalt_lab.jpg" alt="AR VR Simulators" class="feature-img">
                <div style="padding: 28px;">
                    <div style="font-size: 0.8rem; color: var(--primary-color); font-weight: 700; text-transform: uppercase;">Digital & Simulators</div>
                    <h3 style="font-size: 1.3rem; margin: 12px 0; font-weight: 700; color: var(--text-dark);">AR / VR & Training Technology</h3>
                    <ul style="list-style: none; padding: 0; margin-bottom: 20px; font-size: 0.9rem; color: var(--text-muted); line-height: 1.8;">
                        <li>🥽 Augmented Reality (AR) Solutions</li>
                        <li>🕶️ Virtual Reality (VR) Inspection</li>
                        <li>🎮 Automated Training Simulators</li>
                        <li>📹 Surveillance & Security Monitoring Systems</li>
                    </ul>
                    <button class="btn-primary" style="width: 100%; justify-content: center;" onclick="openQuoteModal()">Request AR/VR Tech Demo →</button>
                </div>
            </div>
        </div>
    </section>
"""

# Generate all HTML pages
make_page("index.html", "QCLAB | Testing, Inspection & Calibration Services in Bangladesh", "Premier Testing and Calibration Laboratory", home_content, "home")
make_page("catalog.html", "Master Product & Testing Catalog", "Explore all testing categories and equipment", catalog_content, "catalog")
make_page("aggregates.html", "Aggregates & Rock Testing", "Aggregates and Rock testing equipment and standards", agg_content, "catalog")
make_page("bitumen-asphalt.html", "Bitumen & Asphalt Testing", "Bitumen and asphalt mix testing standards", bitumen_content, "catalog")
make_page("building-materials.html", "Building Materials & Concrete Testing", "Cement, concrete, strength determination", building_content, "catalog")
make_page("ndt-testing.html", "NDT Testing & Inspection", "Non-Destructive Testing Equipment & Field Services", ndt_content, "catalog")
make_page("soil-testing.html", "Soil Mechanics & Geotechnical Testing", "Soil laboratory and field testing standards", soil_content, "catalog")
make_page("petrochemical.html", "Petrochemical & Fuel Testing Laboratory", "Petrochemical, Transformer Oil, and Fuel Quality Testing", petro_content, "catalog")
make_page("environmental.html", "Environmental & Water Quality Testing", "Environmental chemistry, microbiology, and water quality testing", env_content, "catalog")
make_page("about.html", "About Us | QCLAB Solution", "Learn about QCLAB Solution ISO 17025 accredited laboratory", about_content, "about")
make_page("industries.html", "Industries We Serve | QCLAB Solution", "Civil engineering and testing solutions across diverse industries in Bangladesh", industries_content, "industries")
make_page("services.html", "Services & Capabilities | QCLAB Solution", "Civil testing, NDT, calibration and consultancy services", services_content, "services")
make_page("projects.html", "Projects Portfolio | QCLAB Solution", "Infrastructure and industrial quality control projects", projects_content, "projects")
make_page("blog.html", "Technical Blog & Insights | QCLAB Solution", "ASTM testing standards and engineering articles", blog_content, "blog")
make_page("support.html", "Technical Support & Rentals | QCLAB Solution", "Laboratory equipment repairs, parts, rentals and training", support_content, "support")
make_page("contact.html", "Contact Us | QCLAB Solution", "Contact QCLAB Solution laboratory in Dhaka Bangladesh", contact_content, "contact")
