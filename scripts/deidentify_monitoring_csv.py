"""Create a de-identified monitoring CSV for public release.

Usage:
    python scripts/deidentify_monitoring_csv.py input.csv output.csv

This script removes or pseudonymizes common sensitive columns. Review the
output manually before uploading it to any public repository.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


DROP_COLUMNS = {
    "bridge_name",
    "bridge_id",
    "route_id",
    "latitude",
    "longitude",
    "gps_lat",
    "gps_lon",
    "camera_gps",
    "operator_name",
    "inspection_team",
    "exact_sensor_coordinate",
    "pier_coordinate",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_csv", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()

    df = pd.read_csv(args.input_csv)
    drop = [col for col in df.columns if col.lower() in DROP_COLUMNS]
    df = df.drop(columns=drop)

    if "sensor_id" in df.columns:
        mapping = {value: f"S{idx + 1:02d}" for idx, value in enumerate(sorted(df["sensor_id"].dropna().unique()))}
        df["sensor_id"] = df["sensor_id"].map(mapping).fillna(df["sensor_id"])

    if "timestamp" in df.columns:
        ts = pd.to_datetime(df["timestamp"], errors="coerce")
        if ts.notna().any():
            start = ts.min()
            df["day_index"] = ((ts - start).dt.total_seconds() / 86400).round(6)
            df = df.drop(columns=["timestamp"])

    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output_csv, index=False)
    print(f"Wrote de-identified candidate: {args.output_csv}")
    print("Manual review is still required before public release.")


if __name__ == "__main__":
    main()

