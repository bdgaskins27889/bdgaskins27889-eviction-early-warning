[![Python CI](https://github.com/bdgaskins27889/bdgaskins27889-eviction-early-warning/actions/workflows/python-ci.yml/badge.svg)](https://github.com/bdgaskins27889/bdgaskins27889-eviction-early-warning/actions/workflows/python-ci.yml)
# Early Warning Framework for Eviction Pressure

## Overview
This repository contains an applied data science project that develops and evaluates an interpretable early warning framework for identifying periods of elevated eviction pressure using publicly available data. The goal is proactive monitoring that supports housing stability efforts while maintaining ethical restraint and transparency.

## Objectives
- Detect abnormal eviction pressure relative to local historical baselines
- Replicate the scoring framework across jurisdictions (Pitt County, NC and Bay County, FL pilots)
- Translate results into policy- and practitioner-facing deliverables

## Data Sources
Designed to work with:
- Public court-issued eviction filing data (county-level, where available)
- Eviction Lab county-level eviction filings
- Optional public maintenance proxies (e.g., permits) where available

**Privacy Note:** This repository does not contain tenant-level or personally identifiable information.

## Methods (High Level)
- Standardize eviction filings using z-scores relative to local baselines
- Construct an interpretable Early Warning Score
- Optionally integrate lagged maintenance indicators (permits) to improve lead time
- Replicate across counties without parameter tuning
- Optional disaster-period segmentation for recovery contexts

## Quickstart
### 1) Setup
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
