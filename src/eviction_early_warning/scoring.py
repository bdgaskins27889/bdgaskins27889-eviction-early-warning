from __future__ import annotations
import pandas as pd

def score_pressure(df: pd.DataFrame, value_col: str, baseline_window: int = 12) -> pd.DataFrame:
    """
    Simple baseline scoring:
    - rolling mean / std
    - z-score for current value vs rolling baseline
    """
    out = df.copy()
    rolling_mean = out[value_col].rolling(baseline_window, min_periods=3).mean()
    rolling_std = out[value_col].rolling(baseline_window, min_periods=3).std()
    out["z_score"] = (out[value_col] - rolling_mean) / rolling_std
    return out
