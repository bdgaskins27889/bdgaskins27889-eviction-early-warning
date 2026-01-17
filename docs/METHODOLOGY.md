# Methodology

## Early Warning Score (Interpretability-first)
1. Standardize eviction filings relative to local baseline:
   z = (x - mean) / std

2. Optional: integrate lagged proxy indicators (e.g., permits):
   permits_lag_k = permits shifted by k months

3. Composite score:
   score = w1 * filings_z + w2 * permits_z

Weights are documented in `configs/config.yaml`.

## Replication
Replication holds parameters constant across jurisdictions to evaluate robustness.

## Disaster-period segmentation (optional)
For disaster-impacted counties, results may be summarized across:
- pre-disaster
- impact window
- recovery period
