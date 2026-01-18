# Reproducibility

## What this repo includes
- Public-data-compatible pipeline scaffold
- Notebooks for pilot and replication
- Documentation of methods and ethical guardrails

## What this repo excludes
- Tenant-level documents or personally identifiable information
- Raw datasets that are large or sensitive

## Recommended workflow
1. Download public datasets (Eviction Lab or court aggregate files)
2. Place them in `data/raw/` locally (not tracked by git)
3. Run notebooks or pipeline to generate outputs

# Reproducibility Checklist

## Environment
- Python version:
- OS tested:
- Key libraries:

## Data
- Data sources are public and linked
- No tenant-level or PII stored in repo
- Data download steps documented

## Pipeline
- Monthly re-run supported (planned scheduling)
- Outputs are generated deterministically where possible

## Ethics
- Aggregated data only
- No individual risk scoring published
- Clear disclaimer on limitations and intended use
