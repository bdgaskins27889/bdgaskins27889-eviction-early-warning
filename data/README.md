# Data Folder (Not Committed)

This project uses public, aggregate datasets only.

## Folder meaning
- `data/external/` = raw downloaded public datasets (not committed)
- `data/processed/` = cleaned / feature tables (not committed)

## Sources used
1. Eviction Lab (county-level court-issued / proprietary where permitted)
2. County public records (e.g., permits) where available
3. Optional: HUD FMR (county-level rent benchmarks)

## How to fetch
This repo does not store raw downloads. Use the scripts documented in `scripts/run_monthly.py` or place files manually into:
- `data/external/`
