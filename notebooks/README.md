# Notebooks
Jupyter notebooks for the Eviction Early Warning project.
# Eviction Early Warning Notebooks

This folder contains the primary analytical notebooks for the **Eviction Early Warning Framework**, developed as an applied data science project focused on housing instability, disaster impact, and regulatory relevance.

The notebooks are designed to be **interpretable, reproducible, and policy-relevant**, rather than purely predictive.

---

## Notebook Overview

### 1. Pitt County Pilot  
**File:** `01_pitt_county_eviction_early_warning.ipynb`

**Purpose:**  
Establishes a baseline eviction early-warning signal using county-level eviction filings.

**Key Elements:**
- Monthly time-series structure
- Rolling baseline (mean and standard deviation)
- Z-score–based early warning indicator
- Emphasis on transparency and interpretability

**Use Case:**  
Demonstrates how local governments, housing advocates, or regulators could identify **emerging eviction pressure** before crisis thresholds are reached.

---

### 2. Bay County Disaster Segmentation  
**File:** `02_bay_county_disaster_segmentation.ipynb`

**Purpose:**  
Extends the early-warning framework by explicitly segmenting **pre-disaster**, **disaster/aftermath**, and **recovery** periods.

**Key Elements:**
- Disaster-period segmentation logic
- Comparative analysis across periods
- Application to Hurricane Michael (2018) as a case example

**Use Case:**  
Illustrates how eviction pressure behaves differently in disaster contexts and why **post-disaster housing enforcement and oversight** require distinct analytical treatment.

---

## Data Notes

- Current notebooks use **placeholder or example data** for structural demonstration.
- Final implementation replaces placeholders with:
  - County court eviction filings
  - Eviction Lab county-level data
  - Supplementary public indicators (permits, inspections, etc.)

No tenant-level or personally identifiable data is included in this repository.

---

## Reproducibility

These notebooks are intended to be:
- Run locally after cloning the repository, or
- Adapted by other researchers or agencies using their own county-level data

Future versions will modularize shared logic into the `src/` directory.

---

## Ethical Considerations

This work is designed as an **early-warning and oversight support tool**, not a punitive or automated enforcement system.

Interpretation should always be paired with:
- Human review
- Local legal context
- Tenant-protection safeguards

