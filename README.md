# QC Lab Solution - Testing, Inspection & Calibration Platform

A modern, multi-page, SEO-optimized web application for **QC Lab Solution**, Bangladesh's premier ISO/IEC 17025 accredited laboratory.

## 🌟 Key Features

- **3-Tier Interactive Catalog Dashboard (`catalog.html`)**:
  - **Tier 1**: Main Category Cards with sub-category count badges (`Aggregates`, `Bitumen`, `Concrete`, `NDT`, `Soil`, `Petrochemical`, `Environmental`, etc.).
  - **Tier 2**: Sub-Category Cards with child product test counts.
  - **Tier 3**: Individual Product Cards with accredited test specifications and quote requests.
- **Redesigned Broad Full-Page Mega Menu**:
  - 4 major testing division pillars with direct sub-group links.
- **Cloned & Dedicated Industries Page (`industries.html`)**:
  - 24 specialized industry solutions across Power/Utilities, Infrastructure/Roads, Industrial/Mechanical Maintenance, Environmental/Weather, and AR/VR Simulators.
- **Dedicated Subpages & Menus**:
  - Dedicated pages for `About Us`, `Services`, `Projects`, `Blog`, `Support`, and `Contact Us`.
- **Live Auto-Completing Search**:
  - Instant ASTM standard method & keyword search across 150+ testing standards.
- **Quotation Modal**:
  - Interactive popup modal form for instant official price quote inquiries.

## 🛠️ Technology Stack

- **Frontend**: HTML5, Vanilla JavaScript, CSS3 Design System (Glassmorphic cards, CSS grid, CSS custom properties)
- **Data & Build**: Python compiler (`build_pages.py`), scraped data JSON (`scraped_data.json`)
- **Server**: Local Python HTTP Dev Server (`http://localhost:8085/`)

## 🚀 Running Locally

```bash
# Compile HTML Pages
python build_pages.py

# Start Local Server
python -m http.server 8085
```

Open `http://localhost:8085/index.html` or `http://localhost:8085/catalog.html` in your browser.
