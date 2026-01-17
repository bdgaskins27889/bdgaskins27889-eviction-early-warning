from __future__ import annotations
import pandas as pd

def add_lag_features(df: pd.DataFrame, value_col: str, lags=(1, 3)) -> pd.DataFrame:
    """Add simple lag features for a numeric column."""
    out = df.copy()
    for lag in lags:
        out[f"{value_col}_lag_{lag}"] = out[value_col].shift(lag)
    return out
