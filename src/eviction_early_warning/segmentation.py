from __future__ import annotations

import pandas as pd


def assign_disaster_period(
    df: pd.DataFrame,
    year_col: str,
    disaster_start_year: int,
    disaster_end_year: int,
    out_col: str = "period",
) -> pd.DataFrame:
    """
    Assign pre_disaster, disaster_aftermath, and recovery periods.

    This is intentionally simple and transparent for policy and oversight use.
    """
    out = df.copy()
    y = out[year_col]

    out[out_col] = "recovery"
    out.loc[y < disaster_start_year, out_col] = "pre_disaster"
    out.loc[(y >= disaster_start_year) & (y <= disaster_end_year), out_col] = "disaster_aftermath"

    return out
