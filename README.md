# TENeT: Telehealth Effectiveness and Necessity Tracker

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

TENeT is a data-driven application that identifies Alaska regions that are "healthcare deserts" but have stable Internet connectivity, making them ideal candidates for telehealth services.

## 🎯 Project Goal

Help healthcare providers and policymakers identify where telehealth can have the greatest impact by:
- Mapping healthcare access across Alaska
- Measuring Internet connectivity and performance
- Calculating telehealth feasibility scores
- Visualizing opportunities on an interactive map

## 🏥 What is a Healthcare Desert?

A healthcare desert is a region with limited healthcare access, determined by:
- **Few health facilities** relative to population
- **Long distances** to nearest clinic (50+ miles)
- **Limited specialist availability**
- **Poor transportation** infrastructure

## 🌐 Why Alaska?

Alaska presents unique healthcare challenges:
- **229 federally recognized tribes** in remote locations
- Many villages accessible only by plane or boat
- Vast distances between communities
- Growing telehealth infrastructure

TENeT helps identify which remote communities can benefit from telehealth right now.

## 📊 Features

### Current (v0.1.0)
- ✅ Healthcare desert identification algorithm
- ✅ Telehealth feasibility scoring
- ✅ Configurable metrics and thresholds
- ✅ Comprehensive test suite

### Planned
- 🔄 Healthcare facility data collection (healthsites.io)
- 🔄 Internet performance data collection (FCC, broadband maps)
- 🔄 Interactive Alaska map visualization
- 🔄 Analytics dashboard
- 🔄 Historical trend analysis
- 🔄 Recommendation engine

## 🏗️ Architecture
```
TENeT/
├── backend/
│   ├── data_collection/    # Data scraping and collection
│   ├── analysis/            # Healthcare desert & telehealth algorithms
│   ├── database/            # Data models and storage
│   ├── api/                 # REST API endpoints
│   └── config/              # Configuration settings
├── frontend/
│   ├── static/              # CSS, JS, images
│   └── templates/           # HTML templates
├── tests/                   # Comprehensive test suite
├── docs/                    # Documentation
└── scripts/                 # Utility scripts
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/KathiraveluLab/TENeT.git
cd TENeT
```

2. **Create virtual environment**
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run tests**
```bash
pytest tests/ -v
```

## 📖 Usage

### Healthcare Desert Analysis
```python
from backend.analysis.healthcare_desert import HealthcareDesertAnalyzer

analyzer = HealthcareDesertAnalyzer()

# Example region data
region = {
    'facility_count': 1,
    'population': 5000,
    'avg_distance': 45,  # miles to nearest clinic
    'specialists': 0,
    'has_transportation': False
}

# Calculate desert score (0-1, higher = more severe)
score = analyzer.calculate_desert_score(region)
classification = analyzer.classify_region(score)

print(f"Desert Score: {score:.2f}")
print(f"Classification: {classification}")
```

### Telehealth Feasibility Analysis
```python
from backend.analysis.telehealth_feasibility import TelehealthFeasibilityAnalyzer

analyzer = TelehealthFeasibilityAnalyzer()

# Example internet data
region = {
    'download_speed': 5.0,    # Mbps
    'upload_speed': 1.0,      # Mbps
    'internet_coverage': 75,  # percentage
    'reliability': 0.8        # 0-1 score
}

# Calculate feasibility score
score = analyzer.calculate_feasibility_score(region)
is_viable = analyzer.is_telehealth_viable(score)
classification = analyzer.classify_feasibility(score)

print(f"Feasibility Score: {score:.2f}")
print(f"Viable: {is_viable}")
print(f"Classification: {classification}")
```

## 🔬 Methodology

### Healthcare Desert Score

The compound metric considers:
- **Facility Density** (30%): Facilities per 1,000 people
- **Distance to Clinic** (30%): Average distance to nearest healthcare facility
- **Specialist Availability** (20%): Specialists per 10,000 people
- **Transportation Access** (20%): Public transportation availability

### Telehealth Feasibility Score

Factors considered:
- **Internet Speed** (50%): Download/upload speeds (min: 1.5/0.5 Mbps)
- **Coverage** (30%): Percentage of population with internet access
- **Reliability** (20%): Connection stability and uptime

## 🧪 Testing
```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_healthcare_desert.py -v

# Run with coverage
pytest tests/ --cov=backend --cov-report=html
```

## 📚 Data Sources

- **Healthcare Facilities**: healthsites.io API, Alaska DHSS
- **Internet Performance**: FCC Broadband Map, Ookla Speedtest
- **Geographic Data**: Alaska Department of Commerce
- **Population Data**: US Census Bureau

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](docs/CONTRIBUTING.md) for details.

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Write/update tests
5. Ensure tests pass (`pytest tests/ -v`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- University of Alaska Anchorage
- KathiraveluLab research team
- Alaska healthcare providers
- Open-source community

## 📧 Contact

- Project Lead: [Professor Pradeeban Kathiravelu](https://github.com/pradeeban)
- Repository: https://github.com/KathiraveluLab/TENeT
- Issues: https://github.com/KathiraveluLab/TENeT/issues

## 🗺️ Roadmap

- [x] Core analysis algorithms
- [x] Test suite
- [ ] Data collection pipeline
- [ ] Database integration
- [ ] REST API
- [ ] Interactive map interface
- [ ] Analytics dashboard
- [ ] Deployment on Alaska infrastructure

---

**Built with ❤️ for Alaska healthcare access**
```

3. Save (Ctrl+S)

---

## ✅ Step 9: Create .gitignore

### **FILE 16: Update `.gitignore`**

1. `.gitignore` should already exist
2. Open it and make sure it has these lines:
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
*.egg-info/

# Database
*.db
*.sqlite

# IDE
.vscode/
.idea/
*.swp
*.swo

# Environment
.env
.env.local

# Testing
.pytest_cache/
htmlcov/
.coverage

# OS
.DS_Store
Thumbs.db