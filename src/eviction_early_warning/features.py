from __future__ import annotations
import pandas as pd


def make_month_index(ev: pd.DataFrame, county_name: str) -> pd.DataFrame:
    """
    Convert Eviction Lab court-issued file into a county-month time series.
    This function assumes a column naming pattern but is defensive.

    Expected somewhere:
      - county name or FIPS
      - year
      - month
      - filings or court_issued
    """
    df = ev.copy()

    # Standardize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Filter county
    # Try name match first; otherwise user can adjust later to FIPS match.
    if "county" in df.columns:
        mask = df["county"].astype(str).str.lower().str.contains(county_name.lower())
        df = df.loc[mask].copy()

    # Identify year/month
    year_col = "year" if "year" in df.columns else None
    month_col = "month" if "month" in df.columns else None
    if year_col is None or month_col is None:
        raise ValueError("Eviction Lab file must contain 'year' and 'month' columns.")

    # Identify filings column
    filings_col = None
    for cand in ["filings", "court_issued", "eviction_filings", "eviction_filing_count"]:
        if cand in df.columns:
            filings_col = cand
            break
    if filings_col is None:
        # fallback: first numeric col besides year/month
        numeric_cols = [c for c in df.columns if c not in [year_col, month_col] and pd.api.types.is_numeric_dtype(df[c])]
        if not numeric_cols:
            raise ValueError("Could not identify filings column in Eviction Lab file.")
        filings_col = numeric_cols[0]

    df["month"] = pd.to_datetime(dict(year=df[year_col], month=df[month_col], day=1))
    out = df.groupby("month", as_index=False)[filings_col].sum()
    out = out.rename(columns={filings_col: "filings"})
    return out.sort_values("month")


def build_permit_features_monthly(elec: pd.DataFrame, bldg: pd.DataFrame) -> pd.DataFrame:
    """
    Build monthly permit count features from Pitt County permits.
    """
    def _prep(x: pd.DataFrame, label: str) -> pd.DataFrame:
        df = x.copy()
        df.columns = [c.strip().lower() for c in df.columns]
        # Find a date column
        date_col = None
        for cand in ["issued_date", "issue_date", "permit_date", "date", "applied_date"]:
            if cand in df.columns:
                date_col = cand
                break
        if date_col is None:
            # fallback: any column containing 'date'
            date_candidates = [c for c in df.columns if "date" in c]
            if not date_candidates:
                raise ValueError(f"Could not find date column for {label} permits.")
            date_col = date_candidates[0]

        df["month"] = pd.to_datetime(df[date_col], errors="coerce").dt.to_period("M").dt.to_timestamp()
        df = df.dropna(subset=["month"])
        out = df.groupby("month").size().reset_index(name=f"permits_{label}")
        return out

    elec_m = _prep(elec, "electrical")
    bldg_m = _prep(bldg, "building")

    merged = elec_m.merge(bldg_m, on="month", how="outer").fillna(0)
    merged["permits_total"] = merged["permits_electrical"] + merged["permits_building"]
    return merged.sort_values("month")


def merge_fmr_context(scored: pd.DataFrame, fmr: pd.DataFrame, county_name: str) -> pd.DataFrame:
    """
    Merge HUD FMR 2BR and compute YoY delta as a contextual affordability signal.
    """
    df = scored.copy()
    fx = fmr.copy()
    fx.columns = [c.strip().lower() for c in fx.columns]

    # Heuristic matching (can upgrade to FIPS later)
    if "countyname" in fx.columns:
        mask = fx["countyname"].astype(str).str.lower().str.contains(county_name.lower())
        fx = fx.loc[mask].copy()

    # Identify year + fmr
    if "year" not in fx.columns:
        # some files store as "fiscal year" etc.
        year_candidates = [c for c in fx.columns if "year" in c]
        if not year_candidates:
            return df
        fx = fx.rename(columns={year_candidates[0]: "year"})

    # Identify 2BR column
    fmr_col = None
    for cand in ["fmr_2br", "fmr2", "fmr2br", "fmr_2", "two_bedroom", "2br"]:
        if cand in fx.columns:
            fmr_col = cand
            break
    if fmr_col is None:
        # fallback numeric column
        numeric_cols = [c for c in fx.columns if pd.api.types.is_numeric_dtype(fx[c])]
        if numeric_cols:
            fmr_col = numeric_cols[0]
        else:
            return df

    fx = fx.groupby("year", as_index=False)[fmr_col].mean().rename(columns={fmr_col: "fmr_2br"})
    fx = fx.sort_values("year")
    fx["fmr_delta_yoy"] = fx["fmr_2br"].diff()

    # Expand yearly to months by merging on year
    df["year"] = pd.to_datetime(df["month"]).dt.year
    df = df.merge(fx[["year", "fmr_2br", "fmr_delta_yoy"]], on="year", how="left")
    df = df.drop(columns=["year"])
    return df
