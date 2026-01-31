"""Configuration defaults for paths and parameters."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Paths:
    raw_data_dir: str = "data/raw"
    processed_data_dir: str = "data/processed"
    reports_dir: str = "reports"
