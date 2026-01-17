from __future__ import annotations
import pandas as pd

def assign_disaster_period(
    df: pd.DataFrame,
    year_col: str,
    disaster_start_year: int,
    disaster_end_year: int,
    out_col: str = "period",
) -> pd.DataFrame:
    out = df.copy()
    y = out[year_col]
    out[out_col] = "recovery"
    out.loc[y < disaster_start_year, out_col] = "pre_disaster"
    out.loc[(y >= disaster_start_year) & (y <= disaster_end_year), out_col] = "disaster_aftermath"
    return out
