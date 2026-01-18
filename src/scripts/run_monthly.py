from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

from eviction_early_warning.pipeline import PipelineConfig, run_pipeline


def save_outputs(df: pd.DataFrame, county: str, score_type: str) -> None:
    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{county}_{score_type}_scores.csv"
    df.to_csv(out_path, index=False)
    print(f"Saved: {out_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--county", choices=["pitt", "bay"], required=True)
    parser.add_argument("--enhanced", action="store_true", help="Compute enhanced score if data available")
    parser.add_argument("--disaster", action="store_true", help="Enable disaster segmentation logic (Bay)")
    args = parser.parse_args()

    cfg = PipelineConfig(
        county=args.county,
        external_dir=Path("data/external"),
        processed_dir=Path("data/processed"),
        use_enhanced=args.enhanced,
        disaster_segmentation=args.disaster,
    )

    df = run_pipeline(cfg)
    score_type = "enhanced" if args.enhanced else "core"
    save_outputs(df, args.county, score_type)

    print(df.tail(6))


if __name__ == "__main__":
    main()
