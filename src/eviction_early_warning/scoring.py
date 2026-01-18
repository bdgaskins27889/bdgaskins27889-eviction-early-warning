from __future__ import annotations
import pandas as pd
import numpy as np


def zscore(series: pd.Series, eps: float = 1e-9) -> pd.Series:
    mu = series.mean()
    sd = series.std(ddof=0)
    if sd < eps:
        return pd.Series(np.zeros(len(series)), index=series.index)
    return (series - mu) / sd


def rolling_zscore(series: pd.Series, window: int = 24, min_periods: int = 12) -> pd.Series:
    """
    Rolling z-score to flag abnormal pressure relative to local history.
    """
    roll_mean = series.rolling(window=window, min_periods=min_periods).mean()
    roll_std = series.rolling(window=window, min_periods=min_periods).std(ddof=0)
    return (series - roll_mean) / (roll_std.replace(0, np.nan))


def compute_core_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    CORE score uses eviction filings only.
    Expected columns:
      - month (datetime64[ns])
      - filings (numeric)
    """
    out = df.copy()
    out = out.sort_values("month").reset_index(drop=True)

    out["filings_rolling_z"] = rolling_zscore(out["filings"])
    out["filings_z_global"] = zscore(out["filings"])

    # Core score: scaled rolling z score (preferred) with fallback
    core_raw = out["filings_rolling_z"].fillna(out["filings_z_global"])
    out["core_score_raw"] = core_raw

    # Human-friendly 0-100 score
    # Map z ~ [-3, +3] into [0, 100] with clipping
    out["core_score_0_100"] = ((core_raw.clip(-3, 3) + 3) / 6) * 100

    return out[["month", "filings", "filings_rolling_z", "filings_z_global", "core_score_raw", "core_score_0_100"]]


def compute_enhanced_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    ENHANCED score blends CORE eviction pressure with optional maintenance proxies and rent context.

    Optional columns if available:
      - permits_total (monthly count)
      - permits_electrical (monthly count)
      - permits_building (monthly count)
      - fmr_2br (numeric)
      - fmr_delta_yoy (numeric)
    """
    out = df.copy()
    out = out.sort_values("month").reset_index(drop=True)

    # Start with core
    base = out["core_score_raw"]

    # Maintenance proxy (permits): rising permit activity can signal deferred maintenance, rehab, or instability
    if "permits_total" in out.columns:
        out["permits_total_z"] = rolling_zscore(out["permits_total"].fillna(0))
        base = base + 0.35 * out["permits_total_z"].fillna(0)

    # Rent context proxy (FMR): rising benchmarks may relate to affordability pressure
    if "fmr_delta_yoy" in out.columns:
        out["fmr_delta_yoy_z"] = rolling_zscore(out["fmr_delta_yoy"].fillna(0), window=24, min_periods=12)
        base = base + 0.25 * out["fmr_delta_yoy_z"].fillna(0)

    out["enhanced_score_raw"] = base
    out["enhanced_score_0_100"] = ((base.clip(-3, 3) + 3) / 6) * 100

    return out
