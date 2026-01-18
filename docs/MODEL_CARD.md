# Model Card: Eviction Pressure Early Warning Score

## What this is
An interpretable county-level scoring framework that flags periods of elevated eviction pressure relative to local historical baselines.

## What this is NOT
- Not a tenant risk score
- Not a prediction of individual eviction outcomes
- Not a substitute for legal advice

## Inputs (examples)
- Court-issued eviction filings (county-level)
- Optional maintenance proxies (permits)
- Disaster segmentation for Bay County

## Output
A monthly "eviction pressure" score with transparent subcomponents.

## Risks & mitigation
- Risk: misuse for punitive targeting
  - Mitigation: aggregate-only design + privacy policy + no tenant data
- Risk: missingness / reporting gaps
  - Mitigation: documented limitations + sensitivity checks

## Evaluation
- Stability tests vs. baseline
- Back-testing across time periods
- Cross-county replication checks
