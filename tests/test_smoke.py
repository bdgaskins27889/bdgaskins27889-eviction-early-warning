import pandas as pd
from eviction_early_warning.scoring import score_pressure

def test_score_pressure_runs():
    df = pd.DataFrame({"filings": [1, 2, 3, 4, 5, 6]})
    out = score_pressure(df, "filings", baseline_window=3)
    assert "z_score" in out.columns
