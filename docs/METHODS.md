
⚠️ If `docs/` doesn’t exist, GitHub will create it automatically.

---

## Step 2: Paste this entire Methods section

```markdown
# Methods

## Data Source

Eviction filing data were obtained from The Eviction Lab at Princeton University, using the publicly available county-level court-issued eviction filings dataset covering the period from 2000 through 2018. The dataset reports annual counts of eviction filings by county across the United States.

Only aggregate county-level data were used. No tenant-level or personally identifiable information was accessed or analyzed.

## Study Design

This study applies a transparent, policy-oriented early warning framework to detect elevated eviction pressure at the county level. Two counties were selected as comparative case studies:

- Pitt County, North Carolina, representing a non-disaster baseline jurisdiction
- Bay County, Florida, representing a disaster-impacted jurisdiction following Hurricane Michael in 2018

The design mirrors real-world regulatory and policy monitoring contexts where historical baselines are used to identify structural shifts in housing instability.

## Data Preparation

Data preparation consisted of the following steps:

1. Loading the Eviction Lab county court-issued eviction dataset
2. Filtering observations by county name and state
3. Sorting records chronologically by year
4. Retaining eviction filing counts as the primary outcome variable

No transformations or imputations were applied to the eviction filing counts.

## Analytical Framework

The analysis employs comparative temporal analysis rather than predictive modeling. For Pitt County, annual eviction filing trends were evaluated relative to historical baselines to assess persistence and variability in eviction pressure.

For Bay County, filings were segmented into pre-disaster and post-disaster periods, with 2018 used as the disaster demarcation point. Mean eviction filing levels were compared across periods to evaluate structural changes associated with disaster recovery.

## Rationale

This approach prioritizes interpretability, reproducibility, and policy relevance. The framework avoids black-box prediction models and instead emphasizes transparent signals suitable for regulatory review and public accountability. The methodology is intentionally designed to be replicable across jurisdictions with minimal technical infrastructure.
