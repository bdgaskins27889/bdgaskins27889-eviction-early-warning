from __future__ import annotations
from pathlib import Path
import pandas as pd


def _read_any(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(path)
    raise ValueError(f"Unsupported file type: {path.suffix}")


def load_evictionlab_county_court_issued(external_dir: Path) -> pd.DataFrame:
    """
    User places Eviction Lab 'county_court-issued_2000_2018.csv' or equivalent into data/external/.
    """
    # Try common filenames
    candidates = [
        external_dir / "county_court-issued_2000_2018.csv",
        external_dir / "county_court_issued_2000_2018.csv",
        external_dir / "evictionlab_county_court_issued.csv",
    ]
    for c in candidates:
        if c.exists():
            return _read_any(c)

    raise FileNotFoundError(
        "Eviction Lab county court-issued file not found in data/external/. "
        "Place the CSV there (example: county_court-issued_2000_2018.csv)."
    )


def load_pitt_permits_electrical(external_dir: Path) -> pd.DataFrame:
    path = external_dir / "Pitt_County_Electrical_Permits.csv"
    return _read_any(path)


def load_pitt_permits_building(external_dir: Path) -> pd.DataFrame:
    path = external_dir / "Pitt_County_Building_Permits.csv"
    return _read_any(path)


def load_hud_fmr(external_dir: Path) -> pd.DataFrame:
    """
    Accepts either FY26_FMRs.xlsx or FMR2024_final_revised.xlsx
    """
    candidates = [
        external_dir / "FY26_FMRs.xlsx",
        external_dir / "FMR2024_final_revised.xlsx",
        external_dir / "hud_fmr.xlsx",
    ]
    for c in candidates:
        if c.exists():
            return _read_any(c)
    # not fatal, but pipeline expects it for enhanced
    raise FileNotFoundError(
        "HUD FMR file not found in data/external/. "
        "Place FY26_FMRs.xlsx or FMR2024_final_revised.xlsx there."
    )
