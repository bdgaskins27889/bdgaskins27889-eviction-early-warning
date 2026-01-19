How to Run This Project

Requirements
Python 3.9 or higher
pip

Setup
git clone https://github.com/yourusername/eviction-early-warning.git
cd eviction-early-warning
pip install -r requirements.txt

Data Setup
Create a data/ directory with the following structure:
data/
├── eviction_lab/
│   └── county_court_issued_2000_2018.csv
├── civil_caseload/
│   └── civil_caseload_activity_reports.csv
└── permits/
    └── optional_permit_data.csv
    
All data used are publicly available and aggregate.

Running the Analysis
Launch Jupyter:
jupyter notebook

Run notebooks in order:
01_pitt_county_eviction_early_warning.ipynb
02_bay_county_disaster_segmentation.ipynb

Each notebook outputs cleaned datasets, risk scores, and visualizations.

Reproducibility
The framework is designed for monthly updates. New data can be appended to the input files and notebooks re-executed without code modification.
