# TENeT: Telehealth Effectiveness and Necessity Tracker for Alaska

Mentors: Pradeeban Kathiravelu (pkathiravelu -at- alaska.edu) and David Moxley (dpmoxley -at- alaska.edu)

**Overview:**

TENeT (Telehealth Effectiveness and Necessity Tracker) combines public health site data and Internet performance measurements to identify Alaskan regions that lack local healthcare access but have sufficient, stable Internet connectivity to make telehealth feasible. The project produces a web application and interactive dashboard that visualizes where telehealth is both necessary and workable across Alaska's cities and villages.

**Key Goals:**
- Define a compound metric to identify "healthcare deserts" that considers: number of health sites, specialist availability, average distance to the nearest clinic, and presence/quality of transportation networks.
- Combine that healthcare-access metric with Internet availability and performance data (latency, throughput, stability) from public measurement networks and ISP sources.
- Visualize the mashup as an interactive overlay on an Alaska-focused map (OpenStreetMap or similar), showing areas where telehealth is necessary and feasible.

**Compound Metric (suggested components):**
- Health Site Density: number of health facilities per population in a region.
- Specialist Access: presence/absence or count of specialist services within reachable distance.
- Travel Distance / Time: median distance or travel time to the nearest primary care clinic.
- Transportation Network Score: availability of road/sea/air transport that affects access.
- Internet Connectivity Score: combines measurement-based throughput/latency/stability and ISP coverage.

These sub-scores should be normalized and combined into a single index (weights configurable) to highlight healthcare deserts where telehealth would be impactful.

**Data Sources:**
- Health site data: public sources such as https://healthsites.io/map and local/state datasets (recommended to verify and augment public data).
- Internet performance: measurement networks (e.g., broadbandmapping.com), ISP coverage data, and active measurements (where possible).
- Geographic basemaps: OpenStreetMap tiles or vector data focusing on the Alaska extent.

**Visualization & UX:**
- Map-first dashboard that loads Alaska by default and overlays the compound metric as choropleth or heatmap layers.
- Interactive filters for metric weights, facility types, and Internet thresholds.
- Drill-down on communities to show raw inputs (site list, ISP details, measurement samples) and suggested telehealth readiness.

**Expected Outcomes:**
- A web application highlighting telehealth necessity and feasibility in Alaska.
- Reusable pipeline for ingesting health site and Internet measurement data.
- Documentation and a configurable metric so the solution can be adapted to other regions.

**Current Status:**
- Research stage — data sources and metric design are being evaluated.

**Required Skills:**
- Python (data processing, GeoPandas, APIs) or another high-level language
- Frontend experience (React / Vue / Svelte or similar) for dashboard/map UI
- Familiarity with geo data (shapefiles, GeoJSON), map libraries (Leaflet, Mapbox GL), and web mapping

**Code Challenge / Prior Experience:**
- Prior experience working with geospatial frameworks and building map-based dashboards is recommended.

**Project Links:**
- Source code: https://github.com/KathiraveluLab/TENeT
- Discussion forum: https://github.com/KathiraveluLab/TENeT/discussions

**Effort & Difficulty:**
- Estimated effort: ~350 hours
- Difficulty: Intermediate

**Getting Started (developer):**
1. Clone the repository:
	```bash
	git clone https://github.com/KathiraveluLab/TENeT.git
	cd TENeT
	```
2. Review data sources and add credentials/endpoints in `data/` or environment variables.
3. For backend development (suggested): create a Python venv and install requirements inside `backend/` when available:
	```bash
	cd backend
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	```
4. For frontend development: open `frontend/` and add your preferred framework/tooling (Vite/CRA). A minimal placeholder `frontend/README.md` is included.

**Contributing:**
- Open issues or discussions in the repository to propose metric designs, data sources, or visualization ideas.
- Follow the contributor workflow: fork → feature branch → tests → pull request.

**Ethics & Privacy:**
- Avoid committing any sensitive data (personal health information or private credentials). Aggregate or anonymize fine-grained datasets when publishing.

**License:**
- Add license information in `LICENSE` or update this README with the chosen license.

---

If you want, I can also:
- scaffold a minimal backend API and frontend map viewer,
- generate a data-ingestion notebook for health site and measurement data, or
- draft a metric design spreadsheet with suggested weights and example calculations.

Tell me which next step you'd like. 
