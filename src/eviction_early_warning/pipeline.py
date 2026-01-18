from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import pandas as pd

from .scoring import compute_core_score, compute_enhanced_score
from .io import (
    load_evictionlab_county_court_issued,
    load_pitt_permits_electrical,
    load_pitt_permits_building,
    load_hud_fmr,
)
from .features import (
    make_month_index,
    build_permit_features_monthly,
    merge_fmr_context,
)


@dataclass
class PipelineConfig:
    county: str  # "pitt" or "bay"
    data_dir: Path = Path("data")
    external_dir: Path = Path("data/external")
    processed_dir: Path = Path("data/processed")
    use_enhanced: bool = False
    disaster_segmentation: bool = False


def run_pipeline(cfg: PipelineConfig) -> pd.DataFrame:
    """
    Runs either CORE or ENHANCED scoring pipeline.

    Returns:
        dataframe with monthly score and components.
    """
    cfg.processed_dir.mkdir(parents=True, exist_ok=True)

    # --- CORE: eviction filings time series (county-month)
    ev = load_evictionlab_county_court_issued(cfg.external_dir)
    county_ts = make_month_index(ev, county_name=cfg.county)

    core = compute_core_score(county_ts)

    if not cfg.use_enhanced:
        out = core.copy()
        out["score_type"] = "core"
        return out

    # --- ENHANCED: add permits + FMR context where available
    enhanced = core.copy()

    if cfg.county == "pitt":
        elec = load_pitt_permits_electrical(cfg.external_dir)
        bldg = load_pitt_permits_building(cfg.external_dir)
        permit_feats = build_permit_features_monthly(elec, bldg)
        enhanced = enhanced.merge(permit_feats, on="month", how="left")

    fmr = load_hud_fmr(cfg.external_dir)
    enhanced = merge_fmr_context(enhanced, fmr, county_name=cfg.county)

    enhanced = compute_enhanced_score(enhanced)

    enhanced["score_type"] = "enhanced"
    return enhanced
